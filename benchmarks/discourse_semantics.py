"""Semantic-slot evaluation for small controlled Unisermo clause documents.

Only explicit verb, object, tense, and person slots are measured; no claims
about idiomatic translation, pragmatics, or human comprehensibility.
"""
from __future__ import annotations
import json
from pathlib import Path
SOURCE=Path(__file__).resolve().parents[1]/"benchmarks/corpus/discourse-001.jsonl"
def build():
    docs=[json.loads(x) for x in SOURCE.read_text().splitlines() if x.strip()]
    questions=[];keys=[]
    for doc in docs:
        text=("Read these experimental Unisermo clauses. Subject i=first singular, "
              "u=second singular. Each verb is a root followed by tense "
              "(present=none, past=d) and person (i=first, u=second); "
              "the object suffix is -em. Dictionary: "
              +", ".join(k+"="+v for k,v in sorted(doc["root_glossary"].items()))
              +". Return only JSON with an 'events' array, in clause order. "
              "Each event must have 'verb' (the Unisermo root), 'object' "
              "(the Unisermo noun root), 'tense' (present/past), "
              "and 'person' (integer 1/2).\nClauses:\n"
              +"\n".join(doc["clauses"]))
        questions.append({"id":doc["id"],"messages":[{"role":"user","content":text}]})
        keys.append({"id":doc["id"],"events":doc["expected_events"]})
    return questions,keys
def parse(answer):
    if not isinstance(answer,str):return None
    raw=answer.strip()
    fence=chr(96)*3
    if raw.startswith(fence):
        lines=raw.splitlines()
        if len(lines)>=3 and lines[0] in (fence,fence+"json") and lines[-1]==fence:
            raw="\n".join(lines[1:-1])
    try:result=json.loads(raw)
    except (ValueError,TypeError):return None
    return result.get("events") if isinstance(result,dict) and isinstance(result.get("events"),list) else None
def score(key,responses):
    found={r["id"]:r for r in responses}
    if len(found)!=len(responses) or set(found)!={k["id"] for k in key}:raise ValueError("incomplete or duplicated answers")
    correct=0;total=0;documents=[]
    for item in key:
        actual=parse(found[item["id"]]["answer"])
        hits=0
        for i,event in enumerate(item["events"]):
            hits+=int(isinstance(actual,list) and len(actual)>i and isinstance(actual[i],dict)
                and all(actual[i].get(k)==v for k,v in event.items()))
            total+=1
        correct+=hits
        documents.append({"id":item["id"],"correct_events":hits,"total_events":len(item["events"]),
                          "well_formed":actual is not None})
    return {"schema":"unisermo/discourse-semantic-slots@1",
            "correct_events":correct,"total_events":total,"documents":documents,
            "limits":"Checks exact structured slots in controlled clauses only; not free translation quality."}
