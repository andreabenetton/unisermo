# Noun Case System

The case system keeps only a small synthetic core. More specific semantic
relations are expressed by invariant free relators before the noun phrase.
The immutable historical version is preserved under
`legacy/original-language/noun_case_system.md`.

## 1. Canonical synthetic case inventory

The synthetic case inventory is closed to six values:

| Suffix | Function | Meaning |
|---|---|---|
| Ø | nominative / base | subject, dictionary form |
| `-em` | accusative | direct object |
| `-s` / `-es` | genitive | possessive / of |
| `-ad` | dative / allative | to / toward / recipient |
| `-de` | ablative | from / source / origin |
| `-in` | locative | in / at / location |

The former comitative suffix `-ko` is retired. The former extended case
suffixes `-per`, `-pro`, `-due`, `-fin`, `-tem`, and `-mod` are also retired as
case morphology.

## 2. Nominative and accusative

The nominative/base form is unmarked. The accusative `-em` marks an explicit
direct object.

- `uman vida` - the person sees
- `uman vida domem` - the person sees the house

## 3. Dative/allative, ablative, and locative

The remaining spatial/argument cases are compact suffixes on the head noun:

- `umanad` - to/toward the person; to the person as recipient
- `domde` - from the house
- `domin` - in/at the house

These suffixes express the core relation directly; no additional free relator
is required.

The same source/destination opposition is used for explicit state transitions:
`traes DEST-ad SOURCE-de`, e.g. `traes solidad likwidde` "pass from liquid to
solid". Here `-ad` marks the destination state and `-de` the source state.

## 4. Case attachment and noun-phrase structure

A synthetic case suffix attaches to the **head noun**. In the canonical noun
phrase, modifiers precede the head noun, so the case suffix normally also
appears at the right edge of the phrase. Modifiers do not agree in case.

Nominal plurality is not a suffix. The optional particle `wi` precedes the noun
phrase:

- `wi domem` - houses as direct object, explicitly plural
- `tik wi domem` - these houses as direct object

A numeral or quantity-encoding quantifier normally makes `wi` unnecessary:

- `ter domem` - three houses as direct object

The same attachment rule applies to the other synthetic cases:

- `tik umanad` - to this person
- `wi umande` - from people, explicitly plural
- `duo domin` - in two houses

## 5. Genitive `-s / -es`

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

- `dom` -> `doms`
- `fak` -> `faks`
- `vis` -> `vises`
- `spets` -> `spetses`

## 6. Personal possessives

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
`-s`: `ao->aos`, `ae->aes`, `ano->anos`, `ane->anes`.

## 7. Free relational words

Relations that do not belong to the six-case synthetic core are expressed
analytically. The relator precedes an ordinary noun phrase and is invariant:

```text
RELATOR + NOUN PHRASE
```

Canonical relators inherited or revised from the earlier case system are:

| Relator | Function | Meaning |
|---|---|---|
| `kun` | comitative | with / together with |
| `per` | instrumental / perlative | through / by means of |
| `pro` | benefactive | for the benefit of |
| `due` | causal | because of / due to |
| `fin` | purposive | for the purpose of |
| `tem` | temporal | at / during |
| `mod` | manner | in the manner of |

Examples:

- `kun uman` - with a person
- `kun tik uman` - with this person
- `kun wi uman` - with people
- `per dom` - through/by means of the house
- `pro uman` - for the benefit of a person
- `due fakit` - because of what was done / because of the fact
- `fin fak` - for the purpose of doing/making
- `tem dia` - during the day
- `mod uman` - in the manner of a person

The complement of a free relator is normally in the base form because the
relator itself expresses the semantic relation. Synthetic case is not duplicated
merely to repeat the same relation.

## 8. Design principle

Synthetic case is reserved for a small, frequent grammatical core. More
specific semantic relations remain transparent free words. This avoids a long
case paradigm while preserving compact marking for direct objects, possession,
recipients/direction, source, and location.
