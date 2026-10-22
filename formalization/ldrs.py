"""Lightweight LDR index reader (stdlib only; scalar frontmatter deliberately limited)."""
from __future__ import annotations
from datetime import date
from hashlib import sha256
from pathlib import Path
import re

from .core import ROOT

LDR_DIR = ROOT / "docs" / "ldr"
STATES = {"Draft", "Proposed", "Experimental", "Accepted", "Rejected", "Superseded"}
REQUIRED = ("id", "title", "status", "date", "domain", "supersedes")


def load_ldrs() -> list[dict]:
    result: list[dict] = []
    seen = set()
    for path in sorted(LDR_DIR.glob("LDR-[0-9][0-9][0-9][0-9]-*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            raise ValueError(f"missing scalar frontmatter: {path}")
        header, body = text[4:].split("\n---\n", 1)
        meta: dict[str, str] = {}
        for line in header.splitlines():
            if not re.fullmatch(r"[a-z_]+: .+", line):
                raise ValueError(f"invalid metadata line in {path}: {line}")
            k, v = line.split(": ", 1)
            if k in meta or k not in REQUIRED:
                raise ValueError(f"duplicate or unrecognized metadata field {k} in {path}")
            meta[k] = v
        if any(not meta.get(k) for k in REQUIRED):
            raise ValueError(f"missing required LDR field: {path}")
        if meta["id"] != path.name[:8] or meta["id"] in seen:
            raise ValueError(f"LDR file/id mismatch or duplicate: {path}")
        if meta["status"] not in STATES:
            raise ValueError(f"unknown LDR status: {path}")
        if date.fromisoformat(meta["date"]).isoformat() != meta["date"]:
            raise ValueError(f"invalid LDR date: {path}")
        if not body.startswith("\n# " + meta["id"] + " "):
            raise ValueError(f"missing matching heading: {path}")
        for section in ("Context and problem", "Alternatives", "Decision or hypothesis", "Evaluation and evidence", "Consequences and compatibility", "Decision authority", "References"):
            if f"## {section}" not in body:
                raise ValueError(f"missing {section} in {path}")
        seen.add(meta["id"])
        result.append({**meta, "path": str(path.relative_to(ROOT)), "sha256": sha256(text.encode("utf-8")).hexdigest()})
    if not result:
        raise ValueError("no LDR records present")
    ids = {item["id"] for item in result}
    for r in result:
        for prior in (i.strip() for i in r["supersedes"].split(",")):
            if prior != "none" and (prior not in ids or prior == r["id"]):
                raise ValueError(f"invalid supersession reference in {r['id']}: {prior}")
    return result
