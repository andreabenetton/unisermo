"""Ratification regression: roda is the ordinary noun for wheel."""

import unittest

from formalization.core import Unisermo


class WheelNounTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = Unisermo()

    def test_roda_is_a_canonical_noun(self):
        self.assertIn("roda", self.u.nouns)
        self.assertNotIn("roda", self.u.verbs)
        self.assertEqual(self.u.lexicon["roda"]["status"], "confirmed_lexicon")
        self.assertNotIn("rot", self.u.lexicon)
        self.assertNotIn("rota", self.u.lexicon)

    def test_regular_nominal_cases(self):
        for case, expected in {
            "nominative": "roda",
            "accusative": "rodaem",
            "genitive": "rodas",
            "dative_allative": "rodaad",
            "ablative": "rodade",
            "locative": "rodain",
            "resultative": "rodada",
        }.items():
            with self.subTest(case=case):
                self.assertEqual(self.u.generate_noun("roda", case), expected)
                analyses = self.u.analyze_word(expected)["analyses"]
                self.assertTrue(any(
                    item["kind"] == "nominal_case" and
                    item["lemma"] == "roda" and item["case"] == case
                    for item in analyses
                ))

    def test_roda_not_conflated_with_vehicle(self):
        self.assertIn("bik", self.u.nouns)
        self.assertIn("kar", self.u.nouns)
        self.assertNotIn("rodakar", self.u.lexicon)


if __name__ == "__main__":
    unittest.main()
