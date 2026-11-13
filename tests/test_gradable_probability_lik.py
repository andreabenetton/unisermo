"""Ratified LDR-0025: one gradable probability property lik over finite P."""
import unittest
from formalization.core import Unisermo

class GradableProbabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def test_confirmed_root(self):
        entry = self.lang.lexicon["lik"]
        self.assertEqual(entry["status"], "confirmed_lexicon")
        self.assertIn("probability", entry["meaning_en"])
        self.assertNotEqual(self.lang.lexicon["prob"]["meaning_en"], entry["meaning_en"])

    def test_qualitative_grades_one_scale(self):
        for degree in (None, "minu", "pok", "ase", "mult", "ekstrem", "suf"):
            with self.subTest(degree=degree):
                phrase = (degree + " " if degree else "") + "lik uman mova"
                ast = self.lang.parse_sentence(phrase)
                self.assertEqual(ast["kind"], "propositional_degree_property")
                self.assertEqual(ast["property"], "lik")
                self.assertEqual(ast["scale"], "probability")
                self.assertEqual(ast["degree"], degree)
                self.assertEqual(ast["threshold_relative"], degree == "suf")
                self.assertFalse(ast["numeric_threshold_defined"])
                self.assertIsNone(ast["numeric_measure"])
                self.assertFalse(ast["entails_operand_truth"])
                self.assertEqual(ast["operand"]["predicate"]["lemma"], "mov")

    def test_scope_and_other_properties(self):
        ast = self.lang.parse_sentence("mult lik uman mova e vida")
        self.assertEqual(ast["kind"], "propositional_degree_property")
        self.assertEqual(ast["operand"]["kind"], "coordination")
        self.assertEqual(self.lang.parse_sentence("pos uman mova")["interpretation"], "epistemic_possibility")
        self.assertEqual(self.lang.parse_sentence("deb uman mova")["interpretation"], "propositional_necessity")
        self.assertEqual(self.lang.parse_sentence("i kred uman mova")["interpretation"], "belief_that")

    def test_unratified_numeric_attachment_and_nested_semantics(self):
        for phrase in ("lik", "lik mov", "lik kin senim uman mova",
                       "pok lik", "lik pos uman mova",
                       "lik uman mova due vida",
                       "lik uman mova lim",
                       "lik uman mova lim vida"):
            with self.subTest(phrase=phrase):
                with self.assertRaises(ValueError):
                    self.lang.parse_sentence(phrase)

if __name__ == "__main__":
    unittest.main()
