import json
import unittest
from pathlib import Path
from benchmarks.lexical_expansion import evaluate
from benchmarks.lexical_screen import MORPH, LEXICON

ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/"research/lexicon/expansion-batch-001.json").read_text())
M=json.loads(MORPH.read_text())
L=json.loads(LEXICON.read_text())["entries"]

class TestLexicalExpansion(unittest.TestCase):
    def test_one_hundred_unique_concepts(self):
        self.assertEqual(len(DATA["entries"]),100)
        self.assertEqual(len({x["id"] for x in DATA["entries"]}),100)
        self.assertTrue(all(not x["canonical_adoption"] for x in DATA["entries"]))

    def test_screen_preserves_status_and_missing_evidence(self):
        result=evaluate(DATA,M,L)
        self.assertEqual(result["concepts"],100)
        self.assertEqual(result["root_proposals"],56)
        self.assertEqual(result["without_proposals"],44)
        self.assertEqual(len(result["coverage_by_domain"]),10)
        self.assertEqual(result["inventory_invalid"],0)
        self.assertTrue(all(x["status"]=="requires_independent_review" for x in result["results"]))

    def test_canonical_adoption_cannot_be_smuggled(self):
        altered=json.loads(json.dumps(DATA))
        altered["entries"][0]["canonical_adoption"]=True
        with self.assertRaisesRegex(ValueError,"ratification"):
            evaluate(altered,M,L)

    def test_no_fabricated_frequency(self):
        altered=json.loads(json.dumps(DATA))
        altered["entries"][0]["concept_frequency"]=0.95
        with self.assertRaisesRegex(ValueError,"unmeasured"):
            evaluate(altered,M,L)

if __name__=="__main__":unittest.main()
