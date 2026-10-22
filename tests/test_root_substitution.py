import json
import unittest
from pathlib import Path

from benchmarks.lexical_screen import audit
from benchmarks.root_substitution import (
    DERIVATION_SUFFIXES, development_contexts, evaluate, full_finite,
    metrics, samples,
)
from benchmarks.run import load_corpus, PILOT

ROOT = Path(__file__).resolve().parents[1]
MORPH = json.loads((ROOT / "formalization/data/morphology.json").read_text())
LEXICON = json.loads((ROOT / "formalization/data/lexicon_index.json").read_text())["entries"]
REGISTER = json.loads((ROOT / "research/lexicon/candidate-register.json").read_text())


class FakeCounter:
    name = "fake-test-only"
    implementation = "synthetic-test-only"
    vocab_sha256 = None

    def count(self, text):
        return len(text)  # Tests shape only: NOT an actual token count.


class RootSubstitutionTests(unittest.TestCase):
    def test_proposals_are_exact_and_other_roots_frozen(self):
        active = {x["canonical"]: x["proposed_comparison"] for x in REGISTER["candidates"]}
        self.assertEqual(active["dik"], ["dir"])
        self.assertEqual(active["stru"], ["konstru", "kostru"])
        self.assertEqual(active["kurar"], [])
        self.assertEqual(active["sentr"], [])

    def test_source_constru_rejected_but_native_candidates_pass(self):
        self.assertFalse(audit("constru", "stru", MORPH, LEXICON)["inventory_valid"])
        for form, base in [("dir", "dik"), ("konstru", "stru"), ("kostru", "stru")]:
            result = audit(form, base, MORPH, LEXICON)
            self.assertTrue(result["inventory_valid"], form)
            self.assertEqual(result["exact_collisions"], [], form)

    def test_dik_tik_risk_is_reduced_by_dir(self):
        original = audit("dik", "dik", MORPH, LEXICON)
        candidate = audit("dir", "dik", MORPH, LEXICON)
        self.assertIn("tik", original["critical_grammar_risks"])
        self.assertNotIn("tik", candidate["critical_grammar_risks"])

    def test_morphology_examples_and_length(self):
        self.assertEqual(len(full_finite("dir", MORPH)), 54)
        old, new = samples("dik", MORPH), samples("dir", MORPH)
        self.assertIn("diki.", old["finite_pro_drop"])
        self.assertIn("diri.", new["finite_pro_drop"])
        self.assertIn("dikodi.", old["finite_pro_drop"])
        self.assertIn("dirodi.", new["finite_pro_drop"])
        self.assertEqual(len(new["nominal_case_hypotheses"]), 7)
        self.assertEqual(len(new["derivation_hypotheses"]), len(DERIVATION_SUFFIXES))
        self.assertIn("dirit", new["derivation_hypotheses"])

    def test_contexts_are_development_only(self):
        corpus = load_corpus(PILOT)
        contexts = development_contexts(corpus, "dik", "dir")
        expected = sum(
            r["split"] == "development" and r["grammatical_intent"].get("lemma") == "dik"
            for r in corpus
        )
        self.assertEqual(len(contexts), expected)
        self.assertGreater(expected, 0)
        self.assertTrue(all(a.startswith("dik") and b.startswith("dir") for _, a, b in contexts))
        self.assertFalse(development_contexts(corpus, "stru", "konstru"))

    def test_report_is_provisional_and_exposes_no_holdout(self):
        report = evaluate(FakeCounter(), MORPH, LEXICON, REGISTER, load_corpus(PILOT), {})
        self.assertEqual(len(report["comparisons"]), 3)
        self.assertIn("no_language_change", report["status"])
        self.assertIn("generated_inflections_and_development_only", report["study_split"])
        for result in report["comparisons"]:
            self.assertEqual(result["human_semantic_review"], "pending")
            self.assertIsNone(result["modern_spoken_recognizability"])
            self.assertEqual(result["token_groups"]["finite_pro_drop"]["samples"], 54)
            self.assertNotIn("holdout", result["token_groups"])
            self.assertEqual(result["token_groups"]["nominal_case_hypotheses"]["samples"], 7)

    def test_counter_is_used_not_character_guesses(self):
        class ConstantCounter:
            def count(self, text):
                return 2
        result = metrics(ConstantCounter(), ["diki."], ["diri."])
        self.assertEqual(result["baseline_tokens"], 2)
        self.assertEqual(result["alternative_tokens"], 2)
        self.assertEqual(result["extra_tokens"], 0)


if __name__ == "__main__":
    unittest.main()
