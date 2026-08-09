#!/usr/bin/env python3
"""Regression checks for reusable family-level phoneme studies."""
from analyze_family_phonemes import analyze


def main():
    abkh = analyze("abkh1242")
    assert abkh["unit"]["family_name"] == "Abkhaz-Adyge"
    assert abkh["sample"]["distinct_language_count"] == 3
    assert abkh["sample"]["glottolog_language_member_count"] == 5
    assert abkh["sample"]["represented_glottolog_language_member_count"] == 3
    assert {x["name"] for x in abkh["sample"]["absent_glottolog_language_members"]} == {"Abaza", "Ubykh"}
    by_target = {x["target"]: x for x in abkh["target_support"]}
    for target in ["b", "d", "m", "n", "f", "s", "z", "sh", "r", "y", "w"]:
        assert by_target[target]["strict_language_count"] == 3, target
    for target in ["i", "o", "u", "ng"]:
        assert by_target[target]["strict_language_count"] == 0, target
    assert by_target["a"]["strict_language_count"] == 2
    assert by_target["e"]["strict_language_count"] == 1
    assert by_target["v"]["strict_language_count"] == 2
    assert by_target["v"]["strict_plus_soft_language_count"] == 3
    assert abkh["analysis_order"]["rank"] == 23

    indo = analyze("indo1319")
    assert indo["unit"]["family_name"] == "Indo-European"
    assert indo["sample"]["source_record_count"] == 144
    assert indo["sample"]["distinct_language_count"] == 140
    assert indo["sample"]["glottolog_language_member_count"] == 586
    assert indo["sample"]["represented_glottolog_language_member_count"] == 140
    assert indo["analysis_order"]["rank"] == 1
    indo_targets = {x["target"]: x for x in indo["target_support"]}
    assert indo_targets["i"]["strict_language_count"] == 133
    assert indo_targets["u"]["strict_language_count"] == 132
    assert indo_targets["m"]["strict_language_count"] == 139
    assert indo_targets["schwa"]["strict_language_count"] == 71
    assert indo_targets["ng"]["strict_language_count"] == 71
    assert "111 tracked phoneme cells" in indo["methodology"]["source_inventory_limit"]
    print("family-phoneme regression checks: OK")


if __name__ == "__main__":
    main()
