"""Fresh-development paired schema check and historical traceability."""
import json
from pathlib import Path
from benchmarks.operator_variety import PRIMER,GLOSS,score
from benchmarks.operator_schema_strict import SPEC
from benchmarks.operator_schema_paired import GENERIC
SOURCE=Path(__file__).resolve().parents[1]/"benchmarks/corpus/schema-replication-003.jsonl"
def build():
    docs=[json.loads(s) for s in SOURCE.read_text().splitlines() if s.strip()]
    if len(docs)!=8:raise ValueError("requires 8 documents")
    q=[];truth={}
    for i,doc in enumerate(docs):
        truth[doc["id"]]=doc["events"]
        order=("strict","generic") if i%2==0 else ("generic","strict")
        for condition in order:
            note=SPEC if condition=="strict" else GENERIC
            q.append({"id":doc["id"]+"_"+condition,"doc":doc["id"],"condition":condition,
                      "messages":[{"role":"user","content":PRIMER+"Dictionary: "+GLOSS+" "+note+
                      "\nClauses:\n"+"\n".join(doc["clauses"])}]})
    return q,truth
def summarize(rows,truth):
    results={}
    for kind in ("strict","generic"):
        group=[x for x in rows if x["condition"]==kind]
        reference=[{"id":r["id"],"events":truth[r["doc"]]} for r in group]
        data=score(reference,group)
        data["usage"]={k:sum((x.get("usage") or {}).get(k) or 0 for x in group) for k in ("prompt_tokens","completion_tokens","cost")}
        results[kind]=data
    return {"conditions":results,"status":"fresh_development_not_true_holdout","canonical_changes":False}
