"""Approved canonical positive ordinal tests; no fractional grammar implied."""
import random
import unittest
from formalization.core import Unisermo
from formalization.parser.numeral import MAX_CARDINAL

class OrdinalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.lang = Unisermo()

    def test_examples(self):
        examples = {1: "unim", 2: "bisim", 3: "terim", 4: "forim", 8: "otim", 10: "dekim", 11: "dekunim", 21: "bisdekunim", 100: "senim", 1000: "milaim", 1000000: "megaim", MAX_CARDINAL: self.lang.generate_numeral(MAX_CARDINAL)+"im"}
        for n, word in examples.items():
            with self.subTest(n=n):
                self.assertEqual(self.lang.generate_ordinal(n), word)
                self.assertEqual(self.lang.parse_ordinal(word)["value"], n)
                self.assertTrue(any(a["kind"] == "ordinal_numeral" for a in self.lang.analyze_word(word)["analyses"]))

    def test_exhaustive_small_and_sample_large(self):
        rng = random.Random(2071)
        for n in list(range(1, 10000)) + [rng.randint(1, MAX_CARDINAL) for _ in range(1000)]:
            word = self.lang.generate_ordinal(n)
            self.assertEqual(self.lang.parse_ordinal(word)["value"], n)
            self.assertEqual(self.lang.generate_ordinal(self.lang.parse_ordinal(word)["value"]), word)

    def test_analytical_variants(self):
        samples = {"unoim": "unim", "otoim": "otim", "dekunoim": "dekunim", "bisdekunoim": "bisdekunim", "bisdekotoim": "bisdekotim"}
        for form, canonical in samples.items():
            with self.subTest(form=form):
                result = self.lang.parse_ordinal(form)
                self.assertIsNotNone(result)
                self.assertEqual(result["canonical_form"], canonical)
                self.assertEqual(result["status"], "accepted_analytic_variant")
                self.assertEqual(self.lang.generate_ordinal(result["value"]), canonical)

    def test_unapproved_or_invalid(self):
        for word in ("nulim", "milim", "unimim", "Unim", "bis-im", "bisjerim", "bisfolim", "bisimfol", "bisimjer", "im"):
            with self.subTest(word=word): self.assertIsNone(self.lang.parse_ordinal(word))
        for n in (0, -1, MAX_CARDINAL+1, True, 1.5):
            with self.assertRaises(ValueError): self.lang.generate_ordinal(n)

    def test_svo_nominal_case_and_scope(self):
        x = self.lang.parse_sentence("vidi bisim domem")
        self.assertEqual(x["object"]["ordinal_value"], 2)
        self.assertEqual(x["object"]["numerical_value"], None)
        self.assertEqual(x["object"]["case"], "accusative")
        for sentence in ("vidi bis bisim domem", "vidi wi bisim domem", "vidi bisim bis domem"):
            with self.assertRaises(ValueError): self.lang.parse_sentence(sentence)

if __name__ == "__main__": unittest.main()
