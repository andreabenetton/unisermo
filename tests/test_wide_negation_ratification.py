"""Documentary checks for author-ratified no lim wide-scope negation.

The Phase 1 parser does not yet implement compound clauses; these are
source/logic regressions, not claims of executable clause parsing.
"""
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]


def exactly_one(*values):
    return sum(bool(v) for v in values) == 1


class WideNegationRatificationTests(unittest.TestCase):
    def test_old_local_no_preserved(self):
        source = (ROOT / "language/negation.md").read_text(encoding="utf-8")
        self.assertIn("`no` immediately precedes the verb or predicate", source)
        self.assertIn("`no vidi e movi`", source)
        self.assertIn("`no vidi ma movi`", source)
        self.assertIn("adversative relation", source)

    def test_wide_scope_examples_and_lim_boundaries(self):
        negation = (ROOT / "language/negation.md").read_text(encoding="utf-8")
        order = (ROOT / "language/word_order.md").read_text(encoding="utf-8")
        for phrase in (
            "no lim vidi e movi",
            "no lim vidi o movi",
            "no lim o vidi o movi",
            "no lim P e Q o R",
            "no lim P e Q lim o R",
        ):
            self.assertIn(phrase, negation)
        self.assertIn("no lim", order)
        self.assertIn("Bare `lim P`", negation)
        self.assertIn("Phase 1", negation)
        self.assertIn("not executable parser support", (ROOT / "formalization/semantics/README.md").read_text(encoding="utf-8"))

    def test_boolean_truth_conditions(self):
        local_and_wide_differ = False
        for p, q in product((False, True), repeat=2):
            local = (not p) and q
            wide_conjunction = not (p and q)
            local_and_wide_differ |= local != wide_conjunction
            self.assertEqual(not (p or q), (not p) and (not q))
            self.assertEqual(not exactly_one(p, q), exactly_one(not p, q))
        self.assertTrue(local_and_wide_differ)
        right_association_matters = False
        closing_boundary_matters = False
        for p, q, r in product((False, True), repeat=3):
            # `no lim P e Q o R` = NOT(P AND (Q OR R)).
            wide_right = not (p and (q or r))
            # A closing `lim` before `o` excludes R from the negation.
            closed = (not (p and q)) or r
            unclosed_left = not ((p and q) or r)
            right_association_matters |= wide_right != unclosed_left
            closing_boundary_matters |= wide_right != closed
            # Exactly-one and odd parity differ for three alternatives.
            self.assertEqual(not exactly_one(p, q, r), sum((p, q, r)) != 1)
        self.assertTrue(right_association_matters)
        self.assertTrue(closing_boundary_matters)
        self.assertTrue(not exactly_one(True, True, False))

    def test_source_and_generated_registry_are_synchronized(self):
        source = json.loads((ROOT / "research/grammar/confirmed_decisions.json").read_text(encoding="utf-8"))
        entry = next(d for d in source["decisions"] if d["id"] == "propositional_wide_negation_no_lim_20261112")
        registry = json.loads((ROOT / "formalization/data/rule_registry.json").read_text(encoding="utf-8"))
        key = "grammar.propositional_wide_negation_no_lim_20261112"
        matches = [d for d in registry["entries"] if d["id"] == key]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["content_sha256"], sha256(entry["decision"].encode()).hexdigest())

        path = ROOT / "docs/ldr/LDR-0010-wide-scope-negation.md"
        ldrindex = json.loads((ROOT / "formalization/data/ldr_registry.json").read_text(encoding="utf-8"))
        indexrow = next(d for d in ldrindex["entries"] if d["id"] == "LDR-0010")
        self.assertEqual(indexrow["status"], "Accepted")
        self.assertEqual(indexrow["sha256"], sha256(path.read_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()
