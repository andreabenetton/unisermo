"""Audit experimental lexical expansion without ratifying any roots."""
from __future__ import annotations
import argparse
import json
from collections import Counter
from pathlib import Path
from benchmarks.lexical_screen import audit, MORPH, LEXICON

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"research/lexicon/expansion-batch-001.json"

def evaluate(data, morph, lexicon):
    if data.get("schema")!="unisermo/lexical-expansion-batch@1":
        raise ValueError("unexpected batch schema")
    items=data["entries"]
    if len(items)!=100 or len({x["id"] for x in items})!=100:
        raise ValueError("batch must contain 100 unique concepts")
    canonical={x["form"] for x in lexicon if x["status"]=="confirmed_lexicon"}
    proposed=[x["proposal"] for x in items if x["proposal"]]
    if len(proposed)!=len(set(proposed)):
        raise ValueError("proposals must be unique")
    results=[]
    for entry in items:
        if entry.get("canonical_adoption") is not False or entry["review_status"] not in {"concept_and_root_unreviewed", "prior_kinship_system_review_required"}:
            raise ValueError("unauthorized ratification")
        if any(entry[x] is not None for x in ("concept_frequency","written_recognition","spoken_recognition")):
            raise ValueError("unmeasured metric supplied")
        root=entry["proposal"]
        if not root:
            continue
        screen=audit(root, "", morph, lexicon)
        results.append({"concept":entry["id"],"root":root,
            "inventory_valid":screen["inventory_valid"],
            "exact_existing":screen["exact_collisions"],
            "accent_merger_risks":screen["accent_merger_risks"],
            "critical_grammar_risks":screen.get("critical_grammar_risks",[]),
            "status":"requires_independent_review"})
    return {"schema":"unisermo/lexical-expansion-screen@1",
        "status":"experimental_no_canonical_changes",
        "concepts":len(items),"root_proposals":len(results),
        "without_proposals":len(items)-len(results),
        "inventory_invalid":sum(not x["inventory_valid"] for x in results),
        "with_exact_existing":sum(bool(x["exact_existing"]) for x in results),
        "with_accent_risks":sum(bool(x["accent_merger_risks"]) for x in results),
        "coverage_by_domain":dict(sorted(Counter(x["domain"] for x in items).items())),
        "results":results,
        "limitations":["A proposed Latin-like spelling is not etymological evidence.",
          "Accent mergers are heuristics, not speaker comprehension observations.",
          "Root candidates have not undergone full cross-candidate paradigmatic collision tests.",
          "Priority bands are expert hypotheses, not measured global concept frequencies.",
          "Nothing here has been approved as canonical vocabulary."]}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    data=json.loads(SOURCE.read_text())
    morph=json.loads(MORPH.read_text())
    lex=json.loads(LEXICON.read_text())["entries"]
    report=evaluate(data,morph,lex)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+"\n")
    print(f"{report['concepts']} concepts, {report['root_proposals']} roots proposed, "
          f"{report['inventory_invalid']} inventory invalid")
if __name__=="__main__":main()
