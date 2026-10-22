"""Measure modern *surface-form* frequencies for experimental Unisermo roots.

Not concept frequency, speaker recognition, or verified bilingual equivalence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]
SEEDS = ROOT / "research/lexicon/modern-form-seeds.json"
MORPH = ROOT / "formalization/data/morphology.json"
LEXICON = ROOT / "formalization/data/lexicon_index.json"
RELATIONS = {
    "translation_candidate", "translation_non_cognate",
    "related_family_not_equivalent", "related_family_sense_check",
    "orthographic_variant",
}


def validate(seeds: dict, alphabet: str, roots: set[str]) -> None:
    if seeds.get("schema") != "unisermo/modern-form-seeds@1":
        raise ValueError("unknown seeds schema")
    ids: set[str] = set()
    for concept in seeds["concepts"]:
        ident = concept["id"]
        canonical = concept["canonical"]
        if ident in ids:
            raise ValueError(f"duplicate concept: {ident}")
        ids.add(ident)
        if canonical not in roots or not set(canonical) <= set(alphabet):
            raise ValueError(f"noncanonical root: {canonical}")
        source = concept["latin"]
        if not source.get("headword") or not source.get("source_url", "").startswith(
            "https://kaikki.org/dictionary/Latin/meaning/"
        ):
            raise ValueError(f"untraceable Latin source: {ident}")
        seen: set[tuple[str, str]] = set()
        if not concept.get("modern"):
            raise ValueError(f"no modern forms: {ident}")
        for item in concept["modern"]:
            lang, form = item["language"], item["form"]
            if not form or not lang or form.strip() != form or any(c.isspace() for c in form):
                raise ValueError(f"invalid surface form for {ident}: {form!r}")
            key = lang, form.casefold()
            if key in seen:
                raise ValueError(f"duplicate modern form: {ident}/{lang}/{form}")
            seen.add(key)
            if item["comparison_role"] not in RELATIONS:
                raise ValueError(f"unknown comparison role: {item['comparison_role']}")
            if item.get("modern_sense_review") != "pending":
                raise ValueError("seed may not claim independent semantic approval")
            if item.get("spoken_recognizability") is not None or item.get("written_recognizability") is not None:
                raise ValueError("seed may not assert unmeasured recognizability")


def measure(seeds: dict, digest: str, frequency: Callable[[str, str], float],
            provider_version: str, wordlist: str = "best") -> dict:
    """Frequency injection keeps unit tests independent of wordfreq installs."""
    results = []
    for concept in seeds["concepts"]:
        observations = []
        for item in concept["modern"]:
            z = float(frequency(item["form"], item["language"]))
            if not math.isfinite(z) or z < 0:
                raise ValueError(f"invalid frequency for {item['language']}:{item['form']}")
            observations.append({
                "language": item["language"], "form": item["form"],
                "comparison_role": item["comparison_role"],
                "modern_sense_review": item["modern_sense_review"],
                "zipf_form_frequency": z,
                "corpus_coverage": "below_threshold_or_unobserved" if z == 0 else "observed",
                "spoken_recognizability": None, "written_recognizability": None,
                "is_concept_frequency": False,
            })
        results.append({
            "concept_id": concept["id"], "canonical": concept["canonical"],
            "latin": concept["latin"], "modern": observations,
            "concept_frequency": None, "population_weighted_recognition": None,
        })
    return {
        "schema": "unisermo/modern-form-frequencies@1",
        "status": "measured_form_frequencies_unreviewed_senses",
        "source_seed_sha256": digest,
        "frequency_provider": {
            "name": "wordfreq", "version": provider_version,
            "wordlist": wordlist, "url": "https://pypi.org/project/wordfreq/",
        },
        "limitations": [
            "A word form's corpus frequency is NOT concept frequency.",
            "Frequency does not measure auditory or orthographic recognition.",
            "Morphological and spelling variants must not be summed.",
            "Modern meanings, roots and lexical equivalence are pending independent review.",
            "Never sum frequencies across languages as if they were population weighted.",
            "Zipf 0 means unobserved/below threshold, not never used.",
        ],
        "concepts": results,
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--seeds", type=Path, default=SEEDS)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--wordlist", choices=["small", "large", "best"], default="best")
    args = p.parse_args()
    source_bytes = args.seeds.read_bytes()
    seeds = json.loads(source_bytes)
    morph = json.loads(MORPH.read_text(encoding="utf-8"))
    lex = json.loads(LEXICON.read_text(encoding="utf-8"))["entries"]
    validate(seeds, morph["alphabet"], {x["form"] for x in lex if x["status"] == "confirmed_lexicon"})

    try:
        from importlib.metadata import version
        from wordfreq import available_languages, zipf_frequency
    except ImportError as exc:
        raise SystemExit("Install: pip install -r benchmarks/requirements-frequency.txt") from exc

    supported = set(available_languages(wordlist=args.wordlist))
    used = {x["language"] for c in seeds["concepts"] for x in c["modern"]}
    if used - supported:
        raise ValueError(f"unsupported wordfreq languages: {sorted(used - supported)}")
    result = measure(
        seeds, hashlib.sha256(source_bytes).hexdigest(),
        lambda form, lang: zipf_frequency(form, lang, wordlist=args.wordlist),
        version("wordfreq"), args.wordlist,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    count = sum(len(c["modern"]) for c in result["concepts"])
    print(f"Measured {count} modern word forms in {len(result['concepts'])} concepts (no concept or recognition scores)")


if __name__ == "__main__":
    main()
