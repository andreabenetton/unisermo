#!/usr/bin/env python3
"""Order represented Glottolog genealogical units by frozen CLDR speaker exposure.

This is an *analysis-order* aid only. It does not define genealogical weights or
change GlottoDelta semantics. Speaker estimates come from the frozen baseline's
CLDR-derived SPEAKER_ESTIMATES mapping and therefore may include both L1 and L2
speakers and overlap across languages.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyze_phoneme_inventory import load_source

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "phonology"
FAMILY_INVENTORY = RESEARCH / "family_inventory.json"
JSON_OUT = RESEARCH / "family_population_order.json"
MD_OUT = RESEARCH / "family_population_order.md"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def build_order() -> dict:
    fi = load_json(FAMILY_INVENTORY)
    _data, speakers, _inventories, _records, demographic, speaker_base = load_source()

    represented_units = {
        u["top_level_glottocode"]: u for u in fi["units"] if u["represented"]
    }

    mappings_by_unit: dict[str, list[dict]] = {uid: [] for uid in represented_units}
    for row in fi["source_record_mappings"]:
        if row.get("mapping_status") != "genealogical":
            continue
        uid = row.get("top_level_glottocode")
        if uid in mappings_by_unit:
            mappings_by_unit[uid].append(row)

    rows = []
    all_counted_language_keys = set()
    for uid, unit in represented_units.items():
        grouped: dict[str, list[dict]] = {}
        for row in mappings_by_unit[uid]:
            lid = row.get("distinct_language_id")
            if lid:
                grouped.setdefault(lid, []).append(row)

        language_estimates = []
        missing_languages = []
        total = 0.0
        for lid, members in sorted(grouped.items()):
            members = sorted(members, key=lambda r: r["source_key"])
            available = [m for m in members if m["source_key"] in demographic]
            if not available:
                missing_languages.append(
                    {
                        "distinct_language_id": lid,
                        "name": members[0]["name"],
                        "iso": members[0].get("iso"),
                    }
                )
                continue
            chosen = available[0]
            estimate = float(demographic[chosen["source_key"]])
            total += estimate
            all_counted_language_keys.add((uid, lid))
            language_estimates.append(
                {
                    "distinct_language_id": lid,
                    "name": chosen["name"],
                    "iso": chosen.get("iso"),
                    "speaker_estimate": estimate,
                    "source_key": chosen["source_key"],
                }
            )

        rows.append(
            {
                "top_level_glottocode": uid,
                "family_name": unit["family_name"],
                "unit_type": unit["unit_type"],
                "sample_source_record_count": unit["source_record_count"],
                "sample_distinct_language_count": unit["distinct_relevant_language_count"],
                "languages_with_speaker_estimate": len(language_estimates),
                "languages_without_speaker_estimate": len(missing_languages),
                "speaker_exposure_estimate": total if language_estimates else None,
                "speaker_estimate_coverage_pct": (
                    100.0 * len(language_estimates) / unit["distinct_relevant_language_count"]
                    if unit["distinct_relevant_language_count"]
                    else 0.0
                ),
                "language_estimates": language_estimates,
                "languages_without_estimate": missing_languages,
            }
        )

    ranked = sorted(
        (r for r in rows if r["speaker_exposure_estimate"] is not None),
        key=lambda r: (-r["speaker_exposure_estimate"], r["family_name"], r["top_level_glottocode"]),
    )
    unranked = sorted(
        (r for r in rows if r["speaker_exposure_estimate"] is None),
        key=lambda r: (r["family_name"], r["top_level_glottocode"]),
    )
    for i, row in enumerate(ranked, 1):
        row["analysis_order_rank"] = i
    for row in unranked:
        row["analysis_order_rank"] = None

    return {
        "schema": "glottodelta/family-population-order@1",
        "status": "research_ordering_only_not_genealogical_weight",
        "methodology": {
            "genealogy": "top-level Glottolog 5.3 units from family_inventory.json",
            "speaker_source": "frozen baseline SPEAKER_ESTIMATES (CLDR-derived)",
            "speaker_measure": "sum of one CLDR-derived fluent-speaker estimate per distinct sampled Glottolog language; L1/L2 may overlap",
            "deduplication": "multiple GlottoDelta source records mapped to one distinct Glottolog language contribute at most one estimate",
            "purpose": "analysis order only; larger speaker-exposure estimates are examined first",
            "not_a_weight": "the eventual genealogical F score must not inherit these population magnitudes as family weights",
            "missing_data_rule": "represented units with no CLDR-derived estimate are explicitly unranked rather than assigned invented values",
        },
        "coverage": {
            "represented_genealogical_units": len(rows),
            "ranked_units_with_any_speaker_estimate": len(ranked),
            "unranked_units_without_speaker_estimate": len(unranked),
            "distinct_sample_languages_with_estimate": len(all_counted_language_keys),
            "aggregate_ranked_speaker_exposure": sum(r["speaker_exposure_estimate"] for r in ranked),
            "baseline_speaker_weighting_universe": speaker_base,
            "speaker_estimate_entries_in_baseline": len(speakers),
        },
        "ranked_units": ranked,
        "unranked_units": unranked,
    }


def render_markdown(result: dict) -> str:
    c = result["coverage"]
    lines = [
        "# Family analysis order by speaker exposure",
        "",
        "> **Status:** research ordering only. This ranking does not define or alter genealogical weighting.",
        "",
        "## Method",
        "",
        "- Genealogical units are the represented top-level Glottolog 5.3 families/isolates in `family_inventory.json`.",
        "- Speaker estimates come from the frozen baseline `SPEAKER_ESTIMATES`, which is CLDR-derived.",
        "- For each unit, one estimate is counted per distinct sampled Glottolog language; duplicate source records do not multiply the estimate.",
        "- CLDR-style fluent-speaker estimates can include L1 and L2 populations and overlap across languages, so the sum is a **speaker-exposure proxy**, not a unique human headcount.",
        "- Population affects **analysis order only**. It must not determine the eventual genealogical `F` weight.",
        "- Units with no available frozen estimate remain explicitly unranked rather than receiving guessed values.",
        "",
        "## Coverage",
        "",
        f"- Represented genealogical units: **{c['represented_genealogical_units']}**.",
        f"- Ranked units with at least one speaker estimate: **{c['ranked_units_with_any_speaker_estimate']}**.",
        f"- Units with no speaker estimate and therefore currently unranked: **{c['unranked_units_without_speaker_estimate']}**.",
        f"- Distinct sampled languages contributing an estimate: **{c['distinct_sample_languages_with_estimate']}**.",
        "",
        "## Ranked portion",
        "",
        "| Rank | Unit | Type | Speaker-exposure proxy | Estimated sample languages | Sample languages | Coverage |",
        "|---:|---|---|---:|---:|---:|---:|",
    ]
    for r in result["ranked_units"]:
        lines.append(
            f"| {r['analysis_order_rank']} | {r['family_name']} (`{r['top_level_glottocode']}`) | {r['unit_type']} | "
            f"{r['speaker_exposure_estimate']:,.0f} | {r['languages_with_speaker_estimate']} | "
            f"{r['sample_distinct_language_count']} | {r['speaker_estimate_coverage_pct']:.1f}% |"
        )

    lines.extend([
        "",
        "## Unranked represented units",
        "",
        "These units are genealogically represented in GlottoDelta but have no usable frozen CLDR-derived speaker estimate in the sampled languages. They remain in scope; their later ordering requires an explicit supplemental demographic source rather than inference.",
        "",
        ", ".join(f"{r['family_name']} (`{r['top_level_glottocode']}`)" for r in result["unranked_units"]) + ".",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    result = build_order()
    JSON_OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    MD_OUT.write_text(render_markdown(result), encoding="utf-8")
    print(JSON_OUT.relative_to(ROOT))
    print(MD_OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
