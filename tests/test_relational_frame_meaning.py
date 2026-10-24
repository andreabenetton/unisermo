"""Offline tests for role-level relational decoding (no paid API calls)."""
import json
import unittest
from formalization.core import Unisermo
from benchmarks.relational_frame_meaning import (
    FIELDS,GUIDE,MAX_CALLS,OBSERVED_BUDGET_USD,CONDITIONS,
    decode,load_corpus,normalize,requests,score,
)


class RelationalMeaningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang=Unisermo()

    def test_corpus_parser_gate(self):
        rows=load_corpus()
        self.assertEqual(len(rows),12)
        self.assertEqual(sum(len(r["clauses"]) for r in rows),24)
        for r in rows:
            for sentence in r["clauses"]:
                event=normalize(sentence,self.lang)
                self.assertEqual(set(event),set(FIELDS))
                self.assertIsNone(event["patient"] if r["family"]=="transition" else event["source_state"])
        self.assertEqual(normalize("i movi akwaem domad.",self.lang)["destination"],"dom")
        self.assertEqual(normalize("akwa traesa solidad likwidde.",self.lang)["source_state"],"likwid")
        self.assertEqual(normalize("i traesi akwaem solidda.",self.lang)["result_state"],"solid")

    def test_questions_prevent_answer_leak_and_holdout(self):
        rows=load_corpus()
        qs=requests(rows)
        self.assertEqual(len(qs),MAX_CALLS)
        self.assertEqual(len({q["prompt_sha256"] for q in qs}),24)
        self.assertLess(OBSERVED_BUDGET_USD,.03)
        for r in rows:
            pair=[q for q in qs if q["doc"]==r["id"]]
            self.assertEqual({q["condition"] for q in pair},set(CONDITIONS))
            for q in pair:
                prompt=q["messages"][0]["content"]
                self.assertTrue(all(s in prompt for s in r["clauses"]))
                self.assertNotIn("expected_gold",prompt)
            self.assertNotIn(GUIDE,next(q for q in pair if q["condition"]=="cold")["messages"][0]["content"])

    def test_types_and_format(self):
        self.assertEqual(decode('{"events":[{},{}]}')[1],None)
        for raw in ("not json","[]",'{"events":[]}','{"events":[],"excess":0}'):
            self.assertIsNotNone(decode(raw)[1])

    def test_scoring_with_full_corpus_and_errors(self):
        rows=load_corpus()
        responses=[]
        for q in requests(rows):
            corpus_row=next(r for r in rows if r["id"]==q["doc"])
            events=[normalize(s,self.lang) for s in corpus_row["clauses"]]
            responses.append({
                "id":q["id"],"doc":q["doc"],"condition":q["condition"],
                "prompt_sha256":q["prompt_sha256"],
                "answer":json.dumps({"events":events}),
                "usage":{"prompt_tokens":180,"completion_tokens":220,"total_tokens":400,"cost":.0001}
            })
        result=score(responses,rows)
        self.assertEqual(result["comparisons"]["cold"]["exact_propositions"],24)
        self.assertEqual(result["comparisons"]["guided"]["exact_propositions"],24)
        responses[0]["answer"]='{"events":[{},{}]}'
        amended=score(responses,rows)
        self.assertEqual(sum(x["exact_propositions"] for x in amended["comparisons"].values()),46)
        with self.assertRaises(ValueError): score(responses[:-1],rows)
        responses[0]["prompt_sha256"]="wrong"
        with self.assertRaises(ValueError): score(responses,rows)

if __name__=="__main__":
    unittest.main()
