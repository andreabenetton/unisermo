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
root + time + aspect + person vowel + optional N
```

The time and aspect slots are distinct. A finite verb contains at most one time
marker and at most one aspect marker.

Examples with `mov`:

| Structure | Singular | Plural |
|---|---|---|
| present | `movi`, `movu`, `mova` | `movin`, `movun`, `movan` |
| past with `d` | `movdi`, `movdu`, `movda` | `movdin`, `movdun`, `movdan` |
| future with `f` | `movfi`, `movfu`, `movfa` | `movfin`, `movfun`, `movfan` |

The ordering rule is canonical even if the inventory or semantics of individual
TAM markers are reviewed later. TAM never follows the person marker, and plural
`N` never precedes the person vowel.

## 4. Canonical 3×3 tense-aspect system

Finite inflection distinguishes three times and three aspects.

### 4.1 Time slot

- zero — present / temporally unmarked simple present
- `d` — past
- `f` — future

### 4.2 Aspect slot

- zero — simple
- `n` — ongoing / progressive
- `b` — completed / perfect

Time precedes aspect. The nine regular combinations are therefore:

| Time / Aspect | Simple | Progressive | Completed / perfect |
|---|---|---|---|
| present | `Ø` | `n` | `b` |
| past | `d` | `dn` | `db` |
| future | `f` | `fn` | `fb` |

Examples with `dik` in first-person singular:

- `diki` — I say
- `dikni` — I am saying
- `dikbi` — I have said / the saying is completed
- `dikdi` — I said
- `dikdni` — I was saying
- `dikdbi` — I had said
- `dikfi` — I will say
- `dikfni` — I will be saying
- `dikfbi` — I will have said

The former synthetic marker `m` for ability/potential is retired from the TAM
paradigm. Ability, obligation, volition, learned capacity and related modal or
servile meanings are expressed by an ordinary finite servile verb followed by
the bare infinitive/root of the lexical verb. The servile verb carries time,
aspect, person and number; the dependent infinitive remains uninflected.

Schematic examples (the lexical roots for individual servile meanings are
decided separately):

```text
[SERVILE]-i dik      = I can/must/want/know-how-to say
[SERVILE]-di dik     = I could/had-to/wanted/knew-how-to say
[SERVILE]-fin dik    = we will be able/obliged/willing to say
```

This construction is productive: no special synthetic suffix is added to the
lexical verb for modal meanings.

## 5. Participial/resultative `-it`

`-it` is the productive non-finite participial/resultative suffix:

- `dik` → `dikit` — said
- `mov` → `movit` — moved
- `vid` → `vidit` — seen
- `fak` → `fakit` — done / made

`-it` is not the abstract-quality suffix. Abstract qualities use `-itat`.

A participial/resultative form may also function directly as a noun without an
extra nominalizer. In nominal use it denotes a result or resulting entity and
follows ordinary noun grammar:

- `fakit` — fact / thing done, number unspecified
- `wi fakit` — facts / things done, explicitly plural
- `duo fakit` — two facts / two things done

No plural suffix is added to `-it`; `wi` is omitted when a numeral or quantifier
already expresses quantity. Passive-clause syntax is specified separately.

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
