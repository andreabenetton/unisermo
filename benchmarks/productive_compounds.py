"""Validate productive-compound examples without changing canonical morphology.

Do not conflate transparent segmentation, correct compositional gloss, and
selection of an established conventional meaning.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "research/lexicon/productive-compound-trials-001.json"
LEXICON = ROOT / "formalization/data/lexicon_index.json"
ALPHABET = set("aeioupbtdkgmnfvszlrjw")

def build_report():
    trials=json.loads(SOURCE.read_text(encoding="utf-8"))
    entries=json.loads(LEXICON.read_text(encoding="utf-8"))["entries"]
    canonical={x["form"]:x for x in entries if x.get("status")=="confirmed_lexicon"}
    # Compounds are also indexed as noun/verb but not always marked confirmed
    # depending on the earlier generator. Canonical index forms are source of truth.
    indexed={x["form"]:x for x in entries}
    errors=[]
    results=[]
    seen=set()
    for item in trials["cases"]:
        ident=item["id"]
        if ident in seen:errors.append(f"duplicate id: {ident}")
        seen.add(ident)
        components=item["components"]
        expected="".join(components)
        if expected!=item["surface"]:
            errors.append(f"{ident}: surface does not match components")
        if any(not part or not set(part)<=ALPHABET for part in components):
            errors.append(f"{ident}: forbidden grapheme")
        unknown=[part for part in components if part not in canonical]
        if unknown:errors.append(f"{ident}: unconfirmed components {unknown}")
        indexed_surface=item["surface"] in indexed
        if item["evidence"]=="confirmed_compound" and not indexed_surface:
            errors.append(f"{ident}: claimed compound not indexed")
        if item["evidence"]=="hypothetical_test" and item["surface"] in canonical:
            errors.append(f"{ident}: hypothetical is confirmed")
        if item["ambiguity"] not in ("low","medium","high"):
            errors.append(f"{ident}: ambiguity missing")
        results.append({"id":ident,"surface":item["surface"],
            "segmentation":components,"indexed_surface":indexed_surface,
            "evidence":item["evidence"],"ambiguity":item["ambiguity"],
            "meaning_status":"not_semantically_reviewed"})
    if trials.get("canonical_changes") is not False:
        errors.append("trial wrongly asserts canonical changes")
    return {"schema":"unisermo/productive-compound-validation@1",
        "status":"mechanical_only", "count":len(results),
        "errors":errors,"cases":results}

def main():
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    report=build_report()
    if report["errors"]:
        raise SystemExit("\n".join(report["errors"]))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(f"Checked {report['count']} productive-compound trials (not semantic validation)")

if __name__=="__main__":
    main()
