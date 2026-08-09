#!/usr/bin/env python3
"""Regression checks for the first family-level phoneme study."""
from analyze_family_phonemes import analyze


def main():
    r = analyze("abkh1242")
    assert r["unit"]["family_name"] == "Abkhaz-Adyge"
    assert r["sample"]["distinct_language_count"] == 3
    assert r["sample"]["glottolog_language_member_count"] == 5
    assert r["sample"]["represented_glottolog_language_member_count"] == 3
    assert {x["name"] for x in r["sample"]["absent_glottolog_language_members"]} == {"Abaza", "Ubykh"}
    by_target = {x["target"]: x for x in r["target_support"]}
    for target in ["b", "d", "m", "n", "f", "s", "z", "sh", "r", "y", "w"]:
        assert by_target[target]["strict_language_count"] == 3, target
    for target in ["i", "o", "u", "ng"]:
        assert by_target[target]["strict_language_count"] == 0, target
    assert by_target["a"]["strict_language_count"] == 2
    assert by_target["e"]["strict_language_count"] == 1
    assert by_target["v"]["strict_language_count"] == 2
    assert by_target["v"]["strict_plus_soft_language_count"] == 3
    print("family-phoneme regression checks: OK")


if __name__ == "__main__":
    main()
