"""Stream Wiktextract JSONL[.gz] and select four traceable Latin anchors.

No inferred cognates, modern speaker recognition or copied dictionary glosses.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEEDS = ROOT / "research/lexicon/modern-form-seeds.json"


def latin_key(word: str) -> str:
    normalized = unicodedata.normalize("NFD", word.casefold())
    return "".join(ch for ch in normalized if not unicodedata.combining(ch))


def extract(source: Path, lemmas: set[str], source_url: str) -> dict:
    if not source_url.startswith("https://kaikki.org/"):
        raise ValueError("source_url must refer to a Kaikki dataset")
    wanted = {latin_key(lemma) for lemma in lemmas}
    selected: list[dict] = []
    found: set[str] = set()
    digest = hashlib.sha256()
    opener = gzip.open if source.name.endswith(".gz") else open
    with opener(source, "rb") as inp:
        for lineno, raw in enumerate(inp, 1):
            digest.update(raw)
            if not raw.strip():
                continue
            entry = json.loads(raw)
            if not isinstance(entry, dict):
                raise ValueError(f"{lineno}: object expected")
            word = entry.get("word", "")
            if entry.get("lang_code") != "la" or latin_key(word) not in wanted:
                continue
            found.add(latin_key(word))
            ipa = [
                item["ipa"] for item in entry.get("sounds", [])
                if isinstance(item, dict) and isinstance(item.get("ipa"), str)
            ]
            selected.append({
                "line": lineno,
                "headword": word,
                "latin_key": latin_key(word),
                "part_of_speech": entry.get("pos"),
                "senses_count": len(entry.get("senses") or []),
                "source_ipa": ipa[:8],
                "provenance": "Wiktextract Latin; not Unisermo IPA",
            })
    missing = sorted(wanted - found)
    return {
        "schema": "unisermo/kaikki-latin-subset@1",
        "status": "incomplete" if missing else "all_requested_headwords_found",
        "source_url": source_url,
        "decompressed_jsonl_sha256": digest.hexdigest(),
        "requested_latin_keys": sorted(wanted),
        "missing_latin_keys": missing,
        "entries": selected,
        "disclaimer": "Latin dictionary attestations cannot prove modern speaker recognition or concept frequency.",
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dump", type=Path, required=True, help="Downloaded JSONL or JSONL.gz")
    ap.add_argument("--source-url", required=True, help="Exact Kaikki download URL")
    ap.add_argument("--seeds", type=Path, default=SEEDS)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--require-all", action="store_true")
    args = ap.parse_args()
    seed = json.loads(args.seeds.read_text(encoding="utf-8"))
    requested = {item["latin"]["headword"] for item in seed["concepts"]}
    output = extract(args.dump, requested, args.source_url)
    if args.require_all and output["missing_latin_keys"]:
        raise SystemExit("Latin subset incomplete: " + ", ".join(output["missing_latin_keys"]))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Extracted {len(output['entries'])} Latin entries; missing {len(output['missing_latin_keys'])}")


if __name__ == "__main__":
    main()
