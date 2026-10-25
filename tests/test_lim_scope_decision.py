"""Regression checks for author-ratified lim; parser implementation remains pending."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_lim_ratification_source():
    lex = json.loads((ROOT / "research/lexicon/confirmed_lexicon.json").read_text())
    entries = [e for e in lex["entries"] if e["form"] == "lim"]
    assert len(entries) == 1
    assert entries[0]["status"] == "confirmed"
    assert entries[0]["category"] == "functional_word"
    decisions = json.loads((ROOT / "research/grammar/confirmed_decisions.json").read_text())
    d = {x["id"]: x["decision"] for x in decisions["decisions"]}
    assert "explicit_scope_lim_20261025" in d
    spec = (ROOT / "language/word_order.md").read_text()
    for example in ("P ma Q lim ergo R", "P e Q lim o R", "P e Q lim o R lim ma S"):
        assert example in spec
    assert "ordinary comma punctuation has **no scope-changing grammatical force**" in spec


def test_phase_one_does_not_silently_accept_lim_chain():
    # Future parser behavior belongs to a separate approved implementation step.
    # This test intentionally checks normative records only until the parser API is reviewed.
    assert "lim" in (ROOT / "language/word_order.md").read_text()
