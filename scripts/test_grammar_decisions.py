#!/usr/bin/env python3
"""Regression checks for confirmed GlottoDelta grammar decisions."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "research" / "grammar" / "confirmed_decisions.json"
SPEC = ROOT / "research" / "grammar" / "nominal_number_and_quantification.md"


def main() -> None:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    decisions = {item["id"]: item["decision"] for item in payload["decisions"]}

    required = {
        "nominal_number_default",
        "optional_nominal_plural_wi",
        "plural_redundancy",
        "universal_quantifier_omni",
        "integral_totality_tot",
        "modifier_order_demonstrative_quantifier_noun",
        "mi_unassigned",
    }
    assert required <= decisions.keys(), required - decisions.keys()

    assert "wi" in decisions["optional_nominal_plural_wi"]
    assert "ALL / EVERY" in decisions["universal_quantifier_omni"]
    assert "WHOLE / ENTIRE" in decisions["integral_totality_tot"]
    assert "tik omni om" in decisions["modifier_order_demonstrative_quantifier_noun"]
    assert "tan omni om" in decisions["modifier_order_demonstrative_quantifier_noun"]
    assert "currently has no canonical meaning" in decisions["mi_unassigned"]

    text = SPEC.read_text(encoding="utf-8")
    for example in (
        "`wi om`",
        "`omni om`",
        "`tot dom`",
        "`tik omni om`",
        "`tan omni om`",
    ):
        assert example in text, example

    print("grammar decision checks passed")


if __name__ == "__main__":
    main()
