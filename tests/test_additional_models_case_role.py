"""Offline four-family addendum regression tests: no API calls."""
import json
import unittest
from formalization.core import Unisermo
from benchmarks.case_role_decoding import gold, load_corpus
from benchmarks.additional_models_case_role import MODELS, MAX_CALLS, planned, checked_prefix, compare

class FourModelsTests(unittest.TestCase):
    def test_two_additional_model_identifiers_and_identical_prompts(self):
        self.assertEqual(MODELS, {
            "mistral":"mistralai/mistral-small-3.2-24b-instruct",
            "gpt_oss":"openai/gpt-oss-20b",
        })
        plan=planned()
        self.assertEqual(len(plan),MAX_CALLS)
        for i in range(0,len(plan),2):
            a,b=plan[i:i+2]
            self.assertEqual(a["messages"],b["messages"])
            self.assertEqual(a["prompt_sha256"],b["prompt_sha256"])
            self.assertEqual({a["model_label"],b["model_label"]},set(MODELS))
            self.assertNotIn("/no_think",a["messages"][0]["content"])

    def data(self):
        docs={r["id"]:r for r in load_corpus()}
        lang=Unisermo()
        out=[]
        for i,q in enumerate(planned()):
            events=[gold(text,lang,q["condition"]) for text in docs[q["doc"]]["clauses"]]
            out.append({
                **{key:q[key] for key in ("id","doc","condition","model_label",
                                         "requested_model","prompt_sha256")},
                "call_order":i+1,"returned_model":q["requested_model"],
                "provider":"DeepInfra","finish_reason":"stop",
                "answer":json.dumps({"events":events}),
                "usage":{"prompt_tokens":150,"completion_tokens":95,
                         "total_tokens":245,"cost":0.00002},
            })
        return out

    def test_complete_scores_and_agreement(self):
        rows=self.data()
        report=compare(rows)
        for name in MODELS:
            self.assertEqual(report["new_model_results"][name]["scores"]["case"]["exact_clauses"],24)
            self.assertEqual(report["new_model_results"][name]["scores"]["role"]["exact_clauses"],24)
        self.assertEqual(report["new_model_agreement"]["role"],{"both_correct":24})
        self.assertEqual(report["new_model_agreement"]["case"],{"both_correct":24})
        rows[0]["answer"]='{"events":[{},{}]}'
        changed=compare(rows)
        self.assertEqual(changed["new_model_results"]["mistral"]["scores"]["case"]["exact_clauses"],22)

    def test_reject_incomplete_and_modified_prefix(self):
        rows=self.data()
        with self.assertRaises(ValueError): compare(rows[:-1])
        rows[1]["prompt_sha256"]="different"
        with self.assertRaises(ValueError): checked_prefix(rows)
        rows=self.data()
        rows[0]["provider"]="unknown"
        with self.assertRaises(ValueError): checked_prefix(rows)
        rows=self.data()
        rows[0]["call_order"]=2
        with self.assertRaises(ValueError): checked_prefix(rows)

if __name__=="__main__":
    unittest.main()
