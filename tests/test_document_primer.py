import unittest
from benchmarks.document_primer import header
class PrimerTests(unittest.TestCase):
    def test_known(self):
        x=header(['aervok','umanplan','klartrak'])
        self.assertEqual(len(x['roots']),6)
        self.assertEqual(x['segments']['aervok'],['aer','vok'])
        self.assertFalse(x['canonical_changes'])
    def test_unknown(self):
        with self.assertRaises(ValueError):header(['invalidword'])
if __name__=='__main__':unittest.main()
