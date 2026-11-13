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

Independent subject pronouns use the same forms. Unisermo is pro-drop when
the verbal ending makes the subject recoverable.

## 3. Canonical finite structure

Every ordinary finite verb has the fixed order:

```text
root + aspect + time + person vowel + optional N
```

The aspect and time slots are distinct. A finite verb contains at most one
aspect marker and at most one time marker. Aspect is closer to the lexical root;
time follows aspect; person and number remain outermost.

Examples with `mov`:

| Structure | Singular | Plural |
|---|---|---|
| present simple | `movi`, `movu`, `mova` | `movin`, `movun`, `movan` |
| past simple | `movdi`, `movdu`, `movda` | `movdin`, `movdun`, `movdan` |
| future simple | `movfi`, `movfu`, `movfa` | `movfin`, `movfun`, `movfan` |

The ordering rule is canonical: aspect never follows time, TAM never follows the
person marker, and plural `/N/` never precedes the person vowel.

## 4. Canonical 3×3 tense-aspect system

Finite inflection distinguishes three aspects and three times.

### 4.1 Aspect slot

- zero — simple
- `e` — ongoing / progressive
- `o` — completed / perfect

Aspect is expressed by vowels deliberately distinct from the person-vowel set
`i/u/a`.

### 4.2 Time slot

- zero — present
- `d` — past
- `f` — future

Aspect precedes time. The nine regular TAM combinations are therefore:

| Time / Aspect | Simple `Ø` | Progressive `e` | Completed / perfect `o` |
|---|---|---|---|
| present `Ø` | `Ø` | `e` | `o` |
| past `d` | `d` | `ed` | `od` |
| future `f` | `f` | `ef` | `of` |

Examples with `dik` in first-person singular:

- `diki` — I say
- `dikei` — I am saying
- `dikoi` — I have said / the saying is completed
- `dikdi` — I said
- `dikedi` — I was saying
- `dikodi` — I had said
- `dikfi` — I will say
- `dikefi` — I will be saying
- `dikofi` — I will have said

The vowel-before-time order is phonotactically motivated. When both aspect and
time are overt, the aspect vowel separates a consonant-final root from the time
consonant: `dik-e-d-i`, `dik-o-f-i`. In present aspect-marked forms, where time
is zero, aspect and person vowels form an intentional hiatus: `dikei` is
`/dik.e.i/`, and `dikou` is `/dik.o.u/`. This hiatus must remain recoverable and
must not coalesce in a way that erases the aspect distinction.

The former consonantal aspect markers `n` (progressive) and `b` (completed) are
retired from finite TAM. They remain ordinary phonemes elsewhere in the
language. The former synthetic marker `m` for ability/potential is also retired
from TAM.

Ability, obligation, volition, learned capacity and related modal or servile
meanings are expressed by an ordinary finite servile verb followed by the bare
infinitive/root of the lexical verb. The servile verb carries aspect, time,
person and number; the dependent infinitive remains uninflected.

The four **author-ratified short servile roots** (12 November 2026) are
`pos` (situational or circumstantial possibility/opportunity),
`deb` (normative obligation/duty), `vol` (volition/wanting), and
`pot` (ability or capacity of the participant). The independently
confirmed ordinary knowledge verb `sap` additionally admits a
**procedural-knowledge** frame `sap + bare infinitive` ("know how to"),
without implying ability, opportunity or actual performance. These meanings
must not be collapsed: feasible need not mean capable; capable need not mean
knowledgeable; know-how need not guarantee the practical capacity to act.
`pos` alone does not assert legal permission or authorization; permission
and necessity outside the four described types remain separate open issues.

All five heads are ordinary inflectable verbs with the canonical
root + aspect + time + person vowel + optional N pattern. In the
servile/know-how construction each head takes one dependent lexical verb
in its uninflected bare-root form, sharing the head's subject (pro-drop
is retained). No extra modal affix or dependent-person agreement occurs.

| Construction | First-person meaning |
|---|---|
| `posi mov` | it is possible for me to move (opportunity) |
| `debi mov` | I must move (obligation) |
| `voli mov` | I want to move |
| `poti mov` | I am able to move (capacity) |
| `sapi mov` | I know how to move (procedural knowledge) |
| `debdi mov` | I had to move (past obligation) |
| `volfi mov` | I will want to move (future volition) |
| `potin mov` | we are able to move |

The same lexical action gives three different statements: `posi dok`
(I have the opportunity to teach), `poti dok` (I have the capacity to
teach), and `sapi dok` (I know how to teach). None alone asserts
that I actually teach. The differences are semantic, not stylistic.

