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
| `-in` | locative | in / at / within a physical or abstract domain |
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

### Event-interval containment and equality (author ratification, 2026-11-13)

The existing `tem` remains an invariant prenominal temporal relator in established expressions such as `tem dia` ("during the day"). **When two bounded, positive-duration event intervals are explicitly related**, its approved event–event semantics is **strict temporal containment**: for event intervals A=[a0,a1] and B=[b0,b1], `A tem B` means `b0 < a0 < a1 < b1`. A touching or shared endpoint does not count as `tem` in this typed use. This semantic decision does **not** by itself license an arbitrary pair of finite clauses as a syntactic construction; clausal attachment and scope require a separate parser/grammar specification.

**New approved temporal relation `simtem` (author replacement ratified 2026-11-14; supersedes `temekwal`):** `A simtem B` means the **time intervals** coincide exactly: `a0 = b0` and `a1 = b1`. It does *not* assert that A and B are the same event, have the same cause, or have the same participants. `simtem` is a whole lexicalized temporal relation using familiar `tem` + `ekwal`, **not** a newly productive compounding rule. Existing `ekwal` retains general equality/comparison meanings, without implicit event-time interpretation.

**Additional ratification (2026-11-14): six directional temporal interval relations.** For two positive-duration bounded events A=[a0,a1] and B=[b0,b1], the following words are now confirmed. Their distinct semantics are exhaustive together with `tem` and `simtem` and converse argument order:

| Relation | Exact bounded-interval semantics |
| --- | --- |
| `A pretem B` | a1 < b0 (strictly before) |
| `A postem B` | b1 < a0 (strictly after) |
| `A sim B` | a1 = b0 (A meets B; *not* general simultaneity) |
| `A solap B` | a0 < b0 < a1 < b1 (directed partial overlap) |
| `A simpre B` | a0 = b0 and a1 < b1 (shared start, A finishes earlier) |
| `A simpost B` | b0 < a0 and a1 = b1 (shared finish, A starts later) |
| `A tem B` | b0 < a0 and a1 < b1 (strict containment; ratified earlier) |
| `A simtem B` | a0 = b0 and a1 = b1 (coextensive intervals, not identical events; ratified earlier) |

The inverses of `sim`, `solap`, `simpre`, `simpost`, and `tem` are expressed by **reversing A and B**; `postem` is the independently ratified converse of `pretem`. These are **lexicalized functional words**, not evidence that free `sim-`, `pre-`, or `pos-` may automatically derive any functional word. The user rejected endpoint concatenation. For full finite propositions, clause boundary and precedence remain to be specified; do not interpret schematic A and B as proof of parser implementation. `tem dia` retains the nominal time-frame meaning, distinct from strict **event-interval versus event-interval** containment.

### Instants and contextual temporal immediacy (author ratification 2026-11-14)

- **`instan` (noun):** one durationless temporal point (`t`), distinct from a brief interval. It can name an endpoint conceptually, but a point `t` cannot be supplied as a zero-duration Allen event interval; the 13 proper interval relations require `start < end`. Point-to-interval temporal semantics is a separate future decision.
- **`imedi` (temporal modifier):** no contextually significant delay. A small strictly positive gap may exist; this is **not** the mathematical endpoint equality expressed by directed `sim`.
- **`A imedi postem B`**: the bounded event A begins strictly after the end of B, and the intervening delay is contextually negligible (`end(B) < start(A)`). **`A imedi pretem B`**: A ends strictly before B begins with contextually negligible delay (`end(A) < start(B)`). The context supplies a qualitative tolerance, *not* a canonical unit or fixed numerical threshold.
- The two collocations are authorized as a simple event–event modifier immediately preceding `postem` or `pretem`. This does not authorize a free `imedi` adverb, `imedi sim`, arbitrary modifiers, a special instant interval, or automatic application to nominal time expressions. The already ratified construction `A sim B` remains *exact endpoint contact*, not "a tiny time later".

The original Italian target **«Subito dopo la telefonata mi hanno chiamato»** needs a nominal-event reference to the call as well as a finite predicate and an overt temporal attachment. The bare interval schematic `A imedi postem B` alone is **not** a verified full translation of this sentence; noun-to-event binding, argument roles, and nominal temporal frames need independent checks.

Both formulas use A and B as **semantic placeholders**, not verified Unisermo utterances. The narrow event–event interpretation does not silently replace ordinary nominal `tem` with a claim about strict endpoint inequality for point-time nouns. Point events, unbounded/habitual/modal/negated events and finite-proposition connective syntax remain under design. The seven-family design and 13-case Allen matrix have now been lexically ratified; however, clause-level surface syntax, parser implementation, and unbounded/point-event semantics remain outside this decision.

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

## Part-whole relation (ratified 2026-10-25)

`part` is the noun for part/component of a larger whole, including abstract,
structural, and informational wholes. Use existing genitive `-s/-es` to
name the whole: `part doms` = part of the house; `kin part doms` = five
parts of the house. No new case is introduced, and numerals do not require
nominal plural `wi`. This does not assert physical containment or cognition.

## Associative bound prefix versus comitative free relator (ratified 2026-10-25)

Free `kun NOUN_PHRASE` introduces an associate/accompaniment as a
relational complement. Bound `kun-` is an event-modifying derivational
prefix ('jointly/together'), not a replacement for a participant phrase.
`kunten` is a specialized lexical compound meaning physical containment;
it does not mean abstract inclusion by default. The historical associative prefix `ko-` is retired in favor of the
productive bound `kun-` (ratified 2026-10-25). The old nominal
comitative suffix `-ko` remains retired separately.

## Source of permission with `-de` (author ratification 2026-11-12)

