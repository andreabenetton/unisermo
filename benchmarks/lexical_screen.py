"""Inventory-first diagnostic for experimental lexical candidates.

Mechanical screening only: it does not score recognizability or approve roots.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MORPH = ROOT / "formalization/data/morphology.json"
LEXICON = ROOT / "formalization/data/lexicon_index.json"
CANDIDATES = ROOT / "research/lexicon/candidate-register.json"
SOFT_MERGERS = {"b": "p", "d": "t", "g": "k", "z": "s"}

def accent_keys(form: str) -> set[str]:
    """Conservative closures of licensed single-letter accent mergers.

    v can become f or w; each eligible position can merge independently.
    These are *screening* approximations, not phonetic transcriptions.
    """
    keys = {""}
    for letter in form:
        variants = {letter, SOFT_MERGERS.get(letter, letter)}
        if letter == "v":
            variants |= {"f", "w"}
        keys = {prefix + replacement for prefix in keys for replacement in variants}
    return keys

def protected_forms(morph: dict) -> set[str]:
    finite = morph["finite"]
    words = set(finite["person"].values())
    words |= {p + finite["number"]["plural"] for p in finite["person"].values()}
    words |= {morph["syntax"]["polar_marker"], morph["syntax"]["negator"],
              morph["syntax"]["optional_indefinite"], morph["nominal"]["plural_particle"]}
    return words

def nominal_forms(root: str, morph: dict) -> set[str]:
    forms = set()
    for case, suffix in morph["nominal"]["case"].items():
        if case == "genitive" and any(root.endswith(x) for x in morph["nominal"]["genitive_alternate_after"]):
            suffix = morph["nominal"]["genitive_alternate"]
        forms.add(root + suffix)
    return forms

def finite_forms(root: str, morph: dict) -> set[str]:
    f = morph["finite"]
    return {root + a + t + p + n for a in f["aspect"].values()
            for t in f["tense"].values() for p in f["person"].values()
            for n in f["number"].values()}

def audit(candidate: str, canonical: str, morph: dict, lexicon: list[dict]) -> dict:
    alphabet = set(morph["alphabet"])
    invalid = sorted(set(candidate) - alphabet)
    valid = bool(candidate) and candidate.isascii() and candidate.isalpha() and candidate.islower() and not invalid
    result = {"canonical": canonical, "candidate": candidate, "inventory_valid": valid,
              "invalid_letters": invalid, "exact_collisions": [], "accent_merger_risks": [],
              "morphological_collisions": [], "recognizability": "not_measured"}
    if not valid:
        return result
    others = {x["form"]: x["status"] for x in lexicon if x["form"] != canonical}
    guards = protected_forms(morph)
    result["exact_collisions"] = sorted(set(others) & {candidate} | guards & {candidate})
    candidate_accents = accent_keys(candidate)
    result["accent_merger_risks"] = sorted(word for word in (set(others) | guards)
        if word != candidate and candidate_accents & accent_keys(word))
    candidate_family = finite_forms(candidate, morph) | nominal_forms(candidate, morph)
    result["morphological_collisions"] = sorted(candidate_family & (set(others) | guards))
    # A risk is only a screening flag, not automatic proof of unintelligibility.
    return result

def evaluate(register: dict, morph: dict, lexicon: list[dict]) -> dict:
    rows = []
    for entry in register["candidates"]:
        canonical = entry["canonical"]
        forms = [canonical] + entry.get("proposed_comparison", [])
        for form in forms:
            rows.append(audit(form, canonical, morph, lexicon))
    return {"schema": "unisermo/lexical-screen@1", "status": "research_only",
            "limitations": ["No automated modern-language recognizability claim",
                            "No corpus frequency estimates",
                            "Accent screening approximates only explicit letter mergers",
                            "Morphological scan covers finite verbs and nominal cases, not full derivation"],
            "results": rows}

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    morph = json.loads(MORPH.read_text())
    lexicon = json.loads(LEXICON.read_text())["entries"]
    register = json.loads(CANDIDATES.read_text())
    result = evaluate(register, morph, lexicon)
    report = json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report)
    else:
        print(report, end="")

if __name__ == "__main__":
    main()
