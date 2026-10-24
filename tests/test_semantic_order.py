"""Offline regression tests for paired A/B semantic-choice counterbalancing."""
import json
import unittest
from benchmarks.semantic_order import (
    MAX_COST_USD, MAX_REQUESTS, ORIENTATIONS, CONDITIONS,
    load_corpus, make_requests, score,
)

class SemanticOrderTests(unittest.TestCase):
    def test_design_new_source_pairs_and_counterbalance(self):
        rows = load_corpus()
        requests = make_requests(rows)
        self.assertEqual(len(rows), 20)
        self.assertEqual(len(requests), MAX_REQUESTS)
        self.assertEqual({r["orientation"] for r in requests},set(ORIENTATIONS))
        self.assertEqual({r["condition"] for r in requests},set(CONDITIONS))
        self.assertLess(MAX_COST_USD, 0.04)
        for item in rows:
            q = [r for r in requests if r["doc"] == item["id"]]
            self.assertEqual(len(q),4)
            self.assertEqual({(r["condition"],r["orientation"]) for r in q},
                {(c,o) for c in CONDITIONS for o in ORIENTATIONS})
            for r in q:
                msg=r["messages"][0]["content"]
                self.assertIn(item["target_expression"],msg)
                self.assertIn(item["distractor_expression"],msg)
                self.assertIn(item["question_en"],msg)
                self.assertNotIn("expected_choice",msg)
                self.assertNotIn("target_expression",msg)
                self.assertNotIn("distractor_expression",msg)
            self.assertEqual(sum(r["expected_choice"]=="A" for r in q),2)
        self.assertEqual(len({r["prompt_sha256"] for r in requests}),80)

    @staticmethod
    def example_answers(label_function):
        rows = []
        for q in make_requests():
            ans = label_function(q)
            rows.append({
                "id":q["id"],"doc":q["doc"],"condition":q["condition"],
                "orientation":q["orientation"],"prompt_sha256":q["prompt_sha256"],
                "answer":json.dumps({"choice":ans}),
                "usage":{"prompt_tokens":42,"completion_tokens":9,"total_tokens":51,"cost":0.00001}
            })
        return rows

    def test_perfect_answers(self):
        rows = self.example_answers(lambda q:q["expected_choice"])
        x = score(rows)
        for condition in CONDITIONS:
            result = x["comparisons"][condition]
            self.assertEqual(result["correct_presentations"],40)
            self.assertEqual(result["correct_both_orientations"],20)
            self.assertEqual(result["position_sticking_A"],0)
            self.assertEqual(result["distractor_both_orientations"],0)

    def test_always_a_bias(self):
        rows = self.example_answers(lambda q:"A")
        x = score(rows)
        for condition in CONDITIONS:
            result=x["comparisons"][condition]
            self.assertEqual(result["correct_presentations"],20)
            self.assertEqual(result["correct_both_orientations"],0)
            self.assertEqual(result["position_sticking_A"],20)
            self.assertEqual(result["position_sticking_B"],0)

    def test_always_distractor_is_not_position_bias(self):
        rows = self.example_answers(lambda q:"B" if q["expected_choice"]=="A" else "A")
        x = score(rows)
        for condition in CONDITIONS:
            result=x["comparisons"][condition]
            self.assertEqual(result["correct_presentations"],0)
            self.assertEqual(result["distractor_both_orientations"],20)
            self.assertEqual(result["position_sticking_A"],0)

    def test_rejects_incomplete_foreign_and_tampered_prompt(self):
        rows=self.example_answers(lambda q:q["expected_choice"])
        with self.assertRaises(ValueError):
            score(rows[:-1])
        rows[0]["prompt_sha256"]="changed"
        with self.assertRaises(ValueError):
            score(rows)

if __name__=="__main__":
    unittest.main()
