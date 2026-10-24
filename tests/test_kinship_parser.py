#!/usr/bin/env python3
"""Productive, fail-closed kinship path parser tests.

The semantic output is a typed path from ego, *not* a new lexical approval.
"""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from formalization.core import Unisermo
from formalization.parser.kinship import MAX_KINSHIP_STEPS, _cardinal


class KinshipParserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def path(self, word, expected, status=None):
        parsed = self.lang.parse_kinship(word)
        self.assertIsNotNone(parsed, word)
        self.assertEqual(parsed["kind"], "kinship_relation")
        self.assertEqual(parsed["lemma"], word)
        self.assertEqual(parsed["path_from_ego"], expected)
        self.assertEqual(parsed["steps"], len(expected))
        if status:
            self.assertEqual(parsed["status"], status)
        return parsed

    def test_four_maternal_and_paternal_grandparents(self):
        self.path("genegene", ["gene", "gene"], "confirmed_lexicon")
        self.path("genegeno", ["geno", "gene"], "confirmed_lexicon")
        self.path("genogene", ["gene", "geno"], "confirmed_lexicon")
        self.path("genogeno", ["geno", "geno"], "confirmed_lexicon")

    def test_cousins_and_uncle_and_sibling(self):
        self.path("adelgen", ["gen", "adel"], "confirmed_lexicon")
        self.path("filadelgen", ["gen", "adel", "fil"], "confirmed_lexicon")
        self.path("adelo", ["adelo"])
        self.path("adele", ["adele"])
        self.path("fil", ["fil"])

    def test_unbounded_in_principle_chain_with_explicit_path(self):
        self.path("genegenogeno", ["geno", "geno", "gene"], "productive_from_confirmed")
        self.path("filadelgenogeno", ["geno", "geno", "adel", "fil"], "productive_from_confirmed")
        self.path("genegene" * 3, ["gene"] * 6, "productive_from_confirmed")

    def test_numbered_jer_iteration(self):
        self.path("unojergen", ["gen"])
        self.path("bisjergen", ["gen", "gen"], "confirmed_lexicon")
        self.path("terjergene", ["gene", "gene", "gene"], "productive_from_confirmed")
        self.path("bisjergeno", ["geno", "geno"], "productive_from_confirmed")
        self.path("adelbisjergen", ["gen", "gen", "adel"], "productive_from_confirmed")
        self.path("dekbisjergen", ["gen"] * 12, "productive_from_confirmed")
        self.path("senjerfil", ["fil"] * 100, "productive_from_confirmed")
        self.assertEqual(_cardinal(128), "senbisdekoto")
        self.path(_cardinal(MAX_KINSHIP_STEPS) + "jergen", ["gen"] * MAX_KINSHIP_STEPS)

    def test_fails_closed_on_unratified_or_malformed(self):
        for word in ("frat", "germ", "sib", "filo", "file",
                     "nuljergen", "bisjer", "jerfil", "bisjerfrat",
                     "adelfoo", "genoGENE", "genegene?",
                     "sengen", "bisjergen" * 90):
            with self.subTest(word=word):
                self.assertIsNone(self.lang.parse_kinship(word))
        # The generator must not treat a historical or unknown form as
        # an implicitly approved productive genealogical root.
        with self.assertRaises(ValueError):
            self.lang.generate_noun("germgene", "accusative")

    def test_productive_noun_cases_and_sentence_analysis(self):
        lemma = "genegenogeno"  # intentionally absent from fixed index
        self.assertNotIn(lemma, self.lang.lexicon)
        for case in self.lang.morph["nominal"]["case"]:
            surface = self.lang.generate_noun(lemma, case)
            analyses = self.lang.analyze_word(surface)["analyses"]
            matching = [a for a in analyses
                        if a["kind"] == "nominal_case"
                        and a["lemma"] == lemma and a["case"] == case]
            self.assertEqual(len(matching), 1, (case, surface, analyses))
            self.assertEqual(matching[0]["status"], "productive_from_confirmed")
        self.assertEqual(
            self.lang.parse_sentence("vidi " + self.lang.generate_noun(lemma, "accusative"))["object"]["lemma"],
            lemma,
        )

    def test_registered_compound_has_single_nominal_analysis(self):
        for lemma in ("genegene", "genegeno", "genogene", "genogeno",
                      "filadelgen", "bisjergen"):
            for case in self.lang.morph["nominal"]["case"]:
                surface = self.lang.generate_noun(lemma, case)
                analyses = [a for a in self.lang.analyze_word(surface)["analyses"]
                            if a["kind"] == "nominal_case" and a["lemma"] == lemma
                            and a["case"] == case]
                self.assertEqual(len(analyses), 1, (lemma, case, surface, analyses))
                self.assertEqual(analyses[0]["status"], "confirmed_lexicon")


if __name__ == "__main__":
    unittest.main(verbosity=2)
