#!/usr/bin/env python3
"""Lightweight regression checks for the phoneme research analyzer."""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS = os.path.join(ROOT, "research", "phonology", "results.json")
ANALYZER = os.path.join(ROOT, "scripts", "analyze_phoneme_inventory.py")

subprocess.run([sys.executable, ANALYZER, "--write"], cwd=ROOT, check=True,
               stdout=subprocess.DEVNULL)
with open(RESULTS, encoding="utf-8") as f:
    x = json.load(f)

assert x["dataset"]["chart_symbols"] == 111
assert x["dataset"]["languages"] == 2122
assert x["dataset"]["demographic_languages"] == 384

# Sanity anchors from the frozen GlottoDelta baseline.
assert x["targets"]["m"]["P_attested_pct"] > 99.0
assert x["targets"]["y"]["P_attested_pct"] > 98.0
assert x["targets"]["schwa"]["L_family_pct"] < 35.0

current = x["candidates_strict"]["current_simple_21"]
no_schwa = x["candidates_strict"]["no_schwa_20"]
assert no_schwa["P0"] > current["P0"]
assert no_schwa["P2"] > current["P2"]
assert no_schwa["mean_missing_P"] < current["mean_missing_P"]

strict_lex = x["candidates_strict"]["lexical22_yw"]
soft_lex = x["candidates_soft_production"]["lexical22_yw"]
assert soft_lex["P0"] >= strict_lex["P0"]
assert soft_lex["P2"] >= strict_lex["P2"]

three = x["vowel_subsystems"]["three_vowel_aiu"]
five = x["vowel_subsystems"]["five_vowel_aeiou"]
assert three["P0"] > five["P0"]
assert five["target_count"] == 5

print("phoneme-study regression checks: OK")
