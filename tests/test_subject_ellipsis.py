"""Author-ratified bounded subject ellipsis in additive/adversative coordination."""
import unittest
from formalization.core import Unisermo


class SubjectOnlyPredicateEllipsisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = Unisermo()

    def test_user_contrastive_sentence_inverts_only_elided_predicate(self):
        ast = self.u.parse_sentence("adelo vida trenem ma adele")
        self.assertEqual(ast["kind"], "coordination")
        self.assertEqual(ast["operator"], "ma")
        self.assertEqual(ast["relation"], "adversative")
        self.assertTrue(ast["subject_ellipsis"])
        self.assertEqual(ast["left"]["subject"]["lemma"], "adelo")
        self.assertFalse(ast["left"]["negative"])
        self.assertEqual(ast["right"]["kind"], "elliptical_clause")
        self.assertEqual(ast["right"]["subject"]["lemma"], "adele")
        self.assertTrue(ast["right"]["negative"])
        self.assertEqual(ast["right"]["predicate"]["lemma"], "vid")
        self.assertEqual(ast["right"]["object"]["lemma"], "tren")
        self.assertEqual(ast["right"]["ellipsis"]["polarity"], "opposite")

    def test_additive_ellipsis_preserves_polarity(self):
        ast = self.u.parse_sentence("adelo vida trenem e adele")
        self.assertEqual(ast["operator"], "e")
        self.assertFalse(ast["right"]["negative"])
        self.assertEqual(ast["right"]["ellipsis"]["polarity"], "same")
        self.assertEqual(ast["right"]["object"]["lemma"], "tren")

    def test_ma_reverses_an_explicit_negative_antecedent(self):
        a = self.u.parse_sentence("adelo no vida trenem ma adele")
        b = self.u.parse_sentence("adelo no vida trenem e adele")
        self.assertTrue(a["left"]["negative"])
        self.assertFalse(a["right"]["negative"])
        self.assertTrue(b["left"]["negative"])
        self.assertTrue(b["right"]["negative"])

    def test_verb_features_follow_new_subject_without_spoken_finite(self):
        a = self.u.parse_sentence("i vidi trenem ma u")
        self.assertEqual(a["right"]["predicate"]["person"], 2)
        self.assertEqual(a["right"]["predicate"]["number"], "singular")
        self.assertTrue(a["right"]["negative"])
        b = self.u.parse_sentence("adelo vidda trenem ma bis adele")
        self.assertEqual(b["right"]["predicate"]["tense"], "past")
        self.assertEqual(b["right"]["predicate"]["number"], "plural")
        self.assertEqual(b["right"]["subject"]["numerical_value"], 2)
        c = self.u.parse_sentence("adelo vida trenem e wi adele")
        self.assertEqual(c["right"]["predicate"]["number"], "plural")
        self.assertEqual(a["right"]["predicate"]["source"], "left_clause")

    def test_full_adversative_clause_is_not_negated_by_ma(self):
        ast = self.u.parse_sentence("adelo vida trenem ma adele vida trenem")
        self.assertEqual(ast["kind"], "coordination")
        self.assertEqual(ast["right"]["kind"], "svo_clause")
        self.assertFalse(ast["right"]["negative"])
        self.assertNotIn("subject_ellipsis", ast)

    def test_intransitive_ellipsis_inherits_verb_not_extra_arguments(self):
        ast = self.u.parse_sentence("adelo mova ma adele")
        self.assertEqual(ast["right"]["predicate"]["lemma"], "mov")
        self.assertIsNone(ast["right"]["object"])
        self.assertTrue(ast["right"]["negative"])

    def test_fail_closed_on_unlicensed_fragments(self):
        for sentence in (
            "adelo vida trenem ma",
            "adelo vida trenem ma trenem",
            "adelo vida trenem ma adele no",
            "adelo vida trenem ma adele e uman",
            "vida trenem ma adele",
            "adelo vida trenem ma adele-si",
        ):
            with self.subTest(sentence=sentence), self.assertRaises(ValueError):
                self.u.parse_sentence(sentence)


if __name__ == "__main__":
    unittest.main()
