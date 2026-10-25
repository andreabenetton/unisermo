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

Both `P due Q` (effect followed by its causal explanation) and `due Q, P` (fronted causal clause followed by effect) are accepted. In either order Q is the cause and P the effect. `Q, ergo P` instead presents P as an inference/conclusion. General subordinate nesting and delimiter rules are not yet implemented in the restricted Phase 1 parser; no silent acceptance of unparsed forms is implied.


## Factual concessive `etsi` (ratified 24 October 2026)

`etsi` introduces an accepted/factual concession: `etsi P, Q` ('although P, Q') and `Q etsi P` ('Q, although P') are both permitted, with P the conceded proposition and Q the contrasting outcome. Distinguish conditional `se` (IF) and adversative `ma` (BUT). The hypothetical reading 'even if P were to happen' is not automatically ratified. The restricted Phase 1 parser does not yet implement compound concessive clauses.


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

`lim` must immediately precede the connector whose left operand it delimits; it cannot be sentence-initial, sentence-final, or placed between a connective and its complement. Thus `P e lim Q`, `lim P e Q`, and `P e Q lim` are invalid in this subset.

These examples establish the approved **ordinary connector-chain convention**; they do **not** authorize arbitrary combinations of subordinate forms, unrestricted nesting, or a general clause grammar. Existing ratified semantic distinctions of `due`, `nam`, `ergo`, `etsi`, `etsise`, and `eksese` are preserved; their subordinate boundaries and scope constraints await separate formalization. The inclusive/exclusive semantics of `o` remain undecided. Authors and LLM generators should prefer short, linear periods to deep nested structures. The current Phase 1 clause parser **does not implement** these connective-chain constructions and must continue to fail closed rather than infer undocumented structures.


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

**Explicitly still open:** exact parsing and delimitation of fronted `due` causes and other `nam` epistemic explanations in arbitrary compound clauses; interaction of complex postposed subordinate arguments with following connectors; mixed subordinate/coordination scope outside the templates above; disjunction inclusivity, wide-scope negation, and modality. These are not implied by this ratification. The existing Phase 1 clause parser does **not** yet recognize general compound or nested subordinate ASTs and must fail closed pending a separately reviewed implementation.


## Inclusive and exclusive `o` (author ratification 25 October 2026)

The free connector `o` has two **distinct constructions**, without introducing a new word:

- `P o Q` — **inclusive disjunction**: at least one alternative is true; both may be true.
- `o P o Q` — **exclusive choice**: exactly one alternative is true.
- `o P o Q o R` — **exclusive choice over three alternatives**: exactly one of P, Q, R is true. This is an n-ary exactly-one operator, **not** iterated binary XOR (odd parity).

The initial standalone `o` signals the exclusive-choice construction. Further standalone `o` tokens separate its alternatives. Ordinary infix `o` remains inclusive outside this construction. Alternatives must be complete propositional expressions. At least two alternatives are required for the exclusive-choice construction.

In the licensed ordinary connector-chain subset, existing right association is retained: `o P o Q e R` denotes exactly one of P and `(Q e R)`. The existing explicit scope boundary `lim` may close an exclusive-choice group immediately before a following connector: `o P o Q lim e R` denotes `(exactly-one(P,Q)) e R`. `lim` is spoken/written and retains its already ratified role; commas do not change scope.

For all n >= 2, an exclusive-choice expression is true iff **exactly one** alternative is true; it is false if none or two or more alternatives are true. The inclusive `o` requires at least one true alternative. These are truth-conditional propositional semantics; they do not automatically impose a real-world obligation, make alternatives mutually physically possible, or settle any previously open question about modality or conversational implicature.

Detailed interactions with nested subordinate scope, postposed subordinate clauses, negation of whole propositions, and unrestricted connector grammars remain outside this ratification and the current Phase 1 parser, which must fail closed for unsupported compound constructions.
