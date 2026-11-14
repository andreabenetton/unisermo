# Word Order

A formal specification of the default constituent order of the synthetic language, and the conditions under which that order may be relaxed.

## Related documents

- The verb's final person vowel encodes the subject and makes independent subject pronouns optional (pro-drop). See [`verb_specification.md`](verb_specification.md).
- Case suffixes mark the grammatical role of each noun phrase, which is what enables word-order freedom. See [`noun_case_system.md`](noun_case_system.md).
- Optional nominal plurality with `wi` is defined in [`noun_number_system.md`](noun_number_system.md).

This document introduces **no new morphemes** — only a syntactic rule.

---

## 1. Design Goal

The language must have:

- a **single unmarked default order**, so that ordinary prose flows in a predictable way and listeners can parse short utterances without scanning for case markers;
- a **release valve**, so that when a speaker wants to foreground a constituent for emphasis, the case suffixes are enough to keep the sentence unambiguous in any order.

---

## 2. Options Considered

| Option | Example gloss | Most familiar to |
|---|---|---|
| SVO | I see house | English, Romance languages, Mandarin |
| SOV | I house see | Japanese, Korean, Hindi/Urdu, Turkish |
| Free (case-driven) | subject/object marked, order free | possible, but less simple to teach |

---

## 3. Default Order: SVO

The unmarked order is **Subject – Verb – Object**.

```
i vidi domem
= I see the house
```

With a full noun subject:

```
amik vida domem
= the friend sees the house
```

**Pro-drop.** Independent subject pronouns are optional, because the verb's final person vowel already identifies the subject (see [`verb_specification.md`](verb_specification.md)). The bare form

```
vidi domem
```

is also a complete sentence meaning "I see the house" and is the more typical phrasing in connected speech. The explicit pronoun `i` is used for contrast, emphasis, or clarity.

---

## 4. Reordering for Emphasis

Because case suffixes unambiguously identify each noun phrase's grammatical role (see [`noun_case_system.md`](noun_case_system.md)), the SVO default may be relaxed when a speaker wants to foreground a particular constituent. The most common departure is **object fronting** for topicalization:

```
domem vidi i
= the house, I see
```

Here the object `domem` is fronted, but its `-em` suffix keeps it identifiable as the object regardless of where it sits in the sentence. Other orders (OVS, OSV, etc.) are likewise legal whenever the speaker has a reason to use them; the listener relies on the case suffixes, not on position, to assign roles.

**Rule.** SVO is the default. Any other order is marked: it carries pragmatic weight (emphasis, contrast, topicalization) that the speaker is presumed to intend.

---

## 5. Rationale

- **SVO is the most broadly familiar order** among the language's target speaker backgrounds: English, every Romance language, and Mandarin all use SVO as their basic order. Choosing it as the default minimizes the parsing effort for the largest contiguous group of learners.
- **A single fixed default keeps prose consistent.** Unmarked sentences look the same everywhere, which makes the language easier to read at a glance.
- **The case system provides the release valve.** Speakers from SOV backgrounds (Japanese, Korean, Hindi/Urdu, Turkish) or from free-order traditions are not forced to abandon their habits in emphatic or contrastive sentences; they can reorder freely whenever the case suffixes carry the load.

The combination — fixed SVO default plus permitted reordering — gives the regularity of a strict-order language together with the flexibility of a case-marked one, at no extra morphological cost.

## Conditional introducer `se` (ratified 24 October 2026)

`se` is the standalone conditional conjunction **IF**. It is distinct from confirmed free `si` YES and `no` NO/NOT. `se` introduces a condition clause P in a conditional relation between P and Q; the exact placement, boundary marking and nesting rules of complex conditionals are **not yet ratified**. Candidate structures `se P, Q` and `se P, tum Q` are **illustrative proposals**, not a new approved clausal parser grammar. `tum`/ `alor` (THEN), `ergo` (THEREFORE), `nisi` (UNLESS), `sin` (ELSE IF) and `sed` (BUT) remain under consideration. `se` does not by itself establish a counterfactual verbal mood.


## Connectives: `alor`, `ma`, `ergo` (ratified 24 October 2026)

