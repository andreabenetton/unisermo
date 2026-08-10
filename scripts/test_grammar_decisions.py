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
        "nominalized_participle_it",
        "abstract_it_retired",
        "abstract_quality_itat",
        "finite_verb_morphotactics",
        "finite_tense_inventory",
        "finite_aspect_inventory",
        "servile_verbs_analytic",
        "modal_m_retired",
        "finite_aspect_vowel_protection",
        "nominal_case_inventory_six",
        "comitative_kun_analytic",
        "extended_case_suffixes_retired",
    }
    assert required <= decisions.keys(), required - decisions.keys()

    assert "wi" in decisions["optional_nominal_plural_wi"]
    assert "ZERO / NO quantity" in decisions["zero_quantifier_nul"]
    assert "ALL / EVERY" in decisions["universal_quantifier_omni"]
    assert "WHOLE / ENTIRE" in decisions["integral_totality_tot"]
    assert "tik omni uman" in decisions["modifier_order_demonstrative_quantifier_noun"]
    assert "tan omni uman" in decisions["modifier_order_demonstrative_quantifier_noun"]
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
    assert "wi fakit" in decisions["nominalized_participle_it"]
    assert "duo fakit" in decisions["nominalized_participle_it"]
    assert "confirmed -itat" in decisions["abstract_it_retired"]
    assert "bon->bonitat" in decisions["abstract_quality_itat"]
    assert "root + aspect + time + person vowel + optional plural N" in decisions["finite_verb_morphotactics"]
    assert "zero for present, d for past, and f for future" in decisions["finite_tense_inventory"]
    assert "e ongoing/progressive" in decisions["finite_aspect_inventory"]
    assert "o completed/perfect" in decisions["finite_aspect_inventory"]
    assert "canonical hiatus" in decisions["finite_aspect_vowel_protection"]
    assert "finite servile verb followed by the bare infinitive/root" in decisions["servile_verbs_analytic"]
    assert "synthetic m" in decisions["modal_m_retired"]
    assert "-em accusative" in decisions["nominal_case_inventory_six"]
    assert "-in locative" in decisions["nominal_case_inventory_six"]
    assert "kun + noun phrase" in decisions["comitative_kun_analytic"]
    assert "-ko" in decisions["comitative_kun_analytic"]
    assert "RELATOR + NP" in decisions["extended_case_suffixes_retired"]

    nominal = NOMINAL_SPEC.read_text(encoding="utf-8")
    for example in (
        "`wi uman`",
        "`nul uman`",
        "`omni uman`",
        "`tot dom`",
        "`tik omni uman`",
        "`tan omni uman`",
    ):
        assert example in nominal, example

    polarity = POLARITY_SPEC.read_text(encoding="utf-8")
    for example in (
        "`si.`",
        "`no.`",
        "`i-si vidi`",
        "`i-no vidi`",
        "`dom-no ...`",
        "`tik omni uman-si`",
        "`tik omni uman-no`",
    ):
        assert example in polarity, example

    assert "additional pre-verbal `no`" not in polarity
    assert "A second pre-verbal `no` is therefore not" in polarity

    case_spec = CASE_SPEC.read_text(encoding="utf-8")
    for form in ("`doms`", "`faks`", "`vises`", "`...sjes`", "`...tjes`", "`...djes`", "`is`", "`us`", "`as`", "`ins`", "`uns`", "`ans`", "`kun uman`", "`per`", "`pro`", "`due`", "`fin`", "`tem`", "`mod`"):
        assert form in case_spec, form

    copula = COPULA_SPEC.read_text(encoding="utf-8")
    for form in ("`esi`", "`esu`", "`esa`", "`esin`", "`esun`", "`esan`", "`esdi`", "`esdan`", "`esei`", "`esoi`", "`esedi`", "`esodi`", "`esefi`", "`esofi`"):
        assert form in copula, form
    assert "schwa" in copula.lower() and "No schwa form exists" in copula

    finite = (ROOT / "research" / "grammar" / "finite_verb_structure.md").read_text(encoding="utf-8")
    for form in ("`diki`", "`dikei`", "`dikoi`", "`dikdi`", "`dikedi`", "`dikodi`", "`dikfi`", "`dikefi`", "`dikofi`"):
        assert form in finite, form

    participles = PARTICIPLE_SPEC.read_text(encoding="utf-8")
    for form in ("`dikit`", "`movit`", "`vidit`", "`fakit`", "`wi fakit`", "`duo fakit`"):
        assert form in participles, form
    assert "Productive abstract-quality suffix `-itat`" in participles
    for form in ("`bonitat`", "`klaritat`", "`umanitat`"):
        assert form in participles, form

    print("grammar decision checks passed")


if __name__ == "__main__":
    main()
