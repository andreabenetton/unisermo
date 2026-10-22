"""Protect source and provenance boundaries, including git remote independence."""
from pathlib import Path
import subprocess
import unittest

ROOT=Path(__file__).resolve().parents[1]
ATLAS=ROOT/'vendor/glottodelta-atlas'

class TestRepoLayout(unittest.TestCase):
    def test_separation(self):
        for d in ('language','research','formalization','benchmarks','tests','scripts','legacy','docs'):
            self.assertTrue((ROOT/d).is_dir(),d)
        for d in ('baseline','data','public','scripts','docs'):
            self.assertTrue((ATLAS/d).is_dir(),d)
        for d in ('baseline','data','public'):
            self.assertFalse((ROOT/d).exists(),f'atlas directory leaked to root: {d}')

    def test_no_remote(self):
        p=subprocess.run(['git','remote'],cwd=ROOT,capture_output=True,text=True,check=True)
        self.assertEqual(p.stdout.strip(),'')

if __name__=='__main__':unittest.main(verbosity=2)
