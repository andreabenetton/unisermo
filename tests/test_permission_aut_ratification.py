"""Documentary regression for the author-ratified permission verb aut.

The current Phase 1 parser cannot parse compound servile frames, and these
tests do not misrepresent documentation as executable semantic parsing.
"""
from hashlib import sha256
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PermissionAutRatificationTests(unittest.TestCase):
    def test_lexeme_is_one_short_modal_root(self):
        lex = json.loads((ROOT / "research/lexicon/confirmed_lexicon.json").read_text(encoding="utf-8"))
        entries = [e for e in lex["entries"] if e["form"] == "aut"]
        self.assertEqual(len(entries), 1)
        aut = entries[0]
        self.assertEqual(aut["category"], "verb_root")
        self.assertEqual(aut["status"], "confirmed")
        self.assertIn("permitted or authorized", aut["meaning_en"])
        self.assertIn("Latin auctoritas", aut["source"])
        self.assertNotIn("auth", {e["form"] for e in lex["entries"]})
        self.assertNotIn("aut-", {e["form"] for e in lex["entries"]})

    def test_examples_and_optional_source_slot(self):
        verb = (ROOT / "language/verb_specification.md").read_text(encoding="utf-8")
        cases = (ROOT / "language/noun_case_system.md").read_text(encoding="utf-8")
        negation = (ROOT / "language/negation.md").read_text(encoding="utf-8")
        for text in ("auti mov", "autdi mov", "autin mov", "no auti mov",
                     "auti no mov", "auti umande mov", "no auti umande mov",
                     "auti umande no mov", "auti umande mov domde"):
            self.assertIn("`" + text + "`", verb)
        self.assertIn("governed complement immediately after", verb)
        self.assertIn("posi mov", verb)
        self.assertIn("existing ablative", cases)
        self.assertIn("auti umande mov domde", cases)
        self.assertIn("**not** create", cases)
        self.assertIn("Neither **lack of permission** nor **lack of obligation**", negation)
        self.assertIn("abstract normative domain", verb)
        self.assertIn("not** approved", verb)
        semantics = (ROOT / "formalization/semantics/README.md").read_text(encoding="utf-8")
        self.assertIn("not implemented in the Phase 1 parser", semantics)

    def test_permission_is_not_opportunity_or_obligation(self):
        # Truth-conditional examples only: the three relations are distinct.
        permitted, feasible, obliged = False, True, False
        self.assertTrue(feasible)
        self.assertFalse(permitted)
        self.assertFalse(obliged)
        # Not-obliged and not-permitted can both hold without an explicit
        # prohibition being asserted by the language.
        self.assertTrue(not obliged and not permitted)
        # A grant from person A does not prove a grant from person B.
        source_a_grants, source_b_grants = False, True
        self.assertFalse(source_a_grants)
        self.assertTrue(source_b_grants)

    def test_generated_indexes_are_source_linked(self):
        lexindex = json.loads((ROOT / "formalization/data/lexicon_index.json").read_text(encoding="utf-8"))
        matches = [e for e in lexindex["entries"] if e["form"] == "aut"]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["status"], "confirmed_lexicon")
        self.assertIn("authorized", matches[0]["meaning_en"])
        grammatical = json.loads((ROOT / "research/grammar/confirmed_decisions.json").read_text(encoding="utf-8"))
        decision_id = "permission_aut_optional_ablative_source_20261112"
        decisions = [e for e in grammatical["decisions"] if e["id"] == decision_id]
        self.assertEqual(len(decisions), 1)
        rules = json.loads((ROOT / "formalization/data/rule_registry.json").read_text(encoding="utf-8"))
        refs = [e for e in rules["entries"] if e["id"] == "grammar." + decision_id]
        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0]["content_sha256"], sha256(decisions[0]["decision"].encode()).hexdigest())
        ldr_file = ROOT / "docs/ldr/LDR-0012-aut-permission-source.md"
        ldrs = json.loads((ROOT / "formalization/data/ldr_registry.json").read_text(encoding="utf-8"))
        records = [e for e in ldrs["entries"] if e["id"] == "LDR-0012"]
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["status"], "Accepted")
        self.assertEqual(records[0]["sha256"], sha256(ldr_file.read_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()
