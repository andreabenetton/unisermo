"""Source-level regression for ratified generalized alor subordinate grammar.

The Phase 1 parser intentionally has no compound subordinate implementation.
"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class GeneralizedAlorRatificationTests(unittest.TestCase):
    def test_canonical_scope_and_provenance(self):
        spec = (ROOT / "language/word_order.md").read_text(encoding="utf-8")
        decisions = json.loads((ROOT / "research/grammar/confirmed_decisions.json").read_text(encoding="utf-8"))
        entries = [d for d in decisions["decisions"] if d["id"] == "subordinate_scope_generalized_alor_20261025"]
        self.assertEqual(len(entries), 1)
        for fragment in (
            "se P alor Q", "etsi P alor Q", "etsise P alor Q", "eksese P alor Q",
            "se se P alor Q alor R", "se P alor se Q alor R",
            "se etsi P alor Q alor R",
        ):
            self.assertIn(fragment, spec)
        self.assertIn("2026-10-25", entries[0]["decision"])
        self.assertIn("The existing Phase 1 clause parser", spec)
        self.assertIn("not** yet recognize general compound", spec)

    def test_derived_rule_has_matching_source_hash(self):
        from hashlib import sha256
        decisions = json.loads((ROOT / "research/grammar/confirmed_decisions.json").read_text(encoding="utf-8"))
        entry = next(d for d in decisions["decisions"] if d["id"] == "subordinate_scope_generalized_alor_20261025")
        registry = json.loads((ROOT / "formalization/data/rule_registry.json").read_text(encoding="utf-8"))
        matches = [r for r in registry["entries"] if r["id"] == "grammar.subordinate_scope_generalized_alor_20261025"]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["content_sha256"], sha256(entry["decision"].encode()).hexdigest())


if __name__ == "__main__":
    unittest.main()
