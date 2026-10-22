import copy
import json
import math
import unittest
from pathlib import Path

from benchmarks.modern_evidence import measure, validate

ROOT = Path(__file__).resolve().parents[1]
SEED = json.loads((ROOT / "research/lexicon/modern-form-seeds.json").read_text(encoding="utf-8"))
MORPH = json.loads((ROOT / "formalization/data/morphology.json").read_text(encoding="utf-8"))
ROOTS = {x["form"] for x in json.loads(
    (ROOT / "formalization/data/lexicon_index.json").read_text(encoding="utf-8")
)["entries"] if x["status"] == "confirmed_lexicon"}


class ModernEvidenceTests(unittest.TestCase):
    def test_current_seeds_validate(self):
        validate(SEED, MORPH["alphabet"], ROOTS)
        self.assertEqual(len(SEED["concepts"]), 4)
        self.assertEqual(sum(len(x["modern"]) for x in SEED["concepts"]), 32)

    def test_no_synthetic_recognition_or_concept_frequency(self):
        result = measure(SEED, "test-digest", lambda form, lang: 4.25, "test-provider")
        self.assertEqual(result["source_seed_sha256"], "test-digest")
        self.assertTrue(all(x["concept_frequency"] is None for x in result["concepts"]))
        self.assertTrue(all(x["population_weighted_recognition"] is None for x in result["concepts"]))
        self.assertTrue(all(o["spoken_recognizability"] is None
                            and o["written_recognizability"] is None
                            and not o["is_concept_frequency"]
                            for x in result["concepts"] for o in x["modern"]))

    def test_case_folding_duplicate_is_rejected(self):
        altered = copy.deepcopy(SEED)
        altered["concepts"][0]["modern"].append(copy.deepcopy(altered["concepts"][0]["modern"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate modern form"):
            validate(altered, MORPH["alphabet"], ROOTS)

    def test_unearned_semantic_approval_is_rejected(self):
        altered = copy.deepcopy(SEED)
        altered["concepts"][0]["modern"][0]["modern_sense_review"] = "verified"
        with self.assertRaisesRegex(ValueError, "approval"):
            validate(altered, MORPH["alphabet"], ROOTS)

    def test_frequency_provider_must_return_finite_nonnegative(self):
        for bad in (float("nan"), float("inf"), -1.0):
            with self.subTest(bad=bad):
                with self.assertRaisesRegex(ValueError, "invalid frequency"):
                    measure(SEED, "test", lambda form, lang: bad, "fake")

    def test_zero_is_censored_not_absence(self):
        result = measure(SEED, "test", lambda form, lang: 0, "fake")
        first = result["concepts"][0]["modern"][0]
        self.assertEqual(first["corpus_coverage"], "below_threshold_or_unobserved")

    def test_noncognate_translation_is_kept_distinct(self):
        result = measure(SEED, "test", lambda form, lang: 3.0, "fake")
        english_say = [x for x in result["concepts"][0]["modern"] if x["form"] == "say"][0]
        self.assertEqual(english_say["comparison_role"], "translation_candidate")
        english_dictate = [x for x in result["concepts"][0]["modern"] if x["form"] == "dictate"][0]
        self.assertEqual(english_dictate["comparison_role"], "related_family_not_equivalent")


if __name__ == "__main__":
    unittest.main()
