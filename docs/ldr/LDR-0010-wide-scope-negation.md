---
id: LDR-0010
title: Negate coordinated propositions with no lim
status: Accepted
date: 2026-11-12
domain: grammar
supersedes: none
---

# LDR-0010 - Wide-scope propositional negation with no lim

## Context and problem

Canonical `no` immediately precedes the verb or predicate it negates. The
language also ratifies separate `e` and `o` coordination, exactly-one
alternative groups introduced by `o`, right-associated chains, and a
pronounced `lim` boundary before a subsequent connective. A previous
discussion demonstrated that local predicate negation must not be silently
reinterpreted as negation of the whole coordinated expression. For example,
`no vidi e movi` asserts both that I do not see and that I move; it does
not deny the conjunction of my seeing and moving.

The problem is how to assert NOT(P AND Q) without losing pro-drop or
introducing an ambiguous interpretation of the already accepted local `no`.

## Alternatives

1. Extend ordinary pre-predicate `no` automatically to whole chains:
   rejected because it changes existing sentences.
2. Require an overt subject to signal a wider scope:
   rejected because it compromises pro-drop and leaves structural ambiguity.
3. Add a new dedicated negative connective:
   not selected because accepted `no` and `lim` can express the distinction.
4. License the distinct two-token opener `no lim` while preserving ordinary
   local `no`: selected for the limited truth-conditional subset.

## Decision or hypothesis

Author accepts option 4. `no` immediately before a predicate stays local;
`no lim` immediately before an expression negates the entire following
complete proposition within the explicitly licensed `e` and `o`
connector-chain subset, including initial-`o` exactly-one groups.

- `no P e Q` = (NOT P) AND Q, when P is a simple predicate clause.
- `no lim P e Q` = NOT(P AND Q).
- `no lim P o Q` = NOT(P OR Q), where infix `o` is inclusive.
- `no lim o P o Q` = NOT(exactly-one(P,Q)).
- `no lim P e Q lim o R` = NOT(P AND Q) OR R.

A closing `lim` immediately preceding the outer connector terminates
the wide negative operand before that connector; without one, the operand
extends to the end of its enclosing expression. Existing right association,
spoken `lim` delimitation, and the irrelevance of comma punctuation remain.
Only the specially licensed `no lim` opener may place `lim` before the
following proposition; ordinary bare `lim P` remains ungrammatical.

This choice concerns truth conditions. It does not collapse adversative
`ma` into additive `e`. The scope or denial of the pragmatic/discourse
relations contributed by `ma`, `due`, `nam`, `ergo`, and subordinate
openers is not decided. Double negation, negative-focus enclitics, question
scope, arbitrary nesting, and modal scope are also not ratified here.

## Evaluation and evidence

Evidence is the author discussion of 2026-11-12 and the earlier
scope/disjunction ratifications of 2026-10-25, not a natural-language
comprehension experiment. Documentary tests record the minimal pairs
and verify the source hashes; independent truth-table checks verify the
specified two-valued Boolean interpretations on the limited subset.
Neither constitutes proof of human comprehension or full semantic parsing.

## Consequences and compatibility

Existing local `no`, optional subject omission, ordinary `e/o/ma`,
and `lim` before a connector retain their meanings. The exception is
the deliberately explicit `no lim` opener. No new roots are approved.
The current Phase 1 parser recognizes local pre-verbal negation only; it
must fail closed on unsupported coordinated propositions or wide scope.
A future AST and scope parser needs separately reviewed implementation.

## Decision authority

Approved by the project owner in the 2026-11-12 conversation:
after the concrete `no lim` proposal, the owner said "procediamo".
The accepted choice is limited to the precisely described subset;
this record does not infer acceptance of unresolved cases.

## References

- `language/negation.md`
- `language/word_order.md`
- `research/grammar/confirmed_decisions.json`
- `formalization/semantics/README.md`
- `tests/test_wide_negation_ratification.py`
- `docs/ldr/LDR-0003-semantics-preservation.md`
