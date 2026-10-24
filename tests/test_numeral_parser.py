#!/usr/bin/env python3
"""End-to-end checks for ratified mila/mega/giga cardinal powers."""
import random
import unittest
from formalization.core import Unisermo
from formalization.parser.numeral import MAX_CARDINAL, _cardinal, _small_reverse


class NumeralsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def assert_roundtrip(self, value, expected=None):
        word = self.lang.generate_numeral(value)
        if expected is not None:
            self.assertEqual(word, expected)
        parsed = self.lang.parse_numeral(word)
        self.assertIsNotNone(parsed, (value, word))
        self.assertEqual(parsed["value"], value)
        self.assertEqual(self.lang.generate_numeral(parsed["value"]), word)

    def test_examples_from_ratified_normative_spec(self):
        expected = {
            0: "nul", 1: "uno", 2: "bis", 3: "ter", 5: "kin",
            9: "nin", 10: "dek", 11: "dekuno", 12: "dekbis",
            20: "bisdek", 21: "bisdekuno", 25: "bisdekkin",
            90: "nindek", 99: "nindeknin", 100: "sen",
            200: "bissen", 300: "tersen", 321: "tersenbisdekuno",
            405: "forsenkin", 999: "ninsennindeknin",
            1000: "mila", 1001: "milauno", 1100: "milasen",
            2000: "bismila", 2026: "bismilabisdekses",
            9999: "ninmilaninsennindeknin",
            10000: "dekmila", 100000: "senmila",
            1000000: "mega", 1000001: "megauno",
            1001000: "megamila", 10000000: "dekmega",
            100000000: "senmega", 1000000000: "giga",
            10000000000: "dekgiga", 100000000000: "sengiga",
            20345006: "bisdekmegatersenfordekkinmilases",
            MAX_CARDINAL: "ninsennindekningiganinsennindekninmeganinsennindekninmilaninsennindeknin",
        }
        for value, spelling in expected.items():
            with self.subTest(number=value):
                self.assert_roundtrip(value, spelling)

    def test_exhaustive_legacy_range_with_new_mila(self):
        seen = set()
        for value in range(10000):
            word = self.lang.generate_numeral(value)
            self.assertNotIn(word, seen, (value, word))
            seen.add(word)
            self.assertEqual(self.lang.parse_numeral(word)["value"], value)
        self.assertEqual(len(seen), 10000)
        self.assertEqual(len(_small_reverse()), 999)

    def test_all_thousand_group_coefficients_and_boundaries(self):
        for power in (1000, 1000000, 1000000000):
            for coeff in range(1, 1000):
                self.assert_roundtrip(coeff * power)
                if coeff * power + 999 <= MAX_CARDINAL:
                    self.assert_roundtrip(coeff * power + 999)
                if coeff * power - 1 >= 0:
                    self.assert_roundtrip(coeff * power - 1)

    def test_pseudorandom_twelve_digit_roundtrips(self):
        random_gen = random.Random(20261024)
        samples = [random_gen.randrange(0, MAX_CARDINAL + 1) for _ in range(12000)]
        samples += [10**i - 1 for i in range(1, 12)]
        samples += [10**i for i in range(1, 12)]
        samples += [10**i + 1 for i in range(1, 12)]
        for number in samples:
            self.assert_roundtrip(number)

    def test_noncanonical_or_historical_forms_rejected(self):
        for word in (
            "", "mil", "miluno", "bismil", "duo", "cin",
            "unodek", "unosen", "unomila", "unomega", "unogiga",
            "nuldek", "bisdeknul", "bisdekbisdek", "dekdek",
            "nulses", "dekbis sen", "dek-bis", "Dekbis",
            "ninsenunodek", "milanul", "milanuns", "bisdekseses",
            "meganulmila", "giganul", "megamilaunodek", "milamega",
            "megagiga", "gigagiga", "gigamegamega", "megabismega",
            "megauno mega", "megagin", "jer", "bisjer", "bisjergen",
            "kin" * 500,
        ):
            with self.subTest(word=word):
                self.assertIsNone(self.lang.parse_numeral(word))
        for value in (-1, MAX_CARDINAL + 1, 1.5, True, "3", None):
            with self.subTest(number=value):
                with self.assertRaises(ValueError):
                    self.lang.generate_numeral(value)

    def test_iteration_general_range_and_safe_kinship_bound(self):
        for value in (1, 2, 12, 128, 9999, 1000000, MAX_CARDINAL):
            form = self.lang.generate_numeral(value) + "jer"
            self.assertEqual(self.lang.parse_iteration(form)["count"], value)
            analyses = self.lang.analyze_word(form)["analyses"]
            self.assertEqual(len([x for x in analyses if x["kind"] == "iteration_counter"]), 1)
        for word in ("nuljer", "miljer", "duojer", "dekdekjer", "jer", "bis jer", "bisjergen"):
            self.assertIsNone(self.lang.parse_iteration(word))
        self.assertEqual(_cardinal(128), "senbisdekoto")
        self.assertIsNone(self.lang.parse_kinship("senbisdekninjergen"))
        self.assertIsNone(self.lang.parse_kinship("megajergen"))

    def test_compound_numerals_in_svo_grammar(self):
        for noun in ("domem", "adeloem"):
            sentence = "vidi tersenbisdekuno " + noun
            obj = self.lang.parse_sentence(sentence)["object"]
            self.assertEqual(obj["numerical_value"], 321)
        for value in (0, 1, 1000, 20345006, 1000000000, MAX_CARDINAL):
            spelling = self.lang.generate_numeral(value)
            obj = self.lang.parse_sentence("vidi " + spelling + " domem")["object"]
            self.assertEqual(obj["numerical_value"], value)
            self.assertEqual(obj["modifiers"], [spelling])
        with self.assertRaises(ValueError):
            self.lang.parse_sentence("vidi mega wi domem")
        with self.assertRaises(ValueError):
            self.lang.parse_sentence("vidi giga ter domem")
        with self.assertRaises(ValueError):
            self.lang.parse_sentence("vidi mil domem")

    def test_word_analysis_retains_provenance(self):
        entries = self.lang.analyze_word("ter")["analyses"]
        self.assertTrue(any(x["kind"] == "lexical_form" and x["status"] == "example_only" for x in entries))
        self.assertTrue(any(x["kind"] == "cardinal_numeral" and x["value"] == 3 for x in entries))
        for word, number in (("mila", 1000), ("mega", 1000000), ("giga", 1000000000)):
            analyses = self.lang.analyze_word(word)["analyses"]
            self.assertTrue(any(x["kind"] == "lexical_form" and x["status"] == "confirmed_lexicon" for x in analyses))
            self.assertTrue(any(x["kind"] == "cardinal_numeral" and x["value"] == number for x in analyses))
        old = self.lang.analyze_word("mil")["analyses"]
        self.assertTrue(any(x["kind"] == "lexical_form" and x["status"] == "example_only" for x in old))
        self.assertFalse(any(x["kind"] == "cardinal_numeral" for x in old))


if __name__ == "__main__":
    unittest.main(verbosity=2)
