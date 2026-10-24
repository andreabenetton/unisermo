"""No-API regression tests for prospective repeated development schema experiment."""
import json
import unittest
from benchmarks.schema_repeatability_runner import make_requests, summarize

class SchemaProspectiveTests(unittest.TestCase):
    def test_balanced_fixed_prompt_32(self):
        requests, truth = make_requests()
        self.assertEqual(len(requests), 32)
        self.assertEqual(len(truth), 8)
        self.assertEqual(len(set(r["id"] for r in requests)), 32)
        for doc in truth:
            for condition in ("generic", "strict"):
                selected = [r for r in requests if r["doc"] == doc and r["condition"] == condition]
                self.assertEqual(len(selected), 2)
                self.assertEqual(selected[0]["messages"], selected[1]["messages"])
                self.assertEqual(selected[0]["prompt_sha256"], selected[1]["prompt_sha256"])

    def test_scoring_and_stability(self):
        queue, truth = make_requests()
        rows = []
        for q in queue:
            row = {k: q[k] for k in ("id", "doc", "condition", "repetition")}
            row["answer"] = json.dumps({"events": truth[q["doc"]]})
            row["usage"] = {"cost": 0.0001, "prompt_tokens": 100, "completion_tokens": 80, "total_tokens": 180}
            rows.append(row)
        result = summarize(rows, truth)
        self.assertEqual(result["conditions"]["generic"]["exact_events"], 48)
        self.assertEqual(result["conditions"]["strict"]["exact_events"], 48)
        self.assertEqual(result["stability"]["generic"]["equal_feature_vectors"], 24)
        self.assertEqual(result["exact_cluster_sign_flip_p_two_sided_exploratory"], 1.0)
        # Perturb one event in just one strict repetition; document clustering survives.
        rows[0]["answer"] = json.dumps({"events": [
            {**event, "interrogative": not event["interrogative"]} if i == 0 else event
            for i, event in enumerate(truth[rows[0]["doc"]])
        ]})
        revised = summarize(rows, truth)
        self.assertEqual(sum(v["exact_events"] for v in revised["conditions"].values()), 95)

    def test_invalid_or_incomplete_fails(self):
        requests, truth = make_requests()
        with self.assertRaises(ValueError):
            summarize([], truth)

if __name__ == "__main__":
    unittest.main()
