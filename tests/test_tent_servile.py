"""Ratified attempt servile tent: syntax, polarity and lexical evidence."""
import unittest
from formalization.core import Unisermo


class TentServileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def test_regular_finite_attempts(self):
        for finite, tense, aspect in [
            ("tenti", "present", "simple"),
            ("tentdi", "past", "simple"),
            ("tentei", "present", "progressive"),
        ]:
            with self.subTest(finite=finite):
                ast = self.lang.parse_sentence(f"{finite} mov")
                self.assertEqual(ast["kind"], "servile_clause")
                self.assertEqual(ast["head"]["lemma"], "tent")
                self.assertEqual(ast["head"]["tense"], tense)
                self.assertEqual(ast["head"]["aspect"], aspect)
                self.assertEqual(ast["dependent"]["lemma"], "mov")
                self.assertEqual(ast["attempt_frame"], "attempt_goal_directed")
                self.assertTrue(ast["entails_attempt"])
                self.assertFalse(ast["entails_success"])

    def test_head_vs_goal_negation(self):
        denied = self.lang.parse_sentence("no tenti mov")
        avoidance = self.lang.parse_sentence("tenti no mov")
        self.assertFalse(denied["entails_attempt"])
        self.assertTrue(denied["denies_attempt"])
        self.assertFalse(denied["dependent"]["negative"])
        self.assertTrue(avoidance["entails_attempt"])
        self.assertFalse(avoidance["denies_attempt"])
        self.assertTrue(avoidance["dependent"]["negative"])
        self.assertFalse(avoidance["entails_success"])
        self.assertNotEqual(denied, avoidance)

    def test_dependent_verb_retains_valency(self):
        ast = self.lang.parse_sentence("tenti portar akwaem")
        self.assertEqual(ast["dependent"]["lemma"], "portar")
        self.assertEqual(ast["dependent"]["valency"], "physical_transport")
        self.assertEqual(ast["dependent"]["object"]["lemma"], "akwa")
        other = self.lang.parse_sentence("tenti adkap")
        self.assertEqual(other["dependent"]["lemma"], "adkap")

    def test_reject_unsupported_forms(self):
        for sentence in ("tenti", "tenti vol mov", "tenti portar",
                         "tenti portar domde", "no tenti no mov",
                         "tenti ten umanad"):
            with self.subTest(sentence=sentence):
                with self.assertRaises(ValueError):
                    self.lang.parse_sentence(sentence)

    def test_tent_is_not_ten(self):
        self.assertIn("tent", self.lang.verbs)
        self.assertIn("ten", self.lang.verbs)
        self.assertNotEqual(self.lang.parse_sentence("tenti mov")["head"]["lemma"], "ten")
        self.assertEqual(self.lang.valency_evidence("tent")["status"], "undetermined")


if __name__ == "__main__":
    unittest.main()
