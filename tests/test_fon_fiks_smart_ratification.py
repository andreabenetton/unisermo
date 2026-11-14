"""Ratification regressions for historically broad fon and its qualifiers."""

import unittest

from formalization.core import Unisermo


class PhoneLexiconTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = Unisermo()

    def test_phone_and_qualifier_categories(self):
        self.assertIn("fon", self.u.nouns)
        self.assertIn("fiks", self.u.properties)
        self.assertIn("smart", self.u.properties)
        self.assertEqual(self.u.generate_noun("fon", "accusative"), "fonem")
        self.assertIn("fon", self.u.lexicon)
        self.assertIn("fiks", self.u.lexicon)
        self.assertIn("smart", self.u.lexicon)

    def test_train_is_canonical_noun(self):
        self.assertIn("tren", self.u.nouns)
        self.assertNotIn("tren", self.u.verbs)
        self.assertEqual(self.u.generate_noun("tren", "accusative"), "trenem")
        self.assertEqual(self.u.generate_noun("tren", "ablative"), "trende")
        self.assertEqual(self.u.generate_noun("tren", "dative_allative"), "trenad")
        self.assertEqual(self.u.parse_sentence("tren mova")["kind"], "svo_clause")

    def test_not_conflated_with_motion_or_voice(self):
        self.assertNotIn("mobil", self.u.lexicon)
        self.assertNotIn("fix", self.u.lexicon)
        self.assertNotIn("fon", self.u.verbs)
        self.assertIn("vok", self.u.lexicon)
        self.assertIn("pot", self.u.lexicon)


if __name__ == "__main__":
    unittest.main()
