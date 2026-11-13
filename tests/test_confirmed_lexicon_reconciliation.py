"""Regression checks for the 2026-11-13 lexical reconciliation.

These checks read normative source data only. They do not replace the required
formalization build, parser tests, or independent semantic review.
"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "research/lexicon/confirmed_lexicon.json"
HISTORICAL = {"frat", "mil", "doktor", "student"}
CONFIRMED_EXISTING = {
    "ades", "admov", "bis", "dees", "demov", "es", "ines", "inmov",
    "jer", "ka", "mov", "no", "nul", "omni", "rees", "remov", "tot",
    "traes", "uno", "wi",
}
CONFIRMED_FROM_EXAMPLES = {
    "amik", "dom", "likwid", "multi", "san", "solid", "tan", "ter",
    "tes", "tik", "vid",
}


class ConfirmedLexiconSynchronizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads(DATA.read_text(encoding="utf8"))["entries"]
        cls.by_form = {entry["form"]: entry for entry in cls.entries}

    def test_no_duplicate_forms(self):
        self.assertEqual(len(self.entries), len(self.by_form))

    def test_confirmed_existing_and_example_forms(self):
        self.assertTrue(CONFIRMED_EXISTING <= self.by_form.keys())
        self.assertTrue(CONFIRMED_FROM_EXAMPLES <= self.by_form.keys())
        self.assertEqual(len(self.entries), 140)

    def test_historical_and_opaque_labels_not_confirmed(self):
        self.assertFalse(HISTORICAL & self.by_form.keys())

    def test_study_distinct_from_cognitive_verbs(self):
        self.assertEqual(self.by_form["stud"]["category"], "verb_root")
        self.assertEqual(self.by_form["stud"]["status"], "confirmed")
        for form in ("sap", "kap", "pens", "kurar", "dok"):
            self.assertIn(form, self.by_form)

    def test_agent_morphology_canonical_in_documentation(self):
        derivation = (ROOT / "language/derivation.md").read_text(encoding="utf8")
        for form in ("kuraror", "studor", "dokor"):
            self.assertIn(form, derivation)
        self.assertIn("person / agent", derivation)

    def test_demonstratives_follow_live_spec(self):
        docs = (ROOT / "language/demonstratives.md").read_text(encoding="utf8")
        for form in ("tik", "tes", "tan"):
            self.assertIn(form, docs)
            self.assertEqual(self.by_form[form]["category"], "demonstrative")


if __name__ == "__main__":
    unittest.main()
