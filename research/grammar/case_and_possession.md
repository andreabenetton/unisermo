# Genitive and personal possession

> **Status:** confirmed design decision. This specification is canonical for
> the genitive allomorph and the personal possessive forms.

## 1. Genitive suffix

The genitive is a suffix with two surface forms:

- `-s` by default;
- `-es` after a stem whose right edge is sibilant or may coalesce to a
  sibilant/affricate realization that would make direct `-s` attachment hard to
  perceive or pronounce.

The canonical trigger set is:

`-s, -z, -sj, -tj, -dj`

A stem in `-ts` is already covered by the `-s` trigger because its final
canonical segment is /s/.

Examples:

- `dom` -> `doms`
- `fak` -> `faks`
- `vis` -> `vises`
- a stem in `-z` -> `...zes`
- a stem in `-ts` -> `...tses`
- a stem in `-sj` -> `...sjes`, including accents with `[ʃ]`
- a stem in `-tj` -> `...tjes`, including accents with `[tʃ]`
- a stem in `-dj` -> `...djes`, including accents with `[dʒ]`

The letter `j` by itself is the glide /j/ and is **not** a trigger for `-es`.
Thus a plain stem in `-j` takes regular `-s` unless another independent
phonotactic rule is later established.

This preserves the useful old `-s / -es` architecture while updating its
conditioning to the current phoneme inventory. Removed unitary `sh`, `c`, and
old affricate `j` are not referenced by the rule.

## 2. Personal possessives are genitive pronouns

GlottoDelta does not need a separate possessive-pronoun paradigm. Personal
possessives are formed productively by applying the genitive suffix to the
personal pronoun forms.

| Person | Pronoun | Possessive/genitive | Meaning |
|---|---|---|---|
| 1 singular | `i` | `is` | my / mine |
| 2 singular | `u` | `us` | your / yours (singular) |
| 3 singular | `a` | `as` | their/his/her/its, neutral by default |
| 1 plural | `in` | `ins` | our / ours |
| 2 plural | `un` | `uns` | your / yours (plural) |
| 3 plural | `an` | `ans` | their / theirs |

These forms are invariant and do not agree with the possessed noun.

## 3. Optional referential specificity

The already-confirmed optional referential-specificity markers remain part of
the pronoun before genitive `-s` is added. For third person, for example:

- `ao` -> `aos` — his / of that male referent
- `ae` -> `aes` — hers / of that female referent
- `ano` -> `anos` — theirs, explicitly male group/reference
- `ane` -> `anes` — theirs, explicitly female group/reference

The neutral possessives `as` and `ans` always remain valid. No grammatical
gender agreement is introduced.
