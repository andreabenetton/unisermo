#!/usr/bin/env python3
"""Quantify candidate treatments of Latin-root <c> for GlottoDelta.

This is a lexical/orthographic audit over the frozen provisional Latin root seed.
It does not define phoneme prevalence and does not alter production semantics.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "research/phonology/latin_roots_seed.json"
OUT_JSON = ROOT / "research/phonology/c_orthography_study.json"
OUT_MD = ROOT / "research/phonology/c_orthography_study.md"


def c_context(root: str, i: int) -> str:
    if i == len(root) - 1:
        return "final"
    if root[i + 1] in {"e", "i"}:
        return "soft_context"
    return "hard_context"


def transform(root: str, strategy: str) -> str:
    out: list[str] = []
    for i, ch in enumerate(root):
        if ch != "c":
            out.append(ch)
            continue
        context = c_context(root, i)
        soft = context == "soft_context"
        if strategy == "soft_c":
            # c is reserved for the soft category [ts~tsh~s]; hard/final c -> k.
            out.append("c" if soft else "k")
        elif strategy == "no_c_s":
            # No c: soft c -> s; hard/final c -> k.
            out.append("s" if soft else "k")
        elif strategy == "no_c_tj":
            # No c: soft c -> tj; hard/final c -> k.
            out.append("tj" if soft else "k")
        elif strategy == "hard_c":
            # c is /k/; soft-context c -> s. This is one-to-one only if k is
            # removed or otherwise not a competing spelling for /k/.
            out.append("s" if soft else "c")
        elif strategy == "contextual_c":
            # Romance-style contextual reading: no orthographic change.
            out.append("c")
        else:
            raise ValueError(strategy)
    return "".join(out)


def levenshtein(a: str, b: str) -> int:
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(cur[-1] + 1, prev[j] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def collision_groups(forms: dict[str, str]) -> list[dict]:
    by_form: dict[str, list[str]] = defaultdict(list)
    for source, form in forms.items():
        by_form[form].append(source)
    return [
        {"form": form, "roots": sorted(rs)}
        for form, rs in sorted(by_form.items())
        if len(rs) > 1
    ]


def variant_c_to_s(form: str) -> str:
    return form.replace("c", "s")


def main() -> None:
    seed = json.loads(SEED.read_text(encoding="utf-8"))
    roots = [r["root"] for r in seed["roots"]]
    c_roots = [r for r in roots if "c" in r]

    context_counts = Counter()
    context_roots: dict[str, set[str]] = defaultdict(set)
    occurrence_rows = []
    for root in roots:
        for i, ch in enumerate(root):
            if ch != "c":
                continue
            context = c_context(root, i)
            context_counts[context] += 1
            context_roots[context].add(root)
            occurrence_rows.append(
                {
                    "root": root,
                    "index": i,
                    "following": root[i + 1] if i + 1 < len(root) else None,
                    "context": context,
                }
            )

    strategies = {
        "soft_c": {
            "label": "c = soft category [ts~tsh~s]; hard/final c -> k",
            "one_to_one": True,
        },
        "no_c_s": {
            "label": "no c; soft c -> s; hard/final c -> k",
            "one_to_one": True,
        },
        "no_c_tj": {
            "label": "no c; soft c -> tj; hard/final c -> k",
            "one_to_one": True,
        },
        "hard_c": {
            "label": "c = /k/; soft c -> s",
            "one_to_one": "only if k is removed as a competing spelling",
        },
        "contextual_c": {
            "label": "contextual c: soft before e/i, /k/ elsewhere",
            "one_to_one": False,
        },
    }

    strategy_results = {}
    for key, meta in strategies.items():
        forms = {root: transform(root, key) for root in roots}
        changed = [root for root in roots if forms[root] != root]
        c_changed = [root for root in c_roots if forms[root] != root]
        total_edit = sum(levenshtein(root, forms[root]) for root in roots)
        similarities = [
            1.0 - levenshtein(root, forms[root]) / max(len(root), len(forms[root]), 1)
            for root in roots
        ]
        canonical_collisions = collision_groups(forms)

        soft_variant_collisions = []
        if key == "soft_c":
            variant_forms = {root: variant_c_to_s(form) for root, form in forms.items()}
            soft_variant_collisions = collision_groups(variant_forms)

        strategy_results[key] = {
            **meta,
            "exact_unchanged_roots": len(roots) - len(changed),
            "exact_unchanged_rate": (len(roots) - len(changed)) / len(roots),
            "changed_roots": changed,
            "changed_c_bearing_roots": c_changed,
            "exact_unchanged_c_bearing_roots": len(c_roots) - len(c_changed),
            "exact_unchanged_c_bearing_rate": (len(c_roots) - len(c_changed)) / len(c_roots),
            "total_levenshtein_edits": total_edit,
            "mean_root_similarity": sum(similarities) / len(similarities),
            "net_length_change": sum(len(forms[r]) - len(r) for r in roots),
            "canonical_collision_groups": canonical_collisions,
            "soft_c_to_s_variant_collision_groups": soft_variant_collisions,
            "transformed_c_roots": {r: forms[r] for r in c_roots},
        }

    total_c = sum(context_counts.values())
    soft_n = context_counts["soft_context"]
    hard_or_final = context_counts["hard_context"] + context_counts["final"]

    result = {
        "schema": "glottodelta/c-orthography-study@1",
        "status": "research",
        "source": str(SEED.relative_to(ROOT)),
        "method": {
            "scope": "74-root provisional Latin/international audit seed",
            "soft_context_rule": "c immediately before e or i",
            "hard_context_rule": "non-final c not immediately before e or i",
            "final_rule": "final c kept separate descriptively; strategies that need a fixed bare-root realization map it with hard /k/",
            "warning": "This seed is not a frequency corpus; results measure lexical/orthographic cost in the current candidate-root set, not token frequency or global speaker exposure.",
        },
        "summary": {
            "roots": len(roots),
            "c_bearing_roots": len(c_roots),
            "c_bearing_root_rate": len(c_roots) / len(roots),
            "c_occurrences": total_c,
            "soft_context_occurrences": soft_n,
            "soft_context_share": soft_n / total_c,
            "hard_context_occurrences": context_counts["hard_context"],
            "hard_context_share": context_counts["hard_context"] / total_c,
            "final_occurrences": context_counts["final"],
            "final_share": context_counts["final"] / total_c,
            "hard_or_final_occurrences": hard_or_final,
            "hard_or_final_share": hard_or_final / total_c,
            "all_soft_keep_spelling_affected_c_roots": len(
                {row["root"] for row in occurrence_rows if row["context"] != "soft_context"}
            ),
            "all_soft_keep_spelling_affected_c_root_rate": len(
                {row["root"] for row in occurrence_rows if row["context"] != "soft_context"}
            ) / len(c_roots),
        },
        "context_roots": {k: sorted(v) for k, v in context_roots.items()},
        "occurrences": occurrence_rows,
        "strategies": strategy_results,
    }

    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    s = result["summary"]
    soft = strategy_results["soft_c"]
    nos = strategy_results["no_c_s"]
    notj = strategy_results["no_c_tj"]
    hardc = strategy_results["hard_c"]
    contextual = strategy_results["contextual_c"]

    lines = [
        "# Quantitative study: what should written `c` mean?",
        "",
        "## Scope",
        "",
        "This is a lexical/orthographic audit of the frozen provisional `latin_roots_seed.json`. It tests whether adding a written `c` as a soft category is justified by preservation of Latin/international root shapes. It is **not** a phoneme-prevalence study and the 74-root seed is **not** a frequency corpus.",
        "",
        "For reproducibility, a `c` immediately before `e` or `i` is classed as a **soft-context** occurrence. Non-final `c` elsewhere is **hard-context**. Final `c` is reported separately because truncated roots such as `fac-`, `doc-`, and `voc-` can show derivative alternations in descendant languages; when a strategy requires a fixed bare-root reading, final `c` is mapped with /k/.",
        "",
        "## Distribution of `c` in the 74-root seed",
        "",
        f"- Roots: **{s['roots']}**.",
        f"- Roots containing `c`: **{s['c_bearing_roots']}/{s['roots']} = {s['c_bearing_root_rate']*100:.1f}%**.",
        f"- Total `c` occurrences: **{s['c_occurrences']}**.",
        f"- Soft-context (`ce/ci`): **{s['soft_context_occurrences']}/{s['c_occurrences']} = {s['soft_context_share']*100:.1f}%**.",
        f"- Hard-context: **{s['hard_context_occurrences']}/{s['c_occurrences']} = {s['hard_context_share']*100:.1f}%**.",
        f"- Final `c`: **{s['final_occurrences']}/{s['c_occurrences']} = {s['final_share']*100:.1f}%**.",
        f"- Hard-or-final combined: **{s['hard_or_final_occurrences']}/{s['c_occurrences']} = {s['hard_or_final_share']*100:.1f}%**.",
        "",
        "Soft-context roots are `centr`, `cert`, the first `c` of `circul`, and `civ`. Hard-context examples include `cap`, `clar`, `com`, `cur`, `dict`, and `struct`; final examples include `fac`, `doc`, `loc`, `spec`, and `voc`.",
        "",
        "## Strategy comparison",
        "",
        "| Strategy | Exact roots retained | Exact c-roots retained | Total edit distance | Mean similarity | Canonical collisions |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for key in ["soft_c", "no_c_s", "no_c_tj", "hard_c", "contextual_c"]:
        r = strategy_results[key]
        lines.append(
            f"| {r['label']} | {r['exact_unchanged_roots']}/{len(roots)} ({r['exact_unchanged_rate']*100:.1f}%) | "
            f"{r['exact_unchanged_c_bearing_roots']}/{len(c_roots)} ({r['exact_unchanged_c_bearing_rate']*100:.1f}%) | "
            f"{r['total_levenshtein_edits']} | {r['mean_root_similarity']*100:.1f}% | {len(r['canonical_collision_groups'])} |"
        )

    lines += [
        "",
        "### Root-by-root effect on the 20 `c`-bearing roots",
        "",
        "| Seed root | soft `c` `[ts~tʃ~s]` | no `c` (`s/k`) | `c=/k/` |",
        "|---|---|---|---|",
    ]
    for root in c_roots:
        lines.append(
            f"| `{root}` | `{transform(root, 'soft_c')}` | `{transform(root, 'no_c_s')}` | `{transform(root, 'hard_c')}` |"
        )

    lines += [
        "",
        "### Proposed soft `c` = `[ts ~ tʃ ~ s]`",
        "",
        f"If `c` is reserved for the soft category and hard/final Latin `c` is normalized to `k`, only **{soft['exact_unchanged_c_bearing_roots']}/{len(c_roots)} = {soft['exact_unchanged_c_bearing_rate']*100:.1f}%** of the roots containing `c` remain exactly unchanged. Across the whole seed, **{soft['exact_unchanged_roots']}/{len(roots)} = {soft['exact_unchanged_rate']*100:.1f}%** remain exact.",
        "",
        f"Compared with simply having **no `c`** and writing soft-context `c` as `s`, soft `c` saves only **{soft['exact_unchanged_roots'] - nos['exact_unchanged_roots']} exact root spellings** and **{nos['total_levenshtein_edits'] - soft['total_levenshtein_edits']} character substitutions** in this seed.",
        "",
        f"The soft-`c` strategy creates **{len(soft['canonical_collision_groups'])} canonical root collisions**. Allowing its `[s]` accent realization also creates **{len(soft['soft_c_to_s_variant_collision_groups'])} collisions within this 74-root seed**. Thus collision risk is not the immediate problem here; the main cost is that most Latin `c` occurrences are not soft-context occurrences.",
        "",
        "### What if all inherited `c` spellings were kept but `c` were always soft?",
        "",
        f"That would put **{s['hard_or_final_occurrences']}/{s['c_occurrences']} = {s['hard_or_final_share']*100:.1f}%** of the current `c` occurrences into a hard-or-final context, affecting **{s['all_soft_keep_spelling_affected_c_roots']}/{len(c_roots)} = {s['all_soft_keep_spelling_affected_c_root_rate']*100:.1f}%** of the `c`-bearing roots. In other words, an always-soft `c` cannot preserve both spelling and the current root-level sound structure for most of the seed.",
        "",
        "### The orthographically strongest alternative",
        "",
        f"If `c` represented /k/ and soft-context `c` were rewritten `s`, **{hardc['exact_unchanged_roots']}/{len(roots)} = {hardc['exact_unchanged_rate']*100:.1f}%** of all roots would stay exactly unchanged. This is much stronger for Latin-root preservation than soft `c`. But it is compatible with the project's one-to-one spelling principle only if `k` ceases to be a second spelling of /k/; that is a separate orthographic decision, not a result of this test.",
        "",
        "A traditional contextual `c` would preserve 100% of spellings, but it directly violates the current fixed grapheme-to-phoneme principle by making `c` context-dependent.",
        "",
        "## Preliminary conclusion",
        "",
        "On the current 74-root seed, **adding `c` specifically as a soft `[ts ~ tʃ ~ s]` category has a small lexical-recognition payoff**. Only 19.0% of `c` occurrences are in the simple `ce/ci` soft context, and relative to the no-`c` + `s/k` solution the new grapheme preserves only three additional roots exactly. The proposal is collision-safe in this seed, but the benefit is too small to justify freezing `c` yet.",
        "",
        "Before a final orthographic decision, this test should be repeated on the planned 300–500-root Latin/international candidate lexicon. If the same ratio persists, the quantitative evidence would favor **no soft `c` phoneme/grapheme**; if preserving Latin spelling is prioritized strongly enough to keep `c`, the data currently favor investigating **`c` for /k/** (with `k` correspondingly reconsidered) rather than `c` for the soft category.",
    ]

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "roots": len(roots),
        "c_roots": len(c_roots),
        "c_occurrences": total_c,
        "contexts": dict(context_counts),
        "soft_c_exact": soft["exact_unchanged_roots"],
        "no_c_s_exact": nos["exact_unchanged_roots"],
        "no_c_tj_exact": notj["exact_unchanged_roots"],
        "hard_c_exact": hardc["exact_unchanged_roots"],
        "contextual_exact": contextual["exact_unchanged_roots"],
        "soft_c_collisions": len(soft["canonical_collision_groups"]),
        "soft_c_to_s_variant_collisions": len(soft["soft_c_to_s_variant_collision_groups"]),
    }, indent=2))


if __name__ == "__main__":
    main()
