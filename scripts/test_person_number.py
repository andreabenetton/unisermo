#!/usr/bin/env python3
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANALYZER = os.path.join(ROOT, "scripts", "analyze_person_number.py")
RESULTS = os.path.join(ROOT, "research", "phonology", "person_number_results.json")
subprocess.run([sys.executable, ANALYZER], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
x = json.load(open(RESULTS, encoding="utf-8"))

assert x["person_mapping"] == {"1": "i", "2": "u", "3": "a"}
assert x["person_vowel_subsystem"]["P0_attested_pct"] > 98.0
strict_n = x["plural_candidates"]["strict_n"]
arch = x["plural_candidates"]["final_nasal_N_written_n"]
assert arch["P_attested_pct"] > 99.9
assert arch["P0_attested_pct"] > strict_n["P0_attested_pct"]
assert arch["P0_attested_pct"] > 98.0
assert x["layout_pressure"]["VN_person_then_plural"]["marker_induced_CC"] == 0
assert x["layout_pressure"]["NV_plural_then_person"]["marker_induced_CC_pct"] > 95
assert x["decision"]["plural"]["forms"] == {
    "1SG": "i", "2SG": "u", "3SG": "a", "1PL": "in", "2PL": "un", "3PL": "an"
}
print("person-number regression checks: OK")