Free-standing `alor` marks **THEN**, the consequent in a conditional relation introduced by ratified `se` (IF); `ma` is the ordinary adversative conjunction **BUT**; `ergo` introduces an inferential conclusion **THEREFORE / THUS**. They are distinct from each other and from already ratified `e` (AND) and `o` (OR).

Schematic illustrations (not claims of complete parser support): `se P, alor Q` ('if P, then Q'), `P ma Q` ('P but Q'), `P, ergo Q` ('P, therefore Q'). Full clausal grammar, nesting, precedence and whether `alor` may be omitted in every construction remain to be decided separately. `sed` and `tum` were alternatives considered, **not** ratified.


## Order of causal clauses (ratified 24 October 2026)

Both `P due Q` (effect followed by its causal explanation) and `due Q, P` (fronted causal clause followed by effect) are accepted. In either order Q is the cause and P the effect. `Q, ergo P` instead presents P as an inference/conclusion. The typed parser recognizes postposed finite-clause `P due Q`; the fronted `due Q, P` construction remains canonical but is still outside executable scope until its boundary can be parsed without relying solely on punctuation.


## Factual concessive `etsi` (ratified 24 October 2026)

`etsi` introduces an accepted/factual concession: `etsi P, Q` ('although P, Q') and `Q etsi P` ('Q, although P') are both permitted, with P the conceded proposition and Q the contrasting outcome. Distinguish conditional `se` (IF) and adversative `ma` (BUT). The hypothetical reading 'even if P were to happen' is not automatically ratified. The typed parser recognizes postposed simple concessives and the canonical explicitly paired `etsi P alor Q`; arbitrary mixed-subordinate scope remains unsupported.


## Hypothetical concessive `etsise` (ratified 24 October 2026)

The invariant **single-word** compound `etsise` = `etsi` (concessive) + `se` (hypothetical condition) denotes hypothetical **EVEN IF / EVEN SHOULD**. Both `etsise P, Q` ('even if P, Q') and `Q etsise P` ('Q, even if P') are grammatical. The speaker does **not assert that P is true or false**, unlike `etsi` which presents P as factual or accepted. The consequent Q is asserted to hold even in the eventuality P, not in all imaginable circumstances. `etsise` is a specifically licensed compound, **not** evidence that arbitrary connective strings may be fused. Complex subordinate-scope parsing remains outside the current restricted parser.


## Exception and conditional exception (ratified 24 October 2026)

`ekse` is a free invariant EXCEPT/EXCLUDING operator. The fused single-word `eksese` = `ekse` + `se` introduces a conditional exception, UNLESS / EXCEPT IF. The two clause orders `eksese P, Q` ('unless P, Q') and `Q eksese P` ('Q, unless P') are both valid. Unlike simple `se no P, Q` ('if not P, Q'), `eksese` signals that P is an exception to an expectation/rule associated with Q; it does not generally entail that Q must happen whenever P is false. Full syntactic handling of the general exclusion operator and nested subordinate clauses remains future parser work. The fused compound is specifically licensed and does not make arbitrary fusion productive.

## Ratified free coordination (24 October 2026)

`e` AND and `o` OR are free conjunction words, not bound verbal aspect vowels `-e` or `-o`. Mixed-connective scope and precedence are not yet specified.


## Explicit propositional scope marker `lim` (ratified 25 October 2026)

The standalone invariant word `lim` is a **spoken and written propositional scope-boundary marker**, etymologically motivated by Latin *limes, limitis* (boundary). It is not a sentence terminator or a lexical verb. Every syntactically present `lim` is pronounced and written as a separate token; ordinary comma punctuation has **no scope-changing grammatical force**.

In connector chains within the licensed propositional-scope subset, mixed connectors have **no precedence hierarchy**: absent a boundary they associate to the right. Immediately before a following clause-connecting operator, `lim` closes the preceding sequence into the operator's left argument. Illustrative metalanguage (P,Q,R,S denote complete propositions):

- `P ma Q ergo R` = `P ma (Q ergo R)`.
- `P ma Q lim ergo R` = `(P ma Q) ergo R`.
- `P e Q o R` = `P e (Q o R)`.
- `P e Q lim o R` = `(P e Q) o R`.
- `P e Q lim o R lim ma S` = `((P e Q) o R) ma S`.

