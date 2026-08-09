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
    assert abkh["analysis_order"]["rank"] == 24

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

    sino = analyze("sino1245")
    assert sino["unit"]["family_name"] == "Sino-Tibetan"
    assert sino["sample"]["source_record_count"] == 98
    assert sino["sample"]["distinct_language_count"] == 97
    assert sino["sample"]["glottolog_language_member_count"] == 519
    assert sino["sample"]["represented_glottolog_language_member_count"] == 97
    assert sino["analysis_order"]["rank"] == 2
    assert [x["name"] for x in sino["sample"]["non_language_source_records"]] == ["Caodeng rGyalrong"]
    sino_targets = {x["target"]: x for x in sino["target_support"]}
    assert sino_targets["u"]["strict_language_count"] == 97
    assert sino_targets["i"]["strict_language_count"] == 96
    assert sino_targets["p"]["strict_language_count"] == 96
    assert sino_targets["m"]["strict_language_count"] == 96
    assert sino_targets["v"]["strict_language_count"] == 29
    assert sino_targets["f"]["strict_language_count"] == 32
    assert sino_targets["v"]["strict_plus_soft_language_count"] == 87
    assert sino_targets["g"]["strict_plus_soft_language_count"] == 96

    afro = analyze("afro1255")
    assert afro["unit"]["family_name"] == "Afro-Asiatic"
    assert afro["sample"]["distinct_language_count"] == 104
    assert afro["analysis_order"]["rank"] == 3
    afro_targets = {x["target"]: x for x in afro["target_support"]}
    assert afro_targets["a"]["strict_language_count"] == 100
    assert afro_targets["i"]["strict_language_count"] == 92
    assert afro_targets["u"]["strict_language_count"] == 92
    assert afro_targets["e"]["strict_language_count"] == 77
    assert afro_targets["o"]["strict_language_count"] == 68

    aust = analyze("aust1307")
    assert aust["unit"]["family_name"] == "Austronesian"
    assert aust["sample"]["distinct_language_count"] == 109
    assert aust["analysis_order"]["rank"] == 4
    aust_targets = {x["target"]: x for x in aust["target_support"]}
    assert aust_targets["a"]["strict_language_count"] == 108
    assert aust_targets["i"]["strict_language_count"] == 109
    assert aust_targets["u"]["strict_language_count"] == 106
    assert aust_targets["z"]["strict_language_count"] == 12
    assert aust_targets["sh"]["strict_language_count"] == 14

    atla = analyze("atla1278")
    assert atla["unit"]["family_name"] == "Atlantic-Congo"
    assert atla["sample"]["source_record_count"] == 408
    assert atla["sample"]["distinct_language_count"] == 406
    assert atla["analysis_order"]["rank"] == 5
    atla_targets = {x["target"]: x for x in atla["target_support"]}
    assert atla_targets["a"]["strict_language_count"] == 402
    assert atla_targets["i"]["strict_language_count"] == 405
    assert atla_targets["u"]["strict_language_count"] == 404
    assert atla_targets["schwa"]["strict_language_count"] == 118

    drav = analyze("drav1251")
    assert drav["unit"]["family_name"] == "Dravidian"
    assert drav["sample"]["distinct_language_count"] == 32
    assert drav["analysis_order"]["rank"] == 6
    drav_targets = {x["target"]: x for x in drav["target_support"]}
    for target in ["a", "i", "u", "m", "p", "t", "k", "b", "d", "g", "r", "l"]:
        assert drav_targets[target]["strict_language_count"] == 32, target
    assert drav_targets["e"]["strict_language_count"] == 31
    assert drav_targets["o"]["strict_language_count"] == 30

    print("family-phoneme regression checks: OK")


if __name__ == "__main__":
    main()
