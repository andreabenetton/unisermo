"""Complete a cross-family evaluation by retaining the original valid Qwen
run and finishing 24 Gemma3 calls, reusing 7 already paid Gemma replies.

The initial 48-call experiment was INTERRUPTED: 429 from Gemma and empty
Qwen completions when its model-specific /no_think control was removed.
Never present that failed run as a successful controlled comparison.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import time

from benchmarks.case_role_decoding import CORPUS, evaluate, load_corpus, requests
from benchmarks.two_model_case_role import (
    MODELS, PROVIDER, RetryableRateLimit, invoke_same_prompt, plan
)

ROOT=Path(__file__).resolve().parents[1]
QWEN_RAW=ROOT/"benchmarks/evidence/case-role-2026-10-24-run40090842899.jsonl"
FAILED_RUN=40091590850
QWEN_RUN=40090842899
MAX_GEMMA_REQUESTS=24
MAX_OBSERVED_GEMMA_USD=0.02


def jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf8").splitlines() if line.strip()]


def gemma_plan():
    q=[item for item in plan() if item["model_label"]=="gemma"]
    if len(q)!=MAX_GEMMA_REQUESTS or len({x["id"] for x in q})!=24:
        raise ValueError("invalid or duplicate Gemma request plan")
    return q


def restore_prefix(rows):
    """Read only successful Gemma replies from the exact original run."""
    gemma=[dict(row) for row in rows if row.get("model_label")=="gemma"]
    qs=gemma_plan()
    if len(gemma)!=7:
        raise ValueError("expected the original seven successful Gemma calls")
    for i,(reply,request) in enumerate(zip(gemma,qs)):
        if any(reply.get(k)!=request[k] for k in
               ("id","doc","condition","model_label","requested_model","prompt_sha256")):
            raise ValueError("original completed Gemma answer differs from frozen prompt")
        if (reply.get("provider")!=PROVIDER or
            reply.get("returned_model")!=MODELS["gemma"] or
            reply.get("finish_reason")!="stop"):
            raise ValueError("original Gemma reply/provider not normally completed")
        reply["original_call_order"]=reply["call_order"]
        reply["call_order"]=i+1
        reply["original_run"]=FAILED_RUN
    return gemma


def analyze(qwen,gemma):
    base=requests(load_corpus())
    ids={q["id"]:q for q in base}
    def validate(rows,model):
        if len(rows)!=24 or {r.get("id") for r in rows}!=set(ids):
            raise ValueError("incomplete / duplicate model data")
        for r in rows:
            q=ids[r["id"]]
            if any(r.get(k)!=q[k] for k in ("doc","condition","prompt_sha256")):
                raise ValueError("base task changed between models")
            if r.get("returned_model")!=model or r.get("finish_reason")!="stop":
                raise ValueError("model identity or incomplete output")
            if r.get("provider")!=PROVIDER:
                raise ValueError("inference provider mismatch")
        return evaluate(rows,load_corpus())
    q_result=validate(qwen,MODELS["qwen"])
    g_result=validate(gemma,MODELS["gemma"])
    condition_agreement={}
    family_accuracy={}
    for cond in ("case","role"):
        qa={(r["doc"],r["event"]):r for r in q_result["comparisons"][cond]["details"]}
        ga={(r["doc"],r["event"]):r for r in g_result["comparisons"][cond]["details"]}
        if set(qa)!=set(ga):
            raise ValueError("nonaligned model observations")
        matrix=Counter()
        for key in qa:
            a,b=qa[key]["exact"],ga[key]["exact"]
            matrix["both_correct" if a and b else
                   "qwen_only" if a else
                   "gemma_only" if b else
                   "both_wrong"]+=1
        condition_agreement[cond]=dict(matrix)
        family_accuracy[cond]={
            family:{
                "qwen":sum(bool(r["exact"]) for r in qa.values() if r["family"]==family),
                "gemma":sum(bool(r["exact"]) for r in ga.values() if r["family"]==family)
            }
            for family in ("move","transition","cause_result")
        }
    return {
        "schema":"unisermo/qwen-gemma-case-role-followup@1",
        "status":"development_comparison_amended_after_failed_paired_trial",
        "models":{"qwen":MODELS["qwen"],"gemma":MODELS["gemma"]},
        "provenance":{
            "qwen_successful_original_run":QWEN_RUN,
            "gemma_original_partial_run":FAILED_RUN,
            "gemma_reused_billed_prefix":7,
            "prompt_content_note":"Both received same case-role question and grammar guide. Qwen original runner appended /no_think to disable hidden reasoning; Gemma runner did not. Therefore effective input strings were NOT strictly byte-identical. Qwen originally used auto routing, but returned DeepInfra on all calls; Gemma was pinned to DeepInfra.",
        },
        "source_corpus":str(CORPUS.relative_to(ROOT)),
        "comparisons":{
            "qwen":q_result["comparisons"],
            "gemma":g_result["comparisons"]
        },
        "agreement_by_condition":condition_agreement,
        "correct_by_family":family_accuracy,
        "limitations":"This is an exploratory cross-model follow-up, NOT the initially preregistered identical-prompt experiment which failed. Same task and parse-derived gold; model-specific Qwen nonthinking control changes literal effective prompt. Corpus and semantic keys are development-only and unreviewed by an independent human; do not claim linguistic superiority."
    }


def checked_resume_rows(rows, original):
    """Refuse resume unless an exact valid ordered prefix of the same model plan."""
    questions=gemma_plan()
    if not 7 <= len(rows) < len(questions):
        raise ValueError("resume must have 7-23 saved Gemma replies")
    previous=restore_prefix(original)
    for i,(row,q) in enumerate(zip(rows,questions)):
        if row.get("call_order")!=i+1:
            raise ValueError("noncontiguous Gemma resume prefix")
        for k in ("id","doc","condition","model_label","requested_model","prompt_sha256"):
            if row.get(k)!=q[k]:
                raise ValueError(f"Gemma resume prompt/order drift at position {i+1}: {k}")
        if (row.get("provider")!=PROVIDER or row.get("returned_model")!=MODELS["gemma"]
            or row.get("finish_reason")!="stop"):
            raise ValueError("saved response not a valid completed Gemma answer")
        cost=(row.get("usage") or {}).get("cost")
        if type(cost) not in (float,int) or not 0<=cost<MAX_OBSERVED_GEMMA_USD:
            raise ValueError("invalid billed cost in resumed file")
        if i<len(previous):
            keys=("id","doc","condition","model_label","requested_model","prompt_sha256","answer","response_id","provider","finish_reason","usage")
            if any(row.get(k)!=previous[i].get(k) for k in keys):
                raise ValueError("reused original seven replies changed")
    return rows


def run(prefix_path,output,key,resume=False):
    if not key:
        raise ValueError("OPENROUTER_API_KEY missing")
    if output.with_suffix(".score.json").exists():
        raise ValueError("refuse overwrite of existing complete score")
    qwen=jsonl(QWEN_RAW)
    original=jsonl(prefix_path)
    if resume:
        if not output.exists():
            raise ValueError("resume file missing")
        gemma=checked_resume_rows(jsonl(output),original)
    else:
        if output.exists():
            raise ValueError("refuse overwrite")
        gemma=restore_prefix(original)
    q=gemma_plan()
    output.parent.mkdir(parents=True,exist_ok=True)
    spent=sum(x["usage"]["cost"] for x in gemma)
    if spent>=MAX_OBSERVED_GEMMA_USD:
        raise ValueError("previous observations already exhausted spend guard")
    with output.open("a" if resume else "x",encoding="utf8") as f:
        if not resume:
            for row in gemma:
                f.write(json.dumps(row,ensure_ascii=False)+"\n")
            f.flush()
        for question in q[len(gemma):]:
            for attempt in range(6):
                try:
                    result=invoke_same_prompt(key,question)
                    break
                except RetryableRateLimit:
                    if attempt==5:
                        raise
                    delay=(60,90,120,180,240)[attempt]
                    print(f"Gemma 429; waiting {delay}s",flush=True)
                    time.sleep(delay)
            result["call_order"]=len(gemma)+1
            result["original_run"]=None
            gemma.append(result)
            f.write(json.dumps(result,ensure_ascii=False)+"\n")
            f.flush()
            cost=result["usage"].get("cost")
            if type(cost) not in (float,int) or not 0<=cost<=MAX_OBSERVED_GEMMA_USD:
                raise RuntimeError("Gemma provider cost unknown")
            spent+=cost
            print(f"Gemma {len(gemma)}/24; USD {spent:.8f}",flush=True)
            if spent>=MAX_OBSERVED_GEMMA_USD:
                raise RuntimeError("observed Gemma USD limit reached")
            time.sleep(3)
    result=analyze(qwen,gemma)
    result["observed_gemma_usd"]=spent
    result["gemma_sha256"]=hashlib.sha256(output.read_bytes()).hexdigest()
    result["prior_qwen_sha256"]=hashlib.sha256(QWEN_RAW.read_bytes()).hexdigest()
    result["corpus_sha256"]=hashlib.sha256(CORPUS.read_bytes()).hexdigest()
    result["original_failed_prefix_sha256"]=hashlib.sha256(prefix_path.read_bytes()).hexdigest()
    output.with_suffix(".score.json").write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf8")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--prefix",required=True,type=Path,help="unmodified original partial 48-run JSONL")
    p.add_argument("--output",required=True,type=Path)
    p.add_argument("--resume",action="store_true",help="resume checked Gemma-only JSONL prefix")
    a=p.parse_args()
    run(a.prefix,a.output,os.environ.get("OPENROUTER_API_KEY",""),resume=a.resume)
