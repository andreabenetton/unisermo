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
    assert {"kin", "fak", "major", "dik"} <= entries.keys()
    assert entries["kin"]["meaning_it"] == "cinque"
    assert "facere" in entries["fak"]["source"]
    assert "/ma.jor/" in entries["major"]["decision"]
    assert "dicere" in entries["dik"]["source"]
    assert "dikit" in entries["dik"]["decision"]

    seed = json.loads(ROOT_SEED.read_text(encoding="utf-8"))
    c_roots = [item for item in seed["roots"] if "c" in item["root"]]
    assert len(c_roots) == 20

    audit = AUDIT.read_text(encoding="utf-8")
    for item in c_roots:
        assert f"`{item['root']}`" in audit, item["root"]
        latin_display = item["latin"].replace("/", " / ")
        assert f"`{latin_display}`" in audit, item["latin"]
    assert "`cin`" in audit and "`kin`" in audit
    assert "`nacion`" in audit
    assert "confirmed -> `fak`" in audit
    assert "confirmed -> `dik`" in audit and "`dikit`" in audit

    ph = json.loads(PHONOLOGY.read_text(encoding="utf-8"))
    decisions = {item["id"]: item["decision"] for item in ph["decisions"]}
    assert "sj_coalescence" in decisions
    assert "/s+j/" in decisions["sj_coalescence"]
    assert "[ʃ]" in decisions["sj_coalescence"]

    print("lexicon decision checks passed")


if __name__ == "__main__":
    main()
