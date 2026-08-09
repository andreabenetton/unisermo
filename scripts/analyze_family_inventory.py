#!/usr/bin/env python3
"""Build the GlottoDelta top-level genealogical family inventory.

Primary family assignment comes from the official Glottolog 5.3 Newick export,
which is generated from the glottolog/glottolog release data. The companion
Glottolog-CLDF LanguageTable is used only for descriptive metadata, dialect-to-
language normalization, and diagnosis of top-level administrative categories
that are intentionally absent from the genealogical Newick forest.

This script does not calculate phoneme-family scores and does not change
GlottoDelta production semantics.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
from collections import defaultdict
from pathlib import Path

from analyze_phoneme_inventory import load_source

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "phonology"
VENDOR = RESEARCH / "vendor" / "glottolog-5.3"
TREE_PATH = VENDOR / "tree_glottolog_newick.txt"
META_PATH = VENDOR / "languages.csv"
OUT_JSON = RESEARCH / "family_inventory.json"
OUT_MD = RESEARCH / "family_inventory.md"

GLOTTOLOG_VERSION = "5.3"
GLOTTOLOG_TAG = "v5.3"
GLOTTOLOG_COMMIT = "eb7d58221bea745a21cb7b96582118e990a295c2"
GLOTTOLOG_RELEASE_DATE = "2026-03-02"
CURRENT_RELEASE_VERIFIED_ON = "2026-08-09"

GLOTTOCODE_RE = re.compile(r"\[([a-z0-9]{8})\]")
ROOT_LABEL_RE = re.compile(r"\)'((?:[^']|'')+)':1;\s*$")
ROOT_NAME_SUFFIX_RE = re.compile(
    r"\s*\[[a-z0-9]{8}\](?:\[[a-z0-9]{3}\])?(?:-l-)?$"
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def split_macroareas(value: str) -> list[str]:
    return [x for x in value.split(";") if x]


def load_metadata(path: Path = META_PATH) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    by_code = {row["Glottocode"]: row for row in rows if row.get("Glottocode")}
    if len(by_code) != len(rows):
        raise ValueError("Glottolog metadata contains blank or duplicate Glottocodes")
    return by_code


def parse_newick_forest(path: Path = TREE_PATH):
    """Map every Glottocode in each one-line tree to its top-level root."""
    root_by_code: dict[str, str] = {}
    root_info: dict[str, dict] = {}

    lines = path.read_text(encoding="utf-8").splitlines()
    for line_number, line in enumerate(lines, 1):
        match = ROOT_LABEL_RE.search(line)
        if not match:
            raise ValueError(f"cannot parse root label on Newick line {line_number}")
        label = match.group(1).replace("''", "'")
        root_codes = GLOTTOCODE_RE.findall(label)
        if len(root_codes) != 1:
            raise ValueError(
                f"expected one root Glottocode on line {line_number}, got {root_codes}"
            )
        root_code = root_codes[0]
        root_name = ROOT_NAME_SUFFIX_RE.sub("", label)
        is_language_root = label.endswith("-l-")
        if root_code in root_info:
            raise ValueError(f"duplicate top-level root {root_code}")
        root_info[root_code] = {
            "top_level_glottocode": root_code,
            "family_name": root_name,
            "newick_root_label": label,
            "unit_type_from_newick": "isolate" if is_language_root else "family",
        }

        for glottocode in GLOTTOCODE_RE.findall(line):
            previous = root_by_code.get(glottocode)
            if previous is not None and previous != root_code:
                raise ValueError(
                    f"Glottocode {glottocode} appears under both {previous} and {root_code}"
                )
            root_by_code[glottocode] = root_code

    return root_by_code, root_info


def normalized_language_id(row: dict[str, str]) -> str | None:
    if row["Level"] == "language":
        return row["Glottocode"]
    if row["Level"] == "dialect" and row.get("Language_ID"):
        return row["Language_ID"]
    return None


def build_inventory(tree_path: Path = TREE_PATH, meta_path: Path = META_PATH) -> dict:
    metadata = load_metadata(meta_path)
    root_by_code, root_info = parse_newick_forest(tree_path)

    top_family_rows = {
        code: row
        for code, row in metadata.items()
        if row["Level"] == "family" and not row.get("Family_ID")
    }
    top_isolate_rows = {
        code: row
        for code, row in metadata.items()
        if row["Level"] == "language"
        and not row.get("Family_ID")
        and row.get("Is_Isolate", "").lower() == "true"
    }

    newick_roots = set(root_info)
    pseudo_family_ids = set(top_family_rows) - newick_roots
    ordinary_family_ids = set(top_family_rows) & newick_roots
    isolate_ids = set(top_isolate_rows) & newick_roots

    unexpected_roots = newick_roots - ordinary_family_ids - isolate_ids
    if unexpected_roots:
        raise ValueError(f"Newick roots with unexpected metadata level: {unexpected_roots}")

    unit_stats = {
        root_id: {
            "source_record_count": 0,
            "language_ids": set(),
            "non_language_source_records": [],
        }
        for root_id in newick_roots
    }
    pseudo_stats = {
        pseudo_id: {"source_record_count": 0, "language_ids": set(), "records": []}
        for pseudo_id in pseudo_family_ids
    }

    no_glottocode_records = []
    problematic_glottocodes = []
    source_metadata_missing = []
    source_record_mappings = []

    _data, _speakers, _inventories, records, _demographic, _speaker_base = load_source()

    for source_key, record in records.items():
        glottocode = record.get("glottocode") or ""
        item = {
            "source_key": source_key,
            "name": record.get("name", ""),
            "iso": record.get("iso", ""),
            "glottocode": glottocode,
        }
        if not glottocode:
            no_glottocode_records.append(item)
            source_record_mappings.append(
                {
                    **item,
                    "mapping_status": "no_glottocode",
                    "top_level_glottocode": None,
                    "top_level_name": None,
                    "unit_type": None,
                    "distinct_language_id": None,
                }
            )
            continue

        row = metadata.get(glottocode)
        if row is None:
            source_metadata_missing.append(item)
            problem = {**item, "reason": "not present in metadata table"}
            problematic_glottocodes.append(problem)
            source_record_mappings.append(
                {
                    **item,
                    "mapping_status": "problematic",
                    "top_level_glottocode": None,
                    "top_level_name": None,
                    "unit_type": None,
                    "distinct_language_id": None,
                    "reason": problem["reason"],
                }
            )
            continue

        if glottocode in root_by_code:
            root_id = root_by_code[glottocode]
            stats = unit_stats[root_id]
            stats["source_record_count"] += 1
            language_id = normalized_language_id(row)
            if language_id:
                stats["language_ids"].add(language_id)
            else:
                stats["non_language_source_records"].append(
                    {
                        **item,
                        "glottolog_level": row["Level"],
                        "glottolog_name": row["Name"],
                    }
                )
            source_record_mappings.append(
                {
                    **item,
                    "mapping_status": "genealogical",
                    "source_glottolog_name": row["Name"],
                    "source_glottolog_level": row["Level"],
                    "distinct_language_id": language_id,
                    "top_level_glottocode": root_id,
                    "top_level_name": root_info[root_id]["family_name"],
                    "unit_type": root_info[root_id]["unit_type_from_newick"],
                    "macroarea": row.get("Macroarea", "") or None,
                }
            )
            continue

        family_id = row.get("Family_ID") or ""
        if family_id in pseudo_family_ids:
            stats = pseudo_stats[family_id]
            stats["source_record_count"] += 1
            language_id = normalized_language_id(row)
            if language_id:
                stats["language_ids"].add(language_id)
            stats["records"].append(
                {
                    **item,
                    "glottolog_name": row["Name"],
                    "glottolog_level": row["Level"],
                }
            )
            source_record_mappings.append(
                {
                    **item,
                    "mapping_status": "pseudo_category",
                    "source_glottolog_name": row["Name"],
                    "source_glottolog_level": row["Level"],
                    "distinct_language_id": language_id,
                    "top_level_glottocode": family_id,
                    "top_level_name": top_family_rows[family_id]["Name"],
                    "unit_type": "pseudo_category",
                    "macroarea": row.get("Macroarea", "") or None,
                }
            )
        else:
            problem = {
                **item,
                "reason": "present in metadata but absent from genealogical Newick forest",
                "metadata_family_id": family_id or None,
                "glottolog_level": row["Level"],
                "glottolog_name": row["Name"],
            }
            problematic_glottocodes.append(problem)
            source_record_mappings.append(
                {
                    **item,
                    "mapping_status": "problematic",
                    "source_glottolog_name": row["Name"],
                    "source_glottolog_level": row["Level"],
                    "distinct_language_id": normalized_language_id(row),
                    "top_level_glottocode": family_id or None,
                    "top_level_name": top_family_rows.get(family_id, {}).get("Name"),
                    "unit_type": None,
                    "macroarea": row.get("Macroarea", "") or None,
                    "reason": problem["reason"],
                }
            )

    units = []
    all_language_ids: set[str] = set()
    all_non_language_records = []
    for root_id in sorted(newick_roots, key=lambda x: root_info[x]["family_name"].casefold()):
        info = root_info[root_id]
        row = metadata[root_id]
        expected_type = (
            "family"
            if row["Level"] == "family"
            else "isolate"
            if row["Level"] == "language" and row.get("Is_Isolate", "").lower() == "true"
            else None
        )
        if expected_type != info["unit_type_from_newick"]:
            raise ValueError(
                f"root type mismatch for {root_id}: Newick={info['unit_type_from_newick']} metadata={expected_type}"
            )
        stats = unit_stats[root_id]
        all_language_ids.update(stats["language_ids"])
        all_non_language_records.extend(stats["non_language_source_records"])
        units.append(
            {
                "top_level_glottocode": root_id,
                "family_name": info["family_name"],
                "unit_type": expected_type,
                "macroareas": split_macroareas(row.get("Macroarea", "")),
                "represented": bool(stats["source_record_count"]),
                "source_record_count": stats["source_record_count"],
                "distinct_relevant_language_count": len(stats["language_ids"]),
                "non_language_source_record_count": len(stats["non_language_source_records"]),
                "non_language_source_records": stats["non_language_source_records"],
            }
        )

    pseudo_categories = []
    pseudo_language_ids: set[str] = set()
    for pseudo_id in sorted(pseudo_family_ids, key=lambda x: top_family_rows[x]["Name"].casefold()):
        row = top_family_rows[pseudo_id]
        stats = pseudo_stats[pseudo_id]
        pseudo_language_ids.update(stats["language_ids"])
        pseudo_categories.append(
            {
                "top_level_glottocode": pseudo_id,
                "name": row["Name"],
                "macroareas": split_macroareas(row.get("Macroarea", "")),
                "source_record_count": stats["source_record_count"],
                "distinct_relevant_language_count": len(stats["language_ids"]),
                "records": stats["records"],
                "treatment": "excluded_from_genealogical_units",
            }
        )

    represented = [u for u in units if u["represented"]]
    absent = [u for u in units if not u["represented"]]
    represented_families = [u for u in represented if u["unit_type"] == "family"]
    represented_isolates = [u for u in represented if u["unit_type"] == "isolate"]

    source_count = len(records)
    coded_count = source_count - len(no_glottocode_records)
    genealogical_count = sum(u["source_record_count"] for u in units)
    pseudo_count = sum(p["source_record_count"] for p in pseudo_categories)

    result = {
        "schema": "glottodelta/family-inventory@1",
        "scope": "family_inventory_only_no_phoneme_family_scoring",
        "glottolog": {
            "version": GLOTTOLOG_VERSION,
            "tag": GLOTTOLOG_TAG,
            "tag_commit": GLOTTOLOG_COMMIT,
            "release_date": GLOTTOLOG_RELEASE_DATE,
            "verified_current_release_on": CURRENT_RELEASE_VERIFIED_ON,
            "classification_source": "official Glottolog 5.3 tree_glottolog_newick.txt; generated from glottolog/glottolog release data",
            "metadata_source": "Glottolog-CLDF 5.3 languages.csv supplied with the resumed study; used only for metadata, language-level normalization, and pseudo-category diagnostics",
            "tree_sha256": sha256(tree_path),
            "metadata_sha256": sha256(meta_path),
        },
        "methodology": {
            "primary_unit": "top-level Glottolog genealogical unit",
            "isolates": "each top-level isolate is one independent genealogical unit",
            "macroarea_role": "secondary descriptive metadata only; never used for weighting or assignment",
            "family_assignment": "map each source Glottocode to the root of its one-line tree in the official Glottolog 5.3 Newick forest",
            "distinct_language_normalization": "language-level Glottocodes count as themselves; dialect Glottocodes count by their Glottolog Language_ID; family-level source Glottocodes remain source records but are not guessed into a language",
            "pseudo_category_rule": "top-level CLDF family rows absent from the official genealogical Newick forest are kept separate and never treated as independent spoken-language families",
        },
        "universe": {
            "ordinary_plurilingual_family_count": len(ordinary_family_ids),
            "isolate_count": len(isolate_ids),
            "genealogical_unit_count": len(units),
            "pseudo_or_administrative_top_level_category_count": len(pseudo_family_ids),
            "cldf_top_level_family_rows_including_pseudo": len(top_family_rows),
            "cldf_top_level_isolate_rows": len(top_isolate_rows),
        },
        "sample": {
            "source_record_count": source_count,
            "source_records_with_glottocode": coded_count,
            "genealogically_mapped_source_record_count": genealogical_count,
            "genealogically_mapped_pct_of_all_source_records": 100.0 * genealogical_count / source_count,
            "genealogically_mapped_pct_of_coded_source_records": 100.0 * genealogical_count / coded_count if coded_count else 0.0,
            "pseudo_category_source_record_count": pseudo_count,
            "classified_coded_source_record_count_including_pseudo": genealogical_count + pseudo_count,
            "classification_completeness_pct_of_coded_source_records": 100.0 * (genealogical_count + pseudo_count) / coded_count if coded_count else 0.0,
            "ordinary_genealogy_mapping_completeness_after_pseudo_exclusion_pct": 100.0 * genealogical_count / (coded_count - pseudo_count) if coded_count > pseudo_count else 0.0,
            "source_record_count_without_glottocode": len(no_glottocode_records),
            "problematic_or_obsolete_glottocode_count": len(problematic_glottocodes),
            "represented_genealogical_unit_count": len(represented),
            "absent_genealogical_unit_count": len(absent),
            "represented_family_count": len(represented_families),
            "absent_family_count": len(ordinary_family_ids) - len(represented_families),
            "represented_isolate_count": len(represented_isolates),
            "absent_isolate_count": len(isolate_ids) - len(represented_isolates),
            "distinct_relevant_glottolog_language_count_within_genealogical_units": len(all_language_ids),
            "family_level_source_record_count_within_genealogical_units": len(all_non_language_records),
            "distinct_relevant_glottolog_language_count_in_pseudo_categories": len(pseudo_language_ids),
        },
        "units": units,
        "source_record_mappings": source_record_mappings,
        "pseudo_categories": pseudo_categories,
        "records_without_glottocode": no_glottocode_records,
        "problematic_or_obsolete_glottocodes": problematic_glottocodes,
        "source_records_missing_from_metadata": source_metadata_missing,
        "non_language_source_records_within_genealogical_units": all_non_language_records,
    }
    return result


def fmt_pct(value: float) -> str:
    return f"{value:.2f}%"


def md_table(rows: list[list[str]], header: list[str]) -> str:
    out = ["| " + " | ".join(header) + " |", "|" + "|".join(["---"] * len(header)) + "|"]
    out.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(out)


def render_report(result: dict) -> str:
    sample = result["sample"]
    uni = result["universe"]
    represented = sorted(
        (u for u in result["units"] if u["represented"]),
        key=lambda u: (-u["source_record_count"], u["family_name"].casefold()),
    )
    absent = sorted(
        (u for u in result["units"] if not u["represented"]),
        key=lambda u: (u["unit_type"], u["family_name"].casefold()),
    )

    lines = [
        "# GlottoDelta family inventory",
        "",
        "> **Scope:** inventory only. No phoneme-by-family scores or language-design decisions are calculated here.",
        "",
        "## Source and methodological rule",
        "",
        f"The inventory is pinned to **Glottolog {GLOTTOLOG_VERSION}**, tag `{GLOTTOLOG_TAG}`, commit `{GLOTTOLOG_COMMIT}` (release {GLOTTOLOG_RELEASE_DATE}). It was re-verified as the current Glottolog release on {CURRENT_RELEASE_VERIFIED_ON}.",
        "",
        "Primary assignment uses the official `tree_glottolog_newick.txt`: each GlottoDelta source Glottocode is assigned to the root of its Glottolog top-level tree. The companion `languages.csv` is secondary only: it supplies macroarea metadata, dialect-to-language normalization, and a diagnostic list of top-level administrative categories. Macroarea never affects weighting or genealogy.",
        "",
        "The Newick forest contains 239 ordinary plurilingual family roots plus 183 isolate roots. The CLDF table contains 246 top-level `family` rows plus the same 183 isolates. The seven extra CLDF top-level family rows are all non-genealogical/administrative categories and are therefore excluded from the independent-family universe rather than counted as spoken-language families.",
        "",
        "## Completeness",
        "",
        md_table(
            [
                ["Frozen GlottoDelta source records", str(sample["source_record_count"])],
                ["With Glottocode", str(sample["source_records_with_glottocode"])],
                ["Mapped to ordinary family/isolate", str(sample["genealogically_mapped_source_record_count"])],
                ["Ordinary mapping among coded records", fmt_pct(sample["genealogically_mapped_pct_of_coded_source_records"])],
                ["Pseudo/administrative-category records", str(sample["pseudo_category_source_record_count"])],
                ["Coded records classified, including pseudo categories", fmt_pct(sample["classification_completeness_pct_of_coded_source_records"])],
                ["Ordinary genealogy completeness after pseudo exclusion", fmt_pct(sample["ordinary_genealogy_mapping_completeness_after_pseudo_exclusion_pct"])],
                ["Without Glottocode", str(sample["source_record_count_without_glottocode"])],
                ["Unresolved obsolete/problematic Glottocodes", str(sample["problematic_or_obsolete_glottocode_count"])],
                ["Distinct Glottolog languages in genealogical units", str(sample["distinct_relevant_glottolog_language_count_within_genealogical_units"])],
                ["Family-level source Glottocodes not forced into a language", str(sample["family_level_source_record_count_within_genealogical_units"])],
            ],
            ["Measure", "Count / coverage"],
        ),
        "",
        "The 2,122 source-record denominator is intentionally preserved. Distinct-language counts differ because 109 source Glottocodes are dialect-level in Glottolog 5.3 and are normalized to their language-level parent; four source records point to family-level Glottocodes and are not guessed into a particular child language.",
        "",
        "## Genealogical universe represented",
        "",
        md_table(
            [
                ["Ordinary plurilingual families", str(sample["represented_family_count"]), str(uni["ordinary_plurilingual_family_count"]), str(sample["absent_family_count"])],
                ["Isolates", str(sample["represented_isolate_count"]), str(uni["isolate_count"]), str(sample["absent_isolate_count"])],
                ["Total independent genealogical units", str(sample["represented_genealogical_unit_count"]), str(uni["genealogical_unit_count"]), str(sample["absent_genealogical_unit_count"])],
            ],
            ["Unit type", "Represented", "Glottolog 5.3 universe", "Absent"],
        ),
        "",
        "## Pseudo-genealogical / administrative categories",
        "",
        "These are tracked explicitly but excluded from the ordinary genealogical-unit universe:",
        "",
        md_table(
            [
                [p["top_level_glottocode"], p["name"], str(p["source_record_count"]), ", ".join(p["macroareas"])]
                for p in result["pseudo_categories"]
            ],
            ["Glottocode", "Category", "Sample records", "Macroarea metadata"],
        ),
        "",
    ]

    pseudo_records = [
        (p["name"], rec)
        for p in result["pseudo_categories"]
        for rec in p["records"]
    ]
    if pseudo_records:
        lines += [
            "### Source records in excluded categories",
            "",
            md_table(
                [
                    [rec["name"], rec["iso"] or "—", rec["glottocode"], category]
                    for category, rec in sorted(pseudo_records, key=lambda x: x[1]["name"].casefold())
                ],
                ["Source name", "ISO", "Glottocode", "Top-level category"],
            ),
            "",
        ]

    lines += ["## Records requiring explicit handling", ""]
    if result["records_without_glottocode"]:
        lines += [
            "### No Glottocode",
            "",
            md_table(
                [[r["name"], r["iso"] or "—", "No genealogy guessed"] for r in result["records_without_glottocode"]],
                ["Source name", "ISO", "Treatment"],
            ),
            "",
        ]
    if result["problematic_or_obsolete_glottocodes"]:
        lines += [
            "### Unresolved obsolete/problematic Glottocodes",
            "",
            md_table(
                [[r["name"], r["iso"] or "—", r["glottocode"], r["reason"]] for r in result["problematic_or_obsolete_glottocodes"]],
                ["Source name", "ISO", "Glottocode", "Reason"],
            ),
            "",
        ]
    else:
        lines += ["No coded source record remains unresolved after separating the seven pseudo/administrative categories.", ""]

    if result["non_language_source_records_within_genealogical_units"]:
        lines += [
            "### Source Glottocodes at Glottolog family level",
            "",
            "These records can be assigned to a top-level family but are not counted as distinct Glottolog languages, because the source Glottocode itself is classified at family level in 5.3:",
            "",
            md_table(
                [[r["name"], r["iso"] or "—", r["glottocode"], r["glottolog_name"]] for r in result["non_language_source_records_within_genealogical_units"]],
                ["Source name", "ISO", "Glottocode", "Glottolog 5.3 node"],
            ),
            "",
        ]

    lines += [
        "## Represented families and isolates",
        "",
        md_table(
            [
                [
                    u["top_level_glottocode"],
                    u["family_name"],
                    u["unit_type"],
                    str(u["source_record_count"]),
                    str(u["distinct_relevant_language_count"]),
                    ", ".join(u["macroareas"]),
                ]
                for u in represented
            ],
            ["Top-level Glottocode", "Family / isolate", "Type", "Source records", "Distinct languages", "Macroarea metadata"],
        ),
        "",
        "## Absent families and isolates",
        "",
        "These ordinary Glottolog 5.3 genealogical units have no source record in the frozen GlottoDelta/PHOIBLE sample:",
        "",
        md_table(
            [
                [u["top_level_glottocode"], u["family_name"], u["unit_type"], ", ".join(u["macroareas"])]
                for u in absent
            ],
            ["Top-level Glottocode", "Family / isolate", "Type", "Macroarea metadata"],
        ),
        "",
        "## Reproduce",
        "",
        "```bash",
        "python3 scripts/analyze_family_inventory.py",
        "python3 scripts/test_family_inventory.py",
        "```",
        "",
        "The script reads only the frozen `baseline/original.html` plus the pinned research files under `research/phonology/vendor/glottolog-5.3/`. It does not modify production GlottoDelta data or semantics.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    result = build_inventory()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_report(result), encoding="utf-8")
    s = result["sample"]
    print(
        "family inventory: "
        f"{s['genealogically_mapped_source_record_count']}/{s['source_record_count']} ordinary-genealogy records; "
        f"{s['pseudo_category_source_record_count']} pseudo-category; "
        f"{s['source_record_count_without_glottocode']} no Glottocode; "
        f"{s['represented_genealogical_unit_count']} represented units"
    )


if __name__ == "__main__":
    main()
