# Automated candidate screen (research only)

Run from repository root:

```sh
python -m benchmarks.lexical_screen --output benchmarks/reports/lexical-screen.json
python -m unittest discover -s tests -p 'test_lexical_screen.py'
```

The script checks the approved 21-letter alphabet, exact lexical and reserved
grammatical collisions, likely collisions from explicitly licensed soft accent
mergers, and potential overlaps between generated finite-verb/nominal forms
and existing root/grammar forms.

**Limits:** it cannot establish global pronounceability, phonotactic comfort,
speaker recognizability, real usage frequency, or full derivational ambiguity.
The accent equivalence set is deliberately conservative and may over-report
ambiguities; multi-phoneme coalescences are not exhaustively modeled.
A green screen is not approval for a root change.

For the center family, source Italian /tʃ/ is not a Unisermo phoneme. Compare
`sentr` and `kentr` as native candidates, not source `centr` with Italian
reading. The possible coalesced realization of `tj` is not an independent
phoneme.

See LDR-0008 and `research/lexicon/phonetic-graphic-recognizability.md`.
