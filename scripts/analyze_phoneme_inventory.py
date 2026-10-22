#!/usr/bin/env python3
"""Evaluate auxiliary-language phoneme inventories against frozen GlottoDelta data.

This is research tooling. It does not change GlottoDelta's production L/P semantics.
In particular, P_attested below answers a different question from the UI's P:
"does a demographic language have an attested member of this target-realization
family?" It intentionally does not require GlottoDelta's green/amber orthography
adjudication, because this study is about likely production familiarity.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import os
import re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASELINE = os.path.join(ROOT, "baseline", "original.html")
TARGETS_PATH = os.path.join(ROOT, "research", "phonology", "phoneme_targets.json")
CANDIDATES_PATH = os.path.join(ROOT, "research", "phonology", "candidates.json")
ROOTS_PATH = os.path.join(ROOT, "research", "phonology", "latin_roots_seed.json")
RESULTS_PATH = os.path.join(ROOT, "research", "phonology", "results.json")
REPORT_PATH = os.path.join(ROOT, "research", "phonology", "phoneme_selection.md")

PLACEHOLDER_ISO = {None, "", "mis", "und"}


def extract_raw(js: str, name: str) -> str:
    m = re.search(r"\b(?:const|let|var)\s+" + re.escape(name) + r"\s*=\s*", js)
    if not m:
        raise KeyError(name)
    i = m.end()
    op = js[i]
    if op not in "{[":
        raise ValueError(f"{name} does not start with JSON-like object/array")
    cl = {"{": "}", "[": "]"}[op]
    depth = 0
    j = i
    instr = None
    esc = False
    while j < len(js):
        c = js[j]
        if instr:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == instr:
                instr = None
        else:
            if c in "\"'`":
                instr = c
            elif c == op:
                depth += 1
            elif c == cl:
                depth -= 1
                if depth == 0:
                    return js[i : j + 1]
        j += 1
    raise ValueError(f"unbalanced constant {name}")


def lang_key(lang: dict) -> str:
    iso = lang.get("iso")
    if iso not in PLACEHOLDER_ISO:
        return f"i:{iso}"
    glot = lang.get("glottocode")
    return f"g:{glot}" if glot else f"n:{lang.get('name', '')}"


def load_source():
    html = open(BASELINE, encoding="utf-8").read()
    marker = re.search(r"<script>\s*const DATA=", html)
    if not marker:
        raise RuntimeError("DATA script not found in frozen baseline")
    js = html[marker.start() : html.index("</script>", marker.start())]
    data = json.loads(extract_raw(js, "DATA"))
    speakers = json.loads(extract_raw(js, "SPEAKER_ESTIMATES"))

    inventories: dict[str, set[str]] = {}
    records: dict[str, dict] = {}
    for symbol, payload in data.items():
        for lang in payload.get("languages", []):
            key = lang_key(lang)
            inventories.setdefault(key, set()).add(symbol)
            records.setdefault(key, lang)

    demographic = {}
    for key, lang in records.items():
        iso = lang.get("iso")
        if iso and iso in speakers:
            demographic[key] = float(speakers[iso])

    speaker_base = sum(demographic.values())
    return data, speakers, inventories, records, demographic, speaker_base


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def pct(n, d):
    return 100.0 * n / d if d else 0.0


def compatibility_maps(target_defs, inventories):
    strict = {}
    for t, meta in target_defs.items():
        family = set(meta["family"])
        strict[t] = {k: bool(inv & family) for k, inv in inventories.items()}
    return strict


def soft_compatibility_maps(target_defs, soft_mergers, inventories):
    soft = {}
    for t, meta in target_defs.items():
        family = set(meta["family"])
        for fallback in soft_mergers.get(t, []):
            family.update(target_defs[fallback]["family"])
        soft[t] = {k: bool(inv & family) for k, inv in inventories.items()}
    return soft


def set_metrics(target_names, comp, all_keys, demographic, speaker_base):
    dist_pop = Counter()
    dist_lang = Counter()
    pop_missing_total = 0.0
    lang_missing_total = 0
    for key in all_keys:
        missing = sum(not comp[t][key] for t in target_names)
        dist_lang[missing] += 1
        lang_missing_total += missing
        if key in demographic:
            w = demographic[key]
            dist_pop[missing] += w
            pop_missing_total += w * missing

    def cum(counter, limit):
        return sum(v for k, v in counter.items() if k <= limit)

    return {
        "target_count": len(target_names),
        "P0": pct(cum(dist_pop, 0), speaker_base),
        "P1": pct(cum(dist_pop, 1), speaker_base),
        "P2": pct(cum(dist_pop, 2), speaker_base),
        "P3": pct(cum(dist_pop, 3), speaker_base),
        "L0": pct(cum(dist_lang, 0), len(all_keys)),
        "L1": pct(cum(dist_lang, 1), len(all_keys)),
        "L2": pct(cum(dist_lang, 2), len(all_keys)),
        "L3": pct(cum(dist_lang, 3), len(all_keys)),
        "mean_missing_P": pop_missing_total / speaker_base if speaker_base else 0.0,
        "mean_missing_L": lang_missing_total / len(all_keys) if all_keys else 0.0,
        "population_missing_histogram": {str(k): v for k, v in sorted(dist_pop.items())},
        "language_missing_histogram": {str(k): v for k, v in sorted(dist_lang.items())},
    }


def target_metrics(target_defs, comp, all_keys, demographic, speaker_base):
    out = {}
    for t, meta in target_defs.items():
        l_count = sum(comp[t][k] for k in all_keys)
        p_weight = sum(w for k, w in demographic.items() if comp[t][k])
        out[t] = {
            "canonical": meta["canonical"],
            "family": meta["family"],
            "L_family_count": l_count,
            "L_family_pct": pct(l_count, len(all_keys)),
            "P_attested_weight": p_weight,
            "P_attested_pct": pct(p_weight, speaker_base),
        }
    return out


def pair_metrics(pairs, comp, all_keys, demographic, speaker_base):
    out = {}
    for a, b in pairs:
        l_count = sum(comp[a][k] and comp[b][k] for k in all_keys)
        p_weight = sum(w for k, w in demographic.items() if comp[a][k] and comp[b][k])
        out[f"{a}:{b}"] = {
            "targets": [a, b],
            "L_both_pct": pct(l_count, len(all_keys)),
            "P_attested_both_pct": pct(p_weight, speaker_base),
        }
    return out


def tokenize_root(root: str):
    """Coarse Classical/International mapping used only for the root-pressure seed."""
    s = root.lower()
    tokens = []
    i = 0
    while i < len(s):
        if s.startswith("qu", i):
            tokens.extend(["k", "w"])
            i += 2
            continue
        ch = s[i]
        mapping = {
            "a": "a", "e": "e", "i": "i", "o": "o", "u": "u",
            "p": "p", "b": "b", "t": "t", "d": "d", "k": "k",
            "c": "k", "q": "k", "g": "g", "m": "m", "n": "n",
            "f": "f", "v": "v", "s": "s", "z": "z", "l": "l",
            "r": "r", "h": "h", "y": "y", "w": "w", "j": "y",
            "x": None,
        }
        if ch == "x":
            tokens.extend(["k", "s"])
        elif ch in mapping and mapping[ch]:
            tokens.append(mapping[ch])
        i += 1
    return tokens


def root_pressure(roots, candidates):
    demand = Counter()
    tokenized = []
    for rec in roots:
        needed = set(tokenize_root(rec["root"]))
        for t in needed:
            demand[t] += 1
        tokenized.append((rec, needed))

    candidate_scores = {}
    for name, candidate in candidates.items():
        have = set(candidate["targets"])
        exact = 0
        adaptation_units = 0
        missing_counter = Counter()
        examples = []
        for rec, needed in tokenized:
            missing = sorted(needed - have)
            if not missing:
                exact += 1
            else:
                adaptation_units += len(missing)
                missing_counter.update(missing)
                if len(examples) < 12:
                    examples.append({"root": rec["root"], "missing": missing})
        candidate_scores[name] = {
            "roots": len(tokenized),
            "exact_segment_coverage_pct": pct(exact, len(tokenized)),
            "mean_missing_target_types_per_root": adaptation_units / len(tokenized),
            "missing_target_pressure": dict(missing_counter.most_common()),
            "examples_requiring_adaptation": examples,
        }
    return dict(demand.most_common()), candidate_scores


def optimize_grammar_core(target_defs, comp, all_keys, demographic, speaker_base):
    mandatory = ["a", "i", "u"]
    pool = [
        "p", "b", "t", "d", "k", "g", "m", "n", "f", "v", "s", "z",
        "sh", "l", "r", "y", "w", "h", "ng",
    ]
    names = mandatory + pool
    bit = {t: 1 << i for i, t in enumerate(names)}

    # Aggregate demographic languages by their missing-target pattern. This turns
    # 384 language rows into ~250 weighted bitmasks and makes the combinatorial
    # search cheap enough to be a normal regression step.
    patterns = Counter()
    for key, weight in demographic.items():
        missing_mask = 0
        for t in names:
            if not comp[t][key]:
                missing_mask |= bit[t]
        patterns[missing_mask] += weight

    mandatory_mask = sum(bit[t] for t in mandatory)
    result = {}
    for total_size in range(6, 11):
        choose_n = total_size - len(mandatory)
        best = None
        best_targets = None
        for extra in itertools.combinations(pool, choose_n):
            candidate_mask = mandatory_mask
            for t in extra:
                candidate_mask |= bit[t]
            p0 = p1 = p2 = mean_num = 0.0
            for missing_mask, weight in patterns.items():
                missing = (missing_mask & candidate_mask).bit_count()
                if missing == 0:
                    p0 += weight
                if missing <= 1:
                    p1 += weight
                if missing <= 2:
                    p2 += weight
                mean_num += weight * missing
            score = (p0, p1, p2, -mean_num)
            if best is None or score > best:
                best = score
                best_targets = mandatory + list(extra)
        result[str(total_size)] = {
            "targets": best_targets,
            **set_metrics(best_targets, comp, all_keys, demographic, speaker_base),
        }
    return result


def f(x):
    return f"{x:.1f}"


def generate_report(results, roots_meta):
    tm = results["targets"]
    cm = results["candidates_strict"]
    soft = results["candidates_soft_production"]
    pairs = results["pairwise"]
    opt = results["grammar_core_search"]
    rp = results["root_pressure"]

    lines = []
    lines.append("# Phoneme selection study — working report")
    lines.append("")
    lines.append("> **Status:** decisions 1–6 below were confirmed by the project owner on 2026-08-08. The full phoneme inventory is not yet frozen because the affricate and family/macroarea studies remain open.")
    lines.append("")
    lines.append("## Method")
    lines.append("")
    lines.append(
        f"The frozen GlottoDelta baseline contains **{results['dataset']['languages']}** deduplicated source languages and "
        f"**{results['dataset']['demographic_languages']}** demographic-language entries, with a CLDR-derived weighted base of "
        f"**{results['dataset']['speaker_base']:,.0f}**. This base is a weighting universe, not a claim about unique world population."
    )
    lines.append("")
    lines.append("`P_attested` in this study is deliberately different from the production UI's `P`: it asks whether a demographic language has an attested member of a target realization family. It does **not** require GlottoDelta's green/amber orthography adjudication. `L_family` uses all source-attested languages.")
    lines.append("")
    lines.append("A target is a canonical phoneme plus a narrow acceptable realization family. The families are broad enough to avoid treating, for example, every rhotic as a new sound to learn, but are kept disjoint where possible so coverage is not inflated by double-counting one realization as two target vowels.")
    lines.append("")
    lines.append("## Individual target coverage")
    lines.append("")
    lines.append("| Target | Canonical | P_attested | L_family |")
    lines.append("|---|---:|---:|---:|")
    order = ["a","e","i","o","u","schwa","p","b","t","d","k","g","m","n","f","v","s","z","sh","l","r","y","w","h","ng"]
    for t in order:
        x = tm[t]
        lines.append(f"| {t} | /{x['canonical']}/ | {f(x['P_attested_pct'])}% | {f(x['L_family_pct'])}% |")

    lines.append("")
    lines.append("## Inventory candidates")
    lines.append("")
    lines.append("`P0` means zero unfamiliar target categories; `P1`/`P2` allow at most one/two. These are **inventory compatibility proxies**, not comprehension rates.")
    lines.append("")
    lines.append("| Candidate | N | P0 | P1 | P2 | mean missing | L0 |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for name in ["current_simple_21","no_schwa_20","latin17","latin17_yw","lexical22_yw","grammar6","grammar8","grammar10"]:
        x = cm[name]
        lines.append(f"| {name} | {x['target_count']} | {f(x['P0'])}% | {f(x['P1'])}% | {f(x['P2'])}% | {x['mean_missing_P']:.2f} | {f(x['L0'])}% |")

    cur = cm["current_simple_21"]
    nos = cm["no_schwa_20"]
    lines.append("")
    lines.append("### Result 1 — contrastive schwa is currently a poor trade")
    lines.append("")
    lines.append(
        f"Removing contrastive /ə/ raises P0 from **{f(cur['P0'])}%** to **{f(nos['P0'])}%**, "
        f"P2 from **{f(cur['P2'])}%** to **{f(nos['P2'])}%**, and reduces weighted mean missing categories "
        f"from **{cur['mean_missing_P']:.2f}** to **{nos['mean_missing_P']:.2f}**. A sixth vowel raises the theoretical choice capacity "
        f"by only **{results['information']['five_to_six_vowel_bits']:.3f} bits per vowel choice**."
    )
    lines.append("")
    lines.append("**Working recommendation:** remove /ə/ as a contrastive vowel; still allow [ə] as an unstressed reduction/allophone where it cannot change lexical or grammatical identity. The written grapheme question therefore disappears unless later evidence reintroduces contrastive schwa.")

    lines.append("")
    lines.append("### Result 2 — /j/ and /w/ deserve serious inclusion")
    lines.append("")
    lines.append(
        f"The glide target /j/ reaches **{f(tm['y']['P_attested_pct'])}% P_attested / {f(tm['y']['L_family_pct'])}% L_family**; /w/ reaches "
        f"**{f(tm['w']['P_attested_pct'])}% / {f(tm['w']['L_family_pct'])}%**. By comparison, strict /v/ is "
        f"**{f(tm['v']['P_attested_pct'])}% / {f(tm['v']['L_family_pct'])}%** and /z/ **{f(tm['z']['P_attested_pct'])}% / {f(tm['z']['L_family_pct'])}%**. "
        "The glides also have a plausible time-efficiency role because they can resolve hiatus without forcing a full extra syllable."
    )

    lines.append("")
    lines.append("### Result 3 — fragile contrasts should not carry critical grammar")
    lines.append("")
    lines.append("| Contrast | P_attested with both | L with both |")
    lines.append("|---|---:|---:|")
    for key in ["p:b","t:d","k:g","f:v","s:z","s:sh","l:r","e:i","o:u","y:w"]:
        x = pairs[key]
        lines.append(f"| {key.replace(':',' / ')} | {f(x['P_attested_both_pct'])}% | {f(x['L_both_pct'])}% |")
    lines.append("")
    lines.append("Voicing and fricative contrasts are valuable for preserving international roots, but their joint availability is materially lower than the strongest targets. This supports a split policy: robust contrasts for grammar; additional **soft lexical contrasts** where the protected lexicon forbids dangerous minimal pairs.")

    lines.append("")
    lines.append("### Accent-tolerant production experiment")
    lines.append("")
    sx = soft["lexical22_yw"]
    lines.append(
        f"If lexical accents are allowed to merge selected fragile contrasts (b→p, d→t, g→k, v→f/w, z→s, ʃ→s, l↔r) **without permitting those mergers to create protected minimal pairs**, "
        f"the 22-target lexical candidate reaches **{f(sx['P0'])}% production-P0**, **{f(sx['P1'])}% P1**, and **{f(sx['P2'])}% P2**, with weighted mean missing categories **{sx['mean_missing_P']:.2f}**. "
        "This is a production-accessibility model only; it does not prove that listeners can perceive every canonical contrast."
    )

    lines.append("")
    lines.append("## Grammar core search")
    lines.append("")
    lines.append("The search fixes /a i u/ and asks which additional target families maximize strict P0, then P1/P2, for total inventories of 6–10 categories. This is a statistical bound, not an automatic design recommendation.")
    lines.append("")
    lines.append("| N | Best strict target set | P0 | P1 | P2 |")
    lines.append("|---:|---|---:|---:|---:|")
    for n in sorted(opt, key=int):
        x = opt[n]
        lines.append(f"| {n} | {' '.join(x['targets'])} | {f(x['P0'])}% | {f(x['P1'])}% | {f(x['P2'])}% |")
    lines.append("")
    lines.append("The important design signal is not the exact winning set; it is that **grammar can be built from a much smaller, more globally robust contrast inventory than the lexicon**. A three-vowel grammatical subsystem /a i u/ is especially attractive, while the lexicon can retain /e o/ for Latin/international compatibility.")

    lines.append("")
    lines.append("## Latin/international root pressure — provisional seed")
    lines.append("")
    lines.append(f"The current seed has **{roots_meta['count']}** roots. It is intentionally small and must be expanded before final lexical decisions.")
    lines.append("")
    lines.append("Most demanded target categories in the seed:")
    lines.append("")
    demand = rp["target_demand"]
    lines.append(", ".join(f"`{k}` {v}" for k, v in list(demand.items())[:15]) + ".")
    lines.append("")
    lines.append("| Candidate | Exact segment coverage | Mean missing types/root | Main pressure |")
    lines.append("|---|---:|---:|---|")
    for name in ["current_simple_21","no_schwa_20","latin17","latin17_yw","lexical22_yw"]:
        x = rp["candidates"][name]
        pressure = ", ".join(f"{k}:{v}" for k,v in list(x["missing_target_pressure"].items())[:4]) or "—"
        lines.append(f"| {name} | {f(x['exact_segment_coverage_pct'])}% | {x['mean_missing_target_types_per_root']:.2f} | {pressure} |")
    lines.append("")
    lines.append("The seed should be read as a **pressure detector**. In particular it quantifies how often dropping /v/, /g/, /d/, /h/ or /w/ forces adaptation of highly recognizable stems; it does not yet assign frequency weights to those stems.")

    lines.append("")
    lines.append("## Complex segments /ts tʃ dʒ/ — resolved")
    lines.append("")
    lines.append("The dedicated `affricate_study.md` resolves all three as **non-independent phonemes**: `/t+s/ → [ts]`, `/t+j/ → [tj ~ tʃ]`, and `/d+j/ → [dj ~ dʒ]`. Transparent sequence pronunciations remain valid. This exploits retained `/j/`, preserves useful surface affricates, and avoids counting an affricate as a free one-unit timing shortcut.")
    lines.append("")
    lines.append("Whole-base component familiarity measured in that study is **86.3% P / 63.1% L** for `/t+s/`, **86.2% / 74.2%** for `/t+j/`, and **64.0% / 51.6%** for `/d+j/`. Direct affricate evidence is reported separately on the curated-profile denominator.")
    lines.append("")
    lines.append("## Confirmed design constraints — 2026-08-08")
    lines.append("")
    lines.append("1. **Schwa:** drop contrastive /ə/; allow [ə] only as a non-contrastive reduction/allophone.")
    lines.append("2. **Vowel architecture:** lexical /a e i o u/; reserve /a i u/ as the safest pool for grammar-critical endings/particles where practical.")
    lines.append("3. **Glides:** retain canonical /j/; carry /w/ as the strong default lexical candidate pending the final inventory-wide check. Choose spelling later, separately from IPA.")
    lines.append("4. **Rhotic policy:** retain one /r/ category but allow a broad rhotic realization family; do not prescribe trill vs tap vs approximant vs uvular realization.")
    lines.append("5. **Soft lexical contrasts:** continue evaluating /b d ɡ v z ʃ/ as canonical lexical contrasts, but prohibit grammar-critical distinctions and protected minimal pairs that depend only on a fragile merger pair.")
    lines.append("6. **Affricates:** no independent /ts tʃ dʒ/ phonemes. Use /t+s/, /t+j/, /d+j/ with optional fast/coalescent [ts], [tʃ], [dʒ] realizations; transparent sequence pronunciations remain valid.")
    lines.append("")
    lines.append("## Still required before final phoneme freeze")
    lines.append("")
    lines.append("The remaining major quantitative dimension before the full inventory freeze is **Glottolog family/macroarea dispersion (F)**, because the normalized local snapshot does not contain genealogy/area tables. The complex-segment study for `/ts tʃ dʒ/` is complete and no longer blocks the inventory.")
    lines.append("")
    lines.append("These confirmed constraints are recorded in the local repository, but they do not alter GlottoDelta's production L/P semantics. Synchronization into the separate auxiliary-language specification remains a distinct step.")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write results.json and phoneme_selection.md")
    args = parser.parse_args()

    data, speakers, inventories, records, demographic, speaker_base = load_source()
    cfg = load_json(TARGETS_PATH)
    target_defs = cfg["targets"]
    candidates_cfg = load_json(CANDIDATES_PATH)["candidates"]
    roots_cfg = load_json(ROOTS_PATH)
    roots = roots_cfg["roots"]
    all_keys = list(inventories)

    comp = compatibility_maps(target_defs, inventories)
    soft_comp = soft_compatibility_maps(target_defs, cfg.get("soft_mergers", {}), inventories)

    target_out = target_metrics(target_defs, comp, all_keys, demographic, speaker_base)
    candidates_strict = {
        name: set_metrics(c["targets"], comp, all_keys, demographic, speaker_base)
        for name, c in candidates_cfg.items()
    }
    candidates_soft = {
        name: set_metrics(c["targets"], soft_comp, all_keys, demographic, speaker_base)
        for name, c in candidates_cfg.items()
    }
    pairs = [("p","b"),("t","d"),("k","g"),("f","v"),("s","z"),("s","sh"),("l","r"),("e","i"),("o","u"),("y","w")]
    pair_out = pair_metrics(pairs, comp, all_keys, demographic, speaker_base)
    root_demand, root_candidates = root_pressure(roots, candidates_cfg)
    grammar_opt = optimize_grammar_core(target_defs, comp, all_keys, demographic, speaker_base)

    three_vowel = set_metrics(["a","i","u"], comp, all_keys, demographic, speaker_base)
    five_vowel = set_metrics(["a","e","i","o","u"], comp, all_keys, demographic, speaker_base)

    results = {
        "schema": "unisermo/phoneme-study-results@1",
        "dataset": {
            "chart_symbols": len(data),
            "languages": len(all_keys),
            "demographic_languages": len(demographic),
            "speaker_estimate_entries": len(speakers),
            "speaker_base": speaker_base,
            "speaker_base_note": "CLDR-derived weighting universe; not unique world-population headcount.",
        },
        "metric_note": "P_attested is a research metric based on source inventory attestation and target realization families. It is not the production UI P, which requires mapped/variant adjudication.",
        "targets": target_out,
        "candidates_strict": candidates_strict,
        "candidates_soft_production": candidates_soft,
        "pairwise": pair_out,
        "vowel_subsystems": {"three_vowel_aiu": three_vowel, "five_vowel_aeiou": five_vowel},
        "information": {"five_to_six_vowel_bits": math.log2(6/5)},
        "grammar_core_search": grammar_opt,
        "root_pressure": {"target_demand": root_demand, "candidates": root_candidates},
        "limitations": [
            "PHOIBLE is a convenience sample, not a probability sample of world languages.",
            "CLDR-derived speaker estimates form a weighting universe and may overlap L1/L2 populations.",
            "Target realization families are design assumptions and must be reviewed phoneme by phoneme.",
            "Inventory membership is not the same as effortless perception, production in all contexts, or accent-free acquisition.",
            "Affricates /ts tʃ dʒ/ are not directly scored by the current 111-cell standalone chart data.",
            "The Latin/international root seed is provisional and unweighted by usage frequency.",
        ],
    }

    print(json.dumps({
        "dataset": results["dataset"],
        "targets": {k: {"P": round(v["P_attested_pct"], 2), "L": round(v["L_family_pct"], 2)} for k,v in target_out.items()},
        "candidates": {k: {q: round(v[q],2) for q in ("P0","P1","P2","P3","mean_missing_P")} for k,v in candidates_strict.items()},
        "grammar_core_search": {k: {"targets":v["targets"], "P0":round(v["P0"],2), "P1":round(v["P1"],2), "P2":round(v["P2"],2)} for k,v in grammar_opt.items()},
    }, ensure_ascii=False, indent=2))

    if args.write:
        with open(RESULTS_PATH, "w", encoding="utf-8") as fobj:
            json.dump(results, fobj, ensure_ascii=False, indent=2)
            fobj.write("\n")
        report = generate_report(results, {"count": len(roots)})
        with open(REPORT_PATH, "w", encoding="utf-8") as fobj:
            fobj.write(report)


if __name__ == "__main__":
    main()
