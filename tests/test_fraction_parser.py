"""Ratified two-token fraction tests, including improper and unreduced ratios."""
import unittest
from formalization.core import Unisermo
from formalization.parser.numeral import MAX_CARDINAL

class FractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.lang=Unisermo()

    def test_examples(self):
        for num,den,spelling in [(1,2,"uno bisim"),(1,3,"uno terim"),(2,3,"bis terim"),(3,4,"ter forim"),(5,8,"kin otim"),(5,100,"kin senim"),(7,1000,"set milaim"),(5,3,"kin terim"),(0,2,"nul bisim"),(2,4,"bis forim")]:
            with self.subTest(num=num,den=den):
                self.assertEqual(self.lang.generate_fraction(num,den),spelling)
                obj=self.lang.parse_fraction(spelling)
                self.assertEqual((obj["numerator"],obj["denominator"]),(num,den))
                self.assertEqual(obj["canonical_form"],spelling)

    def test_percentages_as_hundredths(self):
        for value in (0, 1, 5, 17, 100, 175):
            with self.subTest(value=value):
                form = self.lang.generate_fraction(value, 100)
                self.assertTrue(form.endswith(" senim"))
                result = self.lang.parse_fraction(form)
                self.assertEqual(result["numerator"], value)
                self.assertEqual(result["denominator"], 100)

    def test_variants_and_bounds(self):
        a=self.lang.parse_fraction("uno otoim")
        self.assertEqual((a["numerator"],a["denominator"]),(1,8))
        self.assertEqual(a["canonical_form"],"uno otim")
        self.assertEqual(a["status"],"accepted_analytic_variant")
        big=self.lang.generate_fraction(MAX_CARDINAL,MAX_CARDINAL)
        self.assertEqual(self.lang.parse_fraction(big)["denominator"],MAX_CARDINAL)

    def test_illegal(self):
        for s in ["uno unim","uno unoim","uno nulim","uno bis","bisjer terim","bisfol terim","bis terim ", " bis terim","bis  terim","bis-terim","bisim terim","uno terim dom", "uno TERIM"]:
            with self.subTest(form=s):self.assertIsNone(self.lang.parse_fraction(s))
        for n,d in [(1,0),(1,1),(1,-2),(-1,2),(MAX_CARDINAL+1,2),(1,MAX_CARDINAL+1),(True,2),(2,True)]:
            with self.assertRaises(ValueError):self.lang.generate_fraction(n,d)

if __name__ == "__main__":unittest.main()