**Local negation of servile frames (same 2026-11-12 ratification):**
free `no` immediately before the conjugated servile denies the modal
relation; free `no` immediately before its uninflected lexical complement
negates the **action inside** the modal relation:

- `no debi mov` = NOT obligated(move): I do not have to move.
- `debi no mov` = obligated(NOT move): I must not move.
- `no posi mov` = NOT possible(move): I cannot move under the circumstances.
- `posi no mov` = possible(NOT move): it is possible for me not to move (no voluntary choice implied).
- `no voli mov` = NOT want(move); `voli no mov` = want(NOT move).
- `no poti mov` = NOT able(move); `poti no mov` = able(NOT move).
- `no sapi mov` = NOT know-how(move); `sapi no mov` = know-how(NOT move).

These constructions express relations to an action; none by itself
asserts that the action takes place or fails to take place.

These are **distinct semantic scopes**, not evidence that "not obliged"
means "forbidden", nor that inability equals lack of opportunity or lack
of procedural knowledge. Each free `no` occupies an existing position
before the predicate it negates; no new negative morpheme is introduced.
`no lim` remains the separately ratified, restricted **coordinated
proposition** scope opener and is not automatically applied to modal frames.
Negation stacking, agent-control exceptions, nested serviles, alternative
complement subjects and general modal scope with clause connectors or
subordinates are not decided here. The typed proposition parser now
implements the single-head shared-subject servile subset and continues
to fail closed on unratified stacked or nested modal scopes.

This construction is productive: no special synthetic suffix is added to
the dependent lexical verb for modal meanings.

### Attempt servile: `tent` (author ratification 13 November 2026)

`tent` is the regularly inflected **attempt servile**: the subject undertakes a genuine goal-directed attempt to bring about the dependent event. It is **not** a separate aspect, tense or causative marker. Its basic canonical frame uses the established shared-subject servile syntax:

```text
[SUBJECT] [no] TENT-FINITE [no] BARE_VERB [DEPENDENT ARGUMENTS...]
```

- `tenti mov` — I attempt to move. A genuine attempt takes place; successful movement is **not** asserted.
- `tentdi mov` — I attempted to move (past attempt; outcome unspecified).
- `tentei mov` — I am attempting to move.
- `tenti adkap` — I attempt to come to understand.
- `tenti adsap` — I attempt to acquire knowledge; this does not entail that I learned anything.
- `tenti portar domem` — I attempt to carry the house; the dependent `portar` retains its own object-valency conditions.
- `no tenti mov` — I do **not** undertake an attempt to move.
- `tenti no mov` — I attempt **not** to move: purposeful restraint or avoidance, not mere failure to move.

The core lexical commitment is **actual attempted action**, plus a targeted event that need not obtain. It is logically stronger than `vol V` (desire alone) and independent of `pot` (capacity), `pos` (circumstantial opportunity), `deb` (duty), `aut` (permission) and `sap` (know-how). A failed or impossible attempt can still be a genuine attempt; `tent V` therefore does not assert `pot V` or `pos V`. An attempt can succeed, but success is never inferred solely from `tent`.

`tent` normally implies an intentional effort **toward the particular dependent event**; it is not a generic marker that every action of the agent is intentional. Non-intentional outcomes and downstream side effects require separate event- and scope-level statements. An aim `fin V` within a different performed action is not necessarily an attempt of V; `vol V` is not necessarily action. The dependent verb retains its **own** required nominal and relational complements. In this parser subset no nested serviles, separately controlled subjects, or dedicated `tent` source/counterpart cases are licensed.

The spelling is the canonical `tent` (four letters, final /t/), not `ten` (hold / maintain a physical constraint). These are distinct lexical roots. Their phonetic proximity deserves empirical testing but is not morphological ambiguity.

`tent` does **not** by itself replace `stud`. The activity of systematically studying can be an attempt to acquire knowledge (`tent adsap`), but those concepts are not proven equivalent in every context. Neither `stud` retirement nor any other servile root is ratified by this decision.

### Permission and authorization: `aut` (author ratification 12 November 2026)

`aut` is one short, ordinary, inflectable **servile verb root** meaning
*be permitted/authorized to perform an action*. The lexical root does
not distinguish informal permission from a formal authorization or
license. Context and an optional source complement make the distinction.
`aut` is derived from the international *auctoritas/authority* family
with the official graphemes only; `auth` with `h` is **not** Unisermo.
`aut` is a root, **not** a newly ratified productive prefix `aut-`.

Its basic frame is regular:

