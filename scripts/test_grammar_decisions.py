#!/usr/bin/env python3
"""Regression checks for confirmed GlottoDelta grammar decisions."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "research" / "grammar" / "confirmed_decisions.json"
NOMINAL_SPEC = ROOT / "research" / "grammar" / "nominal_number_and_quantification.md"
POLARITY_SPEC = ROOT / "research" / "grammar" / "polarity_and_focus_clitics.md"
CASE_SPEC = ROOT / "research" / "grammar" / "case_and_possession.md"
COPULA_SPEC = ROOT / "research" / "grammar" / "copula.md"
PARTICIPLE_SPEC = ROOT / "research" / "grammar" / "participles_and_resultatives.md"


def main() -> None:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    decisions = {item["id"]: item["decision"] for item in payload["decisions"]}

    required = {
        "nominal_number_default",
        "optional_nominal_plural_wi",
        "plural_redundancy",
        "zero_quantifier_nul",
        "universal_quantifier_omni",
        "integral_totality_tot",
        "modifier_order_demonstrative_quantifier_noun",
        "mi_unassigned",
        "polar_responses_si_no",
        "additive_focus_clitic_si",
        "negative_additive_focus_clitic_no",
        "focus_clitic_scope",
        "genitive_allomorph_s_es",
        "personal_possessives_as_genitives",
        "copula_es_current_person_number",
        "participial_resultative_it",
        "abstract_it_retired",
        "abstract_quality_itat",
        "finite_verb_morphotactics",
    }
    assert required <= decisions.keys(), required - decisions.keys()

    assert "wi" in decisions["optional_nominal_plural_wi"]
    assert "ZERO / NO quantity" in decisions["zero_quantifier_nul"]
    assert "ALL / EVERY" in decisions["universal_quantifier_omni"]
    assert "WHOLE / ENTIRE" in decisions["integral_totality_tot"]
    assert "tik omni om" in decisions["modifier_order_demonstrative_quantifier_noun"]
    assert "tan omni om" in decisions["modifier_order_demonstrative_quantifier_noun"]
    assert "currently has no canonical meaning" in decisions["mi_unassigned"]
    assert "YES" in decisions["polar_responses_si_no"]
    assert "NO" in decisions["polar_responses_si_no"]
    assert "-si" in decisions["additive_focus_clitic_si"]
    assert "-no" in decisions["negative_additive_focus_clitic_no"]
    assert "additional pre-verbal no is not required" in decisions["negative_additive_focus_clitic_no"]
    assert "s, z, sj, tj, or dj" in decisions["genitive_allomorph_s_es"]
    assert "i->is" in decisions["personal_possessives_as_genitives"]
    assert "esi, esu, esa, esin, esun, esan" in decisions["copula_es_current_person_number"]
    assert "dik->dikit" in decisions["participial_resultative_it"]
    assert "confirmed -itat" in decisions["abstract_it_retired"]
    assert "bon->bonitat" in decisions["abstract_quality_itat"]
    assert "root + TAM + person vowel + optional plural N" in decisions["finite_verb_morphotactics"]

    nominal = NOMINAL_SPEC.read_text(encoding="utf-8")
    for example in (
        "`wi om`",
        "`nul om`",
        "`omni om`",
        "`tot dom`",
        "`tik omni om`",
        "`tan omni om`",
    ):
        assert example in nominal, example

    polarity = POLARITY_SPEC.read_text(encoding="utf-8")
    for example in (
        "`si.`",
        "`no.`",
        "`i-si vidi`",
        "`i-no vidi`",
        "`dom-no ...`",
        "`tik omni om-si`",
        "`tik omni om-no`",
    ):
        assert example in polarity, example

    assert "additional pre-verbal `no`" not in polarity
    assert "A second pre-verbal `no` is therefore not" in polarity

    case_spec = CASE_SPEC.read_text(encoding="utf-8")
    for form in ("`doms`", "`faks`", "`vises`", "`...sjes`", "`...tjes`", "`...djes`", "`is`", "`us`", "`as`", "`ins`", "`uns`", "`ans`"):
        assert form in case_spec, form

    copula = COPULA_SPEC.read_text(encoding="utf-8")
    for form in ("`esi`", "`esu`", "`esa`", "`esin`", "`esun`", "`esan`", "`esdi`", "`esdan`"):
        assert form in copula, form
    assert "schwa" in copula.lower() and "No schwa form exists" in copula

    finite = (ROOT / "research" / "grammar" / "finite_verb_structure.md").read_text(encoding="utf-8")
    for form in ("`movi`", "`movu`", "`mova`", "`movin`", "`movun`", "`movan`", "`movdi`", "`movdin`"):
        assert form in finite, form

    participles = PARTICIPLE_SPEC.read_text(encoding="utf-8")
    for form in ("`dikit`", "`movit`", "`vidit`", "`fakit`"):
        assert form in participles, form
    assert "Productive abstract-quality suffix `-itat`" in participles
    for form in ("`bonitat`", "`klaritat`", "`umanitat`"):
        assert form in participles, form

    print("grammar decision checks passed")


if __name__ == "__main__":
    main()
