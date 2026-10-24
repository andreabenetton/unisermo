"""Development-only Qwen decoding of canonical relational frames.

Machine gold: source-linked, fail-closed relational parser. Never a substitute
for independent human semantic review. No holdout or language modifications.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import time

from formalization.core import Unisermo
from formalization.semantics.relational_frames import parse_relational_frame
from benchmarks.openrouter_runner import MODELS, RateLimited, invoke

ROOT=Path(__file__).resolve().parents[1]
CORPUS=ROOT/"benchmarks/corpus/relational-frames-dev-001.jsonl"
MODEL=MODELS["qwen"]
CONDITIONS=("cold","guided")
MAX_CALLS=24
MAX_OUTPUT=650
OBSERVED_BUDGET_USD=0.02
FIELDS=("frame","subject","subject_role","predicate","patient","destination",
        "source_state","result_state","tense","aspect","person","number")
FAMILIES={"move":4,"transition":4,"cause_result":4}
GUIDE=(
    "Reference: Unisermo finite verb is ROOT + aspect marker "
    "e(progressive)/o(perfect)/none(simple) + tense d(past)/f(future)/"
    "none(present) + person vowel i(1)/u(2)/a(3) + plural n. "
    "i=I, u=you singular, in=we, un=you plural. "
    "mov=move/transport, traes=transition/transform. "
    "Nominal case -em=direct object, -ad=destination/toward, "
    "-de=source/from, -da=resulting predicate of a transformed object. "
    "Licensed frames: SUBJECT mov PATIENT-em DESTINATION-ad "
    "(subject agent); SUBJECT traes DESTINATION-ad SOURCE-de "
    "(subject is transition theme, not a separate causer); "
    "SUBJECT traes PATIENT-em RESULT-da (subject causes transformation). "
    "Do not confuse allative -ad with transformative -da. "
    "akwa=water, dom=house, uman=person, aerplan=airplane, "
    "solid=solid, likwid=liquid, doktor=doctor, student=student. "
    "Use null for absent semantic arguments; do not invent any "
    "causal/discourse relation between the two independent clauses."
)
INSTRUCTION=(
    "Read the following two independent Unisermo propositions. "
    "Return exactly one JSON object with key events (array of 2 objects "
    "in sentence order). Each event MUST have exactly these 12 fields: "
    'frame (move_transitive_to/transition_between_states/cause_result), '
    "subject (i/u/in/un/uman/akwa), "
    "subject_role (agent/theme/causer), predicate (mov/traes), "
    "patient (null/akwa/dom/uman/aerplan), "
    "destination (null/dom/uman), "
    "source_state (null/likwid/student), "
    "result_state (null/solid/doktor), "
    "tense (present/past/future), aspect (simple/progressive/perfect), "
    "person (integer 1/2/3), number (singular/plural). "
    "JSON null is required for absent roles. No extra keys or prose."
)


def normalize(sentence, lang):
    parsed=parse_relational_frame(sentence,lang)
    roles=parsed["roles"]
    subject=parsed["subject"]
    if subject["kind"]=="pronoun":
        subj_form=subject["form"]
    elif subject["kind"]=="noun_phrase" and not subject["modifiers"]:
        subj_form=subject["lemma"]
    else:
        raise ValueError("outside bare subject corpus")
    if parsed["predicate"]["lemma"] not in ("mov","traes"):
        raise ValueError("unsupported extended lemma for this experiment")
    for role in roles.values():
        if role["modifiers"]:
            raise ValueError("no modifiers in this first relational benchmark")
    return {
        "frame":parsed["frame"],"subject":subj_form,
        "subject_role":parsed["subject_role"],
        "predicate":parsed["predicate"]["lemma"],
        "patient":roles.get("patient",{}).get("lemma"),
        "destination":roles.get("destination",roles.get("destination_state",{})).get("lemma"),
        "source_state":roles.get("source_state",{}).get("lemma"),
        "result_state":roles.get("result_state",{}).get("lemma"),
        "tense":parsed["predicate"]["tense"],
        "aspect":parsed["predicate"]["aspect"],
        "person":parsed["predicate"]["person"],
        "number":parsed["predicate"]["number"],
    }


def load_corpus(path=CORPUS):
    rows=[json.loads(line) for line in path.read_text(encoding="utf8").splitlines() if line.strip()]
    if len(rows)!=12 or len({r["id"] for r in rows})!=12:
        raise ValueError("exactly twelve distinct development documents required")
    if Counter(r["family"] for r in rows)!=FAMILIES:
        raise ValueError("unbalanced frame families")
    if len(set(s for r in rows for s in r["clauses"]))!=24:
        raise ValueError("expected 24 different clauses")
    lang=Unisermo()
    for row in rows:
        if (row["split"]!="development_only" or row["canonical_changes"] is not False
            or row["review_status"]!="machine_parsed_pending_independent_human_review"
            or row["anaphora"]!="none_intended" or row["adverbials"]!="none"):
            raise ValueError("holdout/human annotation integrity failed")
        if len(row["clauses"])!=2 or not all((ROOT/p).exists() for p in row["source_paths"]):
            raise ValueError("source or document issue")
        for clause in row["clauses"]:
            m=normalize(clause,lang)
            match={"move":"move_transitive_to","transition":"transition_between_states",
                   "cause_result":"cause_result"}[row["family"]]
            if m["frame"]!=match:
                raise ValueError("frame family mismatch")
    return rows


def requests(corpus=None):
    rows=corpus if corpus is not None else load_corpus()
    out=[]
    for i,row in enumerate(rows):
        order=CONDITIONS if i%2==0 else tuple(reversed(CONDITIONS))
        for condition in order:
            body=((GUIDE+"\n") if condition=="guided" else "")+INSTRUCTION+\
                 "\nUnisermo:\n"+"\n".join(row["clauses"])
            out.append({
                "id":row["id"]+"_"+condition,"doc":row["id"],"condition":condition,
                "prompt_sha256":hashlib.sha256(body.encode("utf8")).hexdigest(),
                "messages":[{"role":"user","content":body}]
            })
    if len(out)!=MAX_CALLS or len({x["id"] for x in out})!=MAX_CALLS:
        raise ValueError("incorrect call plan")
    return out


def decode(raw):
    if not isinstance(raw,str):
        return None,"missing_answer"
    raw=raw.strip()
    if raw.startswith("```"):
        lines=raw.splitlines()
        if len(lines)<3 or lines[0] not in ("```","```json") or lines[-1]!="```":
            return None,"invalid_fence"
        raw="\n".join(lines[1:-1])
    try:
        obj=json.loads(raw)
    except ValueError:
        return None,"invalid_json"
    if not isinstance(obj,dict) or set(obj)!={"events"} or not isinstance(obj["events"],list):
        return None,"incorrect_envelope"
    if len(obj["events"])!=2:
        return None,"cardinality"
    return obj["events"],None


def score(responses,corpus=None):
    corpus=corpus if corpus is not None else load_corpus()
    planned={q["id"]:q for q in requests(corpus)}
    actual={}
    for r in responses:
        ident=r.get("id")
        if ident not in planned or ident in actual:
            raise ValueError("unexpected or duplicate response")
        q=planned[ident]
        if any(r.get(field)!=q[field] for field in ("doc","condition","prompt_sha256")):
            raise ValueError("result metadata/hash conflict")
        actual[ident]=r
    if len(actual)!=MAX_CALLS:
        raise ValueError("incomplete; partial runs are not scored")
    lang=Unisermo()
    results={}
    for condition in CONDITIONS:
        details=[]
        errors=Counter()
        format_errors=Counter()
        count=0
        for row in corpus:
            expected=[normalize(s,lang) for s in row["clauses"]]
            observed,error=decode(actual[row["id"]+"_"+condition].get("answer"))
            if error:
                format_errors[error]+=1
            parts=[]
            for index,want in enumerate(expected):
                got=(observed[index] if error is None and isinstance(observed[index],dict) else {})
                wrong=[field for field in FIELDS
                       if field not in got or type(got[field]) is not type(want[field])
                       or got[field]!=want[field]]
                if set(got)-set(FIELDS):
                    wrong.append("extra_keys")
                for field in wrong:
                    errors[field]+=1
                ok=(not wrong and error is None)
                count+=int(ok)
                parts.append({"index":index,"correct":ok,"wrong_fields":wrong})
            details.append({"doc":row["id"],"family":row["family"],
                            "events":parts,"format_error":error})
        selected=[actual[q["id"]] for q in planned.values() if q["condition"]==condition]
        usage={}
        for field in ("prompt_tokens","completion_tokens","total_tokens","cost"):
            vals=[(r.get("usage") or {}).get(field) for r in selected]
            usage[field]=(sum(vals) if all(type(x) in (int,float) and x>=0 for x in vals)
                          else None)
        results[condition]={
            "exact_propositions":count,"total_propositions":24,
            "field_error_counts":dict(errors),
            "format_errors":dict(format_errors),"documents":details,
            "usage":usage,
            "cost_per_exact_proposition":(usage["cost"]/count
                if count and usage["cost"] is not None else None)
        }
    return {
        "schema":"unisermo/relational-frame-meaning@1",
        "status":"development_machine_gold_unreviewed",
        "calls":len(responses),"model_requested":MODEL,
        "comparisons":results,
        "limitations":"Case-frame mapping from deterministic parser; person/theme role interpretation provisional. No human approval, no locative finite predication, no referential discourse, no English baseline."
    }


def run(path,secret):
    if not secret:
        raise ValueError("OPENROUTER_API_KEY missing")
    if path.exists() or path.with_suffix(".score.json").exists():
        raise ValueError("refuse overwrite")
    corpus=load_corpus()
    qs=requests(corpus)
    path.parent.mkdir(parents=True,exist_ok=True)
    rows=[];spent=0.0
    with path.open("x",encoding="utf8") as store:
        for q in qs:
            for attempt in range(3):
                try:
                    response=invoke(secret,MODEL,q,None,max_output=MAX_OUTPUT)
                    break
                except RateLimited:
                    if attempt==2: raise
                    time.sleep([8,25][attempt])
            response.update({field:q[field] for field in ("doc","condition","prompt_sha256")})
            response["call_order"]=len(rows)+1
            rows.append(response)
            store.write(json.dumps(response,ensure_ascii=False)+"\n")
            store.flush()
            cost=(response.get("usage") or {}).get("cost")
            if type(cost) not in (int,float) or not 0<=cost<=OBSERVED_BUDGET_USD:
                raise RuntimeError("missing/invalid provider cost; halt")
            spent+=cost
            print(f"{len(rows)}/{MAX_CALLS} responses USD {spent:.8f}",flush=True)
            if spent>=OBSERVED_BUDGET_USD:
                raise RuntimeError("observed budget cutoff; stop")
            time.sleep(.7)
    result=score(rows,corpus)
    result["observed_cost_usd"]=spent
    result["corpus_sha256"]=hashlib.sha256(CORPUS.read_bytes()).hexdigest()
    result["raw_sha256"]=hashlib.sha256(path.read_bytes()).hexdigest()
    result["controls"]={"temperature":0.7,"seed":23,"no_think":True,
                        "provider_fallbacks":False,"max_output_tokens":MAX_OUTPUT,
                        "max_requests":MAX_CALLS,"observed_budget_usd":OBSERVED_BUDGET_USD}
    path.with_suffix(".score.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf8")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    run(args.output,os.environ.get("OPENROUTER_API_KEY"))
