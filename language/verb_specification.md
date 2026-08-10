# Verb Specification

This document is the live specification for finite verb morphology. Historical
forms are preserved in `legacy/original-language/verb_specification.md`.

## 1. Verb roots

The bare lexical root is the dictionary form and imperative unless a lexical
entry specifies otherwise.

Examples:

- `mov` — move
- `vid` — see
- `fak` — do / make
- `dik` — say / express
- `kurar` — care / cure

## 2. Person and number

Person is encoded by a final vowel:

| Person | Vowel |
|---|---|
| first | `i` |
| second | `u` |
| third | `a` |

Plural is encoded by the nasal morphophoneme `/N/`, written `n`, **after** the
person vowel.

| Person | Singular | Plural |
|---|---|---|
| first | `i` | `in` |
| second | `u` | `un` |
| third | `a` | `an` |

Independent subject pronouns use the same forms. GlottoDelta is pro-drop when
the verbal ending makes the subject recoverable.

## 3. Canonical finite structure

Every ordinary finite verb has the fixed order:

```text
root + TAM + person vowel + optional N
```

Examples with `mov`:

| Structure | Singular | Plural |
|---|---|---|
| present | `movi`, `movu`, `mova` | `movin`, `movun`, `movan` |
| past with `d` | `movdi`, `movdu`, `movda` | `movdin`, `movdun`, `movdan` |
| future with `f` | `movfi`, `movfu`, `movfa` | `movfin`, `movfun`, `movfan` |

The ordering rule is canonical even if the inventory or semantics of individual
TAM markers are reviewed later. TAM never follows the person marker, and plural
`N` never precedes the person vowel.

## 4. Current TAM material

The inherited specification currently supplies the following TAM material:

- zero — simple/present
- `d` — past
- `f` — future
- `n` — ongoing/progressive
- `b` — completed/perfective
- `m` — potential/ability

Their **position** is confirmed by §3. Their exact semantic inventory remains
separately reviewable and should not be expanded without an explicit decision.

## 5. Participial/resultative `-it`

`-it` is the productive non-finite participial/resultative suffix:

- `dik` → `dikit` — said
- `mov` → `movit` — moved
- `vid` → `vidit` — seen
- `fak` → `fakit` — done / made

`-it` is not the abstract-quality suffix. Abstract qualities use `-itat`.

## 6. Imperative

The bare verb root serves as the ordinary imperative:

- `mov!` — move!
- `fak!` — do / make!

The negative imperative uses the free negator `no` before the root:

- `no mov!` — do not move!

## 7. Removed legacy forms

The former six-person-vowel paradigm `i/e/a/u/o/ə` is obsolete. No schwa person
marker exists. Forms such as `move`, `movə`, `faco`, and `facə` belong only to
the historical snapshot.

The old nominal plural suffix `-en` is also obsolete. It must not be inferred
from this document's historical predecessors.
