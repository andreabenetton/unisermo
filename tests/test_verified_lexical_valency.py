"""Source-attested lexical valency and explicit unknown-frame boundaries.

Tests intentionally distinguish documented frames from a syntactically
parseable but lexically unratified argument structure. Rejecting an
unsupported structure here is not a claim of language-wide ungrammaticality.
"""
import unittest
import json
import subprocess
import sys
from formalization.core import Unisermo


class VerifiedLexicalValencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = Unisermo()

    def test_force_patient_frame_preserves_no_motion_entailment(self):
        for lemma in ("pel", "trak"):
            with self.subTest(lemma=lemma):
                finite = self.u.generate_verb(lemma)
                clause = self.u.parse_sentence(finite + " domem")
                self.assertEqual(clause["kind"], "svo_clause")
                self.assertEqual(clause["predicate"]["lemma"], lemma)
                self.assertEqual(clause["valency"], "force_on_patient")
                self.assertFalse(clause["entails_successful_displacement"])
                self.assertEqual(clause["object"]["lemma"], "dom")
                self.assertEqual(self.u.valency_evidence(lemma)["status"],
                                 "documented")
                with self.assertRaises(ValueError):
                    self.u.parse_sentence(finite)
                for bad in (" domem umanad", " domem umande", " domin"):
                    with self.subTest(invalid=bad), self.assertRaises(ValueError):
                        self.u.parse_sentence(finite + bad)
        local = self.u.parse_sentence("peli domem domin")
        self.assertEqual(local["valency"], "force_on_patient")
        self.assertEqual(local["complements"][0]["case"], "locative")
        adjunct = self.u.parse_sentence("traki domem kun uman")
        self.assertEqual(adjunct["complements"][0]["relator"], "kun")

    def test_force_verbs_inside_modals_and_regular_phases(self):
        clause = self.u.parse_sentence("debi pel domem")
        self.assertEqual(clause["kind"], "servile_clause")
        self.assertEqual(clause["dependent"]["valency"], "force_on_patient")
        self.assertFalse(clause["dependent"]["entails_successful_displacement"])
        with self.assertRaises(ValueError):
            self.u.parse_sentence("debi trak")
        phase = self.u.parse_sentence("adpeli domem")
        self.assertEqual(phase["valency"], "force_on_patient")
        self.assertEqual(self.u.valency_evidence("adpel")["family"], "force_manner")

    def test_explicit_copula_existential_and_quality_state(self):
        exist = self.u.parse_sentence("i esi")
        self.assertEqual(exist["kind"], "copular_clause")
        self.assertEqual(exist["valency"], "existential_copula")
        self.assertIsNone(exist["state"])
        qual = self.u.parse_sentence("dom esa bon")
        self.assertEqual(qual["kind"], "copular_clause")
        self.assertEqual(qual["valency"], "explicit_copula")
        self.assertEqual(qual["state"], {"kind": "quality_state", "lemma": "bon"})
        nominal = self.u.parse_sentence("esi uman")
        self.assertEqual(nominal["state"], {"kind": "nominal_state", "lemma": "uman"})
        loc = self.u.parse_sentence("esi domin")
        self.assertEqual(loc["state"]["kind"], "locative_state")
        self.assertEqual(loc["state"]["phrase"]["lemma"], "dom")
        polar = self.u.parse_sentence("ka i esi?")
        self.assertEqual(polar["question"]["kind"], "polar")

    def test_phase_state_copula_requires_one_state(self):
        for finite, lemma, frame in (
            ("inesi", "klus", "continue_state"),
            ("adesi", "aper", "enter_state"),
            ("deesi", "bon", "leave_state"),
            ("reesi", "uman", "resume_state"),
        ):
            with self.subTest(finite=finite):
                clause = self.u.parse_sentence(finite + " " + lemma)
                self.assertEqual(clause["kind"], "copular_clause")
                self.assertEqual(clause["predicate"]["lemma"], finite[:-1])
                self.assertEqual(clause["valency"], frame)
                self.assertEqual(clause["state"]["lemma"], lemma)
                self.assertEqual(self.u.valency_evidence(finite[:-1])["status"],
                                 "documented")
        modal = self.u.parse_sentence("debi ades aper")
        self.assertEqual(modal["kind"], "servile_clause")
        self.assertEqual(modal["dependent"]["valency"], "enter_state")
        self.assertEqual(modal["dependent"]["state"]["lemma"], "aper")
        neg = self.u.parse_sentence("no adesi aper")
        self.assertTrue(neg["negative"])
        for text in ("adesi", "inesi", "deesi", "reesi",
                     "adesi domem", "esi domem", "adesi umanad",
                     "adesi aper bon", "debi ades"):
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.u.parse_sentence(text)

    def test_unratified_lexical_valency_remains_explicitly_undetermined(self):
        for lemma in ("pens", "kap", "dik", "vid", "dok",
                      "fak"):
            with self.subTest(lemma=lemma):
                evidence = self.u.valency_evidence(lemma)
                self.assertEqual(evidence["status"], "undetermined")
                self.assertIsNone(evidence["source"])
                self.assertIsNone(evidence["family"])
        self.assertEqual(self.u.valency_evidence("sap")["family"], "knowledge")
        self.assertEqual(self.u.valency_evidence("adsap")["status"], "documented")
        self.assertEqual(self.u.parse_sentence("feri domem")["object"]["lemma"],
                         "dom")
        self.assertEqual(self.u.parse_sentence("vidi domem")["object"]["lemma"],
                         "dom")
        self.assertEqual(self.u.parse_sentence("faki domin")["complements"][0]["case"],
                         "locative")
        self.assertEqual(self.u.parse_sentence("faki kun uman")["complements"][0]["relator"],
                         "kun")
        for text in ("feri umanad", "diki umanad", "portari domde",
                     "vidi umanad", "faki umanem umande"):
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.u.parse_sentence(text)
        with self.assertRaises(ValueError):
            self.u.valency_evidence("unknownverb")

    def test_legacy_mov_and_traes_constraints_unchanged(self):
        motion = self.u.parse_sentence("movi domem umanad")
        self.assertEqual(motion["valency"], "motion_causative")
        transition = self.u.parse_sentence("traesi solidad likwidde")
        self.assertEqual(transition["valency"], "state_transition")
        transformation = self.u.parse_sentence("traesi akwaem aperda")
        self.assertEqual(transformation["valency"], "causative_transformation")
        with self.assertRaises(ValueError):
            self.u.parse_sentence("traesi domem")
        with self.assertRaises(ValueError):
            self.u.parse_sentence("movi domin domin")

    def test_cli_valency_inventory_covers_all_indexed_verb_roots(self):
        completed = subprocess.run(
            [sys.executable, "-m", "formalization", "valency", "--all"],
            check=True, capture_output=True, text=True,
        )
        rows = json.loads(completed.stdout)
        self.assertEqual(len(rows), len(self.u.verbs))
        self.assertEqual([x["lemma"] for x in rows], sorted(self.u.verbs))
        self.assertTrue(any(x["lemma"] == "pel" and x["status"] == "documented"
                            for x in rows))
        self.assertTrue(any(x["lemma"] == "fer" and x["status"] == "documented"
                            for x in rows))
        self.assertTrue(any(x["lemma"] == "pens" and x["status"] == "undetermined"
                            for x in rows))
        single = subprocess.run(
            [sys.executable, "-m", "formalization", "valency", "trak"],
            check=True, capture_output=True, text=True,
        )
        self.assertEqual(json.loads(single.stdout)["family"], "force_manner")

    def test_frame_sources_are_explicit(self):
        registry = self.u.valency
        self.assertIn("pel", registry["force_manner"]["verbs"])
        self.assertIn("trak", registry["force_manner"]["verbs"])
        self.assertFalse(registry["force_manner"]["entails_successful_displacement"])
        self.assertEqual(registry["copula_state"]["phase_predicate"], "required")
        self.assertEqual(registry["undetermined"]["status"],
                         "unratified_lexical_valency")
        self.assertIn("language/copula.md", registry["copula_state"]["source"])


if __name__ == "__main__":
    unittest.main()
