"""Regression for the ratified vehicle lexical family (2026-11-14)."""

import unittest

from formalization.core import Unisermo


class VehicleFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = Unisermo()

    def test_vehicle_roots_and_distinct_cargo_and_foot(self):
        for noun in ("kar", "bus", "tren", "moto", "kam", "van", "bik", "karg", "ped", "via"):
            with self.subTest(noun=noun):
                self.assertIn(noun, self.u.nouns)
                self.assertNotIn(noun, self.u.verbs)
        self.assertEqual(self.u.lexicon["kam"]["meaning_en"], "truck; lorry")
        self.assertEqual(self.u.lexicon["karg"]["meaning_en"], "cargo; freight")
        self.assertEqual(self.u.lexicon["ped"]["meaning_en"], "foot")

    def test_licensed_compounds_are_nouns(self):
        for noun in ("minibus", "minikar", "minivan", "minitren",
                     "karvia", "trenvia", "bikvia"):
            with self.subTest(noun=noun):
                self.assertIn(noun, self.u.nouns)
                accusative = self.u.generate_noun(noun, "accusative")
                self.assertEqual(accusative, noun + "em")
                self.assertEqual(self.u.parse_word(accusative)["lemma"], noun)

    def test_single_vehicle_clause(self):
        self.assertEqual(self.u.parse_sentence("minibus mova")["kind"], "svo_clause")
        self.assertEqual(self.u.parse_sentence("bik mova")["kind"], "svo_clause")

    def test_no_unrestricted_nominal_compounding(self):
        self.assertNotIn("trenkar", self.u.lexicon)
        self.assertNotIn("busvia", self.u.lexicon)
        self.assertNotIn("minikarg", self.u.lexicon)
        self.assertNotIn("vek", self.u.lexicon)


if __name__ == "__main__":
    unittest.main()
