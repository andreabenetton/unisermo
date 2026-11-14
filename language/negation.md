# Negation, Polarity, and Focus

## 1. Free polarity words

- `si` — yes
- `no` — no

## 2. Sentential negation

`no` immediately precedes the verb or predicate it negates:

- `i no vidi` — I do not see
- `a no vida domem` — the person does not see the house
- `no mov!` — do not move!

## 3. Focus enclitics

The same polarity roots have enclitic focus uses:

- `-si` — also / too
- `-no` — neither / not ... either / not even, depending on focus and context

Examples:

- `i-si vidi domem` — I too see the house
- `i-no vidi domem` — not even I / I don't either see the house
- `tik uman-si` — also this person
- `tik uman-no` — not even this person

`-no` carries the negative force of the focused proposition. An additional
preverbal `no` is not normally required: use `i-no vidi`, not ordinary
`*i-no no vidi`.

## 4. Negation is not antonymy

**Ratified 2026-10-24:** Free `no` is the sole ordinary grammatical
negator; historical attached `no-` is retired. Semantic antonyms of
opposable qualitative roots instead use fused `ne-` (see `derivation.md`).

- `tik no bel` — this is not beautiful (does not entail ugly)
- `tik nebel` — this is ugly
- `tik no nebel` — this is not ugly (does not entail beautiful)

`anti-` continues to mark active opposition, not negation or an automatically
derivable antonym.

## 5. Negation of normative predicates (ratified 2026-10-24)

Free `no` negates a proposition. Fused `ne-` indicates a substantive
contrary in domains where a semantic opposite exists:

- `no prob`: not morally good; `neprob`: morally bad.
- `no just`: not just; `nejust`: unjust, not necessarily illegal.
- `no legal`: not legal; `nelegal`: illegal under applicable positive law.
- `no fas`: not permitted under a sacred norm; `nefas`: impious or sacrilegious.

A neutral or indeterminate status need not instantiate the contrary. In a
context with a genuinely exhaustive binary distinction the extension may
coincide, but the grammatical and lexical operations remain separate.

## 6. Wide-scope propositional negation with `no lim` (author ratification 2026-11-12)

Ordinary free `no` remains the **local pre-predicate negator**: it immediately precedes the verb or predicate it negates. Its scope does not silently extend to following coordinated clauses. For simple pro-drop propositions P = `vidi` (I see) and Q = `movi` (I move):

- `no vidi e movi` = (NOT P) AND Q: I do not see and I move.
- `no vidi ma movi` = I do not see, but I move; `ma` contributes an adversative relation not supplied by `e` or by `lim`.

The two **separate, pronounced words** `no lim` are a specially licensed *wide-scope negation introducer*. Unlike local `no`, this construction takes the following complete **truth-conditional propositional expression** as its negated operand, including a right-associated chain built using ordinary `e` (AND), inclusive `o` (OR), or an initial-`o` exclusive choice (exactly one). No explicit subject is required: normal pro-drop is preserved.

- `no lim vidi e movi` = NOT (P AND Q): it is not true that I both see and move.
- `no lim vidi o movi` = NOT (P OR Q): I neither see nor move; here `o` is inclusive inside the negation.
- `no lim o vidi o movi` = NOT (exactly-one(P, Q)): either both propositions are true or both are false. For three or more exclusive alternatives, negation means zero or at least two alternatives are true.
- `no lim P e Q o R` = NOT (P AND (Q OR R)): the already ratified right-association convention is unchanged.

The operand of `no lim` extends to the end of the enclosing propositional expression **unless** a subsequent *closing* `lim`, immediately before a following clause connector, first closes it. Thus `no lim P e Q lim o R` = (NOT (P AND Q)) OR R. The closing `lim` retains its prior boundary function; the `lim` **immediately after `no`** has the new, narrowly licensed opening function. Bare `lim P`, `P e lim Q`, and sentence-final `P lim` remain invalid. Commas do not open or close grammatical scope.

The single-clause `no lim P` need not be preferred when local `no P` expresses the same truth conditions; the marked construction exists for scope precision, not stylistic duplication. Logical equivalences (including De Morgan laws) do not erase distinct connective/discourse meaning, especially `e` versus `ma`.

**Scope boundary:** this ratification defines wide negation only for truth-conditional `e` / `o` clause combinations, including the already ratified exactly-one construction and the explicitly illustrated `lim` boundary. It does **not** define negation of a contrast relation (`ma`), factual cause (`due`), evidential justification (`nam`), inference (`ergo`), or conditional/concessive/exception relations (`se`, `etsi`, `etsise`, `eksese`, `alor`); nor does it ratify arbitrary recursive scope, multiple negations, `-no` focus interactions, or question-wide negation. Those cases require separate work. The typed proposition parser now recognizes this exactly delimited `no lim` subset and continues to reject unapproved wider negation scope. No new word, affix, or parser capability is introduced.

## 7. Negating servile modality versus the dependent action (author ratification 2026-11-12)

The confirmed analytic frame is `[finite SERVILE] + [bare lexical root]`.
The ratified roots are `pos` (situational possibility), `deb`
(obligation), `vol` (volition), `pot` (capacity), plus existing
`sap` with a bare infinitive for practical know-how. The two ordinary
positions of the invariant free word `no` are semantically distinct:

- `no debi mov` — I am not obliged to move: NOT OBLIGATED(move).
- `debi no mov` — I am obliged not to move: OBLIGATED(NOT move).
- `no posi mov` — moving is not possible for me under the circumstances.
- `posi no mov` — not moving is possible for me.
- `no voli mov` / `voli no mov` — do not want to move / want not to move.
- `no poti mov` / `poti no mov` — cannot move due to inability / am able to refrain.
- `no sapi mov` / `sapi no mov` — do not know how to move / know how not to move.

