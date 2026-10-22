"""Counterfactual root-replacement experiment with *real* OpenAI tokenizers.

Research only. Does not edit accepted Unisermo roots or the original corpus.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from .lexical_screen import audit
from .run import PILOT, load_corpus
from .tokenizers import TiktokenCounter

ROOT = Path(__file__).resolve().parents[1]
MORPH = ROOT / "formalization/data/morphology.json"
LEXICON = ROOT / "formalization/data/lexicon_index.json"
REGISTER = ROOT / "research/lexicon/candidate-register.json"
# This is the productive inventory, not a claim that all formations make sense.
DERIVATION_SUFFIXES = ("or", "il", "ia", "it", "itat", "al")


def full_finite(root: str, morph: dict) -> list[dict]:
    finite = morph["finite"]
    rows = []
    for tense, t in finite["tense"].items():
        for aspect, a in finite["aspect"].items():
            for person, p in finite["person"].items():
                for number, n in finite["number"].items():
                    rows.append({
                        "tense": tense, "aspect": aspect, "person": int(person),
                        "number": number, "text": root + a + t + p + n + ".",
                    })
    return rows


def _genitive_suffix(root: str, morph: dict) -> str:
    noun = morph["nominal"]
    return noun["genitive_alternate"] if any(
        root.endswith(x) for x in noun["genitive_alternate_after"]
    ) else noun["case"]["genitive"]


def samples(root: str, morph: dict) -> dict[str, list[str]]:
    finite = full_finite(root, morph)
    nominal = morph["nominal"]["case"]
    return {
        "finite_pro_drop": [x["text"] for x in finite],
        "nominal_case_hypotheses": [
            root + (_genitive_suffix(root, morph) if case == "genitive" else suffix)
            for case, suffix in nominal.items()
        ],
        "derivation_hypotheses": [root + x for x in DERIVATION_SUFFIXES],
    }


def development_contexts(corpus: list[dict], canonical: str,
                         candidate: str) -> list[tuple[str, str, str]]:
    """Preserve whole text other than exact initial root; never touch holdout."""
    result = []
    for row in corpus:
        if (row["split"] != "development"
                or row["grammatical_intent"].get("lemma") != canonical):
            continue
        source = row["unisermo"]
        if not source.startswith(canonical):
            raise ValueError(f"cannot substitute root safely in {row['id']}")
        result.append((row["id"], source, candidate + source[len(canonical):]))
    return result


def metrics(counter, old: list[str], new: list[str]) -> dict:
    if len(old) != len(new) or not old:
        raise ValueError("paired nonempty samples required")
    baseline = sum(counter.count(s) for s in old)
    alternative = sum(counter.count(s) for s in new)
    if baseline <= 0 or alternative <= 0:
        raise ValueError("tokenizer returned non-positive totals")
    return {
        "samples": len(old),
        "baseline_tokens": baseline, "alternative_tokens": alternative,
        "extra_tokens": alternative - baseline,
        "pct_change_from_baseline": round(100 * (alternative / baseline - 1), 3),
    }


def evaluate(counter, morph: dict, lexicon: list[dict], register: dict,
             corpus: list[dict], provenance: dict) -> dict:
    experiment = []
    for entry in register["candidates"]:
        base = entry["canonical"]
        for new in entry.get("proposed_comparison", []):
            risk = audit(new, base, morph, lexicon)
            reference = audit(base, base, morph, lexicon)
            if not risk["inventory_valid"]:
                raise ValueError(f"invalid root candidate: {new}")
            if risk["exact_collisions"]:
                raise ValueError(f"lexical collision: {new} = {risk['exact_collisions']}")
            before = samples(base, morph)
            after = samples(new, morph)
            token_groups = {
                key: metrics(counter, before[key], after[key]) for key in before
            }
            contexts = development_contexts(corpus, base, new)
            if contexts:
                token_groups["existing_pilot_development"] = metrics(
                    counter, [x[1] for x in contexts], [x[2] for x in contexts]
                )
            experiment.append({
                "original_root": base,
                "candidate_root": new,
                "source_only_example": "constru" if base == "stru" else None,
                "candidate_length": len(new),
                "baseline_length": len(base),
                "phonemic_alphabet_valid": True,
                "collision_screen": risk,
                "baseline_collision_screen": reference,
                "token_groups": token_groups,
                "human_semantic_review": "pending",
                "modern_spoken_recognizability": None,
                "modern_written_recognizability": None,
            })
    return {
        "schema": "unisermo/root-substitution-experiment@1",
        "status": "counterfactual_no_language_change",
        "tokenizer": counter.name,
        "implementation": counter.implementation,
        "vocab_sha256": getattr(counter, "vocab_sha256", None),
        "source_sha256": provenance,
        "study_split": "generated_inflections_and_development_only",
        "report_limitations": [
            "Generated paradigms are controlled morphology, not a representative corpus.",
            "The canonical verb category of every hypothetical derived form has not been established.",
            "Existing pilot is unreviewed and contains dik, but no stru example.",
            "No holdout sentences are measured, exposed or ranked for candidate selection.",
            "No evidence of human recognition, semantic correctness or full LLM task cost.",
            "Contrast under soft mergers and phonotactic accessibility require human review.",
        ],
        "comparisons": experiment,
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--encodings", nargs="+", default=["o200k_base", "cl100k_base"])
    p.add_argument("--output-dir", type=Path, default=ROOT / "benchmarks/reports")
    args = p.parse_args()

    paths = {"morphology": MORPH, "lexicon": LEXICON,
             "candidate_register": REGISTER, "original_pilot": PILOT}
    docs = {name: path.read_bytes() for name, path in paths.items()}
    provenance = {name: hashlib.sha256(raw).hexdigest()
                  for name, raw in docs.items()}
    morph = json.loads(docs["morphology"])
    lexicon = json.loads(docs["lexicon"])["entries"]
    register = json.loads(docs["candidate_register"])
    pilot = load_corpus(PILOT)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for encoding in args.encodings:
        counter = TiktokenCounter(encoding)
        report = evaluate(counter, morph, lexicon, register, pilot, provenance)
        output = args.output_dir / f"root-substitution-{encoding}.json"
        output.write_text(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
        print(f"{encoding}: {len(report['comparisons'])} counterfactuals -> {output}")


if __name__ == "__main__":
    main()
