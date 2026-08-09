#!/usr/bin/env python3
"""Regression checks for family analysis ordering by speaker exposure."""
from analyze_family_population_order import build_order


def main() -> None:
    r = build_order()
    c = r["coverage"]
    assert c["represented_genealogical_units"] == 245
    assert c["ranked_units_with_any_speaker_estimate"] + c["unranked_units_without_speaker_estimate"] == 245
    ranked = r["ranked_units"]
    assert ranked[0]["top_level_glottocode"] == "indo1319"
    assert ranked[0]["family_name"] == "Indo-European"
    assert ranked[0]["analysis_order_rank"] == 1
    assert all(
        ranked[i]["speaker_exposure_estimate"] >= ranked[i + 1]["speaker_exposure_estimate"]
        for i in range(len(ranked) - 1)
    )
    abkh = next(x for x in ranked if x["top_level_glottocode"] == "abkh1242")
    assert abkh["analysis_order_rank"] > 1
    print("family-population-order regression checks: OK")


if __name__ == "__main__":
    main()
