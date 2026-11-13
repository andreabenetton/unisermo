---
id: LDR-0022
title: Bare servile heads governing finite propositions, first instance pos
status: Accepted
date: 2026-11-13
domain: grammar
supersedes: none
---

# LDR-0022 — Propositional root-only servile frames

## Context and problem

The author proposed the compact `pos uman mova` in place of an unmotivated third-person `posa [P]`, because a proposition-scoped possibility assessment lacks an autonomous third-person subject. The author subsequently explicitly ratified the general rule of two complement forms for serviles, and specified `pos uman mova lim e vida` to close modal scope before coordinating a separate assertion.

## Alternatives

1. `posa P` with third-person finite agreement: rejected for the impersonal proposition-level reading, since no referent supplies its personal ending.
2. Dedicated complementizer: unnecessary for simple finite P; no new marker accepted.
3. `SERVILE_ROOT FINITE_PROPOSITION`: accepted as a distinct frame from `SERVILE_FINITE BARE_VERB`.
4. Universal semantic conversion of all serviles: rejected pending lexical-semantic evaluation of who has desire, capacity, permission, duty or knowledge. No automatic bare `vol/int/tent/deb/pot/aut/sap P` interpretation is ratified.

## Decision or hypothesis

There are two distinct complement structures:

```
[SUBJECT] SERVILE-FINITE BARE_VERB [ARGS]
[no] SERVILE-ROOT FINITE_PROPOSITION
```

The second has no person marking on the operator; the embedded proposition bears its own normal finite subject/TAM and can differ from any discourse participant. Its semantic interpretation requires a specifically licensed servile. The first confirmed instance is `pos P` = it is epistemically possible that P. `pos P` does not entail P. The personal `posi V` remains situational opportunity for the participant.

The operator takes the complete following Boolean propositional expression by default. The already accepted `lim`, placed **immediately before a following connective**, delimits the modal operand. Thus:

- `pos uman mova e vida` = POSSIBLE(P AND Q).
- `pos uman mova lim e vida` = POSSIBLE(P) AND Q.
- `no pos uman mova` = NOT POSSIBLE(P).
- `pos uman no mova` = POSSIBLE(NOT P).
- `no pos uman no mova` = NOT POSSIBLE(NOT P), hence NECESSARY(P) for the same possibility domain.

Ordinary `no` directly before `pos` negates the assessment, while `no` within the finite operand negates the embedded predicate. This construction is separate from `no lim` wide Boolean negation. Scope of mixed causal, evidential and subordinate operators remains open.

## Evaluation and evidence

Dedicated executable tests check the modal/embedded clause AST, personal and impersonal distinctions, pro-drop and independent subject agreement, both negation positions, `lim` closure before `e`, nested simple Boolean operands, and invalid bare `pos` without a finite operand. Other bare-root servile interpretations and unratified `posd` past assessment must not be silently parsed as approved modal operators.

The author proposed applying the tense suffix directly to a bare propositional operator (`posd P`). That is a **follow-up proposal**, not approved by the two complement-frame ratification; it needs a separate decision about the temporal reference of the evaluation relative to the embedded proposition and about whether personless operator TAM is generally productive.

## Consequences and compatibility

No new person ending, conjunction, case or scope marker. `lim` retains its previously ratified closing-boundary position; modal operand trees integrate with the same binary connector AST. The existing single-head finite servile `posi V` continues unchanged. Only `pos` has a confirmed epistemic propositional meaning. Others must be considered separately; `deb P` is not automatically either deontic or logical necessity, `sap P` must not silently assume unknown knowers, and `pot P` must not silently adopt a nonsensical stative ability.

## Decision authority

Owner (2026-11-13): '3a la frase 2 la renderei con `pos uman mova lim e vida` ... 5 regola ratifciata', referring explicitly to the proposed distinct `SERVILE-FINITO VERBO-ROOT` and `SERVILE-ROOT PROPOSIZIONE-FINITA` frames. The owner asked for practical examples on other serviles and the past suffix, but did not ratify those further semantic/TAM extensions.

## References

- `language/verb_specification.md`
- `language/word_order.md`
- `language/negation.md`
- `formalization/parser/proposition.py`
