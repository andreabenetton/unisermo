---
id: LDR-0023
title: Subject-bearing bare serviles with independent finite propositions
status: Accepted
date: 2026-11-13
domain: grammar
supersedes: none
---

# LDR-0023 — Explicit subject, bare servile, finite proposition

## Context

After ratifying bare `pos FINITE_PROPOSITION` in LDR-0022, the author rejected putting personal agreement on a propositional attitude head. Instead the person or nominal subject appears before the invariant servile root: `i vol u movu`, with two independently identifiable subjects.

## Accepted decision

```
SUBJECT [no] SERVILE-ROOT FINITE_PROPOSITION
```

The outer nominal/pronoun subject is mandatory and belongs to the bare servile. Its dependent propositional operand has its own finite verb and optional independent subject (ordinary pro-drop). The head lacks person, number, tense, aspect by **current normative grammar**. Only the root is ratified for this propositional construction; speculative personless `vold`, `sapd`, `posd` and aspectual variants are not approved.

The new template is distinct from `SERVILE-FINITE BARE_VERB` (shared subject) and `pos FINITE_PROPOSITION` (subjectless epistemic possibility).

Semantically licensed overt-subject propositional heads initially: `vol` (desire P), `int` (adopted intention toward P), `tent` (actual effort toward P; does **not** entail P or causation), `sap` (factive knowledge P in positive affirmations), `kred` (non-factive belief P, existing confirmed lexical root). Others do not gain this frame by category membership alone.

- `i vol u movu`: I desire your moving.
- `i int u movu`: I intend your moving.
- `i tent uman mova`: I undertake an attempt aimed at someone's moving; outcome not entailed.
- `i sap uman mova`: I know the person moves; positive assertion entails embedded truth.
- `i kred uman mova`: I believe the person moves; truth not entailed.
- `u sap i movdi`: You know I moved.
- `i no vol u movu`: I do not want you to move.
- `i vol u no movu`: I want you not to move.

A shared-subject finite-head structure remains legal, including `voli mov`, `inti mov`, `tenti mov`, `sapi mov`. No new personal agreement, no complementizer, no general agent-causative. If a speaker expresses a desire or intention for another agent, it does not follow the other agent will comply.

As in LDR-0022, the bare root governs the complete following Boolean proposition until existing closing `lim` before a connective. Unmarked `i vol u movu e vida` scopes `vol` over both finite clauses; `i vol u movu lim e vida` asserts the right finite clause outside the desire.

## Alternatives

- `voli [u movu]`: rejected for this frame because the author explicitly chose bare `vol` preceded by `i`.
- Impersonal `vol u movu`: rejected because desire requires an identifiable desirer.
- New complementizer: not needed for an independently finite complement.
- Giving every existing servile the same propositional valency: not licensed semantically.
- Personless TAM (`vold`, `sapd`): deferred, not ratified by this decision.

## Parser conformance

Supports canonical subject NP/pronoun, bare head with finite operand, simple embedded predicates, Boolean e/o clauses and closing lim, and outer/inner negative scope. Does not infer agent identity from an omitted matrix subject; refuses unsupported nested/modally ambiguous scope. A bare `sap` knowledge frame is truth-entailing only under a positive outer head assertion, not under outer negation.

## Decision authority

Owner on 2026-11-13: 'io metterei il soggetto o il pronome davanti e lascerei invece la radice senza persona', followed by explicit 'ratifica e fai merge'. This ratifies the explicit-subject bare-root + finite proposition structure and the agreed three-frame contrast. It does not ratify optional personless tense suffixes or other propositional meanings not supported by prior examples.

## References

- `language/verb_specification.md`
- `language/word_order.md`
- `language/negation.md`
- `docs/ldr/LDR-0022-bare-propositional-serviles.md`
