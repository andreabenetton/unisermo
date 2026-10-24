"""Offline semantic-contrast benchmark regressions, no API calls."""
import json
import unittest
from benchmarks.semantic_contrast import (
    CORPUS, GUIDE, MAX_COST_USD, MAX_REQUESTS, build_questions, load_corpus, parse_choice, score
)

class SemanticContrastTest(unittest.TestCase):
    def test_corpus_attested_balanced_and_development(self):
        corpus = load_corpus()
        self.assertEqual(len(corpus), 30)
        self.assertEqual(sum(x["expected_choice"] == "A" for x in corpus), 15)
        self.assertTrue(all(x["split"] == "development_not_holdout" for x in corpus))
        self.assertTrue(all(x["canonical_changes"] is False for x in corpus))

    def test_prompt_has_no_answer_key(self):
        corpus = load_corpus()
        calls = build_questions(corpus)
        self.assertEqual(len(calls), MAX_REQUESTS)
        self.assertEqual(len({q["id"] for q in calls}), MAX_REQUESTS)
        self.assertLess(MAX_COST_USD, 0.05)
        for item in corpus:
            pair = [q for q in calls if q["doc"] == item["id"]]
            self.assertEqual(len(pair), 2)
            self.assertEqual({q["condition"] for q in pair},{"cold","guided"})
            for q in pair:
                prompt = q["messages"][0]["content"]
                self.assertIn(item["option_A"],prompt)
                self.assertIn(item["option_B"],prompt)
                self.assertIn(item["question_en"],prompt)
                self.assertNotIn("expected_choice",prompt)
            self.assertIn(GUIDE,pair[0]["messages"][0]["content"]+pair[1]["messages"][0]["content"])
            cold = next(q for q in pair if q["condition"] == "cold")
            self.assertNotIn(GUIDE,cold["messages"][0]["content"])

    def test_exact_json_choice(self):
        self.assertEqual(parse_choice('{"choice":"A"}'),("A",None))
        self.assertEqual(parse_choice('```json\n{"choice":"B"}\n```'),("B",None))
        self.assertIsNotNone(parse_choice('{"choice":"A","explanation":"x"}')[1])
        self.assertIsNotNone(parse_choice('A')[1])
        self.assertIsNotNone(parse_choice('{"choice":true}')[1])
        self.assertIsNotNone(parse_choice('{"choice":"C"}')[1])

    def test_score_and_pairing(self):
        corpus = load_corpus()
        answers = []
        for q in build_questions(corpus):
            item = next(x for x in corpus if x["id"] == q["doc"])
            answers.append({
                "id":q["id"],"doc":q["doc"],"condition":q["condition"],
                "answer":json.dumps({"choice":item["expected_choice"]}),
                "usage":{"prompt_tokens":200,"completion_tokens":8,"total_tokens":208,"cost":0.0001}
            })
        summary = score(answers, corpus)
        self.assertEqual(summary["paired_outcomes"],{"both_correct":30})
        self.assertEqual(summary["conditions"]["cold"]["correct"],30)
        self.assertEqual(summary["conditions"]["guided"]["correct"],30)
        answers[0]["answer"] = '{"choice":"invalid"}'
        result = score(answers, corpus)
        self.assertEqual(sum(v["correct"] for v in result["conditions"].values()),59)
        self.assertEqual(sum(result["paired_outcomes"].values()),30)
        with self.assertRaises(ValueError):
            score(answers[:-1],corpus)
        with self.assertRaises(ValueError):
            score(answers[:-1]+[answers[0]],corpus)

if __name__=="__main__":
    unittest.main()
