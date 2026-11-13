"""Canonical Unisermo decimal cardinal numerals, 0..999,999,999,999.

The author ratified mila=10^3, mega=10^6, giga=10^9 on 24 October 2026,
retiring the former `mil`. Each high-order group has a coefficient in 1..999
spelled with the existing digit/dek/sen grammar; coefficient 1 is unspoken.
The final units group is likewise 1..999, or absent when divisible by 1,000.

The parser is compositional: only the 999 possible low-order coefficients
are indexed. No enumeration of 10^12 numeric values or guesswork.
"""
from __future__ import annotations

from functools import lru_cache
import json
from pathlib import Path

DIGITS = ("nul", "uno", "bis", "ter", "for", "kin", "ses", "set", "oto", "nin")
SCALES = ((10**9, "giga"), (10**6, "mega"), (10**3, "mila"))
MAX_CARDINAL = 10**12 - 1
MAX_NUMERAL_CHARS = 128
SI_PREFIXES = json.loads((Path(__file__).resolve().parents[1] / "data" / "si_prefixes.json").read_text(encoding="utf-8"))["entries"]
UNIT_DIMENSIONS = {"gram": "mass", "sekun": "duration"}


def _small_cardinal(number: int) -> str:
    """Unique low-order spelling for a group in 1..999."""
    if not 1 <= number <= 999:
        raise ValueError("numeric group must be 1..999")
    parts = []
    hundreds, remainder = divmod(number, 100)
    tens, units = divmod(remainder, 10)
    if hundreds:
        parts.append((DIGITS[hundreds] if hundreds > 1 else "") + "sen")
    if tens:
        parts.append((DIGITS[tens] if tens > 1 else "") + "dek")
    if units:
        parts.append(DIGITS[units])
    return "".join(parts)


@lru_cache(maxsize=1)
def _small_reverse() -> dict[str, int]:
    forms = {_small_cardinal(value): value for value in range(1, 1000)}
    if len(forms) != 999:
        raise ValueError("three-digit numeral grammar is not injective")
    return forms


def _cardinal(number: int) -> str:
    """Generate the unique accepted numeral for 0 <= number <= 999,999,999,999."""
    if (isinstance(number, bool) or not isinstance(number, int)
            or not 0 <= number <= MAX_CARDINAL):
        raise ValueError("numeral must be an integer in 0..999999999999")
    if number == 0:
        return DIGITS[0]
    remaining = number
    parts = []
    for size, word in SCALES:
        coefficient, remaining = divmod(remaining, size)
        if coefficient:
            parts.append((_small_cardinal(coefficient) if coefficient > 1 else "") + word)
    if remaining:
        parts.append(_small_cardinal(remaining))
    return "".join(parts)


def _decode(surface: str) -> int | None:
    if surface == "nul":
        return 0
    remaining = surface
    total = 0
    groups = _small_reverse()
    for multiplier, word in SCALES:
        index = remaining.find(word)
        if index == -1:
            continue
        coefficient = groups.get(remaining[:index]) if index else 1
        if coefficient is None:
            return None
        total += coefficient * multiplier
        remaining = remaining[index + len(word):]
    if remaining:
        units = groups.get(remaining)
        if units is None:
            return None
        total += units
    if total == 0 or total > MAX_CARDINAL:
        return None
    # Re-generation enforces canonical order, silent zero groups,
    # implicit 'uno' and one occurrence of each power.
    if _cardinal(total) != surface:
        return None
    return total


