"""Build and score a counterbalanced, blind lexical inference trial.

No provider calls are made. Each question MUST be sent to the tested model
in an isolated conversation, without the answer key. Experimental only.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

from formalization.core import Unisermo
from .root_semantic_guard import shadow_reference_language

ROOT = Path(__file__).resolve().parents[1]
SENSES = ("say or tell", "direct or guide", "build or construct")
TARGETS = (("dik", 0, "baseline"), ("dir", 0, "experimental"), ("dirig", 1, "control"))
CONDITIONS = ("unglossed", "explicit_glossary")

# Identical balanced feature sets for all target roots: 9 development + 3
# frozen evaluation cases. Avoid corpus pilot and all its prior holdout data.
FEATURES = (
    ("present", "simple", 1, "singular"),
    ("present", "simple", 2, "singular"),
    ("present", "simple", 3, "singular"),
    ("present", "simple", 1, "plural"),
    ("past", "simple", 2, "plural"),
    ("future", "simple", 3, "plural"),
    ("past", "progressive", 1, "singular"),
    ("present", "progressive", 2, "singular"),
    ("present", "perfect", 3, "singular"),
    ("past", "perfect", 1, "plural"),
    ("future", "perfect", 2, "plural"),
    ("future", "progressive", 3, "plural"),
)

PRIMER = (
    "Unisermo is an experimental constructed language. Finite verbs have a "
    "root followed by an optional aspect vowel (e=progressive, o=completed), "
    "a tense marker (present=none, past=d, future=f), then person "
    "(i=first, u=second, a=third) and optional plural n. "
    "This question asks which lexical ACTION the root most likely means, "
    "NOT which tense or person the ending encodes. "
    "The meaning is not guaranteed to be inferable from the spelling alone."
)
GLOSSARY = (
    "For this controlled test, use the following temporary dictionary: "
    "dik=say/tell; dir=say/tell (hypothetical alternative); "
    "dirig=direct/guide. Other words are not relevant."
)


def generated_form(root: str, feature: tuple, morph: dict) -> str:
    tense, aspect, person, number = feature
    f = morph["finite"]
    return root + f["aspect"][aspect] + f["tense"][tense] + \
        f["person"][str(person)] + f["number"][number] + "."


def build_pack() -> tuple[list[dict], list[dict]]:
    baseline, shadow = Unisermo(), shadow_reference_language()
    questions, answer_key = [], []
    for condition_index, condition in enumerate(CONDITIONS):
        for case_index, feature in enumerate(FEATURES):
            split = "development" if case_index < 9 else "frozen_evaluation"
            for root_index, (root, sense_index, role) in enumerate(TARGETS):
                surface = generated_form(root, feature, baseline.morph)
                interpreter = shadow if role == "experimental" else baseline
                parsed = interpreter.parse_sentence(surface)
                if (parsed["predicate"]["lemma"] != root
                        or parsed["predicate"]["tense"] != feature[0]
                        or parsed["predicate"]["aspect"] != feature[1]
                        or parsed["predicate"]["person"] != feature[2]
                        or parsed["predicate"]["number"] != feature[3]):
                    raise ValueError(f"unusable controlled surface: {surface}")
                # Permute the THREE sense choices so each correct letter is
                # represented exactly 4 times per root and per condition.
                offset = (case_index + root_index + condition_index) % 3
                labels = ("A", "B", "C")
                choice_senses = SENSES[offset:] + SENSES[:offset]
                choices = {letter: meaning for letter, meaning in zip(labels, choice_senses)}
                correct = next(letter for letter, meaning in choices.items()
                               if meaning == SENSES[sense_index])
                ident = f"R{len(questions)+1:03d}"
                extra = "\n" + GLOSSARY if condition == "explicit_glossary" else ""
                text = (
                    PRIMER + extra + "\n\n"
                    f"Word to interpret: {surface}\n"
                    + "\n".join(f"{letter}) {meaning}" for letter, meaning in choices.items())
                    + "\nReply with ONLY the capital letter A, B, or C."
                )
                questions.append({
                    "id": ident, "split": split, "condition": condition,
                    "surface": surface, "choices": choices,
                    "messages": [{"role": "user", "content": text}],
                    "response_format": "single_choice_letter",
                    "independent_conversation_required": True,
                })
                answer_key.append({
                    "id": ident, "split": split, "condition": condition,
                    "case_index": case_index, "root": root, "role": role,
                    "expected_choice": correct, "expected_sense": SENSES[sense_index],
                    "grammar_features": {
                        "tense": feature[0], "aspect": feature[1],
                        "person": feature[2], "number": feature[3],
                    },
                })
    if len(questions) != 72 or len(answer_key) != 72:
        raise ValueError("unexpected trial size")
    return questions, answer_key


def validate_responses(responses: list[dict], key: list[dict]) -> dict[str, str]:
    expected = {x["id"]: x for x in key}
    observed = {}
    if len(expected) != len(key):
        raise ValueError("duplicate IDs in answer key")
    for response in responses:
        ident = response.get("id")
        if ident in observed:
            raise ValueError(f"duplicate response: {ident}")
        if ident not in expected:
            raise ValueError(f"unknown trial id: {ident}")
        answer = response.get("answer")
        if not isinstance(answer, str):
            raise ValueError(f"missing answer at {ident}")
        # Invalid model outputs are preserved and scored as incorrect, not
        # silently 'fixed' by extracting a nearby letter.
        observed[ident] = answer.strip()
    if set(expected) != set(observed):
        raise ValueError(f"missing responses for {len(set(expected)-set(observed))} trials")
    return observed


def score(key: list[dict], responses: list[dict], model_id: str) -> dict:
    if not model_id.strip():
        raise ValueError("an explicit model ID is mandatory")
    observed = validate_responses(responses, key)
    groups = defaultdict(lambda: [0, 0, 0])
    paired = defaultdict(dict)
    for question in key:
        ident = question["id"]
        actual = observed[ident]
        correct = actual == question["expected_choice"]
        group = (question["split"], question["condition"], question["root"])
        groups[group][0] += 1
        groups[group][1] += int(correct)
        groups[group][2] += int(actual not in ("A", "B", "C"))
        pair = (question["split"], question["condition"], question["case_index"])
        if question["root"] in ("dik", "dir"):
            paired[pair][question["root"]] = correct
    comparisons = []
    for (split, condition, root), (total, correct, malformed) in sorted(groups.items()):
        comparisons.append({
            "split": split, "condition": condition, "root": root,
            "samples": total, "correct": correct, "malformed": malformed,
            "accuracy": round(correct / total, 4),
        })
    pairwise = []
    for split in ("development", "frozen_evaluation"):
        for condition in CONDITIONS:
            shared = [values for (s, c, _), values in paired.items()
                      if s == split and c == condition]
            if any(set(values) != {"dik", "dir"} for values in shared):
                raise ValueError("not all paired cases are present")
            pairwise.append({
                "split": split, "condition": condition, "pairs": len(shared),
                "dir_only_correct": sum(v["dir"] and not v["dik"] for v in shared),
                "dik_only_correct": sum(v["dik"] and not v["dir"] for v in shared),
                "both_correct": sum(v["dik"] and v["dir"] for v in shared),
                "both_wrong": sum(not v["dik"] and not v["dir"] for v in shared),
            })
    return {
        "schema": "unisermo/root-recognition-score@1",
        "status": "model_answers_scored_not_human_validation",
        "model_id": model_id,
        "questions_scored": len(key),
        "summary": comparisons,
        "paired_comparison": pairwise,
        "interpretation_limits": [
            "Tiny, highly dependent forms from only three lexemes; no statistical generalization.",
            "The unglossed test estimates lexical guessing, not full model understanding.",
            "The glossary test checks use of a supplied dictionary, not spontaneous recognition.",
            "Each question must be a separate model conversation with answer keys absent.",
            "Public prompts and answer keys may become contaminated in future model training.",
            "The frozen evaluation portion must not drive changes to spelling or prompts.",
            "No response counts here measure actual human auditory recognition.",
        ],
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    commands = p.add_subparsers(dest="command", required=True)
    build = commands.add_parser("build")
    build.add_argument("--output-dir", type=Path, required=True)
    build.add_argument("--check", action="store_true")
    report = commands.add_parser("score")
    report.add_argument("--key", type=Path, required=True)
    report.add_argument("--responses", type=Path, required=True)
    report.add_argument("--model-id", required=True)
    report.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    if args.command == "build":
        questions, keys = build_pack()
        out = args.output_dir
        texts = {
            out / "root-recognition-prompts-v1.jsonl": "".join(
                json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in questions
            ),
            out / "root-recognition-answer-key-v1.jsonl": "".join(
                json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in keys
            ),
        }
        for path, content in texts.items():
            if args.check:
                if not path.exists() or path.read_text(encoding="utf-8") != content:
                    raise SystemExit(f"trial pack is out of sync: {path}")
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
        print(f"Prepared {len(questions)} blinded trial prompts and separate answer key")
    elif args.command == "score":
        keys = [json.loads(x) for x in args.key.read_text(encoding="utf-8").splitlines() if x.strip()]
        responses = [json.loads(x) for x in args.responses.read_text(encoding="utf-8").splitlines() if x.strip()]
        result = score(keys, responses, args.model_id)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
        print(f"Scored {result['questions_scored']} model answers; no human recognition claim")


if __name__ == "__main__":
    main()
