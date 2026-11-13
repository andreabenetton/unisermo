"""Ratified int adopted-intention servile and distinction from vol/tent."""
import unittest
from formalization.core import Unisermo


class IntentionServileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def test_finite_head_and_arguments(self):
        for form,tense,aspect in [
            ("inti","present","simple"),
            ("intdi","past","simple"),
            ("intei","present","progressive"),
        ]:
            with self.subTest(form=form):
                ast=self.lang.parse_sentence(f"{form} mov")
                self.assertEqual(ast["kind"],"servile_clause")
                self.assertEqual(ast["head"]["lemma"],"int")
                self.assertEqual(ast["head"]["tense"],tense)
                self.assertEqual(ast["head"]["aspect"],aspect)
                self.assertEqual(ast["dependent"]["lemma"],"mov")
                self.assertTrue(ast["entails_intention"])
                self.assertFalse(ast["entails_attempt"])
                self.assertFalse(ast["entails_performance"])

        ast=self.lang.parse_sentence("inti portar akwaem")
        self.assertEqual(ast["dependent"]["valency"],"physical_transport")
        self.assertEqual(ast["dependent"]["object"]["lemma"],"akwa")

    def test_negated_intention_and_intended_avoidance(self):
        denied=self.lang.parse_sentence("no inti mov")
        refrain=self.lang.parse_sentence("inti no mov")
        self.assertFalse(denied["entails_intention"])
        self.assertTrue(denied["denies_intention"])
        self.assertFalse(denied["dependent"]["negative"])
        self.assertTrue(refrain["entails_intention"])
        self.assertFalse(refrain["denies_intention"])
        self.assertTrue(refrain["dependent"]["negative"])
        self.assertFalse(refrain["entails_performance"])

    def test_vol_int_tent_distinct(self):
        wanting=self.lang.parse_sentence("voli mov")
        intending=self.lang.parse_sentence("inti mov")
        trying=self.lang.parse_sentence("tenti mov")
        self.assertEqual([wanting["modal"],intending["modal"],trying["modal"]],["vol","int","tent"])
        self.assertTrue(trying["entails_attempt"])
        self.assertFalse(intending["entails_attempt"])
        self.assertTrue(intending["entails_intention"])

    def test_reject_out_of_subset(self):
        for sentence in ("inti","inti vol mov","inti portar","inti portar domde","no inti no mov"):
            with self.subTest(sentence=sentence):
                with self.assertRaises(ValueError):
                    self.lang.parse_sentence(sentence)

    def test_index_and_lexical_distinction(self):
        self.assertIn("int",self.lang.verbs)
        self.assertEqual(self.lang.lexicon["int"]["status"],"confirmed_lexicon")
        self.assertIn("adopted",self.lang.lexicon["int"]["decision"])
        self.assertEqual(self.lang.valency_evidence("int")["status"],"undetermined")


if __name__=="__main__":
    unittest.main()
