"""Research-only checks for UCUB diverse communication target proposal.

No proposed Italian target here is a ratified Unisermo expression.
"""
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "benchmarks" / "ucub001" / "proposals" / "communicative_diversity_36.json"

class CommunicativeDiversityProposalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(SOURCE.read_text(encoding="utf-8"))

    def test_12_subject_areas_three_natural_targets_each(self):
        d = self.data
        self.assertEqual(d["status"], "research_draft_not_ratified_no_unisermo_translations")
        self.assertTrue(d["development_only"])
        self.assertEqual(len(d["cases"]), 36)
        self.assertEqual(d["case_count"], 36)
        self.assertEqual(d["domain_count"], 12)
        histogram = Counter(x["domain"] for x in d["cases"])
        self.assertEqual(len(histogram), 12)
        self.assertTrue(all(v == 3 for v in histogram.values()))
        self.assertEqual(len({x["meaning_it"] for x in d["cases"]}), 36)
        self.assertEqual(len({x["id"] for x in d["cases"]}), 36)

    def test_no_unratified_unisermo_is_leaked_as_canonical(self):
        for case in self.data["cases"]:
            self.assertIsNone(case["unisermo"])
            self.assertFalse(case["parser_verified"])
            self.assertEqual(case["semantic_review"], "not_started")
            self.assertTrue(case["do_not_publish_as_language"])
            self.assertTrue(case["meaning_it"].strip())
            self.assertTrue(case["lexicon_and_grammar_gaps_to_check"].strip())
            self.assertIn(case["target_level"], ("L1","L2","L3","L4"))

if __name__ == "__main__":
    unittest.main()
