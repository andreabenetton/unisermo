"""Ratified LDR-0029: complete 24-prefix SI inventory and milli spelling."""
import unittest

from formalization.core import Unisermo
from formalization.parser.numeral import SI_PREFIXES


class SIPrefixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lang = Unisermo()

    def test_exact_complete_inventory(self):
        expected = {
            "kwetta": 30, "ronna": 27, "jotta": 24, "zetta": 21,
            "eksa": 18, "peta": 15, "tera": 12, "giga": 9,
            "mega": 6, "kilo": 3, "ekto": 2, "deka": 1,
            "desi": -1, "senti": -2, "milli": -3, "mikro": -6,
            "nano": -9, "piko": -12, "femto": -15, "atto": -18,
            "zepto": -21, "jokto": -24, "ronto": -27, "kwekto": -30,
        }
        self.assertEqual(len(SI_PREFIXES), 24)
        self.assertEqual({x["form"]: x["exponent"] for x in SI_PREFIXES}, expected)
        symbols = [x["si_symbol"] for x in SI_PREFIXES]
        self.assertEqual(len(set(symbols)), 24)
        for x in SI_PREFIXES:
            self.assertTrue(set(x["form"]) <= set("aeioupbtdkgmnfvszlrjw"))
            self.assertIn("measurement_prefix", self.lang.lexicon[x["form"]]["categories"])

    def test_all_prefixes_on_both_confirmed_units(self):
        for prefix in SI_PREFIXES:
            for unit, dimension in (("gram", "mass"), ("sekun", "duration")):
                with self.subTest(prefix=prefix["form"], unit=unit):
                    surface = prefix["form"] + unit
                    tree = self.lang.parse_measurement_unit(surface)
                    self.assertEqual(tree["kind"], "measurement_unit")
                    self.assertEqual(tree["form"], surface)
                    self.assertEqual(tree["root"], unit)
                    self.assertEqual(tree["dimension"], dimension)
                    self.assertEqual(tree["prefix"], prefix["form"])
                    self.assertEqual(tree["decimal_exponent"], prefix["exponent"])
                    self.assertEqual(tree["si_symbol"], prefix["si_symbol"])
                    n = tree["scale_numerator"]
                    d = tree["scale_denominator"]
                    if prefix["exponent"] >= 0:
                        self.assertEqual(n, 10**prefix["exponent"])
                        self.assertEqual(d, 1)
                    else:
                        self.assertEqual(n, 1)
                        self.assertEqual(d, 10**(-prefix["exponent"]))
                    measure = self.lang.parse_measurement_expression("uno " + surface)
                    self.assertEqual(measure["kind"], "measurement")
                    self.assertEqual(measure["unit_spec"], tree)

    def test_milli_and_mila_are_distinct(self):
        self.assertEqual(self.lang.parse_numeral("mila")["value"], 1000)
        self.assertEqual(self.lang.parse_measurement_expression("mila gram")["quantity"]["value"], 1000)
        kilo = self.lang.parse_measurement_expression("uno kilogram")
        self.assertEqual(kilo["quantity"]["value"], 1)
        self.assertEqual(kilo["unit_spec"]["scale_numerator"], 1000)
        milli = self.lang.parse_measurement_expression("uno milligram")
        self.assertEqual(milli["unit_spec"]["scale_denominator"], 1000)
        self.assertIsNone(self.lang.parse_measurement_expression("uno miligram"))
        self.assertEqual(self.lang.parse_numeral("mega")["value"], 1000000)
        self.assertEqual(self.lang.parse_numeral("giga")["value"], 1000000000)
        self.assertEqual(self.lang.parse_measurement_unit("megagram")["decimal_exponent"], 6)
        self.assertEqual(self.lang.parse_measurement_unit("gigagram")["decimal_exponent"], 9)

    def test_prefixed_ellipsis_and_operators(self):
        full = self.lang.parse_measurement_expression("inter dek kilogram e bisdek kilogram")
        short = self.lang.parse_measurement_expression("inter dek e bisdek kilogram")
        self.assertEqual(full["kind"], "measurement_interval")
        self.assertEqual(short["kind"], "measurement_interval")
        self.assertEqual(full["lower"]["unit_spec"], short["lower"]["unit_spec"])
        self.assertTrue(short["lower"]["unit_elliptic"])
        self.assertFalse(full["lower"]["unit_elliptic"])
        self.assertEqual(short["unit_spec"]["decimal_exponent"], 3)
        approx = self.lang.parse_measurement_expression("sirka kin millisekun")
        self.assertEqual(approx["quantity"]["kind"], "quantitative_approximation")
        self.assertEqual(approx["unit_spec"]["decimal_exponent"], -3)
        minimal = self.lang.parse_measurement_expression("kin kwektogram")
        self.assertEqual(minimal["unit_spec"]["decimal_exponent"], -30)
        maximal = self.lang.parse_measurement_expression("kin kwettagram")
        self.assertEqual(maximal["unit_spec"]["decimal_exponent"], 30)

    def test_forbid_stacked_prefixes_unknown_units_and_mixed_interval(self):
        for phrase in ("uno kilomilligram", "uno megakilogram", "uno kilo",
                       "uno miligram", "uno metre", "uno kilome tr",
                       "inter dek kilogram e bisdek gram",
                       "inter dek e bisdek metre",
                       "inter dek gram e bisdek kilogram"):
            with self.subTest(phrase=phrase):
                self.assertIsNone(self.lang.parse_measurement_expression(phrase))


if __name__ == "__main__":
    unittest.main()
