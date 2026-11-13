"""Executable conformance: ratified LDR-0014 physical action valency.

The four verbs share accusative -em but do NOT share thematic roles.
No sentence-level implication of ownership, permission, voluntary
agency, arrival or object-omission is manufactured by the parser.
"""
import json
import subprocess
import sys
import unittest

from formalization.core import Unisermo


class PhysicalActionValencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = Unisermo()

    def test_overt_object_frames_and_distinct_roles(self):
        samples = [
            ("i feri portaem", "fer", "physical_acquisition", "taker", "physically_acquired_entity"),
            ("i portari portaem", "portar", "physical_transport", "carrier", "cargo"),
            ("i teni portaem", "ten", "maintained_constraint", "constraint_maintainer", "constrained_entity"),
            ("dom kuntena akwaem", "kunten", "spatial_containment", "physical_container", "physically_contained_entity"),
        ]
        for phrase, lemma, frame, subject_role, object_role in samples:
            with self.subTest(phrase=phrase):
                node = self.u.parse_sentence(phrase)
                self.assertEqual(node["kind"], "svo_clause")
                self.assertEqual(node["predicate"]["lemma"], lemma)
                self.assertEqual(node["valency"], frame)
                self.assertEqual(node["argument_roles"]["base"], lemma)
                self.assertEqual(node["argument_roles"]["subject"], subject_role)
                self.assertEqual(node["argument_roles"]["object"],
                                 {"case": "accusative", "role": object_role})
                self.assertEqual(node["object"]["case"], "accusative")
                self.assertEqual(self.u.valency_evidence(lemma)["status"], "documented")
                self.assertEqual(self.u.valency_evidence(lemma)["family"], "physical_action")
                self.assertEqual(node["argument_roles"]["case_complements"], [])

    def test_fer_source_is_physical_not_ownership(self):
        x = self.u.parse_sentence("i feri portaem umande")
        self.assertEqual(x["valency"], "physical_acquisition")
        self.assertEqual(x["complements"][0]["case"], "ablative")
        self.assertEqual(x["complements"][0]["nominal"]["lemma"], "uman")
        self.assertEqual(x["argument_roles"]["case_complements"],
                         [{"case": "ablative", "role": "physical_origin"}])
        self.assertFalse(x["argument_roles"]["semantic_entailments"]["entails_ownership_transfer"])
        self.assertFalse(x["argument_roles"]["semantic_entailments"]["entails_transport"])
        self.assertFalse(x["argument_roles"]["semantic_entailments"]["entails_permission"])
        for bad in ("feri", "feri domde", "feri portaem umanad",
                    "feri portaem domde umande", "feri portaem aperda"):
            with self.subTest(rejected=bad), self.assertRaises(ValueError):
                self.u.parse_sentence(bad)

    def test_portar_optional_origin_destination_and_no_arrival(self):
        for phrase, cases, roles in (
            ("i portari portaem", [], []),
            ("i portari portaem domde", ["ablative"], ["transport_origin"]),
            ("i portari portaem umanad", ["dative_allative"], ["transport_destination"]),
            ("i portari portaem domde umanad",
             ["ablative", "dative_allative"],
             ["transport_origin", "transport_destination"]),
        ):
            with self.subTest(phrase=phrase):
                x = self.u.parse_sentence(phrase)
                self.assertEqual(x["valency"], "physical_transport")
                self.assertEqual([z["case"] for z in x["complements"]], cases)
                self.assertEqual([z["role"] for z in x["argument_roles"]["case_complements"]], roles)
                self.assertFalse(x["argument_roles"]["semantic_entailments"]["entails_arrival"])
                self.assertFalse(x["argument_roles"]["semantic_entailments"]["entails_ownership_transfer"])
        for bad in ("portari", "portari domde", "portari domad",
                    "portari portaem domde domde",
                    "portari portaem domad umande",
                    "portari portaem umanem",
                    "portari portaem aperda"):
            with self.subTest(rejected=bad), self.assertRaises(ValueError):
                self.u.parse_sentence(bad)

    def test_ten_and_kunten_are_not_movement_frames(self):
        for lemma, clause, role in (
            ("ten", "i teni portaem", "constrained_entity"),
            ("kunten", "dom kuntena akwaem", "physically_contained_entity"),
        ):
            node = self.u.parse_sentence(clause)
            self.assertEqual(node["argument_roles"]["object"]["role"], role)
            self.assertFalse(self.u.parse_derivation("kunten"))
            for extra in (" domde", " domad"):
                with self.subTest(lemma=lemma, extra=extra), self.assertRaises(ValueError):
                    self.u.parse_sentence(clause + extra)
        located = self.u.parse_sentence("dom kuntena akwaem domin")
        self.assertEqual(located["valency"], "spatial_containment")
        self.assertEqual(located["argument_roles"]["case_complements"],
                         [{"case": "locative", "role": "event_location"}])
        for bad in ("teni", "kunteni", "dom kuntena", "teni portaem portaem",
                    "dom kuntena akwaem domde"):
            with self.subTest(rejected=bad), self.assertRaises(ValueError):
                self.u.parse_sentence(bad)

    def test_regular_single_prefix_and_lexical_specialization(self):
        for lemma, base, frame in (
            ("adfer", "fer", "physical_acquisition"),
            ("infer", "fer", "physical_acquisition"),
            ("defer", "fer", "physical_acquisition"),
            ("refer", "fer", "physical_acquisition"),
            ("adportar", "portar", "physical_transport"),
            ("inportar", "portar", "physical_transport"),
            ("deportar", "portar", "physical_transport"),
            ("reportar", "portar", "physical_transport"),
            ("adten", "ten", "maintained_constraint"),
            ("inten", "ten", "maintained_constraint"),
            ("deten", "ten", "maintained_constraint"),
            ("reten", "ten", "maintained_constraint"),
            ("kunfer", "fer", "physical_acquisition"),
            ("kunportar", "portar", "physical_transport"),
            ("adkunten", "kunten", "spatial_containment"),
        ):
            with self.subTest(lemma=lemma):
                self.assertEqual(self.u.physical_action_base(lemma), base)
                self.assertEqual(self.u.valency_evidence(lemma)["status"], "documented")
                sentence = self.u.generate_verb(lemma) + " portaem"
                node = self.u.parse_sentence(sentence)
                self.assertEqual(node["valency"], frame)
                self.assertEqual(node["argument_roles"]["base"], base)
        self.assertEqual(self.u.physical_action_base("kunten"), "kunten")
        self.assertNotEqual(self.u.physical_action_base("kunten"), "ten")
        self.assertIsNone(self.u.physical_action_base("adkunportar"))
        self.assertIsNone(self.u.physical_action_base("redef er".replace(" ", "")))

    def test_modal_complements_share_checked_frames(self):
        samples = [
            ("debi fer portaem", "physical_acquisition", "physically_acquired_entity"),
            ("auti portar portaem domad", "physical_transport", "cargo"),
            ("poti ten portaem", "maintained_constraint", "constrained_entity"),
            ("sapi kunten akwaem", "spatial_containment", "physically_contained_entity"),
        ]
        for phrase, frame, role in samples:
            with self.subTest(phrase=phrase):
                node = self.u.parse_sentence(phrase)
                self.assertEqual(node["kind"], "servile_clause")
                self.assertEqual(node["dependent"]["valency"], frame)
                self.assertEqual(node["dependent"]["argument_roles"]["object"]["role"], role)
        for bad in ("debi fer", "auti portar domad", "poti ten",
                    "sapi kunten", "debi kunten akwaem domad"):
            with self.subTest(rejected=bad), self.assertRaises(ValueError):
                self.u.parse_sentence(bad)

    def test_free_relators_and_local_event_locative_remain_adjuncts(self):
        for phrase, lemma in (
            ("i feri portaem kun uman", "fer"),
            ("i portari portaem domin", "portar"),
            ("i teni portaem domin", "ten"),
            ("dom kuntena akwaem kun uman", "kunten"),
        ):
            with self.subTest(phrase=phrase):
                node = self.u.parse_sentence(phrase)
                self.assertEqual(node["predicate"]["lemma"], lemma)
                self.assertIn(node["valency"], {
                    "physical_acquisition", "physical_transport",
                    "maintained_constraint", "spatial_containment"})
                self.assertEqual(len(node["complements"]), 1)

    def test_lexical_evidence_cli_and_source_registry(self):
        val = self.u.valency["physical_action"]
        self.assertEqual(val["status"], "ratified")
        self.assertTrue(val["object_required_in_parser"])
        self.assertEqual(val["omitted_objects"], "undecided_for_discourse")
        self.assertEqual(set(val["frames"]), {"fer", "portar", "ten", "kunten"})
        self.assertEqual(val["lexicalized_containment"], "kunten")
        self.assertIn("LDR-0014", val["source"])
        for lemma in ("fer", "portar", "ten", "kunten"):
            p = subprocess.run([sys.executable, "-m", "formalization", "valency", lemma],
                               capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(p.stdout)["status"], "documented")
        self.assertEqual(self.u.valency_evidence("pens")["status"], "undetermined")
        with open("formalization/data/morphology.json", encoding="utf-8") as f:
            canonical = json.load(f)
        self.assertIn("undetermined_lexical_valency_outside_documented_families",
                      canonical["not_implemented"])


if __name__ == "__main__":
    unittest.main()
