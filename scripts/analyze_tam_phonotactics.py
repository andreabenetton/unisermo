#!/usr/bin/env python3
"""Compare the retired consonantal TAM morphology with the canonical vowel-aspect system.

The retired pre-change pattern is:
    root + time(0/d/f) + aspect(0/n/b) + person(i/u/a) + number(0/n)

The confirmed canonical pattern is:
    root + aspect(0/e/o) + time(0/d/f) + person(i/u/a) + number(0/n)

This script reproduces the phonotactic comparison that motivated the canonical change. It measures phonotactic load, hiatus, and surface collisions over two root samples.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOWELS = set("aeiou")
PERSONS = {"1": "i", "2": "u", "3": "a"}
NUMBERS = {"sg": "", "pl": "n"}
TIMES = {"present": "", "past": "d", "future": "f"}
FORMER_ASPECTS = {"simple": "", "progressive": "n", "perfect": "b"}
VOWEL_ASPECTS = {"simple": "", "progressive": "e", "perfect": "o"}

# Confirmed replacements that overlap the 74-root provisional seed.
CURRENTIZED = {
    "act": "ager",
    "cad": "kad",
    "cap": "kap",
    "centr": "sentr",
    "cert": "sert",
    "circul": "sirkul",
    "civ": "siv",
    "clar": "klar",
    "com": "kun",
    "cred": "kred",
    "cur": "kurar",
    "dec": "dek",
    "dict": "dik",
    "direct": "dirig",
    "doc": "dok",
    "fac": "fak",
    "loc": "lok",
    "spec": "spets",
    "struct": "stru",
    "voc": "vok",
}


def char_class(ch: str) -> str:
    return "V" if ch in VOWELS else "C"


def annotated_form(root: str, time: str, aspect: str, person: str, number: str, proposal: bool):
    pieces = [(root, "R")]
    if proposal:
        pieces += [(aspect, "A"), (time, "T"), (person, "P"), (number, "N")]
    else:
        pieces += [(time, "T"), (aspect, "A"), (person, "P"), (number, "N")]
    chars = []
    for text, label in pieces:
        chars.extend((ch, label) for ch in text)
    return chars


def surface(chars) -> str:
    return "".join(ch for ch, _ in chars)


def morphology_run_metrics(chars):
    """Return V/C runs that contain at least one non-root character."""
    runs = []
    i = 0
    while i < len(chars):
        cls = char_class(chars[i][0])
        j = i + 1
        while j < len(chars) and char_class(chars[j][0]) == cls:
            j += 1
        labels = {label for _, label in chars[i:j]}
        if labels - {"R"}:
            runs.append((cls, j - i, "".join(ch for ch, _ in chars[i:j]), labels))
        i = j
    return runs


def load_root_sets():
    lex = json.loads((ROOT / "research/lexicon/confirmed_lexicon.json").read_text())
    confirmed = [e["form"] for e in lex["entries"] if e.get("category") == "root"]
    # Live verbal roots used normatively but not yet all present in confirmed_lexicon.json.
    for extra in ["mov", "vid", "es"]:
        if extra not in confirmed:
            confirmed.append(extra)

    seed_data = json.loads((ROOT / "research/phonology/latin_roots_seed.json").read_text())
    seed = [CURRENTIZED.get(e["root"], e["root"]) for e in seed_data["roots"]]
    return {
        "confirmed_plus_live": sorted(set(confirmed)),
        "currentized_seed74": sorted(set(seed)),
    }


def generate(roots, proposal):
    aspects = VOWEL_ASPECTS if proposal else FORMER_ASPECTS
    rows = []
    for root in roots:
        for t_name, t in TIMES.items():
            for a_name, a in aspects.items():
                for p_name, p in PERSONS.items():
                    for n_name, n in NUMBERS.items():
                        chars = annotated_form(root, t, a, p, n, proposal)
                        rows.append({
                            "root": root,
                            "time": t_name,
                            "aspect": a_name,
                            "person": p_name,
                            "number": n_name,
                            "form": surface(chars),
                            "chars": chars,
                        })
    return rows


def generate_vowel_after_time(roots):
    """Control system: root + time + vowel aspect + person + number."""
    rows = []
    for root in roots:
        for t_name, t in TIMES.items():
            for a_name, a in VOWEL_ASPECTS.items():
                for p_name, p in PERSONS.items():
                    for n_name, n in NUMBERS.items():
                        pieces = [(root, "R"), (t, "T"), (a, "A"), (p, "P"), (n, "N")]
                        chars = []
                        for text, label in pieces:
                            chars.extend((ch, label) for ch in text)
                        rows.append({
                            "root": root,
                            "time": t_name,
                            "aspect": a_name,
                            "person": p_name,
                            "number": n_name,
                            "form": surface(chars),
                            "chars": chars,
                        })
    return rows


def collision_summary(rows):
    by_surface = defaultdict(list)
    for r in rows:
        by_surface[r["form"]].append(r)
    collisions = {k: v for k, v in by_surface.items() if len(v) > 1}
    within_root = {}
    cross_root = {}
    for form, vals in collisions.items():
        roots = {v["root"] for v in vals}
        if len(roots) == 1:
            within_root[form] = vals
        else:
            cross_root[form] = vals
    return {
        "surface_collision_count": len(collisions),
        "within_root_collision_count": len(within_root),
        "cross_root_collision_count": len(cross_root),
        "examples": {
            "within_root": sorted(within_root)[:10],
            "cross_root": sorted(cross_root)[:10],
        },
    }


def shadow_pairs(roots):
    rootset = set(roots)
    pairs = []
    for r in roots:
        for v in "eo":
            if r + v in rootset:
                pairs.append((r, r + v, v))
    return pairs


def accent_hiatus_collapse_key(row, proposal):
    """Worst-case diagnostic, not a canonical pronunciation rule.

    For the e/o proposal only, raise the aspect marker e->i and o->u, then
    coalesce an identical adjacent aspect/person vowel pair in present forms.
    This estimates vulnerability if a speaker lacks stable mid vowels and also
    repairs identical-vowel hiatus by coalescence.
    """
    if not proposal:
        return row["form"]
    root = row["root"]
    t = TIMES[row["time"]]
    a = VOWEL_ASPECTS[row["aspect"]]
    p = PERSONS[row["person"]]
    n = NUMBERS[row["number"]]
    raised = {"e": "i", "o": "u"}.get(a, a)
    if not t and raised and raised == p:
        # Collapse the two identical adjacent vowels into one.
        return root + raised + n
    return root + raised + t + p + n


def summarize(rows, roots, proposal):
    total = len(rows)
    c_ge2 = c_ge3 = c_ge4 = 0
    v_ge2 = v_ge3 = v_ge4 = 0
    max_c = max_v = 0
    same_vowel_adj = 0
    for row in rows:
        runs = morphology_run_metrics(row["chars"])
        cmax = max([length for cls, length, _, _ in runs if cls == "C"] or [0])
        vmax = max([length for cls, length, _, _ in runs if cls == "V"] or [0])
        max_c = max(max_c, cmax)
        max_v = max(max_v, vmax)
        c_ge2 += cmax >= 2
        c_ge3 += cmax >= 3
        c_ge4 += cmax >= 4
        v_ge2 += vmax >= 2
        v_ge3 += vmax >= 3
        v_ge4 += vmax >= 4
        s = row["form"]
        same_vowel_adj += any(s[i] == s[i + 1] and s[i] in VOWELS for i in range(len(s) - 1))

    result = {
        "root_count": len(roots),
        "form_count": total,
        "root_final_vowel_count": sum(r[-1] in VOWELS for r in roots),
        "root_final_e_or_o_count": sum(r.endswith(("e", "o")) for r in roots),
        "root_final_e_or_o": [r for r in roots if r.endswith(("e", "o"))],
        "morphology_created_runs": {
            "C_ge_2": c_ge2,
            "C_ge_2_pct": 100 * c_ge2 / total,
            "C_ge_3": c_ge3,
            "C_ge_3_pct": 100 * c_ge3 / total,
            "C_ge_4": c_ge4,
            "C_ge_4_pct": 100 * c_ge4 / total,
            "max_C_run": max_c,
            "V_ge_2": v_ge2,
            "V_ge_2_pct": 100 * v_ge2 / total,
            "V_ge_3": v_ge3,
            "V_ge_3_pct": 100 * v_ge3 / total,
            "V_ge_4": v_ge4,
            "V_ge_4_pct": 100 * v_ge4 / total,
            "max_V_run": max_v,
            "forms_with_identical_adjacent_vowels": same_vowel_adj,
            "forms_with_identical_adjacent_vowels_pct": 100 * same_vowel_adj / total,
        },
        "collisions": collision_summary(rows),
        "e_o_root_shadow_pairs": shadow_pairs(roots),
    }

    if proposal:
        by_key = defaultdict(list)
        for row in rows:
            by_key[accent_hiatus_collapse_key(row, True)].append(row)
        vulnerable = {}
        for key, vals in by_key.items():
            bundles = {(v["root"], v["time"], v["aspect"], v["person"], v["number"]) for v in vals}
            if len(bundles) > 1:
                vulnerable[key] = vals
        result["worst_case_mid_vowel_raising_plus_identical_hiatus_coalescence"] = {
            "collision_surface_count": len(vulnerable),
            "affected_bundle_count": sum(len(v) for v in vulnerable.values()),
            "examples": sorted(vulnerable)[:12],
            "note": "Diagnostic only: e->i, o->u in the aspect slot plus coalescence of identical aspect/person vowels in present forms. This is not a canonical rule.",
        }
    return result


def examples(root: str):
    out = []
    for proposal, label in [(False, "former_consonantal"), (True, "canonical_vowel_aspect")]:
        rows = generate([root], proposal)
        selected = {}
        for r in rows:
            if r["person"] == "1" and r["number"] == "sg":
                selected[f"{r['time']}_{r['aspect']}"] = r["form"]
        out.append((label, selected))
    return dict(out)


def main():
    root_sets = load_root_sets()
    report = {
        "schema": "glottodelta/tam-phonotactics-study@1",
        "status": "confirmed_canonical_vowel_aspect",
        "systems": {
            "former_consonantal": "root + time(0/d/f) + aspect(0/n/b) + person(i/u/a) + number(0/n)",
            "canonical_vowel_aspect": "root + aspect(0/e/o) + time(0/d/f) + person(i/u/a) + number(0/n)",
        },
        "samples": {},
        "examples": {r: examples(r) for r in ["mov", "vid", "fak", "stru"]},
    }
    for name, roots in root_sets.items():
        current_rows = generate(roots, False)
        proposed_rows = generate(roots, True)
        after_rows = generate_vowel_after_time(roots)
        report["samples"][name] = {
            "roots": roots,
            "former_consonantal": summarize(current_rows, roots, False),
            "canonical_vowel_aspect": summarize(proposed_rows, roots, True),
            "vowel_aspect_after_time_control": summarize(after_rows, roots, False),
        }

    output = ROOT / "research/grammar/tam_phonotactics_results.json"
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(output)
    for sample, data in report["samples"].items():
        print(f"\n[{sample}] roots={data['former_consonantal']['root_count']} forms={data['former_consonantal']['form_count']}")
        for system in ["former_consonantal", "canonical_vowel_aspect", "vowel_aspect_after_time_control"]:
            m = data[system]["morphology_created_runs"]
            c = data[system]["collisions"]
            print(
                f"  {system:13s} C>=3 {m['C_ge_3']:4d} ({m['C_ge_3_pct']:5.1f}%) "
                f"V>=2 {m['V_ge_2']:4d} ({m['V_ge_2_pct']:5.1f}%) "
                f"V>=3 {m['V_ge_3']:4d} ({m['V_ge_3_pct']:5.1f}%) "
                f"collisions {c['surface_collision_count']}"
            )
        w = data["canonical_vowel_aspect"]["worst_case_mid_vowel_raising_plus_identical_hiatus_coalescence"]
        print(f"  vowel worst-case accent/coalescence surfaces={w['collision_surface_count']} bundles={w['affected_bundle_count']}")


if __name__ == "__main__":
    main()
