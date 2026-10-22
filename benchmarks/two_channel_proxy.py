"""Script-aware orthographic and IPA-edit diagnostics for Unisermo.

These are mechanical similarity PROXIES, never recognition probabilities.
No transliteration or mapping of excluded source phonemes into Unisermo.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEEDS = ROOT / "research/lexicon/modern-form-seeds-v2.json"
IPA = ROOT / "research/lexicon/attested-pronunciation-pilot.json"
MORPH = ROOT / "formalization/data/morphology.json"


def grapheme_script(form: str) -> str:
    """Only compare Latin-script spellings; other scripts need independent transliteration."""
    if not form or not all(
        ("LATIN" in unicodedata.name(char, "") and unicodedata.category(char).startswith("L"))
        or (unicodedata.category(char).startswith("M"))
        for char in unicodedata.normalize("NFD", form)
    ):
        return "not_latin"
    return "latin"


def edit_distance(first: list[str], second: list[str]) -> int:
    previous = list(range(len(second) + 1))
    for i, a in enumerate(first, start=1):
        row = [i]
        for j, b in enumerate(second, start=1):
            row.append(min(row[-1] + 1, previous[j] + 1,
                           previous[j - 1] + (a != b)))
        previous = row
    return previous[-1]


def normalized_edit_similarity(first: list[str], second: list[str]) -> float:
    if not first or not second:
        raise ValueError("empty string is not comparable")
    return round(1.0 - edit_distance(first, second) / max(len(first), len(second)), 5)


def written_proxy(candidate: str, modern_form: str) -> float | None:
    if grapheme_script(modern_form) != "latin":
        return None
    return normalized_edit_similarity(
        list(unicodedata.normalize("NFC", candidate.casefold())),
        list(unicodedata.normalize("NFC", modern_form.casefold())),
    )


def ipa_segments(ipa: str) -> list[str]:
    """Segment IPA conservatively, retaining source-only phonemes/diacritics.

    /t͡ʃ/ is kept as ONE source affricate unit, not transliterated to Unisermo.
    Stress, syllable breaks and length are ignored ONLY for this crude edit proxy.
    """
    if not ipa.startswith("/") or not ipa.endswith("/") or len(ipa) < 3:
        raise ValueError(f"expected one phonemic IPA form enclosed by slashes: {ipa!r}")
    result: list[str] = []
    tie = False
    for ch in ipa[1:-1]:
        if ch in ("ˈ", "ˌ", ".", "ː", " "):
            continue
        if ch in ("͡", "͜"):
            if not result:
                raise ValueError("dangling IPA tie bar")
            result[-1] += ch
            tie = True
        elif unicodedata.combining(ch):
            if not result:
                raise ValueError("dangling IPA diacritic")
            result[-1] += ch
        elif tie:
            result[-1] += ch
            tie = False
        else:
            result.append(ch)
    if tie or not result:
        raise ValueError("incomplete IPA sequence")
    return result


def evaluate(seeds: dict, ipa_evidence: dict, alphabet: str,
             seed_hash: str, evidence_hash: str) -> dict:
    if seeds.get("schema") != "unisermo/modern-form-seeds@1":
        raise ValueError("unknown seed schema")
    if ipa_evidence.get("schema") != "unisermo/attested-ipa-pilot@1":
        raise ValueError("unknown IPA evidence schema")
    rows: dict[tuple[str, str, str], dict] = {}
    for concept in seeds["concepts"]:
        for entry in concept["modern"]:
            key = (concept["id"], entry["language"], entry["form"])
            if key in rows:
                raise ValueError(f"duplicate seed: {key}")
            rows[key] = entry

    evidence: dict[tuple[str, str, str], list[dict]] = {}
    for item in ipa_evidence["attestations"]:
        key = (ipa_evidence["concept"], item["language"], item["form"])
        if key not in rows:
            raise ValueError(f"IPA evidence has no matching seed: {key}")
        if item["review_status"] != "pronunciation_source_checked":
            raise ValueError(f"unverified source pronunciation: {key}")
        if not item["source_url"].startswith("https://kaikki.org/"):
            raise ValueError("IPA needs a documented Kaikki reference")
        ipa_segments(item["source_ipa"])
        evidence.setdefault(key, []).append(item)

    items: list[dict] = []
    for concept in seeds["concepts"]:
        candidates = [concept["canonical"]]
        if concept["id"] == ipa_evidence["concept"]:
            candidates += ipa_evidence["candidate_unisermo_forms"]
        candidates = list(dict.fromkeys(candidates))
        for candidate in candidates:
            if not candidate or not set(candidate) <= set(alphabet) or not candidate.isascii():
                raise ValueError(f"candidate violates Unisermo inventory: {candidate}")
            for entry in concept["modern"]:
                key = (concept["id"], entry["language"], entry["form"])
                transcriptions = []
                for attest in evidence.get(key, []):
                    raw_similarity = normalized_edit_similarity(
                        list(candidate), ipa_segments(attest["source_ipa"])
                    )
                    transcriptions.append({
                        "source_ipa": attest["source_ipa"],
                        "variety": attest["variety"],
                        "source_url": attest["source_url"],
                        "ipa_segment_edit_similarity_proxy": raw_similarity,
                        "perceptual_model": None,
                    })
                items.append({
                    "concept_id": concept["id"],
                    "candidate_unisermo": candidate,
                    "language": entry["language"],
                    "modern_form": entry["form"],
                    "comparison_role": entry["comparison_role"],
                    "semantic_review": entry["modern_sense_review"],
                    "modern_script": grapheme_script(entry["form"]),
                    "written_codepoint_similarity_proxy": written_proxy(candidate, entry["form"]),
                    "transliteration_used": False,
                    "phonetic": transcriptions,
                    "human_written_recognition": None,
                    "human_spoken_recognition": None,
                })

    return {
        "schema": "unisermo/two-channel-similarity-pilot@1",
        "status": "mechanical_proxies_not_human_recognition",
        "source_seed_sha256": seed_hash,
        "source_ipa_sha256": evidence_hash,
        "comparisons": items,
        "summary": {
            "seed_forms": sum(len(c["modern"]) for c in seeds["concepts"]),
            "comparisons": len(items),
            "ipa_attested_variants": sum(len(v) for v in evidence.values()),
            "written_comparable": sum(x["written_codepoint_similarity_proxy"] is not None for x in items),
            "ipa_comparisons": sum(bool(x["phonetic"]) for x in items),
            "independently_semantically_verified": 0,
            "human_recognition_trials": 0,
        },
        "limitations": [
            "Simple codepoint edit similarity only compares Latin script; no inferred transliteration.",
            "IPA segment edit similarity is not a perceptual distance or speaker-recognition measure.",
            "Raw IPA source phonemes remain intact even when not present in Unisermo.",
            "One or two pronunciation varieties do not represent all speakers of a language.",
            "Unreviewed translation candidates and non-equivalent cognates must not be ranked as equivalents.",
            "Do not convert proxy values into an international recognizability score or select roots with them.",
        ],
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--seeds", type=Path, default=SEEDS)
    p.add_argument("--ipa", type=Path, default=IPA)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    source = args.seeds.read_bytes()
    evidence = args.ipa.read_bytes()
    morph = json.loads(MORPH.read_text(encoding="utf-8"))
    result = evaluate(json.loads(source), json.loads(evidence), morph["alphabet"],
                      hashlib.sha256(source).hexdigest(),
                      hashlib.sha256(evidence).hexdigest())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
                           encoding="utf-8")
    print(f"{result['summary']['comparisons']} candidate/form comparisons; "
          f"{result['summary']['ipa_comparisons']} with attested IPA; "
          "zero human recognition claims")


if __name__ == "__main__":
    main()