In this established **closing-boundary** use, `lim` must immediately precede the connector whose left operand it delimits; it cannot be sentence-initial, sentence-final, or placed between a connective and its complement. The separately ratified `no lim` opening construction (see `negation.md`) is a narrow exception and does not license bare `lim` before a clause. Thus `P e lim Q`, `lim P e Q`, and `P e Q lim` are invalid in this subset.

These examples establish the approved **ordinary connector-chain convention**; they do **not** authorize arbitrary combinations of subordinate forms, unrestricted nesting, or a general clause grammar. Existing ratified semantic distinctions of `due`, `nam`, `ergo`, `etsi`, `etsise`, and `eksese` are preserved; their subordinate boundaries and scope constraints await separate formalization. The inclusive/exclusive semantics of `o` are ratified in the later section below: ordinary infix `o` is inclusive, while an initial `o` introduces an exactly-one exclusive choice. Authors and LLM generators should prefer short, linear periods to deep nested structures. The typed proposition parser implements the listed bounded connective-chain constructions, retaining distinct operator nodes and rejecting undocumented combinations.


## Anteposed subordinate scope and generalized `alor` (author ratification 25 October 2026)

This section ratifies the nine-part subordinate-scope design, as amended by the author to generalize `alor`. This is a **syntactic extension** of ratified `alor`: in an explicitly marked anteposed subordinate construction it separates the subordinate operand from the matrix/main proposition. The opening connector determines the semantic relation; `alor` itself does **not** convert a factual concession, hypothetical concession, or exception into a conditional inference.

Canonical explicit anteposed templates (P = subordinate clause, Q = matrix clause):

- `se P alor Q` — condition; if P, then Q.
- `etsi P alor Q` — factual concession; although P, Q, with P presented as factual/accepted.
- `etsise P alor Q` — hypothetical concession; even if P, Q, without asserting P's truth or falsity.
- `eksese P alor Q` — conditional exception; Q unless P, with the normative exception-to-expectation reading, **not** the simple logical equivalent of `se no P alor Q`.

The explicit `alor` separator is required for the above *anteposed canonical templates*. This does not revoke already ratified postposed orders `Q etsi P`, `Q etsise P`, or `Q eksese P`, nor previously attested factual causal clause orders. It also does not retroactively declare every illustrated comma-delimited historical example invalid; those historical illustrations are superseded **as canonical boundary notation**, not erased.

The scope of the opening subordinate extends to its matching `alor`. In a nested sequence, delimiters are paired recursively from the innermost currently open antecedent to the outer one. Thus `se se P alor Q alor R` represents `se (se P alor Q) alor R`; `se P alor se Q alor R` represents `se P alor (se Q alor R)`; and `se etsi P alor Q alor R` represents `se (etsi P alor Q) alor R`. Here capital P/Q/R are schematic **complete propositions**, not Unisermo words.

This subordinate relation is separate from the already ratified ordinary connector-chain right association and `lim`. `lim` still closes the prior clause-chain segment immediately before a subsequent connector; it is **not** a substitute for `alor`, and comma punctuation does not delimit grammatical scope. Subordinate openers and scope separators have structural roles, not an arbitrary precedence hierarchy.

The grammar distinguishes a simple clause, a connector-linked compound clause, and subordinate relation nodes with typed antecedent/matrix operands. It permits composition and finite recursion as a linguistic rule; actual parser depth limits may be implementation safeguards, not new grammatical prohibitions. Authors and LLM generators should favor short linear periods and avoid unnecessarily deep nesting.

**Explicitly still open:** exact parsing and delimitation of fronted `due` causes and other `nam` epistemic explanations in arbitrary compound clauses; interaction of complex postposed subordinate arguments with following connectors; mixed subordinate/coordination scope outside the templates above; wide-scope negation beyond the separately licensed `no lim` truth-conditional subset and modality. These are not implied by this ratification. The typed parser recognizes the explicitly paired `alor` subordinate trees and their finite nesting under safeguards; arbitrary mixed subordinate/coordination scope remains unsupported and fails closed.


