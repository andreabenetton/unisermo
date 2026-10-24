"""Two-model controlled replication of case-vs-role development prompts.

Runs Qwen3-32B and Gemma3-27B on EXACTLY the same user prompt strings
from the frozen case-vs-role study. Both are served by a single provider,
temperature, and maximum completion length where supported; model-specific
reasoning disabling is a documented routing control. Do not use the holdout.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path
import time
import urllib.error
import urllib.request

from benchmarks.case_role_decoding import (
    CALL_CAP as QUESTIONS, CONDITIONS, CORPUS, evaluate,
    load_corpus, requests,
)

ROOT=Path(__file__).resolve().parents[1]
ENDPOINT="https://openrouter.ai/api/v1/chat/completions"
MODELS={"qwen":"qwen/qwen3-32b", "gemma":"google/gemma-3-27b-it"}
PROVIDER="DeepInfra"
MAX_REQUESTS=48
MAX_OUTPUT_TOKENS=340
MAX_OBSERVED_SPEND_USD=0.03
TEMPERATURE=0.7
SEED=23


class RetryableRateLimit(Exception):
    pass


def plan():
    """Each document receives four calls, balanced by model order."""
    corpus=load_corpus()
    base=requests(corpus)
    lookup={(q["doc"],q["condition"]):q for q in base}
    if len(lookup)!=QUESTIONS or len(corpus)!=12:
        raise ValueError("unexpected frozen question plan")
    ordered=[]
    for index, row in enumerate(corpus):
        for condition in CONDITIONS if index % 2==0 else CONDITIONS[::-1]:
            pair=lookup[(row["id"],condition)]
            labels=list(MODELS) if index % 2==0 else list(reversed(MODELS))
            for label in labels:
                ordered.append({
                    "id":pair["id"],"doc":pair["doc"],"condition":condition,
                    "messages":[dict(x) for x in pair["messages"]],
                    "prompt_sha256":pair["prompt_sha256"],"model_label":label,
                    "requested_model":MODELS[label],
                })
    if len(ordered)!=MAX_REQUESTS or len({(q["id"],q["model_label"]) for q in ordered})!=MAX_REQUESTS:
        raise ValueError("missing or duplicate experiment arms")
    grouped=defaultdict(list)
    for q in ordered:
        grouped[q["id"]].append(q)
    if any(len(pair)!=2 or pair[0]["messages"]!=pair[1]["messages"] or
           pair[0]["prompt_sha256"]!=pair[1]["prompt_sha256"] for pair in grouped.values()):
        raise ValueError("within-pair prompt content drift")
    return ordered


def invoke_same_prompt(key, question):
    """Identical prompt/temperature/seed/provider selection across models."""
    model=question["requested_model"]
    payload={
        "model":model, "messages":question["messages"],
        "temperature":TEMPERATURE, "seed":SEED,
        "max_tokens":MAX_OUTPUT_TOKENS, "stream":False,
        "provider":{
            "only":[PROVIDER], "order":[PROVIDER],
            "allow_fallbacks":False,"data_collection":"deny",
        },
    }
    # Qwen has optional explicit non-thinking mode; the prompt text is
    # deliberately NOT suffixed with /no_think, unlike earlier Qwen runs.
    # Gemma has no corresponding requested reasoning switch.
    if question["model_label"]=="qwen":
        payload["reasoning"]={"enabled":False}
    req=urllib.request.Request(
        ENDPOINT,method="POST",
        data=json.dumps(payload).encode("utf8"),
        headers={
            "Authorization":"Bearer "+key,
            "Content-Type":"application/json",
            "HTTP-Referer":"https://github.com/andreabenetton/unisermo",
            "X-OpenRouter-Title":"Unisermo two-model semantic test",
        }
    )
    try:
        with urllib.request.urlopen(req,timeout=90) as res:
            data=json.load(res)
    except urllib.error.HTTPError as err:
        if err.code==429:
            raise RetryableRateLimit("HTTP 429 for "+question["id"]+" model "+model) from None
        raise RuntimeError("OpenRouter HTTP "+str(err.code)+" for "+question["id"]+" model "+model) from None
    candidates=data.get("choices") or []
    if len(candidates)!=1:
        raise RuntimeError("unexpected number of model choices")
    choice=candidates[0]
    usage=data.get("usage") or {}
    message=choice.get("message") or {}
    return {
        "id":question["id"],"doc":question["doc"],
        "condition":question["condition"],"model_label":question["model_label"],
        "requested_model":model,
        "prompt_sha256":question["prompt_sha256"],
        "response_id":data.get("id"),
        "returned_model":data.get("model"),
        "provider":data.get("provider"),
        "finish_reason":choice.get("finish_reason"),
        "answer":message.get("content") if isinstance(message.get("content"),str) else "",
        "usage":{k:usage.get(k) for k in ("prompt_tokens","completion_tokens","total_tokens","cost")},
        "controls":{"temperature_requested":TEMPERATURE,"seed_requested":SEED,
                    "max_output_tokens":MAX_OUTPUT_TOKENS,"reasoning_disabled_requested":question["model_label"]=="qwen",
                    "inline_no_think_suffix":False,"provider_requested":PROVIDER},
    }


def compare(rows, corpus=None):
    corpus=corpus if corpus is not None else load_corpus()
    expected={(q["id"],q["model_label"]):q for q in plan()}
    seen={}
    for row in rows:
        key=(row.get("id"),row.get("model_label"))
        if key not in expected or key in seen:
            raise ValueError("foreign / duplicate model response")
        want=expected[key]
        if any(row.get(k)!=want[k] for k in ("doc","condition","prompt_sha256","requested_model")):
            raise ValueError("prompt/model mismatch")
        seen[key]=row
    if len(rows)!=MAX_REQUESTS or len(seen)!=MAX_REQUESTS:
        raise ValueError("experiment incomplete: no partial scoring")
    by_model={}
    for label,model in MODELS.items():
        subset=[seen[(q["id"],label)] for q in requests(corpus)]
        result=evaluate(subset,corpus)
        by_model[label]={
            "requested_model":model,
            "conditions":result["comparisons"],
            "document_pairing":result["document_pairing"],
            "returned_models":dict(Counter(r["returned_model"] for r in subset)),
            "providers":dict(Counter(r["provider"] for r in subset)),
            "finish_reasons":dict(Counter(r["finish_reason"] for r in subset)),
        }
    agreements={}
    for cond in CONDITIONS:
        qwen={(d["doc"],d["event"]):bool(d["exact"])
              for d in by_model["qwen"]["conditions"][cond]["details"]}
        gemma={(d["doc"],d["event"]):bool(d["exact"])
              for d in by_model["gemma"]["conditions"][cond]["details"]}
        if set(qwen)!=set(gemma) or len(qwen)!=24:
            raise ValueError("nonaligned model scoring")
        agreement=Counter()
        for key in qwen:
            a,b=qwen[key],gemma[key]
            agreement["both_correct" if a and b else
                      "qwen_only" if a else
                      "gemma_only" if b else
                      "both_incorrect"]+=1
        agreements[cond]=dict(agreement)
    by_family={}
    for cond in CONDITIONS:
        by_family[cond]={}
        for family in ("move","transition","cause_result"):
            by_family[cond][family]={
                label:sum(bool(d["exact"]) for d in by_model[label]["conditions"][cond]["details"]
                          if d["family"]==family)
                for label in MODELS
            }
    return {
        "schema":"unisermo/two-model-case-role@1",
        "status":"development_not_heldout_human_semantic_review_pending",
        "requested_models":MODELS,
        "questions":QUESTIONS, "billable_responses":MAX_REQUESTS,
        "same_prompt_text_within_model_pairs":True,
        "model_results":by_model, "exact_event_agreement":agreements,
        "correct_by_family":by_family,
        "limitations":"Two open models from distinct families, one inference provider. Model-specific handling of reasoning controls may differ; common temperature/seed are requests, not a guarantee of identical sampling. Familiar generated-development clauses and parser-derived labels, no human-reviewed semantic gold. Exact-match JSON compliance remains part of outcome. Not an English or real-discourse language-efficiency benchmark."
    }


def run(output,key):
    if not key:
        raise ValueError("OPENROUTER_API_KEY missing")
    if output.exists() or output.with_suffix(".score.json").exists():
        raise ValueError("refuse overwrite evidence")
    questions=plan()
    output.parent.mkdir(parents=True,exist_ok=True)
    rows,spent=[],0.0
    with output.open("x",encoding="utf8") as f:
        for q in questions:
            for attempt in range(3):
                try:
                    r=invoke_same_prompt(key,q)
                    break
                except RetryableRateLimit:
                    if attempt==2:
                        raise
                    time.sleep((10,30)[attempt])
            r["call_order"]=len(rows)+1
            rows.append(r)
            f.write(json.dumps(r,ensure_ascii=False)+"\n")
            f.flush()
            cost=(r["usage"] or {}).get("cost")
            if type(cost) not in (int,float) or not 0 <= cost <= MAX_OBSERVED_SPEND_USD:
                raise RuntimeError("unknown or invalid provider cost: stop calling")
            spent+=cost
            print(f"{len(rows)}/{MAX_REQUESTS} calls; observed USD {spent:.8f}",flush=True)
            if spent >= MAX_OBSERVED_SPEND_USD:
                raise RuntimeError("observed-spend limit reached")
            time.sleep(0.5)
    score=compare(rows)
    score["observed_usd"]=spent
    score["response_sha256"]=hashlib.sha256(output.read_bytes()).hexdigest()
    score["corpus_sha256"]=hashlib.sha256(CORPUS.read_bytes()).hexdigest()
    score["control_parameters"]={
        "requested_temperature":TEMPERATURE,"requested_seed":SEED,
        "provider_only":PROVIDER,"provider_fallbacks":False,
        "no_inline_no_think_suffix":True,
        "qwen_reasoning_disabled_requested":True,
        "max_output_tokens_per_call":MAX_OUTPUT_TOKENS,
        "max_calls":MAX_REQUESTS,
        "observed_spend_guard_usd":MAX_OBSERVED_SPEND_USD,
    }
    output.with_suffix(".score.json").write_text(
        json.dumps(score,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
    print("completed and scored",flush=True)


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    run(args.output,os.environ.get("OPENROUTER_API_KEY",""))
