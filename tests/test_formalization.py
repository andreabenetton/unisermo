#!/usr/bin/env python3
"""Standalone Phase 1 semantic-safety and traceability tests."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from formalization.core import Unisermo
from formalization.ldrs import load_ldrs


class FormalizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def test_complete_finite_paradigm(self):
        generated = {
            self.lang.generate_verb("dik", tense, aspect, person, number)
            for tense in ("present", "past", "future")
            for aspect in ("simple", "progressive", "perfect")
            for person in (1, 2, 3)
            for number in ("singular", "plural")
        }
        self.assertEqual(len(generated), 54)
        self.assertEqual(self.lang.generate_verb("dik", "past", "perfect"), "dikodi")

    def test_noun_case_and_allomorph(self):
        self.assertEqual(len({self.lang.generate_noun("dom", case) for case in self.lang.morph["nominal"]["case"]}), 7)
        self.assertEqual(self.lang.generate_noun("spets", "genitive"), "spetses")
        self.assertEqual(self.lang.generate_noun("dom", "accusative"), "domem")

    def test_ambiguity_preserved(self):
        analyses = self.lang.analyze_word("fakit")["analyses"]
        self.assertIn("participle", {a["kind"] for a in analyses})
        self.assertIn("nominal_case", {a["kind"] for a in analyses})

    def test_clause_subset(self):
        parsed = self.lang.parse_sentence("ka i no diki domem?")
        self.assertTrue(parsed["negative"])
        self.assertTrue(parsed["interrogative"])
        self.assertEqual(parsed["object"]["lemma"], "dom")
        self.assertEqual(self.lang.parse_sentence("uman dika domem")["predicate"]["person"], 3)
        with self.assertRaises(ValueError):
            self.lang.parse_sentence("u diki domem")  # pronoun/verb disagreement
        with self.assertRaises(ValueError):
            self.lang.parse_sentence("unrecognized random string")

    def test_lexical_attestation_not_ratification(self):
        idx = json.loads((ROOT / "formalization/data/lexicon_index.json").read_text())
        entries = {x["form"]: x for x in idx["entries"]}
        self.assertEqual(entries["spets"]["status"], "confirmed_lexicon")
        self.assertEqual(entries["dom"]["status"], "example_only")
        self.assertNotEqual(entries["mov"]["status"], "confirmed_lexicon")

    def test_decisions_not_auto_ratified(self):
        entries = load_ldrs()
        self.assertTrue({"LDR-0001", "LDR-0002", "LDR-0003", "LDR-0004"} <= {x["id"] for x in entries})
        self.assertEqual({x["id"]: x["status"] for x in entries}["LDR-0002"], "Experimental")
        self.assertEqual({x["id"]: x["status"] for x in entries}["LDR-0004"], "Proposed")

    def test_generated_indexes_in_sync(self):
        result = subprocess.run([sys.executable, "-m", "formalization", "build", "--check"],
                                cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
