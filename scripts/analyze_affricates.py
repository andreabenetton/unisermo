#!/usr/bin/env python3
"""Evaluate /ts tʃ dʒ/ without pretending complex segments are free phonemes.

The frozen GlottoDelta chart does not expose these affricates as standalone DATA
cells. This study therefore keeps two evidence layers separate:

1. whole-base *component availability* proxies from the 2,122-language frozen
   inventory aggregation; and
2. direct affricate attestation in the 77 currently curated orthography/phoneme
   profiles, reported only against the population represented by those profiles.

The goal is auxiliary-language design, not a new production L/P metric.
"""
from __future__ import annotations

import json
import os
import re

from analyze_phoneme_inventory import BASELINE, extract_raw, load_source, pct

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "research", "phonology", "affricate_results.json")
REPORT = os.path.join(ROOT, "research", "phonology", "affricate_study.md")
SUPP = os.path.join(ROOT, "data", "orthography-supplement.json")

FAMILIES = {
    "t": {"t", "ʈ"},
    "d": {"d", "ɖ"},
    "s": {"s"},
    "sh": {"ʃ", "ɕ", "ʂ"},
    "zh": {"ʒ", "ʑ", "ʐ"},
    "j": {"j", "ɰ"},
}

PROXIES = {
    "ts_components": ("t", "s"),
    "tsh_components": ("t", "sh"),
    "dzh_components": ("d", "zh"),
    "tj_components": ("t", "j"),
    "dj_components": ("d", "j"),
}


def has_parts(inv: set[str], parts: tuple[str, ...]) -> bool:
    return all(bool(inv & FAMILIES[p]) for p in parts)


def component_metrics(inventories, demographic, speaker_base):
    out = {}
    for name, parts in PROXIES.items():
        l = sum(has_parts(inv, parts) for inv in inventories.values())
        p = sum(w for key, w in demographic.items() if has_parts(inventories[key], parts))
        out[name] = {
            "parts": list(parts),
            "L_component_pct": pct(l, len(inventories)),
            "P_component_pct": pct(p, speaker_base),
        }
    return out


def load_curated_profiles(speakers):
    html = open(BASELINE, encoding="utf-8").read()
    marker = re.search(r"<script>\s*const DATA=", html)
    js = html[marker.start() : html.index("</script>", marker.start())]
    ortho = json.loads(extract_raw(js, "ORTHO"))
    verified = json.loads(extract_raw(js, "VERIFIED_ORTHO"))
    by_iso_raw = extract_raw(js, "ORTHO_BY_ISO")
    by_iso = dict(re.findall(r"([a-z]{3}):'([^']+)'", by_iso_raw))

    profiles = {iso: set(mapping) for iso, mapping in verified.items()}
    for iso, key in by_iso.items():
        if iso not in profiles and key in ortho:
            profiles[iso] = set(ortho[key])

    supplement = json.load(open(SUPP, encoding="utf-8"))
    for iso, entry in supplement.items():
        if iso.startswith("_"):
            continue
        profiles.setdefault(iso, set()).update((entry.get("ortho") or {}).keys())

    weighted = {iso: float(speakers[iso]) for iso in profiles if iso in speakers}
    return profiles, weighted


def normalize_affricate(label: str) -> str:
    # Tie bars and narrow coronal place diacritics do not create a new target here.
    for mark in ("͡", "̠", "̪", "̺", "̟"):
        label = label.replace(mark, "")
    return label


def curated_affricate_metrics(profiles, weighted):
    targets = {"ts": "ts", "tsh": "tʃ", "dzh": "dʒ"}
    base = sum(weighted.values())
    out = {}
    for name, normalized_target in targets.items():
        hit = [
            iso for iso, keys in profiles.items()
            if iso in weighted and any(normalize_affricate(k) == normalized_target for k in keys)
        ]
        pop = sum(weighted[iso] for iso in hit)
        out[name] = {
            "profile_language_count": len(hit),
            "P_within_profiled_pct": pct(pop, base),
            "profiled_population_weight": pop,
            "profiled_isos": sorted(hit),
        }
    return {
        "profile_language_count": len(profiles),
        "weighted_profile_language_count": len(weighted),
        "profiled_population_base": base,
        "targets": out,
    }


def recommendations(component, curated):
    return {
        "ts": {
            "status": "sequence",
            "underlying": ["t", "s"],
            "surface": ["ts"],
            "new_phoneme": False,
            "reason": "Both components are already core candidates; treating /ts/ as a sequence preserves the sound without a new contrast.",
        },
        "tsh": {
            "status": "coalescent_sequence",
            "underlying": ["t", "j"],
            "surface": ["tj", "tʃ"],
            "new_phoneme": False,
            "reason": "With /j/ retained, /tj/ can remain transparent or coalesce to [tʃ]. This avoids requiring a separate affricate category.",
        },
        "dzh": {
            "status": "coalescent_sequence",
            "underlying": ["d", "j"],
            "surface": ["dj", "dʒ"],
            "new_phoneme": False,
            "reason": "With /j/ retained, /dj/ can remain transparent or coalesce to [dʒ]. The underlying /d/ is already a soft lexical contrast, so this must not carry critical grammar.",
        },
        "j_assumption": "Treat canonical /j/ as retained. /w/ is also carried forward as the default lexical candidate unless later evidence overturns it.",
    }


