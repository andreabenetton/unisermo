"""Paired, development-only morphological-case vs semantic-role labeling.

Both arms read the same 24 complete finite clauses, the same short grammar
guide, and return the same JSON shape. Only the requested 'tag' vocabulary
differs. No original evidence, holdout, or accepted language rules are edited.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import time

from benchmarks.openrouter_runner import MODELS, RateLimited, invoke
from formalization.core import Unisermo
from formalization.semantics.relational_frames import parse_relational_frame

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "benchmarks/corpus/case-role-dev-001.jsonl"
PREVIOUS = ROOT / "benchmarks/corpus/relational-frames-dev-001.jsonl"
MODEL = MODELS["qwen"]
CONDITIONS = ("case", "role")
CALL_CAP = 24
OUTPUT_CAP = 340
OBSERVED_USD_LIMIT = 0.02

# Case and role projections are both derived from the licensed parsed frame.
CASE = {
    "patient": "accusative",
    "destination": "dative_allative",
    "destination_state": "dative_allative",
    "source_state": "ablative",
    "result_state": "resultative",
}
ROLE = {
    "patient": "patient",
    "destination": "destination",
    "destination_state": "destination",
    "source_state": "source",
    "result_state": "result",
}
GUIDE = (
    "Unisermo source-defined grammar reference (provided identically in both arms): "
    "finite roots mov=move and traes=transition or cause transformation, "
    "with regular aspect/time/person inflection. "
    "A noun ending -em is accusative/patient; -ad marks an allative destination; "
    "-de marks source/ablative; -da marks a resulting state of a transformed object. "
    "Licensed valency patterns: SUBJECT mov PATIENT-em DESTINATION-ad; "
    "SUBJECT traes DESTINATION-ad SOURCE-de (non-causative two-state transition); "
    "SUBJECT traes PATIENT-em RESULT-da (causative transformation). "
    "A state arrived at via -ad is a destination; a resulting predicate in "
    "the causative construction marked -da is a result. "
    "The surface stem names are preserved (dom, uman, akwa, aerplan, "
    "solid, likwid, doktor, student). No anaphora between independent clauses."
)


def gold(sentence, lang, condition):
    parsed = parse_relational_frame(sentence, lang)
    verb = parsed["predicate"]["lemma"]
    if verb not in ("mov", "traes"):
        raise ValueError("unsupported verb in this controlled pilot")
    mapping = CASE if condition == "case" else ROLE
    names = list(parsed["roles"])
    if len(names) != 2:
        raise ValueError("expected two licensed postverbal arguments")
    if any(parsed["roles"][name]["modifiers"] for name in names):
        raise ValueError("modifiers outside benchmark scope")
    return {
        "verb": verb,
        "args": [{"stem": parsed["roles"][name]["lemma"], "tag": mapping[name]}
                 for name in names]
    }


def load_corpus(path=CORPUS):
    corpus = [json.loads(line) for line in path.read_text(encoding="utf8").splitlines() if line.strip()]
    if len(corpus) != 12 or len({r["id"] for r in corpus}) != 12:
        raise ValueError("expected exactly 12 distinct documents")
    if Counter(row["family"] for row in corpus) != Counter(
            {"move": 4, "transition": 4, "cause_result": 4}):
        raise ValueError("unbalanced families")
    previous = [json.loads(line) for line in PREVIOUS.read_text(encoding="utf8").splitlines() if line.strip()]
    known = set(sentence for row in previous for sentence in row["clauses"])
    sentences = [x for row in corpus for x in row["clauses"]]
    if len(sentences) != 24 or len(set(sentences)) != 24 or set(sentences) & known:
        raise ValueError("incomplete or reused complete clauses")
    lang = Unisermo()
    for row in corpus:
        if (row["split"] != "development_only" or row["canonical_changes"] is not False or
            "pending_independent_human_review" not in row["review_status"] or
            row["relation_annotation"] != "case_and_role_projection_not_human_ground_truth"):
            raise ValueError("invalid corpus research protections")
        if not all((ROOT / path).exists() for path in row["source_paths"]):
            raise ValueError("missing normative source")
        for sentence in row["clauses"]:
            parsed = parse_relational_frame(sentence, lang)
            if parsed["frame"] != {
                "move": "move_transitive_to",
                "transition": "transition_between_states",
                "cause_result": "cause_result"}[row["family"]]:
                raise ValueError("incompatible licensed frame")
            for cond in CONDITIONS:
                assert len(gold(sentence, lang, cond)["args"]) == 2
    return corpus


def requests(corpus=None):
    rows = corpus if corpus is not None else load_corpus()
    result = []
    for index, row in enumerate(rows):
        order = CONDITIONS if index % 2 == 0 else CONDITIONS[::-1]
        for cond in order:
            tags = ("accusative, dative_allative, ablative, resultative"
                    if cond == "case" else "patient, destination, source, result")
            prompt = (
                GUIDE + "\n" +
                "For each of the two independent Unisermo clauses below, extract the finite "
                "verb's root and the TWO post-verbal nominal argument stems IN THEIR ORIGINAL ORDER. "
                "Return exactly one JSON object with events (array of two objects), "
                "each object exactly {\"verb\":string,\"args\":[{\"stem\":string,\"tag\":string},"
                "{\"stem\":string,\"tag\":string}]}. "
                "For each argument, tag the " +
                ("MORPHOLOGICAL CASE of its head suffix" if cond == "case"
                 else "SEMANTIC ROLE licensed by the whole verb-and-case construction") +
                ". Valid tag values ONLY: " + tags +
                ". Do not invent additional fields, tags, entities or explanations. "
                "Exactly two args per event, and events in sentence order.\nUnisermo:\n" +
                "\n".join(row["clauses"])
            )
            result.append({
                "id": row["id"] + "_" + cond, "doc": row["id"], "condition": cond,
                "prompt_sha256": hashlib.sha256(prompt.encode("utf8")).hexdigest(),
                "messages": [{"role": "user", "content": prompt}]
            })
    if len(result) != CALL_CAP or len({r["id"] for r in result}) != CALL_CAP:
        raise ValueError("unexpected request count")
    return result


def decode(raw):
    if not isinstance(raw, str):
        return None, "missing"
    raw = raw.strip()
    if raw.startswith("```"):
        lines = raw.splitlines()
        if len(lines) < 3 or lines[0] not in ("```", "```json") or lines[-1] != "```":
            return None, "invalid_fence"
        raw = "\n".join(lines[1:-1])
    try:
        obj = json.loads(raw)
    except ValueError:
        return None, "invalid_json"
    if not isinstance(obj, dict) or set(obj) != {"events"} or not isinstance(obj["events"], list):
        return None, "invalid_envelope"
    if len(obj["events"]) != 2:
        return None, "wrong_cardinality"
    return obj["events"], None


def evaluate(outputs, corpus=None):
    corpus = corpus if corpus is not None else load_corpus()
    planned = {q["id"]: q for q in requests(corpus)}
    found = {}
    for row in outputs:
        ident = row.get("id")
        if ident not in planned or ident in found:
            raise ValueError("foreign or duplicate response")
        if any(row.get(k) != planned[ident][k] for k in ("doc", "condition", "prompt_sha256")):
            raise ValueError("request identity mismatch")
        found[ident] = row
    if len(found) != CALL_CAP:
        raise ValueError("missing responses; partial paid experiments are not scored")
    lang = Unisermo()
    stats = {}
    by_doc = {}
    for cond in CONDITIONS:
        exact_clauses = 0
        exact_args = 0
        exact_stems = 0
        exact_tags = 0
        format_errors = Counter()
        wrong_tags = Counter()
        details = []
        for row in corpus:
            response = found[row["id"] + "_" + cond]
            events, error = decode(response.get("answer"))
            if error:
                format_errors[error] += 1
            for index, clause in enumerate(row["clauses"]):
                expected = gold(clause, lang, cond)
                received = (events[index] if error is None and isinstance(events[index], dict) else {})
                args = received.get("args")
                valid = (
                    isinstance(received, dict) and set(received) == {"verb", "args"} and
                    type(received.get("verb")) is str and
                    isinstance(args, list) and len(args) == 2 and
                    all(isinstance(a, dict) and set(a) == {"stem", "tag"} and
                        type(a["stem"]) is str and type(a["tag"]) is str for a in args)
                )
                clause_ok = valid and received["verb"] == expected["verb"]
                for j, want in enumerate(expected["args"]):
                    got = args[j] if valid else {}
                    stem_ok = got.get("stem") == want["stem"]
                    tag_ok = got.get("tag") == want["tag"]
                    exact_stems += int(stem_ok)
                    exact_tags += int(tag_ok)
                    exact_args += int(stem_ok and tag_ok)
                    clause_ok = clause_ok and stem_ok and tag_ok
                    if not tag_ok:
                        wrong_tags[f"{want['tag']} -> {got.get('tag', '<missing>')}"] += 1
                exact_clauses += int(clause_ok)
                details.append({
                    "doc": row["id"], "family": row["family"], "event": index,
                    "exact": bool(clause_ok), "valid_event_shape": bool(valid),
                    "expected": expected,
                    "received": received,
                })
        used = [found[q["id"]] for q in planned.values() if q["condition"] == cond]
        usage = {}
        for k in ("prompt_tokens", "completion_tokens", "total_tokens", "cost"):
            values = [(r.get("usage") or {}).get(k) for r in used]
            usage[k] = sum(values) if all(type(v) in (int, float) and v >= 0 for v in values) else None
        stats[cond] = {
            "exact_clauses": exact_clauses, "total_clauses": 24,
            "exact_arguments": exact_args, "total_arguments": 48,
            "exact_stems": exact_stems, "exact_tags": exact_tags,
            "format_errors": dict(format_errors),
            "tag_confusions": dict(wrong_tags),
            "usage": usage,
            "cost_per_exact_clause": usage["cost"] / exact_clauses
                if usage["cost"] is not None and exact_clauses else None,
            "details": details,
        }
        by_doc[cond] = {d["id"]: sum(int(x["exact"]) for x in details
                                   if x["doc"] == d["id"]) for d in corpus}
    paired = [{"doc": d["id"], "family": d["family"],
               "case": by_doc["case"][d["id"]], "role": by_doc["role"][d["id"]]}
              for d in corpus]
    return {
        "schema": "unisermo/case-role-decoding-dev@1",
        "status": "development_automated_gold_not_independent_semantic_validation",
        "requested_model": MODEL, "calls": len(outputs), "documents": len(corpus),
        "comparisons": stats, "document_pairing": paired,
        "limitations": "Different outputs evaluate different target labels; no semantic equivalence or English baseline. The grammar primer teaches the relevant rule. Same lexical material and templated families are not a genuine held-out sample."
    }


def run(path, key):
    if not key:
        raise ValueError("OPENROUTER_API_KEY missing")
    if path.exists() or path.with_suffix(".score.json").exists():
        raise ValueError("refuse overwrite")
    corpus = load_corpus()
    plan = requests(corpus)
    rows, spent = [], 0.0
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf8") as output:
        for q in plan:
            for attempt in range(3):
                try:
                    response = invoke(key, MODEL, q, None, max_output=OUTPUT_CAP)
                    break
                except RateLimited:
                    if attempt == 2:
                        raise
                    time.sleep([8, 25][attempt])
            response.update({k: q[k] for k in ("doc", "condition", "prompt_sha256")})
            response["call_order"] = len(rows) + 1
            rows.append(response)
            output.write(json.dumps(response, ensure_ascii=False) + "\n")
            output.flush()
            cost = (response.get("usage") or {}).get("cost")
            if type(cost) not in (int, float) or not 0 <= cost <= OBSERVED_USD_LIMIT:
                raise RuntimeError("invalid/missing provider reported cost")
            spent += cost
            print(f"{len(rows)}/{CALL_CAP} calls, observed USD {spent:.8f}", flush=True)
            if spent >= OBSERVED_USD_LIMIT:
                raise RuntimeError("observed spending limit reached")
            time.sleep(0.6)
    scored = evaluate(rows, corpus)
    scored["raw_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    scored["corpus_sha256"] = hashlib.sha256(CORPUS.read_bytes()).hexdigest()
    scored["observed_cost_usd"] = spent
    scored["controls"] = {
        "temperature": 0.7, "seed": 23, "no_think": True,
        "provider_fallbacks": False, "max_output": OUTPUT_CAP,
        "call_cap": CALL_CAP, "observed_cost_guard_usd": OBSERVED_USD_LIMIT
    }
    path.with_suffix(".score.json").write_text(
        json.dumps(scored, indent=2, ensure_ascii=False) + "\n", encoding="utf8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    run(args.output, os.environ.get("OPENROUTER_API_KEY"))
