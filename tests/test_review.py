import copy
import unittest
from benchmarks.review import validate, records, PILOT, LEDGER

class ReviewLedgerTests(unittest.TestCase):
    def setUp(self):
        self.pilot=records(PILOT)
        self.ledger=records(LEDGER)

    def test_complete_but_no_unearned_approvals(self):
        result=validate(self.pilot,self.ledger)
        self.assertEqual(result["total"],78)
        self.assertEqual(result["verified"],0)

    def test_reject_missing_ids(self):
        with self.assertRaisesRegex(ValueError,"exactly"):
            validate(self.pilot,self.ledger[:-1])

    def test_reject_source_drift(self):
        changed=copy.deepcopy(self.ledger)
        changed[0]["source_english"]="altered"
        with self.assertRaisesRegex(ValueError,"source drift"):
            validate(self.pilot,changed)

    def test_reject_unattributed_approval(self):
        changed=copy.deepcopy(self.ledger)
        changed[0]["status"]="verified"
        with self.assertRaisesRegex(ValueError,"reviewer"):
            validate(self.pilot,changed)

if __name__=="__main__":
    unittest.main()
