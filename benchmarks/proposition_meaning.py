"""Narrow, executable Unisermo proposition-meaning benchmark.

This maps only the ALREADY IMPLEMENTED SVO parser subset into a controlled
meaning representation. It is *not* a general language/discourse parser.
English action labels and gold events are mechanical research annotations,
not independently human-reviewed semantic gold.
"""
from __future__ import annotations

from collections import Counter, defaultdict
import argparse
import hashlib
import json
import os
from pathlib import Path
import time

from formalization.core import Unisermo
from benchmarks.openrouter_runner import MODELS, RateLimited, invoke

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "benchmarks/corpus/proposition-dev-001.jsonl"
MODEL = MODELS["qwen"]
CONDITIONS = ("cold", "guided")
MAX_REQUESTS = 24
MAX_OUTPUT = 520
MAX_OBSERVED_COST_USD = 0.02

# Restricted lexical and reference equivalences, used only for research scoring.
# Bare nominal number is NOT assigned an arbitrary singular interpretation.
ACTION = {"vid": "see", "pel": "push", "trak": "pull", "mov": "move"}
NOMINAL = {"dom": "house", "akwa": "water", "aerplan": "airplane",
           "uman": "person", "frat": "brother"}
PRONOUN_AGENT = {"i": "speaker", "u": "listener", "in": "speaker_group",
                 "un": "listener_group"}
DEIXIS = {"tik": "speaker_near", "tes": "listener_near", "tan": "far"}
QUANTITY = {"wi": "explicit_plural", "bis": "two", "ter": "three",
            "omni": "all_members", "nul": "zero", "multi": "many"}
FIELDS = ("action", "agent", "agent_number", "patient", "patient_quantity",
          "patient_deixis", "tense", "aspect", "polarity", "speech_act")
ALLOWED_AGENT = set(PRONOUN_AGENT.values()) | {"person"}
GUIDE = (
    "Unisermo compact decoding reference: SVO subject-verb-object. "
    "Verb=lexical root + aspect e progressive/o perfect or zero simple + "
    "time d past/f future or zero present + person i first/u second/a third "
    "+ optional plural n. i=speaker, u=listener, in=we/speaker group, "
    "un=you plural/listener group. A subject noun without wi is number-neutral "
    "but the finite verb indicates grammatical agent number. "
    "-em on the object noun signals patient. "
    "vid=see, pel=push, trak=pull, mov=move; "
    "dom=house, akwa=water, aerplan=airplane, uman=person, frat=brother. "
    "Nominal modifier wi=explicit plural, bis=two, ter=three, "
    "omni=all members (scope/distributivity unspecified), nul=zero, "
    "multi=many. Bare object noun=quantity unspecified. "
    "tik=near speaker, tes=near listener, tan=far from both. "
    "Free no before verb negates; initial ka marks yes/no question. "
    "Pel and trak indicate force, not proof of completed displacement."
)

OUTPUT_SCHEMA = (
    "Return ONLY one JSON object with key events, an array in sentence order. "
    "Each of its two objects MUST have exactly these ten keys: "
    'action (see/push/pull/move), agent (speaker/listener/speaker_group/'
    "listener_group/person), agent_number (singular/plural), "
    "patient (house/water/airplane/person/brother), "
    "patient_quantity (unspecified/explicit_plural/two/three/all_members/zero/many), "
    "patient_deixis (none/speaker_near/listener_near/far), "
    "tense (present/past/future), aspect (simple/progressive/perfect), "
    "polarity (positive/negative), speech_act (statement/polar_question). "
    "Never infer referential links between sentences, or invent definiteness "
    "or collective/distributive scope. No prose or additional keys."
)


