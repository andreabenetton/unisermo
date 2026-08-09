#!/usr/bin/env python3
"""Aggregate phoneme support across the largest represented families.

The cross-family diagnostic F is population-weighted at the *family* level:

    F(target) = sum_f exposure(f) * within_family_support(f, target)
                / sum_f exposure(f)

Within-family support is deliberately the unweighted share of distinct sampled
languages. Thus population matters for the size of the genealogical group, while
one mega-language cannot by itself stand in for all languages inside that family.

The frozen CLDR-derived speaker estimates can include L1 and L2 speakers and can
overlap, so all population quantities are speaker-exposure proxies rather than
unique-person counts.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "phonology"
ORDER_PATH = RESEARCH / "family_population_order.json"
RESULTS_PATH = RESEARCH / "results.json"
FAMILIES_DIR = RESEARCH / "families"
JSON_OUT = RESEARCH / "top_family_weighted_support.json"
MD_OUT = RESEARCH / "top_family_weighted_support.md"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def family_studies() -> dict[str, dict]:
    out = {}
    for path in FAMILIES_DIR.glob("*.json"):
        row = load_json(path)
        unit = row.get("unit", {})
        uid = unit.get("top_level_glottocode")
        if uid:
            out[uid] = row
    return out


def build(top_n: int = 10) -> dict:
    order = load_json(ORDER_PATH)
    baseline = load_json(RESULTS_PATH)
    studies = family_studies()
    ranked = order["ranked_units"][:top_n]

    missing = [r["top_level_glottocode"] for r in ranked if r["top_level_glottocode"] not in studies]
    if missing:
        raise ValueError(f"missing family studies for top-{top_n}: {missing}")

    exposure_total = sum(float(r["speaker_exposure_estimate"]) for r in ranked)
    families = []
    for r in ranked:
        study = studies[r["top_level_glottocode"]]
        families.append(
            {
                "rank": r["analysis_order_rank"],
                "top_level_glottocode": r["top_level_glottocode"],
                "family_name": r["family_name"],
                "speaker_exposure_estimate": float(r["speaker_exposure_estimate"]),
                "normalized_weight_pct": 100.0 * float(r["speaker_exposure_estimate"]) / exposure_total,
                "sample_distinct_language_count": study["sample"]["distinct_language_count"],
                "glottolog_language_member_count": study["sample"]["glottolog_language_member_count"],
                "glottolog_language_member_coverage_pct": study["sample"]["glottolog_language_member_coverage_pct"],
            }
        )

    # Use the first analyzed family to define the target ordering; all family
    # studies are generated from the same frozen target definition.
    first = studies[ranked[0]["top_level_glottocode"]]
    targets = []
    for seed in first["target_support"]:
        target = seed["target"]
        family_rows = []
        strict_weighted = 0.0
        soft_weighted = 0.0
        for r in ranked:
            study = studies[r["top_level_glottocode"]]
            t = next(x for x in study["target_support"] if x["target"] == target)
            exposure = float(r["speaker_exposure_estimate"])
            strict = t["strict_language_pct"] / 100.0
            soft = t["strict_plus_soft_language_pct"] / 100.0
            strict_weighted += exposure * strict
            soft_weighted += exposure * soft
            family_rows.append(
                {
                    "rank": r["analysis_order_rank"],
                    "family_name": r["family_name"],
                    "top_level_glottocode": r["top_level_glottocode"],
                    "speaker_exposure_estimate": exposure,
                    "family_weight_pct": 100.0 * exposure / exposure_total,
                    "strict_language_pct": t["strict_language_pct"],
                    "strict_plus_soft_language_pct": t["strict_plus_soft_language_pct"],
                    "strict_exclusion_exposure": exposure * (1.0 - strict),
                    "soft_exclusion_exposure": exposure * (1.0 - soft),
                    "sample_distinct_language_count": study["sample"]["distinct_language_count"],
                }
            )

        f_strict = 100.0 * strict_weighted / exposure_total
        f_soft = 100.0 * soft_weighted / exposure_total
        base = baseline["targets"][target]
        family_rows_by_exclusion = sorted(
            family_rows,
            key=lambda x: (-x["strict_exclusion_exposure"], x["rank"]),
        )
        targets.append(
            {
                "target": target,
                "canonical": seed["canonical"],
                "class": seed["class"],
                "P_attested_pct": base["P_attested_pct"],
                "L_family_pct": base["L_family_pct"],
                "F_population_weighted_strict_pct": f_strict,
                "F_population_weighted_soft_pct": f_soft,
                "strict_exclusion_exposure": exposure_total - strict_weighted,
                "soft_exclusion_exposure": exposure_total - soft_weighted,
                "families_ge_80_strict": sum(1 for x in family_rows if x["strict_language_pct"] >= 80.0),
                "families_below_50_strict": sum(1 for x in family_rows if x["strict_language_pct"] < 50.0),
                "lowest_family_strict_pct": min(x["strict_language_pct"] for x in family_rows),
                "largest_strict_exclusion_contributors": family_rows_by_exclusion[:3],
                "family_support": family_rows,
            }
        )

    return {
        "schema": "glottodelta/top-family-population-weighted-support@1",
        "status": "experimental_cross_family_evidence_not_confirmed_inventory_decision",
        "methodology": {
            "family_set": f"top {top_n} represented genealogical units by frozen CLDR-derived speaker exposure",
            "family_weight": "speaker_exposure_estimate normalized across the analyzed family set",
            "within_family_support": "unweighted share of distinct sampled languages attesting the target family",
            "F_strict": "sum(family exposure * strict within-family support) / total analyzed family exposure",
            "F_soft": "same population-weighted family aggregation using only pre-existing soft-merger fallbacks",
            "why_hybrid": "population determines how costly exclusion of a genealogical group is, while unweighted within-family support prevents one mega-language from representing an entire family",
            "relation_to_P": "P_attested remains the direct demographic-language exposure metric; F adds genealogical structure rather than replacing P",
            "population_caveat": "CLDR-derived estimates may include L1 and L2 and overlap; exposure totals are not unique-human population counts",
            "sampling_caveat": "within-family support is estimated from the frozen PHOIBLE/GlottoDelta sample and can be noisy for sparsely sampled families",
        },
        "top_n": top_n,
        "analyzed_family_exposure_total": exposure_total,
        "families": families,
        "targets": targets,
    }


def render_markdown(result: dict) -> str:
    lines = [
        f"# Population-weighted genealogical phoneme support — top {result['top_n']} families",
        "",
        "> **Status:** experimental cross-family evidence. This report does not itself freeze or remove any GlottoDelta phoneme.",
        "",
        "## Metric",
        "",
        "`F` is now explicitly **population-weighted at the family level**. Each family's speaker-exposure proxy weights the unweighted share of its sampled distinct languages that support a target.",
        "",
        "This is intentional: population measures the practical cost of excluding a large group, while the unweighted within-family share keeps a single mega-language from standing in for its whole genealogy. Existing `P_attested` remains the direct demographic-language metric; `F` adds genealogical structure.",
        "",
        "CLDR-derived exposure estimates may include L1 and L2 speakers and overlap, so the exposure totals below are not unique-person counts.",
        "",
        "## Family weights",
        "",
        "| Rank | Family | Exposure proxy | Normalized F weight | Sample languages | Glottolog coverage |",
        "|---:|---|---:|---:|---:|---:|",
    ]
    for f in result["families"]:
        lines.append(
            f"| {f['rank']} | {f['family_name']} | {f['speaker_exposure_estimate']:,.0f} | "
            f"{f['normalized_weight_pct']:.2f}% | {f['sample_distinct_language_count']} | {f['glottolog_language_member_coverage_pct']:.1f}% |"
        )

    lines.extend([
        "",
        "## Target comparison",
        "",
        "| Target | P_attested | L_family | F strict | F soft | Strict excluded exposure | Families >=80% | Families <50% |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for t in sorted(result["targets"], key=lambda x: (-x["F_population_weighted_strict_pct"], x["target"])):
        lines.append(
            f"| /{t['canonical']}/ | {t['P_attested_pct']:.1f}% | {t['L_family_pct']:.1f}% | "
            f"{t['F_population_weighted_strict_pct']:.1f}% | {t['F_population_weighted_soft_pct']:.1f}% | "
            f"{t['strict_exclusion_exposure']/1e9:.2f}B | {t['families_ge_80_strict']}/{result['top_n']} | {t['families_below_50_strict']}/{result['top_n']} |"
        )

    lines.extend([
        "",
        "## Largest strict exclusion contributors by target",
        "",
    ])
    for t in sorted(result["targets"], key=lambda x: (-x["strict_exclusion_exposure"], x["target"])):
        contributors = "; ".join(
            f"{x['family_name']} {x['strict_language_pct']:.1f}% support -> {x['strict_exclusion_exposure']/1e9:.2f}B exposure-equivalent gap"
            for x in t["largest_strict_exclusion_contributors"]
        )
        lines.append(f"- /{t['canonical']}/: {contributors}.")

    lines.extend([
        "",
        "## Interpretation rule",
        "",
        "A high `P_attested` says the sound is common in heavily spoken languages. A high population-weighted `F` says that support is also broad inside the large genealogical groups. For final inventory decisions, phonemes should be preferred when both are strong; a low `F` or a large exclusion contribution from one major family is a warning even if global `P` is high.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = build(args.top)
    text = render_markdown(result)
    if args.write:
        JSON_OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        MD_OUT.write_text(text, encoding="utf-8")
        print(JSON_OUT.relative_to(ROOT))
        print(MD_OUT.relative_to(ROOT))
    else:
        print(text)


if __name__ == "__main__":
    main()
