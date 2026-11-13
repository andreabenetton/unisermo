"""UCUB-001 human equivalence review: one appearance per unique sentence.

This test does NOT certify any proposed Italian translation as correct.
"""
import json
import unittest
from collections import Counter
from pathlib import Path

from benchmarks.ucub001.runner import load_corpus


ROOT = Path(__file__).resolve().parents[1] / "benchmarks" / "ucub001"


class UniqueTranslationReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original, cls.source_manifest = load_corpus()
        cls.review = [json.loads(line) for line in
                      (ROOT / "unique_translation_review_63.jsonl").read_text(encoding="utf-8").splitlines()
                      if line.strip()]
        cls.audit_manifest = json.loads(
            (ROOT / "unique_translation_review_manifest.json").read_text(encoding="utf-8"))

    def test_exactly_63_unique_complete_sentences(self):
        self.assertEqual(len(self.review), 63)
        self.assertEqual(len({r["unisermo"] for r in self.review}), 63)
        self.assertEqual(len({r["id"] for r in self.review}), 63)
        self.assertTrue(all(r["meaning_it"].strip() for r in self.review))
        self.assertTrue(all(r["review_status"] == "pending_human_equivalence_check"
                            for r in self.review))
        self.assertEqual(Counter(r["level"] for r in self.review),
                         {"L1":14, "L2":16, "L3":14, "L4":19})

    def test_every_original_ucub_item_maps_to_one_translation_question(self):
        self.assertEqual(self.audit_manifest["source_sha256"],
                         self.source_manifest["corpus_sha256"])
        self.assertEqual(self.audit_manifest["source_cases"], 80)
        self.assertEqual(len(self.original), 80)
        by_phrase = {}
        for row in self.original:
            by_phrase.setdefault(row["unisermo"], []).append(row)
        self.assertEqual(len(by_phrase), 63)
        for example in self.review:
            source_rows = by_phrase[example["unisermo"]]
            self.assertEqual(example["id"], source_rows[0]["id"])
            self.assertEqual(example["level"], source_rows[0]["level"])
            self.assertEqual(example["source_english"], source_rows[0]["english"])
            self.assertEqual(example["source_ids"], [r["id"] for r in source_rows])
            self.assertEqual(example["english_variants"],
                             list(dict.fromkeys(r["english"] for r in source_rows)))

    def test_human_form_has_no_logic_labels_or_hypothesis(self):
        for row in self.review:
            self.assertEqual(set(row), {
                "id", "level", "unisermo", "meaning_it", "source_english",
                "english_variants", "source_ids", "review_status"
            })
            for banned in ("gold", "hypothesis", "entailment", "contradiction"):
                self.assertNotIn(banned, row)
        self.assertEqual(self.audit_manifest["source_hypothesis_gold_included"], False)
        self.assertEqual(self.audit_manifest["count"], 63)
        self.assertEqual(self.audit_manifest["stage"],
                         "proposed Italian meaning equivalence only, no entailment judgments")

    def test_each_level_has_a_single_known_tally_form(self):
        forms=self.audit_manifest["tally_forms"]
        self.assertEqual(forms, {
            "L1": "https://tally.so/r/DqkEyX",
            "L2": "https://tally.so/r/zEyRoZ",
            "L3": "https://tally.so/r/5XjgDv",
            "L4": "https://tally.so/r/dba41D"
        })


if __name__ == "__main__":
    unittest.main()
