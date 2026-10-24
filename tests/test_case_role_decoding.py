"""No-API tests for paired morphological-case / semantic-role labeling."""
import json
import unittest

from benchmarks.case_role_decoding import (
    CASE, ROLE, CALL_CAP, CONDITIONS, OBSERVED_USD_LIMIT,
    GUIDE, decode, evaluate, gold, load_corpus, requests,
)
from formalization.core import Unisermo


class CaseRoleDecodingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def test_source_licensed_development_only(self):
        rows = load_corpus()
        self.assertEqual(len(rows), 12)
        self.assertEqual(len(set(x for d in rows for x in d["clauses"])), 24)
        self.assertTrue(all(x["split"] == "development_only" for x in rows))

    def test_exact_case_vs_role_projection(self):
        x = "akwa traesoa solidad likwidde."
        g = gold(x, self.lang, "case")
        h = gold(x, self.lang, "role")
        self.assertEqual(g, {"verb":"traes","args":[
            {"stem":"solid","tag":"dative_allative"},
            {"stem":"likwid","tag":"ablative"}]})
        self.assertEqual(h, {"verb":"traes","args":[
            {"stem":"solid","tag":"destination"},
            {"stem":"likwid","tag":"source"}]})
        z = "i traesfi akwaem solidda."
        self.assertEqual([a["tag"] for a in gold(z,self.lang,"case")["args"]],
                         ["accusative","resultative"])
        self.assertEqual([a["tag"] for a in gold(z,self.lang,"role")["args"]],
                         ["patient","result"])
        self.assertEqual(gold("i movdi domem umanad.",self.lang,"role")["args"][1]["tag"],
                         "destination")

    def test_same_reference_across_conditions(self):
        rows = load_corpus()
        qs = requests(rows)
        self.assertEqual(len(qs), CALL_CAP)
        self.assertLess(OBSERVED_USD_LIMIT,.03)
        for row in rows:
            pair=[q for q in qs if q["doc"]==row["id"]]
            self.assertEqual({q["condition"] for q in pair},set(CONDITIONS))
            for q in pair:
                p = q["messages"][0]["content"]
                self.assertIn(GUIDE,p)
                for sentence in row["clauses"]:
                    self.assertIn(sentence,p)
                self.assertNotIn("expected_choice",p)

    def fake(self, labels):
        out=[]
        rows=load_corpus()
        for q in requests(rows):
            doc=next(x for x in rows if x["id"]==q["doc"])
            events=[gold(s,self.lang,q["condition"]) for s in doc["clauses"]]
            if labels == "swap_case_tags" and q["condition"]=="case":
                for evt in events:
                    evt["args"][0]["tag"]="resultative"
            out.append({
                "id":q["id"],"doc":q["doc"],"condition":q["condition"],
                "prompt_sha256":q["prompt_sha256"],
                "answer":json.dumps({"events":events}),
                "usage":{"prompt_tokens":100,"completion_tokens":110,
                         "total_tokens":210,"cost":0.00005}
            })
        return out

    def test_perfect_and_confusion_scores(self):
        scored=evaluate(self.fake(None))
        for c in CONDITIONS:
            s=scored["comparisons"][c]
            self.assertEqual(s["exact_clauses"],24)
            self.assertEqual(s["exact_arguments"],48)
            self.assertEqual(s["exact_stems"],48)
            self.assertEqual(s["exact_tags"],48)
        a=evaluate(self.fake("swap_case_tags"))
        self.assertEqual(a["comparisons"]["case"]["exact_clauses"],0)
        self.assertEqual(a["comparisons"]["role"]["exact_clauses"],24)
        self.assertEqual(a["comparisons"]["case"]["exact_stems"],48)
        self.assertEqual(a["comparisons"]["case"]["exact_tags"],24)

    def test_reject_partial_modified_and_wrong_format(self):
        result=self.fake(None)
        with self.assertRaises(ValueError):
            evaluate(result[:-1])
        result[0]["prompt_sha256"]="changed"
        with self.assertRaises(ValueError):
            evaluate(result)
        self.assertIsNotNone(decode('{"events":[]}')[1])
        self.assertIsNotNone(decode('{"events":[],"extra":1}')[1])
        self.assertIsNotNone(decode('not json')[1])
        self.assertEqual(decode('{"events":[{},{}]}')[1],None)

if __name__ == "__main__":
    unittest.main()
