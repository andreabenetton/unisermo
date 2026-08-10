# Copula `es`

> **Status:** confirmed design decision. This specification updates the copula
> to the current `i/u/a + N` person-number system.

## 1. Root and function

The copula root remains `es`, with the meanings **be / exist**. It is a regular
verb root for person and number.

The present simple may retain zero copula for ordinary adjectival, nominal, and
locative predicates. The explicit copula is available for emphasis and is used
when an overt verbal carrier is needed, including existential use and tensed or
aspectual/modal forms.

## 2. Present person-number paradigm

The finite copula uses the confirmed person vowels `i/u/a`, followed by plural
`N` written `n`.

| Person | Form |
|---|---|
| 1 singular | `esi` |
| 2 singular | `esu` |
| 3 singular | `esa` |
| 1 plural | `esin` |
| 2 plural | `esun` |
| 3 plural | `esan` |

No schwa form exists.

Examples:

- `i esi` — I am, when the copula is expressed
- `u esu` — you are
- `a esa` — he/she/it is, neutral third singular reference
- `in esin` — we are
- `un esun` — you are, plural
- `an esan` — they are

## 3. Interaction with canonical TAM

`es` follows the same finite architecture as every other verb:

```text
root + aspect + time + person vowel + optional N
```

Simple past and future remain:

| Person | Past | Future |
|---|---|---|
| 1 singular | `esdi` | `esfi` |
| 2 singular | `esdu` | `esfu` |
| 3 singular | `esda` | `esfa` |
| 1 plural | `esdin` | `esfin` |
| 2 plural | `esdun` | `esfun` |
| 3 plural | `esdan` | `esfan` |

The canonical aspect vowels occur before time just as with lexical verbs. First-person singular examples are:

- `esei` — present progressive
- `esoi` — present completed/perfect
- `esedi` — past progressive
- `esodi` — past completed/perfect
- `esefi` — future progressive
- `esofi` — future completed/perfect

Present aspect-person vowel adjacency is canonical hiatus, so `esei` is parsed as `es-e-i`, not as a merged simple form.

## 4. Zero copula

In present-simple adjectival, nominal, and locative predicates, zero copula
remains the compact default when no overt verb is required.

- `dom bon` — the house is good
- `uman doktor` — the person is a doctor

When the copula is needed explicitly, the current person-number form is used:

- `dom esa bon` — the house is good, explicit/emphatic
- `wi dom esan bon` — the houses are good, explicit plural subject

Because nominal number is now optionally marked with `wi`, the old nominal
plural suffix `-en` is not part of the copula system.

## 5. State-phase family built on `es`

The copular/existential root `es` is also the base of a canonical family of
state-phase verbs. These are fused written forms with no hyphen:

| Form | Analysis | Core meaning |
|---|---|---|
| `es` | `es` | be / exist / hold state X |
| `ines` | `in-` + `es` | remain / continue to be X |
| `ades` | `ad-` + `es` | become X / enter state X |
| `dees` | `de-` + `es` | cease to be X / leave state X |
| `rees` | `re-` + `es` | return to being X / become X again |

The contrasts are semantic, not stylistic. `es X` simply predicates X;
`ines X` adds persistence; `ades X` marks entry into X; `dees X` marks exit
from X without implying entry into the lexical opposite; and `rees X` marks
restoration of a previously held state.

Examples with a qualitative predicate `san` "healthy":

- `es san` — be healthy
- `ines san` — remain / stay healthy
- `ades san` — become healthy
- `dees san` — cease to be healthy
- `rees san` — become healthy again / recover

`ades` is deliberately distinct from `aes`, which is already the canonical
genitive/possessive form of the specific third-person pronoun `ae`.

These prefixed forms are ordinary verbal roots for finite TAM and person-number
inflection. The prefixes themselves do not replace the finite aspect system.

## 6. Explicit state transition with `traes`

The canonical verb `traes` expresses an explicit transition between two
predicative states, roles, classes, or conditions. It is distinct from simple
`ades`: `ades X` only asserts entry into X, while `traes` profiles both the
source and the destination of the transition.

Canonical frame:

```text
traes DEST-ad SOURCE-de
```

The destination takes the existing dative/allative `-ad`; the source takes the
existing ablative `-de`. No new transition case or free relator is introduced.

Examples:

- `traes solidad likwidde` — pass from liquid to solid
- `traes doktorad studentde` — pass from student to doctor
- `ades solid` — become solid, with no source state asserted

`traes` is an ordinary verbal root for finite TAM and person-number inflection.
The case-marked state expressions remain nominal/predicative complements; their
case marking identifies destination and source.

## 7. Causative transformation with `traes` and resultative `-da`

`traes` also has a canonical transitive causative frame for an agent or cause
that transforms an explicit object into a resulting state, role, class, or
property:

```text
Y-NOM traes X-em RESULT-da
```

The causer Y is nominative/base, the transformed entity X is accusative `-em`,
and the resulting predicative complement takes resultative/transformative
`-da`.

Examples:

- `Y traes akvaem solidda` — Y makes/transforms the water solid
- `Y traes umanem doktorda` — Y makes/transforms/trains the person into a doctor

This frame is distinct from both `ades X` and the intransitive two-pole frame
`traes DEST-ad SOURCE-de`. The three constructions therefore encode:

- `ades solid` — become solid; source unspecified
- `traes solidad likwidde` — pass from liquid to solid
- `Y traes akvaem solidda` — Y transforms the water, making it solid

`-da` marks the **resulting predicate of the transformed object**; it is not an
ordinary copular predicate marker and does not replace `-ad` or `-de`.
