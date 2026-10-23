"""Opt-in OpenRouter runner for the existing root-recognition trial.

Fail closed on transport/API errors. Never log credentials or prompt bodies.
Each model response receives a single isolated one-message conversation.
"""
from __future__ import annotations
import argparse
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

from benchmarks.root_recognition import build_pack, score

URL = "https://openrouter.ai/api/v1/chat/completions"
MODELS = {"qwen": "qwen/qwen3-32b", "gemma": "google/gemma-3-27b-it"}
MAX_PER_MODEL = 72
MAX_OUTPUT = 48

class RateLimited(RuntimeError):
    """Retryable provider rate limit, without copying upstream response bodies."""

def invoke(key: str, model: str, question: dict, provider: str | None, max_output: int = MAX_OUTPUT) -> dict:
    routing = {"allow_fallbacks": False, "data_collection": "deny"}
    if provider:
        routing["only"] = [provider]
        routing["order"] = [provider]
    payload = {
        "model": model, "messages": question["messages"],
        "stream": False, "temperature": 0, "max_tokens": max_output,
        "provider": routing,
    }
    # Qwen3 defaults to reasoning and can consume MAX_OUTPUT with no visible
    # answer. Request non-thinking mode explicitly for this lexical task.
    if model == MODELS["qwen"]:
        payload["reasoning"] = {"enabled": False}
        payload["temperature"] = 0.7
        payload["seed"] = 23
        # Qwen3 model-card supported inline switch: provider may ignore the
        # nested reasoning flag. Treat this as an explicit prompt variant.
        # Preserve prior turns for persistent-context experiments.
        payload["messages"] = [dict(message) for message in question["messages"]]
        last_user = next((i for i in range(len(payload["messages"])-1, -1, -1)
                          if payload["messages"][i]["role"] == "user"), None)
        if last_user is None:
            raise ValueError("Qwen request requires a user turn")
        payload["messages"][last_user]["content"] += "\n/no_think"
    request = urllib.request.Request(URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json",
                 "HTTP-Referer": "https://github.com/andreabenetton/unisermo",
                 "X-OpenRouter-Title": "Unisermo lexical pilot"},
        method="POST")
    try:
        with urllib.request.urlopen(request, timeout=75) as response:
            result = json.load(response)
    except urllib.error.HTTPError as exc:
        # Do not emit upstream body, which can echo private request data.
        if exc.code == 429:
            raise RateLimited(f"OpenRouter HTTP 429 on question {question['id']}") from None
        raise RuntimeError(f"OpenRouter HTTP {exc.code} on question {question['id']}") from None
    choices = result.get("choices") or []
    if len(choices) != 1:
        raise RuntimeError(f"Unexpected response choices for {question['id']}")
    message = choices[0].get("message") or {}
    answer = message.get("content")
    if not isinstance(answer, str):
        answer = ""
    usage = result.get("usage") or {}
    return {
        "id": question["id"], "answer": answer,
        "response_id": result.get("id"), "returned_model": result.get("model"),
        "provider": result.get("provider"),
        "finish_reason": choices[0].get("finish_reason"),
        "usage": {k: usage.get(k) for k in ("prompt_tokens", "completion_tokens",
                                              "total_tokens", "cost")},
    }


def run(key: str, model: str, provider: str | None, subset: str,
        max_requests: int, output: Path) -> None:
    if not key:
        raise ValueError("OPENROUTER_API_KEY missing")
    if model not in MODELS.values():
        raise ValueError("Only approved model IDs are permitted")
    if max_requests < 1 or max_requests > MAX_PER_MODEL:
        raise ValueError("max_requests outside safe bounds")
    questions, answer_key = build_pack()
    if subset == "probe":
        selected = [q for q in questions if q["split"] == "development"][:2]
    elif subset == "smoke":
        # Only development items, both glossary conditions and all three roots.
        selected = [q for q in questions if q["split"] == "development"][:6]
    elif subset == "development":
        selected = [q for q in questions if q["split"] == "development"]
    else:
        selected = questions
    if len(selected) > max_requests:
        raise ValueError(f"{subset} requires {len(selected)} requests; cap {max_requests}")
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        raise ValueError("refuse to overwrite existing raw result")
    rows = []
    # Persist each completed billed call, even when a later request fails.
    with output.open("x", encoding="utf-8") as record:
        for q in selected:
            for attempt in range(3):
                try:
                    response = invoke(key, model, q, provider)
                    break
                except RateLimited:
                    if attempt == 2:
                        raise
                    time.sleep([5, 15][attempt])
            rows.append(response)
            record.write(json.dumps(response, ensure_ascii=False) + "\n")
            record.flush()
            print(f"{model}: completed {len(rows)}/{len(selected)}", flush=True)
            time.sleep(1.0)
    if subset == "full":
        key_rows = [x for x in answer_key if x["id"] in {r["id"] for r in rows}]
        scored = score(key_rows, rows, model)
        output.with_suffix(".score.json").write_text(
            json.dumps(scored, ensure_ascii=False, sort_keys=True, indent=2) + "\n")
    print(f"Done: {len(rows)} responses. Model={model}; subset={subset}.")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--model", required=True, choices=sorted(MODELS.values()))
    p.add_argument("--provider", default="")
    p.add_argument("--subset", choices=("probe", "smoke", "development", "full"), default="smoke")
    p.add_argument("--max-requests", type=int, default=6)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    run(os.environ.get("OPENROUTER_API_KEY", ""), args.model,
        args.provider.strip() or None, args.subset, args.max_requests, args.output)


if __name__ == "__main__":
    main()
