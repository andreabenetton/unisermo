"""LDR-0019 sap phase family: nominal knowledge and procedural know-how.

These are regression assertions for the parser's accepted bounded syntax.
"""
import unittest
from formalization.core import Unisermo


class SapFamilyValencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def test_content_frame_across_all_phases(self):
        for finite, lemma in [
            ("sapi", "sap"),
            ("adsapi", "adsap"),
            ("insapi", "insap"),
            ("desapi", "desap"),
            ("resapi", "resap"),
        ]:
            with self.subTest(finite=finite):
                ast = self.lang.parse_sentence(f"{finite} domem")
                self.assertEqual(ast["predicate"]["lemma"], lemma)
                self.assertEqual(ast["valency"], "knowledge_content")
                self.assertEqual(ast["object"]["lemma"], "dom")

    def test_procedural_frame_across_all_phases(self):
        for finite, lemma in [
            ("sapi", "sap"),
            ("adsapi", "adsap"),
            ("insapi", "insap"),
            ("desapi", "desap"),
            ("resapi", "resap"),
            ("adsapei", "adsap"),
        ]:
            with self.subTest(finite=finite):
                ast = self.lang.parse_sentence(f"{finite} dok")
                self.assertEqual(ast["kind"], "servile_clause")
                self.assertEqual(ast["head"]["lemma"], lemma)
                self.assertEqual(ast["knowledge_frame"], "procedural_knowledge")
                self.assertEqual(ast["dependent"]["lemma"], "dok")
                self.assertFalse(ast["entails_performance"])

    def test_content_is_not_causative_learner(self):
        ast = self.lang.parse_sentence("adsapi umanem")
        self.assertEqual(ast["valency"], "knowledge_content")
        self.assertEqual(ast["object"]["lemma"], "uman")
        self.assertNotEqual(ast["valency"], "caused_learning")

    def test_reject_unlicensed_case_roles(self):
        for sentence in ("adsapi domad", "desapi umande",
                         "resapi domem umanad", "adsapi"):
            with self.subTest(sentence=sentence):
                with self.assertRaises(ValueError):
                    self.lang.parse_sentence(sentence)

    def test_reject_unlicensed_procedural_objects(self):
        for sentence in ("adsapi dok domem", "desapi dok umanad"):
            with self.subTest(sentence=sentence):
                with self.assertRaises(ValueError):
                    self.lang.parse_sentence(sentence)

    def test_no_automatic_learning_or_teaching_causation(self):
        frames = self.lang.valency["knowledge"]
        self.assertFalse(frames["generic_causative"])
        self.assertFalse(frames["entails_teaching"])
        self.assertFalse(frames["entails_performance"])
        self.assertEqual(self.lang.valency_evidence("adsap")["family"], "knowledge")


if __name__ == "__main__":
    unittest.main()
