#!/usr/bin/env python3
"""Evaluate compact person/number morphology against frozen GlottoDelta data.

Canonical proposal under study:
  1SG -i, 2SG -u, 3SG -a
  plural = final nasal archiphoneme /N/ written n -> -in/-un/-an

The script deliberately separates segment-inventory familiarity from
phonotactic evidence. GlottoDelta does not encode coda licensing.
"""
from __future__ import annotations

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHON = os.path.join(ROOT, "research", "phonology")
RESULTS = os.path.join(PHON, "person_number_results.json")
ROOTS = os.path.join(PHON, "latin_roots_seed.json")
TARGETS = os.path.join(PHON, "phoneme_targets.json")

sys.path.insert(0, os.path.join(ROOT, "scripts"))
import analyze_phoneme_inventory as base  # noqa: E402

PERSON = {"1": "i", "2": "u", "3": "a"}
TAM_FINALS = ["", "d", "f", "n", "b", "m"]
VOWELS = set("aeiou")


def raw_family_coverage(family, inventories, demographic, speaker_base):
    family = set(family)
    all_keys = list(inventories)
    l = sum(bool(inventories[k] & family) for k in all_keys)
    p = sum(w for k, w in demographic.items() if inventories[k] & family)
    return {
        "family": sorted(family),
        "L_pct": base.pct(l, len(all_keys)),
        "P_attested_pct": base.pct(p, speaker_base),
    }


def combined_coverage(family, person_comp, inventories, demographic, speaker_base):
    family = set(family)
    all_keys = list(inventories)
    def ok(k):
        return all(person_comp[v][k] for v in PERSON.values()) and bool(inventories[k] & family)
    l = sum(ok(k) for k in all_keys)
    p = sum(w for k, w in demographic.items() if ok(k))
    return {
        "L0_pct": base.pct(l, len(all_keys)),
        "P0_attested_pct": base.pct(p, speaker_base),
    }


def layout_pressure(roots):
    total = 0
    post_vn_clusters = 0
    pre_nv_clusters = 0
    examples = []
    for rec in roots:
        root = rec["root"]
        for tam in TAM_FINALS:
            total += 1
            stem = root + tam
            preceding = stem[-1]
            # V+N: plural nasal comes after the person vowel, so the marker itself
            # never creates a consonant-consonant adjacency.
            # N+V: the plural nasal comes before the person vowel. If the stem ends
            # in a consonant, this necessarily creates C+N at the morpheme boundary.
            if preceding.lower() not in VOWELS:
                pre_nv_clusters += 1
                if len(examples) < 12:
                    examples.append({"stem": stem, "VN": stem + "in", "NV": stem + "ni"})
    return {
        "contexts": total,
        "tam_contexts": TAM_FINALS,
        "VN_person_then_plural": {
            "marker_induced_CC": post_vn_clusters,
            "marker_induced_CC_pct": base.pct(post_vn_clusters, total),
            "shape": "stem + person-vowel + N",
            "examples": ["...iN", "...uN", "...aN"],
        },
        "NV_plural_then_person": {
            "marker_induced_CC": pre_nv_clusters,
            "marker_induced_CC_pct": base.pct(pre_nv_clusters, total),
            "shape": "stem + N + person-vowel",
            "examples_requiring_cluster_or_coda_repair": examples,
        },
    }


def main():
    _, _, inventories, _, demographic, speaker_base = base.load_source()
    defs = json.load(open(TARGETS, encoding="utf-8"))["targets"]
    comp = base.compatibility_maps(defs, inventories)
    roots = json.load(open(ROOTS, encoding="utf-8"))["roots"]

    strict_n = set(defs["n"]["family"])
    final_nasal = strict_n | set(defs["m"]["family"]) | set(defs["ng"]["family"])
    fixed_candidates = {
        "strict_n": strict_n,
        "final_nasal_N_written_n": final_nasal,
        "fixed_m": set(defs["m"]["family"]),
        "fixed_s": set(defs["s"]["family"]),
        "fixed_t": set(defs["t"]["family"]),
        "fixed_k": set(defs["k"]["family"]),
        "fixed_r": set(defs["r"]["family"]),
    }

    person_metrics = base.set_metrics(list(PERSON.values()), comp, list(inventories), demographic, speaker_base)
    candidates = {}
    for name, family in fixed_candidates.items():
        candidates[name] = {
            **raw_family_coverage(family, inventories, demographic, speaker_base),
            **combined_coverage(family, comp, inventories, demographic, speaker_base),
        }

    out = {
        "schema": "unisermo/person-number-study@1",
        "dataset": {
            "languages": len(inventories),
            "demographic_languages": len(demographic),
            "speaker_base": speaker_base,
        },
        "person_mapping": PERSON,
        "person_vowel_subsystem": {
            "P0_attested_pct": person_metrics["P0"],
            "L0_pct": person_metrics["L0"],
        },
        "plural_candidates": candidates,
        "layout_pressure": layout_pressure(roots),
        "external_phonotactic_evidence": {
            "wals": {
                "sample_languages": 486,
                "simple_CV_only": 61,
                "moderately_complex": 274,
                "complex": 151,
                "note": "CV is reported as the syllable type occurring in every language; final C is a step up in complexity."
            },
            "kramer_zec_2020": {
                "restricted_word_final_coda_systems": 97,
                "nasals_allowed_pct": 97.9,
                "nasals_only_pct": 24.7,
                "note": "In their restricted-coda sample, nasals are overwhelmingly the most permissive final consonant class."
            }
        },
        "decision": {
            "person": {"first": "i", "second": "u", "third": "a"},
            "plural": {
                "morphophoneme": "N",
                "written": "n",
                "default_realization": "n",
                "accepted_place_realizations": ["n", "ɳ", "m", "ŋ", "ɴ"],
                "position": "after person vowel",
                "forms": {"1SG": "i", "2SG": "u", "3SG": "a", "1PL": "in", "2PL": "un", "3PL": "an"},
                "reason": "near-zero demographic inventory penalty under place-tolerant nasal production, exceptional coda typology, and zero marker-induced CC clusters in the tested suffix architecture"
            }
        }
    }
    with open(RESULTS, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
