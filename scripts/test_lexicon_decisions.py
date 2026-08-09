#!/usr/bin/env python3
"""Regression checks for confirmed GlottoDelta lexical decisions."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEXICON = ROOT / "research" / "lexicon" / "confirmed_lexicon.json"
AUDIT = ROOT / "research" / "lexicon" / "legacy_c_root_audit.md"
ROOT_SEED = ROOT / "research" / "phonology" / "latin_roots_seed.json"
PHONOLOGY = ROOT / "research" / "phonology" / "confirmed_decisions.json"


def main() -> None:
    data = json.loads(LEXICON.read_text(encoding="utf-8"))
    entries = {item["form"]: item for item in data["entries"]}
    expected = {
        "ager", "kad", "kap", "sentrum", "sert", "sirkul", "siv", "klar",
        "kom", "kred", "kur", "dek", "dik", "dirig", "dots", "fak",
        "lok", "spets", "stru", "vok", "kin", "nation", "major",
    }
    assert expected <= entries.keys(), expected - entries.keys()
    assert entries["kin"]["meaning_it"] == "cinque"
    assert entries["fak"]["source"] == "Latin facere"
    assert "/ma.jor/" in entries["major"]["decision"]
    assert entries["dik"]["source"] == "Latin dicere"
    assert "dikit" in entries["dik"]["decision"]
    assert "normalized to sirkul" in entries["sirkul"]["decision"]

    audit = AUDIT.read_text(encoding="utf-8")
    mapping = {
        "act":"ager", "cad":"kad", "cap":"kap", "centr":"sentrum",
        "cert":"sert", "circul":"sirkul", "civ":"siv", "clar":"klar",
        "com":"kom", "cred":"kred", "cur":"kur", "dec":"dek",
        "dict":"dik", "direct":"dirig", "doc":"dots", "fac":"fak",
        "loc":"lok", "spec":"spets", "struct":"stru", "voc":"vok",
        "cin":"kin", "nacion":"nation",
    }
    for old, newform in mapping.items():
        assert f"`{old}`" in audit, old
        assert f"`{newform}`" in audit, newform

    ph = json.loads(PHONOLOGY.read_text(encoding="utf-8"))
    decisions = {item["id"]: item["decision"] for item in ph["decisions"]}
    assert "sj_coalescence" in decisions
    assert "/s+j/" in decisions["sj_coalescence"]
    assert "[ʃ]" in decisions["sj_coalescence"]

    print("lexicon decision checks passed")


if __name__ == "__main__":
    main()
