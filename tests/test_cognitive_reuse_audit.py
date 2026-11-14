"""Research-only parser evidence for cognitive compositionality (no new grammar)."""
import unittest

from formalization.core import Unisermo


class CognitiveReuseAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = Unisermo()

    def test_knowledge_phases_use_existing_content_frame(self):
        for surface, lemma in (
            ("i sapi konem", "sap"),
            ("i adsapi konem", "adsap"),
            ("i insapi konem", "insap"),
            ("i desapi konem", "desap"),
            ("i resapi konem", "resap"),
            ("i adsapei konem", "adsap"),
        ):
            with self.subTest(surface=surface):
                ast = self.u.parse_sentence(surface)
                self.assertEqual(ast["kind"], "svo_clause")
                self.assertEqual(ast["predicate"]["lemma"], lemma)
                self.assertEqual(ast["object"]["lemma"], "kon")
                self.assertEqual(ast["valency"], "knowledge_content")

    def test_understanding_phase_and_recovery_are_morphologically_distinct(self):
        for surface, lemma in (
            ("i kapi konem", "kap"),
            ("i adkapi konem", "adkap"),
            ("i rekapi konem", "rekap"),
            ("i pensi konem", "pens"),
            ("i adpensi konem", "adpens"),
        ):
            with self.subTest(surface=surface):
                ast = self.u.parse_sentence(surface)
                self.assertEqual(ast["kind"], "svo_clause")
                self.assertEqual(ast["predicate"]["lemma"], lemma)
                self.assertEqual(ast["object"]["lemma"], "kon")
                # The AST does NOT prove a specific source or manner.

    def test_knowledge_of_procedure_is_not_assertion_of_event(self):
        for surface, head in (
            ("i sapi dok", "sap"),
            ("i adsapi dok", "adsap"),
            ("i resapi dok", "resap"),
        ):
            with self.subTest(surface=surface):
                ast = self.u.parse_sentence(surface)
                self.assertEqual(ast["kind"], "servile_clause")
                self.assertEqual(ast["head"]["lemma"], head)
                self.assertEqual(ast["dependent"]["lemma"], "dok")

    def test_known_propositional_attitudes_differ(self):
        belief = self.u.parse_sentence("i kred uman mova")
        knowledge = self.u.parse_sentence("i sap uman mova")
        self.assertEqual(belief["kind"], "propositional_servile")
        self.assertEqual(knowledge["kind"], "propositional_servile")
        self.assertEqual(belief["operator"], "kred")
        self.assertEqual(knowledge["operator"], "sap")
        self.assertFalse(belief["entails_operand_truth"])
        self.assertTrue(knowledge["entails_operand_truth"])
        # These frames do not assert that belief is knowledge.

    def test_information_source_is_not_automatically_licensed_by_case(self):
        for surface in (
            "i adsapi konem umande",
            "i resapi konem umande",
            "i adkapi konem umande",
            "i sapi konem mod uman",
        ):
            with self.subTest(surface=surface), self.assertRaises(ValueError):
                self.u.parse_sentence(surface)

    def test_no_new_cognitive_roots_are_implicitly_accepted(self):
        for word in (
            "intui", "ide", "supoz", "solv", "imagin", "presag",
            "deduk", "mem", "memor",
        ):
            with self.subTest(word=word):
                self.assertNotIn(word, self.u.lexicon)


if __name__ == "__main__":
    unittest.main()
