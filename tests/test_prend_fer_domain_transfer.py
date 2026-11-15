"""Ratification 2026-11-15: prend physical grasp, fer achieved cross-domain transfer."""
import unittest

from formalization.core import Unisermo


class PrendFerTransferTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = Unisermo()

    def test_lexical_division_and_previous_mnemonic_family(self):
        self.assertIn("prend", self.u.verbs)
        self.assertIn("fer", self.u.verbs)
        self.assertEqual(self.u.lexicon["prend"]["meaning_en"], "take; grasp physically")
        self.assertIn("transfer", self.u.lexicon["fer"]["meaning_en"])
        self.assertEqual(self.u.valency_evidence("prend")["family"], "physical_action")
        self.assertEqual(self.u.valency_evidence("fer")["family"], "domain_transfer")
        self.assertEqual(self.u.valency_evidence("rememor")["family"], "mnemonic")
        self.assertEqual(self.u.parse_sentence("i rememori konem")["valency"], "mnemonic_recall")

    def test_transfer_destination_achieved_and_origin_optional(self):
        for sentence, expected_roles in (
            ("i feri konem umanad",
             ["achieved_destination_domain"]),
            ("i feri konem domde umanad",
             ["transfer_origin", "achieved_destination_domain"]),
            ("i feri portaem domde domad",
             ["transfer_origin", "achieved_destination_domain"]),
        ):
            with self.subTest(sentence=sentence):
                node = self.u.parse_sentence(sentence)
                self.assertEqual(node["valency"], "domain_transfer")
                self.assertEqual(node["predicate"]["lemma"], "fer")
                self.assertEqual(node["argument_roles"]["object"]["role"], "transferred_entity")
                self.assertEqual([x["role"] for x in node["argument_roles"]["case_complements"]],
                                 expected_roles)
                effects = node["argument_roles"]["semantic_entailments"]
                self.assertTrue(effects["entails_destination_relation"])
                for key in ("entails_physical_motion", "entails_source_deletion",
                            "entails_source_retention", "entails_copying",
                            "entails_ownership_transfer", "entails_carriage"):
                    self.assertFalse(effects[key])

    def test_transfer_requires_object_and_achieved_destination(self):
        for sentence in (
            "i feri",
            "i feri konem",
            "i feri domde domad",
            "i feri konem domde",
            "i feri konem domad domad",
            "i feri konem domde umande domad",
            "i feri konem domad domde",
            "i feri konem aperda",
        ):
            with self.subTest(sentence=sentence), self.assertRaises(ValueError):
                self.u.parse_sentence(sentence)

    def test_prend_has_only_physical_acquisition(self):
        x = self.u.parse_sentence("i prendi portaem umande")
        self.assertEqual(x["valency"], "physical_acquisition")
        self.assertEqual(x["argument_roles"]["case_complements"][0]["role"], "physical_origin")
        for sentence in ("i prendi portaem domad", "i prendi konem domad",
                         "i prendi"):
            with self.subTest(sentence=sentence), self.assertRaises(ValueError):
                self.u.parse_sentence(sentence)

    def test_phase_derivation_preserves_family_and_infer_is_not_deduction(self):
        for lemma, base, family in (
            ("adprend", "prend", "physical_action"),
            ("inprend", "prend", "physical_action"),
            ("deprend", "prend", "physical_action"),
            ("reprend", "prend", "physical_action"),
            ("kunprend", "prend", "physical_action"),
            ("adfer", "fer", "domain_transfer"),
            ("infer", "fer", "domain_transfer"),
            ("defer", "fer", "domain_transfer"),
            ("refer", "fer", "domain_transfer"),
            ("kunfer", "fer", "domain_transfer"),
        ):
            with self.subTest(lemma=lemma):
                d = self.u.parse_derivation(lemma)
                self.assertEqual(d["base"], base)
                self.assertEqual(self.u.valency_evidence(lemma)["family"], family)
                tail = " domem umanad" if base == "fer" else " portaem"
                node = self.u.parse_sentence(self.u.generate_verb(lemma) + tail)
                self.assertEqual(node["valency"],
                                 "domain_transfer" if base == "fer" else "physical_acquisition")

    def test_modal_dependent_transfer_uses_its_own_frame(self):
        x = self.u.parse_sentence("debi fer konem umanad")
        self.assertEqual(x["kind"], "servile_clause")
        self.assertEqual(x["dependent"]["valency"], "domain_transfer")
        self.assertTrue(x["dependent"]["argument_roles"]["semantic_entailments"]
                        ["entails_destination_relation"])
        self.assertEqual(self.u.parse_sentence("i portari portaem domad")
                         ["valency"], "physical_transport")
        self.assertEqual(self.u.parse_sentence("traesi solidad likwidde")
                         ["valency"], "state_transition")


if __name__ == "__main__":
    unittest.main()
