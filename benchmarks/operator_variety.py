"""Evaluate seven exact slots on previously untested operator/aspect documents."""
import json
from pathlib import Path
from benchmarks.discourse_semantics import parse

def parse_event_array(answer):
    """Accept a pure JSON array or an events wrapper; never scrape prose."""
    parsed=parse(answer)
    if parsed is not None:return parsed
    if not isinstance(answer,str):return None
    raw=answer.strip()
    fence=chr(96)*3
    if raw.startswith(fence):
        lines=raw.splitlines()
        if len(lines)>=3 and lines[0] in (fence,fence+"json") and lines[-1]==fence:
            raw=chr(10).join(lines[1:-1])
    try:obj=json.loads(raw)
    except (ValueError,TypeError):return None
    return obj if isinstance(obj,list) else None
SOURCE=Path(__file__).resolve().parents[1]/"benchmarks/corpus/operator-variety-001.jsonl"
GLOSS="pel=push, trak=pull, vid=see; akwa=water, frat=brother, aerplan=airplane."
PRIMER=("Finite verb = root + aspect + tense + person + number. "
        "Aspect: simple=zero, progressive=e. Tense: present=zero, past=d, future=f. "
        "Person: first=i, second=u, third=a; plural=n, singular=zero. "
        "Example: peli=pel+present+1st singular; peldu=pel+past+2nd singular; "
        "pelfa=pel+future+3rd singular; pelein=pel+progressive+present+1st plural. "
        "no means negation; ka at start means yes/no question. "
        "The noun accusative suffix -em marks the object. ")
def build():
    docs=[json.loads(x) for x in SOURCE.read_text().splitlines() if x.strip()]
    q=[];key=[]
    for doc in docs:
        instruction=(PRIMER+"Dictionary: "+GLOSS+
            " Return only JSON with an events array, one object per clause, in order. "
            "Each event must contain lemma, object_lemma, tense, aspect, person (integer), "
            "number, negative (boolean) and interrogative (boolean).\nClauses:\n"+
            "\n".join(doc["clauses"]))
        q.append({"id":doc["id"],"messages":[{"role":"user","content":instruction}]})
        key.append({"id":doc["id"],"events":doc["events"]})
    if len(q)!=8:raise ValueError("expected eight documents")
    return q,key
FIELDS=("lemma","object_lemma","tense","aspect","person","number","negative","interrogative")
def score(key,responses):
    found={x["id"]:x for x in responses}
    if set(found)!={x["id"] for x in key} or len(found)!=len(responses):raise ValueError("incomplete answers")
    by_field={field:{"correct":0,"total":0} for field in FIELDS}
    exact=0;total=0;details=[]
    for truth in key:
        actual=parse_event_array(found[truth["id"]].get("answer"))
        hits=0
        for i,event in enumerate(truth["events"]):
            candidate=actual[i] if isinstance(actual,list) and i<len(actual) and isinstance(actual[i],dict) else {}
            one=all(candidate.get(f)==event[f] for f in FIELDS)
            hits+=int(one);exact+=int(one);total+=1
            for field in FIELDS:
                by_field[field]["correct"]+=int(candidate.get(field)==event[field])
                by_field[field]["total"]+=1
        details.append({"id":truth["id"],"exact":hits,"total":len(truth["events"]),"valid_json":actual is not None})
    return {"schema":"unisermo/structural-slots-v2","exact_events":exact,"total_events":total,
            "field_scores":by_field,"documents":details,
            "limitations":"Parser-verified grammatical features only, not semantic translation or natural discourse."}
