"""Retrospective paired-schema analysis, treating documents as statistical units.

Read original Actions JSONL; do not infer outcomes from summary reports.
Usage:
 python -m benchmarks.schema_repeatability --corpus benchmarks/corpus/schema-replication-003.jsonl --responses schema-fresh.jsonl
"""
import argparse
import collections
import itertools
import json
import random
from pathlib import Path

FIELDS = ("lemma", "object_lemma", "tense", "aspect", "person", "number", "negative", "interrogative")
ENUMS = {"tense": {"present", "past", "future"}, "aspect": {"simple", "progressive"}, "number": {"singular", "plural"}}


def decode(raw):
    if not isinstance(raw, str):
        return None, "missing_answer"
    s = raw.strip()
    if s.startswith("```"):
        lines = s.splitlines()
        if len(lines) < 3 or lines[0] not in ("```", "```json") or lines[-1] != "```":
            return None, "invalid_fence"
        s = "\n".join(lines[1:-1])
    try:
        data = json.loads(s)
    except ValueError:
        return None, "invalid_json"
    if isinstance(data, dict):
        if set(data) != {"events"}:
            return None, "invalid_wrapper"
        data = data["events"]
    if not isinstance(data, list):
        return None, "not_event_list"
    return data, None


def incorrect_fields(expected, actual):
    errors = {}
    for field in FIELDS:
        want = expected[field]
        got = actual.get(field)
        if field not in actual or type(want) is not type(got) or want != got:
            errors[field] = {"expected": want, "actual": got}
    return errors


def analyze(corpus, responses, bootstrap_samples=20000, seed=20261024):
    docs = {x["id"]: x for x in corpus}
    if len(docs) != len(corpus):
        raise ValueError("duplicate corpus ID")
    indexed = {}
    for r in responses:
        key = (r["doc"], r["condition"])
        if key in indexed or key[0] not in docs or key[1] not in ("generic", "strict"):
            raise ValueError("duplicate or unexpected response")
        if r.get("id") != "_".join(key):
            raise ValueError("response ID mismatch")
        indexed[key] = r
    if len(indexed) != len(docs) * 2:
        raise ValueError("incomplete paired responses")
    event_totals = {c: 0 for c in ("generic", "strict")}
    field_errors = {c: collections.Counter() for c in ("generic", "strict")}
    category_errors = {c: collections.Counter() for c in ("generic", "strict")}
    doc_deltas = []
    details = []
    for docid, doc in docs.items():
        outcomes = {}
        for cond in ("generic", "strict"):
            row = indexed[(docid, cond)]
            events, decode_error = decode(row.get("answer"))
            expected = doc["events"]
            exact = 0
            failures = []
            if events is None or len(events) != len(expected):
                category_errors[cond]["format_or_cardinality"] += 1
            else:
                for idx, (want, got) in enumerate(zip(expected, events)):
                    if not isinstance(got, dict):
                        category_errors[cond]["invalid_event_object"] += 1
                        failures.append({"event": idx, "category": "invalid_event_object"})
                        continue
                    errors = incorrect_fields(want, got)
                    if errors:
                        for field, payload in errors.items():
                            field_errors[cond][field] += 1
                        failures.append({"event": idx, "fields": errors, "category": "feature_error"})
                    else:
                        exact += 1
            event_totals[cond] += exact
            outcomes[cond] = exact
            details.append({"document": docid, "condition": cond, "correct": exact,
                            "total": len(expected), "decode_error": decode_error,
                            "failures": failures, "usage": row.get("usage", {}),
                            "provider": row.get("provider"), "returned_model": row.get("returned_model")})
        doc_deltas.append(outcomes["strict"] - outcomes["generic"])
    n = len(doc_deltas)
    denom = sum(len(d["events"]) for d in docs.values())
    observed = abs(sum(doc_deltas))
    # Exact document-level sign-flip randomization, with all ties kept.
    if n <= 20:
        possible = 1 << n
        extreme = sum(abs(sum(sign * delta for sign, delta in zip(signs, doc_deltas))) >= observed
                      for signs in itertools.product((-1, 1), repeat=n))
        pvalue = extreme / possible
    else:
        pvalue = None
    rng = random.Random(seed)
    boot = sorted(sum(rng.choices(doc_deltas, k=n)) / denom for _ in range(bootstrap_samples))
    lo = boot[int(.025 * bootstrap_samples)]
    hi = boot[min(bootstrap_samples - 1, int(.975 * bootstrap_samples))]
    return {"schema": "unisermo/schema-repeatability@1", "unit_of_inference": "document",
            "documents": n, "events_per_condition": denom, "exact_events": event_totals,
            "difference_strict_minus_generic_events": sum(doc_deltas),
            "document_differences": doc_deltas, "exact_sign_flip_p_two_sided": pvalue,
            "cluster_bootstrap_difference_fraction_95pct": [lo, hi],
            "field_errors": {k: dict(v) for k, v in field_errors.items()},
            "other_errors": {k: dict(v) for k, v in category_errors.items()},
            "details": details,
            "limitations": "Exploratory post-hoc analysis of development data; document clusters are not independent corpus samples. Bootstrap and randomization do not confer holdout status."}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--corpus", required=True, type=Path)
    p.add_argument("--responses", required=True, type=Path)
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    def rows(file):
        return [json.loads(line) for line in file.read_text(encoding="utf8").splitlines() if line.strip()]
    result = analyze(rows(args.corpus), rows(args.responses))
    output = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        if args.output.exists():
            p.error("refusing to overwrite existing analysis")
        args.output.write_text(output, encoding="utf8")
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
