#!/usr/bin/env python3
"""Regression checks for canonical finite TAM morphology."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TIMES = {"present": "", "past": "d", "future": "f"}
ASPECTS = {"simple": "", "progressive": "e", "perfect": "o"}
PERSONS = {"1": "i", "2": "u", "3": "a"}
NUMBERS = {"sg": "", "pl": "n"}


def form(root: str, aspect: str, time: str, person: str, number: str) -> str:
    return root + ASPECTS[aspect] + TIMES[time] + PERSONS[person] + NUMBERS[number]


def main() -> None:
    expected = {
        ("present", "simple"): "diki",
        ("present", "progressive"): "dikei",
        ("present", "perfect"): "dikoi",
        ("past", "simple"): "dikdi",
        ("past", "progressive"): "dikedi",
        ("past", "perfect"): "dikodi",
        ("future", "simple"): "dikfi",
        ("future", "progressive"): "dikefi",
        ("future", "perfect"): "dikofi",
    }
    for (time, aspect), surface in expected.items():
        assert form("dik", aspect, time, "1", "sg") == surface

    # Person and number remain outermost after aspect and time.
    assert form("mov", "progressive", "past", "1", "pl") == "movedin"
    assert form("mov", "perfect", "future", "2", "pl") == "movofun"
    assert form("mov", "perfect", "present", "3", "pl") == "movoan"

    # Present marked aspect creates intentional aspect-person hiatus.
    assert form("dik", "progressive", "present", "1", "sg") == "dikei"
    assert form("dik", "perfect", "present", "2", "sg") == "dikou"

    lex = json.loads((ROOT / "research/lexicon/confirmed_lexicon.json").read_text(encoding="utf-8"))
    roots = sorted({e["form"] for e in lex["entries"] if e.get("category") == "root"})
    rootset = set(roots)

    # Vowel-aspect morphology makes R vs R+e/o a dangerous lexical shadow pair.
    shadow_pairs = [(r, r + v) for r in roots for v in "eo" if r + v in rootset]
    assert not shadow_pairs, shadow_pairs

    # Every canonical root must retain 54 distinct finite bundles.
    for root in roots:
        surfaces = []
        for time in TIMES:
            for aspect in ASPECTS:
                for person in PERSONS:
                    for number in NUMBERS:
                        surfaces.append(form(root, aspect, time, person, number))
        assert len(surfaces) == 54
        assert len(set(surfaces)) == 54, root

    print("finite TAM checks passed")


if __name__ == "__main__":
    main()
