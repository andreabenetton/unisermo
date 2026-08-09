# Phonology research workspace

This directory contains both confirmed design constraints and continuing phoneme
research. Confirmed design decisions are recorded in `confirmed_decisions.json`. Research experiments
remain separated until selected, and none of this tooling changes GlottoDelta production
semantics.

## Files

- `confirmed_decisions.json` — project-owner-confirmed phonological design constraints.
- `phoneme_targets.json` — canonical target labels plus acceptable-realization
  families used by the analysis.
- `candidates.json` — inventory candidates under comparison.
- `latin_roots_seed.json` — provisional Latin/international root pressure test.
- `results.json` — generated quantitative results.
- `phoneme_selection.md` — generated human-readable working report.
- `person_marker_study.md` — selected person/number morphology and rationale.
- `person_number_results.json` — generated person/number coverage and layout metrics.
- `optional_gender_study.md` — confirmed optional masculine/feminine referential-specificity study and `ano/ane` resolution.
- `affricate_study.md` — decision study for /ts tʃ dʒ/ as complex segments/sequences.
- `affricate_results.json` — generated component and curated-profile evidence for the affricate study.
- `family_inventory.json` — generated Glottolog 5.3 top-level genealogical inventory for the frozen source sample.
- `family_inventory.md` — human-readable represented/absent family and isolate report, with pseudo-category diagnostics.
- `vendor/glottolog-5.3/` — pinned Glottolog 5.3 research inputs; the Newick forest is the primary genealogy source.

## Reproduce

```bash
python3 scripts/analyze_phoneme_inventory.py --write
python3 scripts/analyze_person_number.py
python3 scripts/test_person_number.py
python3 scripts/analyze_affricates.py
python3 scripts/test_affricates.py
python3 scripts/analyze_family_inventory.py
python3 scripts/test_family_inventory.py
```

The phoneme/person/affricate analyzers read the frozen `baseline/original.html`;
the family inventory additionally reads the pinned Glottolog inputs under
`research/phonology/vendor/glottolog-5.3/`. None of these tools alters
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
The current root seed is unweighted and deliberately small. The Glottolog 5.3
top-level family/isolate inventory is now built in `family_inventory.json`, but
**no phoneme-by-family score has yet been calculated**. Genealogical independence
is the primary structure; macroarea is retained only as secondary descriptive
metadata. Affricates `/ts tʃ dʒ/` have now been resolved as sequences/coalescent
surface realizations rather than independent phonemes; see `affricate_study.md`.
