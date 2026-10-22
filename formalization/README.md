# Unisermo — Phase 1 formal reference (work in progress)

This is a **source-linked executable mirror** of the existing accepted
Unisermo specification, not a new dialect. The normative sources remain
`language/` and the `research/*/confirmed_decisions.json` files until a
subsequent LDR explicitly approves a source-of-truth migration (see
`docs/ldr/LDR-0004-formal-source-of-truth.md`).

## Recorded decisions and rationale

`docs/ldr/` contains Language Design Records. Use them to track a hypothesis
from proposal and alternatives through evidence to explicit acceptance. The
weighted lexical objective in LDR-0002 remains **Experimental**, not an
established language rule.

## Commands

From the repository root (Python 3.11+ recommended):

```sh
python3 -m formalization build
python3 -m formalization build --check
python3 -m formalization validate
python3 -m formalization analyze dikodi
python3 -m formalization sentence 'ka i no diki domem?'
python3 -m formalization generate dik --tense past --aspect perfect --person 1
python3 -m formalization noun spets --case genitive
python3 tests/test_formalization.py
```

`build` deterministically derives:

- `data/rule_registry.json`: references and content hashes for all confirmed
  grammar and phonology decisions; **not** synthetic retrospective LDRs.
- `data/lexicon_index.json`: the confirmed lexicon plus separately marked,
  sourced attested/example-only entries. These entries are not auto-approved.
- `data/ldr_registry.json`: current LDR status, provenance and file checksum.
- `corpus/morphology.jsonl`: exhaustive forms for five representative verbs
  (5 x 3 aspects x 3 times x 3 persons x 2 numbers) and seven cases for six
  sample nominals (6 x 7), with a machine-readable analysis and lexical status.
  These are **312 morphological forms**, not 312 semantic sentence pairs.

## Runtime modules

The `Unisermo` API is assembled in `formalization/core.py` from dedicated
mixins in `formalization/generator/` and `formalization/parser/`. This is a
pure code organization refactor; all feature values still come from the
existing accepted source-linked data. `formalization/semantics/` documents the
unimplemented logical-form layer and must not be mistaken for a real semantic parser.

## Capabilities and deliberate limits

The reference parser recognizes finite tense/aspect/person/number, case-marked
nominals, the `-it` resultative/participle, and a small SVO sentence pattern
with optional pronoun subject, pro-drop, `ka` questions, and pre-verbal `no`.
Multiple analyses are preserved for ambiguous forms; unsupported syntax is
rejected rather than assigned guessed semantics.

Not yet implemented: full lexical valency, focus enclitic scope, all free
relator constructions, derivational compounding, passives, optional word-order
variants, all wh-questions, zero copula and non-canonical phonetic realizations.
These remain legitimate language phenomena even when unsupported by this
**reference subset**.

The input corpus is for deterministic *morphological* regression. Semantic
benchmarks require new source-reviewed sentence meaning pairs and holdouts;
measuring token savings before those exist would be premature.

## Dependencies

The builder, parser and invariant checks use Python's standard library. When
`jsonschema` is available, `validate` additionally validates JSON schema
shapes. It is optional and cannot substitute for the semantic checks.
