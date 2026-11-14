"""Independent concept noun kon, distinct from the productive suffix -kon."""
import unittest
from formalization.core import Unisermo


class IndependentKonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = Unisermo()

    def test_independent_concept_noun_and_case(self):
        self.assertIn("kon", self.u.nouns)
        self.assertEqual(self.u.lexicon["kon"]["status"], "confirmed_lexicon")
        self.assertEqual(self.u.generate_noun("kon", "accusative"), "konem")
        self.assertEqual(self.u.generate_noun("kon", "genitive"), "kons")
        self.assertEqual(self.u.parse_sentence("i kapi konem")["object"]["lemma"], "kon")
        self.assertIsNone(self.u.parse_derivation("kon"))

    def test_suffix_keeps_distinct_semantics(self):
        self.assertEqual(self.u.parse_derivation("rodakon")["base"], "roda")
        self.assertEqual(self.u.parse_derivation("rodakon")["operation"], "concept_of")
        self.assertEqual(self.u.parse_derivation("bonitatkon")["base"], "bonitat")
        self.assertNotIn("rodakon", self.u.lexicon)

    def test_idea_and_intuition_are_not_silently_ratified(self):
        for form in ("idea", "intu", "intuision", "ideakon"):
            with self.subTest(form=form):
                self.assertNotIn(form, self.u.lexicon)


if __name__ == "__main__":
    unittest.main()