def main():
    _, speakers, inventories, _, demographic, speaker_base = load_source()
    comp = component_metrics(inventories, demographic, speaker_base)
    profiles, weighted = load_curated_profiles(speakers)
    curated = curated_affricate_metrics(profiles, weighted)
    result = {
        "schema": "glottodelta/affricate-study@1",
        "method": {
            "warning": "Whole-base figures are component-availability proxies, not direct affricate prevalence. Direct affricate figures use only curated profiles and have their own denominator.",
            "speaker_base": speaker_base,
            "language_base": len(inventories),
        },
        "component_proxies": comp,
        "curated_profiles": curated,
        "recommendations": recommendations(comp, curated),
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")

    def cp(name):
        m = comp[name]
        return f"{m['P_component_pct']:.1f}% P / {m['L_component_pct']:.1f}% L"

    ct = curated["targets"]
    profile_share = pct(curated["profiled_population_base"], speaker_base)
    report = f"""# Affricate study — /ts tʃ dʒ/

## Status

Decision-ready study. Canonical `/j/` is treated as retained; `/w/` is carried forward as the strong default lexical candidate. No production GlottoDelta L/P semantics are changed.

## Why two evidence layers are required

The frozen GlottoDelta chart has 111 standalone IPA chart symbols and does not expose `/ts tʃ dʒ/` as directly comparable DATA cells. Reporting a made-up whole-population affricate percentage would therefore be methodologically wrong.

Instead this study reports:

1. **component availability** across the complete frozen GlottoDelta language/demographic base; and
2. **direct affricate presence** only inside the curated orthography/phoneme profiles, whose weighted population covers **{profile_share:.1f}%** of the demographic base.

## Whole-base component availability

| Construction | Interpretation | P component | L component |
|---|---|---:|---:|
| `/t+s/` | transparent route to [ts] | {comp['ts_components']['P_component_pct']:.1f}% | {comp['ts_components']['L_component_pct']:.1f}% |
| `/t+ʃ/` | speakers familiar with both portions of [tʃ] | {comp['tsh_components']['P_component_pct']:.1f}% | {comp['tsh_components']['L_component_pct']:.1f}% |
| `/d+ʒ/` | speakers familiar with both portions of [dʒ] | {comp['dzh_components']['P_component_pct']:.1f}% | {comp['dzh_components']['L_component_pct']:.1f}% |
| `/t+j/` | proposed underlying route to [tʃ] | {comp['tj_components']['P_component_pct']:.1f}% | {comp['tj_components']['L_component_pct']:.1f}% |
| `/d+j/` | proposed underlying route to [dʒ] | {comp['dj_components']['P_component_pct']:.1f}% | {comp['dj_components']['L_component_pct']:.1f}% |

The `/tj/` route is especially attractive: its component familiarity is almost the same as `/ts/` and substantially broader than requiring a native `/ʃ/` category as a prerequisite. `/dj/` inherits the weaker global availability of `/d/`, which is already classified as a soft lexical contrast.

## Direct affricate evidence in curated profiles

The profiled denominator is deliberately separate from the complete GlottoDelta base.

| Affricate | Profile languages | Share of profiled population |
|---|---:|---:|
| `/ts/` | {ct['ts']['profile_language_count']} | {ct['ts']['P_within_profiled_pct']:.1f}% |
| `/tʃ/` | {ct['tsh']['profile_language_count']} | {ct['tsh']['P_within_profiled_pct']:.1f}% |
| `/dʒ/` | {ct['dzh']['profile_language_count']} | {ct['dzh']['P_within_profiled_pct']:.1f}% |

This confirms that the postalveolar affricates are familiar to a large part of the heavily weighted profiled population, but it does **not** establish that they deserve independent phoneme status.

## Timing and perceptual interpretation

An affricate is not a free one-beat substitute for a stop plus fricative. Its identity depends on temporally coordinated closure/release and frication cues. For a language whose explicit objective is speaking-time efficiency, counting a written `c` or `j` as one character therefore must not be counted as a one-segment timing gain.

The useful optimization is instead **coarticulation**: allow adjacent phonemes to fuse in fluent speech without making the fused realization a new lexical contrast.

## Recommendation

### `/ts/`: remove independent phoneme status

Represent it phonologically as `/t+s/`. A speaker may realize the sequence tightly as [ts]. This keeps the useful surface sound while adding no phoneme and no new minimal-pair axis.

### `/tʃ/`: remove independent phoneme status; derive from `/t+j/`

Permit `/tj/ → [tʃ]` as an accepted coalescent pronunciation. A non-coalesced [tj] remains equally valid. Because `/j/` is independently extremely strong in the inventory study, this recovers [tʃ] using categories we want anyway.

### `/dʒ/`: remove independent phoneme status; derive from `/d+j/`

Permit `/dj/ → [dʒ]` as an accepted coalescent pronunciation, with [dj] equally valid. Since `/d/` is a soft lexical contrast, no grammar-critical opposition should depend on this sequence versus a form that would collide under `d→t` accent tolerance.

## Lexical consequence

The current Latin/international seed creates essentially no independent pressure for affricate phonemes. Classical/learned Latin roots already map through `/k g t d s j/`; modern descendants disagree strongly on the outcome of soft `c/g` and palatalization. Encoding one descendant's affricate as canonical would often reduce neutrality rather than improve it.

Therefore the design rule should be:

> Preserve international roots with the simpler underlying phonemes; permit [ts], [tʃ], and [dʒ] as fast/coalesced surface realizations where the underlying sequence licenses them.

## Resulting phoneme accounting

The former three entries `ts`, `c=/tʃ/`, `j=/dʒ/` contribute **zero independent phonemes**. Canonical IPA `/j/` returns as a glide; its eventual grapheme must therefore be chosen independently of the old `j=/dʒ/` convention. `/w/` remains the presumed lexical glide candidate.
"""
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write(report)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
