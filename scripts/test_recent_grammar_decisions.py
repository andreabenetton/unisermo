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
print('recent grammar decision checks passed')
