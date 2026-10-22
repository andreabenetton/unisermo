import collections
import copy
import unittest

from benchmarks.root_recognition import build_pack, score, validate_responses


class RootRecognitionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.questions, cls.key = build_pack()

    def test_pack_is_balanced_and_keys_stay_separate(self):
        self.assertEqual(len(self.questions), 72)
        self.assertEqual(len(self.key), 72)
        self.assertEqual(len({x["id"] for x in self.questions}), 72)
        self.assertEqual([x["id"] for x in self.questions],
                         [x["id"] for x in self.key])
        for question in self.questions:
            self.assertNotIn("expected_choice", question)
            self.assertNotIn("expected_sense", question)
            self.assertEqual(len(question["messages"]), 1)
            self.assertTrue(question["independent_conversation_required"])
        categories = collections.Counter((x["condition"], x["root"], x["split"]) for x in self.key)
        for condition in ("unglossed", "explicit_glossary"):
            for root in ("dik", "dir", "dirig"):
                self.assertEqual(categories[condition, root, "development"], 9)
                self.assertEqual(categories[condition, root, "frozen_evaluation"], 3)
                letters = collections.Counter(x["expected_choice"] for x in self.key
                    if x["condition"] == condition and x["root"] == root)
                self.assertEqual(letters, collections.Counter({"A": 4, "B": 4, "C": 4}))

    def test_unglossed_has_no_root_dictionary(self):
        for question in self.questions:
            text = question["messages"][0]["content"]
            if question["condition"] == "unglossed":
                self.assertNotIn("dir=say", text)
                self.assertNotIn("dik=say", text)
            else:
                self.assertIn("dir=say", text)
                self.assertIn("dirig=direct", text)

    def test_scoring_with_fake_perfect_predictions(self):
        responses = [{"id": x["id"], "answer": x["expected_choice"]} for x in self.key]
        result = score(self.key, responses, "synthetic-unit-test-only")
        self.assertEqual(result["questions_scored"], 72)
        self.assertTrue(all(row["accuracy"] == 1 for row in result["summary"]))
        self.assertTrue(all(row["dir_only_correct"] == 0
                            and row["dik_only_correct"] == 0
                            for row in result["paired_comparison"]))
        self.assertEqual(result["status"], "model_answers_scored_not_human_validation")
        self.assertFalse("per_item_results" in result)

    def test_pairwise_scoring_is_directional_and_aggregate(self):
        responses = [{"id": x["id"], "answer": x["expected_choice"]} for x in self.key]
        victim = next(x for x in self.key if x["root"] == "dik"
                      and x["condition"] == "unglossed" and x["split"] == "development")
        for row in responses:
            if row["id"] == victim["id"]:
                row["answer"] = next(c for c in "ABC" if c != victim["expected_choice"])
        result = score(self.key, responses, "synthetic-unit-test-only")
        pair = next(x for x in result["paired_comparison"]
                    if x["condition"] == "unglossed" and x["split"] == "development")
        self.assertEqual(pair["dir_only_correct"], 1)
        self.assertEqual(pair["dik_only_correct"], 0)

    def test_unknown_missing_duplicate_are_rejected(self):
        responses = [{"id": x["id"], "answer": x["expected_choice"]} for x in self.key]
        with self.assertRaisesRegex(ValueError, "missing responses"):
            validate_responses(responses[:-1], self.key)
        with self.assertRaisesRegex(ValueError, "duplicate response"):
            validate_responses(responses + [responses[0]], self.key)
        altered = copy.deepcopy(responses)
        altered[0]["id"] = "UNKNOWN"
        with self.assertRaisesRegex(ValueError, "unknown trial id"):
            validate_responses(altered, self.key)

    def test_malformed_model_answer_counts_as_error(self):
        responses = [{"id": x["id"], "answer": x["expected_choice"]} for x in self.key]
        responses[0]["answer"] = "The answer is A because ..."
        result = score(self.key, responses, "synthetic-unit-test-only")
        group = next(x for x in result["summary"] if
                     x["condition"] == self.key[0]["condition"]
                     and x["root"] == self.key[0]["root"]
                     and x["split"] == self.key[0]["split"])
        self.assertEqual(group["malformed"], 1)
        self.assertEqual(group["correct"], group["samples"] - 1)

    def test_missing_model_id_is_rejected(self):
        responses = [{"id": x["id"], "answer": x["expected_choice"]} for x in self.key]
        with self.assertRaisesRegex(ValueError, "model ID"):
            score(self.key, responses, "")


if __name__ == "__main__":
    unittest.main()
