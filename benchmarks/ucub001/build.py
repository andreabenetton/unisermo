"""UCUB-001 authored contrast families: 80 independent semantic judgments.

Ground-truth labels are authored as explicit human-auditable judgments, NOT
obtained from the Unisermo parser. Parser checks only syntax acceptance.
The corpus is a DESIGN CANDIDATE until independent human semantic review.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORPUS = Path(__file__).resolve().parent / "corpus.jsonl"
MANIFEST = Path(__file__).resolve().parent / "manifest.json"
LABELS = {"entailed", "contradicted", "undetermined"}

# Each group is an independent four-way contrast family. Keep every group
# intact in one split to avoid leakage of minimal-pair alternatives.
# The last group in each 5-group tier is sealed as evaluation holdout.
# Each item is (Unisermo clauses, controlled English, hypothesis, relation).
GROUPS = [
    ("L1", "visual_polarity", [
        ("i vidi akwaem.", "I see water.", "I see water.", "entailed"),
        ("i no vidi akwaem.", "I do not see water.", "I see water.", "contradicted"),
        ("i peli akwaem.", "I push water.", "I see water.", "undetermined"),
        ("i traki akwaem.", "I pull water.", "I see water.", "undetermined"),
    ]),
    ("L1", "force_polarity", [
        ("i peli akwaem.", "I push water.", "I push water.", "entailed"),
        ("i no peli akwaem.", "I do not push water.", "I push water.", "contradicted"),
        ("i vidi akwaem.", "I see water.", "I push water.", "undetermined"),
        ("i traki akwaem.", "I pull water.", "I push water.", "undetermined"),
    ]),
    ("L1", "temporal_morphology", [
        ("i viddi akwaem.", "I saw water.", "I saw water.", "entailed"),
        ("i no viddi akwaem.", "I did not see water.", "I saw water.", "contradicted"),
        ("i vidi akwaem.", "I see water.", "I saw water.", "undetermined"),
        ("i vidfi akwaem.", "I will see water.", "I saw water.", "undetermined"),
    ]),
    ("L1", "participant_agreement", [
        ("u vidu akwaem.", "You see water.", "You see water.", "entailed"),
        ("u no vidu akwaem.", "You do not see water.", "You see water.", "contradicted"),
        ("i vidi akwaem.", "I see water.", "You see water.", "undetermined"),
        ("a vida akwaem.", "That person sees water.", "You see water.", "undetermined"),
    ]),
    ("L1", "object_roles", [
        ("i vidi aerplanem.", "I see an airplane.", "I see an airplane.", "entailed"),
        ("i no vidi aerplanem.", "I do not see an airplane.", "I see an airplane.", "contradicted"),
        ("i vidi akwaem.", "I see water.", "I see an airplane.", "undetermined"),
        ("i peli aerplanem.", "I push an airplane.", "I see an airplane.", "undetermined"),
    ]),
    ("L2", "desire_intention_attempt", [
        ("i voli mov.", "I want to move.", "I want to move.", "entailed"),
        ("i no voli mov.", "I do not want to move.", "I want to move.", "contradicted"),
        ("i inti mov.", "I intend to move.", "I want to move.", "undetermined"),
        ("i tenti mov.", "I attempt to move.", "I want to move.", "undetermined"),
    ]),
    ("L2", "attempt_not_success", [
        ("i tenti mov.", "I attempt to move.", "I attempt to move.", "entailed"),
        ("i no tenti mov.", "I do not attempt to move.", "I attempt to move.", "contradicted"),
        ("i voli mov.", "I want to move.", "I attempt to move.", "undetermined"),
        ("i inti mov.", "I intend to move.", "I attempt to move.", "undetermined"),
    ]),
    ("L2", "personal_necessity", [
        ("i debi mov.", "I must move.", "I have an obligation to move.", "entailed"),
        ("i no debi mov.", "I do not have to move.", "I have an obligation to move.", "contradicted"),
        ("i voli mov.", "I want to move.", "I have an obligation to move.", "undetermined"),
        ("i posi mov.", "I can move.", "I have an obligation to move.", "undetermined"),
    ]),
    ("L2", "proposition_necessity", [
        ("deb uman mova.", "It is necessary that a person moves.", "The person's movement is necessary.", "entailed"),
        ("no deb uman mova.", "It is not necessary that a person moves.", "The person's movement is necessary.", "contradicted"),
        ("pos uman mova.", "It is possible that a person moves.", "The person's movement is necessary.", "undetermined"),
        ("lik uman mova.", "It is probable that a person moves.", "The person's movement is necessary.", "undetermined"),
    ]),
    ("L2", "belief_knowledge", [
        ("i kred u movu.", "I believe that you move.", "I believe that you move.", "entailed"),
        ("i no kred u movu.", "I do not believe that you move.", "I believe that you move.", "contradicted"),
        ("i sap u movu.", "I know that you move.", "I believe that you move.", "undetermined"),
        ("i vol u movu.", "I want you to move.", "I believe that you move.", "undetermined"),
    ]),
    ("L3", "conjunction_first", [
        ("i vidi akwaem e peli akwaem.", "I see water and I push water.", "I see water.", "entailed"),
        ("i no vidi akwaem e peli akwaem.", "I do not see water and I push water.", "I see water.", "contradicted"),
        ("i peli akwaem e traki akwaem.", "I push water and I pull water.", "I see water.", "undetermined"),
        ("i vidi akwaem o peli akwaem.", "I see water or I push water, inclusively.", "I see water.", "undetermined"),
    ]),
    ("L3", "conjunction_second", [
        ("i vidi akwaem e peli akwaem.", "I see water and I push water.", "I push water.", "entailed"),
        ("i vidi akwaem e no peli akwaem.", "I see water and I do not push water.", "I push water.", "contradicted"),
        ("i vidi akwaem e traki akwaem.", "I see water and I pull water.", "I push water.", "undetermined"),
        ("i vidi akwaem o peli akwaem.", "I see water or I push water, inclusively.", "I push water.", "undetermined"),
    ]),
    ("L3", "propositional_scope_negative", [
        ("deb uman no mova.", "It is necessary that a person does not move.", "It is necessary that a person does not move.", "entailed"),
        ("no deb uman mova.", "It is not necessary that a person moves.", "It is necessary that a person moves.", "contradicted"),
        ("pos uman mova.", "It is possible that a person moves.", "It is necessary that a person does not move.", "undetermined"),
        ("lik uman mova.", "It is probable that a person moves.", "It is necessary that a person does not move.", "undetermined"),
    ]),
    ("L3", "probability_value_scope", [
        ("lik setdek senim uman mova.", "The stated probability that a person moves is 70 percent.", "The stated probability is exactly 70 percent.", "entailed"),
        ("no lik setdek senim uman mova.", "It is not true that the stated probability that a person moves is 70 percent.", "The stated probability is exactly 70 percent.", "contradicted"),
        ("lik sirka setdek senim uman mova.", "The probability that a person moves is approximately 70 percent.", "The probability is exactly 70 percent.", "undetermined"),
        ("lik major setdek senim uman mova.", "The probability that a person moves exceeds 70 percent.", "The probability is exactly 70 percent.", "contradicted"),
    ]),
    ("L3", "quantitative_bounds", [
        ("lik no minor setdek senim uman mova.", "The probability of movement is at least 70 percent.", "The probability is at least 70 percent.", "entailed"),
        ("lik minor setdek senim uman mova.", "The probability of movement is less than 70 percent.", "The probability is at least 70 percent.", "contradicted"),
        ("lik sirka setdek senim uman mova.", "The probability of movement is approximately 70 percent.", "The probability is at least 70 percent.", "undetermined"),
        ("lik inter sesdek senim e setdek senim uman mova.", "The probability of movement lies between 60 and 70 percent, endpoint inclusion unspecified.", "The probability is at least 70 percent.", "undetermined"),
    ]),
    ("L4", "discourse_recall_polarity", [
        ("i vidi akwaem. i no peli akwaem. u traku akwaem.", "I see water. I do not push water. You pull water.", "I do not push water.", "entailed"),
        ("i vidi akwaem. i peli akwaem. u traku akwaem.", "I see water. I push water. You pull water.", "I do not push water.", "contradicted"),
        ("i vidi akwaem. u pelu akwaem. u traku akwaem.", "I see water. You push water. You pull water.", "I do not push water.", "undetermined"),
        ("i vidi akwaem. i traki akwaem. u traku akwaem.", "I see water. I pull water. You pull water.", "I do not push water.", "undetermined"),
    ]),
    ("L4", "discourse_tense", [
        ("i viddi akwaem. i no peli akwaem. u traku akwaem.", "I saw water. I do not push water. You pull water.", "I saw water.", "entailed"),
        ("i no viddi akwaem. i peli akwaem. u traku akwaem.", "I did not see water. I push water. You pull water.", "I saw water.", "contradicted"),
        ("i vidfi akwaem. i peli akwaem. u traku akwaem.", "I will see water. I push water. You pull water.", "I saw water.", "undetermined"),
        ("i vidi akwaem. i peli akwaem. u traku akwaem.", "I see water. I push water. You pull water.", "I saw water.", "undetermined"),
    ]),
    ("L4", "discourse_modal_actuality", [
        ("i tenti mov. i movi. u vidu akwaem.", "I attempt to move. I move. You see water.", "I move.", "entailed"),
        ("i tenti mov. i no movi. u vidu akwaem.", "I attempt to move. I do not move. You see water.", "I move.", "contradicted"),
        ("i tenti mov. u vidu akwaem. u traku akwaem.", "I attempt to move. You see water. You pull water.", "I move.", "undetermined"),
        ("i voli mov. u vidu akwaem. u traku akwaem.", "I want to move. You see water. You pull water.", "I move.", "undetermined"),
    ]),
    ("L4", "discourse_necessity_vs_action", [
        ("deb uman mova. uman mova. i vidi akwaem.", "It is necessary that a person moves. The person moves. I see water.", "The person moves.", "entailed"),
        ("deb uman mova. uman no mova. i vidi akwaem.", "It is necessary that a person moves. The person does not move. I see water.", "The person moves.", "contradicted"),
        ("deb uman mova. i vidi akwaem. u traku akwaem.", "It is necessary that a person moves. I see water. You pull water.", "The person moves.", "undetermined"),
        ("pos uman mova. i vidi akwaem. u traku akwaem.", "It is possible that a person moves. I see water. You pull water.", "The person moves.", "undetermined"),
    ]),
    ("L4", "discourse_probability_hyperbole", [
        ("lik bissen senim uman mova. i vidi akwaem. u traku akwaem.", "The stated likelihood of movement is 200 percent. I see water. You pull water.", "The claimed likelihood is 200 percent.", "entailed"),
        ("no lik bissen senim uman mova. i vidi akwaem. u traku akwaem.", "It is not true that the stated likelihood of movement is 200 percent. I see water. You pull water.", "The claimed likelihood is 200 percent.", "contradicted"),
        ("lik setdek senim uman mova. i vidi akwaem. u traku akwaem.", "The stated likelihood of movement is 70 percent. I see water. You pull water.", "The claimed likelihood is 200 percent.", "contradicted"),
        ("lik sirka bissen senim uman mova. i vidi akwaem. u traku akwaem.", "The stated likelihood of movement is approximately 200 percent. I see water. You pull water.", "The claimed likelihood is exactly 200 percent.", "undetermined"),
    ]),
]

def build() -> list[dict]:
    from formalization.core import Unisermo
    lang = Unisermo()
    assert len(GROUPS) == 20
    rows = []
    for index, (level, name, examples) in enumerate(GROUPS):
        assert len(examples) == 4
        level_index = index % 5
        split = "holdout" if level_index == 4 else "development"
        for variant, (unisermo, english, hypothesis, gold) in enumerate(examples):
            clauses = [x.strip() for x in unisermo.split(".") if x.strip()]
            for clause in clauses:
                try:
                    lang.parse_sentence(clause + ".")  # structural validation ONLY
                except ValueError as exc:
                    raise ValueError(f"UCUB G{index+1:02d} variant {variant+1}: {clause!r}: {exc}") from exc
            assert gold in LABELS
            assert len([x for x in english.split(".") if x.strip()]) == len(clauses)
            rows.append({
                "id": f"UCUB-{index+1:02d}-{variant+1}",
                "group": f"G{index+1:02d}",
                "level": level, "family": name, "split": split,
                "unisermo": unisermo, "english": english,
                "hypothesis": hypothesis, "gold": gold,
                "syntax": "parser_verified",
                "semantic_review": "author_draft_pending_independent_review",
                "english_review": "draft_pending_independent_review",
            })
    assert len(rows) == 80 and len({r["id"] for r in rows}) == 80
    assert sum(r["split"] == "holdout" for r in rows) == 16
    assert all(sum(r["level"] == lev for r in rows) == 20 for lev in ("L1","L2","L3","L4"))
    return rows

def render() -> tuple[str,str]:
    rows = build()
    serialized = "".join(json.dumps(r, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n" for r in rows)
    manifest = {
        "schema": "unisermo/ucub-001@1",
        "status": "draft_pending_independent_semantic_review",
        "suite": "UCUB-001",
        "total": len(rows), "development": 64, "holdout": 16,
        "groups": 20, "levels": {lev: 20 for lev in ("L1","L2","L3","L4")},
        "corpus_sha256": hashlib.sha256(serialized.encode()).hexdigest(),
        "grouping": "four contrasts per group; whole groups held out",
        "holdout_group_ids": [f"G{i:02d}" for i in (5,10,15,20)],
        "gold_provenance": "manually authored contrast templates, never parser-derived",
        "english_controls": "draft, not independently validated",
    }
    return serialized, json.dumps(manifest, indent=2, sort_keys=True) + "\n"

def main():
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("--check",action="store_true")
    opts=p.parse_args()
    corpus,manifest=render()
    if opts.check:
        if not CORPUS.exists() or CORPUS.read_text() != corpus: raise SystemExit("UCUB corpus out of sync")
        if not MANIFEST.exists() or MANIFEST.read_text() != manifest: raise SystemExit("UCUB manifest out of sync")
    else:
        CORPUS.write_text(corpus)
        MANIFEST.write_text(manifest)
    print("UCUB-001: 80 parser-verified drafts; independent semantic review pending")

if __name__=="__main__":
    main()