In the first position `no` negates the **finite modal head** and thus
denies the modality with respect to the given action. In the second
position it negates the **dependent action** while leaving the modal
head affirmative. The bare infinitive/root stays uninflected with either
placement, so ordinary subject pro-drop and finite TAM remain intact.

In particular, `no debi mov` does **not** mean prohibition; `debi no mov`
does. These distinctions are **not** interchangeable even if contexts
make speakers infer similar consequences. This is not a second use of
`no lim`; that previously accepted opener has a separate, limited
truth-conditional clause-chain domain. Multiple `no` tokens in one
servile frame, modal negation of subordinate clauses, and a full parser
for servile complements are outside this decision. See
[verb_specification.md](verb_specification.md).

## 8. Negation of permission `aut` (ratified 2026-11-12)

The same already ratified local positional distinction applies to
the newly accepted permission verb `aut`:

- `no auti mov` — I lack permission/authorization to move.
- `auti no mov` — I have permission to refrain from moving.
- `debi no mov` — I am obliged not to move (a prohibition).
- `no debi mov` — I am not obliged to move (no obligation).

Neither **lack of permission** nor **lack of obligation** is
automatically a positive prohibition or a permission to refrain.
`no auti umande mov` narrows the denial to the stated granting
source `uman-de`, rather than all possible grantors. See
[verb_specification.md](verb_specification.md) and
[noun_case_system.md](noun_case_system.md).

`aut` is not a synonym for physical feasibility `pos`; it marks
a normative permission, including authorization where an authority
is specified. No new negation operator or `no lim` interaction is
ratified.


## Attempt servile negation (ratified 2026-11-13)

The regular servile `tent` uses the existing two local negation positions:

- `no tenti mov` — NOT [attempt to move]; does not claim movement occurred or failed.
- `tenti no mov` — attempt [NOT move]; a purposeful attempt to remain motionless, not simply a failure to move.

Neither expression entails the positive occurrence of `mov`. An attempted action that fails is **not** the same as the denial of an attempt. The attempt is an event asserted by the head `tent`, whereas the dependent event is only a goal. No extra negative morpheme or scope operator is introduced. See `language/verb_specification.md`.


## Committed-intention servile negation (ratified 2026-11-13)

The new shared-subject servile `int` preserves the existing negation positions:

- `no inti mov` — I have no adopted intention to move; not a positive intention to refrain.
- `inti no mov` — I have adopted the intention *not* to move; it does not guarantee that I remain still.

`voli mov` (desire to move) does not entail `inti mov` (adopted intention), and `inti mov` does not entail `tenti mov` (actual effort) or `movi` (movement). All scope markings are ordinary pre-predicate `no`, with no new case or negator.


## Propositional epistemic `pos` negation (author ratification 2026-11-13)

In `pos FINITE_PROPOSITION`, the invariant bare `pos` has no subject or personal suffix. The free negator retains its normal positional scope:

- `no pos uman mova` = NOT POSSIBLE(person moves).
- `pos uman no mova` = POSSIBLE(person does not move).
- `no pos uman no mova` = NOT POSSIBLE(person does not move), the epistemic necessity of movement relative to the same possibility domain.
- `no pos uman mova lim e vida` = NOT POSSIBLE(person moves) AND person sees: `lim` closes the operator before `e`.

This is **not** an instance of the two-token wide-negation operator `no lim`. Neither `no pos P` nor `pos no P` entails P by itself. Probability grades and necessity from independent normative premises are not implied by these forms.


## Outer-subject bare serviles with finite propositions (ratified 2026-11-13)

The subject precedes an uninflected propositional servile, so negation immediately before the **bare head** denies the attitude/attempt/knowledge relation, while negation before the embedded **finite verb** denies the embedded event:

- `i no vol u movu` = I do not want you to move.
- `i vol u no movu` = I want you not to move.
- `i no sap u movu` = I do not know that you move; this does not assert you do or do not move.
- `i sap u no movu` = I know you do not move; the positive knowledge assertion commits to its embedded negative content.

The pre-head negative must not be confused with grammatical `no lim` sentential-negation scope. No new negative particle is introduced.


## Propositional necessity and personless tense (ratified 2026-11-13)

`deb FINITE_PROPOSITION` is necessary(P) relative to the relevant modal premises, not the personal duty `debi BARE_VERB`. `no deb P` negates necessity, whereas `deb no P` asserts necessity of not-P. A tensed head, e.g. `no debd uman movfa`, retains the same relative scopes while locating the **necessity assessment** in the past and the dependent event later than that assessment. `no posd uman movfa` negates a past possibility judgment; it does not assert P's negation. `no pos no P` and `deb P` are equivalent only under one fixed accessibility domain.

## Elliptical subject contrast with `ma` (author approval 2026-11-14)

The bounded `S1 V [ARGS] ma S2` construction of [word order](word_order.md) recovers the finite predicate and its arguments with **opposite polarity** when S2 is a bare subject without a finite verb. `e S2` recovers the **same polarity**. Thus `adelo vida trenem ma adele` = 'the brother sees the train but the sister does not', whereas `adelo vida trenem e adele` = 'the brother sees the train and so does the sister'. This is **ellipsis recovery**, not a redefinition of `ma` as a grammatical negator; complete clauses still indicate negative polarity with `no`.