def meaning(sentence, lang):
    """Reject all clauses outside a deliberately declared canonical subset."""
    parsed = lang.parse_sentence(sentence)
    verb = parsed["predicate"]
    if verb["lemma"] not in ACTION or parsed["object"] is None:
        raise ValueError("not a licensed transitive meaning frame")
    sub = parsed["subject"]
    if sub["kind"] == "pronoun":
        agent = PRONOUN_AGENT.get(sub["form"])
        if agent is None:
            raise ValueError("unresolved third-person referent")
    elif sub["kind"] == "noun_phrase" and sub["lemma"] == "uman":
        agent = "person"
        # wi signals overt nominal plurality; verbal plural must agree.
        if ("wi" in sub["modifiers"]) != (verb["number"] == "plural"):
            raise ValueError("explicit subject noun plurality and finite number inconsistent")
        if sub["modifiers"] not in ([], ["wi"]):
            raise ValueError("unmodeled subject modifier")
    else:
        raise ValueError("pro-drop or nominal agent outside this benchmark")
    obj = parsed["object"]
    lemma = NOMINAL.get(obj["lemma"])
    if lemma is None:
        raise ValueError("unmodeled patient nominal")
    quantity = "unspecified"
    deixis = "none"
    for m in obj["modifiers"]:
        if m in QUANTITY:
            if quantity != "unspecified":
                raise ValueError("multiple quantity modifiers")
            quantity = QUANTITY[m]
        elif m in DEIXIS:
            if deixis != "none":
                raise ValueError("multiple deictics")
            deixis = DEIXIS[m]
        else:
            raise ValueError("unmodeled nominal modifier")
    return {
        "action": ACTION[verb["lemma"]], "agent": agent,
        "agent_number": verb["number"], "patient": lemma,
        "patient_quantity": quantity, "patient_deixis": deixis,
        "tense": verb["tense"], "aspect": verb["aspect"],
        "polarity": "negative" if parsed["negative"] else "positive",
        "speech_act": "polar_question" if parsed["interrogative"] else "statement",
    }


def load_corpus(path=CORPUS):
    rows = [json.loads(line) for line in path.read_text(encoding="utf8").splitlines()
            if line.strip()]
    if len(rows) != 12 or len({r["id"] for r in rows}) != 12:
        raise ValueError("must have 12 unique development documents")
    if len({clause for r in rows for clause in r["clauses"]}) != 24:
        raise ValueError("must have 24 distinct complete statements")
    lang = Unisermo()
    for row in rows:
        if (row["split"] != "development_only_exposed_after_run"
            or row["canonical_changes"] is not False
            or row["discourse_coreference"] != "not_asserted"
            or "pending_human_review" not in row["review_status"]):
            raise ValueError("holdout/semantic review integrity failure")
        if len(row["clauses"]) != 2:
            raise ValueError("two propositions per document")
        if not row["source_paths"] or not all((ROOT / p).exists() for p in row["source_paths"]):
            raise ValueError("missing source provenance")
        for clause in row["clauses"]:
            meaning(clause, lang)
    return rows


def build_questions(corpus=None):
    corpus = corpus if corpus is not None else load_corpus()
    out = []
    for i, row in enumerate(corpus):
        order = CONDITIONS if i % 2 == 0 else tuple(reversed(CONDITIONS))
        for condition in order:
            text = ((GUIDE + "\n" if condition == "guided" else "") +
                    OUTPUT_SCHEMA + "\nUnisermo text:\n" +
                    "\n".join(row["clauses"]))
            out.append({
                "id":row["id"] + "_" + condition,
                "doc":row["id"], "condition":condition,
                "messages":[{"role":"user","content":text}],
                "prompt_sha256":hashlib.sha256(text.encode("utf8")).hexdigest(),
            })
    if len(out) != MAX_REQUESTS or len({x["id"] for x in out}) != MAX_REQUESTS:
        raise ValueError("invalid request count")
    return out


def decode(raw):
    if not isinstance(raw,str):
        return None, "not_string"
    s=raw.strip()
    if s.startswith("```"):
        lines=s.splitlines()
        if len(lines)<3 or lines[0] not in ("```","```json") or lines[-1]!="```":
            return None,"invalid_fence"
        s="\n".join(lines[1:-1])
    try:
        obj=json.loads(s)
    except ValueError:
        return None,"invalid_json"
    if not isinstance(obj,dict) or set(obj)!={"events"} or not isinstance(obj["events"],list):
        return None,"invalid_wrapper"
    if len(obj["events"])!=2:
        return None,"wrong_cardinality"
    return obj["events"],None


