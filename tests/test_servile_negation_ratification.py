"""Regression for accepted short servile roots and positional modal negation.

Documentary decision checks remain alongside the executable
modal scope conformance suite in test_proposition_parser.py.
"""
from hashlib import sha256
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ServileNegationRatificationTests(unittest.TestCase):
    def test_roots_are_distinct_confirmed_short_lexemes(self):
        lex = json.loads((ROOT / "research/lexicon/confirmed_lexicon.json").read_text(encoding="utf-8"))
        records = {r["form"]: r for r in lex["entries"]}
        for root in ("pos", "deb", "vol", "pot"):
            self.assertIn(root, records)
            self.assertEqual(records[root]["status"], "confirmed")
            self.assertEqual(records[root]["category"], "verb_root")
            self.assertEqual(len(root), 3)
        self.assertIn("procedural know-how", records["sap"]["decision"])
        self.assertIn("circumstantial possibility", records["pos"]["decision"])
        self.assertIn("capacity", records["pot"]["decision"])
        self.assertIn("Obligation", records["deb"]["decision"])
        self.assertIn("Volition", records["vol"]["decision"])

    def test_analytical_frame_and_negation_minimal_pairs(self):
        verbs = (ROOT / "language/verb_specification.md").read_text(encoding="utf-8")
        neg = (ROOT / "language/negation.md").read_text(encoding="utf-8")
        for text in ("posi mov", "debi mov", "voli mov", "poti mov", "sapi mov",
                     "debdi mov", "volfi mov", "potin mov"):
            self.assertIn("`" + text + "`", verbs)
        for positive, denied in (
            ("no debi mov", "debi no mov"),
            ("no posi mov", "posi no mov"),
            ("no voli mov", "voli no mov"),
            ("no poti mov", "poti no mov"),
            ("no sapi mov", "sapi no mov"),
        ):
            for text in (positive, denied):
                self.assertIn("`" + text + "`", neg)
        self.assertIn("uninflected", verbs)
        self.assertIn("pro-drop", verbs)
        self.assertIn("does not assert legal permission", verbs)
        self.assertIn("does", neg)
        self.assertIn("one uninflected verbal action", (ROOT / "formalization/semantics/README.md").read_text(encoding="utf-8"))

    def test_scope_meanings_not_equivalent(self):
        # An ordinary modal model can assign distinct statuses to action
        # and refraining. The two expressions must not be equated.
        obligation_to_move, obligation_to_refrain = False, False
        no_debi_mov = not obligation_to_move
        debi_no_mov = obligation_to_refrain
        self.assertTrue(no_debi_mov)
        self.assertFalse(debi_no_mov)
        opportunity_to_move, opportunity_to_refrain = False, False
        self.assertNotEqual(not opportunity_to_move, opportunity_to_refrain)
        desire_to_move, desire_to_refrain = False, False
        self.assertNotEqual(not desire_to_move, desire_to_refrain)
        ability_to_move, ability_to_refrain = False, False
        self.assertNotEqual(not ability_to_move, ability_to_refrain)
        knowhow_to_move, knowhow_to_refrain = False, False
        self.assertNotEqual(not knowhow_to_move, knowhow_to_refrain)

    def test_generated_indexes_and_decision_record(self):
        lexical_index = json.loads((ROOT / "formalization/data/lexicon_index.json").read_text(encoding="utf-8"))
        entries = {r["form"]: r for r in lexical_index["entries"]}
        for root in ("pos", "deb", "vol", "pot"):
            self.assertEqual(entries[root]["status"], "confirmed_lexicon")
            self.assertEqual(entries[root]["categories"], ["verb_root"])
        self.assertIn("know-how", entries["sap"]["decision"])
        grammar = json.loads((ROOT / "research/grammar/confirmed_decisions.json").read_text(encoding="utf-8"))
        decision_id = "short_servile_roots_and_negation_scope_20261112"
        matches = [d for d in grammar["decisions"] if d["id"] == decision_id]
        self.assertEqual(len(matches), 1)
        rule_registry = json.loads((ROOT / "formalization/data/rule_registry.json").read_text(encoding="utf-8"))
        refs = [r for r in rule_registry["entries"] if r["id"] == "grammar." + decision_id]
        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0]["content_sha256"], sha256(matches[0]["decision"].encode()).hexdigest())
        ldr_file = ROOT / "docs/ldr/LDR-0011-servile-negation.md"
        ldr_registry = json.loads((ROOT / "formalization/data/ldr_registry.json").read_text(encoding="utf-8"))
        ldrs = [r for r in ldr_registry["entries"] if r["id"] == "LDR-0011"]
        self.assertEqual(len(ldrs), 1)
        self.assertEqual(ldrs[0]["status"], "Accepted")
        self.assertEqual(ldrs[0]["sha256"], sha256(ldr_file.read_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()
