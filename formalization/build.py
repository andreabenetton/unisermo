"""Generate stable, sourced indexes and a reproducible morphological corpus."""
from __future__ import annotations
from hashlib import sha256
import itertools
import json
from pathlib import Path
from .core import DATA, ROOT
from .ldrs import load_ldrs


def read(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def canonical(obj: object) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def build_indexes() -> dict[str, str]:
    registry = []
    for domain in ("grammar", "phonology"):
        source = f"research/{domain}/confirmed_decisions.json"
        entries = read(source)["decisions"]
        for decision in entries:
            registry.append({"id": f"{domain}.{decision['id']}", "status": "confirmed",
                             "source": f"{source}#decisions/{decision['id']}",
                             "content_sha256": sha256(decision["decision"].encode()).hexdigest()})
    registry.sort(key=lambda d: d["id"])
    core = read("research/lexicon/confirmed_lexicon.json")["entries"]
    roles = read("formalization/data/lexical_roles.json")
    attested = read("formalization/data/attested_forms.json")["entries"]
    entries: dict[str, dict] = {}
    for record in core:
        lemma = record["form"]
        role_list = [k for k, forms in roles.items() if isinstance(forms, list) and lemma in forms]
        if not role_list:
            role_list = [record["category"]]
        entries[lemma] = {"form": lemma, "status": "confirmed_lexicon", "source": "research/lexicon/confirmed_lexicon.json",
                          "categories": sorted(set(role_list + ([record["category"]] if record["category"] in ("compound", "numeral") else []))),
                          "meaning_en": record.get("meaning_en", ""), "meaning_it": record.get("meaning_it", ""),
                          "origin": record.get("source", ""), "decision": record.get("decision", "")}
    for record in attested:
        lemma = record["form"]
        if not (ROOT / record["source"]).is_file():
            raise ValueError(f"attestation document is absent: {record['source']}")
        text = (ROOT / record["source"]).read_text(encoding="utf-8")
        if lemma not in text:
            raise ValueError(f"missing textual attestation of {lemma} in {record['source']}")
        if lemma in entries:
            # Preserve attestation in source registry; current confirmed lexeme wins.
            continue
        entries[lemma] = {"form": lemma, "status": record["status"], "source": record["source"],
                          "categories": [record["category"]]}
    accepted_alphabet = set(read("formalization/data/morphology.json")["alphabet"])
    for lemma, record in entries.items():
        # Lexicon convention writes a productive prefix with a terminal hyphen.
        # The hyphen is a notation boundary, not a phoneme in its surface.
        is_prefix = any(x["form"] == lemma and x["category"] == "derivational_prefix" for x in core)
        phonemes = lemma[:-1] if is_prefix and lemma.endswith("-") else lemma
        if not phonemes or not set(phonemes) <= accepted_alphabet:
            raise ValueError(f"illegal grapheme in {lemma}")
    generated = {"formalization/data/rule_registry.json": canonical({"schema": "unisermo/rule-registry@1", "entries": registry}),
                 "formalization/data/lexicon_index.json": canonical({"schema": "unisermo/lexicon-index@1", "entries": [entries[k] for k in sorted(entries)]}),
                 "formalization/data/ldr_registry.json": canonical({"schema": "unisermo/ldr-registry@1", "entries": load_ldrs()})}
    return generated


def build_corpus() -> str:
    from .core import Unisermo
    language = Unisermo()
    rows = []
    # Structured, deterministic forms; these are NOT a sample of natural prose.
    for lemma in ["dik", "fak", "mov", "es", "vid"]:
        for tense, aspect, person, number in itertools.product(language.morph["finite"]["tense"],
                language.morph["finite"]["aspect"], (1, 2, 3), language.morph["finite"]["number"]):
            rows.append({"surface": language.generate_verb(lemma, tense, aspect, person, number),
                         "analysis": {"kind": "finite_verb", "lemma": lemma, "tense": tense, "aspect": aspect,
                                      "person": person, "number": number},
                         "lexical_status": language.lexicon[lemma]["status"], "source": "generated-from-morphology@1"})
    for lemma in ["dom", "uman", "akwa", "adelo", "spets", "solid"]:
        for case in language.morph["nominal"]["case"]:
            rows.append({"surface": language.generate_noun(lemma, case),
                         "analysis": {"kind": "nominal_case", "lemma": lemma, "case": case},
                         "lexical_status": language.lexicon[lemma]["status"], "source": "generated-from-morphology@1"})
    return "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows)


def run(check: bool = False) -> None:
    indexes = build_indexes()
    for rel, content in indexes.items():
        target = ROOT / rel
        if check:
            if target.read_text(encoding="utf-8") != content:
                raise ValueError(f"generated index out of sync: {rel}")
        else:
            target.write_text(content, encoding="utf-8")
    corpus = build_corpus()
    path = ROOT / "formalization/corpus/morphology.jsonl"
    if check:
        if path.read_text(encoding="utf-8") != corpus:
            raise ValueError("generated corpus out of sync")
    else:
        path.write_text(corpus, encoding="utf-8")
    print(f"formalization {'checked' if check else 'built'}: "
          f"{len(read('formalization/data/rule_registry.json')['entries'])} confirmed decision references, "
          f"{len(read('formalization/data/ldr_registry.json')['entries'])} LDRs, "
          f"{len(read('formalization/data/lexicon_index.json')['entries'])} lexical records, "
          f"{len(corpus.splitlines())} annotated morphology forms")
