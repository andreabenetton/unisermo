"""Two additional model families for the Unisermo case/role development study.

Run Mistral Small 3.2 24B and OpenAI gpt-oss-20b on exactly the frozen
case/role question strings already used with Qwen3 and Gemma3.
This is an exploratory expansion of PR #16, NOT a holdout assessment.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import time
import urllib.error
import urllib.request

from benchmarks.case_role_decoding import CORPUS, evaluate, load_corpus, requests
from benchmarks.two_model_case_role import PROVIDER

ROOT=Path(__file__).resolve().parents[1]
ENDPOINT="https://openrouter.ai/api/v1/chat/completions"
MODELS={
    "mistral":"mistralai/mistral-small-3.2-24b-instruct",
    "gpt_oss":"openai/gpt-oss-20b",
}
CONDITIONS=("case","role")
MAX_CALLS=48
MAX_OUTPUT=1000
MAX_OBSERVED_SPEND_USD=0.03


class RetryableError(Exception):
    pass


def planned():
    baseline=requests(load_corpus())
    result=[]
    for idx,question in enumerate(baseline):
        order=("mistral","gpt_oss") if idx%2==0 else ("gpt_oss","mistral")
        for label in order:
            result.append({
                "id":question["id"],"doc":question["doc"],
                "condition":question["condition"],"prompt_sha256":question["prompt_sha256"],
                "messages":question["messages"],"model_label":label,
                "requested_model":MODELS[label],
            })
    if len(result)!=MAX_CALLS or len({(q["id"],q["model_label"]) for q in result})!=MAX_CALLS:
        raise ValueError("invalid 48-call model plan")
    for i in range(0,len(result),2):
        a,b=result[i:i+2]
        if (a["id"]!=b["id"] or a["prompt_sha256"]!=b["prompt_sha256"] or
            a["messages"]!=b["messages"] or a["model_label"]==b["model_label"]):
            raise ValueError("model pairing drift")
    return result


def invoke(key,question):
    payload={
        "model":question["requested_model"],
        "messages":question["messages"],
        "temperature":0.7,
        "seed":23,
        "max_tokens":MAX_OUTPUT,
        "stream":False,
        "provider":{"only":[PROVIDER],"order":[PROVIDER],"allow_fallbacks":False,
                    "data_collection":"deny"},
    }
    # gpt-oss is a reasoning model. Request low reasoning rather than silently
    # equating its token budget with a non-reasoning model's visible output.
    if question["model_label"]=="gpt_oss":
        payload["reasoning"]={"effort":"low"}
    request=urllib.request.Request(ENDPOINT,method="POST",
        data=json.dumps(payload).encode("utf8"),headers={
            "Authorization":"Bearer "+key,"Content-Type":"application/json",
            "HTTP-Referer":"https://github.com/andreabenetton/unisermo",
            "X-OpenRouter-Title":"Unisermo additional-model case-role study"})
    try:
        with urllib.request.urlopen(request,timeout=100) as answer:
            data=json.load(answer)
    except urllib.error.HTTPError as e:
        if e.code in (429,502,503,504):
            raise RetryableError(f"provider HTTP {e.code}") from None
        raise RuntimeError(f"request for {question['requested_model']} failed HTTP {e.code}") from None
    choices=data.get("choices") or []
    if len(choices)!=1:
        raise RuntimeError("expected one completion")
    message=choices[0].get("message") or {}
    usage=data.get("usage") or {}
    return {
        **{k:question[k] for k in ("id","doc","condition","model_label",
                                   "requested_model","prompt_sha256")},
        "returned_model":data.get("model"),
        "provider":data.get("provider"),
        "response_id":data.get("id"),
        "answer":message.get("content") if isinstance(message.get("content"),str) else "",
        "finish_reason":choices[0].get("finish_reason"),
        "usage":{k:usage.get(k) for k in ("prompt_tokens","completion_tokens",
                                         "total_tokens","cost")},
        "controls":{"requested_temperature":0.7,"requested_seed":23,
                    "max_output_tokens":MAX_OUTPUT,"provider_only":PROVIDER,
                    "gpt_oss_reasoning_effort":"low" if question["model_label"]=="gpt_oss" else None},
    }


def checked_prefix(rows):
    q=planned()
    if len(rows)>len(q):
        raise ValueError("too many responses")
    for i,row in enumerate(rows):
        expected=q[i]
        if row.get("call_order")!=i+1:
            raise ValueError("response order mismatch")
        if any(row.get(k)!=expected[k] for k in
               ("id","doc","condition","model_label","requested_model","prompt_sha256")):
            raise ValueError("response does not match planned model prompt")
        if row.get("returned_model")!=expected["requested_model"] or row.get("provider")!=PROVIDER:
            raise ValueError("response model/provider did not match requested model")
        cost=(row.get("usage") or {}).get("cost")
        if type(cost) not in (float,int) or cost<0:
            raise ValueError("missing observed provider cost")
    return q


def compare(rows):
    plan=checked_prefix(rows)
    if len(rows)!=MAX_CALLS:
        raise ValueError("incomplete responses: never score partial work")
    baseline=requests(load_corpus())
    result={}
    for label in MODELS:
        subset=[next(row for row in rows if row["id"]==q["id"] and row["model_label"]==label)
                for q in baseline]
        score=evaluate(subset,load_corpus())
        result[label]={
            "model":MODELS[label],
            "scores":score["comparisons"],
            "providers":dict(Counter(r["provider"] for r in subset)),
            "finish_reasons":dict(Counter(r["finish_reason"] for r in subset)),
            "returned_models":dict(Counter(r["returned_model"] for r in subset)),
        }
    agreement={}
    for condition in CONDITIONS:
        x={(d["doc"],d["event"]):d["exact"] for d in result["mistral"]["scores"][condition]["details"]}
        y={(d["doc"],d["event"]):d["exact"] for d in result["gpt_oss"]["scores"][condition]["details"]}
        if set(x)!=set(y):
            raise ValueError("unaligned paired events")
        counts=Counter()
        for key in x:
            counts["both_correct" if x[key] and y[key] else
                   "mistral_only" if x[key] else
                   "gpt_oss_only" if y[key] else "both_wrong"]+=1
        agreement[condition]=dict(counts)
    return {
        "schema":"unisermo/four-model-case-role-addendum@1",
        "status":"development_extra_two_models_unreviewed_semantics",
        "new_model_results":result,
        "new_model_agreement":agreement,
        "previous_model_results_are_separate":"See Qwen run 40090842899 and Gemma verified final in PR16",
        "limits":"No human-validated gold; familiar templates; gpt-oss has explicit reasoning effort unlike Mistral. A four-model exploratory comparison is not a controlled language-efficiency benchmark.",
    }


def run(path,key,resume=False):
    if not key:
        raise ValueError("OPENROUTER_API_KEY missing")
    score_path=path.with_suffix(".score.json")
    if score_path.exists():
        raise ValueError("do not overwrite scored research output")
    path.parent.mkdir(parents=True,exist_ok=True)
    if resume:
        if not path.exists():
            raise ValueError("resume needs original partial JSONL")
        records=[json.loads(s) for s in path.read_text().splitlines() if s.strip()]
        if not records or len(records)==MAX_CALLS:
            raise ValueError("resume requires nonempty incomplete file")
    else:
        if path.exists():
            raise ValueError("refuse overwrite existing original evidence")
        records=[]
    questions=checked_prefix(records)
    spent=sum(x["usage"]["cost"] for x in records)
    if spent>=MAX_OBSERVED_SPEND_USD:
        raise ValueError("previous observed spend reached bound")
    with path.open("a" if resume else "x",encoding="utf8") as file:
        for question in questions[len(records):]:
            for attempt in range(4):
                try:
                    reply=invoke(key,question)
                    break
                except RetryableError:
                    if attempt==3:
                        raise
                    time.sleep([30,60,90][attempt])
            reply["call_order"]=len(records)+1
            records.append(reply)
            file.write(json.dumps(reply,ensure_ascii=False)+"\n")
            file.flush()
            cost=reply["usage"]["cost"]
            if type(cost) not in (int,float) or not 0<=cost<=MAX_OBSERVED_SPEND_USD:
                raise RuntimeError("unknown provider billed cost; stop immediately")
            spent+=cost
            print(f"{len(records)}/48 model calls; observed USD {spent:.7f}",flush=True)
            if spent>=MAX_OBSERVED_SPEND_USD:
                raise RuntimeError("observed provider budget cutoff")
            time.sleep(2)
    scored=compare(records)
    scored["observed_usd"]=spent
    scored["raw_sha256"]=hashlib.sha256(path.read_bytes()).hexdigest()
    scored["corpus_sha256"]=hashlib.sha256(CORPUS.read_bytes()).hexdigest()
    score_path.write_text(json.dumps(scored,indent=2,ensure_ascii=False)+"\n",encoding="utf8")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",required=True,type=Path)
    p.add_argument("--resume",action="store_true")
    args=p.parse_args()
    run(args.output,os.environ.get("OPENROUTER_API_KEY"),args.resume)
