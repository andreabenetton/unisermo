import unittest
from benchmarks.open_inference import build,score,extract
class OpenInferenceTests(unittest.TestCase):
    def test_pairing(self):
        q,k=build()
        self.assertEqual(len(q),48)
        self.assertEqual(len(k),48)
        self.assertEqual(sum(x["root"]=="dir" for x in k),16)
        self.assertTrue(all("answer" not in v for v in q))
    def test_scorer(self):
        q,k=build()
        rows=[{"id":v["id"],"answer":'{"verb":"'+("say" if v["meaning"]=="say" else "guide")+'"}'} for v in k]
        x=score(k,rows,"synthetic-fixture")
        self.assertEqual(sum(c["recognized"] for c in x["groups"]),48)
        self.assertEqual(extract('{"verb":"tell"}'),"tell")
        self.assertIsNone(extract("say"))
    def test_unbalanced(self):
        q,k=build()
        with self.assertRaisesRegex(ValueError,"incomplete"):
            score(k,[],"synthetic")
if __name__=="__main__":unittest.main()
