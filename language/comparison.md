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

## 12. Absolute degree modifiers (ratified 2026-10-24)

Absolute intensity is marked analytically by invariant, independent words
preceding a gradable adjective or qualitative predicate. Scale A is canonical:

| Modifier | Example | Reading |
|---|---|---|
| `minu` | `minu bel` | barely/minimally beautiful |
| `pok` | `pok bel` | slightly/a little beautiful |
| unmarked | `bel` | beautiful, unspecified degree |
| `mult` | `mult bel` | very beautiful |
| `ekstrem` | `ekstrem bel` | extremely beautiful |

`minu` is **not** `minim`: `minim bel` means the least beautiful
within a comparison set. `ekstrem bel` means extremely beautiful;
`masim bel` means the most beautiful in a comparison set, without
entailing extreme absolute beauty. Similarly `mult nebel` = very ugly,
while `no mult bel` negates 'very beautiful' without entailing ugliness.

Degree modifiers apply to the *selected qualitative predicate*, including
a semantically licensed antonym in `ne-`. They do not change comparative
or superlative meanings. Their scale is qualitative/contextual, not an
exact numerical partition. The distinction between moderate degree and threshold sufficiency is
ratified separately below.

## 13. Moderate degree and threshold sufficiency (ratified 2026-10-24)

Two invariant free modifiers precede a gradable predicate:

- `ase` — fairly / rather / moderately, asserting a moderately positive
  degree on the property scale; it does not assert that any requirement is met.
- `suf` — sufficiently / enough, asserting that the property reaches a
  contextually relevant threshold for a purpose or requirement; it does not
  assert high absolute intensity.

Examples (present-tense zero copula):

- `tik dom ase bel` — this house is fairly beautiful.
- `tik dom suf gran` — this house is large enough (for the contextual need).
- `tik dom no suf gran` — this house is not large enough.
- `tik dom ase nebel` — this house is rather ugly.

The `ase` scale position is moderate, not a mathematically fixed value.
`suf` does **not** occupy a fixed position on that scale: a modest absolute
value can be sufficient for an easy threshold, and a high value insufficient
for a demanding threshold. When the purpose is expressed, use an already
licensed purpose construction; this ratification does not create a new
purpose-marker or mandate a particular syntactic frame.

Negation remains independent: `no ase bel` denies the moderately-high degree;
`no suf gran` denies threshold satisfaction. Neither entails `nebel`
or `negran` respectively.

## 14. Purpose-qualified sufficiency (ratified 2026-10-24)

The existing purposive free relator `fin` may explicitly specify the goal
against which a quality is judged sufficient. Canonical construction:

```text
SUBJECT suf QUALITY fin PURPOSE
```

Example: `tik dom suf gran fin fak` — this house is large enough for
the purpose of making/producing something. The exact suitability threshold
is contextual; neither `suf` nor `fin` encodes a numerical value.

When the goal is implicit, `suf QUALITY` remains sufficient. The already
established `pro` denotes a beneficiary, not the purpose threshold;
`per` denotes an instrument/means, not the purpose. A quantitative
capacity requirement (e.g. sufficient for five persons) requires separate
review of numerals and measurement constructions; this rule does not
silently license a new quantitative frame.

## 15. Quantified object within an explicit purpose (approved design C, 2026-10-25)

For a sufficiency condition defined by an activity involving a number of
entities, retain the existing purpose relator `fin` and spell out the event
whose feasibility defines the threshold:

```text
SUBJECT suf QUALITY fin VERB_ROOT [NUMERAL NOUN-em]
```

The bare verb root is the dependent, non-finite lexical verb; it takes no
person/tense marking. Where that verb licenses a direct object, the object
remains accusative (`-em`) and the numeral is an invariant prenominal
modifier; no plural `wi` is needed. As a schematic example, `fin fak kin
objektem` would mean "for making five objects" **if** `objekt` is separately
adopted as a lexical root; this example is not lexical ratification.

This extends the already ratified `suf QUALITY fin PURPOSE` frame with
an explicit verb phrase. It does not assign `fin` a new meaning of "capacity
for N people" and does not reinterpret `pro` as quantitative capacity.
The exact verb for lodging/hosting people remains unratified, so a fully
canonical translation of "large enough to accommodate five people"
is pending that lexical choice.


## 16. One scalar meaning, qualitative and numerical degree (author ratification 2026-11-13; LDR-0025)

