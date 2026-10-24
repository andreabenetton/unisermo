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

DIGITS = ("nul", "uno", "bis", "ter", "for", "kin", "ses", "set", "oto", "nin")
SCALES = ((10**9, "giga"), (10**6, "mega"), (10**3, "mila"))
MAX_CARDINAL = 10**12 - 1
MAX_NUMERAL_CHARS = 128


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