class NumeralParser:
    def generate_numeral(self, value: int) -> str:
        return _cardinal(value)

    def parse_numeral(self, surface: str) -> dict | None:
        if (not isinstance(surface, str) or not surface
                or len(surface) > MAX_NUMERAL_CHARS
                or not surface.isascii() or not surface.isalpha()
                or surface != surface.lower()):
            return None
        number = _decode(surface)
        if number is None:
            return None
        return {
            "kind": "cardinal_numeral", "form": surface, "value": number,
            "status": "canonical_by_rule", "source": "language/numerals.md",
        }

    def parse_iteration(self, surface: str) -> dict | None:
        """Positive NUMjer is general iteration, not a genealogical root."""
        if not isinstance(surface, str) or not surface.endswith("jer"):
            return None
        number = self.parse_numeral(surface[:-3])
        if number is None or number["value"] == 0:
            return None
        return {
            "kind": "iteration_counter", "form": surface,
            "count": number["value"],
            "status": "canonical_by_rule", "source": "language/numerals.md",
        }

    def generate_ordinal(self, value: int) -> str:
        """Canonical positive ordinal: cardinal + im; final uno/oto lose o."""
        base = self.generate_numeral(value)
        if value == 0:
            raise ValueError("zero ordinal has not been ratified")
        return (base[:-1] if base.endswith(("uno", "oto")) else base) + "im"

    def parse_ordinal(self, surface: str) -> dict | None:
        """Decode only ratified canonical ordinals, without guessing variants."""
        if (not isinstance(surface, str) or not surface.endswith("im")
                or len(surface) > MAX_NUMERAL_CHARS + 2
                or not surface.isascii() or not surface.isalpha()
                or surface != surface.lower()):
            return None
        stem = surface[:-2]
        for cardinal_form in (stem, stem + "o"):
            cardinal = self.parse_numeral(cardinal_form)
            if cardinal is None or cardinal["value"] == 0:
                continue
            value = cardinal["value"]
            canonical = self.generate_ordinal(value)
            if canonical == surface or (cardinal_form.endswith("o") and cardinal_form + "im" == surface and canonical != surface):
                return {
                    "kind": "ordinal_numeral", "form": surface,
                    "value": value, "status": "canonical_by_rule" if canonical == surface else "accepted_analytic_variant",
                    "canonical_form": canonical, "source": "language/numerals.md",
                }
        return None

    def generate_fraction(self, numerator: int, denominator: int) -> str:
        """Ratified analytic fraction: positive denominator >=2, numerator >=0."""
        if isinstance(denominator, bool) or not isinstance(denominator, int) or denominator < 2 or denominator > MAX_CARDINAL:
            raise ValueError("denominator must be an integer in 2..999999999999")
        return self.generate_numeral(numerator) + " " + self.generate_ordinal(denominator)

    def parse_fraction(self, surface: str) -> dict | None:
        """Preserve exact numerator/denominator, without simplifying fractions."""
        if not isinstance(surface, str) or len(surface) > 2 * (MAX_NUMERAL_CHARS + 2) + 1:
            return None
        parts = surface.split(" ")
        if len(parts) != 2:
            return None
        numerator = self.parse_numeral(parts[0])
        denominator = self.parse_ordinal(parts[1])
        if numerator is None or denominator is None or denominator["value"] < 2:
            return None
        num, den = numerator["value"], denominator["value"]
        return {"kind": "fraction", "form": surface, "numerator": num,
                "denominator": den, "canonical_form": self.generate_fraction(num, den),
                "status": "canonical_by_rule" if surface == self.generate_fraction(num, den) else "accepted_analytic_variant",
                "source": "language/numerals.md"}

    def parse_quantitative_expression(self, surface: str) -> dict | None:
        """General-purpose bounded scalar range/estimate/limit grammar.

        No property-specific bounds: even a hyperbolic 200% expression is
        grammatical. Parse every numeric subvalue as the existing cardinal
        or two-token fraction (with its original numerator and denominator).
        """
        if not isinstance(surface, str) or not surface:
            return None
        words = surface.split()
        if not words or len(words) > 8 or " ".join(words) != surface:
            return None
        out = self._quantitative_prefix(words)
        return out[0] if out is not None and out[1] == len(words) else None

    def _quantitative_value(self, words: list[str], start: int) -> tuple[dict, int] | None:
        """Recognize a positive integer cardinal or analytic fraction."""
        if start >= len(words):
            return None
        if start + 1 < len(words):
            fraction = self.parse_fraction(" ".join(words[start:start+2]))
            if fraction is not None:
                return fraction, start + 2
        cardinal = self.parse_numeral(words[start])
        return (cardinal, start + 1) if cardinal is not None else None

    def _quantitative_prefix(self, words: list[str], start: int = 0) -> tuple[dict, int] | None:
        """Return a typed quantity and its end offset, never guess a clause."""
        if start >= len(words):
            return None
        markers = {"major": ("greater", False), "minor": ("less", False),
                   "ekwal": ("equal", True)}
        pos = start
        if words[pos] == "inter":
            left = self._quantitative_value(words, pos + 1)
            if left is None:
                return None
            first, end = left
            if end >= len(words) or words[end] != "e":
                return None
            right = self._quantitative_value(words, end + 1)
            if right is None:
                return None
            second, end = right
            return ({"kind": "quantitative_interval", "lower": first, "upper": second,
                     "endpoints": "contextual", "inclusive": None,
                     "semantics": "between", "scope": "quantitative"}, end)
        if words[pos] == "sirka":
            val = self._quantitative_value(words, pos + 1)
            if val is None:
                return None
            amount, end = val
            return ({"kind": "quantitative_approximation", "operator": "sirka",
                     "value": amount, "tolerance": "contextual",
                     "scope": "quantitative"}, end)
        negated = words[pos] == "no"
        if negated:
            pos += 1
            if pos >= len(words) or words[pos] not in markers:
                return None
        if words[pos] in markers:
            operator = words[pos]
            val = self._quantitative_value(words, pos + 1)
            if val is None:
                return None
            amount, end = val
            relations = {("major", False): "greater_than",
                         ("minor", False): "less_than",
                         ("ekwal", False): "equal_to",
                         ("major", True): "less_than_or_equal",
                         ("minor", True): "greater_than_or_equal",
                         ("ekwal", True): "not_equal_to"}
            return ({"kind": "quantitative_comparison", "operator": operator,
                     "negative": negated, "relation": relations[(operator, negated)],
                     "value": amount, "scope": "quantitative"}, end)
        return self._quantitative_value(words, pos)

    def parse_measurement_unit(self, surface: str) -> dict | None:
        """A confirmed unit with zero or exactly one officially ratified SI prefix.

        All 24 prefixes are data-driven and use integer decimal exponents,
        so exponents down to -30 never require floating point arithmetic.
        """
        if not isinstance(surface, str) or not surface.isascii() or not surface.isalpha():
            return None
        if surface in UNIT_DIMENSIONS:
            return {"kind": "measurement_unit", "form": surface, "root": surface,
                    "dimension": UNIT_DIMENSIONS[surface], "prefix": None,
                    "si_name": None, "si_symbol": None, "decimal_exponent": 0,
                    "scale_numerator": 1, "scale_denominator": 1}
        for item in SI_PREFIXES:
            root = surface[len(item["form"]):] if surface.startswith(item["form"]) else None
            if root not in UNIT_DIMENSIONS:
                continue
            exp = item["exponent"]
            return {"kind": "measurement_unit", "form": surface, "root": root,
                    "dimension": UNIT_DIMENSIONS[root], "prefix": item["form"],
                    "si_name": item["si_name"], "si_symbol": item["si_symbol"],
                    "decimal_exponent": exp,
                    "scale_numerator": 10**exp if exp >= 0 else 1,
                    "scale_denominator": 1 if exp >= 0 else 10**(-exp)}
        return None

    def parse_measurement_expression(self, surface: str) -> dict | None:
        """Parse prefixed or unprefixed measurements and unit ellipsis.

        Strictly identical explicit surface units are required for full
        intervals.  Mixed unit conversions and stacked prefixes are deferred.
        """
        if not isinstance(surface, str) or not surface or " ".join(surface.split()) != surface:
            return None
        words = surface.split()
        if len(words) > 12:
            return None

        if words[0] == "inter":
            first = self._quantitative_value(words, 1)
            if first is None:
                return None
            lower, cursor = first
            first_unit = self.parse_measurement_unit(words[cursor]) if cursor < len(words) else None
            if first_unit is not None:
                cursor += 1
            if cursor >= len(words) or words[cursor] != "e":
                return None
            second = self._quantitative_value(words, cursor + 1)
            if second is None:
                return None
            upper, cursor = second
            second_unit = self.parse_measurement_unit(words[cursor]) if cursor < len(words) else None
            if second_unit is None or cursor + 1 != len(words):
                return None
            if first_unit is not None and first_unit["form"] != second_unit["form"]:
                return None
            resolved = second_unit
            return {
                "kind": "measurement_interval", "unit": resolved["form"],
                "unit_spec": resolved,
                "dimension": resolved["dimension"],
                "lower": {"kind": "measurement", "quantity": lower,
                          "unit": resolved["form"], "unit_spec": resolved,
                          "dimension": resolved["dimension"],
                          "unit_elliptic": first_unit is None},
                "upper": {"kind": "measurement", "quantity": upper,
                          "unit": resolved["form"], "unit_spec": resolved,
                          "dimension": resolved["dimension"],
                          "unit_elliptic": False},
                "unit_ellipsis": first_unit is None,
                "endpoints": "contextual", "inclusive": None,
                "source_form": surface
            }

        parsed = self._quantitative_prefix(words)
        if parsed is None:
            return None
        quantity, end = parsed
        if quantity["kind"] == "quantitative_interval":
            return None
        unit = self.parse_measurement_unit(words[end]) if end < len(words) else None
        if end + 1 != len(words) or unit is None:
            return None
        return {"kind": "measurement", "quantity": quantity,
                "unit": unit["form"], "unit_spec": unit,
                "dimension": unit["dimension"], "unit_elliptic": False,
                "source_form": surface}

    def generate_multiplicative(self, value: int) -> str:
        """Generate NUMfol as a factor, distinct from NUMjer repetition."""
        if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= MAX_CARDINAL:
            raise ValueError("multiplicative factor must be an integer in 1..999999999999")
        return _cardinal(value) + "fol"

    def parse_multiplicative(self, surface: str) -> dict | None:
        """Recognize only positive, canonically spelled NUMfol factors."""
        if not isinstance(surface, str) or not surface.endswith("fol"):
            return None
        cardinal = self.parse_numeral(surface[:-3])
        if cardinal is None or cardinal["value"] == 0:
            return None
        return {
            "kind": "multiplicative_factor", "form": surface,
            "factor": cardinal["value"], "status": "canonical_by_rule",
            "source": "language/numerals.md",
        }

