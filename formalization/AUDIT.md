# Phase 1 baseline audit — 2026-10-22

## Sources and preserved decisions

- `research/grammar/confirmed_decisions.json`: 42 pre-existing confirmed
  grammar decisions.
- `research/phonology/confirmed_decisions.json`: 13 pre-existing confirmed
  phonology decisions.
- `research/lexicon/confirmed_lexicon.json`: 44 previously confirmed lexical
  entries. `formalization/data/attested_forms.json` adds 34 separate entries
  drawn from living specifications, clearly marked either `example_only` or
  `decision_attested_not_indexed`, not promoted to the confirmed lexicon.
- Four LDRs start the decision-provenance system; accepted governance decisions
  are distinct from experimental efficiency proposals.

## Reconciled documentary discrepancies

- `language/README.md` formerly listed six nominal cases despite the seven
  case values in the live `language/noun_case_system.md`. The summary now lists
  the seventh resultative `-da` while preserving the analytic `kun` comitative.
- A form `tot` was attributed to `language/noun_number_system.md`, which did
  not contain it. The inventory now cites the actual document
  `research/grammar/nominal_number_and_quantification.md`.
- `spets` is an already **confirmed** lexical entry but was omitted from the
  reference parser's nominal-role set; it is now recognized as a noun, not
  duplicated as an example-only entry.

## Open formalization questions

1. Several decisions explicitly exist in confirmed decision JSON or Markdown
   but lack confirmed lexicon entries. Their attestations are indexed without
   conferring canonical lexical status, pending lexical reconciliation.
2. Lexical valency and ambiguity resolution require an explicit semantic
   schema; only narrow deterministic syntactic patterns are currently parsed.
3. Human-root recognizability, articulation cost, tokenizer cost, and
   interpretive accuracy are currently **unmeasured**. LDR-0002 records a
   proposed experimental scoring framework, not fitted coefficients.
4. Several established language features are not yet in the executable mirror;
   the complete list is in `formalization/data/morphology.json`.
5. A future LDR needs to decide whether structured data become normative for
   individual grammar rules; no automatic authority transfer occurred.

## Reproducibility

```sh
python3 -m formalization build --check
python3 -m formalization validate
python3 tests/test_formalization.py
for t in tests/test_*.py; do python3 "$t"; done
```

No atlas research data or historical language snapshots were modified.
