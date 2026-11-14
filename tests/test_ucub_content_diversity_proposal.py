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


class CommunicativeFeasibilityResearchTests(unittest.TestCase):
    def test_audit_is_research_only_and_aligned_to_36_targets(self):
        path = ROOT / "benchmarks" / "ucub001" / "proposals" / "communicative_diversity_36_feasibility_audit.json"
        audit = json.loads(path.read_text(encoding="utf-8"))
        targets = json.loads(SOURCE.read_text(encoding="utf-8"))
        self.assertEqual(audit["status"], "research_only_unratified_static_audit")
        self.assertEqual({x["id"] for x in audit["cases"]},
                         {x["id"] for x in targets["cases"]})
        self.assertEqual(len(audit["cases"]), 36)
        for entry in audit["cases"]:
            self.assertIs(entry["parser_executed"], False)
            self.assertTrue(entry["reason_it"])
            self.assertTrue(entry["next_action_it"])
            self.assertIn(entry["grammar_audit"],
                          ("documented", "needs_semantic_review", "requires_design"))

    def test_temporal_contrast_research_cannot_be_misreported_as_language(self):
        path = ROOT / "benchmarks" / "ucub001" / "proposals" / "temporal_contrast_research_14.json"
        proposal = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(proposal["status"], "research_draft_not_ratified")
        self.assertEqual(proposal["case_count"], 14)
        self.assertEqual(len(proposal["cases"]), 14)
        self.assertEqual(len({x["id"] for x in proposal["cases"]}), 14)
        for entry in proposal["cases"]:
            self.assertTrue(entry["meaning_it"])
            self.assertTrue(entry["intended_semantics_en"])
            self.assertTrue(entry["do_not_infer_en"])
            self.assertIsNone(entry["unisermo"])
            self.assertIs(entry["parser_verified"], False)
            self.assertIs(entry["benchmark_admitted"], False)
            self.assertEqual(entry["independent_semantic_review"], "not_started")

if __name__ == "__main__":
    unittest.main()
