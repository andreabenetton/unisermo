"""Paired replication: short rule+examples vs verbose instruction, new pro-drop clauses."""
import json
from pathlib import Path
from benchmarks.discourse_tense_clarification import EXPLICIT
from benchmarks.discourse_tense_ablation import PARTS
from benchmarks.discourse_semantics import score
SOURCE=Path(__file__).resolve().parents[1]/"benchmarks/corpus/tense-replication-002.jsonl"
SHORT=PARTS["zero"]+PARTS["examples"]
GLOSS="aerplan=airplane, akwa=water, frat=brother, pel=push, trak=pull, vid=see"
BASE=("Read experimental Unisermo clauses. The subject pronoun is omitted; infer person from the ending. "
      "The object suffix is -em. Dictionary: "+GLOSS+
      ". Return only JSON with an 'events' array, in clause order. "
      "Each event must have 'verb' (root), 'object' (noun root), 'tense' (present/past), "
      "and 'person' (integer 1/2).\nClauses:\n")
def build():
    docs=[json.loads(x) for x in SOURCE.read_text().splitlines() if x.strip()]
    if len(docs)!=6:raise ValueError("six new documents required")
    prompts=[];truth={}
    for j,doc in enumerate(docs):
        if len(doc["clauses"])!=3 or doc["canonical_changes"] is not False:raise ValueError("invalid source")
        truth[doc["id"]]=doc["expected_events"]
        # Counterbalance presentation order across documents; complete answers before the next document.
        order=("short","full") if j%2==0 else ("full","short")
        for variant in order:
            prompt=(SHORT if variant=="short" else EXPLICIT)+BASE+"\n".join(doc["clauses"])
            prompts.append({"id":doc["id"]+"_"+variant,"doc":doc["id"],"variant":variant,
                            "messages":[{"role":"user","content":prompt}]})
    return prompts,truth
def report(rows,truth):
    groups={}
    for variant in ("short","full"):
        subset=[r for r in rows if r["variant"]==variant]
        key=[{"id":r["id"],"events":truth[r["doc"]]} for r in subset]
        scored=score(key,subset)
        usage={field:sum((r.get("usage") or {}).get(field) or 0 for r in subset)
               for field in ("prompt_tokens","completion_tokens","cost")}
        groups[variant]={"correct_events":scored["correct_events"],"total_events":scored["total_events"],
                         "documents":scored["documents"],"usage":usage}
    return {"schema":"unisermo/tense-replication@1","conditions":groups,
            "limits":"Novel development clauses are pro-drop transformations of known root/object/tense patterns, not independent naturalistic prose. Exact slot scoring only."}
