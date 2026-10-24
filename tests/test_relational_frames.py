"""Regression gate for explicitly attested case/valency frames (no APIs)."""
import unittest
from formalization.core import Unisermo
from formalization.semantics.relational_frames import parse_relational_frame


class LicensedFramesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang=Unisermo()

    def parse(self,text):
        return parse_relational_frame(text,self.lang)

    def test_move_transitive_destination(self):
        event=self.parse("i movi akwaem domad.")
        self.assertEqual(event["frame"],"move_transitive_to")
        self.assertEqual(event["subject_role"],"agent")
        self.assertEqual(event["subject"]["form"],"i")
        self.assertEqual(event["roles"]["patient"]["lemma"],"akwa")
        self.assertEqual(event["roles"]["patient"]["case"],"accusative")
        self.assertEqual(event["roles"]["destination"]["lemma"],"dom")
        self.assertEqual(event["roles"]["destination"]["case"],"dative_allative")

    def test_transition_two_poles_not_result(self):
        event=self.parse("akwa traesa solidad likwidde.")
        self.assertEqual(event["frame"],"transition_between_states")
        self.assertEqual(event["subject_role"],"theme")
        self.assertEqual(event["subject"]["lemma"],"akwa")
        self.assertEqual(event["roles"]["destination_state"]["lemma"],"solid")
        self.assertEqual(event["roles"]["source_state"]["lemma"],"likwid")
        self.assertEqual(event["roles"]["destination_state"]["case"],"dative_allative")
        self.assertEqual(event["roles"]["source_state"]["case"],"ablative")

    def test_transitive_causative_result_predicate(self):
        event=self.parse("i traesi akwaem solidda.")
        self.assertEqual(event["frame"],"cause_result")
        self.assertEqual(event["subject_role"],"causer")
        self.assertEqual(event["roles"]["patient"]["case"],"accusative")
        self.assertEqual(event["roles"]["result_state"]["case"],"resultative")

    def test_transitive_causative_person_role(self):
        event=self.parse("u traesu umanem doktorda.")
        self.assertEqual(event["frame"],"cause_result")
        self.assertEqual(event["roles"]["patient"]["lemma"],"uman")
        self.assertEqual(event["roles"]["result_state"]["lemma"],"doktor")

    def test_tam_and_phrase_modifiers(self):
        event=self.parse("in movdin tik wi domem tes umanad.")
        self.assertEqual(event["predicate"]["tense"],"past")
        self.assertEqual(event["subject"]["number"],"plural")
        self.assertEqual(event["roles"]["patient"]["modifiers"],["tik","wi"])
        self.assertEqual(event["roles"]["destination"]["modifiers"],["tes"])

    def test_noun_subject_plural(self):
        event=self.parse("wi uman movan akwaem domad.")
        self.assertEqual(event["subject"]["modifiers"],["wi"])
        self.assertEqual(event["predicate"]["number"],"plural")

    def test_morphological_locative_is_valid_but_no_frame_inferred(self):
        forms=self.lang.analyze_word("domin")["analyses"]
        self.assertTrue(any(a["kind"]=="nominal_case" and a["case"]=="locative" for a in forms))
        with self.assertRaises(ValueError):
            self.parse("i movi akwaem domin.")

    def test_scope_limits_and_case_disambiguation(self):
        bad=[
            "i traesi akwaem solidad.",    # wrong result case
            "i traesi akwaem solidde.",    # wrong result case
            "akwa traesa solidda likwidde.",  # wrong destination case
            "akwa traesa solidad likwidda.",  # wrong source case
            "i movi akwaem solidda.",    # motion is not transformation
            "i peli akwaem domad.",     # push doesn't entail motion
            "u traku akwaem domad.",    # pull doesn't entail motion
            "i movi domad akwaem.",     # word-order swap not modeled
            "i movi akwaem domad umanad.", # two destinations
            "i movi akwaem.",           # existing transitive frame not this exact three-role template
            "i movi domad.",            # untested one-argument direction
            "i movi akwaem domin.",     # locative does not substitute for destination
            "i no movi akwaem domad.",  # negated frame not validated
            "ka i movi akwaem domad?",  # question frame not validated
            "i movi akwaem domad?",     # unsupported punctuation/question
            "u movi akwaem domad.",     # person mismatch
            "wi uman mova akwaem domad.", # overt plurality vs singular verb
            "uman movi akwaem domad.", # noun agent cannot license 1sg
            "movi akwaem domad.",       # don't resolve pro-drop here
            "i traesi solidda akwaem.", # result/obj order wrong
            "i traesi akwaem solidda umanad.",
            "i traesi akwaem solidda!"]
        for sentence in bad:
            with self.subTest(sentence=sentence),self.assertRaises(ValueError):
                self.parse(sentence)

    def test_does_not_expand_existing_svo_parser(self):
        self.assertEqual(self.lang.parse_sentence("i vidi domem")["object"]["lemma"],"dom")
        with self.assertRaises(ValueError):
            self.lang.parse_sentence("i movi akwaem domad.")

if __name__ == "__main__":
    unittest.main()
