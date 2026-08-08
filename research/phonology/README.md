# Phonology research workspace

This directory is intentionally **non-canonical**. It exists on the local
`phoneme-study` branch while phoneme choices are being evaluated. Confirmed
choices may later be merged into local `main`; unconfirmed experiments must not
change GlottoDelta production semantics or the auxiliary-language specification.

## Files

- `phoneme_targets.json` — canonical target labels plus acceptable-realization
  families used by the analysis.
- `candidates.json` — inventory candidates under comparison.
- `latin_roots_seed.json` — provisional Latin/international root pressure test.
- `results.json` — generated quantitative results.
- `phoneme_selection.md` — generated human-readable working report.

## Reproduce

```bash
python3 scripts/analyze_phoneme_inventory.py --write
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
not carry a Glottolog genealogy/area table. Affricates `/ts tʃ dʒ/` also require
separate complex-segment treatment rather than being silently priced as one
simple chart cell.
