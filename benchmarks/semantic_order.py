"""Counterbalanced semantic-choice development experiment (20 x 2 orders x 2 guides).

Not independent meaning validation; every pair is new but some canonical
expressions were used in prior studies. Never reads or modifies holdout.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path
import time

from benchmarks.openrouter_runner import MODELS, RateLimited, invoke
from benchmarks.semantic_contrast import GUIDE, parse_choice

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "benchmarks/corpus/semantic-order-dev-001.jsonl"
PREVIOUS = ROOT / "benchmarks/corpus/semantic-contrast-dev-001.jsonl"
MODEL = MODELS["qwen"]
CONDITIONS = ("cold", "guided")
ORIENTATIONS = ("target_first", "target_second")
MAX_REQUESTS = 80
MAX_OUTPUT = 130
MAX_COST_USD = 0.03


def pair_key(a, b):
    return tuple(sorted((a, b)))


def load_corpus(path=CORPUS, previous=PREVIOUS):
    rows = [json.loads(s) for s in path.read_text(encoding="utf8").splitlines() if s.strip()]
    if len(rows) != 20 or len({r["id"] for r in rows}) != 20:
        raise ValueError("20 unique source-based pairs required")
    if Counter(r["family"] for r in rows) != {
        "case": 4, "relator": 4, "quantity": 4,
        "deixis_possession": 4, "transition_focus": 4
    }:
        raise ValueError("family quota mismatch")
    earlier = [json.loads(s) for s in previous.read_text(encoding="utf8").splitlines() if s.strip()]
    seen = {pair_key(r["option_A"], r["option_B"]) for r in earlier}
    unique = set()
    for row in rows:
        a, b = row["target_expression"], row["distractor_expression"]
        key = pair_key(a, b)
        if key in seen or key in unique or a == b:
            raise ValueError("reused or duplicate unordered expression pair: " + row["id"])
        unique.add(key)
        if (row["split"] != "development_exposed_after_execution"
            or row["canonical_changes"] is not False
            or row["review_status"] != "researcher_authored_key_pending_independent_human_review"):
            raise ValueError("holdout/human-review protection missing")
        for expression in (a, b):
            if not any(expression in (ROOT / p).read_text(encoding="utf8")
                       for p in row["source_paths"]):
                raise ValueError("unattested normative fragment: " + row["id"])
        if not row["question_en"] or not row["source_paths"]:
            raise ValueError("missing question or source")
    return rows


def make_requests(corpus=None):
    rows = corpus if corpus is not None else load_corpus()
    q = []
    for i, item in enumerate(rows):
        # Four-way Latin square order rotates at each successive document.
        arms = [(cond, orient) for cond in CONDITIONS for orient in ORIENTATIONS]
        arms = arms[i % 4:] + arms[:i % 4]
        for condition, orientation in arms:
            a, b = ((item["target_expression"], item["distractor_expression"])
                    if orientation == "target_first"
                    else (item["distractor_expression"], item["target_expression"]))
            expected = "A" if orientation == "target_first" else "B"
            preface = (
                "Choose which of the two Unisermo expressions carries the meaning asked "
                "in English. Return ONLY one JSON object: "
                '{"choice":"A"} or {"choice":"B"}. '
                "No prose, reasoning, explanations or additional fields."
            )
            message = ((GUIDE + "\n" if condition == "guided" else "") +
                       preface + "\nExpression A: " + a +
                       "\nExpression B: " + b +
                       "\nQuestion: " + item["question_en"])
            q.append({
                "id":item["id"] + "_" + condition + "_" + orientation,
                "doc":item["id"],"condition":condition,"orientation":orientation,
                "expected_choice":expected,
                "prompt_sha256":hashlib.sha256(message.encode("utf8")).hexdigest(),
                "messages":[{"role":"user","content":message}]
            })
    if len(q) != MAX_REQUESTS or len({r["id"] for r in q}) != MAX_REQUESTS:
        raise ValueError("incorrect experiment size")
    return q


def score(responses, corpus=None):
    corpus = corpus if corpus is not None else load_corpus()
    questions = make_requests(corpus)
    question_map = {r["id"]: r for r in questions}
    indexed = {}
    for row in responses:
        ident = row.get("id")
        if ident not in question_map or ident in indexed:
            raise ValueError("unexpected or repeated response")
        reference = question_map[ident]
        for field in ("doc","condition","orientation"):
            if row.get(field) != reference[field]:
                raise ValueError("mismatched result metadata")
        if row.get("prompt_sha256") != reference["prompt_sha256"]:
            raise ValueError("prompt digest mismatch")
        indexed[ident] = row
    if len(indexed) != MAX_REQUESTS:
        raise ValueError("incomplete results")
    by_cond = {}
    pair_details = []
    for condition in CONDITIONS:
        total_correct = 0
        formats = Counter()
        families = defaultdict(lambda: {"correct_presentations":0,"total_presentations":0,"both_correct_pairs":0,"total_pairs":0})
        both_correct = both_wrong = stick_a = stick_b = 0
        for item in corpus:
            answers = {}
            for orientation in ORIENTATIONS:
                id_ = item["id"]+"_"+condition+"_"+orientation
                row = indexed[id_]
                label, error = parse_choice(row.get("answer"))
                if error: formats[error] += 1
                expected = "A" if orientation == "target_first" else "B"
                correct = error is None and label == expected
                total_correct += int(correct)
                families[item["family"]]["correct_presentations"] += int(correct)
                families[item["family"]]["total_presentations"] += 1
                answers[orientation] = {"choice":label, "error":error, "correct":correct}
            x, y = answers["target_first"], answers["target_second"]
            families[item["family"]]["total_pairs"] += 1
            if x["correct"] and y["correct"]:
                both_correct += 1
                families[item["family"]]["both_correct_pairs"] += 1
                outcome = "target_both"
            elif (not x["correct"] and not y["correct"] and x["error"] is None
                  and y["error"] is None):
                both_wrong += 1
                outcome = "distractor_both"
            elif x["error"] is None and y["error"] is None and x["choice"] == y["choice"]:
                if x["choice"] == "A":
                    stick_a += 1
                    outcome = "always_A"
                else:
                    stick_b += 1
                    outcome = "always_B"
            else:
                outcome = "format_or_other"
            pair_details.append({"doc": item["id"], "family": item["family"],
                                 "condition": condition, "outcome": outcome,
                                 "target_first": x, "target_second": y})
        used = [indexed[q["id"]] for q in questions if q["condition"] == condition]
        usage = {}
        for key in ("prompt_tokens","completion_tokens","total_tokens","cost"):
            values = [(r.get("usage") or {}).get(key) for r in used]
            usage[key] = (sum(values) if all(type(x) in (int,float) and x >= 0 for x in values)
                          else None)
        by_cond[condition] = {
            "correct_presentations":total_correct,"total_presentations":40,
            "correct_both_orientations":both_correct,"total_contrast_pairs":20,
            "distractor_both_orientations":both_wrong,
            "position_sticking_A":stick_a,"position_sticking_B":stick_b,
            "other_pairs":20-both_correct-both_wrong-stick_a-stick_b,
            "format_errors":dict(formats),"by_family":dict(families),
            "usage":usage,
            "usd_per_correct_presentation":(usage["cost"]/total_correct
                if usage["cost"] is not None and total_correct else None),
            "usd_per_both_correct_pair":(usage["cost"]/both_correct
                if usage["cost"] is not None and both_correct else None)
        }
    transitions = Counter()
    for item in corpus:
        a = next(p["outcome"] for p in pair_details if p["doc"]==item["id"] and p["condition"]=="cold")
        b = next(p["outcome"] for p in pair_details if p["doc"]==item["id"] and p["condition"]=="guided")
        transitions[a+" -> "+b] += 1
    return {
        "schema":"unisermo/semantic-order-counterbalance@1",
        "status":"development_not_holdout_keys_unreviewed",
        "model_requested":MODEL,"documents":20,"requests":MAX_REQUESTS,
        "comparisons":by_cond,
        "joint_outcome_transitions":dict(transitions),
        "pairs":pair_details,
        "limitations":"Original pairs newly combined but vocabulary/examples seen elsewhere; forced-choice English queries, key meanings researcher-assigned; orientation pairing may share stochastic and template effects. Descriptive only; no independent human validation."
    }


def run(output, key):
    if not key:
        raise ValueError("OPENROUTER_API_KEY missing")
    if output.exists() or output.with_suffix(".score.json").exists():
        raise ValueError("refusing overwrite of original evidence")
    corpus = load_corpus()
    questions = make_requests(corpus)
    rows, spend = [], 0.0
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open("x",encoding="utf8") as file:
        for q in questions:
            for attempt in range(3):
                try:
                    response = invoke(key, MODEL, q, None, max_output=MAX_OUTPUT)
                    break
                except RateLimited:
                    if attempt == 2:
                        raise
                    time.sleep((8,25)[attempt])
            response.update({k:q[k] for k in ("doc","condition","orientation","prompt_sha256")})
            response["call_order"] = len(rows)+1
            rows.append(response)
            file.write(json.dumps(response,ensure_ascii=False)+"\n")
            file.flush()
            cost = (response.get("usage") or {}).get("cost")
            if type(cost) not in (float,int) or not 0 <= cost <= MAX_COST_USD:
                raise ValueError("missing/invalid cost; stop additional API requests")
            spend += cost
            print(f"{len(rows)}/{MAX_REQUESTS} responses; observed USD {spend:.7f}",flush=True)
            if spend >= MAX_COST_USD:
                raise RuntimeError("observed cost guard reached; no more requests")
            time.sleep(.6)
    summary=score(rows,corpus)
    summary["observed_cost_usd"]=spend
    summary["corpus_sha256"]=hashlib.sha256(CORPUS.read_bytes()).hexdigest()
    summary["raw_sha256"]=hashlib.sha256(output.read_bytes()).hexdigest()
    summary["controls"]={
        "model":MODEL,"temperature":0.7,"seed":23,"reasoning_disabled":True,
        "no_think_suffix":True,"provider_fallbacks":False,
        "max_output_tokens_per_request":MAX_OUTPUT,"max_requests":MAX_REQUESTS,
        "cumulative_observed_cost_stop_usd":MAX_COST_USD
    }
    output.with_suffix(".score.json").write_text(
        json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
    print("complete original outputs and score saved",flush=True)


if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",required=True,type=Path)
    args=p.parse_args()
    run(args.output,os.environ.get("OPENROUTER_API_KEY"))
