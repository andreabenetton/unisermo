#!/usr/bin/env python3
"""Order represented Glottolog genealogical units by frozen CLDR speaker exposure.

This is an *analysis-order* aid only. It does not define genealogical weights or
change GlottoDelta semantics. Speaker estimates come from the frozen baseline's
CLDR-derived SPEAKER_ESTIMATES mapping and therefore may include both L1 and L2
speakers and overlap across languages.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from analyze_family_inventory import load_metadata, parse_newick_forest
from analyze_phoneme_inventory import load_source

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "phonology"
FAMILY_INVENTORY = RESEARCH / "family_inventory.json"
JSON_OUT = RESEARCH / "family_population_order.json"
MD_OUT = RESEARCH / "family_population_order.md"

WORLD_POPULATION_2026 = 8_300_678_395.5
WORLD_POPULATION_SOURCE = {
    "year": 2026,
    "population": WORLD_POPULATION_2026,
    "source": "United Nations, DESA Population Division, World Population Prospects 2024 Revision",
    "indicator": "Total population by sex, both sexes, World (M49 900), 2026 median projection",
    "retrieved_on": "2026-08-09",
    "url": "https://population.un.org/dataportal/",
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def build_order() -> dict:
    fi = load_json(FAMILY_INVENTORY)
    _data, speakers, _inventories, _records, demographic, speaker_base = load_source()
    metadata = load_metadata()
    root_by_code, _root_info = parse_newick_forest()

    represented_units = {
        u["top_level_glottocode"]: u for u in fi["units"] if u["represented"]
    }

    # Population ordering is independent of PHOIBLE sample membership. Map every
    # frozen CLDR speaker-estimate ISO code to its Glottolog 5.3 language node,
    # then use the official pinned Newick forest for the top-level genealogy.
    # The convenience metadata table is only an ISO -> Glottocode index here.
    iso_rows: dict[str, list[dict]] = defaultdict(list)
    for row in metadata.values():
        iso = row.get("ISO639P3code") or ""
        if iso:
            iso_rows[iso].append(row)

    speaker_rows_by_unit: dict[str, list[dict]] = defaultdict(list)
    speaker_mapping_problems = []
    for iso, estimate in sorted(speakers.items()):
        rows = [r for r in iso_rows.get(iso, []) if r.get("Level") == "language"]
        if not rows:
            rows = iso_rows.get(iso, [])
        roots = {root_by_code.get(r["Glottocode"]) for r in rows if root_by_code.get(r["Glottocode"])}
        if len(roots) != 1:
            speaker_mapping_problems.append(
                {
                    "iso": iso,
                    "speaker_estimate": float(estimate),
                    "candidate_glottocodes": [r.get("Glottocode") for r in rows],
                    "candidate_roots": sorted(x for x in roots if x),
                }
            )
            continue
        root_id = next(iter(roots))
        # Prefer a language-level row when duplicate ISO-bearing metadata rows exist.
        chosen = sorted(rows, key=lambda r: (r.get("Level") != "language", r.get("Glottocode", "")))[0]
        speaker_rows_by_unit[root_id].append(
            {
                "iso": iso,
                "glottocode": chosen["Glottocode"],
                "name": chosen["Name"],
                "speaker_estimate": float(estimate),
            }
        )

    if speaker_mapping_problems:
        raise ValueError(f"unresolved frozen speaker estimates: {speaker_mapping_problems}")

    mappings_by_unit: dict[str, list[dict]] = {uid: [] for uid in represented_units}
    for row in fi["source_record_mappings"]:
        if row.get("mapping_status") != "genealogical":
            continue
        uid = row.get("top_level_glottocode")
        if uid in mappings_by_unit:
            mappings_by_unit[uid].append(row)

    rows = []
    all_counted_sample_language_keys = set()
    for uid, unit in represented_units.items():
        grouped: dict[str, list[dict]] = {}
        for row in mappings_by_unit[uid]:
            lid = row.get("distinct_language_id")
            if lid:
                grouped.setdefault(lid, []).append(row)

        sample_language_estimates = []
        missing_sample_languages = []
        for lid, members in sorted(grouped.items()):
            members = sorted(members, key=lambda r: r["source_key"])
            available = [m for m in members if m["source_key"] in demographic]
            if not available:
                missing_sample_languages.append(
                    {
                        "distinct_language_id": lid,
                        "name": members[0]["name"],
                        "iso": members[0].get("iso"),
                    }
                )
                continue
            chosen = available[0]
            estimate = float(demographic[chosen["source_key"]])
            all_counted_sample_language_keys.add((uid, lid))
            sample_language_estimates.append(
                {
                    "distinct_language_id": lid,
                    "name": chosen["name"],
                    "iso": chosen.get("iso"),
                    "speaker_estimate": estimate,
                    "source_key": chosen["source_key"],
                }
            )

        family_speaker_rows = sorted(
            speaker_rows_by_unit.get(uid, []),
            key=lambda r: (-r["speaker_estimate"], r["iso"]),
        )
        total = sum(x["speaker_estimate"] for x in family_speaker_rows)

        rows.append(
            {
                "top_level_glottocode": uid,
                "family_name": unit["family_name"],
                "unit_type": unit["unit_type"],
                "sample_source_record_count": unit["source_record_count"],
                "sample_distinct_language_count": unit["distinct_relevant_language_count"],
                "sample_languages_with_speaker_estimate": len(sample_language_estimates),
                "sample_languages_without_speaker_estimate": len(missing_sample_languages),
                "sample_speaker_estimate_coverage_pct": (
                    100.0 * len(sample_language_estimates) / unit["distinct_relevant_language_count"]
                    if unit["distinct_relevant_language_count"]
                    else 0.0
                ),
                "speaker_estimate_language_count": len(family_speaker_rows),
                "speaker_exposure_estimate": total if family_speaker_rows else None,
                "speaker_estimate_languages": family_speaker_rows,
                "sample_language_estimates": sample_language_estimates,
                "sample_languages_without_estimate": missing_sample_languages,
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
    cumulative = 0.0
    threshold_row = None
    for i, row in enumerate(ranked, 1):
        row["analysis_order_rank"] = i
        cumulative += row["speaker_exposure_estimate"]
        row["cumulative_speaker_exposure"] = cumulative
        row["cumulative_world_population_proxy_pct"] = 100.0 * cumulative / WORLD_POPULATION_2026
        if threshold_row is None and row["cumulative_world_population_proxy_pct"] >= 95.0:
            threshold_row = {
                "rank": i,
                "top_level_glottocode": row["top_level_glottocode"],
                "family_name": row["family_name"],
                "cumulative_speaker_exposure": cumulative,
                "cumulative_world_population_proxy_pct": row["cumulative_world_population_proxy_pct"],
            }
    for row in unranked:
        row["analysis_order_rank"] = None

    return {
        "schema": "glottodelta/family-population-order@2",
        "status": "research_ordering_only_not_genealogical_weight",
        "methodology": {
            "genealogy": "top-level Glottolog 5.3 units from the official pinned Newick forest",
            "speaker_source": "frozen baseline SPEAKER_ESTIMATES (CLDR-derived)",
            "speaker_measure": "sum of all frozen CLDR-derived fluent-speaker estimates whose ISO codes map through Glottolog 5.3 into the represented unit; L1/L2 may overlap",
            "speaker_genealogy_mapping": "languages.csv supplies ISO-to-Glottocode indexing; top-level assignment comes from the pinned official Glottolog 5.3 Newick forest",
            "sample_independence": "population ordering uses all frozen speaker-estimate entries, not only languages present in the PHOIBLE/GlottoDelta sample",
            "purpose": "analysis order and a pragmatic 95%-of-world-population exposure stop rule only",
            "not_a_weight": "the eventual genealogical F score must not inherit these population magnitudes as family weights",
            "world_population_caveat": "the cumulative percentage is an exposure proxy, not unique-human coverage, because fluent-speaker estimates may include L2 speakers and overlap across languages; it may exceed 100%",
            "missing_data_rule": "represented units with no frozen estimate are explicitly unranked rather than assigned invented values",
        },
        "world_population_reference": WORLD_POPULATION_SOURCE,
        "threshold_95pct": threshold_row,
        "coverage": {
            "represented_genealogical_units": len(rows),
            "ranked_units_with_any_speaker_estimate": len(ranked),
            "unranked_units_without_speaker_estimate": len(unranked),
            "frozen_speaker_estimate_entries": len(speakers),
            "frozen_speaker_estimate_entries_mapped_to_glottolog": sum(len(v) for v in speaker_rows_by_unit.values()),
            "distinct_sample_languages_with_estimate": len(all_counted_sample_language_keys),
            "aggregate_ranked_speaker_exposure": sum(r["speaker_exposure_estimate"] for r in ranked),
            "aggregate_all_frozen_speaker_exposure": sum(float(x) for x in speakers.values()),
            "baseline_speaker_weighting_universe": speaker_base,
        },
        "ranked_units": ranked,
        "unranked_units": unranked,
    }


def render_markdown(result: dict) -> str:
    c = result["coverage"]
    threshold = result["threshold_95pct"]
    world = result["world_population_reference"]
    lines = [
        "# Family analysis order by speaker exposure",
        "",
        "> **Status:** research ordering only. This ranking does not define or alter genealogical weighting.",
        "",
        "## Method",
        "",
        "- Genealogical units are the represented top-level Glottolog 5.3 families/isolates in `family_inventory.json`.",
        "- Speaker estimates come from the frozen baseline `SPEAKER_ESTIMATES`, which is CLDR-derived.",
        "- Population ordering uses **all** frozen speaker-estimate ISO entries that map into a represented family, not only PHOIBLE-sampled languages.",
        "- `languages.csv` is used only to index ISO codes to Glottocodes; top-level genealogy comes from the pinned official Glottolog 5.3 Newick forest.",
        "- CLDR-style fluent-speaker estimates can include L1 and L2 populations and overlap across languages. Therefore the cumulative percentage below is a **speaker-exposure proxy**, not unique-human coverage, and can exceed 100%.",
        "- Population affects **analysis order only**. It must not determine the eventual genealogical `F` weight.",
        "- Units with no available frozen estimate remain explicitly unranked rather than receiving guessed values.",
        "",
        "## 95% operational stop rule",
        "",
        f"- UN world-population reference for {world['year']}: **{world['population']:,.0f}** people (World Population Prospects 2024 Revision; retrieved {world['retrieved_on']}).",
        "- Because the language estimates overlap, `95%` here means cumulative frozen **speaker exposure / UN world population**, not a claim that 95% of unique humans have been assigned exactly once.",
        f"- The proxy first reaches 95% at rank **{threshold['rank']}**, **{threshold['family_name']}** (`{threshold['top_level_glottocode']}`), at **{threshold['cumulative_world_population_proxy_pct']:.2f}%**.",
        "",
        "## Coverage",
        "",
        f"- Represented genealogical units: **{c['represented_genealogical_units']}**.",
        f"- Ranked units with at least one speaker estimate: **{c['ranked_units_with_any_speaker_estimate']}**.",
        f"- Units with no speaker estimate and therefore currently unranked: **{c['unranked_units_without_speaker_estimate']}**.",
        f"- Frozen speaker-estimate ISO entries: **{c['frozen_speaker_estimate_entries']}**; mapped to Glottolog: **{c['frozen_speaker_estimate_entries_mapped_to_glottolog']}**.",
        f"- Distinct PHOIBLE-sampled languages that independently have an estimate: **{c['distinct_sample_languages_with_estimate']}**.",
        "",
        "## Ranked portion",
        "",
        "| Rank | Unit | Type | Speaker-exposure proxy | Cumulative / UN world | Estimate languages | PHOIBLE sample languages | Sample estimate coverage |",
        "|---:|---|---|---:|---:|---:|---:|---:|",
    ]
    for r in result["ranked_units"]:
        lines.append(
            f"| {r['analysis_order_rank']} | {r['family_name']} (`{r['top_level_glottocode']}`) | {r['unit_type']} | "
            f"{r['speaker_exposure_estimate']:,.0f} | {r['cumulative_world_population_proxy_pct']:.2f}% | "
            f"{r['speaker_estimate_language_count']} | {r['sample_distinct_language_count']} | "
            f"{r['sample_speaker_estimate_coverage_pct']:.1f}% |"
        )

    lines.extend([
        "",
        "## Unranked represented units",
        "",
        "These units are genealogically represented in GlottoDelta but have no usable frozen CLDR-derived speaker estimate. They remain in scope; their later ordering requires an explicit supplemental demographic source rather than inference.",
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
