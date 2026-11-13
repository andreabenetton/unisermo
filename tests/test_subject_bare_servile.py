"""Owner-ratified overt-subject bare-root serviles governing independently finite propositions."""
import unittest

from formalization.core import Unisermo


class SubjectBareServileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def test_distinct_subjects_and_modal_meanings(self):
        for surface, lemma, meaning, truth in (
            ("i vol u movu", "vol", "desire_that", False),
            ("i int u movu", "int", "intention_that", False),
            ("i tent uman mova", "tent", "attempt_that", False),
            ("i sap uman mova", "sap", "knowledge_that", True),
            ("i kred uman mova", "kred", "belief_that", False),
            ("u sap i movdi", "sap", "knowledge_that", True),
        ):
            with self.subTest(sentence=surface):
                ast = self.lang.parse_sentence(surface)
                self.assertEqual(ast["kind"], "propositional_servile")
                self.assertEqual(ast["operator"], lemma)
                self.assertEqual(ast["operator_form"], "bare_root")
                self.assertEqual(ast["interpretation"], meaning)
                self.assertFalse(ast["negative"])
                self.assertTrue(ast["operand_finite"])
                self.assertEqual(ast["entails_operand_truth"], truth)
                self.assertIn("subject", ast)
                self.assertNotEqual(ast["subject"], ast["operand"]["subject"])

    def test_both_subjects_are_independent(self):
        ast = self.lang.parse_sentence("i vol u movu")
        self.assertEqual(ast["subject"]["person"], 1)
        self.assertEqual(ast["operand"]["subject"]["person"], 2)
        ast = self.lang.parse_sentence("u sap i movdi")
        self.assertEqual(ast["subject"]["person"], 2)
        self.assertEqual(ast["operand"]["subject"]["person"], 1)
        self.assertEqual(ast["operand"]["predicate"]["tense"], "past")

    def test_outer_and_inner_negation_scopes(self):
        a = self.lang.parse_sentence("i no vol u movu")
        b = self.lang.parse_sentence("i vol u no movu")
        self.assertTrue(a["negative"])
        self.assertFalse(a["operand"]["negative"])
        self.assertFalse(b["negative"])
        self.assertTrue(b["operand"]["negative"])
        know_not = self.lang.parse_sentence("i sap u no movu")
        not_know = self.lang.parse_sentence("i no sap u movu")
        self.assertTrue(know_not["entails_operand_truth"])
        self.assertFalse(not_know["entails_operand_truth"])

    def test_truth_vs_attempt(self):
        attempt = self.lang.parse_sentence("i tent uman mova")
        self.assertTrue(attempt["entails_attempt"])
        self.assertFalse(attempt["entails_operand_truth"])
        desire = self.lang.parse_sentence("i vol uman mova")
        self.assertFalse(desire["entails_intention"])
        plan = self.lang.parse_sentence("i int uman mova")
        self.assertTrue(plan["entails_intention"])

    def test_matrix_scope_uses_existing_lim(self):
        wide = self.lang.parse_sentence("i vol u movu e vida")
        narrow = self.lang.parse_sentence("i vol u movu lim e vida")
        self.assertEqual(wide["kind"], "propositional_servile")
        self.assertEqual(wide["operand"]["kind"], "coordination")
        self.assertEqual(narrow["kind"], "coordination")
        self.assertEqual(narrow["left"]["kind"], "propositional_servile")
        self.assertEqual(narrow["right"]["kind"], "svo_clause")

    def test_personal_serviles_and_impersonal_pos_unchanged(self):
        self.assertEqual(self.lang.parse_sentence("voli mov")["kind"], "servile_clause")
        self.assertEqual(self.lang.parse_sentence("inti mov")["kind"], "servile_clause")
        self.assertEqual(self.lang.parse_sentence("tenti mov")["kind"], "servile_clause")
        self.assertEqual(self.lang.parse_sentence("sapi mov")["kind"], "servile_clause")
        self.assertEqual(self.lang.parse_sentence("pos uman mova")["kind"], "propositional_servile")

    def test_unsupported_implicit_subjects_and_personless_tam(self):
        for sentence in ("vol u movu", "int u movu", "tent uman mova",
                         "sap uman mova", "kred uman mova",
                         "i pot u movu", "i deb u movu", "i aut u movu",
                         "i vol", "i vol mov",
                         "i vol u movu lim", "i vol u movu due vida"):
            with self.subTest(sentence=sentence):
                with self.assertRaises(ValueError):
                    self.lang.parse_sentence(sentence)


if __name__ == "__main__":
    unittest.main()
