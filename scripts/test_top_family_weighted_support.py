#!/usr/bin/env python3
"""Regression checks for population-weighted cross-family F."""
from analyze_top_family_weighted_support import build


def main() -> None:
    r = build(10)
    assert r["top_n"] == 10
    assert len(r["families"]) == 10
    assert r["families"][0]["family_name"] == "Indo-European"
    assert r["families"][-1]["family_name"] == "Tai-Kadai"
    assert abs(sum(x["normalized_weight_pct"] for x in r["families"]) - 100.0) < 1e-8
    by = {x["target"]: x for x in r["targets"]}
    assert by["m"]["F_population_weighted_strict_pct"] > 99.0
    assert by["i"]["F_population_weighted_strict_pct"] > 95.0
    assert by["u"]["F_population_weighted_strict_pct"] > 95.0
    assert by["schwa"]["F_population_weighted_strict_pct"] < 51.0
    assert by["v"]["F_population_weighted_soft_pct"] > 97.0
    assert by["sh"]["F_population_weighted_soft_pct"] > 96.0
    assert by["a"]["P_attested_pct"] > by["a"]["F_population_weighted_strict_pct"]
    print("top-family weighted-support regression checks: OK")


if __name__ == "__main__":
    main()
