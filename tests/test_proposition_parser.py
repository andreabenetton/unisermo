"""Executable grammar-conformance tests for the typed proposition AST.

Only constructions authorized by the living language spec are tested as
accepted. Explicitly open/ambiguous constructions must fail closed or keep
attachment unresolved; no invented scope from punctuation or word order.
"""
import unittest

from formalization.core import Unisermo


class TypedPropositionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = Unisermo()

    def test_canonical_lexical_roles_are_executable(self):
        for root in ("pos", "deb", "vol", "pot", "sap", "aut",
                     "pens", "fer", "portar", "ten", "kunten"):
            with self.subTest(root=root):
                self.assertIn(root, self.u.verbs)
                self.assertEqual(self.u.generate_verb(root), root + "i")
                self.assertIn("finite_verb", {a["kind"] for a in
                              self.u.analyze_word(root + "i")["analyses"]})
        self.assertIn("porta", self.u.nouns)
        self.assertEqual(self.u.generate_noun("porta", "locative"), "portain")
        self.assertNotIn("porta", self.u.verbs)
        self.assertIn("bel", self.u.properties)
        self.assertNotIn("gen", self.u.properties)

    def test_legacy_ast_stays_compatible(self):
        x = self.u.parse_sentence("ka i no diki domem?")
        self.assertEqual(x["kind"], "svo_clause")
        self.assertTrue(x["negative"])
        self.assertTrue(x["interrogative"])
        self.assertEqual(x["predicate"]["lemma"], "dik")
        self.assertEqual(x["object"]["lemma"], "dom")
        self.assertEqual(self.u.parse_sentence("vidi bisfol domem")["object"]["multiplicative_factor"], 2)
        self.assertEqual(self.u.parse_sentence("vidi bisim domem")["object"]["ordinal_value"], 2)

    def test_modal_scope_and_source_attachment(self):
        a = self.u.parse_sentence("no debi mov")
        b = self.u.parse_sentence("debi no mov")
        self.assertEqual(a["kind"], "servile_clause")
        self.assertTrue(a["negative"])
        self.assertFalse(a["dependent"]["negative"])
        self.assertFalse(b["negative"])
        self.assertTrue(b["dependent"]["negative"])
        for root in ("pos", "vol", "pot", "sap", "aut"):
            with self.subTest(root=root):
                y = self.u.parse_sentence(root + "i no mov")
                self.assertEqual(y["modal"], root)
                self.assertTrue(y["dependent"]["negative"])
        x = self.u.parse_sentence("auti umande mov domde")
        self.assertEqual(x["source"]["lemma"], "uman")
        self.assertEqual(x["source"]["case"], "ablative")
        self.assertEqual(x["dependent"]["lemma"], "mov")
        self.assertEqual(x["dependent"]["complements"][0]["case"], "ablative")
        self.assertEqual(x["dependent"]["complements"][0]["nominal"]["lemma"], "dom")
        z = self.u.parse_sentence("auti mov domde")
        self.assertIsNone(z["source"])
        self.assertEqual(z["dependent"]["complements"][0]["case"], "ablative")
        denied = self.u.parse_sentence("no auti umande mov")
        self.assertTrue(denied["negative"])
        self.assertEqual(denied["source"]["lemma"], "uman")
        with self.assertRaises(ValueError):
            self.u.parse_sentence("no debi no mov")
        with self.assertRaises(ValueError):
            self.u.parse_sentence("auti umande")  # no dependent action

    def test_arguments_relators_and_purpose(self):
        q = self.u.parse_sentence("movi domin")
        self.assertEqual(q["complements"][0]["case"], "locative")
        q = self.u.parse_sentence("faki kun uman")
        self.assertEqual(q["complements"][0]["relator"], "kun")
        q = self.u.parse_sentence("faki fin dok bis umanem")
        self.assertEqual(q["complements"][0]["kind"], "purpose_infinitive")
        self.assertEqual(q["complements"][0]["verb"], "dok")
        self.assertEqual(q["complements"][0]["object"]["numerical_value"], 2)
        for invalid in ("vidi uman", "vidi domem umanem",
                        "vidi kun", "faki kun umanem"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                self.u.parse_sentence(invalid)

    def test_locative_fronting_preserves_ambiguity(self):
        q = self.u.parse_sentence("domin movi")
        self.assertEqual(q["preposed_locative"]["attachment"], "undetermined")
        self.assertEqual(q["preposed_locative"]["phrase"]["lemma"], "dom")
        q = self.u.parse_sentence("nationin auti umande mov")
        self.assertEqual(q["preposed_locative"]["attachment"], "undetermined")
        self.assertEqual(q["source"]["lemma"], "uman")
        q = self.u.parse_sentence("nationin no auti umande mov")
        self.assertTrue(q["negative"])

    def test_local_coordination_vs_wide_negation(self):
        local = self.u.parse_sentence("no vidi e movi")
        wide = self.u.parse_sentence("no lim vidi e movi")
        self.assertEqual(local["kind"], "coordination")
        self.assertTrue(local["left"]["negative"])
        self.assertEqual(local["operator"], "e")
        self.assertEqual(wide["kind"], "wide_negation")
        self.assertEqual(wide["operand"]["operator"], "e")
        contrasted = self.u.parse_sentence("no vidi ma movi")
        self.assertEqual(contrasted["relation"], "adversative")
        self.assertEqual(self.u.parse_sentence("no lim vidi o movi")["operand"]["relation"], "inclusive_or")
        with self.assertRaises(ValueError):
            self.u.parse_sentence("no lim vidi ma movi")

    def test_right_association_and_explicit_lim(self):
        unmarked = self.u.parse_sentence("vidi e movi o faki")
        self.assertEqual(unmarked["operator"], "e")
        self.assertEqual(unmarked["right"]["operator"], "o")
        marked = self.u.parse_sentence("vidi e movi lim o faki")
        self.assertEqual(marked["operator"], "o")
        self.assertEqual(marked["left"]["operator"], "e")
        nested = self.u.parse_sentence("vidi ma movi lim ergo faki")
        self.assertEqual(nested["kind"], "inference_relation")
        self.assertEqual(nested["premise"]["operator"], "ma")
        scoped = self.u.parse_sentence("no lim vidi e movi lim o faki")
        self.assertEqual(scoped["operator"], "o")
        self.assertEqual(scoped["left"]["kind"], "wide_negation")
        for invalid in ("lim vidi e movi", "vidi e lim movi", "vidi e movi lim"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                self.u.parse_sentence(invalid)

    def test_exactly_one_is_nary_not_iterated_binary_xor(self):
        x = self.u.parse_sentence("o vidi o movi o faki")
        self.assertEqual(x["kind"], "exclusive_choice")
        self.assertEqual(len(x["alternatives"]), 3)
        self.assertEqual(x["semantics"], "exactly_one")
        x = self.u.parse_sentence("o vidi o movi e faki")
        self.assertEqual(len(x["alternatives"]), 2)
        self.assertEqual(x["alternatives"][1]["operator"], "e")
        x = self.u.parse_sentence("o vidi o movi lim e faki")
        self.assertEqual(x["operator"], "e")
        self.assertEqual(x["left"]["kind"], "exclusive_choice")
        x = self.u.parse_sentence("no lim o vidi o movi")
        self.assertEqual(x["kind"], "wide_negation")
        self.assertEqual(x["operand"]["kind"], "exclusive_choice")
        for invalid in ("o vidi", "o vidi o", "no o vidi o movi"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                self.u.parse_sentence(invalid)

    def test_cause_evidence_inference_remain_distinct(self):
        cause = self.u.parse_sentence("vidi due movi")
        evidence = self.u.parse_sentence("vidi nam movi")
        inference = self.u.parse_sentence("vidi ergo movi")
        self.assertEqual(cause["kind"], "causal_relation")
        self.assertEqual(evidence["kind"], "evidential_relation")
        self.assertEqual(inference["kind"], "inference_relation")
        self.assertIs(evidence["causal_implication"], False)
        np = self.u.parse_sentence("vidi domem due fakit")
        self.assertEqual(np["complements"][0]["relator"], "due")

    def test_subordinate_anteposed_postposed_and_nesting(self):
        for opener in ("se", "etsi", "etsise", "eksese"):
            x = self.u.parse_sentence(opener + " vidi alor movi")
            self.assertEqual(x["kind"], "subordinate")
            self.assertEqual(x["operator"], opener)
            self.assertEqual(x["placement"], "anteposed")
        a = self.u.parse_sentence("se se vidi alor movi alor faki")
        self.assertEqual(a["subordinate"]["operator"], "se")
        b = self.u.parse_sentence("se vidi alor se movi alor faki")
        self.assertEqual(b["matrix"]["operator"], "se")
        for opener in ("etsi", "etsise", "eksese"):
            x = self.u.parse_sentence("movi " + opener + " vidi")
            self.assertEqual(x["placement"], "postposed")
        for bad in ("se vidi, movi", "se vidi alor",
                    "movi alor vidi", "se vidi e movi alor faki"):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                self.u.parse_sentence(bad)

    def test_wh_questions_zero_copula_imperative(self):
        x = self.u.parse_sentence("kis vida?")
        self.assertEqual(x["question"]["role"], "subject")
        x = self.u.parse_sentence("kidem vidu?")
        self.assertEqual(x["question"]["role"], "object")
        x = self.u.parse_sentence("kos movan?")
        self.assertEqual(x["question"]["role"], "location")
        x = self.u.parse_sentence("kot dom vidu?")
        self.assertEqual(x["question"]["role"], "quantity")
        self.assertEqual(x["question"]["nominal_head"], "dom")
        x = self.u.parse_sentence("tik no bel")
        self.assertEqual(x["kind"], "zero_copula")
        self.assertTrue(x["negative"])
        x = self.u.parse_sentence("i no legal")
        self.assertEqual(x["kind"], "zero_copula")
        x = self.u.parse_sentence("no mov!")
        self.assertEqual(x["kind"], "imperative")
        self.assertTrue(x["negative"])
        with self.assertRaises(ValueError):
            self.u.parse_sentence("vidi?")
        with self.assertRaises(ValueError):
            self.u.parse_sentence("ka vidi e movi?")

    def test_fail_closed_and_size_guards(self):
        for invalid in ("", "xyzzy", "autin unknown", "vidi e",
                        "movi ma", "vidi ma no lim movi",
                        "se vidi alor movi e faki", "vidi lim movi",
                        "ka ka vidi?", "autii mov"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                self.u.parse_sentence(invalid)
        with self.assertRaises(ValueError):
            self.u.parse_proposition("vidi " * 129)


if __name__ == "__main__":
    unittest.main()
