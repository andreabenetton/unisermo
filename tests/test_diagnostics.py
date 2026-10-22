import copy
import hashlib
import json
import unittest
from pathlib import Path
from benchmarks.diagnostics import analyze
from benchmarks.run import PILOT, load_corpus

ROOT=Path(__file__).resolve().parents[1]
EVIDENCE=ROOT/'benchmarks/evidence'

class DiagnosticTests(unittest.TestCase):
    def setUp(self):
        self.reports=[json.loads(p.read_text()) for p in sorted(EVIDENCE.glob('*.json'))]
        self.corpus=load_corpus(PILOT)
        self.raw=PILOT.read_bytes()

    def test_results_validate_provenance(self):
        result=analyze(self.reports,self.corpus,self.raw)
        self.assertEqual(result['pairs'],78)
        self.assertEqual(len(result['encodings']),2)
        self.assertEqual(len(result['review']),78)

    def test_corpus_mismatch_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'fingerprint'):
            analyze(self.reports,self.corpus,self.raw+b' ')

    def test_row_mismatch_is_rejected(self):
        bad=copy.deepcopy(self.reports)
        bad[0]['pairs'][0]['id']='unknown'
        with self.assertRaisesRegex(ValueError,'rows mismatch'):
            analyze(bad,self.corpus,self.raw)

    def test_holdout_not_ranked(self):
        result=analyze(self.reports,self.corpus,self.raw)
        for e in result['encodings'].values():
            self.assertTrue(all(x['split']=='development' for x in e['development_best']+e['development_worst']))
            self.assertEqual(e['holdout_aggregate']['samples'],15)

    def test_no_unearned_human_review(self):
        result=analyze(self.reports,self.corpus,self.raw)
        self.assertTrue(all(r['review_status']=='pending_independent_review' for r in result['review'].values()))

if __name__=='__main__':unittest.main()
