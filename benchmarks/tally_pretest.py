"""Create a DRAFT Tally form for Unisermo spontaneous comprehension.

Usage:
  python -m benchmarks.tally_pretest --dry-run > /tmp/unisermo-form.json
  export TALLY_API_KEY='...'  # locally, never commit or paste this token in chats
  python -m benchmarks.tally_pretest --create-draft

Only --create-draft performs an authenticated POST. No submissions are created.
Tally API reference: https://developers.tally.so/api-reference/endpoint/forms/post
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
from pathlib import Path
import urllib.error
import urllib.request
import uuid

API = "https://api.tally.so/forms"
VERSION = "2025-02-01"
HERE = Path(__file__).resolve().parent
SPEC = HERE / "corpus" / "tally-spontaneous-pretest-v1.json"


def block(block_type, group_type, payload, group=None):
    unique = str(uuid.uuid4())
    return {"uuid": unique, "groupUuid": group or unique,
            "groupType": group_type, "type": block_type, "payload": payload}


def plain(content):
    return f"<p>{html.escape(content)}</p>"


def build(spec):
    assert spec["schema"] == "unisermo/tally-spontaneous-pretest@1"
    assert len(spec["items"]) == 6
    blocks = [block("FORM_TITLE", "FORM_TITLE",
                    {"title": spec["title"], "html": plain(spec["title"])})]
    blocks.append(block("TEXT", "TEXT", {"html": plain(spec["instructions"])}))
    for item in spec["items"]:
        # Separate stable field key is retained in both question label and
        # payload name; the question wording contains no English translation.
        uid = str(uuid.uuid4())
        blocks.append(block("TITLE", "QUESTION", {
            "html": plain(f"{item['id']} — {item['sentence']}")
        }, group=uid))
        blocks.append(block("TEXTAREA", "TEXTAREA", {
            "name": f"meaning_{item['id']}",
            "isRequired": False,
            "placeholder": "Che cosa pensi che significhi?"
        }, group=uid))
        conf = str(uuid.uuid4())
        blocks.append(block("LABEL", "LABEL", {
            "html": plain("Quanto sei sicuro della tua interpretazione? (1 = molto poco; 5 = molto)")
        }, group=conf))
        blocks.append(block("LINEAR_SCALE", "LINEAR_SCALE", {
            "name": f"confidence_{item['id']}",
            "isRequired": False,
            "start": 1,"end": 5,"step": 1,
            "hasLeftLabel": True,"leftLabel": "Poco",
            "hasRightLabel": True,"rightLabel": "Molto"
        }, group=conf))
    return {
        "status": "DRAFT",
        "blocks": blocks,
        "settings": {"language": "it", "hasProgressBar": True}
    }


def main():
    p = argparse.ArgumentParser()
    options = p.add_mutually_exclusive_group(required=True)
    options.add_argument("--dry-run", action="store_true")
    options.add_argument("--create-draft", action="store_true")
    args = p.parse_args()
    source = SPEC.read_bytes()
    payload = build(json.loads(source))
    if args.dry_run:
        print(json.dumps({"spec_sha256": hashlib.sha256(source).hexdigest(),
                          "form": payload}, ensure_ascii=False, indent=2))
        return
    key = os.environ.get("TALLY_API_KEY")
    if not key:
        raise SystemExit("Set TALLY_API_KEY in your own shell; never paste it in chat.")
    request = urllib.request.Request(
        API, method="POST", data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": "Bearer " + key,
                 "Content-Type": "application/json",
                 "tally-version": VERSION})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.load(response)
    except urllib.error.HTTPError as exc:
        # Never echo upstream response which might contain private data.
        raise SystemExit(f"Tally returned HTTP {exc.code}; form not confirmed.") from None
    print(json.dumps({"created": True, "status_requested": "DRAFT",
                      "form_id": result.get("id"),
                      "spec_sha256": hashlib.sha256(source).hexdigest()},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
