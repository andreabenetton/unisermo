#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
g=json.loads((ROOT/'research/grammar/confirmed_decisions.json').read_text())
d={x['id']:x['decision'] for x in g['decisions']}
assert '/i.a/' in d['derivational_place_field_ia']
assert 'uno dom' in d['indefinite_singular_uno']
assert 'No separate apocopated article un' in d['indefinite_singular_uno']
assert 'kom' in d['question_words_kom_ker'] and 'ker' in d['question_words_kom_ker']
assert '-or' in d['derivational_person_agent_or'] and 'Historical agentive -er is retired' in d['derivational_person_agent_or']
assert '-il' in d['derivational_instrument_device_il'] and 'Historical instrumental -or is retired' in d['derivational_instrument_device_il']
assert 'per + NP' in d['derivational_instrument_device_il']
assert 'ines' in d['state_phase_family_es'] and 'ades' in d['state_phase_family_es'] and 'dees' in d['state_phase_family_es'] and 'rees' in d['state_phase_family_es']
assert 'aes is already the canonical genitive/possessive of ae' in d['state_phase_family_es']
assert 'inmov' in d['phase_prefix_family'] and 'admov' in d['phase_prefix_family'] and 'demov' in d['phase_prefix_family'] and 'remov' in d['phase_prefix_family']
assert 'do not replace finite aspect' in d['phase_prefix_family']
assert 'X-NOM mov = X moves' in d['motion_family_valency_mov'] and 'Y-NOM mov X-em = Y moves/displaces X' in d['motion_family_valency_mov']
assert 'admov, inmov, demov, remov' in d['motion_family_valency_mov'] and 'does not lexicalize push or pull' in d['motion_family_valency_mov']
assert 'traes DEST-ad SOURCE-de' in d['explicit_state_transition_traes'] and 'ades X' in d['explicit_state_transition_traes']
assert 'Y-NOM traes X-em RESULT-da' in d['explicit_state_transition_traes'] and 'akwaem solidda' in d['explicit_state_transition_traes']
assert '-da resultative predicative/transformative' in d['nominal_case_inventory_seven']
print('recent grammar decision checks passed')
assert 'pel = push' in d['motion_force_roots_pel_trak'] and 'trak = pull/draw' in d['motion_force_roots_pel_trak']
assert 'mov altad' in d['vertical_motion_alt_bas'] and 'mov basad' in d['vertical_motion_alt_bas']
assert 'altmov = ascend/go up' in d['vertical_motion_alt_bas'] and 'basmov = descend/go down' in d['vertical_motion_alt_bas']
assert 'admov remains begin moving' in d['vertical_motion_alt_bas'] and 'demov remains cease moving' in d['vertical_motion_alt_bas']


def test_cardinal_two_is_bis_everywhere_canonical():
    root = Path(__file__).resolve().parents[1]
    numerals = (root / "language" / "numerals.md").read_text()
    decisions = json.loads((root / "research" / "grammar" / "confirmed_decisions.json").read_text())
    assert "| 2 | `bis` |" in numerals
    assert "duo" not in numerals
    entry = next(d for d in decisions["decisions"] if d["id"] == "numeral_two_bis")
    assert "cardinal numeral 2" in entry["decision"]


def test_jer_is_general_iteration_counter_and_compounds_are_fused():
    root = Path(__file__).resolve().parents[1]
    numerals = (root / "language" / "numerals.md").read_text()
    decisions = json.loads((root / "research" / "grammar" / "confirmed_decisions.json").read_text())
    assert "`dekbis`" in numerals and "`bisdek`" in numerals
    assert "`dek bis`" not in numerals and "`bis dek`" not in numerals
    assert "bisjer = two times; two iterations; two steps" in numerals
    entry = next(d for d in decisions["decisions"] if d["id"] == "iteration_counter_jer")
    assert "not restricted to genealogy" in entry["decision"]
    assert "bisjer = two times/two iterations/two steps" in entry["decision"]
