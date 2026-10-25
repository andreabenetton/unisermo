#!/usr/bin/env python3
"""Regression checks for confirmed Unisermo lexical decisions."""

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
        "ager", "kad", "kap", "sentr", "sert", "sirkul", "siv", "klar",
        "kun", "kom", "ker", "per", "pro", "due", "fin", "tem", "mod", "kred", "kurar", "dek", "dik", "dirig", "dok", "fak",
        "mila", "mega", "giga", "lok", "spets", "stru", "vok", "kin", "nation", "uman", "major", "ekwal", "alt", "bas", "altmov", "basmov", "aer", "plan", "aerplan", "adel", "adelo", "adele", "gen", "geno", "gene", "adelgen", "bisjergen", "fil", "filadelgen", "genegene", "genegeno", "genogene", "genogeno",
    }
    assert expected <= entries.keys(), expected - entries.keys()
    assert entries["kin"]["meaning_it"] == "cinque"
    assert entries["fak"]["source"] == "Latin facere"
    assert "/ma.jor/" in entries["major"]["decision"]
    assert entries["dik"]["source"] == "Latin dicere"
    assert "dikit" in entries["dik"]["decision"]
    assert "normalized to sirkul" in entries["sirkul"]["decision"]
    assert "/e.kwal/" in entries["ekwal"]["decision"]
    assert entries["uman"]["meaning_it"] == "persona; essere umano"
    assert entries["pel"]["meaning_en"] == "push"
    assert entries["trak"]["meaning_en"] == "pull; draw; drag"
    assert entries["alt"]["meaning_en"] == "high; upper; up"
    assert entries["bas"]["meaning_en"] == "low; lower; down"
    assert entries["altmov"]["meaning_en"] == "ascend; go up"
    assert entries["basmov"]["meaning_en"] == "descend; go down"
    assert entries["aer"]["meaning_en"] == "air"
    assert entries["plan"]["meaning_en"] == "plane; flat; level"
    assert entries["aerplan"]["meaning_en"] == "airplane; aeroplane"
    assert entries["aerplan"]["category"] == "compound"
    assert "aer+plan" in entries["aerplan"]["decision"]
    assert entries["adel"]["meaning_en"].startswith("sibling")
    assert entries["adelo"]["meaning_en"].startswith("brother")
    assert entries["adele"]["meaning_en"].startswith("sister")
    assert entries["gen"]["meaning_en"].startswith("parent")
    assert entries["geno"]["meaning_en"] == "father"
    assert entries["gene"]["meaning_en"] == "mother"
    assert entries["adelgen"]["meaning_en"].startswith("uncle or aunt")
    assert entries["bisjergen"]["category"] == "compound"
    assert entries["fil"]["meaning_en"].startswith("offspring")
    assert entries["filadelgen"]["meaning_en"].startswith("first cousin")
    for term in ("genegene", "genegeno", "genogene", "genogeno"):
        assert entries[term]["category"] == "compound"
    assert entries["genegene"]["meaning_en"].startswith("maternal grandmother")
    assert entries["genegeno"]["meaning_en"].startswith("paternal grandmother")
    assert entries["genogene"]["meaning_en"].startswith("maternal grandfather")
    assert entries["genogeno"]["meaning_en"].startswith("paternal grandfather")
    assert entries["mila"]["meaning_en"].startswith("thousand")
    assert entries["mega"]["meaning_en"].startswith("million")
    assert entries["giga"]["meaning_en"].startswith("billion")
    assert "mil" not in entries
    assert "frat" not in entries
    assert "umano" in entries["uman"]["decision"]
    assert "umane" in entries["uman"]["decision"]
    assert "umanitat" in entries["uman"]["decision"]
    assert "kun + noun phrase" in entries["kun"]["decision"]
    for rel in ("per", "pro", "due", "fin", "tem", "mod"):
        assert entries[rel]["category"] == "function_word"
        assert "Former suffix" in entries[rel]["decision"]

    # Canonical lexical forms may use only the 21 official graphemes.
    allowed = set("aeioupbtdkgmnfvszlrjw")
    # A trailing hyphen is the dictionary notation for a derivational prefix,
    # not an extra grapheme in the spoken lexical root.
    normalized_forms = {
        form: form[:-1] if item["category"] == "derivational_prefix" and form.endswith("-") else form
        for form, item in entries.items()
    }
    invalid_forms = {form: sorted(set(surface) - allowed) for form, surface in normalized_forms.items()
                     if not surface or set(surface) - allowed}
    assert invalid_forms == {}, invalid_forms

    audit = AUDIT.read_text(encoding="utf-8")
    mapping = {
        "act":"ager", "cad":"kad", "cap":"kap", "centr":"sentr",
        "cert":"sert", "circul":"sirkul", "civ":"siv", "clar":"klar",
        "com":"kun", "cred":"kred", "cur":"kurar", "dec":"dek",
        "dict":"dik", "direct":"dirig", "doc":"dok", "fac":"fak",
        "loc":"lok", "spec":"spets", "struct":"stru", "voc":"vok",
        "cin":"kin", "nacion":"nation",
    }
    for old, newform in mapping.items():
        assert f"`{old}`" in audit, old
        assert f"`{newform}`" in audit, newform

    full_audit = json.loads((ROOT / "research" / "lexicon" / "legacy_full_lexicon_audit.json").read_text(encoding="utf-8"))
    assert full_audit["collisions"] == []
    all_forms = {item["legacy_form"]: item for item in full_audit["all_forms"]}
    assert all_forms["kom"]["status"] == "valid_orthography"
    assert all_forms["kur"]["replacement"] == "ker"
    assert all_forms["un"]["replacement"] == "uno"
    assert all_forms["ekual"]["replacement"] == "ekwal"
    assert all_forms["cin"]["replacement"] == "kin"

    ph = json.loads(PHONOLOGY.read_text(encoding="utf-8"))
    decisions = {item["id"]: item["decision"] for item in ph["decisions"]}
    assert "sj_coalescence" in decisions
    assert "/s+j/" in decisions["sj_coalescence"]
    assert "[ʃ]" in decisions["sj_coalescence"]

    print("lexicon decision checks passed")


if __name__ == "__main__":
    main()