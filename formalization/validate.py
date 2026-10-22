"""Auditable Phase 1 invariants. Stdlib checks always run; jsonschema is optional."""
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path

from .build import read, run
from .core import ROOT, Unisermo
from .ldrs import load_ldrs


def validate() -> None:
    run(check=True)
    grammar = read("research/grammar/confirmed_decisions.json")["decisions"]
    phonology = read("research/phonology/confirmed_decisions.json")["decisions"]
    rules = read("formalization/data/rule_registry.json")["entries"]
    assert len(rules) == len(grammar) + len(phonology)
    source_records = {f"{category}.{d['id']}": d for category, data in
                      (("grammar", grammar), ("phonology", phonology)) for d in data}
    assert len(source_records) == len(rules), "duplicate confirmed IDs"
    for entry in rules:
        src = source_records[entry["id"]]
        assert entry["status"] == "confirmed"
        assert sha256(src["decision"].encode()).hexdigest() == entry["content_sha256"]

    ldrs = load_ldrs()
    assert read("formalization/data/ldr_registry.json")["entries"] == ldrs
    assert any(x["id"] == "LDR-0002" and x["status"] == "Experimental" for x in ldrs)
    for entry in ldrs:
        assert (ROOT / entry["path"]).exists()

    lang = Unisermo()
    assert len(lang.morph["finite"]["aspect"]) == 3
    assert len(lang.morph["finite"]["tense"]) == 3
    assert len(lang.morph["nominal"]["case"]) == 7
    assert lang.generate_verb("dik", "past", "perfect", 1, "singular") == "dikodi"
    assert lang.generate_noun("spets", "genitive") == "spetses"
    assert lang.generate_noun("dom", "accusative") == "domem"
    assert len(lang.lexicon) == len(read("formalization/data/lexicon_index.json")["entries"])
    assert any(a["kind"] == "participle" for a in lang.analyze_word("fakit")["analyses"])
    assert any(a["kind"] == "nominal_case" for a in lang.analyze_word("fakit")["analyses"])
    assert lang.parse_sentence("ka i no diki domem?")["negative"]

    with (ROOT / "formalization/corpus/morphology.jsonl").open(encoding="utf-8") as stream:
        corpus = [json.loads(line) for line in stream]
    assert len(corpus) >= 200
    for entry in corpus:
        matching = lang.analyze_word(entry["surface"])["analyses"]
        match_fields = entry["analysis"]
        assert any(all(a.get(k) == v for k, v in match_fields.items()) for a in matching), (
            entry["surface"], match_fields, matching)

    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        print("Optional jsonschema package missing; external schema validation skipped")
    else:
        for schema_name, payload in (
            ("morphology", read("formalization/data/morphology.json")),
            ("lexicon", read("formalization/data/lexicon_index.json"))):
            schema = read(f"formalization/schema/{schema_name}.schema.json")
            Draft202012Validator.check_schema(schema)
            Draft202012Validator(schema).validate(payload)
        a_schema = read("formalization/schema/analysis.schema.json")
        Draft202012Validator(a_schema).validate(lang.analyze_word("dikodi"))

    assert "seven synthetic cases" in (ROOT / "language/README.md").read_text(encoding="utf-8")
    print(f"VALIDATED: {len(rules)} source decisions, {len(ldrs)} LDRs, "
          f"{len(lang.lexicon)} lexical records, {len(corpus)} morphological examples")
