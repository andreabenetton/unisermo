"""Offline regression tests for two distinct model families on identical prompts."""
import json
import unittest
from collections import Counter

from formalization.core import Unisermo
from benchmarks.case_role_decoding import gold, load_corpus
from benchmarks.two_model_case_role import (
    MODELS, MAX_REQUESTS, MAX_OBSERVED_SPEND_USD, MAX_OUTPUT_TOKENS,
    PROVIDER, plan, compare,
)


class TwoModelCaseRoleTests(unittest.TestCase):
    def test_same_corpus_exact_prompts_and_order_balance(self):
        questions=plan()
        self.assertEqual(len(questions),MAX_REQUESTS)
        self.assertEqual(set(MODELS),{"qwen","gemma"})
        self.assertEqual(PROVIDER,"DeepInfra")
        self.assertLessEqual(MAX_OBSERVED_SPEND_USD,0.03)
        self.assertEqual(MAX_OUTPUT_TOKENS,340)
        groups={}
        for q in questions:
            groups.setdefault(q["id"],[]).append(q)
        self.assertEqual(len(groups),24)
        for same in groups.values():
            self.assertEqual(len(same),2)
            self.assertEqual({x["model_label"] for x in same},set(MODELS))
            self.assertEqual(same[0]["messages"],same[1]["messages"])
            self.assertEqual(same[0]["prompt_sha256"],same[1]["prompt_sha256"])
        self.assertEqual(sum(q["model_label"]=="qwen" for q in questions[:24]),12)
        self.assertEqual(sum(q["model_label"]=="gemma" for q in questions[:24]),12)

    def fixture(self):
        language=Unisermo()
        documents={x["id"]:x for x in load_corpus()}
        rows=[]
        for index,q in enumerate(plan()):
            doc=documents[q["doc"]]
            events=[gold(s,language,q["condition"]) for s in doc["clauses"]]
            rows.append({
                "id":q["id"],"doc":q["doc"],"condition":q["condition"],
                "model_label":q["model_label"],"requested_model":q["requested_model"],
                "prompt_sha256":q["prompt_sha256"],
                "returned_model":q["requested_model"],"provider":"DeepInfra",
                "finish_reason":"stop",
                "answer":json.dumps({"events":events}),
                "usage":{"prompt_tokens":250,"completion_tokens":95,"total_tokens":345,
                         "cost":0.00004},
            })
        return rows

    def test_equal_gold_and_joint_accuracy(self):
        rows=self.fixture()
        scored=compare(rows)
        self.assertEqual(scored["billable_responses"],48)
        for label in MODELS:
            for condition in ("case","role"):
                s=scored["model_results"][label]["conditions"][condition]
                self.assertEqual(s["exact_clauses"],24)
                self.assertEqual(s["exact_tags"],48)
        for condition in ("case","role"):
            self.assertEqual(scored["exact_event_agreement"][condition],{"both_correct":24})
        # Introduce a model-specific tag confusion.
        r=next(x for x in rows if x["model_label"]=="gemma" and x["condition"]=="role")
        data=json.loads(r["answer"])
        data["events"][0]["args"][0]["tag"]="result"
        r["answer"]=json.dumps(data)
        changed=compare(rows)
        self.assertEqual(changed["model_results"]["gemma"]["conditions"]["role"]["exact_clauses"],23)
        self.assertEqual(changed["model_results"]["qwen"]["conditions"]["role"]["exact_clauses"],24)
        self.assertEqual(changed["exact_event_agreement"]["role"],{
            "both_correct":23,"qwen_only":1
        })

    def test_incomplete_and_mismatched_requests_fail(self):
        rows=self.fixture()
        with self.assertRaises(ValueError):
            compare(rows[:-1])
        rows[0]["prompt_sha256"]="a different prompt"
        with self.assertRaises(ValueError):
            compare(rows)
        rows=self.fixture()
        rows[1]["requested_model"]="qwen/qwen3-32b"
        with self.assertRaises(ValueError):
            compare(rows)

if __name__=="__main__":
    unittest.main()
