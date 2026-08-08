#!/usr/bin/env python3
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'analyze_affricates.py')], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
path = os.path.join(ROOT, 'research', 'phonology', 'affricate_results.json')
r = json.load(open(path, encoding='utf-8'))
c = r['component_proxies']
assert c['tj_components']['P_component_pct'] > 80
assert c['ts_components']['P_component_pct'] > 80
assert c['dj_components']['P_component_pct'] > 55
assert r['recommendations']['ts']['new_phoneme'] is False
assert r['recommendations']['tsh']['underlying'] == ['t', 'j']
assert r['recommendations']['dzh']['underlying'] == ['d', 'j']
print('affricate study checks passed')
