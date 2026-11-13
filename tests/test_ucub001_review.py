"""UCUB-001: blind review protocol, synthetic reviewer fixtures, balanced plan.

No test fixture represents an actual human-reviewed case.
"""
from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from benchmarks.ucub001.review import (
    REVIEW_SCHEMA, make_packet, validate_review_file, summarize_review,
)
from benchmarks.ucub001.runner import (
    load_corpus, balanced_development_sample, prompt,
)


class UCUB001IndependentReviewProtocolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.manifest = load_corpus()

    def test_gold_blinded_in_both_review_packets(self):
        for stage in ("semantic", "equivalence"):
            for split, count in (("all", 80), ("development", 64), ("holdout", 16)):
                text, meta = make_packet(stage, split=split)
                cases = [json.loads(line) for line in text.splitlines()]
                self.assertEqual(len(cases), count)
                self.assertEqual(meta["count"], count)
                self.assertEqual(meta["corpus_sha256"], self.manifest["corpus_sha256"])
                self.assertEqual(meta["packet_sha256"], hashlib.sha256(text.encode()).hexdigest())
                self.assertEqual(meta["gold_visible"], False)
                self.assertEqual(meta["source_split_visible"], False)
                for item in cases:
                    self.assertEqual(
                        set(item),
                        {"id", "level", "unisermo", "hypothesis"}
                        | ({"draft_english"} if stage == "equivalence" else set()),
                    )
                    self.assertNotIn("gold", item)
                    self.assertNotIn("split", item)
                    if stage == "equivalence":
                        self.assertTrue(item["draft_english"])
        a, _ = make_packet("semantic")
        b, _ = make_packet("semantic")
        self.assertEqual(a, b)

    def test_gold_blind_paired_four_level_sampling(self):
        selected = balanced_development_sample(self.rows)
        again = balanced_development_sample(list(reversed(self.rows)))
        self.assertEqual({x["id"] for x in selected}, {x["id"] for x in again})
        self.assertEqual(len(selected), 16)
        self.assertNotIn("G01", {x["group"] for x in selected})
        self.assertTrue(all(x["split"] == "development" for x in selected))
        self.assertEqual(len({x["group"] for x in selected}), 4)
        for level in ("L1", "L2", "L3", "L4"):
            self.assertEqual(sum(x["level"] == level for x in selected), 4)
        all_answers = {arm: {prompt(r, arm)["id"] for r in selected}
                       for arm in ("cold", "lexicon", "grammar", "english")}
        self.assertEqual(len(set(map(frozenset, all_answers.values()))), 1)

    def synthetic_review(self, reviewer: str) -> dict:
        return {
            "schema": REVIEW_SCHEMA,
            "corpus_sha256": self.manifest["corpus_sha256"],
            "reviewer_id": reviewer,
            "review_method": "human",
            "independent_of_corpus_author": True,
            "reviewed_at_utc": "2099-01-01T00:00:00Z",
            "annotations": [
                {
                    "id": x["id"], "label": x["gold"],
                    "own_translation": "SYNTHETIC TEST FIXTURE: " + x["english"],
                    "english_equivalence": "equivalent",
                    "confidence": 5,
                    "rationale": "SYNTHETIC TEST FIXTURE: strict restatement",
                    "ambiguity": "",
                }
                for x in self.rows
            ]
        }

    def validate_fixture(self, d: dict) -> dict:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "review.json"
            path.write_text(json.dumps(d, indent=2), encoding="utf-8")
            return validate_review_file(
                path,
                expected_ids={x["id"] for x in self.rows},
                corpus_sha256=self.manifest["corpus_sha256"],
            )

    def test_review_shape_and_independence_attestation(self):
        form_a = self.synthetic_review("synthetic-tester-a")
        self.assertEqual(
            self.validate_fixture(form_a)["reviewer_id"], "synthetic-tester-a"
        )
        for edit in (
            lambda d: d.update({"corpus_sha256": "bad"}),
            lambda d: d.update({"review_method": "model"}),
            lambda d: d.update({"independent_of_corpus_author": False}),
            lambda d: d["annotations"].pop(),
            lambda d: d["annotations"][0].update({"label": "other"}),
            lambda d: d["annotations"][0].update({"own_translation": ""}),
            lambda d: d["annotations"][0].update({"confidence": 0}),
            lambda d: d["annotations"][1].update({"id": d["annotations"][0]["id"]}),
        ):
            candidate = copy.deepcopy(form_a)
            edit(candidate)
            with self.assertRaises(ValueError):
                self.validate_fixture(candidate)

    def test_agreement_is_not_automatic_final_certification(self):
        a = self.synthetic_review("synthetic-tester-a")
        b = self.synthetic_review("synthetic-tester-b")
        report = summarize_review(a, b, self.rows, self.manifest["corpus_sha256"])
        self.assertEqual(report["status"], "awaiting_formal_signoff")
        self.assertEqual(report["counts"]["agreed_draft_gold"], 80)
        self.assertEqual(report["human_independence"],
                         "self_attested_not_technically_verified")
        with self.assertRaises(ValueError):
            summarize_review(a, a, self.rows, self.manifest["corpus_sha256"])
        b["annotations"][0]["label"] = "contradicted"
        changed = summarize_review(a, b, self.rows, self.manifest["corpus_sha256"])
        self.assertEqual(changed["status"], "incomplete_or_disputed")
        self.assertEqual(changed["needs_adjudication"], 1)
        b["annotations"][0]["label"] = "undetermined"
        a["annotations"][0]["label"] = "undetermined"
        changed = summarize_review(a, b, self.rows, self.manifest["corpus_sha256"])
        self.assertEqual(changed["counts"]["agreed_but_draft_gold_disputed"], 1)
        self.assertEqual(changed["needs_adjudication"], 1)
        b["annotations"][0]["english_equivalence"] = "uncertain"
        changed = summarize_review(a, b, self.rows, self.manifest["corpus_sha256"])
        self.assertEqual(changed["counts"]["requires_adjudication"], 1)

    def test_curator_risks_are_flagged_not_changed_gold(self):
        path = Path(__file__).resolve().parents[1] / "benchmarks/ucub001/preaudit-flags.json"
        audit = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(audit["corpus_sha256"], self.manifest["corpus_sha256"])
        self.assertIn("nonindependent", audit["status"])
        ids = {x["id"] for x in self.rows}
        self.assertTrue(audit["flags"])
        for note in audit["flags"]:
            self.assertIn(note["severity"], ("medium", "high"))
            self.assertTrue(set(note["ids"]) <= ids)
            self.assertTrue(note["sources"])
            self.assertTrue(note["question"])


if __name__ == "__main__":
    unittest.main()
