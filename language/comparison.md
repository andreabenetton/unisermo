# Comparison and Superlative

A formal specification of comparison constructions in the synthetic language: comparative of majority, comparative of minority, superlative maximum, superlative minimum, and equality. The system uses six dedicated function words.

## Related documents

- Adjectives appear unchanged in every comparison construction (no comparative or superlative inflection); placement and no-agreement rule in [`adjectives.md`](adjectives.md).
- Comparison sentences obey the zero-copula present rule (e.g. `tik dom major gran dan tan dom`); for past, future, aspect, or modality, the copula `es` is inserted in the usual way — see [`copula.md`](copula.md).
- The demonstratives `tik` (this) and `tan` (that, far) used in the examples below are in [`demonstratives.md`](demonstratives.md).
- Negation follows the rule in [`negation.md`](negation.md).

This document introduces **six new function words**: `major`, `minor`, `masim`, `minim`, `dan`, `ekwal`.

---

## 1. Design Goal

- **Compactness.** Each comparison type has a single dedicated function word.
- **Recognizability.** Forms are adapted from internationally recognized roots (Latin / Romance / English *major*, *minor*, *max*, *min*, *equal*, *than*).
- **Regularity.** A single marker `dan` introduces the second term in every "than / as / compared with" construction, whether equal or unequal.
- **No inflection on adjectives.** The adjective itself never changes form; comparison is expressed entirely by the function words.

---

## 2. Inventory

| Function | Form | Meaning | Pronunciation |
|---|---|---|---|
| Comparative of majority | `major` | more / -er | /ma.jor/ |
| Comparative of minority | `minor` | less | /minor/ |
| Superlative maximum | `masim` | most / -est | /masim/ |
| Superlative minimum | `minim` | least | /minim/ |
| Comparison marker | `dan` | than / compared with / as | /dan/ |
| Equality | `ekwal` | as / equally | /e.kwal/ |

**Note on `ekwal`.** Canonical `w=/w/` is available, so the international /kw/ sequence is represented transparently as `kw`: `ekwal` = /e.kwal/.

---

## 3. Comparative of Majority

Pattern:

```
A  major  ADJ  dan  B
```

Example:

```
tik dom major gran dan tan dom
= this house is bigger than that house
```

The structure is: subject + `major` + adjective + `dan` + second term.

---

## 4. Comparative of Minority

Pattern:

```
A  minor  ADJ  dan  B
```

Example:

```
i minor vel dan u
= I am less fast than you
```

---

## 5. Superlative Maximum

Pattern:

```
A  masim  ADJ
```

Example:

```
tik dom masim gran
= this house is the biggest
```

No `dan` is used, because there is no overt second term — the comparison is implicit (against the relevant set of alternatives in context).

---

## 6. Superlative Minimum

Pattern:

```
A  minim  ADJ
```

Example:

```
tik dom minim vel
= this one is the least fast
```

---

## 7. Equality

Pattern:

```
A  ekwal  ADJ  dan  B
```

Example:

```
i ekwal vel dan u
= I am as fast as you
```

Here `dan` introduces the second term of an equality comparison — equivalent to English "as ... as".

---

## 8. The Role of `dan`

`dan` is the **general second-term marker** in every comparison that has an overt second term:

- After `major` or `minor`, `dan` corresponds to English "than".
- After `ekwal`, `dan` corresponds to English "as" in the "as ... as" construction.

This unifies all comparison constructions under a single second-term marker. The form is the same regardless of whether the comparison is one of inequality or equality.

The superlatives (`masim`, `minim`) do not take `dan`, because they do not compare against a specific second term.

---

## 9. Interaction with Other Constructions

Comparison sentences follow all the usual rules of the language; the comparison words slot into a normal clause without changing anything else.

**Zero copula in the present simple** (see [`copula.md`](copula.md)):

```
tik dom major gran dan tan dom
= this house is bigger than that house
```

No copula appears because the predicate is a comparative construction in the present.

**Copula required for past, future, aspect, or modality:**

```
tik dom esda major gran dan tan dom
= this house was bigger than that house

tik dom esfa major gran dan tan dom
= this house will be bigger than that house
```

**Negation** (see [`negation.md`](negation.md)) — `no` immediately before the comparison expression in the zero-copula present, or immediately before the copula when one is present:

```
tik dom no major gran dan tan dom
= this house is not bigger than that house

tik dom no esda major gran dan tan dom
= this house was not bigger than that house
```

**Adjective remains invariant** (see [`adjectives.md`](adjectives.md)): `gran` and `vel` do not inflect for the comparison; the function words carry the entire grammatical load.

---

## 10. Summary

| Word | Function |
|---|---|
| `major` | comparative — more / -er |
| `minor` | comparative — less |
| `masim` | superlative — most / -est |
| `minim` | superlative — least |
| `dan` | comparison marker (than / as) |
| `ekwal` | equal / equally / as |

Patterns:

- **A `major` ADJ `dan` B** — A is more ADJ than B
- **A `minor` ADJ `dan` B** — A is less ADJ than B
- **A `masim` ADJ** — A is the most ADJ
- **A `minim` ADJ** — A is the least ADJ
- **A `ekwal` ADJ `dan` B** — A is as ADJ as B

The system is compact (six words cover the full comparison space), internationally recognizable (every word is adapted from a familiar Latin / Romance / English source), and regular (no adjective inflection, single second-term marker).

## 11. Ratified separation: comparison versus absolute intensity (2026-10-24)

The relative superlatives are `masim` (most) and `minim` (least), a symmetric
pair. Historical `minus` is retired from its superlative-minimum role.
Comparatives remain `major` and `minor`; equality remains `ekwal`.

`masim ADJ` means the highest degree within the contextually relevant
comparison set, not necessarily a very high absolute degree. Likewise,
`minim ADJ` is the lowest within that set, not necessarily a low absolute
degree. A comparative without an overt `dan` complement is not automatically
a superlative: its comparator may simply be implicit.

Absolute intensity is expressed separately using degree modifiers. No
particular new degree word is ratified by this decision. In particular,
`super-` is **not** an absolute-superlative operator on adjectives; historical
`super-` remains available for other established derivational uses but does
not replace `masim` and does not mean `-est`.
