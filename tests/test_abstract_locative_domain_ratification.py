"""Documentary regression for the accepted abstract-domain extension of -in.

The implementation does NOT claim semantic parsing of proposition-domain
scope. All checks are on the accepted normative documents, source-linked
indexes, and deliberately limited syntax.
"""
from pathlib import Path
from hashlib import sha256
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]


class AbstractDomainLocativeTests(unittest.TestCase):
    def test_one_locative_suffix_not_a_new_case(self):
        spec = (ROOT / "language/noun_case_system.md").read_text(encoding="utf-8")
        morph = json.loads((ROOT / "formalization/data/morphology.json").read_text(encoding="utf-8"))
        self.assertEqual(morph["nominal"]["case"]["locative"], "in")
        self.assertEqual(len(morph["nominal"]["case"]), 7)
        self.assertIn("physical or abstract domain", spec)
        self.assertIn("movi domin", spec)
        self.assertIn("domin movi", spec)
        self.assertIn("physical space", spec)
        for term in ("normative", "institutional", "disciplines",
                     "computational", "simulated"):
            self.assertIn(term, spec)
        self.assertIn("tem", spec)
        self.assertIn("due", spec)
        self.assertIn("mod", spec)

    def test_proposition_domain_and_local_event_attach_differently(self):
        spec = (ROOT / "language/noun_case_system.md").read_text(encoding="utf-8")
        order = (ROOT / "language/word_order.md").read_text(encoding="utf-8")
        for example in (
            "[NORMA]-in auti umande mov",
            "[NORMA]-in no auti umande mov",
            "[SISTEMA]-in faki",
            "[SIMULAZIONE]-in movi",
        ):
            self.assertIn(example, spec)
        self.assertIn("single simple proposition", spec)
        self.assertIn("left-peripheral", order)
        self.assertIn("movi domin", order)
        self.assertIn("domin movi", order)
        self.assertIn("fronting alone is insufficient", " ".join(order.split()))
        self.assertIn("position alone", spec)
        self.assertIn("placeholder", spec.lower())
        self.assertIn("unratified", spec.lower())
        self.assertIn("Phase 1 parser", spec)
        self.assertIn("not automatically", spec)

    def test_sources_not_domains_and_no_scope_leaks(self):
        verb = (ROOT / "language/verb_specification.md").read_text(encoding="utf-8")
        cases = (ROOT / "language/noun_case_system.md").read_text(encoding="utf-8")
        semantic = (ROOT / "formalization/semantics/README.md").read_text(encoding="utf-8")
        self.assertIn("[NORMA]-in auti umande mov", verb)
        self.assertIn("uman-de", verb)
        self.assertIn("normative domain", cases)
        self.assertIn("source", cases)
        self.assertIn("P e Q", cases)
        self.assertIn("temporal", cases)
        self.assertIn("tem", cases)
        self.assertIn("does **not**", semantic)
        self.assertIn("remain ambiguous", semantic)
        self.assertIn("not implemented", semantic.lower())

    def test_generated_indexes_and_ldr_hash(self):
        gram = json.loads((ROOT / "research/grammar/confirmed_decisions.json").read_text(encoding="utf-8"))
        key = "locative_in_abstract_domain_simple_proposition_20261112"
        record = [x for x in gram["decisions"] if x["id"] == key]
        self.assertEqual(len(record), 1)
        self.assertIn("existing locative suffix -in", record[0]["decision"])
        self.assertIn("fronting", record[0]["decision"].lower())
        rule = json.loads((ROOT / "formalization/data/rule_registry.json").read_text(encoding="utf-8"))
        entries = [x for x in rule["entries"] if x["id"] == "grammar." + key]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["content_sha256"], sha256(record[0]["decision"].encode()).hexdigest())
        ldr = ROOT / "docs/ldr/LDR-0013-abstract-domain-locative.md"
        ldrs = json.loads((ROOT / "formalization/data/ldr_registry.json").read_text(encoding="utf-8"))
        refs = [x for x in ldrs["entries"] if x["id"] == "LDR-0013"]
        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0]["status"], "Accepted")
        self.assertEqual(refs[0]["sha256"], sha256(ldr.read_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()