- `auti mov` — I am permitted to move.
- `autdi mov` — I was permitted to move.
- `autin mov` — we are permitted to move.
- `no auti mov` — I am not permitted/authorized to move.
- `auti no mov` — I am permitted to refrain from moving.

The distinction with `posi mov` (circumstances make moving possible)
is essential: I may have an opportunity without permission, or
permission without an opportunity. `pot` still marks participant
capacity, `sap` practical know-how, `vol` desire, and `deb` duty.
Neither `aut` nor `pos` asserts that the action actually occurs.

**Permission source (existing ablative `-de`):** a granting
person, body, or normative source may be specified as an **optional
governed complement immediately after the finite `aut` head**, and
before the dependent bare verb. The canonical unmarked sequence is:

```text
[SUBJECT] [no] AUT-FINITE [SOURCE-NP-de] [no] VERB-ROOT [VERB ARGUMENTS...]
```

For example, with existing `uman` (person) and `dom` (house):

- `auti umande mov` — I have permission **from a person** to move.
- `no auti umande mov` — I am **not** permitted by that person to move.
- `auti umande no mov` — that person permits me **not** to move.
- `auti umande mov domde` — I have permission **from a person** to move
  **from a house**.

The last sentence illustrates why source attachment matters. The
`SOURCE-de` phrase in the **head slot immediately after `aut`**
denotes the origin of the permission; a later `-de` phrase inside
the dependent action may denote the origin of the movement. Without
this positional distinction, `auti mov domde` cannot automatically
be read as permission **from** the house: the `domde` may belong to
the movement. No new ablative suffix or general change to cases is
implied. This head-specific source slot is the narrow exception to
immediate `finite servile + bare infinitive` adjacency; both the
finite verb and dependent verb retain their ordinary morphology.

`no auti V` denies that the relevant permission exists; it does
not itself assert an explicit prohibition (`debi no V`). Likewise
`auti no V` affirms permission to refrain and does not automatically
mean an absence of obligation (`no debi V`). An explicit
`SOURCE-de` restricts the denial or permission to that source;
it does not make claims about all possible other authorities.

The separately approved abstract-domain extension of locative `-in`
(LDR-0013, 2026-11-12) allows a *left-peripheral* proposition-level
`DOMAIN-NP-in` ahead of a **simple proposition** containing `aut`.
For example, `[NORMA]-in auti umande mov` distinguishes the
normative **domain** from the granting **source** `uman-de`. The
normative domain and granting source need not be identical. All
abstract-domain noun labels shown in brackets are *unratified
placeholders*, not lexemes. This extension is deliberately limited
to simple propositions; no mixed subordination, connector scope or
multiple domain operators is implied. See
[noun_case_system.md](noun_case_system.md).

The typed proposition parser now supports one finite `aut` head, an
optional governed source `-de` and one bare verbal complement; this
remains a restricted syntactic implementation, not an authorization
reasoner or unrestricted modal-scope interpreter. Unsupported parsing
must fail closed.


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
- `bis fakit` — two facts / two things done

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

## 8. Motion-family valency

Canonical `mov` may be used intransitively or transitively without a separate
causative derivation:

- `X mov` — X moves
- `Y mov X-em` — Y moves / displaces X
- `Y mov X-em DEST-ad` — Y moves X toward DEST

This valency alternation is inherited by `admov`, `inmov`, `demov`, and `remov`:
transitive `admov` sets an object in motion, `inmov` keeps it in motion, `demov`
stops it, and `remov` sets it in motion again. `inmov` is not lexical "push" or
"pull"; those notions require their own manner/force semantics.
## 9. Force/manner verbs: `pel` and `trak`

Two independent canonical roots describe the physical manner/force relation without
collapsing it into the `mov` phase family:

- `Y pel X-em` — Y pushes X
- `Y trak X-em` — Y pulls / draws X

`pel` and `trak` do not by themselves entail successful displacement. A speaker may
push or pull an object that does not move. Actual caused displacement is expressed
with transitive `mov`, optionally with a destination in `-ad`. Thus force/manner and
resulting motion remain semantically distinct.

## 10. Vertical motion

The vertical-axis roots are `alt` = high/upper/up and `bas` = low/lower/down.
With the allative case they form analytic motion directions:

- `mov altad` — move / go upward
- `mov basad` — move / go downward

The transparent compounds are also canonical:

- `altmov` — ascend / go up
- `basmov` — descend / go down

They encode direction and must not be confused with phase-derived `admov`
(begin moving) or `demov` (cease moving).


