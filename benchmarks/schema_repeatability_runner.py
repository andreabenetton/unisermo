"""Prospective, tightly bounded development-only schema repeatability experiment.

32 isolated Qwen3 32B OpenRouter requests = 8 docs x 2 conditions x 2 repeats.
Uses exact historical prompts from operator_schema_fresh.build; never accesses holdout.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import time
from collections import Counter
from pathlib import Path

from benchmarks.openrouter_runner import MODELS, RateLimited, invoke
from benchmarks.operator_schema_fresh import build as historical_build
from benchmarks.schema_repeatability import analyze, decode, incorrect_fields

MAX_REQUESTS = 32
MAX_OUTPUT_TOKENS = 450
MAX_COST_USD = 0.02
MODEL = MODELS["qwen"]
SEED = 20261024


def make_requests():
    """Balanced condition order per doc and replicate; identical prompts."""
    original, truth = historical_build()
    if len(original) != 16 or len(truth) != 8:
        raise ValueError("unexpected historical development pack")
    by_pair = {(r["doc"], r["condition"]): r for r in original}
    docs = tuple(truth.keys())
    expected = {(doc, condition) for doc in docs for condition in ("generic", "strict")}
    if set(by_pair) != expected:
        raise ValueError("historical prompt pairs incomplete")
    queue = []
    for repetition in (1, 2):
        for index, doc in enumerate(docs):
            conditions = ("generic", "strict") if (index + repetition) % 2 == 0 else ("strict", "generic")
            for condition in conditions:
                item = by_pair[(doc, condition)]
                queue.append({
                    "id": f"{doc}_{condition}_r{repetition}",
                    "doc": doc, "condition": condition, "repetition": repetition,
                    "messages": [dict(m) for m in item["messages"]],
                    "prompt_sha256": hashlib.sha256(item["messages"][0]["content"].encode("utf8")).hexdigest(),
                })
    if len(queue) != MAX_REQUESTS or len({r["id"] for r in queue}) != MAX_REQUESTS:
        raise ValueError("incorrect call cap / duplicate identifiers")
    for doc in docs:
        for kind in ("generic", "strict"):
            a, b = [r for r in queue if r["doc"] == doc and r["condition"] == kind]
            if a["messages"] != b["messages"] or a["prompt_sha256"] != b["prompt_sha256"]:
                raise ValueError("prompt drift across repeated condition")
    return queue, truth


def summarize(rows, truth):
    queue, _ = make_requests()
    expected = {q["id"] for q in queue}
    if len(rows) != MAX_REQUESTS or {r["id"] for r in rows} != expected:
        raise ValueError("experiment incomplete, duplicates or foreign response ids")
    for r in rows:
        if r.get("repetition") not in (1, 2):
            raise ValueError("invalid repetition id")
    docs = [{"id": d, "events": v} for d, v in truth.items()]
    rounds = {}
    by_repetition = {1: {}, 2: {}}
    for repetition in (1, 2):
        subset = []
        for row in rows:
            if row["repetition"] != repetition:
                continue
            x = dict(row)
            x["id"] = f"{x['doc']}_{x['condition']}"
            subset.append(x)
            by_repetition[repetition][(x["doc"], x["condition"])] = x
        rounds[str(repetition)] = analyze(docs, subset, bootstrap_samples=5000)

    # Across-repetition event-by-event agreement (same doc + condition),
    # computed from fields, not raw formatting or response envelope.
    stability = {}
    paired_doc_deltas = []
    for condition in ("generic", "strict"):
        stable = same_exact_correct = event_comparisons = 0
        differing_examples = []
        for doc, events in truth.items():
            a, b = (by_repetition[rep][(doc, condition)] for rep in (1, 2))
            left, le = decode(a.get("answer"))
            right, re = decode(b.get("answer"))
            if le is not None or re is not None or len(left) != len(events) or len(right) != len(events):
                differing_examples.append({"doc": doc, "reason": "invalid_or_wrong_length"})
                event_comparisons += len(events)
                continue
            for index, truth_event in enumerate(events):
                event_comparisons += 1
                x, y = left[index], right[index]
                if isinstance(x, dict) and isinstance(y, dict):
                    good_a = not incorrect_fields(truth_event, x)
                    good_b = not incorrect_fields(truth_event, y)
                    same_exact_correct += int(good_a and good_b)
                    equal = all(
                        (field in x and field in y and type(x[field]) is type(y[field]) and x[field] == y[field])
                        for field in truth_event
                    )
                    stable += int(equal)
                    if not equal:
                        differing_examples.append({"doc": doc, "event": index, "left": x, "right": y})
                else:
                    differing_examples.append({"doc": doc, "event": index, "reason": "non_object"})
        stability[condition] = {
            "equal_feature_vectors": stable, "events_compared": event_comparisons,
            "correct_in_both_repetitions": same_exact_correct,
            "differing_examples": differing_examples,
        }

    for doc in truth:
        def correct(condition):
            return sum(next(item["correct"] for item in rounds[str(rep)]["details"]
                            if item["document"] == doc and item["condition"] == condition)
                       for rep in (1, 2))
        paired_doc_deltas.append(correct("strict") - correct("generic"))

    totals = {}
    for condition in ("generic", "strict"):
        group = [r for r in rows if r["condition"] == condition]
        usage = {}
        for field in ("prompt_tokens", "completion_tokens", "total_tokens", "cost"):
            if any((r.get("usage") or {}).get(field) is None for r in group):
                usage[field] = None
            else:
                usage[field] = sum(r["usage"][field] for r in group)
        exact = sum(rounds[str(rep)]["exact_events"][condition] for rep in (1, 2))
        totals[condition] = {
            "exact_events": exact, "total_events": 48,
            "event_accuracy": exact / 48,
            "usage": usage,
            "usd_per_correct_event": usage["cost"] / exact if exact and usage["cost"] is not None else None,
            "field_errors": dict(sum((Counter(rounds[str(rep)]["field_errors"][condition]) for rep in (1, 2)), Counter())),
        }

    observed = abs(sum(paired_doc_deltas))
    # Permute condition labels for both repetitions jointly per document.
    import itertools
    signs = itertools.product((-1, 1), repeat=len(truth))
    extremes = sum(abs(sum(a * b for a, b in zip(sign, paired_doc_deltas))) >= observed for sign in signs)
    perm_p = extremes / (1 << len(truth))
    rng = random.Random(SEED)
    boot = sorted(sum(rng.choices(paired_doc_deltas, k=len(truth))) / 48 for _ in range(20000))
    return {
        "schema": "unisermo/schema-prospective-repeatability@1",
        "experimental_status": "repeated_existing_development_templates_not_independent_validation",
        "model_requested": MODEL, "requests": len(rows), "docs": len(truth),
        "repetitions": 2, "scoring_unit": "document",
        "conditions": totals, "rounds": rounds, "stability": stability,
        "paired_doc_strict_minus_generic": paired_doc_deltas,
        "combined_event_difference": sum(paired_doc_deltas),
        "exact_cluster_sign_flip_p_two_sided_exploratory": perm_p,
        "cluster_bootstrap_accuracy_difference_95pct": [boot[500], boot[19500]],
        "call_controls": {"max_requests": MAX_REQUESTS, "max_output_tokens": MAX_OUTPUT_TOKENS,
                          "max_cost_usd": MAX_COST_USD, "seed": 23, "temperature": 0.7,
                          "reasoning_enabled": False, "no_think_suffix": True,
                          "provider_fallbacks": False, "provider_pinned": False},
        "limitations": "Repeated responses to familiar highly templated development clauses, not independent semantic comprehension. Provider selection can vary. Underpowered exploratory inference; do not choose a canonical grammar or schema from this alone.",
    }


def execute(output: Path, secret: str):
    if not secret:
        raise ValueError("OPENROUTER_API_KEY missing")
    if output.exists():
        raise ValueError("refuse to overwrite raw responses")
    requests, truth = make_requests()
    output.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    billed_total = 0.0
    # Save each response immediately; partial results survive a timeout/failure.
    with output.open("x", encoding="utf8") as store:
        for request in requests:
            for attempt in range(3):
                try:
                    response = invoke(secret, MODEL, request, None, max_output=MAX_OUTPUT_TOKENS)
                    break
                except RateLimited:
                    if attempt == 2:
                        raise
                    time.sleep([8, 25][attempt])
            response.update({k: request[k] for k in ("doc", "condition", "repetition", "prompt_sha256")})
            response["call_order"] = len(rows) + 1
            rows.append(response)
            store.write(json.dumps(response, ensure_ascii=False) + "\n")
            store.flush()
            usage = response.get("usage") or {}
            cost = usage.get("cost")
            if not isinstance(cost, (float, int)) or not 0 <= cost <= MAX_COST_USD:
                raise RuntimeError("Missing/invalid individual provider cost: stop before another billable request")
            billed_total += cost
            print(f"completed {len(rows)}/{MAX_REQUESTS}, billed USD {billed_total:.7f}", flush=True)
            if billed_total >= MAX_COST_USD:
                raise RuntimeError("USD request budget reached; stopped")
            time.sleep(1)

    score = summarize(rows, truth)
    score["observed_provider_cost_usd"] = billed_total
    score["corpus_path"] = "benchmarks/corpus/schema-replication-003.jsonl"
    score["corpus_digest_sha256"] = hashlib.sha256(
        (Path(__file__).resolve().parents[1] / score["corpus_path"]).read_bytes()).hexdigest()
    score["response_digest_sha256"] = hashlib.sha256(output.read_bytes()).hexdigest()
    output.with_suffix(".score.json").write_text(json.dumps(score, indent=2, ensure_ascii=False) + "\n",
                                                  encoding="utf8")
    print("completed, raw and score artifacts written", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    execute(args.output, os.environ.get("OPENROUTER_API_KEY", ""))


if __name__ == "__main__":
    main()
