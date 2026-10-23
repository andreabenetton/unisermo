import unittest
from benchmarks.build_discourse_001 import build
class DiscourseTests(unittest.TestCase):
    def test_six_documents(self):
        docs=build()
        self.assertEqual(len(docs),6)
        self.assertEqual(sum(len(d["clauses"]) for d in docs),18)
        self.assertTrue(all(not d["canonical_changes"] for d in docs))
        self.assertTrue(all(d["status"]=="structurally_verified_semantics_unreviewed" for d in docs))
        for d in docs:
            self.assertEqual(len({e["verb"] for e in d["expected_events"]}),3)
            self.assertEqual(len({e["object"] for e in d["expected_events"]}),1)
if __name__=="__main__":unittest.main()
