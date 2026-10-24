"""Development-only semantic contrast pilot: normative fragments, not full discourse.

30 canon-attested contrast questions x 2 decoding conditions (cold, compact guide).
This benchmarks semantic choice, not simply morphological slot extraction.
All answer keys are provisional and need independent bilingual review.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path
import random
import time

from benchmarks.openrouter_runner import MODELS, RateLimited, invoke

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "benchmarks/corpus/semantic-contrast-dev-001.jsonl"
MODEL = MODELS["qwen"]
MAX_REQUESTS = 60
MAX_COST_USD = 0.04
MAX_OUTPUT = 130
CONDITIONS = ("cold", "guided")
RUN_SEED = 20261024

# A reference guide in English, derived from *existing* normative documents.
# It is supplied only in the guided arm; no example answer or answer key is shown.
GUIDE = (
    "Reference guide to Unisermo (not an English sentence translation): "
    "Nominal suffixes -em=direct object, -s/-es=possession/of, "
    "-ad=to/toward/recipient, -de=from/source, -in=in/at, "
    "-da=resulting state or role of an explicitly transformed object. "
    "Relators kun=with/together with, per=through/by means of, "
    "pro=for someone's benefit, due=because of, fin=for the purpose of, "
    "tem=during, mod=in the manner of. "
    "Nominal quantity wi=explicit plural, uno=one, bis=two, ter=three, "
    "nul=zero/no quantity, multi=many, omni=all/every member, "
    "tot=whole/entire referent; unmarked nouns do not specify number. "
    "Deixis tik=near speaker, tes=near listener, tan=far from both. "
    "Possession is=my, us=your singular, ins=our, ans=their, "
    "aos=male third-person possessor, aes=female third-person possessor. "
    "The frame traes DEST-ad SOURCE-de explicitly says change from SOURCE to DEST; "
    "ades X says enter state X without naming a source. "
    "The frame Y traes X-em RESULT-da says Y transforms X into RESULT. "
    "Focus -si=also/too; -no=not even; free no=not. "
    "Lexical glosses: dom=house; uman=person; dia=day; "
    "akwa=water; solid=solid; likwid=liquid; doktor=doctor; "
    "student=student; fak=make/do; fakit=thing done/fact; vid=see. "
)


def load_corpus(path=CORPUS):
    data = [json.loads(line) for line in path.read_text(encoding="utf8").splitlines() if line.strip()]
    if len(data) != 30 or len({x["id"] for x in data}) != 30:
        raise ValueError("corpus must contain exactly 30 unique probes")
    if Counter(row["family"] for row in data) != Counter({
        "case":6, "relator":6, "quantity":6, "deixis_possession":6, "transition_focus":6
    }):
        raise ValueError("family quotas changed")
    if Counter(x["expected_choice"] for x in data) != Counter({"A":15,"B":15}):
        raise ValueError("answer label balance changed")
    for row in data:
        if (row["split"] != "development_not_holdout" or row["canonical_changes"] is not False
            or "pending_independent_review" not in row["status"]):
            raise ValueError("missing development-only/semantic-review protection")
        if not row["source_paths"] or row["option_A"] == row["option_B"]:
            raise ValueError("invalid evidence citation or trivial pair")
        if not all(path.startswith(("language/", "research/grammar/")) for path in row["source_paths"]):
            raise ValueError("source outside normative documentation")
        for expression in (row["option_A"], row["option_B"]):
            if not any(expression in (ROOT / path).read_text(encoding="utf8") for path in row["source_paths"]):
                raise ValueError(f"missing canonical attestation: {row['id']} / {expression}")
    return data


def build_questions(rows=None):
    rows = rows if rows is not None else load_corpus()
    questions = []
    for index, row in enumerate(rows):
        # Within each pair alternate request order, avoiding systematic first-arm advantage.
        order = CONDITIONS if index % 2 == 0 else tuple(reversed(CONDITIONS))
        for condition in order:
            preface = (
                "Choose which of the two Unisermo expressions carries the meaning "
                "asked in English. Return ONLY one JSON object: "
                '{"choice":"A"} or {"choice":"B"}. '
                "No prose, reasoning, explanations, or additional fields. "
            )
            text = (
                (GUIDE + "\n" if condition == "guided" else "") +
                preface + "\nExpression A: " + row["option_A"] +
                "\nExpression B: " + row["option_B"] +
                "\nQuestion: " + row["question_en"]
            )
            questions.append({
                "id": row["id"] + "_" + condition,
                "doc": row["id"], "condition": condition,
                "messages": [{"role": "user", "content": text}],
                "prompt_sha256": hashlib.sha256(text.encode("utf8")).hexdigest()
            })
    if len(questions) != MAX_REQUESTS or len({q["id"] for q in questions}) != MAX_REQUESTS:
        raise ValueError("incorrect request count or duplicate")
    return questions


def parse_choice(raw):
    if not isinstance(raw, str):
        return None, "missing_answer"
    raw = raw.strip()
    if raw.startswith("```"):
        lines = raw.splitlines()
        if len(lines) < 3 or lines[0] not in ("```", "```json") or lines[-1] != "```":
            return None, "malformed_fence"
        raw = "\n".join(lines[1:-1])
    try:
        obj = json.loads(raw)
    except ValueError:
        return None, "invalid_json"
    if not isinstance(obj, dict) or set(obj) != {"choice"}:
        return None, "incorrect_schema"
    if obj["choice"] not in ("A", "B"):
        return None, "incorrect_choice_type"
    return obj["choice"], None


def score(rows, corpus=None):
    corpus = corpus if corpus is not None else load_corpus()
    expected = {(item["id"], condition) for item in corpus for condition in CONDITIONS}
    found = {}
    for row in rows:
        key = (row.get("doc"), row.get("condition"))
        if key not in expected or key in found or row.get("id") != key[0] + "_" + key[1]:
            raise ValueError("invalid, foreign or duplicate result")
        found[key] = row
    if len(found) != MAX_REQUESTS:
        raise ValueError("incomplete result; partial paid data must never masquerade as a completed experiment")
    results = {}
    for condition in CONDITIONS:
        right = 0
        by_family = defaultdict(lambda: {"correct":0,"total":0})
        failures = []
        usage = {}
        selected = [found[(case["id"], condition)] for case in corpus]
        for field in ("prompt_tokens","completion_tokens","total_tokens","cost"):
            vals = [(row.get("usage") or {}).get(field) for row in selected]
            usage[field] = sum(vals) if all(isinstance(v, (int,float)) and v>=0 for v in vals) else None
        for item in corpus:
            row = found[(item["id"], condition)]
            answer, error = parse_choice(row.get("answer"))
            correct = answer == item["expected_choice"] and error is None
            right += int(correct)
            group = by_family[item["family"]]
            group["correct"] += int(correct)
            group["total"] += 1
            if not correct:
                failures.append({"id":item["id"],"expected":item["expected_choice"],
                                 "actual":answer,"format_error":error,"family":item["family"]})
        results[condition] = {
            "correct":right,"total":len(corpus),"accuracy":right/len(corpus),
            "by_family":dict(by_family),"failures":failures,
            "usage":usage,"usd_per_correct_choice":usage["cost"]/right if right and usage["cost"] is not None else None,
        }
    wins = Counter()
    details = []
    for item in corpus:
        x = {}
        for condition in CONDITIONS:
            row = found[(item["id"],condition)]
            answer, error = parse_choice(row.get("answer"))
            x[condition] = error is None and answer == item["expected_choice"]
        outcome = ("guided_only" if x["guided"] and not x["cold"] else
                   "cold_only" if x["cold"] and not x["guided"] else
                   "both_correct" if x["cold"] else "neither")
        wins[outcome] += 1
        details.append({"id":item["id"],"family":item["family"],"outcome":outcome})
    return {
        "schema":"unisermo/semantic-contrast-development@1",
        "status":"completed_development_experiment_not_independent_review",
        "requested_model": MODEL,
        "probes":len(corpus),"calls":len(rows),"conditions":results,
        "paired_outcomes":dict(wins),"paired_details":details,
        "guardrails":{"holdout_touched":False,"canonical_changes":False,"human_review":"pending",
                      "max_requests":MAX_REQUESTS,"observed_cost_limit_usd":MAX_COST_USD},
        "limitations":"Canonical expression examples, author-assigned semantic keys, forced-choice English questions, templated pairs, no independently validated translations or dialogue-level anaphora; a high score measures constrained discrimination only."
    }


def run(output, key):
    if not key:
        raise ValueError("OPENROUTER_API_KEY absent")
    if output.exists():
        raise ValueError("refuse overwrite")
    corpus = load_corpus()
    questions = build_questions(corpus)
    rows, spend = [], 0.0
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf8") as handle:
        for q in questions:
            for attempt in range(3):
                try:
                    response = invoke(key, MODEL, q, None, max_output=MAX_OUTPUT)
                    break
                except RateLimited:
                    if attempt == 2: raise
                    time.sleep((8,25)[attempt])
            response.update({field:q[field] for field in ("doc","condition","prompt_sha256")})
            response["call_index"] = len(rows)+1
            rows.append(response)
            handle.write(json.dumps(response, ensure_ascii=False)+"\n")
            handle.flush()
            cost = (response.get("usage") or {}).get("cost")
            if not isinstance(cost,(float,int)) or cost < 0 or cost > MAX_COST_USD:
                raise ValueError("missing/invalid provider cost: stop before any additional paid call")
            spend += cost
            print(f"completed {len(rows)}/{MAX_REQUESTS}, observed USD {spend:.7f}", flush=True)
            if spend >= MAX_COST_USD:
                raise RuntimeError("maximum observed cost reached, no more requests")
            time.sleep(0.8)
    result = score(rows, corpus)
    result["corpus_sha256"] = hashlib.sha256(CORPUS.read_bytes()).hexdigest()
    result["raw_sha256"] = hashlib.sha256(output.read_bytes()).hexdigest()
    result["observed_cost_usd"] = spend
    result["model_controls"] = {"temperature":0.7,"seed":23,"non_thinking":True,
                                "request_max_output":MAX_OUTPUT,"provider_fallbacks":False}
    score_path = output.with_suffix(".score.json")
    if score_path.exists():
        raise ValueError("refuse overwrite score")
    score_path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf8")


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    run(args.output, os.environ.get("OPENROUTER_API_KEY"))