## Inclusive and exclusive `o` (author ratification 25 October 2026)

The free connector `o` has two **distinct constructions**, without introducing a new word:

- `P o Q` — **inclusive disjunction**: at least one alternative is true; both may be true.
- `o P o Q` — **exclusive choice**: exactly one alternative is true.
- `o P o Q o R` — **exclusive choice over three alternatives**: exactly one of P, Q, R is true. This is an n-ary exactly-one operator, **not** iterated binary XOR (odd parity).

The initial standalone `o` signals the exclusive-choice construction. Further standalone `o` tokens separate its alternatives. Ordinary infix `o` remains inclusive outside this construction. Alternatives must be complete propositional expressions. At least two alternatives are required for the exclusive-choice construction.

In the licensed ordinary connector-chain subset, existing right association is retained: `o P o Q e R` denotes exactly one of P and `(Q e R)`. The existing explicit scope boundary `lim` may close an exclusive-choice group immediately before a following connector: `o P o Q lim e R` denotes `(exactly-one(P,Q)) e R`. `lim` is spoken/written and retains its already ratified role; commas do not change scope.

For all n >= 2, an exclusive-choice expression is true iff **exactly one** alternative is true; it is false if none or two or more alternatives are true. The inclusive `o` requires at least one true alternative. These are truth-conditional propositional semantics; they do not automatically impose a real-world obligation, make alternatives mutually physically possible, or settle any previously open question about modality or conversational implicature.

Detailed interactions with nested subordinate scope, postposed subordinate clauses, whole-proposition negation outside the separately licensed `no lim` subset, and unrestricted connector grammars remain outside this ratification; the typed parser fails closed for these unsupported compound constructions.


## Wide negation cross-reference (author ratification 12 November 2026)

The separately ratified two-token **`no lim`** opener negates an entire truth-conditional `e/o` expression (including initial-`o` exactly-one choice), rather than a single local predicate. For schematic complete simple clauses P, Q, and R: `no P e Q` = (NOT P) AND Q; `no lim P e Q` = NOT(P AND Q); `no lim P e Q lim o R` = NOT(P AND Q) OR R. The opener does not change ordinary right association, the already ratified closing-boundary use of `lim`, or the distinct discourse meaning of `ma`. The exact licensed scope and exclusions are specified in [negation.md](negation.md); compound-clause parsing remains unimplemented in Phase 1.

## Proposition-domain frames versus event locatives (ratified 2026-11-12)

The single locative suffix `-in` may mark either a spatial/event
location or an abstract *domain of reference*. The approved
**unmarked, scope-explicit writing convention** for a *simple
proposition* is `[DOMAIN-NP-in] [P]` (domain left-peripheral,
before the overt subject or finite verb), contrasted with an
event-attached locative inside the predicate such as
`movi domin` ("I move in the house").

Crucially, this is a **difference in syntactic attachment**,
not an unconditional rule that every initial `NP-in` takes
whole-proposition scope. Existing case-based fronting of a
spatial/event locative remains legal: `domin movi` is not
automatically an assertion in the institutional or hypothetical
domain of the house. For semantically dual-use noun phrases
(e.g., a physical institution versus its legal regime), fronting
alone is insufficient for disambiguation; preserve ambiguity
until the semantic frame is stated or the sentence rewritten.
The domain operator limits the evaluation context of the simple
proposition rather than changing a local predicate into a
different truth-conditional claim about the world outside that
context.

Schematic, placeholder-bearing illustration:
`[NORMA]-in auti umande mov` = under that normative framework
a person grants me permission to move; the preposed `-in`
defines the domain, while governed `uman-de` after `aut`
remains the **source of permission**.

Neither connector-chain scope nor subordinate scope, stacked
domains, or lexical roots for hypothetical domains are
ratified here. Unisermo punctuation carries no grammatical
scope. Its typed parser recognizes a preposed locative phrase but
**preserves unresolved event/domain attachment** rather than declaring
whole-proposition scope from initial placement alone. See [noun_case_system.md](noun_case_system.md).


## Propositional bare serviles and `lim` scope (author ratification 2026-11-13)

