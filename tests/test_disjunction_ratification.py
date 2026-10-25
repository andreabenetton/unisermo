"""Documentary regression for ratified inclusive and n-ary exclusive disjunction."""
import json
import unittest
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DisjunctionRatificationTests(unittest.TestCase):
    def test_normative_examples(self):
        spec = (ROOT / "language/word_order.md").read_text(encoding="utf-8")
        for fragment in ("P o Q", "o P o Q", "o P o Q o R", "o P o Q e R", "o P o Q lim e R"):
            self.assertIn(fragment, spec)
        self.assertIn("not** iterated binary XOR", spec)
        self.assertIn("exactly one", spec)

    def test_registered_decision_and_checksum(self):
        grammar = json.loads((ROOT / "research/grammar/confirmed_decisions.json").read_text(encoding="utf-8"))
        records = [d for d in grammar["decisions"] if d["id"] == "disjunction_inclusive_exclusive_initial_o_20261025"]
        self.assertEqual(len(records), 1)
        registry = json.loads((ROOT / "formalization/data/rule_registry.json").read_text(encoding="utf-8"))
        refs = [e for e in registry["entries"] if e["id"] == "grammar.disjunction_inclusive_exclusive_initial_o_20261025"]
        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0]["content_sha256"], sha256(records[0]["decision"].encode()).hexdigest())


if __name__ == "__main__":
    unittest.main()
