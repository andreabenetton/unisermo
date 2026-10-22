import json
import unittest
from benchmarks.lexical_screen import audit, evaluate, accent_keys, protected_forms
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MORPH = json.loads((ROOT / "formalization/data/morphology.json").read_text())
LEXICON = json.loads((ROOT / "formalization/data/lexicon_index.json").read_text())["entries"]
REGISTER = json.loads((ROOT / "research/lexicon/candidate-register.json").read_text())

class LexicalScreenTests(unittest.TestCase):
    def test_inventory_rejects_source_c_and_h(self):
        self.assertFalse(audit("centr", "sentr", MORPH, LEXICON)["inventory_valid"])
        self.assertFalse(audit("human", "uman", MORPH, LEXICON)["inventory_valid"])

    def test_inventory_accepts_relevant_adaptations(self):
        self.assertTrue(audit("sentr", "sentr", MORPH, LEXICON)["inventory_valid"])
        self.assertTrue(audit("kentr", "sentr", MORPH, LEXICON)["inventory_valid"])

    def test_existing_other_lexeme_collision(self):
        res = audit("dik", "kurar", MORPH, LEXICON)
        self.assertIn("dik", res["exact_collisions"])

    def test_protected_forms(self):
        self.assertIn("i", protected_forms(MORPH))
        self.assertIn("no", audit("no", "kurar", MORPH, LEXICON)["exact_collisions"])

    def test_mergers_are_conservative(self):
        self.assertIn("pat", accent_keys("bad"))
        self.assertIn("wok", accent_keys("vok"))

    def test_dik_tik_demonstrative_accent_risk_is_exposed(self):
        # Current dik is preserved, but accepted d -> t accents can make
        # the high-value demonstrative tik acoustically identical.
        result = audit("dik", "dik", MORPH, LEXICON)
        self.assertIn("tik", result["accent_merger_risks"])
        self.assertIn("tik", result["critical_grammar_risks"])

    def test_register_is_auditable(self):
        output = evaluate(REGISTER, MORPH, LEXICON)
        self.assertEqual(output["status"], "research_only")
        self.assertEqual({x["candidate"] for x in output["results"]}, {"dik", "dir", "stru", "konstru", "kostru", "kurar", "sentr"})
        self.assertTrue(all(x["recognizability"] == "not_measured" for x in output["results"]))

if __name__ == "__main__":
    unittest.main()
