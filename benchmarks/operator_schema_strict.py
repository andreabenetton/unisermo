"""Strict response-type primer for fresh clause combinations."""
import json
from pathlib import Path
from benchmarks.operator_variety import PRIMER,GLOSS,score
SOURCE=Path(__file__).resolve().parents[1]/"benchmarks/corpus/schema-variety-002.jsonl"
SPEC=('Response must be one JSON object {"events":[...]}. Each event must contain exactly: '
      '"lemma" string, "object_lemma" string, "tense" one of "present","past","future", '
      '"aspect" one of "simple","progressive", "person" integer 1,2,3, '
      '"number" string exactly "singular" or "plural" (NEVER numeric 1 or 2), '
      '"negative" JSON boolean and "interrogative" JSON boolean. '
      'Do not confuse person with grammatical number. ')
def build_strict():
    docs=[json.loads(line) for line in SOURCE.read_text().splitlines() if line.strip()]
    q=[];key=[]
    for d in docs:
        q.append({"id":d["id"],"messages":[{"role":"user","content":PRIMER+"Dictionary: "+GLOSS+" "+SPEC+
            "\nClauses:\n"+"\n".join(d["clauses"])}]})
        key.append({"id":d["id"],"events":d["events"]})
    if len(q)!=8:raise ValueError("unexpected corpus size")
    return q,key
