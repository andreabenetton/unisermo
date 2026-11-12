#!/usr/bin/env python3
"""Regression for ratified productive factor marker NUMfol."""
import random
import unittest

from formalization.core import Unisermo
from formalization.parser.numeral import MAX_CARDINAL


class MultiplicativeFactorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def assert_factor(self, value, form=None):
        written = self.lang.generate_multiplicative(value)
        self.assertEqual(written, (form if form is not None else
                                   self.lang.generate_numeral(value) + "fol"))
        parsed = self.lang.parse_multiplicative(written)
        self.assertIsNotNone(parsed, written)
        self.assertEqual(parsed["kind"], "multiplicative_factor")
        self.assertEqual(parsed["factor"], value)
        self.assertEqual(parsed["status"], "canonical_by_rule")
        recognized = [a for a in self.lang.analyze_word(written)["analyses"]
                      if a["kind"] == "multiplicative_factor"]
        self.assertEqual(len(recognized), 1)
        self.assertEqual(recognized[0]["factor"], value)

    def test_ratified_multiplicatives(self):
        for n, term in {
            1: "unofol", 2: "bisfol", 3: "terfol", 4: "forfol",
            5: "kinfol", 8: "otofol", 10: "dekfol",
            20: "bisdekfol", 100: "senfol", 321: "tersenbisdekunofol",
            1000: "milafol", 1000000: "megafol", 1000000000: "gigafol",
            MAX_CARDINAL: self.lang.generate_numeral(MAX_CARDINAL) + "fol",
        }.items():
            with self.subTest(n=n):
                self.assert_factor(n, term)

    def test_full_existing_numeral_domain_and_random_high_values(self):
        for n in range(1, 10000):
            self.assert_factor(n)
        rng = random.Random(20261024)
        for _ in range(1000):
            self.assert_factor(rng.randint(1, MAX_CARDINAL))

    def test_reject_unapproved_or_noncanonical(self):
        for word in ("", "fol", "mul", "bismul", "termul", "formul",
                     "nulfol", "unfol", "otfol", "unimil", "milfol",
                     "bismilfol", "unomilafol", "unomegafol",
                     "bisjer", "bisjerfol", "bisfoljer", "bis fol",
                     "bis-fol", "Bisfol", "forFOl", "gigagigafol",
                     "kin" * 200 + "fol"):
            with self.subTest(word=word):
                self.assertIsNone(self.lang.parse_multiplicative(word))
        for number in (0, -1, MAX_CARDINAL + 1, True, 2.0, None, "2"):
            with self.subTest(number=number):
                with self.assertRaises(ValueError):
                    self.lang.generate_multiplicative(number)

    def test_meaning_disjoint_from_cardinal_and_iteration(self):
        for w, kind in (("bis", "cardinal_numeral"),
                        ("bisjer", "iteration_counter"),
                        ("bisfol", "multiplicative_factor")):
            analyses = self.lang.analyze_word(w)["analyses"]
            kinds = {a["kind"] for a in analyses}
            self.assertIn(kind, kinds)
            self.assertEqual(len(kinds & {"cardinal_numeral",
                                          "iteration_counter",
                                          "multiplicative_factor"}), 1)

    def test_restricted_svo_factor_modifier(self):
        obj = self.lang.parse_sentence("vidi bisfol domem")["object"]
        self.assertEqual(obj["lemma"], "dom")
        self.assertEqual(obj["modifiers"], ["bisfol"])
        self.assertEqual(obj["multiplicative_factor"], 2)
        self.assertIsNone(obj["numerical_value"])
        for text in ("vidi bisfol ter domem",
                     "vidi bisfol wi domem",
                     "vidi bisfol terfol domem",
                     "vidi nulfol domem",
                     "vidi formul domem"):
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    self.lang.parse_sentence(text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
