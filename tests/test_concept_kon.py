"""Ratified -kon conceptual nominalization and strict -itat contrast."""
import unittest
from formalization.core import Unisermo


class ConceptSuffixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = Unisermo()

    def test_concepts_from_known_nominals_properties_and_verbs(self):
        for form, base in (
            ("rodakon", "roda"), ("karkon", "kar"),
            ("umankon", "uman"), ("bonkon", "bon"),
            ("belkon", "bel"), ("dokkon", "dok"),
        ):
            with self.subTest(form=form):
                d = self.u.parse_derivation(form)
                self.assertIsNotNone(d)
                self.assertEqual(d["base"], base)
                self.assertEqual(d["affix"], "kon")
                self.assertEqual(d["operation"], "concept_of")
                self.assertEqual(d["category"], "noun")
                self.assertEqual(d["status"], "productive_from_confirmed")
                self.assertNotIn(form, self.u.lexicon)
                self.assertEqual(self.u.generate_noun(form), form)
                self.assertEqual(self.u.generate_noun(form, "accusative"), form + "em")
                self.assertIn("nominal_case", {
                    a["kind"] for a in self.u.analyze_word(form + "em")["analyses"]
                })

    def test_abstract_quality_distinct_from_concept(self):
        a = self.u.parse_derivation("bonitat")
        b = self.u.parse_derivation("bonkon")
        c = self.u.parse_derivation("bonitatkon")
        self.assertEqual(a["operation"], "abstract_quality")
        self.assertEqual(b["operation"], "concept_of")
        self.assertEqual(c["operation"], "concept_of")
        self.assertEqual(c["base"], "bonitat")
        self.assertEqual(c["base_derivation"]["operation"], "abstract_quality")
        self.assertEqual(self.u.generate_noun("bonitatkon", "accusative"), "bonitatkonem")
        self.assertEqual(self.u.parse_derivation("belitatkon")["base"], "belitat")
        self.assertEqual(self.u.parse_derivation("umanitatkon")["base"], "umanitat")
        self.assertEqual(self.u.parse_sentence("i kapi rodakonem")["object"]["lemma"],
                         "rodakon")

    def test_unapproved_suffix_chains_and_nonconceptual_bases_fail_closed(self):
        for word in (
            "rodaitat", "rodaitatkon", "bonkonkon", "dokkonkon",
            "bonkonitat", "eksekon", "makon", "bisekon", "foobarkon",
            "major kon", "roda kon",
        ):
            with self.subTest(word=word):
                self.assertIsNone(self.u.parse_derivation(word))
        with self.assertRaises(ValueError):
            self.u.generate_noun("rodaitatkon", "accusative")

    def test_genitive_and_other_cases_attach_after_kon(self):
        self.assertEqual(self.u.generate_noun("rodakon", "genitive"), "rodakons")
        self.assertEqual(self.u.generate_noun("bonkon", "dative_allative"), "bonkonad")
        self.assertTrue(any(
            x["kind"] == "nominal_case" and x["case"] == "genitive"
            for x in self.u.analyze_word("rodakons")["analyses"]
        ))


if __name__ == "__main__":
    unittest.main()
