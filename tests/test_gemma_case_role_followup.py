"""Offline validation of authentic two-family follow-up and exact prefix reuse."""
import json
import unittest

from formalization.core import Unisermo
from benchmarks.case_role_decoding import gold,load_corpus,requests
from benchmarks.two_model_case_role import MODELS,plan
from benchmarks.gemma_case_role_followup import (
    QWEN_RAW,analyze,gemma_plan,restore_prefix,jsonl
)


class GemmaFollowupTests(unittest.TestCase):
    def test_real_original_qwen_valid(self):
        r=jsonl(QWEN_RAW)
        self.assertEqual(len(r),24)
        self.assertEqual({x["id"] for x in r},{q["id"] for q in requests()})
        self.assertTrue(all(x["returned_model"]==MODELS["qwen"]
                            and x["provider"]=="DeepInfra" for x in r))

    def test_original_gemma_prefix_order(self):
        q=gemma_plan()
        self.assertEqual(len(q),24)
        self.assertEqual(len({x["id"] for x in q}),24)
        partial=[]
        plan_rows=plan()
        for i,item in enumerate(plan_rows[:14]):
            partial.append({**{k:item[k] for k in
                        ("id","doc","condition","model_label","requested_model","prompt_sha256")},
                        "call_order":i+1,"provider":"DeepInfra",
                        "returned_model":item["requested_model"],"finish_reason":"stop",
                        "answer":"{}","usage":{"cost":0.00004}})
        prefix=restore_prefix(partial)
        self.assertEqual(len(prefix),7)
        self.assertEqual([r["id"] for r in prefix],[r["id"] for r in q[:7]])
        self.assertEqual([r["call_order"] for r in prefix],list(range(1,8)))
        self.assertEqual([r["original_call_order"] for r in prefix],[2,4,5,7,10,12,13])
        partial[1]["prompt_sha256"]="changed"
        with self.assertRaises(ValueError):
            restore_prefix(partial)

    def test_fair_task_pairing_and_agreement(self):
        lang=Unisermo()
        docs={x["id"]:x for x in load_corpus()}
        qwen=[]
        gemma=[]
        for q in requests():
            gold_events=[gold(sentence,lang,q["condition"]) for sentence in docs[q["doc"]]["clauses"]]
            for label,out in (("qwen",qwen),("gemma",gemma)):
                out.append({
                    "id":q["id"],"doc":q["doc"],"condition":q["condition"],
                    "prompt_sha256":q["prompt_sha256"],
                    "returned_model":MODELS[label],"provider":"DeepInfra","finish_reason":"stop",
                    "answer":json.dumps({"events":gold_events}),
                    "usage":{"prompt_tokens":150,"completion_tokens":95,"total_tokens":245,"cost":0.00004}
                })
        result=analyze(qwen,gemma)
        self.assertEqual(result["agreement_by_condition"]["case"],{"both_correct":24})
        self.assertEqual(result["agreement_by_condition"]["role"],{"both_correct":24})
        for condition in ("case","role"):
            for label in ("qwen","gemma"):
                self.assertEqual(result["comparisons"][label][condition]["exact_clauses"],24)
        qwen[0]["prompt_sha256"]="not-the-same-question"
        with self.assertRaises(ValueError):
            analyze(qwen,gemma)


if __name__=="__main__":
    unittest.main()
