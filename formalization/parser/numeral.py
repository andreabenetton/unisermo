"""Canonical Unisermo numerals: deterministic 0..9999 generation and parsing.

Source: language/numerals.md (three-letter 0..9, dek/sen/mil and
largest-place-first concatenation). Powers use implicit one (sen, mil),
and no leading-zero, zero-place, or *uno+power variants are accepted.
This closes the existing documented 0..9999 range; >9999 is not yet
specified and is never interpreted by guessing.
"""
from __future__ import annotations

from functools import lru_cache

DIGITS = ("nul", "uno", "bis", "ter", "for", "kin", "ses", "set", "oto", "nin")
MAX_CARDINAL = 9999


def _cardinal(number: int) -> str:
    """Generate the one canonical form for an integer in 0..9999."""
    if isinstance(number, bool) or not isinstance(number, int) or not 0 <= number <= MAX_CARDINAL:
        raise ValueError("numeral must be an integer in 0..9999")
    if number < 10:
        return DIGITS[number]
    parts = []
    remainder = number
    for multiplier, power in ((1000, "mil"), (100, "sen"), (10, "dek")):
        digit, remainder = divmod(remainder, multiplier)
        if digit:
            parts.append((DIGITS[digit] if digit > 1 else "") + power)
    if remainder:
        parts.append(DIGITS[remainder])
    return "".join(parts)


@lru_cache(maxsize=1)
def _reverse_index() -> dict[str, int]:
    forms = {_cardinal(n): n for n in range(MAX_CARDINAL + 1)}
    if len(forms) != MAX_CARDINAL + 1:
        raise ValueError("numeral grammar is not injective")
    return forms


class NumeralParser:
    def generate_numeral(self, value: int) -> str:
        return _cardinal(value)

    def parse_numeral(self, surface: str) -> dict | None:
        if (not isinstance(surface, str) or not surface or len(surface) > 64
                or not surface.isascii() or not surface.isalpha()
                or surface != surface.lower()):
            return None
        value = _reverse_index().get(surface)
        if value is None:
            return None
        return {
            "kind": "cardinal_numeral", "form": surface, "value": value,
            "status": "canonical_by_rule", "source": "language/numerals.md",
        }

    def parse_iteration(self, surface: str) -> dict | None:
        """General count+jer for positive numerals; zero iteration not ratified."""
        if not isinstance(surface, str) or not surface.endswith("jer"):
            return None
        cardinal = self.parse_numeral(surface[:-3])
        if cardinal is None or cardinal["value"] == 0:
            return None
        return {
            "kind": "iteration_counter", "form": surface,
            "count": cardinal["value"],
            "status": "canonical_by_rule", "source": "language/numerals.md",
        }
