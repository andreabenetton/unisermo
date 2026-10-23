"""First incremental corpus expansion: parser-verified structure ONLY.

Separate from the immutable 78-row bilingual pilot and its frozen holdout.
This contains no invented English-equivalent sentences and no human review.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from formalization.core import Unisermo

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "benchmarks/corpus/expansion-001.jsonl"
VERBS = ("vid", "pel", "trak")
NOUNS = ("akwa", "frat", "aerplan")
FEATURES = (
    ("present", "simple", 1, "singular"),
    ("past", "simple", 2, "singular"),
    ("future", "simple", 3, "singular"),
    ("present", "progressive", 1, "plural"),
)
# Four grammatical shapes: subject omitted, explicit pronoun, negated, polar question.
SHAPES = ("pro_drop", "subject", "negative", "polar")

def build() -> list[dict]:
    language = Unisermo()
    rows: list[dict] = []
    for verb in VERBS:
        for noun in NOUNS:
            for tense, aspect, person, number in FEATURES:
                finite = language.generate_verb(verb, tense, aspect, person, number)
                obj = language.generate_noun(noun, "accusative")
                subject = language.person_to_form[(number, person)]
                for shape in SHAPES:
                    clause = {
                        "pro_drop": finite + " " + obj + ".",
                        "subject": subject + " " + finite + " " + obj + ".",
                        "negative": "no " + finite + " " + obj + ".",
                        "polar": "ka " + finite + " " + obj + "?",
                    }[shape]
                    parsed = language.parse_sentence(clause)
                    predicate = parsed["predicate"]
                    if (predicate["lemma"], predicate["tense"], predicate["aspect"],
                        predicate["person"], predicate["number"]) != (verb, tense, aspect, person, number):
                        raise ValueError(f"parser meaning mismatch: {clause}")
                    if parsed["object"] is None or parsed["object"]["lemma"] != noun:
                        raise ValueError(f"object mismatch: {clause}")
                    if parsed["negative"] != (shape == "negative") or parsed["interrogative"] != (shape == "polar"):
                        raise ValueError(f"operator mismatch: {clause}")
                    rows.append({
                        "id": f"E{len(rows)+1:04d}",
                        "unisermo": clause,
                        "group": "basic_clauses_objects" if shape in ("pro_drop", "subject") else "negation_questions_operators_conditionals",
                        "subgroup": shape,
                        "semantic_review": "pending",
                        "english": None,
                        "parser_verified": True,
                        "historical_pilot_member": False,
                        "split": "development",
                        "grammatical_intent": {
                            "lemma": verb, "object_lemma": noun, "tense": tense, "aspect": aspect,
                            "person": person, "number": number, "negative": shape == "negative",
                            "interrogative": shape == "polar",
                        },
                    })
    if len(rows) != 144 or len({x["unisermo"] for x in rows}) != 144:
        raise ValueError("expansion row count/uniqueness error")
    return rows

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--check", action="store_true")
    args = p.parse_args()
    rows = build()
    content = "".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in rows)
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf8") != content:
            raise SystemExit("expansion-001 corpus out of sync")
    else:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(content, encoding="utf8")
    print(f"expansion-001: {len(rows)} draft parser-verified clauses; sha256={hashlib.sha256(content.encode()).hexdigest()}")

if __name__ == "__main__":
    main()
