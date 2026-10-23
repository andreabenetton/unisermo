import unittest
from benchmarks.productive_compounds import build_report

class TestProductiveCompounds(unittest.TestCase):
    def test_mechanical_validation_only(self):
        r=build_report()
        self.assertEqual(r["count"],12)
        self.assertEqual(r["errors"],[])
        self.assertTrue(all(x["meaning_status"]=="not_semantically_reviewed" for x in r["cases"]))
        self.assertEqual(sum(x["evidence"]=="confirmed_compound" for x in r["cases"]),3)
        self.assertTrue(any(x["warning"]=="mov_standalone_status_unconfirmed" for x in r["cases"]))

if __name__=="__main__": unittest.main()
