# Noun Case System

The case system keeps only a small synthetic core. More specific semantic
relations are expressed by invariant free relators before the noun phrase.
The immutable historical version is preserved under
`legacy/original-language/noun_case_system.md`.

## 1. Canonical synthetic case inventory

The synthetic case inventory is closed to seven values:

| Suffix | Function | Meaning |
|---|---|---|
| Ø | nominative / base | subject, dictionary form |
| `-em` | accusative | direct object |
| `-s` / `-es` | genitive | possessive / of |
| `-ad` | dative / allative | to / toward / recipient |
| `-de` | ablative | from / source / origin |
| `-in` | locative | in / at / location |
| `-da` | resultative predicative / transformative | as / into the resulting state or role |

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

## 4. Resultative predicative / transformative `-da`

The suffix `-da` marks a state, role, class, or property assigned as the **result**
of a transformation to an explicit object. Its canonical causative-transition frame is:

```text
Y-NOM traes X-em RESULT-da
```

Here Y is the causer/transformer in the nominative/base form, X is the entity
undergoing transformation in accusative `-em`, and `RESULT-da` is the resulting
predicative complement.

Examples:

- `Y traes akwaem solidda` - Y transforms the water, making it solid
- `Y traes umanem doktorda` - Y transforms/trains the person into a doctor

`-da` is not an allative destination. Compare `solidad` "toward/to the solid
state" in the two-pole intransitive transition `traes solidad likwidde` with
`solidda` "as/resulting solid" in the causative frame. It is also not used for
ordinary copular predication: plain `X solid` or explicit `X esa solid` remains
the normal way to say that X is solid.

## 5. Case attachment and noun-phrase structure

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
- `bis domin` - in two houses

## 6. Genitive `-s / -es`

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

## 7. Personal possessives

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

## 8. Free relational words

Relations that do not belong to the seven-case synthetic core are expressed
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

## 9. Design principle

Synthetic case is reserved for a small, frequent grammatical core. More
specific semantic relations remain transparent free words. This avoids a long
case paradigm while preserving compact marking for direct objects, possession,
recipients/direction, source, location, and resultative predication.

## Purpose relator with sufficiency (ratified 2026-10-24)

The existing free relator `fin` can follow a `suf + qualitative predicate`
construction to introduce the specific purpose that determines the sufficiency
threshold: `SUBJECT suf QUALITY fin PURPOSE`.
For example, `tik dom suf gran fin fak` means that this house is large
enough for making/producing something. `pro` remains benefactive and `per`
remains instrumental; neither automatically replaces `fin`.
Numerical capacity thresholds are a distinct, still-open construction.

## Purposive verb phrases with quantified objects (approved design C, 2026-10-25)

After `suf QUALITY`, `fin` may introduce an explicit verbal purpose:
`fin VERB_ROOT [NUMERAL NOUN-em]`. The verb root is uninflected, matching
the language's existing bare dependent infinitive usage. A transitive
purpose verb governs its direct object in `-em`; cardinal numerals precede
number-neutral nouns without obligatory `wi`.

This allows the sufficiency threshold to depend on a quantified activity
rather than adding a new meaning to `fin` or `pro`. A lexical verb for
"to host/accommodate" must be ratified before providing a canonical house
capacity example with `kin umanem`.

## Causal clauses introduced by `due` (ratified 24 October 2026)

The already confirmed free relator `due` ('because of', introducing a nominal phrase) **also introduces a complete causal proposition** ('because', 'since'). Both orders are accepted:

- `P due Q` — P because Q (effect first; Q is the cause).
- `due Q, P` — Since Q, P (cause first; P is the effect).

This is not the same construction as `Q, ergo P` ('Q, therefore P'): `ergo` explicitly introduces an inference/conclusion rather than labeling the subordinate proposition as a cause. Interrogative `ker` remains WHY. No separate causal connector `kar` is introduced. A parser must preserve which clause is cause and which is effect, and distinguish `due + NP` from `due + finite clause`; punctuation and nested-clause rules beyond the simple examples require further specification.


## Factual cause versus evidential justification — required distinction (24 October 2026)

The author requires two separate grammatical treatments for a *real-world causal relation* (one circumstance brings about or contributes to an effect) and a *speaker's reason/evidence for asserting a proposition* (an observation supports an inference without causing the inferred event). `due` is the confirmed **factual causal** linker; the distinct evidential/argumentative linker is now **ratified as `nam`** (Latin-derived). `P nam Q` presents Q as a reason/evidence supplied by the speaker for asserting P, without asserting that Q caused P or that Q is true, sufficient, or a valid proof. `due` retains factual causality. Existing `ergo` introduces an inference/conclusion in `Q ergo P`, whereas `P nam Q` foregrounds the assertion before its justification. Do not silently parse evidence/support as `due` causation.
