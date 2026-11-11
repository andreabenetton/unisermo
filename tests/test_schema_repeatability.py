"""Offline regression tests for schema-repeatability scoring."""
import unittest
from benchmarks.schema_repeatability import analyze, decode, incorrect_fields

def truth():
    return {"lemma": "vid", "object_lemma": "akwa", "tense": "past",
            "aspect": "simple", "person": 2, "number": "singular",
            "negative": False, "interrogative": True}

class SchemaRepeatabilityTests(unittest.TestCase):
    def test_wrapped_and_array(self):
        self.assertEqual(decode('[{"a":1}]')[0], [{"a":1}])
        self.assertEqual(decode('```json\n{"events":[{"a":1}]}\n```')[0], [{"a":1}])
        self.assertEqual(decode('some text')[1], "invalid_json")
        self.assertEqual(decode('{"events":[],"extra":1}')[1], "invalid_wrapper")

    def test_types_are_not_coerced(self):
        wrong = {**truth(), "person": True, "number": 1}
        self.assertEqual(set(incorrect_fields(truth(), wrong)), {"person", "number"})

    def test_document_cluster(self):
        import json
        expected = truth()
        corpus = [{"id": f"D{i}", "events": [expected, expected, expected]} for i in (1,2)]
        ok = json.dumps([expected] * 3)
        bad = json.dumps([{**expected, "aspect": "progressive"}] * 3)
        rows = [
            {"id":"D1_generic","doc":"D1","condition":"generic","answer":bad},
            {"id":"D1_strict","doc":"D1","condition":"strict","answer":ok},
            {"id":"D2_generic","doc":"D2","condition":"generic","answer":ok},
            {"id":"D2_strict","doc":"D2","condition":"strict","answer":bad}
        ]
        result = analyze(corpus, rows, bootstrap_samples=1000)
        self.assertEqual(result["exact_events"], {"generic":3,"strict":3})
        self.assertEqual(result["document_differences"], [3,-3])
        self.assertEqual(result["exact_sign_flip_p_two_sided"], 1.0)
        self.assertEqual(result["field_errors"]["strict"], {"aspect":3})

    def test_refuses_incomplete_or_duplicate(self):
        doc = [{"id":"D1","events":[truth()]}]
        row = {"id":"D1_generic","doc":"D1","condition":"generic","answer":"[]"}
        with self.assertRaises(ValueError):
            analyze(doc,[row])
        with self.assertRaises(ValueError):
            analyze(doc,[row,row])

if __name__ == "__main__":
    unittest.main()
