#!/usr/bin/env python3
"""Regression checks for the Glottolog 5.3 family inventory."""
from analyze_family_inventory import build_inventory


def main() -> None:
    result = build_inventory()
    u = result["universe"]
    s = result["sample"]

    assert u["ordinary_plurilingual_family_count"] == 239
    assert u["isolate_count"] == 183
    assert u["genealogical_unit_count"] == 422
    assert u["pseudo_or_administrative_top_level_category_count"] == 7
    assert u["cldf_top_level_family_rows_including_pseudo"] == 246

    assert s["source_record_count"] == 2122
    assert s["source_records_with_glottocode"] == 2121
    assert s["genealogically_mapped_source_record_count"] == 2114
    assert s["pseudo_category_source_record_count"] == 7
    assert s["classified_coded_source_record_count_including_pseudo"] == 2121
    assert s["classification_completeness_pct_of_coded_source_records"] == 100.0
    assert s["ordinary_genealogy_mapping_completeness_after_pseudo_exclusion_pct"] == 100.0
    assert s["source_record_count_without_glottocode"] == 1
    assert s["problematic_or_obsolete_glottocode_count"] == 0
    assert s["represented_family_count"] == 174
    assert s["represented_isolate_count"] == 71
    assert s["represented_genealogical_unit_count"] == 245
    assert s["absent_genealogical_unit_count"] == 177
    assert s["distinct_relevant_glottolog_language_count_within_genealogical_units"] == 2070
    assert s["family_level_source_record_count_within_genealogical_units"] == 4

    pseudo = {p["name"] for p in result["pseudo_categories"]}
    assert pseudo == {
        "Artificial Language",
        "Bookkeeping",
        "Mixed Language",
        "Pidgin",
        "Speech Register",
        "Unattested",
        "Unclassifiable",
    }

    no_code = result["records_without_glottocode"]
    assert len(no_code) == 1 and no_code[0]["name"] == "Djindewal"

    mappings = result["source_record_mappings"]
    assert len(mappings) == 2122
    status_counts = {status: sum(m["mapping_status"] == status for m in mappings) for status in {m["mapping_status"] for m in mappings}}
    assert status_counts == {"genealogical": 2114, "pseudo_category": 7, "no_glottocode": 1}
    assert all(m["top_level_glottocode"] for m in mappings if m["mapping_status"] == "genealogical")

    represented = {u["top_level_glottocode"] for u in result["units"] if u["represented"]}
    absent = {u["top_level_glottocode"] for u in result["units"] if not u["represented"]}
    assert represented.isdisjoint(absent)
    assert len(represented | absent) == 422

    print("family-inventory regression checks: OK")


if __name__ == "__main__":
    main()
