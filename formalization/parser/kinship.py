"""Deterministic productive kinship parser for the confirmed Unisermo subset.

A+B = A relative to B. The rightmost link is traversed first from ego.
NUMjer+R repeats *one entire atomic* kinship relation R. This deliberately
does not guess how NUMjer would scope over an unbracketed multi-link compound.

Only approved relation roots, themselves confirmed in the lexical index, are
admitted. An unsupported or structurally ambiguous form fails closed.
"""
from __future__ import annotations

from functools import lru_cache


# Approved atomic relations, not arbitrary nouns or historical candidate roots.
KINSHIP_LINKS = ("adelo", "adele", "adel", "geno", "gene", "gen", "fil")
DIGITS = ("nul", "uno", "bis", "ter", "for", "kin", "ses", "set", "oto", "nin")
MAX_KINSHIP_STEPS = 128
MAX_KINSHIP_CHARS = 256


def _cardinal(n: int) -> str:
    """Canonical fused decimal expression for 1..MAX_KINSHIP_STEPS."""
    if not 1 <= n <= MAX_KINSHIP_STEPS:
        raise ValueError("kinship iteration out of supported range")
    if n < 10:
        return DIGITS[n]
    if n < 20:
        return "dek" + ("" if n == 10 else DIGITS[n - 10])
    if n < 100:
        tens, units = divmod(n, 10)
        return DIGITS[tens] + "dek" + (DIGITS[units] if units else "")
    hundreds, remainder = divmod(n, 100)
    return ("" if hundreds == 1 else DIGITS[hundreds]) + "sen" + (
        _cardinal(remainder) if remainder else ""
    )


# Longest numeric prefixes first; no zero-iteration form.
_ITERATIONS = tuple(sorted(
    ((_cardinal(n) + "jer", n) for n in range(2, MAX_KINSHIP_STEPS + 1)),
    key=lambda pair: (-len(pair[0]), pair[0]),
))


class KinshipParser:
    def parse_kinship(self, surface: str) -> dict | None:
        """Return one uniquely structured kinship path, or None.

        The returned 'path_from_ego' is in **evaluation** order, nearest link
        to ego first. 'segments' remain in written left-to-right order.
        A loop's count applies to exactly the next approved atomic link.
        """
        if (not isinstance(surface, str) or not surface
                or len(surface) > MAX_KINSHIP_CHARS
                or not surface.isascii() or not surface.isalpha()
                or surface != surface.lower()
                or not set(surface) <= set(self.morph["alphabet"])):
            return None

        links = tuple(link for link in KINSHIP_LINKS
                      if self.lexicon.get(link, {}).get("status") == "confirmed_lexicon"
                      and "noun" in self.lexicon[link]["categories"])
        if not links:
            return None

        @lru_cache(maxsize=None)
        def visit(pos: int):
            if pos == len(surface):
                return ((),)
            solutions = {}
            # A segment is (atomic relation, repeat count). A repeated
            # token consumes just the next atomic link, not the rest.
            choices = ((name, 1, name) for name in links)
            repeated = ((name, n, prefix + name)
                        for prefix, n in _ITERATIONS
                        if surface.startswith(prefix, pos)
                        for name in links)
            for name, count, token in (*choices, *repeated):
                if not surface.startswith(token, pos):
                    continue
                for suffix in visit(pos + len(token)):
                    candidate = ((name, count),) + suffix
                    total = sum(mult for _, mult in candidate)
                    if total > MAX_KINSHIP_STEPS:
                        continue
                    # Equivalent segmentations expand to the same relation
                    # sequence. If meanings differ, do not guess.
                    expanded = tuple(rel for rel, mult in candidate
                                     for _ in range(mult))
                    solutions.setdefault(expanded, candidate)
                    if len(solutions) > 1:
                        return tuple(solutions.values())
            return tuple(solutions.values())

        parses = visit(0)
        if len(parses) != 1:
            return None
        segments = parses[0]
        if not segments:
            return None
        path = tuple(rel for name, count in reversed(segments)
                     for rel in (name,) * count)
        return {
            "kind": "kinship_relation",
            "lemma": surface,
            "status": (self.lexicon[surface]["status"] if surface in self.lexicon
                       else "productive_from_confirmed"),
            "segments": [{"relation": name, "count": count}
                         for name, count in segments],
            "path_from_ego": list(path),
            "steps": len(path),
            "source": "language/kinship.md",
        }
