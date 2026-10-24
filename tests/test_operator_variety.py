import json,unittest
from benchmarks.operator_variety import build,score,FIELDS
class OperatorVarietyTests(unittest.TestCase):
    def test_pack_and_scorer(self):
        q,key=build()
        self.assertEqual(len(q),8)
        self.assertEqual(sum(len(x["events"]) for x in key),24)
        rows=[{"id":x["id"],"answer":json.dumps({"events":x["events"]})} for x in key]
        result=score(key,rows)
        self.assertEqual(result["exact_events"],24)
        self.assertEqual(len(FIELDS),8)
    def test_incomplete_fails(self):
        _,key=build()
        with self.assertRaises(ValueError):score(key,[])
if __name__=="__main__":unittest.main()
