"""Ratified LDR-0026: likelihood fraction AST and unrestricted hyperbolic values."""
import unittest

from formalization.core import Unisermo


class NumericLikelihoodTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def test_ratified_fraction_forms_without_probability_range_guard(self):
        samples = (
            ("lik nul senim uman mova", 0, 100),
            ("lik kin senim uman mova", 5, 100),
            ("lik uno bisim uman mova", 1, 2),
            ("lik setdek senim uman mova", 70, 100),
            ("lik sen senim uman mova", 100, 100),
            ("lik bissen senim uman mova", 200, 100),
            ("lik kin terim uman mova", 5, 3),
        )
        for sentence, numerator, denominator in samples:
            with self.subTest(sentence=sentence):
                tree = self.lang.parse_sentence(sentence)
                self.assertEqual(tree["kind"], "propositional_degree_property")
                self.assertEqual(tree["scale"], "probability")
                self.assertTrue(tree["numeric_threshold_defined"])
                self.assertEqual(tree["numeric_measure"]["kind"], "fraction")
                self.assertEqual(tree["numeric_measure"]["numerator"], numerator)
                self.assertEqual(tree["numeric_measure"]["denominator"], denominator)
                self.assertEqual(tree["numeric_measure"]["form"],
                                 " ".join(sentence.split()[1:3]))
                self.assertIsNone(tree["degree"])
                self.assertFalse(tree["entails_operand_truth"])

    def test_negation_has_distinct_positions(self):
        outer = self.lang.parse_sentence("no lik setdek senim uman mova")
        inner = self.lang.parse_sentence("lik setdek senim uman no mova")
        self.assertTrue(outer["negative"])
        self.assertFalse(outer["operand"]["negative"])
        self.assertFalse(inner["negative"])
        self.assertTrue(inner["operand"]["negative"])

    def test_lim_delimits_numeric_assessment(self):
        narrow = self.lang.parse_sentence("lik setdek senim uman mova lim e vida")
        wide = self.lang.parse_sentence("lik setdek senim uman mova e vida")
        self.assertEqual(narrow["kind"], "coordination")
        self.assertEqual(narrow["left"]["kind"], "propositional_degree_property")
        self.assertEqual(narrow["left"]["numeric_measure"]["numerator"], 70)
        self.assertEqual(narrow["right"]["kind"], "svo_clause")
        self.assertEqual(wide["kind"], "propositional_degree_property")
        self.assertEqual(wide["operand"]["kind"], "coordination")

    def test_quantity_of_subject_is_not_numeric_probability(self):
        clause = self.lang.parse_sentence("lik setdek uman mova")
        self.assertIsNone(clause["numeric_measure"])
        self.assertEqual(clause["kind"], "propositional_degree_property")

    def test_do_not_invent_unratified_numerical_constructions(self):
        for sentence in (
            "lik setdek senim",
            "mult lik setdek senim uman mova",
            "lik sen nulim uman mova",
            "lik kin unim uman mova",
            "lik setdek senim uman mova lim",
            "lik setdek senim uman mova due vida",
        ):
            with self.subTest(sentence=sentence):
                with self.assertRaises(ValueError):
                    self.lang.parse_sentence(sentence)


if __name__ == "__main__":
    unittest.main()