An inherently gradable property has **one** underlying lexical meaning; translations such as 'P is probable' and 'P has a degree of probability' do not warrant two roots or independently defined meanings. Invariant analytic modifiers `minu`, `pok`, `ase`, `mult`, `ekstrem` and threshold `suf` qualify the *same property*, while a numerical specification of that same scale is possible **where a meaningful and validated measurement convention exists**. No universal numerical unit is implied for nonmeasurable gradable qualities.

`lik` is a separately and explicitly **ratified** root for the gradable **probability of a finite proposition** (author approval, 2026-11-13). It is not a synonym of `pos` (logical/epistemic possibility), `deb` (necessity), `kred` (belief) or `prob` (morally upright). The bounded propositional constructions are:

- `lik uman mova` — it is probable that the person moves; no fixed 50% numerical threshold is lexicalized.
- `minu lik uman mova` — minimally probable that the person moves.
- `pok lik uman mova` — low probability of the person's movement.
- `ase lik uman mova` — moderate likelihood of the movement.
- `mult lik uman mova` — high probability of the movement.
- `ekstrem lik uman mova` — extremely high probability of the movement.
- `suf lik uman mova` — probable enough relative to the relevant decision threshold.

The modifier precedes `lik`, which takes the following complete finite Boolean proposition as its argument. A specific numeric probability may ultimately be expressed using **existing** fractions/percentages such as `kin senim` = 5%, but a scoped composition of number and `lik P` is **not yet ratified**; such sentences must not be generated as canonical grammar. Likewise no independently ratified personless `likd/likf` operator tense, nested `lik pos P`, or generic scalar comparison over two propositions is introduced by this decision. Unmodified `lik` has a context-dependent threshold for idiomatic translation only, never an automatic precise percentage cutoff.


## 17. Exact numeric degree of `lik` (author ratification 2026-11-13; LDR-0026)

The existing two-word rational-fraction construction now directly quantifies the gradable propositional probability property:

```text
[no] lik CARDINAL ORDINAL FINITE_PROPOSITION
```

Examples: `lik kin senim uman mova` = 5% for P, `lik setdek senim uman mova` = 70% for P, `lik uno bisim uman mova` = 1/2 for P. `no lik setdek senim uman mova` rejects the **70% valuation**, not P itself; `lik setdek senim uman no mova` assigns 70% to NOT-P. The ordinary `lim` immediately before a following connective closes the measured proposition: `lik setdek senim uman mova lim e vida` = 70% for movement, AND someone sees. Without `lim`, normal following Boolean coordination remains under `lik`.

**The grammar/parser MUST NOT constrain a numeric statement about probability to [0,1].** `lik bissen senim uman mova` (200%) is grammatically accepted and retained verbatim as a possible hyperbole, even though it violates ordinary mathematical probability axioms. Syntactic validity and numerical/model feasibility are separate analytical layers. No clamping or invented probabilities. The preexisting fractions allow improper forms such as `kin terim` (5/3); the parser preserves their numerator, denominator and surface form.

Quantitative and qualitative degrees modify the **same** `lik` property, but their **simultaneous syntactic combination** has not been settled. Existing standalone forms `pok lik P`, `mult lik P`, etc. remain valid. General-purpose approximation, range and bound syntax is reserved for an independent language-wide decision; do not invent special-purpose probability terms for them.


## 18. Universal quantitative comparisons, approximation and intervals (ratified 2026-11-13; LDR-0027)

The **same** existing comparative operators receive a quantitative-value frame, without changing adjective comparisons `major ADJ dan B`:

```text
ekwal N      (= N)
major N      (> N)
minor N      (< N)
no minor N   (>= N)
no major N   (<= N)
no ekwal N   (!= N)
sirka N      (approximately N)
inter A e B  (between A and B)
```

`sirka` and `inter` are newly ratified roots. `no` modifies the **numeric comparison**, not the surrounding clause. `sirka` has contextual tolerance, not automatically epistemic uncertainty. For `inter`, the `e` between endpoints is an **internal numeric connector**, not proposition coordination; endpoint inclusivity is contextual by default. For precise bounds compose `major/minor/no minor/no major` where those values are measured. The parser preserves numeric claims, including hyperbolic values, without imposing property-specific mathematical ranges.

These constructions can quantify nominal counts (`sirka setdek uman` = approximately seventy people, `inter sesdek e setdek uman` = between sixty and seventy people) and existing scalar probabilities (`lik sirka setdek senim uman mova` = approximately 70% probability of movement; `lik no minor setdek senim uman mova` = at least 70%). Reuse the canonical numeral and fraction grammar; no new percentage or unit morpheme. Restricted parser implementations are not universal licenses for unspecified measurement units, decimals or compound interval calculations.
