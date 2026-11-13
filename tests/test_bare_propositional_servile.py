"""Author-ratified bare servile + finite proposition scope, first pos frame."""
import unittest
from formalization.core import Unisermo


class BarePropositionalServileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def test_personal_and_propositional_are_distinct(self):
        personal = self.lang.parse_sentence("posi mov")
        modal = self.lang.parse_sentence("pos uman mova")
        self.assertEqual(personal["kind"], "servile_clause")
        self.assertEqual(personal["modal"], "pos")
        self.assertEqual(personal["dependent"]["lemma"], "mov")
        self.assertEqual(modal["kind"], "propositional_servile")
        self.assertEqual(modal["operator"], "pos")
        self.assertEqual(modal["interpretation"], "epistemic_possibility")
        self.assertEqual(modal["operator_form"], "bare_root")
        self.assertEqual(modal["operand"]["kind"], "svo_clause")
        self.assertFalse(modal["entails_operand_truth"])
        self.assertEqual(modal["operand"]["predicate"]["lemma"], "mov")

    def test_embedded_person_and_tam_independent(self):
        for words, person, tense in [
            ("pos mova", 3, "present"),
            ("pos movdi", 1, "past"),
            ("pos uman movda", 3, "past"),
        ]:
            with self.subTest(words=words):
                ast = self.lang.parse_sentence(words)
                self.assertEqual(ast["kind"], "propositional_servile")
                self.assertEqual(ast["operand"]["predicate"]["person"], person)
                self.assertEqual(ast["operand"]["predicate"]["tense"], tense)

    def test_modal_vs_inner_negation(self):
        denied = self.lang.parse_sentence("no pos uman mova")
        possible_not = self.lang.parse_sentence("pos uman no mova")
        necessary = self.lang.parse_sentence("no pos uman no mova")
        self.assertTrue(denied["negative"])
        self.assertFalse(denied["operand"]["negative"])
        self.assertFalse(possible_not["negative"])
        self.assertTrue(possible_not["operand"]["negative"])
        self.assertTrue(necessary["negative"])
        self.assertTrue(necessary["operand"]["negative"])

    def test_default_wide_scope_and_explicit_lim_closure(self):
        wide = self.lang.parse_sentence("pos uman mova e vida")
        narrow = self.lang.parse_sentence("pos uman mova lim e vida")
        self.assertEqual(wide["kind"], "propositional_servile")
        self.assertEqual(wide["operand"]["kind"], "coordination")
        self.assertEqual(wide["operand"]["operator"], "e")
        self.assertEqual(narrow["kind"], "coordination")
        self.assertEqual(narrow["operator"], "e")
        self.assertEqual(narrow["left"]["kind"], "propositional_servile")
        self.assertEqual(narrow["right"]["kind"], "svo_clause")
        self.assertEqual(narrow["left"]["operand"]["predicate"]["lemma"], "mov")
        self.assertEqual(narrow["right"]["predicate"]["lemma"], "vid")
        no_narrow = self.lang.parse_sentence("no pos uman mova lim e vida")
        self.assertTrue(no_narrow["left"]["negative"])
        self.assertEqual(no_narrow["right"]["kind"], "svo_clause")

    def test_longer_boolean_operand(self):
        ast = self.lang.parse_sentence("pos uman mova o vida")
        self.assertEqual(ast["kind"], "propositional_servile")
        self.assertEqual(ast["operand"]["kind"], "coordination")
        self.assertEqual(ast["operand"]["operator"], "o")

    def test_open_semantic_or_tam_extensions_fail_closed(self):
        for sentence in (
            "pos", "no pos", "pos mov",
            "vol uman mova", "tent uman mova",
            "pot uman mova", "sap uman mova",
            "pos uman mova lim", "pos uman mova lim vida",
            "pos uman mova e", "pos uman mova due vida",
            "pos pos uman mova"
        ):
            with self.subTest(sentence=sentence):
                with self.assertRaises(ValueError):
                    self.lang.parse_sentence(sentence)


if __name__ == "__main__":
    unittest.main()