The existing ablative `-de` means source/origin; it may therefore
express the **granting source** of the servile permission verb `aut`,
without a new case or relator. The **canonical unmarked valency frame**
is `AUT-FINITE [SOURCE-NP-de] VERB-ROOT`, where the optional source
phrase immediately follows `aut` and precedes the uninflected action.
See [verb_specification.md](verb_specification.md) for scope and
negation. Thus `auti umande mov` is "I am permitted by a person
to move", whereas in `auti umande mov domde` the first ablative
(`umande`) is permission source, and the later `domde` is the
origin of the movement. The latter is an example of two **different
argument relations**, not two meanings conflated into one case.

This rule is specifically a lexical valency construction for `aut`.
The ablative remains "from/source/origin" elsewhere. This does
**not** create a universally productive "authority-source" meaning
for every `-de` phrase, nor does it decide how to mark an abstract
regulatory or social domain with `-in`; that is a separate question.

## Abstract-domain extension of locative `-in` (ratified 2026-11-12)

The **same existing locative case `-in`** expresses *in/at/within a
domain of reference*, whether the domain is physical or abstract. No
additional case, suffix, or compulsory new free relator is introduced.
The licensed semantic classes include **physical space**, **normative
rules**, **institutional frameworks**, **academic/technical disciplines**,
**software/computational environments**, and **simulated or fictional
worlds**. This is a productive semantic extension of one case, not a
lexical synonym for `due`, `fin`, `tem`, `mod`, `per` or `-de`.

The distinction to preserve is the **syntactic level of attachment**:

1. **Event/predicate adjunct:** a `LOCATION-NP-in` within a simple
   predicate supplies the location or local domain of *the event*.
   Canonical ordinary example: `movi domin` = I move in the house.
2. **Proposition-level domain frame:** an abstract `DOMAIN-NP-in`
   is a **left-peripheral adjunct of an entire simple proposition P**,
   constraining the frame in which P is asserted, assessed or valid.
   Canonical unmarked schema is `[DOMAIN-NP-in] [SIMPLE PROPOSITION P]`
   with the domain phrase **before the subject**, if explicit, or
   **before the finite predicate**, if pro-drop applies. It scopes over
   that one whole simple proposition, including its local negation
   and ordinary predicate dependents; the domain phrase is not itself
   negated simply because a predicate is negated.

Schematic examples below use uppercase placeholders **only for
unratified nominal roots**, not newly approved Unisermo lexemes:

- `[NORMA]-in auti umande mov` = within the framework of that norm,
  I am permitted by a person to move (domain = NORMA, grant source =
  `uman-de`).
- `[NORMA]-in no auti umande mov` = under that norm, I lack permission
  from that person to move; the `no` negates `aut`, not the domain.
- `[SISTEMA]-in faki` = I act/make something within that system,
  as evaluated in its system context; the root `fak` is already
  canonical and `[SISTEMA]` is a semantic placeholder.
- `[SIMULAZIONE]-in movi` = within that simulation, I move (this
  does **not** assert movement outside the simulation).

The **surface position alone does not always prove scope**:
Unisermo already permits topicalization and fronting of ordinary
case-marked event complements. In particular, `domin movi` may
still be a fronted **spatial** event-locative ("in the house, I
move") and MUST NOT automatically become a proposition-domain
reading just because it is initial. A noun that can refer both to
an institution and a physical location likewise may have more
than one reading; its nominal semantics and explicitly expressed
frame determine the intended attachment. When ambiguous, preserve
that ambiguity or restructure for clarity. A leading `-in` is
the **preferred unmarked presentation** of a proposition-level
domain, **not** an automatic override of existing fronting rules.
Do not claim guaranteed disambiguation from word order alone.

With an `aut` frame, a proposition-domain `-in` and a permission
source `-de` remain distinct arguments:
`[NORMA]-in auti umande mov` locates the assertion within the
normative domain; `uman-de` identifies who granted the permission.
A norm-domain is not automatically the source granting the permit;
nor is the norm necessarily the cause, purpose or time of the action.

**Scope limit of this ratification:** only the spatial/local
baseline and the illustrated *single simple proposition* domain
frame are accepted. It does **not** decide how far `-in` scopes
over `P e Q`, `P o Q`, `ma`, `due`, `nam`, `ergo`,
`se P alor Q` or nested clauses, nor does it decide multi-domain
stacking, modal-domain interactions beyond a single simple
`aut` frame, or arbitrary movement of the domain adjunct.
Punctuation does not carry grammatical scope. The existing
temporal relator `tem` remains canonical for "during/at a
time"; `-in` is not automatically a temporal case. The
typed parser identifies preposed locatives while leaving their
event-domain versus proposition-domain attachment **unresolved**;
it does **not** infer abstract domain truth solely from word order.

## Physical action frames with existing cases (ratified 2026-11-13)

The accusative `-em` marks the direct participant for
`fer`, `portar`, `ten`, and `kunten`, but the
**semantic role is verb-dependent**: acquired entity,
cargo, held/controlled entity, or contents, respectively.
In `fer X-em SOURCE-de`, ablative `-de` is the
*physical origin* of taking, not the object's owner
or authorization source. In `portar X-em SOURCE-de DEST-ad`,
ablative and allative locate transport origin and
destination, not the fact of arrival. The movement cases
do not automatically belong to non-motion `ten` or
spatial-containment `kunten`. Ordinary event-local
`LOCATION-in` remains a freely interpretable adjunct,
not a second contents argument.

These distinctions are encoded as **lexical valency**
rather than as extra nominal cases or morphological
agreement. Object omission is an open separate decision;
the typed parser subset requires explicit `X-em`.
See [derivation.md](derivation.md) and
[LDR-0014](../docs/ldr/LDR-0014-physical-action-valency.md).
