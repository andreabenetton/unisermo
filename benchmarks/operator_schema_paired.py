"""Paired generic vs strict response schema on exactly the same eight documents."""
import json
from benchmarks.operator_schema_strict import build_strict,SOURCE
from benchmarks.operator_variety import PRIMER,GLOSS,score
GENERIC=('Return only JSON with an events array, one object per clause, in order. '
         'Each event must contain lemma, object_lemma, tense, aspect, person (integer), '
         'number, negative (boolean) and interrogative (boolean). ')
def build():
    docs=[json.loads(x) for x in SOURCE.read_text().splitlines() if x.strip()]
    strict,key=build_strict()
    pairs=[]
    for idx,doc in enumerate(docs):
        generic=PRIMER+"Dictionary: "+GLOSS+" "+GENERIC+"\nClauses:\n"+"\n".join(doc["clauses"])
        specific=strict[idx]["messages"][0]["content"]
        conditions=(("generic",generic),("strict",specific))
        if idx%2:conditions=tuple(reversed(conditions))
        for kind,prompt in conditions:
            pairs.append({"id":doc["id"]+"_"+kind,"doc":doc["id"],"condition":kind,
                          "messages":[{"role":"user","content":prompt}]})
    return pairs,{x["id"]:x["events"] for x in key}
def summarize(rows,answer_key):
    result={}
    for kind in ("generic","strict"):
        data=[x for x in rows if x["condition"]==kind]
        keys=[{"id":r["id"],"events":answer_key[r["doc"]]} for r in data]
        output=score(keys,data)
        output["usage"]={k:sum((r.get("usage") or {}).get(k) or 0 for r in data)
                         for k in ("prompt_tokens","completion_tokens","cost")}
        result[kind]=output
    return {"schema":"unisermo/paired-schema-comparison@1","conditions":result,
            "limitations":"Same documents are used in both arms; dataset was used in prior strict pilot and is development, not independent holdout."}
