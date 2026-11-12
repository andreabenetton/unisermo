"""Executable conformance for already ratified focus enclitics and genitives.

No lexical innovation: -si/-no and -s/-es are the existing canonical
morphology. Only bounded NP attachment is evaluated; double negation,
modal-focus combinations and nested possessors fail closed.
"""
import unittest

from formalization.core import Unisermo


class FocusAndGenitiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = Unisermo()

    def test_personal_genitive_pronouns_are_productive(self):
        canonical = {
            "is": ("i", "singular", 1),
            "us": ("u", "singular", 2),
            "as": ("a", "singular", 3),
            "ins": ("in", "plural", 1),
            "uns": ("un", "plural", 2),
            "ans": ("an", "plural", 3),
            "aos": ("ao", "singular", 3),
            "aes": ("ae", "singular", 3),
            "anos": ("ano", "plural", 3),
            "anes": ("ane", "plural", 3),
        }
        for surface, expected in canonical.items():
            with self.subTest(surface=surface):
                analysis = self.u.analyze_word(surface)["analyses"]
                pronouns = [a for a in analysis if a["kind"] == "genitive_pronoun"]
                self.assertEqual(len(pronouns), 1)
                self.assertEqual((pronouns[0]["lemma"], pronouns[0]["number"],
                                  pronouns[0]["person"]), expected)
                self.assertEqual(pronouns[0]["case"], "genitive")
                self.assertEqual(pronouns[0]["status"], "canonical_by_rule")

    def test_genitive_allomorph_not_assumed_for_final_j(self):
        self.assertEqual(self.u.generate_noun("spets", "genitive"), "spetses")
        self.assertEqual(self.u.generate_noun("dom", "genitive"), "doms")
        # No free-field generalization that -es follows all final j.
        self.assertEqual(self.u.genitive_suffix("adeloj"), "s")

    def test_possessives_have_distinct_np_attachment(self):
        x = self.u.parse_sentence("vidi is domem")
        self.assertEqual(x["object"]["lemma"], "dom")
        owner = x["object"]["possessor"]
        self.assertEqual(owner["kind"], "genitive_relation")
        self.assertEqual(owner["phrase"]["kind"], "genitive_pronoun")
        self.assertEqual(owner["phrase"]["form"], "is")
        self.assertEqual(x["object"]["case"], "accusative")
        s = self.u.parse_sentence("is dom vida")
        self.assertEqual(s["subject"]["possessor"]["phrase"]["person"], 1)
        for form in ("us", "as", "ins", "uns", "ans", "aos", "aes", "anos", "anes"):
            with self.subTest(form=form):
                y = self.u.parse_sentence("vidi " + form + " domem")
                self.assertEqual(y["object"]["possessor"]["phrase"]["form"], form)
        # Syntactic genitive is marked on the possessor's own head.
        z = self.u.parse_sentence("vidi tik umans domem")
        self.assertEqual(z["object"]["possessor"]["phrase"]["lemma"], "uman")
        self.assertEqual(z["object"]["possessor"]["phrase"]["modifiers"], ["tik"])
        self.assertEqual(z["object"]["possessor"]["phrase"]["case"], "genitive")
        plural = self.u.parse_sentence("vidi is wi domem")
        self.assertEqual(plural["object"]["possessor"]["phrase"]["form"], "is")
        self.assertEqual(plural["object"]["modifiers"], ["wi"])

    def test_postposed_genitive_only_in_ratified_part_whole_frame(self):
        x = self.u.parse_sentence("part doms vida")
        self.assertEqual(x["subject"]["lemma"], "part")
        self.assertEqual(x["subject"]["part_whole"]["kind"], "part_whole")
        self.assertEqual(x["subject"]["part_whole"]["whole"]["lemma"], "dom")
        y = self.u.parse_sentence("vidi kin partem doms")
        self.assertEqual(y["object"]["lemma"], "part")
        self.assertEqual(y["object"]["numerical_value"], 5)
        self.assertEqual(y["object"]["part_whole"]["whole"]["case"], "genitive")
        with self.assertRaises(ValueError):
            self.u.parse_sentence("vidi domem umans")  # not a part-whole frame

    def test_focus_on_final_word_of_entire_np(self):
        x = self.u.parse_sentence("i-si vidi domem")
        self.assertFalse(x["negative"])
        self.assertEqual(x["subject"]["focus"]["marker"], "-si")
        self.assertEqual(x["focus"]["kind"], "additive_focus")
        self.assertEqual(x["focus"]["target_role"], "subject")
        y = self.u.parse_sentence("tik omni uman-si vida")
        self.assertEqual(y["subject"]["modifiers"], ["tik", "omni"])
        self.assertEqual(y["focus"]["target_role"], "subject")
        self.assertEqual(y["focus"]["scope"], "entire_constituent")
        obj = self.u.parse_sentence("vidi is domem-si")
        self.assertEqual(obj["focus"]["target_role"], "object")
        self.assertEqual(obj["object"]["possessor"]["phrase"]["form"], "is")
        self.assertEqual(obj["object"]["focus"]["scope"], "entire_constituent")

    def test_negative_additive_focus_is_not_plain_local_no(self):
        x = self.u.parse_sentence("i-no vidi")
        self.assertTrue(x["negative"])
        self.assertEqual(x["negation_type"], "negative_additive_focus")
        self.assertEqual(x["focus"]["marker"], "-no")
        self.assertFalse(self.u.parse_sentence("i-si vidi")["negative"])
        y = self.u.parse_sentence("tik omni uman-no vida")
        self.assertTrue(y["negative"])
        self.assertEqual(y["focus"]["scope"], "entire_constituent")
        z = self.u.parse_sentence("vidi domem-no")
        self.assertTrue(z["negative"])
        self.assertEqual(z["focus"]["target_role"], "object")
        contrast = self.u.parse_sentence("i-si no vidi")
        self.assertTrue(contrast["negative"])
        self.assertEqual(contrast["focus"]["kind"], "additive_focus")
        self.assertNotIn("negation_type", contrast)
        with self.assertRaises(ValueError):
            self.u.parse_sentence("i-no no vidi")

    def test_word_level_bound_vs_free_polarity(self):
        for form in ("i-si", "i-no", "uman-si", "domem-no", "doms-si"):
            with self.subTest(form=form):
                a = self.u.analyze_word(form)["analyses"]
                self.assertEqual(len([x for x in a if x["kind"] == "focus_enclitic"]), 1)
        for invalid in ("i--no", "i-si-no", "-si", "xyzzy-si", "umansi"):
            self.assertFalse(any(a["kind"] == "focus_enclitic"
                                 for a in self.u.analyze_word(invalid)["analyses"]))
        a = self.u.analyze_word("si")["analyses"]
        b = self.u.analyze_word("no")["analyses"]
        self.assertFalse(any(x["kind"] == "focus_enclitic" for x in a + b))

    def test_fail_closed_mixed_or_ambiguous_scopes(self):
        for text in (
            "i-no no vidi", "i-no debi mov", "i-si debi mov",
            "no lim i-no vidi e movi", "no lim i-si vidi e movi",
            "ka i-no vidi?", "i-no vidi?",
            "i-si u-no vidi", "i-si vidi domem-si",
            "vidi partem doms-si", "vidi is-no domem",
            "tik-si uman vida", "i-si-si vidi",
            "vidi is us domem", "vidi domem umans",
            "vidi domem-si-no",
        ):
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.u.parse_sentence(text)

    def test_existing_svo_and_modal_invariants(self):
        x = self.u.parse_sentence("ka i no diki domem?")
        self.assertTrue(x["negative"])
        self.assertTrue(x["interrogative"])
        self.assertNotIn("focus", x)
        self.assertEqual(x["object"]["lemma"], "dom")
        y = self.u.parse_sentence("no debi mov")
        self.assertEqual(y["kind"], "servile_clause")
        self.assertTrue(y["negative"])
        self.assertFalse(y["dependent"]["negative"])
        z = self.u.parse_sentence("debi no mov")
        self.assertFalse(z["negative"])
        self.assertTrue(z["dependent"]["negative"])


if __name__ == "__main__":
    unittest.main()
