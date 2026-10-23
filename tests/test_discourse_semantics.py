import json
import unittest
from benchmarks.discourse_semantics import build,score
class SemanticSlotTests(unittest.TestCase):
    def test_ideal_answers(self):
        q,key=build()
        self.assertEqual(len(q),6)
        answers=[{'id':item['id'],'answer':json.dumps({'events':item['events']})} for item in key]
        result=score(key,answers)
        self.assertEqual(result['correct_events'],18)
        self.assertEqual(result['total_events'],18)
    def test_missing(self):
        _,key=build()
        with self.assertRaises(ValueError):score(key,[])
if __name__=='__main__':unittest.main()
