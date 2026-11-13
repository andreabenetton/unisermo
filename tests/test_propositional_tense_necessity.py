"""Accepted LDR-0024: bare propositional necessity and personless tense."""
import unittest
from formalization.core import Unisermo

class PropositionalTenseNecessityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def test_impersonal_tense_and_embedded_reference(self):
        for sentence, root, assessment, embedded in (
            ("pos uman mova", "pos", "present", "present"),
            ("posd uman movfa", "pos", "past", "future"),
            ("posd uman movda", "pos", "past", "past"),
            ("posf uman movda", "pos", "future", "past"),
            ("deb uman mova", "deb", "present", "present"),
            ("debd uman movfa", "deb", "past", "future"),
            ("debf uman movda", "deb", "future", "past"),
        ):
            with self.subTest(sentence=sentence):
                ast=self.lang.parse_sentence(sentence)
                self.assertEqual(ast["kind"],"propositional_servile")
                self.assertEqual(ast["operator"],root)
                self.assertEqual(ast["assessment_tense"],assessment)
                self.assertEqual(ast["embedded_tense_anchor"],"relative_to_assessment")
                self.assertEqual(ast["operand"]["predicate"]["tense"],embedded)
                self.assertNotIn("subject",ast)
                self.assertFalse(ast["entails_operand_truth"])

    def test_subject_bearing_tense_and_knowledge(self):
        for surface, head, tense, meaning in (
            ("i vold u movu","vol","past","desire_that"),
            ("i volf u movfu","vol","future","desire_that"),
            ("i sapd u movdu","sap","past","knowledge_that"),
            ("i sapf u movu","sap","future","knowledge_that"),
            ("i intd u movfu","int","past","intention_that"),
            ("i tentd u movfu","tent","past","attempt_that"),
            ("i kredd u movu","kred","past","belief_that"),
        ):
            with self.subTest(surface=surface):
                ast=self.lang.parse_sentence(surface)
                self.assertEqual(ast["kind"],"propositional_servile")
                self.assertEqual(ast["operator"],head)
                self.assertEqual(ast["assessment_tense"],tense)
                self.assertEqual(ast["interpretation"],meaning)
                self.assertEqual(ast["embedded_tense_anchor"],"relative_to_assessment")
                self.assertEqual(ast["subject"]["person"],1)
                self.assertEqual(ast["operand"]["subject"]["person"],2)
        self.assertTrue(self.lang.parse_sentence("i sapd u movdu")["entails_operand_truth"])
        self.assertFalse(self.lang.parse_sentence("i no sapd u movda")["entails_operand_truth"])

    def test_necessity_scope_not_equated_with_ability_or_duty(self):
        necessary=self.lang.parse_sentence("deb uman mova")
        not_necessary=self.lang.parse_sentence("no deb uman mova")
        prohibited=self.lang.parse_sentence("deb uman no mova")
        self.assertEqual(necessary["interpretation"],"propositional_necessity")
        self.assertFalse(necessary["negative"])
        self.assertTrue(not_necessary["negative"])
        self.assertFalse(prohibited["negative"])
        self.assertTrue(prohibited["operand"]["negative"])
        self.assertEqual(self.lang.parse_sentence("debi mov")["kind"],"servile_clause")
        old=self.lang.parse_sentence("no pos uman no mova")
        self.assertTrue(old["negative"])
        self.assertTrue(old["operand"]["negative"])

    def test_tensed_lim_and_external_negation(self):
        ast=self.lang.parse_sentence("posd uman mova lim e vida")
        self.assertEqual(ast["kind"],"coordination")
        self.assertEqual(ast["left"]["assessment_tense"],"past")
        self.assertEqual(ast["right"]["kind"],"svo_clause")
        ast=self.lang.parse_sentence("i no vold u movu lim e vida")
        self.assertEqual(ast["kind"],"coordination")
        self.assertTrue(ast["left"]["negative"])
        self.assertEqual(ast["left"]["assessment_tense"],"past")

    def test_unsupported_aspect_and_missing_outer_subject(self):
        for sentence in ("pose uman mova", "poso uman mova",
                         "i vole u movu", "i volo u movu",
                         "vold u movu", "sapd u movu", "kredd u movu",
                         "posd", "deb", "debd mov", "deb deb uman mova"):
            with self.subTest(sentence=sentence):
                with self.assertRaises(ValueError):
                    self.lang.parse_sentence(sentence)

if __name__=="__main__":
    unittest.main()