## 11. Ratified physical and cognitive verb roots (2026-10-25)

`fer` = take/grasp physically; `portar` = carry/transport; `kap` =
understand (no longer take/capture); `sap` = know; `pens` = think.
These roots have distinct event/state meanings. Their phase derivatives
are defined by the regular `ad-/in-/de-/re-` operators in
[derivation.md](derivation.md), not by Latin or modern homonyms.

## 12. Physical-action valency: `fer`, `portar`, `ten`, `kunten` (ratified 2026-11-13)

The canonical overt-argument patterns use the **existing** case
inventory and are distinguished by the action root:

- `Y fer X-em [SOURCE-de]`: Y physically takes/grasp X,
  optionally from a *physical* source. This does **not**
  entail carrying, ownership, permission or continued holding.
- `Y portar X-em [SOURCE-de] [DEST-ad]`: Y physically carries
  X; the optional ablative source and allative destination
  belong to the transport event. `DEST-ad` does **not**
  entail arrival.
- `Y ten X-em`: Y maintains physical/control constraint
  over X through time. This is **not** acquisition,
  movement or automatically physical enclosure.
- `CONTAINER kunten CONTENTS-em`: a physical entity
  spatially contains CONTENTS. The subject **need not**
  be a volitional agent; no ownership or abstract
  part-whole claim follows from this verb.

`SOURCE-de` attached to `fer` is an origin, *not*
necessarily a former owner. `kunten` remains a **lexicalized
compound**; productive associative `kun-` does not
mean containment on other verbs. A regular single phase
prefix preserves the base's arguments; a productive
associative event prefix does so for `fer`, `portar`
and `ten`, without adding an obligatory co-agent.
A further `kun-` on lexicalized `kunten`
(`kunkunten`) is outside the bounded approved subset. A separate locative
`-in` or normal invariant relator may act as a
nonselected adjunct, not a new patient argument.

The bounded reference parser **requires an overt `X-em`**
for these constructions. Contextual object omission is
**not ratified here**: it remains a future question,
not a universal grammatical prohibition. See
[derivation.md](derivation.md) and
[LDR-0014](../docs/ldr/LDR-0014-physical-action-valency.md).


## 13. Knowledge-state valency: sap family (ratified 2026-11-13)

The root `sap` describes the subject's state of knowing. Its already ratified phase family `adsap`, `insap`, `desap`, `resap` retains the same **knower** as subject. They respectively express entry into knowledge, continued knowledge, leaving knowledge, and return to previously held knowledge. `desap` does not by itself encode the psychological mechanism of forgetting; `resap` does not select between spontaneous remembering and relearning.

Two non-interchangeable explicit-argument frames are licensed for each member:

| Frame | Syntax | Interpretation |
|---|---|---|
| knowledge content | `KNOWER-NOM sap-family CONTENT-em` | Content is what the knower knows / comes to know / retains / loses / regains |
| procedural knowledge | `KNOWER-NOM sap-family BARE_VERB` | Bare action is what the knower knows how to perform, or comes to know / ceases to know how to perform |

Examples (with ordinary finite morphology):

- `i sapi domem` — I know the house (knowledge/familiarity of a referent; does not assert any particular fact about it).
- `i adsapi domem` — I come to know / become familiar with the house.
- `i desapi domem` — I lose my knowledge/familiarity of the house.
- `i sapi dok` — I know how to teach (previously ratified frame).
- `i adsapi dok` — I acquire the know-how to teach.
- `i adsapei dok` — I am acquiring know-how to teach; completed acquisition is not entailed by progressive aspect.
- `i resapi dok` — I regain know-how to teach.

The procedural complement is a **bare lexical verb**, with the same subject as the knowledge head, and is not a second independently asserted action. `sapi dok` does not entail actual teaching, and `adsapi dok` does not entail that an instructional activity `dok` occurred. This extension **does not** authorize arbitrary bare-verb complements with other roots or new causative valencies.

The accusative of the content frame is **always the content**, never a person induced to learn. Thus `Y adsap PERSON-em` can only mean knowledge *of the person*, not Y teaching that person. A causative for acquiring knowledge is reserved for a general, separately ratified state-causation analysis. Ordinary `dok` (teaching) and `stud` (studying) remain independent and do not entail successful knowledge acquisition. `lern` is not adopted.

A knowledge-content noun does not automatically mean its propositional truth, and propositional subordinate complements require their own syntax. This parser subset implements only explicit nominal content and procedural bare verbs; omissions and mixed knowledge frames are excluded. See `docs/ldr/LDR-0019-sap-knowledge-family.md`.
