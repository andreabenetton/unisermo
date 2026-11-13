"""Read-only structural/provenance preflight for UCUB-001 candidates.

Not a semantic equivalence validator, not a parser verification, not a scored run.
Run from repository root: python -m benchmarks.ucub_001_validate
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "benchmarks/corpus/ucub-001/candidates.jsonl"
CONFIRMED = ROOT / "research/lexicon/confirmed_lexicon.json"
INDEX = ROOT / "formalization/data/lexicon_index.json"


def audit() -> dict:
    cases = [json.loads(line) for line in CORPUS.read_text(encoding="utf8").splitlines() if line.strip()]
    confirmed = {e["form"] for e in json.loads(CONFIRMED.read_text(encoding="utf8"))["entries"]}
    indexed = {e["form"]: e for e in json.loads(INDEX.read_text(encoding="utf8"))["entries"]}
    errors, warnings = [], []
    seen_ids, seen_prompts = set(), set()
    groups = defaultdict(set)
    levels, splits, provenance = Counter(), Counter(), Counter()
    lexical = set()

    if len(cases) != 80:
        errors.append(f"expected 80 candidate cases; found {len(cases)}")
    for case in cases:
        ident = case.get("id")
        if ident in seen_ids:
            errors.append(f"duplicate ID {ident}")
        seen_ids.add(ident)
        level, split, family = case.get("level"), case.get("split"), case.get("family_id")
        levels[level] += 1
        splits[split] += 1
        groups[(level, family)].add(split)
        if split not in ("development", "holdout"):
            errors.append(f"{ident}: unexpected split {split!r}")
        prompt_key = (level, case.get("unisermo"), case.get("question"))
        if prompt_key in seen_prompts:
            errors.append(f"{ident}: duplicate level/input/question")
        seen_prompts.add(prompt_key)
        if case.get("semantic_review") != "independently_reviewed":
            warnings.append(f"{ident}: English/gold not independently reviewed")
        if case.get("parser_status") not in ("verified", "reviewed_unsupported"):
            warnings.append(f"{ident}: parser verification outstanding")
        for form, declaration in case.get("lexicon", {}).items():
            lexical.add(form)
            if form in confirmed:
                expected = "confirmed_lexicon"
            elif form in indexed:
                expected = indexed[form]["status"]
            else:
                expected = "missing_index"
            observed = case.get("lexicon_provenance", {}).get(form)
            if observed != expected:
                errors.append(f"{ident}: provenance {form}: {observed!r} != {expected!r}")
            provenance[expected] += 1
            if expected == "missing_index":
                errors.append(f"{ident}: unindexed lexical item {form!r}")
            if not isinstance(declaration, str) or not declaration.strip():
                errors.append(f"{ident}: empty lexical gloss for {form!r}")

    if set(levels) != {1, 2, 3, 4} or any(levels[i] != 20 for i in (1, 2, 3, 4)):
        errors.append(f"expected 20 per level: {dict(levels)}")
    if dict(splits) != {"development": 60, "holdout": 20}:
        errors.append(f"expected 60/20 split: {dict(splits)}")
    for (level, family), memberships in groups.items():
        if len(memberships) > 1:
            errors.append(f"split-leaking family: L{level} {family}: {sorted(memberships)}")

    return {
        "schema": "unisermo/ucub-001-preflight@1",
        "readiness": "BLOCKED" if errors or warnings else "STRUCTURAL_ONLY",
        "candidate_count": len(cases),
        "levels": dict(sorted(levels.items(), key=lambda kv: str(kv[0]))),
        "splits": dict(sorted(splits.items())),
        "distinct_lexicon_forms_in_glossaries": len(lexical),
        "lexical_provenance_occurrences": dict(sorted(provenance.items())),
        "errors": errors,
        "warnings_count": len(warnings),
        "warnings_sample": warnings[:12],
        "not_verified": [
            "canonical lexical valency of each case",
            "parser semantics",
            "English equivalence",
            "independent logical gold",
            "true semantic/template holdout isolation",
        ],
    }


def main() -> None:
    result = audit()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["errors"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
