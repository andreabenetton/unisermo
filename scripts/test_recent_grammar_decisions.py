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
assert 'traes DEST-ad SOURCE-de' in d['explicit_state_transition_traes'] and 'ades X' in d['explicit_state_transition_traes']
assert 'Y-NOM traes X-em RESULT-da' in d['explicit_state_transition_traes'] and 'akvaem solidda' in d['explicit_state_transition_traes']
assert '-da resultative predicative/transformative' in d['nominal_case_inventory_seven']
print('recent grammar decision checks passed')
