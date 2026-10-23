import unittest
from benchmarks.document_scaling import build,synthetic_roots,WORDS
class ScalingTests(unittest.TestCase):
    def test_size(self):
        for n in (100,1000):
            x=build(n)
            self.assertEqual(x['placeholder_count'],n-15)
            self.assertIn('aervok',x['minimal'])
            self.assertLess(len(x['minimal']),len(x['full']))
    def test_no_collision(self):
        v=synthetic_roots(985)
        self.assertEqual(len(v),len(set(k for k,_ in v)))
    def test_bounded(self):
        with self.assertRaises(ValueError):build(10000)
if __name__=='__main__':unittest.main()
