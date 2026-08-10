# Noun Case System

The case system marks the grammatical role of a noun phrase at its right edge.
The immutable historical version is preserved under
`legacy/original-language/noun_case_system.md`.

## 1. Case inventory

### Base cases

| Suffix | Function | Meaning |
|---|---|---|
| Ø | nominative / base | subject, dictionary form |
| `-em` | accusative | direct object |
| `-s` / `-es` | genitive | possessive / of |
| `-de` | ablative | from / source / origin |
| `-ad` | allative / dative | to / toward / recipient |
| `-in` | locative | in / at / location |
| `-ko` | comitative | with / together with |

### Extended cases retained from the original specification

| Suffix | Function | Meaning |
|---|---|---|
| `-per` | instrumental / perlative | through / by means of |
| `-pro` | benefactive | for the benefit of |
| `-due` | causal | because of / due to |
| `-fin` | purposive | for the purpose of |
| `-tem` | temporal | at / during |
| `-mod` | modal / manner | in the manner of |

## 2. Nominative and accusative

The nominative is the unmarked base form. The accusative `-em` marks an explicit
direct object.

- `uman vida` — the person sees
- `uman vida domem` — the person sees the house

## 3. Attachment

The case suffix appears once at the right edge of the noun phrase. Modifiers do
not agree in case.

Nominal plurality is not a suffix. The optional particle `wi` precedes the noun
phrase:

- `wi domem` — houses as direct object, explicitly plural
- `tik wi domem` — these houses as direct object

A numeral or quantity-encoding quantifier normally makes `wi` unnecessary:

- `ter domem` — three houses as direct object

## 4. Genitive `-s / -es`

The genitive is `-s` by default. Use `-es` after a stem whose right edge is
sibilant or may coalesce to a sibilant/affricate realization that makes direct
`-s` attachment difficult.

Canonical trigger set:

```text
-s  -z  -sj  -tj  -dj
```

A stem in `-ts` is already covered because its final canonical segment is /s/.
Plain final `j=/j/` does **not** trigger `-es`.

Examples:

- `dom` → `doms`
- `fak` → `faks`
- `vis` → `vises`
- `spets` → `spetses`

## 5. Personal possessives

Personal possessives are simply genitive pronouns:

| Person | Pronoun | Possessive |
|---|---|---|
| 1sg | `i` | `is` |
| 2sg | `u` | `us` |
| 3sg | `a` | `as` |
| 1pl | `in` | `ins` |
| 2pl | `un` | `uns` |
| 3pl | `an` | `ans` |

Optional referential specificity remains inside the pronoun before genitive
`-s`: `ao→aos`, `ae→aes`, `ano→anos`, `ane→anes`.

## 6. Analytic alternatives

Where the lexicon provides an equivalent free relation word, analytic phrasing
may coexist with the compact suffix. The suffix system remains the canonical
case morphology.