The **root-only** propositional servile frame `SERVILE_ROOT FINITE_PROPOSITION` takes a finite clause, not a bare infinitive. Its initial semantically licensed instance is epistemic `pos`:

- `pos uman mova` — It is possible that the person moves.
- `pos uman mova e vida` — It is possible that the person moves **and** sees: `pos` scopes over both finite clauses.
- `pos uman mova lim e vida` — It is possible that the person moves, **and** the person sees: the already ratified `lim` closes the left proposition before `e`, keeping `vida` outside modal scope.

A preposed `no pos` negates the propositional modal, while `no` before a finite verb inside the operand negates that verb. This extends the uses of the already ratified closing `lim`, not the inventory of markers. Bare-root modal scope across `due`, `nam`, `ergo` or subordinate operators is not decided. The personal `posi mov` frame remains separate.


## Overt subject before a bare propositional servile (ratified 2026-11-13)

An attitude-holder or actor is placed **before** the bare servile root when a subject-bearing servile takes a finite proposition: `SUBJECT [no] SERVILE_ROOT FINITE_PROPOSITION`. For example `i vol u movu` means 'I want you to move'; `u sap i movdi` means 'you know I moved'; `i tent uman mova` means 'I try to bring about the person's moving'. The outer subject does not agree with the inner finite predicate. Pro-drop applies *inside* the subordinate finite clause when its own person marking identifies the subject, but the subject of the bare head is **not omitted**.

The currently licensed bare subject-bearing heads are `vol`, `int`, `tent`, `sap`, and `kred`. Epistemic impersonal `pos P` retains its separate frame. The existing closing `lim` before `e/o` delimits the propositional argument: `i vol u movu lim e vida` = [I want you to move] AND [someone sees], not I want both events. `i vol u movu e vida` applies the desire to the joint embedded expression. The parser remains fail-closed on mixed discourse/subordination; personless temporal operator suffixes Ø/d/f were subsequently ratified in LDR-0024.


## Personless propositional tense and necessity (ratified 2026-11-13)

The already accepted propositional-head slot extends regularly to `ROOT + TENSE(Ø/d/f)` for lexically licensed modal heads, without outer person/number suffix. The finite subordinate retains its own tense/aspect/person with its time reference anchored **relative to the outer assessment time**. `posd uman movfa` asserts a past possibility evaluation about a subsequent movement; `i vold u movu` expresses past desire toward contemporaneous movement. The newly licensed impersonally interpreted `deb P` means necessary(P) under the salient domain; `debi V` remains normative duty for the subject. `lim` continues to close the scoped operand before a following connective.

## Subject-only predicate ellipsis after `e` and `ma` (author approval 2026-11-14)

The compact pattern is **`S1 FINITE-V [ARGUMENTS] e|ma S2`**, where S1 and S2 are overt nominative subjects, the first clause is a simple finite declarative SVO clause, and S2 is a bare nominative subject phrase **without a spoken predicate**. The second clause inherits the same verb meaning, tense, aspect, and arguments as the first, with person/number controlled by S2.

- `adelo vida trenem e adele` = the brother sees the train **and the sister sees it too**; `e` copies polarity.
- `adelo vida trenem ma adele` = the brother sees the train, **but the sister does not**; `ma` reverses polarity **only within this licensed ellipsis**.
- `adelo no vida trenem ma adele` = the brother does not see the train, but the sister does.
- `adelo no vida trenem e adele` = neither the brother nor the sister sees the train.
- `i vidi trenem ma u` = I see the train, but you do not; the unspoken predicate agrees with `u`.

**Boundary:** `ma` remains an **adversative conjunction**, not a general negator, when joining complete clauses. Bare-subject polarity inversion is a special convention of contrastive predicate ellipsis. `e` never flips polarity. No omitted negative can be inferred merely from a different subject in an independently complete clause.

This rule is restricted to **one simple antecedent plus one bare second subject**, not arbitrary clause chains, fragment questions, omitted arguments without a second subject, negation at the end of a subject, or constituent extraction across conditionals. The typed parser exposes an `elliptical_clause` with recovered predicate/arguments and explicit polarity. Its number is left contextual when the nominal subject is unmarked. Punctuation has no grammatical scope effect.
