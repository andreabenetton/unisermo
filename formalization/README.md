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

## Ratified scalar factors, ordinals and fractions (2026-10-24)

The following author-approved numeral constructions are supported in the
deterministic reference implementation, without inventing new roots:

- `NUMfol` (positive scalar factor) differs from `NUMjer` repetition;
  e.g. `bisfol` = ×2, `terfol` = ×3, `forfol` = ×4. The
  contracted `unfol`, zero `nulfol`, and historical `-mul`
  are not ratified.
- Positive ordinal `NUMim` applies to an entire cardinal and
  contracts terminal `-o` (`unim`, `otim`, `dekunim`).
  Full `unoim` / `otoim` forms remain valid **noncanonical**
  accepted variants, normalized by the parser.
- Two-word fraction `CARDINAL ORDINAL`, with numerator 0..999999999999
  and denominator 2..999999999999, retains unreduced values;
  `bis forim` = 2/4, `uno bisim` = 1/2.
- Percentages are ordinary fractions with denominator `senim`:
  `kin senim` means 5%. There is no separate percentage lexeme.

```sh
python3 -m formalization factor 4
python3 -m formalization multiplicative forfol
python3 -m formalization order 21
python3 -m formalization ordinal bisdekunim
python3 -m formalization ratio 2 4
python3 -m formalization fraction 'kin senim'
```

The restricted SVO noun-phrase parser permits **one** ordinal modifier
or **one** scalar factor modifier, but does not infer the scope of
mixed modifier sequences or parse standalone fractional NPs as
ordinary nominal modifiers. Numeric generators are deterministic;
there is no claim of new semantic interpreter support.

## Cardinal numerals and iteration (0–999,999,999,999)

The `formalization/parser/numeral.py` module now generates and parses **every canonical number 0–999,999,999,999**. It composes groups of three digits using only a 999-entry coefficient index and rejects variants with explicit zero-place components, redundant `uno` before a power, repeated powers and unknown spellings. It also recognizes positive `NUMjer` counters and passes the same normalized `_cardinal` generator to the kinship parser (whose *path expansion* independently remains limited to 128).

Examples:

```sh
python3 -m formalization number 321
python3 -m formalization numeral tersenbisdekuno
python3 -m formalization iteration bisjer
python3 -m formalization sentence 'vidi tersenbisdekuno domem'
```

Numerals act as **prenomial quantifiers** and are never case-inflected; case remains on the following noun. `nul` means zero. Redundant `wi` is rejected in the supported SVO subset when quantity is specified by any canonical numeral. The ordinary confirmed-lexicon and historical-example provenance of words is retained independently from the newly computed `cardinal_numeral` analysis (`status: canonical_by_rule`). No implication of new canonical words or empirical efficiency is intended.

See [normative numerals](../language/numerals.md). Powers beyond giga, signed numbers and decimals remain **outside this approved reference range**; ordinal, fraction and scalar-factor extensions are documented above.

## Commands

From the repository root (Python 3.11+ recommended):

```sh
python3 -m formalization build
python3 -m formalization build --check
python3 -m formalization validate
python3 -m formalization analyze dikodi
python3 -m formalization numeral tersenbisdekuno
python3 -m formalization number 321
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

The reference parser recognizes canonical cardinals through 999,999,999,999 as prenominal quantifiers, positive NUMjer counters, ratified positive ordinals and NUMfol factors, and separately parsed two-word fractions, finite tense/aspect/person/number, case-marked
nominals, the `-it` resultative/participle, and a small SVO sentence pattern
with optional pronoun subject, pro-drop, `ka` questions, and pre-verbal `no`.
Multiple analyses are preserved for ambiguous forms; unsupported syntax is
rejected rather than assigned guessed semantics.

## Productive genealogy (approved subset)

`python3 -m formalization kinship genegenogeno` returns a **typed
`path_from_ego`** (rightmost link first), while
`python3 -m formalization analyze genegenogenoem` returns the
recognized productive nominal accusative. Standard noun generation and the
restricted SVO clause parser accept these derived kinship forms.

Accepted atomic links: `adel/adelo/adele`, `gen/geno/gene`, and `fil`.
Relations compose `A+B = A of B`, traversing **right-to-left**.
Numeral `NUMjer` repeats **the next complete atomic relation link**,
for example `bisjergene` = mother's mother and `adelbisjergen` =
sibling of a grandparent. This scoping rule is deliberately narrow: an
unbracketed `NUMjer` does not attempt to repeat an arbitrarily complex
compound. It supports canonical cardinal expressions for counts from
1 through 128, with a 256-character input and a 128-step expansion guard.
It never imports former proposals or historical `frat` as productive roots.

An unlisted well-formed family relation is labelled
`productive_from_confirmed`, **not** added to the confirmed lexicon.
Ambiguous or malformed segmentations fail closed; the parser returns
**relational paths, not human comprehension or full semantic inference**.
See [normative kinship](../language/kinship.md) and
[`tests/test_kinship_parser.py`](../tests/test_kinship_parser.py).

Not yet implemented: full lexical valency, focus enclitic scope, all free
relator constructions, general (non-kinship) derivational compounding, passives, optional word-order
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
