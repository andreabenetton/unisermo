"""Phase 2 corpus, tokenizer adapters, and reporting invariants (unittest)."""
from pathlib import Path
import json
import subprocess
import sys
import types
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from benchmarks.run import load_corpus, run, readiness
from benchmarks.tokenizers import TiktokenCounter, _tiktoken_vocab_digest
from formalization.core import Unisermo


class FakeCounter:
    # TEST-ONLY mock checks arithmetic; it MUST NOT appear in published reports.
    name = 'TEST_ONLY:space-words (NOT REAL TOKENS)'
    implementation = 'test-only'

    def count(self, text):
        return len(text.split())


class DummyEncoding:
    _mergeable_ranks = {b'a': 1, b'b': 0, b'ab': 2}

    def encode(self, text, disallowed_special=()):
        assert disallowed_special == ()
        return list(text.encode('utf-8'))


class TestBenchmarks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.corpus = load_corpus()
        cls.lang = Unisermo()

    def test_corpus_regeneration(self):
        p = subprocess.run([sys.executable, 'benchmarks/build_pilot.py', '--check'],
                           cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)

    def test_parser_and_intent(self):
        self.assertEqual(len(self.corpus), 78)
        for r in self.corpus:
            ast = self.lang.parse_sentence(r['unisermo'])
            for key, value in r['grammatical_intent'].items():
                got = (ast['object']['lemma'] if key == 'object_lemma' else
                       ast[key] if key in ('negative', 'interrogative') else ast['predicate'][key])
                self.assertEqual(got, value, r['id'])
            self.assertEqual(r['review_status'], 'draft_parser_verified')

    def test_no_tokenizer_as_fallback(self):
        result = run(FakeCounter())
        self.assertEqual(result['review_status'], 'not_human_verified')
        self.assertEqual(result['overall']['samples'], len(self.corpus))
        self.assertEqual(sum(x['samples'] for x in result['splits'].values()), len(self.corpus))
        self.assertTrue(result['encoding'].startswith('TEST_ONLY'))

    def test_readiness_does_not_claim_numbers(self):
        r = readiness()
        self.assertIsNone(r['actual_token_counts'])
        self.assertEqual(r['human_reviewed'], 0)

    def test_tiktoken_vocab_digest_deterministic(self):
        one = DummyEncoding()
        two = DummyEncoding()
        two._mergeable_ranks = dict(reversed(list(one._mergeable_ranks.items())))
        self.assertEqual(_tiktoken_vocab_digest(one), _tiktoken_vocab_digest(two))
        self.assertEqual(len(_tiktoken_vocab_digest(one)), 64)
        two._mergeable_ranks[b'ab'] = 3
        self.assertNotEqual(_tiktoken_vocab_digest(one), _tiktoken_vocab_digest(two))

    def test_tiktoken_adapter_version_and_encoding(self):
        fake = types.SimpleNamespace(get_encoding=lambda name: DummyEncoding())
        with patch.dict(sys.modules, {'tiktoken': fake}):
            with patch('importlib.metadata.version', return_value='0.TEST'):
                obj = TiktokenCounter('o200k_base')
        self.assertEqual(obj.count('dikodi'), len('dikodi'))
        self.assertEqual(obj.implementation, 'tiktoken:0.TEST')
        self.assertEqual(obj.name, 'o200k_base')
        self.assertEqual(len(obj.vocab_sha256), 64)

    def test_unavailable_tiktoken_fails_closed(self):
        # The CI workflow may have tiktoken; always request a nonexistent name
        # to assert failure without depending on installed modules/cache.
        fake = types.SimpleNamespace(get_encoding=lambda name: (_ for _ in ()).throw(KeyError(name)))
        with patch.dict(sys.modules, {'tiktoken': fake}):
            with self.assertRaisesRegex(RuntimeError, 'Cannot load tiktoken encoding'):
                TiktokenCounter('not_a_real_encoding')

    def test_cli_refuses_draft_unless_opted_in(self):
        p = subprocess.run([sys.executable, '-m', 'benchmarks', 'measure-openai'],
                           cwd=ROOT, capture_output=True, text=True)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn('--include-draft', p.stderr)


if __name__ == '__main__':
    unittest.main(verbosity=2)
