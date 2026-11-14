"""Ratified bound memor family and its separations from knowledge phase verbs."""
import unittest
from formalization.core import Unisermo


class MnemonicFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = Unisermo()

    def test_bound_root_is_not_independent_verb_or_noun(self):
        self.assertIn("memor", self.u.lexicon)
        self.assertEqual(self.u.lexicon["memor"]["categories"], ["semantic_root"])
        self.assertNotIn("memor", self.u.verbs)
        self.assertNotIn("memor", self.u.nouns)
        self.assertIsNone(self.u.parse_derivation("memor"))
        self.assertEqual(self.u.analyze_word("memori")["analyses"], [])

    def test_family_has_four_distinct_typed_operations(self):
        expected = {
            "admemor": ("ad", "mnemonic_encode"),
            "inmemor": ("in", "mnemonic_retain"),
            "dememor": ("de", "mnemonic_lose_trace"),
            "rememor": ("re", "mnemonic_retrieve"),
        }
        for lemma, (prefix, operation) in expected.items():
            with self.subTest(lemma=lemma):
                d = self.u.parse_derivation(lemma)
                self.assertIsNotNone(d)
                self.assertEqual(d["base"], "memor")
                self.assertEqual(d["affix"], prefix)
                self.assertEqual(d["operation"], operation)
                self.assertEqual(d["category"], "verb")
                self.assertEqual(d["status"], "productive_from_confirmed")
                surface = lemma + "i"
                clause = self.u.parse_sentence(surface + " konem")
                self.assertEqual(clause["predicate"]["lemma"], lemma)
                self.assertEqual(clause["object"]["lemma"], "kon")
                self.assertEqual(clause["valency"],
                                 self.u.valency["mnemonic"]["frames"][lemma]["id"])
                self.assertEqual(self.u.valency_evidence(lemma)["family"], "mnemonic")
                with self.assertRaises(ValueError):
                    self.u.parse_sentence(surface)
                with self.assertRaises(ValueError):
                    self.u.parse_sentence(surface + " konem umande")

    def test_memory_domain_noun_and_cases(self):
        d = self.u.parse_derivation("memoria")
        self.assertEqual((d["base"], d["category"], d["operation"]),
                         ("memor", "noun", "mnemonic_domain"))
        for case, suffix in (("nominative", ""), ("accusative", "em"),
                             ("locative", "in"), ("ablative", "de")):
            with self.subTest(case=case):
                surface = self.u.generate_noun("memoria", case)
                self.assertEqual(surface, "memoria" + suffix)
                assert any(a["kind"] == "nominal_case" and a["case"] == case
                           for a in self.u.analyze_word(surface)["analyses"])

    def test_mnemonic_recall_does_not_override_knowledge_phase(self):
        recall = self.u.parse_derivation("rememor")
        regain_knowledge = self.u.parse_derivation("resap")
        self.assertEqual(recall["operation"], "mnemonic_retrieve")
        self.assertEqual(regain_knowledge["operation"], "phase_resume")
        self.assertTrue(self.u.valency["mnemonic"]["frames"]["rememor"]["requires_retained_trace"])
        self.assertFalse(self.u.valency["mnemonic"]["frames"]["rememor"]["entails_deletion"])
        self.assertFalse(self.u.valency["mnemonic"]["frames"]["rememor"]["entails_new_learning"])

    def test_no_general_nonverbal_phase_rule_or_unlimited_stacking(self):
        for invalid in ("adkon", "dekon", "rekon", "rememoria",
                        "admemoria", "rememormemor", "dememoria"):
            with self.subTest(invalid=invalid):
                self.assertIsNone(self.u.parse_derivation(invalid))


if __name__ == "__main__":
    unittest.main()
