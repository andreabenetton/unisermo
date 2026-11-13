"""UCUB-001 offline prompts, opt-in hosted run, and strict ternary scoring.

No model calls occur without the explicit 'run' subcommand, API key, model,
max-call budget and --allow-unreviewed. No stored or printed credentials.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CORPUS = ROOT / "corpus.jsonl"
MANIFEST = ROOT / "manifest.json"
ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"
LABELS = {"entailed", "contradicted", "undetermined"}

# Only known, currently ratified words in this draft benchmark.
DICTIONARY = (
    "Unisermo dictionary: i=I; u=you (singular); a=third-person singular; "
    "uman=person; akwa=water; aerplan=airplane; vid=see; pel=push; "
    "trak=pull; mov=move; vol=desire/want; int=intend/commit to an action; "
    "tent=attempt; deb=obligated (personal)/necessary (impersonal); "
    "pos=possible; kred=believe; sap=know; lik=probability/likelihood; "
    "no=not; e=and; o=inclusive or; sirka=approximately; "
    "major=greater than; minor=less than; setdek=70; sesdek=60; "
    "sen=100; bissen=200; senim=one-hundredth (fraction denominator)."
)
GRAMMAR = (
    "Unisermo grammar: finite lexical verbs are root + optional aspect "
    "+ optional tense (d past, f future, empty present) + person vowel "
    "(i first, u second, a third); the object case suffix is -em. "
    "A finite personal servile takes a bare verb: 'i voli mov' means "
    "'I want to move', not 'I move'. The no immediately before a finite "
    "head negates that head; 'no deb P' means P is not necessary, "
    "whereas 'deb no P' means it is necessary that not-P. Bare heads "
    "'deb P' and 'pos P' are impersonal proposition operators; "
    "'i kred u movu' means I believe that you move, not necessarily that "
    "you actually move. 'tent' denotes attempt, not success. "
    "Conjunction e asserts both clauses; o is inclusive OR, not XOR. "
    "'lik NUMBER senim P' assigns a stated fractional probability; "
    "'no lik NUMBER senim P' denies that precise assignment, not P. "
    "'lik sirka NUMBER senim P' makes the number approximate; "
    "'lik major NUMBER senim P' is strictly greater; "
    "'lik no minor NUMBER senim P' means at least that value. "
    "'lik inter X senim e Y senim P' is a numeric interval whose "
    "endpoint inclusion can be contextual. Do not reject 200 percent "
    "claims as ungrammatical: speakers may use hyperbole. "
    "Bare statements of possibility, desire, intent, necessity or "
    "probability do not assert actual action in the real world. "
    "When the premises do not determine a hypothesis, answer undetermined."
)
INSTRUCTION = (
    "Classify the relation between the passage and the hypothesis. "
    "Use only what is logically stated; don't infer unmentioned actions "
    "from desires, attempts, probabilities or world knowledge. "
    "Return ONLY one JSON object with a single 'label' field, whose value "
    "is exactly 'entailed', 'contradicted', or 'undetermined'."
)


def load_corpus() -> tuple[list[dict], dict]:
    raw = CORPUS.read_bytes()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if hashlib.sha256(raw).hexdigest() != manifest["corpus_sha256"]:
        raise ValueError("UCUB-001 corpus does not match frozen manifest digest")
    rows = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line]
    if len(rows) != 80 or len({r["id"] for r in rows}) != 80:
        raise ValueError("invalid UCUB-001 corpus IDs/size")
    if sum(r["split"] == "development" for r in rows) != 64:
        raise ValueError("invalid development split")
    if sum(r["split"] == "holdout" for r in rows) != 16:
        raise ValueError("invalid holdout split")
    by_group = {}
    for row in rows:
        if row["gold"] not in LABELS:
            raise ValueError("invalid gold label")
        by_group.setdefault(row["group"], []).append(row)
    if len(by_group) != 20 or any(len(g) != 4 or len({r["split"] for r in g}) != 1 for g in by_group.values()):
        raise ValueError("contrast family leakage")
    return rows, manifest


def prompt(row: dict, condition: str) -> dict:
    if condition not in ("cold", "lexicon", "grammar", "english"):
        raise ValueError("unknown experiment condition")
    preface = ""
    if condition in ("lexicon", "grammar"):
        preface = DICTIONARY + "\n"
    if condition == "grammar":
        preface += GRAMMAR + "\n"
    language = "English" if condition == "english" else "Unisermo"
    passage = row["english"] if condition == "english" else row["unisermo"]
    return {
        "id": row["id"], "group": row["group"], "level": row["level"],
        "split": row["split"], "condition": condition,
        "messages": [{"role": "user", "content": INSTRUCTION + "\n" + preface +
                      "Passage language: " + language +
                      "\nPassage:\n" + passage +
                      "\nHypothesis (English): " + row["hypothesis"]}],
    }


def select(rows: list[dict], split: str, limit: int | None) -> list[dict]:
    if split not in ("development", "holdout"):
        raise ValueError("explicit split selection required")
    selected = [r for r in rows if r["split"] == split]
    if limit is not None:
        if limit <= 0 or limit > len(selected):
            raise ValueError("invalid request limit")
        selected = selected[:limit]
    return selected


def parse_label(text: str) -> str | None:
    if not isinstance(text, str):
        return None
    try:
        data = json.loads(text)
    except (ValueError, TypeError):
        return None
    if (not isinstance(data, dict) or set(data) != {"label"}
            or not isinstance(data["label"], str)
            or data["label"] not in LABELS):
        return None
    return data["label"]


def score(responses: list[dict], rows: list[dict], *, allow_partial: bool = False) -> dict:
    keys = {r["id"]: r for r in rows}
    if len({r["id"] for r in responses}) != len(responses):
        raise ValueError("duplicate response IDs")
    if not responses:
        raise ValueError("no model responses")
    if any(x["id"] not in keys for x in responses):
        raise ValueError("response ID not in selected corpus split")
    if not allow_partial and set(x["id"] for x in responses) != set(keys):
        raise ValueError("response file must match all cases in selected split")
    conditions = {x.get("condition") for x in responses}
    if len(conditions) != 1 or next(iter(conditions)) not in ("cold", "lexicon", "grammar", "english"):
        raise ValueError("responses must have one valid condition")
    results = []
    for response in responses:
        case = keys[response["id"]]
        predicted = parse_label(response.get("answer", ""))
        expected = case["gold"]
        results.append({"id": case["id"], "level": case["level"],
                        "group": case["group"], "expected": expected,
                        "prediction": predicted,
                        "correct": predicted == expected,
                        "valid": predicted is not None,
                        "usage": response.get("usage") or {}})
    count = len(results)
    breakdown = {}
    for level in ("L1", "L2", "L3", "L4"):
        subset = [x for x in results if x["level"] == level]
        if subset:
            breakdown[level] = {"count": len(subset),
                                "correct": sum(x["correct"] for x in subset),
                                "accuracy": sum(x["correct"] for x in subset) / len(subset)}
    confusion = {}
    for gold in sorted(LABELS):
        confusion[gold] = dict(Counter(str(r["prediction"]) for r in results if r["expected"] == gold))
    usage = {}
    for key in ("prompt_tokens", "completion_tokens", "total_tokens", "cost"):
        vals = [x["usage"].get(key) for x in results]
        usage[key] = sum(v for v in vals if isinstance(v, (int, float)) and not isinstance(v, bool)) if any(isinstance(v, (int, float)) for v in vals) else None
    return {"schema": "unisermo/ucub001-score@1",
            "status": "exploratory_unreviewed_semantics",
            "condition": next(iter(conditions)), "count": count,
            "correct": sum(x["correct"] for x in results),
            "accuracy": sum(x["correct"] for x in results) / count,
            "invalid_outputs": sum(not x["valid"] for x in results),
            "by_level": breakdown, "confusion": confusion,
            "usage_totals": usage,
            "items": [{k: r[k] for k in ("id", "correct", "valid", "prediction")} for r in results]}


def invoke(key: str, model: str, question: dict, provider: str | None) -> dict:
    """An opt-in network call; credentials never enter recorded results."""
    payload = {
        "model": model,
        "messages": question["messages"],
        "temperature": 0,
        "max_tokens": 80,
        "stream": False,
        "provider": {"allow_fallbacks": False, "data_collection": "deny"},
    }
    if provider:
        payload["provider"]["only"] = [provider]
        payload["provider"]["order"] = [provider]
    if model.startswith("qwen/qwen3-"):
        # Qwen3 may spend the entire response budget on thinking.
        payload["reasoning"] = {"enabled": False}
        payload["messages"] = [dict(m) for m in question["messages"]]
        payload["messages"][-1]["content"] += "\n/no_think"
        payload["temperature"] = 0.7
        payload["seed"] = 23
    req = urllib.request.Request(
        ENDPOINT, method="POST",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json",
                 "Authorization": "Bearer " + key,
                 "HTTP-Referer": "https://github.com/andreabenetton/unisermo",
                 "X-OpenRouter-Title": "Unisermo UCUB-001"},
    )
    try:
        with urllib.request.urlopen(req, timeout=75) as res:
            result = json.load(res)
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"provider HTTP {exc.code} for {question['id']}") from None
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError(f"provider transport error for {question['id']}") from None
    choices = result.get("choices") or []
    if len(choices) != 1:
        raise RuntimeError("missing/ambiguous provider response")
    m = choices[0].get("message") or {}
    usage = result.get("usage") or {}
    return {
        "id": question["id"], "condition": question["condition"],
        "answer": m.get("content") if isinstance(m.get("content"), str) else "",
        "response_id": result.get("id"), "model_requested": model,
        "model_returned": result.get("model"),
        "provider": result.get("provider"),
        "finish_reason": choices[0].get("finish_reason"),
        "usage": {k: usage.get(k) for k in ("prompt_tokens","completion_tokens","total_tokens","cost")},
    }


def write_new(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as handle:
        handle.write(content)


def main() -> None:
    p = argparse.ArgumentParser(description="UCUB-001 controlled semantic comprehension")
    sub = p.add_subparsers(dest="operation", required=True)
    for name in ("prepare", "run"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--condition", required=True, choices=("cold","lexicon","grammar","english"))
        cmd.add_argument("--split", required=True, choices=("development","holdout"))
        cmd.add_argument("--limit", type=int)
        cmd.add_argument("--allow-unreviewed", action="store_true")
        cmd.add_argument("--unlock-holdout", action="store_true")
        cmd.add_argument("--output", type=Path, required=True)
        if name == "run":
            cmd.add_argument("--model", required=True)
            cmd.add_argument("--provider")
            cmd.add_argument("--max-calls", type=int, required=True)
    score_cmd = sub.add_parser("score")
    score_cmd.add_argument("--responses", type=Path, required=True)
    score_cmd.add_argument("--split", choices=("development","holdout"), default="development")
    score_cmd.add_argument("--allow-partial", action="store_true")
    score_cmd.add_argument("--allow-unreviewed", action="store_true")
    score_cmd.add_argument("--unlock-holdout", action="store_true")
    score_cmd.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    if not args.allow_unreviewed:
        p.error("UCUB semantic gold and English drafts have no independent human review; use --allow-unreviewed explicitly")
    rows, manifest = load_corpus()
    if args.split == "holdout" and not args.unlock_holdout:
        p.error("holdout is sealed until review and choices are frozen; requires --unlock-holdout explicitly")
    if args.operation == "score":
        responses = [json.loads(line) for line in args.responses.read_text(encoding="utf-8").splitlines() if line]
        report = score(responses, select(rows, args.split, None), allow_partial=args.allow_partial)
        report.update({"corpus_sha256": manifest["corpus_sha256"], "split": args.split})
        write_new(args.output, json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n")
        print("scored unreviewed cases:", report["count"], "accuracy:", report["accuracy"])
        return
    chosen = select(rows, args.split, args.limit)
    questions = [prompt(r, args.condition) for r in chosen]
    if args.operation == "prepare":
        write_new(args.output, "".join(json.dumps(q, ensure_ascii=False, sort_keys=True) + "\n" for q in questions))
        print("prepared", len(questions), "offline prompts; status: unreviewed")
        return
    if not re.fullmatch(r"[a-zA-Z0-9_.:-]+/[a-zA-Z0-9_.:-]+", args.model):
        p.error("provide an explicit OpenRouter vendor/model id")
    if not 1 <= args.max_calls <= 320 or args.max_calls < len(questions):
        p.error("max-calls must explicitly cover selected requests and be <=320")
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        p.error("OPENROUTER_API_KEY missing")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as handle:
        for question in questions:
            # Capture each billable result immediately: never claim a completed
            # full experiment after a failed call. No automatic retry billing.
            response = invoke(key, args.model, question, args.provider)
            response["split"] = args.split
            response["corpus_sha256"] = manifest["corpus_sha256"]
            response["timestamp_unix"] = int(time.time())
            handle.write(json.dumps(response, ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()
    print("finished", len(questions), "calls; raw results are unreviewed")


if __name__ == "__main__":
    main()
