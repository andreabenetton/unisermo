"""Validate independent review ledger against the immutable pilot corpus."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "benchmarks/corpus/pilot.jsonl"
LEDGER = ROOT / "docs/reviews/pilot-reviews.jsonl"
ALLOWED = {"pending", "needs_revision", "verified", "rejected"}

def records(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

def validate(pilot: list[dict], reviews: list[dict]) -> dict:
    corpus = {r["id"]:r for r in pilot}
    ledger = {r["id"]:r for r in reviews}
    if len(corpus) != len(pilot) or len(ledger) != len(reviews):
        raise ValueError("duplicate review or corpus IDs")
    if set(corpus) != set(ledger):
        raise ValueError("ledger does not cover exactly the pilot IDs")
    counts = {status:0 for status in sorted(ALLOWED)}
    for ident, review in ledger.items():
        sample=corpus[ident]
        if review["status"] not in ALLOWED:
            raise ValueError(f"{ident}: invalid status")
        if (review["source_unisermo"] != sample["unisermo"] or
                review["source_english"] != sample["english"]):
            raise ValueError(f"{ident}: source drift; version the corpus instead")
        if review["status"] == "verified":
            if not all(review.get(k) for k in ("reviewer","reviewed_at","approved_english")):
                raise ValueError(f"{ident}: verified requires reviewer, date and approved rendering")
        else:
            if review.get("approved_english"):
                raise ValueError(f"{ident}: unverified row cannot have approved rendering")
        counts[review["status"]] += 1
    return {"total": len(pilot), "statuses": counts, "verified": counts["verified"]}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--pilot",type=Path,default=PILOT)
    p.add_argument("--ledger",type=Path,default=LEDGER)
    a=p.parse_args()
    print(json.dumps(validate(records(a.pilot),records(a.ledger)),sort_keys=True))

if __name__=="__main__":
    main()
