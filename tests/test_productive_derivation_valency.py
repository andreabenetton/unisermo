"""Executable conformance of approved derivation and argument-frame rules.

No derived form is added to the confirmed lexicon merely by parsing it.
Documented lexicalized or ambiguous exceptions are preserved.
"""
import unittest

from formalization.core import Unisermo


class ProductiveDerivationAndValencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = Unisermo()

    def test_nominal_suffixes_and_post_derivation_case(self):
        for form, base, operation in (
            ("fakor", "fak", "agent"),
            ("dokor", "dok", "agent"),
            ("fakil", "fak", "instrument"),
            ("fakia", "fak", "domain_place"),
            ("klaritat", "klar", "abstract_quality"),
            ("umanitat", "uman", "abstract_quality"),
        ):
            with self.subTest(form=form):
                d = self.u.parse_derivation(form)
                self.assertIsNotNone(d)
                self.assertEqual(d["base"], base)
                self.assertEqual(d["category"], "noun")
                self.assertEqual(d["operation"], operation)
                self.assertEqual(d["status"], "productive_from_confirmed")
                self.assertNotIn(form, self.u.lexicon)
                self.assertEqual(self.u.generate_noun(form), form)
                lemma = [x for x in self.u.analyze_word(form)["analyses"]
                         if x["kind"] == "nominal_case"]
                self.assertEqual(len(lemma), 1)
                self.assertEqual(lemma[0]["case"], "nominative")
                self.assertEqual(lemma[0]["status"], "productive_from_confirmed")
        self.assertEqual(self.u.generate_noun("fakor", "accusative"), "fakorem")
        self.assertEqual(self.u.generate_noun("fakia", "genitive"), "fakias")
        self.assertEqual(self.u.generate_noun("klaritat", "accusative"), "klaritatem")
        x = self.u.parse_sentence("vidi fakorem")
        self.assertEqual(x["object"]["lemma"], "fakor")
        self.assertEqual(x["object"]["lexical_status"], "productive_from_confirmed")
        self.assertEqual(self.u.parse_sentence("vidi klaritatem")["object"]["lemma"], "klaritat")

    def test_relational_adjectives_have_distinct_role(self):
        d = self.u.parse_derivation("fakal")
        self.assertEqual(d["category"], "adjective")
        self.assertEqual(d["operation"], "relational_adjective")
        word = self.u.analyze_word("fakal")["analyses"]
        self.assertEqual([x["kind"] for x in word], ["derived_adjective"])
        clause = self.u.parse_sentence("vidi fakal domem")
        self.assertEqual(clause["object"]["lemma"], "dom")
        self.assertEqual(clause["object"]["relational_adjectives"][0]["base"], "fak")
        with self.assertRaises(ValueError):
            self.u.generate_noun("fakal")
        for text in ("vidi fakal ter domem", "vidi fakal bon domem"):
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.u.parse_sentence(text)

    def test_ratified_passive_abil_suffix(self):
        for form, root in (("movabil", "mov"), ("vidabil", "vid"),
                           ("dikabil", "dik"), ("fakabil", "fak"),
                           ("portarabil", "portar")):
            with self.subTest(form=form):
                d = self.u.parse_derivation(form)
                self.assertIsNotNone(d)
                self.assertEqual((d["base"], d["affix"], d["category"],
                                  d["operation"]),
                                 (root, "abil", "adjective", "passive_potential"))
                self.assertEqual(self.u.analyze_word(form)["analyses"][0]["kind"],
                                 "derived_adjective")
                self.assertNotIn(form, self.u.lexicon)
        for form in ("abil", "potabil", "debabil", "esabil", "fonabil",
                     "movabilitat", "refakabil"):
            with self.subTest(unlicensed=form):
                self.assertIsNone(self.u.parse_derivation(form))

    def test_phase_and_associative_prefixes_are_regular_finite_verbs(self):
        for form, base, op in (
            ("refak", "fak", "phase_resume"),
            ("adfak", "fak", "phase_begin"),
            ("infak", "fak", "phase_continue"),
            ("defak", "fak", "phase_cease"),
            ("kunfak", "fak", "joint_event"),
            ("adpens", "pens", "phase_begin"),
            ("refern", "fern", "phase_resume"),
        ):
            if base == "fern":  # A hypothetical base is NEVER authorized.
                self.assertIsNone(self.u.parse_derivation(form))
                continue
            with self.subTest(form=form):
                d = self.u.parse_derivation(form)
                self.assertEqual((d["base"], d["operation"], d["category"]),
                                 (base, op, "verb"))
                finite = self.u.generate_verb(form, "past", person=2)
                analyses = [x for x in self.u.analyze_word(finite)["analyses"]
                            if x["kind"] == "finite_verb"]
                self.assertEqual(len(analyses), 1)
                self.assertEqual(analyses[0]["lemma"], form)
                self.assertEqual(analyses[0]["tense"], "past")
                self.assertEqual(analyses[0]["person"], 2)
        x = self.u.parse_sentence("refaki")
        self.assertEqual(x["predicate"]["lemma"], "refak")
        self.assertEqual(self.u.parse_sentence("kunfaki")["predicate"]["lemma"], "kunfak")
        z = self.u.parse_sentence("debi refak")
        self.assertEqual(z["dependent"]["lemma"], "refak")
        self.assertEqual(self.u.parse_sentence("kunfak!")["verb"], "kunfak")

    def test_derived_phase_participles_can_take_nominal_cases(self):
        self.assertEqual(self.u.generate_participle("refak"), "refakit")
        self.assertEqual(self.u.generate_noun("refakit", "accusative"), "refakitem")
        kinds = {x["kind"] for x in self.u.analyze_word("refakit")["analyses"]}
        self.assertIn("participle", kinds)
        self.assertIn("nominal_case", kinds)
        x = self.u.parse_sentence("vidi refakitem")
        self.assertEqual(x["object"]["lemma"], "refakit")

    def test_lexicalization_and_unapproved_derivations_fail_closed(self):
        for literal in ("major", "kunten", "portar", "nelegal"):
            with self.subTest(form=literal):
                self.assertIsNone(self.u.parse_derivation(literal))
                self.assertIn(literal, self.u.lexicon)
        self.assertIsNone(self.u.parse_derivation("nedom"))
        self.assertIsNone(self.u.parse_derivation("nemedi"))
        self.assertIsNone(self.u.parse_derivation("fakorar"))  # no invented suffix
        self.assertIsNone(self.u.parse_derivation("refakor"))  # no chaining yet
        self.assertIsNone(self.u.parse_derivation("deportari"))  # finite surface, not root
        self.assertEqual(self.u.parse_derivation("nebel")["operation"], "semantic_antonym")
        with self.assertRaises(ValueError):
            self.u.generate_verb("nebel")
        self.assertEqual(self.u.parse_sentence("tik nebel")["kind"], "zero_copula")

    def test_documented_motion_valency(self):
        base = self.u.parse_sentence("movi")
        self.assertEqual(base["kind"], "svo_clause")
        self.assertEqual(base["valency"], "motion_intransitive")
        causative = self.u.parse_sentence("movi domem")
        self.assertEqual(causative["valency"], "motion_causative")
        self.assertEqual(causative["object"]["lemma"], "dom")
        directed = self.u.parse_sentence("movi domem umanad")
        self.assertEqual(directed["valency"], "motion_causative")
        self.assertEqual(directed["complements"][0]["case"], "dative_allative")
        for form in ("admov", "inmov", "demov", "remov", "kunmov", "altmov", "basmov"):
            if form not in self.u.verbs and self.u.parse_derivation(form) is None:
                continue
            with self.subTest(lemma=form):
                word = self.u.generate_verb(form)
                x = self.u.parse_sentence(word + " domem")
                self.assertEqual(x["valency"], "motion_causative")
        with self.assertRaises(ValueError):
            self.u.parse_sentence("movi domin domin")

    def test_traes_exact_frames_and_absence_of_lexical_overreach(self):
        a = self.u.parse_sentence("traesi solidad likwidde")
        self.assertEqual(a["valency"], "state_transition")
        self.assertIsNone(a["object"])
        b = self.u.parse_sentence("traesi akwaem aperda")
        self.assertEqual(b["valency"], "causative_transformation")
        for text in ("traesi domem", "traesi akwaem domad",
                     "traesi solidad", "traesi solidad likwidde domin",
                     "traesi akwaem aperda kun uman"):
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.u.parse_sentence(text)
        generic = self.u.parse_sentence("faki domem")
        self.assertNotIn("valency", generic)
        modal = self.u.parse_sentence("debi mov domem umanad")
        self.assertEqual(modal["dependent"]["lemma"], "mov")
        self.assertEqual(modal["dependent"]["object"]["lemma"], "dom")
        with self.assertRaises(ValueError):
            self.u.parse_sentence("debi mov domin domin")

    def test_semantic_ratification_of_modal_capacity_result_without_surface_overreach(self):
        registry = self.u.valency["traes"]["modal_capacity_result"]
        self.assertEqual(registry["id"], "causative_modal_capacity")
        self.assertEqual(registry["status"], "ratified_semantics_surface_syntax_pending")
        self.assertEqual(registry["result"]["head"], "pot")
        self.assertEqual(registry["result"]["controller"], "accusative_patient")
        self.assertTrue(registry["result"]["entails_capacity_acquired"])
        self.assertFalse(registry["result"]["entails_dependent_action"])
        self.assertFalse(registry["result"]["entails_permission"])
        self.assertFalse(registry["parser_enabled"])
        for unratified_surface in ("traesi umanem pot movda",
                                   "traesi umanem aut movda",
                                   "traesi umanem pos movda"):
            with self.subTest(unratified_surface=unratified_surface):
                with self.assertRaises(ValueError):
                    self.u.parse_sentence(unratified_surface)

    def test_free_da_ad_de_state_markers(self):
        self.assertTrue({"da", "ad", "de"} <= self.u.lexicon.keys())
        for w in ("da", "ad", "de"):
            self.assertIn("function_word", self.u.lexicon[w]["categories"])
        made = self.u.parse_sentence("i traesi umanem da pot mov")
        self.assertEqual(made["valency"], "causative_modal_capacity")
        self.assertEqual(made["object"]["lemma"], "uman")
        self.assertEqual(made["state_result"]["head"], "pot")
        self.assertEqual(made["state_result"]["controller"], "accusative_patient")
        self.assertEqual(made["state_result"]["action"]["lemma"], "mov")
        self.assertTrue(made["state_result"]["entails_capacity_acquired"])
        self.assertFalse(made["state_result"]["entails_action"])
        change = self.u.parse_sentence("uman traesa ad pot mov de no pot mov")
        self.assertEqual(change["valency"], "state_transition")
        a = change["state_transition"]
        self.assertEqual(a["controller"], "matrix_subject")
        self.assertEqual(a["destination"]["head"], "pot")
        self.assertFalse(a["destination"]["negative"])
        self.assertTrue(a["source"]["negative"])
        simple = self.u.parse_sentence("uman traesa ad bon de nebon")
        self.assertEqual(simple["state_transition"]["destination"]["lemma"], "bon")
        self.assertEqual(simple["state_transition"]["source"]["lemma"], "nebon")
        previous = self.u.parse_sentence("traesi solidad likwidde")
        self.assertEqual(previous["valency"], "state_transition")
        previous2 = self.u.parse_sentence("traesi akwaem aperda")
        self.assertEqual(previous2["valency"], "causative_transformation")
        self.assertEqual(self.u.generate_verb("pot", "past", person=3), "potda")

    def test_free_state_markers_do_not_authorize_general_modal_scope(self):
        for text in (
            "i traesi umanem da aut mov",
            "i traesi umanem da pos mov",
            "i traesi umanem da no pot mov",
            "i traesi umanem da potda mov",
            "i traesi umanem da pot pot mov",
            "uman traesa ad pot mov",
            "uman traesa de no pot mov ad pot mov",
            "uman traesa ad pot mov de aut mov",
            "uman traesa ad pot mov de pot mov de pot mov",
            "i faki umanem da pot mov",
        ):
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.u.parse_sentence(text)

    def test_boundaries_and_provenance(self):
        frames = self.u.valency
        self.assertEqual(frames["schema"], "unisermo/valency-frames@1")
        self.assertEqual({f["id"] for f in frames["traes"]["frames"]},
                         {"state_transition", "causative_transformation"})
        self.assertIn("language/derivation.md#mov-valency-alternation", frames["sources"])
        self.assertEqual(self.u.parse_derivation("fakor")["status"],
                         "productive_from_confirmed")
        self.assertEqual(self.u.parse_derivation("vidil")["status"],
                         "productive_from_attested")


if __name__ == "__main__":
    unittest.main()
