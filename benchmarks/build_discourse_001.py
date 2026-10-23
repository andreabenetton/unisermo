"""Build controlled multi-clause comprehension cases, with independent answer keys.

These are syntactically verified experimental clause bundles, not idiomatic
Unisermo narratives or validated translations.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"benchmarks/corpus/expansion-001.jsonl"
OUT=ROOT/"benchmarks/corpus/discourse-001.jsonl"
VERBS={"vid":"see","pel":"push","trak":"pull"}
NOUNS={"akwa":"water","frat":"brother","aerplan":"airplane"}
def build():
    src=[json.loads(x) for x in SOURCE.read_text().splitlines() if x.strip()]
    selected=[]
    # Paired contrast cases compare three actions on the same object and
    # grammatical features; no optimization on any earlier holdout.
    for noun in ("akwa","frat","aerplan"):
        for tense in ("present","past"):
            matches=[x for x in src if x["grammatical_intent"]["object_lemma"]==noun
                and x["grammatical_intent"]["tense"]==tense
                and x["grammatical_intent"]["aspect"]=="simple"
                and x["subgroup"]=="subject"]
            matches=sorted(matches,key=lambda x:x["grammatical_intent"]["lemma"])
            if len(matches)!=3:raise ValueError("unexpected source coverage")
            selected.append({
                "id":f"D{len(selected)+1:03d}",
                "clauses":[x["unisermo"] for x in matches],
                "source_ids":[x["id"] for x in matches],
                "root_glossary":{**VERBS,**NOUNS},
                "expected_events":[{
                    "verb":x["grammatical_intent"]["lemma"],
                    "object":x["grammatical_intent"]["object_lemma"],
                    "tense":x["grammatical_intent"]["tense"],
                    "person":x["grammatical_intent"]["person"],
                } for x in matches],
                "split":"development",
                "status":"structurally_verified_semantics_unreviewed",
                "canonical_changes":False,
            })
    if len(selected)!=6 or len({tuple(x["clauses"]) for x in selected})!=6:
        raise ValueError("invalid discourse pack")
    return selected
def main():
    import argparse
    p=argparse.ArgumentParser();p.add_argument("--check",action="store_true");a=p.parse_args()
    content="".join(json.dumps(x,sort_keys=True,ensure_ascii=False)+"\n" for x in build())
    if a.check:
        if not OUT.exists() or OUT.read_text()!=content:raise SystemExit("discourse corpus out of sync")
    else:OUT.write_text(content)
    print("six three-clause documents verified against existing structural corpus")
if __name__=="__main__":main()
