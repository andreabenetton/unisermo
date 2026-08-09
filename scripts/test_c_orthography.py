#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(ROOT / 'scripts/analyze_c_orthography.py')], check=True, stdout=subprocess.DEVNULL)
data = json.loads((ROOT / 'research/phonology/c_orthography_study.json').read_text(encoding='utf-8'))
s = data['summary']
assert s['roots'] == 74
assert s['c_bearing_roots'] == 20
assert s['c_occurrences'] == 21
assert s['soft_context_occurrences'] == 4
assert s['hard_context_occurrences'] == 11
assert s['final_occurrences'] == 6
soft = data['strategies']['soft_c']
no_s = data['strategies']['no_c_s']
hard = data['strategies']['hard_c']
assert soft['exact_unchanged_roots'] == 57
assert no_s['exact_unchanged_roots'] == 54
assert hard['exact_unchanged_roots'] == 70
assert not soft['canonical_collision_groups']
assert not soft['soft_c_to_s_variant_collision_groups']
print('c-orthography regression checks: OK')
