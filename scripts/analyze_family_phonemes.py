#!/usr/bin/env python3
"""Analyze target-phoneme support inside one Glottolog genealogical unit.

This is research tooling. It reads the frozen GlottoDelta source inventories and
the already-built Glottolog 5.3 family inventory. It does not alter production
GlottoDelta semantics and it does not define the eventual cross-family F score.

For a selected top-level family or isolate, the script reports descriptive
within-sample support: how many distinct relevant source languages attest each
target realization family, plus an accent-tolerant soft-merger diagnostic.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from analyze_phoneme_inventory import load_source

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "phonology"
FAMILY_INVENTORY = RESEARCH / "family_inventory.json"
TARGETS_PATH = RESEARCH / "phoneme_targets.json"
CANDIDATES_PATH = RESEARCH / "candidates.json"
TREE_PATH = RESEARCH / "vendor" / "glottolog-5.3" / "tree_glottolog_newick.txt"
FAMILIES_DIR = RESEARCH / "families"

LANGUAGE_LABEL_RE = re.compile(
    r"'((?:[^']|'')+?) \[([a-z0-9]{8})\](?:\[([a-z0-9]{3})\])?-l-'"
)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")
    return slug or "unit"


def glottolog_member_languages(unit_id: str) -> list[dict]:
    """Extract Glottolog language-level nodes from the selected Newick tree."""
    for line in TREE_PATH.read_text(encoding="utf-8").splitlines():
        if f"[{unit_id}]" not in line:
            continue
        # Ensure we found the tree whose root is unit_id, not merely a descendant.
        if not re.search(rf"\[{re.escape(unit_id)}\](?:\[[a-z0-9]{{3}}\])?(?:-l-)?':1;\s*$", line):
            continue
        members = []
        seen = set()
        for match in LANGUAGE_LABEL_RE.finditer(line):
            name, code, iso = match.groups()
            if code in seen:
                continue
            seen.add(code)
            members.append(
                {
                    "glottocode": code,
                    "name": name.replace("''", "'"),
                    "iso": iso,
                }
            )
        return members
    raise KeyError(f"top-level Glottolog unit {unit_id} not found in pinned Newick forest")


def target_status(inv: set[str], target: str, targets: dict, soft_mergers: dict):
    strict_family = set(targets[target]["family"])
    strict_matches = sorted(inv & strict_family)
    if strict_matches:
        return "strict", strict_matches

    soft_family = set(strict_family)
    for fallback in soft_mergers.get(target, []):
        soft_family.update(targets[fallback]["family"])
    soft_matches = sorted(inv & soft_family)
    if soft_matches:
        return "soft_only", soft_matches
    return "absent", []


def candidate_metrics(candidate_targets, language_rows, inventories, targets, soft_mergers):
    per_language = []
    for row in language_rows:
        inv = inventories[row["source_key"]]
        strict_missing = []
        tolerant_missing = []
        for target in candidate_targets:
            status, _matches = target_status(inv, target, targets, soft_mergers)
            if status != "strict":
                strict_missing.append(target)
            if status == "absent":
                tolerant_missing.append(target)
        per_language.append(
            {
                "source_key": row["source_key"],
                "name": row["name"],
                "strict_missing": strict_missing,
                "strict_missing_count": len(strict_missing),
                "accent_tolerant_missing": tolerant_missing,
                "accent_tolerant_missing_count": len(tolerant_missing),
            }
        )
    n = len(per_language)
    return {
        "target_count": len(candidate_targets),
        "mean_strict_missing": sum(x["strict_missing_count"] for x in per_language) / n if n else 0,
        "mean_accent_tolerant_missing": sum(x["accent_tolerant_missing_count"] for x in per_language) / n if n else 0,
        "per_language": per_language,
    }


def analyze(unit_id: str) -> dict:
    family_inventory = load_json(FAMILY_INVENTORY)
    target_payload = load_json(TARGETS_PATH)
    targets = target_payload["targets"]
    soft_mergers = target_payload["soft_mergers"]
    candidates = load_json(CANDIDATES_PATH)["candidates"]

    unit = next((u for u in family_inventory["units"] if u["top_level_glottocode"] == unit_id), None)
    if unit is None:
        raise KeyError(f"unknown genealogical unit {unit_id}")
    if not unit["represented"]:
        raise ValueError(f"genealogical unit {unit_id} is not represented in the GlottoDelta sample")

    mappings = [
        row
        for row in family_inventory["source_record_mappings"]
        if row.get("mapping_status") == "genealogical"
        and row.get("top_level_glottocode") == unit_id
    ]
    _data, _speakers, inventories, _records, _demographic, _speaker_base = load_source()

    # The family inventory already normalizes dialect records to distinct languages.
    # For this first-stage support diagnostic, keep one source record per distinct
    # language ID. If multiple records ever map to the same language, prefer the
    # lexicographically first source key and expose the duplication in the output.
    grouped: dict[str, list[dict]] = {}
    non_language_rows = []
    for row in mappings:
        language_id = row.get("distinct_language_id")
        if language_id:
            grouped.setdefault(language_id, []).append(row)
        else:
            non_language_rows.append(row)

    language_rows = []
    duplicate_language_records = []
    for language_id, rows in sorted(grouped.items()):
        rows = sorted(rows, key=lambda r: r["source_key"])
        chosen = rows[0]
        language_rows.append(chosen)
        if len(rows) > 1:
            duplicate_language_records.append(
                {
                    "distinct_language_id": language_id,
                    "chosen_source_key": chosen["source_key"],
                    "all_source_keys": [r["source_key"] for r in rows],
                }
            )

    matrix = []
    for row in language_rows:
        inv = inventories[row["source_key"]]
        statuses = {}
        for target in targets:
            status, matches = target_status(inv, target, targets, soft_mergers)
            statuses[target] = {"status": status, "matched_symbols": matches}
        matrix.append(
            {
                "source_key": row["source_key"],
                "name": row["name"],
                "iso": row["iso"],
                "glottocode": row["glottocode"],
                "distinct_language_id": row["distinct_language_id"],
                "inventory_symbol_count": len(inv),
                "inventory_symbols": sorted(inv),
                "targets": statuses,
            }
        )

    target_support = []
    n = len(language_rows)
    for target, meta in targets.items():
        strict_rows = []
        soft_rows = []
        absent_rows = []
        for lang in matrix:
            status = lang["targets"][target]["status"]
            if status == "strict":
                strict_rows.append(lang["name"])
            elif status == "soft_only":
                soft_rows.append(lang["name"])
            else:
                absent_rows.append(lang["name"])
        target_support.append(
            {
                "target": target,
                "canonical": meta["canonical"],
                "class": meta["class"],
                "strict_language_count": len(strict_rows),
                "strict_language_pct": 100.0 * len(strict_rows) / n if n else 0.0,
                "soft_only_language_count": len(soft_rows),
                "strict_plus_soft_language_count": len(strict_rows) + len(soft_rows),
                "strict_plus_soft_language_pct": 100.0 * (len(strict_rows) + len(soft_rows)) / n if n else 0.0,
                "strict_languages": strict_rows,
                "soft_only_languages": soft_rows,
                "absent_languages": absent_rows,
            }
        )

    members = glottolog_member_languages(unit_id)
    represented_language_ids = {row["distinct_language_id"] for row in language_rows}
    represented_members = [m for m in members if m["glottocode"] in represented_language_ids]
    absent_members = [m for m in members if m["glottocode"] not in represented_language_ids]

    candidate_results = {
        name: candidate_metrics(meta["targets"], language_rows, inventories, targets, soft_mergers)
        for name, meta in candidates.items()
    }

    return {
        "schema": "glottodelta/family-phoneme-study@1",
        "status": "experimental_family_evidence_not_confirmed_design_decision",
        "methodology": {
            "genealogical_unit": "top-level Glottolog 5.3 family/isolate from family_inventory.json",
            "within_family_measure": "unweighted share of distinct relevant GlottoDelta languages in this unit attesting each target realization family",
            "soft_measure": "strict support plus the already-defined accent-tolerant soft-merger fallbacks",
            "cross_family_F": "not defined or calculated by this script",
            "warning": "phonemic inventory attestation is evidence about phonological category familiarity, not a complete model of allophonic production ability or learnability",
        },
        "unit": unit,
        "sample": {
            "source_record_count": len(mappings),
            "distinct_language_count": len(language_rows),
            "duplicate_language_records": duplicate_language_records,
            "non_language_source_records": non_language_rows,
            "glottolog_language_member_count": len(members),
            "represented_glottolog_language_member_count": len(represented_members),
            "glottolog_language_member_coverage_pct": 100.0 * len(represented_members) / len(members) if members else 0.0,
            "represented_glottolog_language_members": represented_members,
            "absent_glottolog_language_members": absent_members,
        },
        "languages": matrix,
        "target_support": target_support,
        "candidate_support": candidate_results,
    }


def fmt_pct(value: float) -> str:
    return f"{value:.1f}%"


def render_markdown(result: dict) -> str:
    unit = result["unit"]
    sample = result["sample"]
    lines = [
        f"# Family phoneme study — {unit['family_name']}",
        "",
        "> **Status:** experimental family-level evidence. No canonical GlottoDelta/auxiliary-language decision is changed by this report.",
        "",
        "## Scope and method",
        "",
        f"- Top-level Glottolog unit: **{unit['family_name']} (`{unit['top_level_glottocode']}`)**.",
        f"- Unit type: **{unit['unit_type']}**.",
        f"- Macroarea metadata: **{', '.join(unit['macroareas'])}** (descriptive only; it does not determine weighting).",
        f"- Frozen GlottoDelta sample: **{sample['distinct_language_count']}** distinct relevant languages from **{sample['source_record_count']}** source records.",
        f"- Glottolog 5.3 language-member coverage: **{sample['represented_glottolog_language_member_count']}/{sample['glottolog_language_member_count']} = {fmt_pct(sample['glottolog_language_member_coverage_pct'])}**.",
        "- Target support below is the unweighted share of sampled distinct languages attesting the target realization family.",
        "- `strict+soft` additionally allows only the soft-merger fallbacks already defined in `phoneme_targets.json`.",
        "- This report deliberately **does not define or calculate the eventual cross-family F score**.",
        "",
        "## Family membership coverage",
        "",
        "Represented Glottolog language members: " + ", ".join(f"{x['name']} (`{x['glottocode']}`)" for x in sample["represented_glottolog_language_members"]) + ".",
        "",
        "Absent from the frozen GlottoDelta sample: " + (", ".join(f"{x['name']} (`{x['glottocode']}`)" for x in sample["absent_glottolog_language_members"]) or "none") + ".",
        "",
        "## Target support",
        "",
        "| Target | Canonical | Strict | Strict+soft | Strict languages | Soft-only |",
        "|---|---:|---:|---:|---|---|",
    ]
    for row in result["target_support"]:
        strict = f"{row['strict_language_count']}/{sample['distinct_language_count']} ({fmt_pct(row['strict_language_pct'])})"
        tolerant = f"{row['strict_plus_soft_language_count']}/{sample['distinct_language_count']} ({fmt_pct(row['strict_plus_soft_language_pct'])})"
        lines.append(
            "| {target} | /{canonical}/ | {strict} | {tolerant} | {strict_langs} | {soft_langs} |".format(
                target=row["target"], canonical=row["canonical"], strict=strict, tolerant=tolerant,
                strict_langs=", ".join(row["strict_languages"]) or "—",
                soft_langs=", ".join(row["soft_only_languages"]) or "—",
            )
        )

    lines.extend([
        "",
        "## Per-language target matrix",
        "",
        "`S` = strict target-family match, `~` = only an existing soft-merger fallback, `—` = absent in the frozen phonemic inventory.",
        "",
    ])
    target_names = [x["target"] for x in result["target_support"]]
    lines.append("| Language | " + " | ".join(target_names) + " |")
    lines.append("|---|" + "---:|" * len(target_names))
    for lang in result["languages"]:
        marks = []
        for target in target_names:
            status = lang["targets"][target]["status"]
            marks.append({"strict": "S", "soft_only": "~", "absent": "—"}[status])
        lines.append(f"| {lang['name']} | " + " | ".join(marks) + " |")

    lines.extend([
        "",
        "## Candidate inventory pressure",
        "",
        "Mean missing target categories per sampled language. The tolerant column applies only the pre-existing soft-merger experiment; it does not invent new family-specific substitutions.",
        "",
        "| Candidate | Targets | Mean strict missing | Mean tolerant missing |",
        "|---|---:|---:|---:|",
    ])
    for name, row in result["candidate_support"].items():
        lines.append(f"| {name} | {row['target_count']} | {row['mean_strict_missing']:.2f} | {row['mean_accent_tolerant_missing']:.2f} |")

    by_target = {x["target"]: x for x in result["target_support"]}
    full = [x["target"] for x in result["target_support"] if x["strict_language_count"] == sample["distinct_language_count"]]
    zero = [x["target"] for x in result["target_support"] if x["strict_language_count"] == 0]
    partial = [x["target"] for x in result["target_support"] if 0 < x["strict_language_count"] < sample["distinct_language_count"]]
    vowels = [x for x in result["target_support"] if x["class"] == "vowel"]

    lines.extend([
        "",
        "## Reading for GlottoDelta auxiliary-language design",
        "",
        f"- Strictly universal in this three-language sample: **{', '.join(full) or 'none'}**.",
        f"- Partial strict support: **{', '.join(partial) or 'none'}**.",
        f"- Zero strict support: **{', '.join(zero) or 'none'}**.",
        "- The strongest local warning is the vowel subsystem: " + ", ".join(f"`{x['target']}` {x['strict_language_count']}/{sample['distinct_language_count']}" for x in vowels) + ".",
        "- This is a **dispersion warning, not an automatic veto**. The project-wide P/L evidence and already-confirmed design constraints remain separate evidence, and phoneme inventories do not enumerate every producible allophone.",
        "- Before turning this family result into the final cross-family `F` metric, the aggregation rule should be fixed consistently for all families; this report intentionally preserves the raw within-family evidence needed for that choice.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--unit", required=True, help="top-level Glottolog unit Glottocode")
    parser.add_argument("--write", action="store_true", help="write JSON and Markdown under research/phonology/families")
    args = parser.parse_args()

    result = analyze(args.unit)
    report = render_markdown(result)
    if args.write:
        FAMILIES_DIR.mkdir(parents=True, exist_ok=True)
        slug = slugify(result["unit"]["family_name"])
        json_path = FAMILIES_DIR / f"{args.unit}_{slug}.json"
        md_path = FAMILIES_DIR / f"{args.unit}_{slug}.md"
        json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(report, encoding="utf-8")
        print(json_path.relative_to(ROOT))
        print(md_path.relative_to(ROOT))
    else:
        print(report)


if __name__ == "__main__":
    main()
