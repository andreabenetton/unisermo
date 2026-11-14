"""Lexical-policy guardrails against catch-all idea/intuition synonym roots."""
import unittest
from formalization.core import Unisermo


class SemanticSpecificityPolicyTests(unittest.TestCase):
    def test_catchall_idea_is_excluded_from_confirmed_lexicon(self):
        language = Unisermo()
        self.assertNotIn("ide", language.lexicon)
        self.assertNotIn("ide", language.nouns)
        self.assertEqual(language.lexicon["kon"]["status"], "confirmed_lexicon")
        self.assertEqual(language.lexicon["kon"]["meaning_en"].split(";")[0], "concept")

    def test_semantic_map_candidates_are_not_implicitly_ratified(self):
        language = Unisermo()
        for candidate in ("propoz", "program", "solv", "imagin",
                          "supoz", "previs", "presag", "intui"):
            with self.subTest(candidate=candidate):
                self.assertNotIn(candidate, language.lexicon)
                self.assertEqual(language.analyze_word(candidate)["analyses"], [])


if __name__ == "__main__":
    unittest.main()
