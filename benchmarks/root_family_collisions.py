"""Conservative whole-paradigm collision screen for root replacement.

Generated forms from roots with ambiguous category are HYPOTHETICAL; flags
are candidates for linguistic review, not certified real grammatical collisions.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from .lexical_screen import (
    MORPH, LEXICON, CANDIDATES, accent_keys, finite_forms, nominal_forms,
    protected_forms,
)

DERIVED = ("or", "il", "ia", "it", "itat", "al")


def possible_family(root: str, morph: dict) -> dict[str, str]:
    forms: dict[str, str] = {root: "bare"}
    forms.update({x: "finite_hypothesis" for x in finite_forms(root, morph)})
    forms.update({x: "nominal_hypothesis" for x in nominal_forms(root, morph)})
    forms.update({root + x: "derivation_hypothesis" for x in DERIVED})
    return forms


def analyze(root: str, old: str, morph: dict, lexicon: list[dict],
            limit: int = 80) -> dict:
    if not root or not root.isascii() or not root.isalpha() or root != root.lower() or not set(root) <= set(morph["alphabet"]):
        raise ValueError(f"noncanonical candidate: {root}")
    candidates = possible_family(root, morph)

    # Keep only lexicon's confirmed base families; attested/example-only surface
    # forms are included as standalone words but never licensed productively.
    other_surfaces: dict[str, set[str]] = defaultdict(set)
    for entry in lexicon:
        source = entry["form"]
        if source == old:
            continue
        other_surfaces[source].add(source)
        if entry["status"] == "confirmed_lexicon":
            for variant in possible_family(source, morph):
                other_surfaces[variant].add(source)
    guards = protected_forms(morph) | {"tik", "tes", "tan"}
    for guard in guards:
        other_surfaces[guard].add(f"protected:{guard}")

    exact = []
    soft = []
    # Accent variants indexed once per other surface, then matched on candidate.
    accent_index: dict[str, set[str]] = defaultdict(set)
    for surface in other_surfaces:
        for key in accent_keys(surface):
            accent_index[key].add(surface)
    for candidate, role in sorted(candidates.items()):
        if candidate in other_surfaces:
            exact.append({
                "candidate_form": candidate, "formation": role,
                "other_form": candidate, "other_sources": sorted(other_surfaces[candidate]),
            })
        merged = set()
        for key in accent_keys(candidate):
            merged.update(accent_index.get(key, set()))
        for other in sorted(merged - {candidate}):
            soft.append({
                "candidate_form": candidate, "formation": role,
                "other_form": other, "other_sources": sorted(other_surfaces[other]),
            })
    return {
        "candidate": root, "replaces": old, "generated_candidate_surfaces": len(candidates),
        "other_surfaces": len(other_surfaces),
        "exact_count": len(exact), "accent_merge_risk_count": len(soft),
        "exact_collisions": exact[:limit], "accent_merge_risks": soft[:limit],
        "truncated": len(exact) > limit or len(soft) > limit,
        "status": "mechanical_overgeneration_not_human_validated",
        "limits": [
            "All productive categories are hypothetically generated for confirmed lexical entries.",
            "Attested-only and example-only entries contribute only their bare forms.",
            "Accent keys cover only documented soft single-grapheme mergers.",
            "Contextual parsing, syllabification and unmodeled coalescences are not evaluated.",
        ],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    morph = json.loads(MORPH.read_text(encoding="utf-8"))
    lexicon = json.loads(LEXICON.read_text(encoding="utf-8"))["entries"]
    register = json.loads(CANDIDATES.read_text(encoding="utf-8"))
    records = []
    for item in register["candidates"]:
        if item["proposed_comparison"]:
            records.append(analyze(item["canonical"], item["canonical"], morph, lexicon))
        for alternative in item["proposed_comparison"]:
            records.append(analyze(alternative, item["canonical"], morph, lexicon))
    result = {"schema": "unisermo/root-family-collision-screen@1",
              "status": "experimental", "comparisons": records}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, sort_keys=True, ensure_ascii=False, indent=2)+"\n")
    print(", ".join(f"{x['candidate']}: exact={x['exact_count']} soft={x['accent_merge_risk_count']}" for x in records))


if __name__ == "__main__":
    main()
