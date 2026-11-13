"""Ratified LDR-0028: invariant units and homogeneous interval ellipsis."""
import unittest
from formalization.core import Unisermo

class SimpleMeasurementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def test_confirmed_unit_roots(self):
        for word, dimension in (("gram", "mass"), ("sekun", "duration")):
            with self.subTest(word=word):
                self.assertEqual(self.lang.lexicon[word]["status"], "confirmed_lexicon")
                self.assertIn("measurement_unit", self.lang.lexicon[word]["categories"])
                node = self.lang.parse_measurement_expression("kin " + word)
                self.assertEqual(node["kind"], "measurement")
                self.assertEqual(node["unit"], word)
                self.assertEqual(node["dimension"], dimension)
                self.assertEqual(node["quantity"]["value"], 5)

    def test_general_operators_and_fractions(self):
        for surface, kind in (
            ("sirka setdek gram", "quantitative_approximation"),
            ("no minor dek sekun", "quantitative_comparison"),
            ("major sen gram", "quantitative_comparison"),
            ("kin terim gram", "fraction"),
            ("bissen gram", "cardinal_numeral"),
        ):
            with self.subTest(surface=surface):
                node = self.lang.parse_measurement_expression(surface)
                self.assertEqual(node["kind"], "measurement")
                self.assertEqual(node["quantity"]["kind"], kind)

    def test_repeated_and_elliptical_units_equivalent(self):
        full = self.lang.parse_measurement_expression("inter dek gram e bisdek gram")
        short = self.lang.parse_measurement_expression("inter dek e bisdek gram")
        self.assertEqual(full["kind"], "measurement_interval")
        self.assertEqual(short["kind"], "measurement_interval")
        self.assertEqual(full["dimension"], "mass")
        self.assertEqual(full["unit"], "gram")
        self.assertEqual(full["lower"]["quantity"], short["lower"]["quantity"])
        self.assertEqual(full["upper"]["quantity"], short["upper"]["quantity"])
        self.assertEqual(full["lower"]["unit"], short["lower"]["unit"])
        self.assertEqual(full["upper"]["unit"], short["upper"]["unit"])
        self.assertFalse(full["unit_ellipsis"])
        self.assertTrue(short["unit_ellipsis"])
        self.assertFalse(full["lower"]["unit_elliptic"])
        self.assertTrue(short["lower"]["unit_elliptic"])
        self.assertEqual(short["source_form"], "inter dek e bisdek gram")

    def test_seconds_and_fraction_intervals(self):
        node = self.lang.parse_measurement_expression("inter kin e dek sekun")
        self.assertEqual(node["dimension"], "duration")
        self.assertEqual(node["lower"]["unit"], "sekun")
        self.assertEqual(node["upper"]["quantity"]["value"], 10)
        f = self.lang.parse_measurement_expression("inter uno bisim e ter forim gram")
        self.assertEqual(f["lower"]["quantity"]["numerator"], 1)
        self.assertEqual(f["upper"]["quantity"]["denominator"], 4)

    def test_unratified_units_and_cross_unit_intervals_fail_closed(self):
        for surface in (
            "kin metr", "kin sekund", "kin gram e dek gram",
            "inter dek gram e bisdek sekun",
            "inter dek gram e bisdek",
            "inter dek e bisdek",
            "inter dek gram e bisdek gram e terdek gram",
            "inter dek e bisdek metr",
            "sirka gram", "no sirka dek gram"
        ):
            with self.subTest(surface=surface):
                self.assertIsNone(self.lang.parse_measurement_expression(surface))

    def test_scalar_parser_is_not_implicitly_measured(self):
        self.assertEqual(self.lang.parse_quantitative_expression("inter dek e bisdek")["kind"], "quantitative_interval")
        self.assertIsNone(self.lang.parse_quantitative_expression("inter dek e bisdek gram"))


if __name__ == "__main__":
    unittest.main()