def score(responses, corpus=None):
    corpus = corpus if corpus is not None else load_corpus()
    expected_q = {q["id"]:q for q in build_questions(corpus)}
    actual = {}
    for row in responses:
        ident=row.get("id")
        if ident not in expected_q or ident in actual:
            raise ValueError("foreign or duplicate answer")
        req=expected_q[ident]
        if any(row.get(k)!=req[k] for k in ("doc","condition","prompt_sha256")):
            raise ValueError("mismatched condition/document/prompt hash")
        actual[ident]=row
    if len(actual)!=MAX_REQUESTS:
        raise ValueError("incomplete; never score partial paid results")
    lang=Unisermo()
    outputs={}
    documents=[]
    for condition in CONDITIONS:
        exact = 0
        fields = {k:{"correct":0,"total":0} for k in FIELDS}
        details=[]
        total_usage={}
        subset=[actual[r["id"]+"_"+condition] for r in corpus]
        for k in ("prompt_tokens","completion_tokens","total_tokens","cost"):
            v=[(r.get("usage") or {}).get(k) for r in subset]
            total_usage[k]=sum(v) if all(type(x) in (float,int) and x>=0 for x in v) else None
        for row in corpus:
            gold=[meaning(c,lang) for c in row["clauses"]]
            result=actual[row["id"]+"_"+condition]
            events,error=decode(result.get("answer"))
            successes=0
            event_report=[]
            for i,want in enumerate(gold):
                got=events[i] if error is None and isinstance(events[i],dict) else {}
                mismatch=[]
                for k in FIELDS:
                    fields[k]["total"]+=1
                    if k in got and type(got[k]) is type(want[k]) and got[k]==want[k]:
                        fields[k]["correct"]+=1
                    else:
                        mismatch.append(k)
                # Unexpected event keys invalidate the entire proposition.
                extra=sorted(set(got)-set(FIELDS))
                if extra:
                    mismatch+=["extra_keys"]
                correct=not mismatch and error is None
                successes+=int(correct)
                exact+=int(correct)
                event_report.append({"event_index":i,"correct":correct,
                                     "wrong_fields":mismatch})
            details.append({"doc":row["id"],"stratum":row["stratum"],
                            "correct_events":successes,"total_events":2,
                            "decode_error":error,"events":event_report})
        outputs[condition]={
            "exact_propositions":exact,"total_propositions":24,
            "accuracy":exact/24,"fields":fields,"documents":details,
            "usage":total_usage,
            "usd_per_exact_proposition":total_usage["cost"]/exact
                if exact and total_usage["cost"] is not None else None
        }
    paired=[]
    for row in corpus:
        a=next(r["correct_events"] for r in outputs["cold"]["documents"] if r["doc"]==row["id"])
        b=next(r["correct_events"] for r in outputs["guided"]["documents"] if r["doc"]==row["id"])
        paired.append({"doc":row["id"],"stratum":row["stratum"],"cold":a,"guided":b,"delta_guided_minus_cold":b-a})
    return {
        "schema":"unisermo/proposition-meaning-dev@1",
        "status":"development_parser_derived_unreviewed",
        "unit_of_analysis":"two-proposition_document",
        "requested_model":MODEL,"documents":12,"calls":MAX_REQUESTS,
        "conditions":outputs,"paired_documents":paired,
        "limitations":"Controlled SVO agent/patient lexical/grammatical interpretation only. Gold is produced from restricted parser; source words include example-only entries. No independent semantic review, no cross-clause anaphora/scope, no full language competence, no English baseline."
    }


def run(output, secret):
    if not secret:
        raise ValueError("OPENROUTER_API_KEY missing")
    if output.exists() or output.with_suffix(".score.json").exists():
        raise ValueError("refuse to overwrite experiment evidence")
    corpus=load_corpus()
    requests=build_questions(corpus)
    output.parent.mkdir(parents=True,exist_ok=True)
    rows,spent=[],0.0
    with output.open("x",encoding="utf8") as fp:
        for q in requests:
            for attempt in range(3):
                try:
                    response=invoke(secret,MODEL,q,None,max_output=MAX_OUTPUT)
                    break
                except RateLimited:
                    if attempt==2:
                        raise
                    time.sleep((8,25)[attempt])
            response.update({k:q[k] for k in ("doc","condition","prompt_sha256")})
            response["call_order"]=len(rows)+1
            rows.append(response)
            fp.write(json.dumps(response,ensure_ascii=False)+"\n")
            fp.flush()
            cost=(response.get("usage") or {}).get("cost")
            if type(cost) not in (float,int) or not 0<=cost<=MAX_OBSERVED_COST_USD:
                raise RuntimeError("invalid cost; no more paid requests")
            spent+=cost
            print(f"{len(rows)}/{MAX_REQUESTS} billed calls; USD {spent:.8f}",flush=True)
            if spent>=MAX_OBSERVED_COST_USD:
                raise RuntimeError("observed-spend guard exceeded")
            time.sleep(.8)
    summary=score(rows,corpus)
    summary["corpus_sha256"]=hashlib.sha256(CORPUS.read_bytes()).hexdigest()
    summary["responses_sha256"]=hashlib.sha256(output.read_bytes()).hexdigest()
    summary["observed_cost_usd"]=spent
    summary["request_controls"]={"temperature":0.7,"seed":23,"no_think":True,
            "provider_fallbacks":False,"max_output":MAX_OUTPUT,"max_requests":MAX_REQUESTS,
            "observed_spend_limit_usd":MAX_OBSERVED_COST_USD}
    output.with_suffix(".score.json").write_text(
        json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf8")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",required=True,type=Path)
    args=parser.parse_args()
    run(args.output,os.environ.get("OPENROUTER_API_KEY"))
