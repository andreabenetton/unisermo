"""Resume invariants after cancelled Gemma provider run; offline only."""
import unittest
from benchmarks.two_model_case_role import plan
from benchmarks.gemma_case_role_followup import checked_resume_rows, gemma_plan


def fake_row(q, original_order, gemma_order):
    return {**{k:q[k] for k in ("id","doc","condition","model_label",
                             "requested_model","prompt_sha256")},
            "call_order":gemma_order,"original_call_order":original_order,
            "response_id":f"fixture-{original_order}","provider":"DeepInfra",
            "returned_model":q["requested_model"],"finish_reason":"stop",
            "answer":'{"events":[{},{}]}',
            "usage":{"cost":0.00004}}


class ReuseNineteenResponsesTest(unittest.TestCase):
    def fixture(self):
        originals=[]
        for i,q in enumerate(plan()[:14]):
            originals.append(fake_row(q,i+1,i+1))
        gplan=gemma_plan()
        gemma=[fake_row(q,i+1,i+1) for i,q in enumerate(gplan[:19])]
        for i,prior in enumerate(r for r in originals if r["model_label"]=="gemma"):
            gemma[i]=dict(prior)
            gemma[i]["original_call_order"]=prior["call_order"]
            gemma[i]["call_order"]=i+1
            gemma[i]["original_run"]=40091590850
        return originals,gemma

    def test_19_valid_replies_have_exactly_five_remaining_questions(self):
        original,gemma=self.fixture()
        self.assertEqual(len(checked_resume_rows(gemma,original)),19)
        self.assertEqual(len(gemma_plan()[len(gemma):]),5)

    def test_modified_original_reply_is_rejected(self):
        original,gemma=self.fixture()
        gemma[0]["answer"]="substituted"
        with self.assertRaises(ValueError):
            checked_resume_rows(gemma,original)

    def test_noncontiguous_order_is_rejected(self):
        original,gemma=self.fixture()
        gemma[18]["call_order"]=20
        with self.assertRaises(ValueError):
            checked_resume_rows(gemma,original)

    def test_partial_or_reordered_prefix_is_rejected(self):
        original,gemma=self.fixture()
        gemma[10],gemma[11]=gemma[11],gemma[10]
        with self.assertRaises(ValueError):
            checked_resume_rows(gemma,original)

if __name__=="__main__":
    unittest.main()
