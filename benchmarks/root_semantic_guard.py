"""Reference-parser semantic-structure guard for hypothetical dik -> dir.

This checks deterministic grammar features ONLY, not bilingual comprehension,
speaker recognition, or user approval of a new canonical lemma.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

from formalization.core import Unisermo
from .root_substitution import full_finite

ROOT = Path(__file__).resolve().parents[1]
MORPH = ROOT / "formalization/data/morphology.json"
LEXICON = ROOT / "formalization/data/lexicon_index.json"
BASE = "dik"
PROPOSAL = "dir"
SUBJECTS = {
    (1, "singular"): "i", (2, "singular"): "u", (3, "singular"): "a",
    (1, "plural"): "in", (2, "plural"): "un", (3, "plural"): "an",
}


def shadow_reference_language() -> Unisermo:
    """Experimental in-memory overlay; generated and normative files untouched."""
    language = Unisermo()
    if BASE not in language.verbs or PROPOSAL in language.lexicon:
        raise ValueError("candidate cannot be overlaid without replacing a unique verb")
    entry = copy.deepcopy(language.lexicon.pop(BASE))
    entry["form"] = PROPOSAL
    entry["experimental_alias_of"] = BASE
    language.lexicon[PROPOSAL] = entry
    language.verbs.remove(BASE)
    language.verbs.add(PROPOSAL)
    return language


def structure(parsed: dict) -> dict:
    pred = parsed["predicate"]
    subj = parsed["subject"]
    obj = parsed["object"]
    return {
        "semantic_root": "say_tell" if pred["lemma"] in {BASE, PROPOSAL} else pred["lemma"],
        "tense": pred["tense"], "aspect": pred["aspect"],
        "person": pred["person"], "number": pred["number"],
        "negative": parsed["negative"], "interrogative": parsed["interrogative"],
        "subject": {
            "kind": subj["kind"], "person": subj.get("person"), "number": subj.get("number"),
            "lemma": subj.get("lemma"), "modifiers": subj.get("modifiers"),
        },
        "object": None if obj is None else {
            "lemma": obj["lemma"], "case": obj["case"], "modifiers": obj["modifiers"],
        },
    }


def paired_inputs(morph: dict) -> list[dict]:
    cases = []
    for row in full_finite(BASE, morph):
        old = row["text"][:-1]
        suffix = old[len(BASE):]
        new = PROPOSAL + suffix
        person, number = row["person"], row["number"]
        pronoun = SUBJECTS[(person, number)]
        intents = {x: row[x] for x in ("tense", "aspect", "person", "number")}
        for shape, left, right in (
            ("pro_drop", old + ".", new + "."),
            ("explicit_subject", f"{pronoun} {old}.", f"{pronoun} {new}."),
            ("negated", f"no {old}.", f"no {new}."),
            ("polar_question", f"ka {old}?", f"ka {new}?"),
        ):
            cases.append({
                "id": f"S{len(cases)+1:03d}",
                "shape": shape, "intent": intents,
                "baseline_text": left, "candidate_text": right,
            })
    # The participle fakit is attested in the existing reference parser;
    # tik is the protected proximal demonstrative. These examples test syntax
    # and lexical separation, NOT whether "say a fact" is natural discourse.
    for shape, old, new in (
        ("object_participle", "diki fakitem.", "diri fakitem."),
        ("object_with_tik", "diki tik fakitem.", "diri tik fakitem."),
        ("negated_object", "i no diki fakitem.", "i no diri fakitem."),
        ("question_with_tik", "ka diki tik fakitem?", "ka diri tik fakitem?"),
        ("negative_question_with_tik", "ka i no diki tik fakitem?", "ka i no diri tik fakitem?"),
    ):
        cases.append({
            "id": f"S{len(cases)+1:03d}", "shape": shape,
            "intent": None, "baseline_text": old, "candidate_text": new,
        })
    return cases


def evaluate() -> dict:
    baseline = Unisermo()
    candidate = shadow_reference_language()
    generated = paired_inputs(baseline.morph)
    by_shape: dict[str, int] = {}
    errors = []
    for item in generated:
        try:
            b = baseline.parse_sentence(item["baseline_text"])
            c = candidate.parse_sentence(item["candidate_text"])
            if structure(b) != structure(c):
                raise ValueError(f"semantic-structure mismatch in {item['id']}")
            if b["predicate"]["lemma"] != BASE or c["predicate"]["lemma"] != PROPOSAL:
                raise ValueError(f"wrong lemma in {item['id']}")
            by_shape[item["shape"]] = by_shape.get(item["shape"], 0) + 1
        except (KeyError, ValueError) as exc:
            errors.append({"id": item["id"], "error": str(exc)})
    # Control for prefix confusion with existing dirig; this root is NEVER
    # replaced or segmented as dir + an invented suffix.
    control_texts = [
        "dirigi.", "dirigdi.", "ka u dirigdu?", "no dirigia.",
        "i dirigi.", "ka no dirigi?",
    ]
    controls = []
    for text in control_texts:
        try:
            b = baseline.parse_sentence(text)
            c = candidate.parse_sentence(text)
            if b["predicate"]["lemma"] != "dirig" or c["predicate"]["lemma"] != "dirig":
                raise ValueError(f"dirig misparsed in {text}")
            if structure(b) != structure(c):
                raise ValueError(f"dirig meaning changed in {text}")
            controls.append(text)
        except (KeyError, ValueError) as exc:
            errors.append({"control": text, "error": str(exc)})
    # No backward-compatible unmarked aliases: both interpreters fail closed.
    for language, text, label in (
        (baseline, "diri.", "canonical_parser_does_not_know_candidate"),
        (candidate, "diki.", "candidate_parser_does_not_accept_old_root"),
    ):
        try:
            language.parse_sentence(text)
            errors.append({"control": label, "error": "unexpected acceptance"})
        except ValueError:
            controls.append(label)

    files = {"morphology": MORPH, "lexicon_index": LEXICON}
    return {
        "schema": "unisermo/root-structural-parity@1",
        "status": "experimental_parser_parity_not_comprehension",
        "candidate": PROPOSAL, "baseline": BASE,
        "source_sha256": {
            name: hashlib.sha256(path.read_bytes()).hexdigest()
            for name, path in files.items()
        },
        "generated_pairs": len(generated),
        "passing_pairs": sum(by_shape.values()),
        "controls_passed": len(controls),
        "coverage_by_shape": dict(sorted(by_shape.items())),
        "failures": errors,
        "semantic_review": "not_independently_verified",
        "recognition_evidence": None,
        "limitations": [
            "Parser equivalence is structural, not human or LLM comprehension.",
            "The shadow parser is a hypothetical root substitution, not a canonical migration.",
            "Generated paradigms are controlled cases; no pilot holdout data is read.",
            "Object examples check syntax, not natural semantic selection restrictions.",
            "Only supported SVO reference grammar is assessed; no full language equivalence.",
        ],
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    result = evaluate()
    if result["failures"] or result["passing_pairs"] != result["generated_pairs"] or result["controls_passed"] != 8:
        raise SystemExit(f"Structural parity failed: {json.dumps(result['failures'])}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)+"\n")
    print(f"Structural parity: {result['passing_pairs']}/{result['generated_pairs']} pairs and "
          f"{result['controls_passed']} contrast controls passed (no comprehension claim)")


if __name__ == "__main__":
    main()
