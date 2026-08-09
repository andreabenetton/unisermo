# Phonology research workspace

This directory contains both confirmed design constraints and continuing phoneme
research. Confirmed design decisions are recorded in `confirmed_decisions.json`, and the
current normative sound-system specification is `alphabet_and_phonology_revised.md`.
Research experiments remain separated until selected, and none of this tooling changes
GlottoDelta production semantics.

## Files

- `confirmed_decisions.json` — project-owner-confirmed phonological design constraints.
- `alphabet_and_phonology_revised.md` — current normative alphabet, canonical phonemes, accent/coalescence rules, and root-adaptation policy.
- `phoneme_targets.json` — canonical target labels plus acceptable-realization
  families used by the analysis.
- `candidates.json` — inventory candidates under comparison.
- `latin_roots_seed.json` — provisional Latin/international root pressure test.
- `results.json` — generated quantitative results.
- `phoneme_selection.md` — generated historical/working quantitative report; its investigated candidates may include sounds later excluded by `confirmed_decisions.json`.
- `person_marker_study.md` — selected person/number morphology and rationale.
- `person_number_results.json` — generated person/number coverage and layout metrics.
- `optional_gender_study.md` — confirmed optional masculine/feminine referential-specificity study and `ano/ane` resolution.
- `affricate_study.md` — decision study for /ts tʃ dʒ/ as complex segments/sequences.
- `affricate_results.json` — generated component and curated-profile evidence for the affricate study.

## Reproduce

```bash
python3 scripts/analyze_phoneme_inventory.py --write
python3 scripts/analyze_person_number.py
python3 scripts/test_person_number.py
python3 scripts/analyze_affricates.py
python3 scripts/test_affricates.py
```

The analyzer reads only the frozen `baseline/original.html`. It does not alter
GlottoDelta's production `L`/`P` calculations.

### Metric distinction

The research metric `P_attested` is **not** the UI metric `P`:

- GlottoDelta UI `P` counts demographic languages only when the relevant symbol
  has a green/amber mapped or variant relation in the curated adjudication layer.
- Research `P_attested` asks whether a demographic language has an attested
  member of a target-realization family in the frozen source inventories.

This distinction is deliberate: the research question is likely familiarity
with producing a target category, not orthography-verification coverage.

## Important limitations

The target families are design hypotheses, not claims that their members are
phonologically identical. PHOIBLE is a convenience sample. The CLDR-derived
population universe is a weighting base and may overlap L1/L2 populations.
The current root seed is unweighted and deliberately small. Family/macroarea
balance is not yet calculated because the normalized GlottoDelta snapshot does
not carry a Glottolog genealogy/area table. Affricates `/ts tʃ dʒ/` have now been
resolved as sequences/coalescent surface realizations rather than independent
phonemes; see `affricate_study.md`.
