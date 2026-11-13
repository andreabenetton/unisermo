"""Ratified universal numerical relations (LDR-0027)."""
import unittest
from formalization.core import Unisermo


class QuantitativeRelationsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def test_six_comparisons(self):
        cases = {
            "ekwal setdek": "equal_to",
            "major setdek": "greater_than",
            "minor setdek": "less_than",
            "no minor setdek": "greater_than_or_equal",
            "no major setdek": "less_than_or_equal",
            "no ekwal setdek": "not_equal_to",
        }
        for surface, expected in cases.items():
            with self.subTest(surface=surface):
                node = self.lang.parse_quantitative_expression(surface)
                self.assertEqual(node["kind"], "quantitative_comparison")
                self.assertEqual(node["relation"], expected)
                self.assertEqual(node["value"]["value"], 70)

    def test_approximation_interval_and_fractions(self):
        approx = self.lang.parse_quantitative_expression("sirka setdek")
        self.assertEqual(approx["kind"], "quantitative_approximation")
        self.assertEqual(approx["value"]["value"], 70)
        self.assertEqual(approx["tolerance"], "contextual")
        interval = self.lang.parse_quantitative_expression("inter sesdek e setdek")
        self.assertEqual(interval["kind"], "quantitative_interval")
        self.assertEqual(interval["lower"]["value"], 60)
        self.assertEqual(interval["upper"]["value"], 70)
        self.assertIsNone(interval["inclusive"])
        frac = self.lang.parse_quantitative_expression("inter sesdek senim e setdek senim")
        self.assertEqual(frac["lower"]["numerator"], 60)
        self.assertEqual(frac["upper"]["denominator"], 100)
        self.assertEqual(self.lang.parse_quantitative_expression("sirka kin terim")["value"]["numerator"], 5)

    def test_probability_attachments_use_one_general_grammar(self):
        for sentence, kind in (
            ("lik sirka setdek senim uman mova", "quantitative_approximation"),
            ("lik major setdek senim uman mova", "quantitative_comparison"),
            ("lik no minor setdek senim uman mova", "quantitative_comparison"),
            ("lik inter sesdek senim e setdek senim uman mova", "quantitative_interval"),
            ("lik sirka bissen senim uman mova", "quantitative_approximation"),
        ):
            with self.subTest(sentence=sentence):
                ast = self.lang.parse_sentence(sentence)
                self.assertEqual(ast["kind"], "propositional_degree_property")
                self.assertEqual(ast["numeric_measure"]["kind"], kind)
                self.assertEqual(ast["operand"]["predicate"]["lemma"], "mov")
        a = self.lang.parse_sentence("lik inter sesdek senim e setdek senim uman mova e vida")
        self.assertEqual(a["kind"], "propositional_degree_property")
        self.assertEqual(a["operand"]["kind"], "coordination")
        b = self.lang.parse_sentence("lik inter sesdek senim e setdek senim uman mova lim e vida")
        self.assertEqual(b["kind"], "coordination")
        self.assertEqual(b["left"]["kind"], "propositional_degree_property")

    def test_quantified_nominal_subjects(self):
        cases = (
            ("sirka setdek uman movan", "quantitative_approximation"),
            ("no minor setdek uman movan", "quantitative_comparison"),
            ("inter sesdek e setdek uman movan", "quantitative_interval"),
        )
        for sentence, kind in cases:
            with self.subTest(sentence=sentence):
                tree = self.lang.parse_sentence(sentence)
                self.assertEqual(tree["subject"]["quantitative_constraint"]["kind"], kind)
        ordinary = self.lang.parse_sentence("lik setdek uman movan")
        self.assertIsNone(ordinary["numeric_measure"])
        self.assertEqual(ordinary["operand"]["subject"]["numerical_value"], 70)

    def test_invalid_structure_not_guessed(self):
        for value in ("sirka", "inter dek e", "inter dek setdek", "major",
                      "no sirka setdek", "major badvalue",
                      "inter setdek e setdek e terdek",
                      "sirka major setdek"):
            with self.subTest(value=value):
                self.assertIsNone(self.lang.parse_quantitative_expression(value))
        for value in ("lik sirka uman mova", "lik inter sesdek e uman mova",
                      "lik no minor uman mova",
                      "lik mult sirka setdek senim uman mova"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    self.lang.parse_sentence(value)


if __name__ == "__main__":
    unittest.main()
