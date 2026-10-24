#!/usr/bin/env python3
"""Exhaustive roundtrip and integration tests for the 0..9999 numerals."""
import unittest
from formalization.core import Unisermo
from formalization.parser.numeral import MAX_CARDINAL, _cardinal


class NumeralsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def test_examples_from_normative_spec(self):
        for value, form in {
            0: "nul", 1: "uno", 2: "bis", 3: "ter", 5: "kin",
            9: "nin", 10: "dek", 11: "dekuno", 12: "dekbis",
            20: "bisdek", 21: "bisdekuno", 25: "bisdekkin",
            90: "nindek", 99: "nindeknin", 100: "sen",
            200: "bissen", 300: "tersen", 321: "tersenbisdekuno",
            405: "forsenkin", 999: "ninsennindeknin", 1000: "mil",
            1001: "miluno", 2000: "bismil", 2026: "bismilbisdekses",
            9999: "ninmilninsennindeknin",
        }.items():
            with self.subTest(number=value):
                self.assertEqual(self.lang.generate_numeral(value), form)
                parsed = self.lang.parse_numeral(form)
                self.assertIsNotNone(parsed)
                self.assertEqual(parsed["value"], value)

    def test_exhaustive_injectivity_roundtrip(self):
        seen = set()
        for number in range(MAX_CARDINAL + 1):
            form = self.lang.generate_numeral(number)
            self.assertNotIn(form, seen, (form, number))
            seen.add(form)
            self.assertEqual(self.lang.parse_numeral(form)["value"], number)
            self.assertEqual(self.lang.generate_numeral(self.lang.parse_numeral(form)["value"]), form)
        self.assertEqual(len(seen), 10000)

    def test_noncanonical_forms_rejected(self):
        for word in ("", "duo", "cin", "unodek", "unosen", "unomil",
                     "nuldek", "bisdeknul", "bisdekbisdek", "dekdek",
                     "nulses", "dekbis sen", "dek-bis", "Dekbis",
                     "ninsenunodek", "milnul", "milnuns", "bisdekseses",
                     "jer", "bisjer", "bisjergen", "kin" * 500):
            with self.subTest(word=word):
                self.assertIsNone(self.lang.parse_numeral(word))
        for value in (-1, 10000, 1.5, True, "3", None):
            with self.subTest(number=value):
                with self.assertRaises(ValueError):
                    self.lang.generate_numeral(value)

    def test_iteration_count_without_guilt_by_association(self):
        for value in (1, 2, 3, 12, 128, 9999):
            form = self.lang.generate_numeral(value) + "jer"
            self.assertEqual(self.lang.parse_iteration(form)["count"], value)
            a = self.lang.analyze_word(form)["analyses"]
            self.assertEqual(len([x for x in a if x["kind"] == "iteration_counter"]), 1)
        for word in ("nuljer", "duojer", "dekdekjer", "jer", "bis jer", "bisjergen"):
            self.assertIsNone(self.lang.parse_iteration(word))
        self.assertEqual(_cardinal(128), "senbisdekoto")
        # The genealogical parser intentionally caps *expanded steps* at 128.
        self.assertIsNone(self.lang.parse_kinship("senbisdekninjergen"))

    def test_compound_numerals_in_grammar(self):
        cases = ("domem", "adeloem")
        for noun in cases:
            sentence = "vidi tersenbisdekuno " + noun
            obj = self.lang.parse_sentence(sentence)["object"]
            self.assertEqual(obj["numerical_value"], 321)
            self.assertEqual(obj["modifiers"], ["tersenbisdekuno"])
        z = self.lang.parse_sentence("vidi nul domem")["object"]
        self.assertEqual(z["numerical_value"], 0)
        self.assertEqual(self.lang.parse_sentence("vidi uno domem")["object"]["numerical_value"], 1)
        with self.assertRaises(ValueError):
            self.lang.parse_sentence("vidi bisdek wi domem")
        with self.assertRaises(ValueError):
            self.lang.parse_sentence("vidi bisdek ter domem")
        with self.assertRaises(ValueError):
            self.lang.parse_sentence("vidi unosen domem")

    def test_word_analysis_preserves_lexical_history(self):
        entries = self.lang.analyze_word("ter")["analyses"]
        self.assertTrue(any(a["kind"] == "lexical_form" and a["status"] == "example_only"
                            for a in entries))
        self.assertTrue(any(a["kind"] == "cardinal_numeral" and a["value"] == 3
                            and a["status"] == "canonical_by_rule" for a in entries))
        value = self.lang.analyze_word("tersenbisdekuno")["analyses"]
        self.assertEqual(len([a for a in value if a["kind"] == "cardinal_numeral"]), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
