import unittest

from formalization.core import Unisermo
from benchmarks.root_semantic_guard import (
    BASE, PROPOSAL, evaluate, paired_inputs, shadow_reference_language,
    structure,
)


class RootSemanticGuardTests(unittest.TestCase):
    def test_canonical_language_is_not_mutated(self):
        baseline = Unisermo()
        candidate = shadow_reference_language()
        self.assertIn(BASE, baseline.verbs)
        self.assertNotIn(PROPOSAL, baseline.lexicon)
        self.assertNotIn(BASE, candidate.verbs)
        self.assertIn(PROPOSAL, candidate.verbs)
        self.assertIn("dirig", candidate.verbs)

    def test_full_finite_paradigm_with_pronouns_negation_questions(self):
        reference = Unisermo()
        rows = paired_inputs(reference.morph)
        self.assertEqual(len(rows), 54 * 4 + 5)
        for shape in ("pro_drop", "explicit_subject", "negated", "polar_question"):
            self.assertEqual(sum(x["shape"] == shape for x in rows), 54)

    def test_parser_parity_is_exact_without_semantic_approval(self):
        result = evaluate()
        self.assertEqual(result["generated_pairs"], 221)
        self.assertEqual(result["passing_pairs"], 221, result["failures"])
        self.assertEqual(result["controls_passed"], 8, result["failures"])
        self.assertEqual(result["failures"], [])
        self.assertEqual(result["semantic_review"], "not_independently_verified")
        self.assertIsNone(result["recognition_evidence"])

    def test_dirig_remains_independent(self):
        baseline, candidate = Unisermo(), shadow_reference_language()
        for sample in ("dirigi.", "ka u dirigdu?", "no diriga."):
            a, b = baseline.parse_sentence(sample), candidate.parse_sentence(sample)
            self.assertEqual(a["predicate"]["lemma"], "dirig")
            self.assertEqual(structure(a), structure(b))

    def test_demonstrative_tik_is_not_reinterpreted_as_say(self):
        old, new = Unisermo(), shadow_reference_language()
        a = old.parse_sentence("ka i no diki tik fakitem?")
        b = new.parse_sentence("ka i no diri tik fakitem?")
        self.assertEqual(structure(a), structure(b))
        self.assertEqual(b["object"]["modifiers"], ["tik"])
        self.assertEqual(b["predicate"]["lemma"], "dir")


if __name__ == "__main__":
    unittest.main()
