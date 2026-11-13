---
id: LDR-0021
title: Separate volitional desire from intended action
status: Proposed
date: 2026-11-13
domain: grammar
supersedes: none
---

# LDR-0021 — Desire, commitment to act and attempt

## Context and problem

The current confirmed lexical specification defines `vol` as "want; desire/intend to perform an action." This combines distinct commitments: one may desire a journey while deciding not to undertake it, or intend an unpleasant medical intervention one does not desire. The author approved `tent` as the regular servile for **actual goal-directed attempt**, leaving a gap between wanting and already trying.

No owner ratification of a separate intention root has occurred. This is a research decision candidate, not executable grammar.

## Alternatives

A. **Keep polysemous `vol`.** Minimal roots but fails to unambiguously express "I want V, but I have decided not to do V" without additional narrative.

B. **Use `vol` plus `fin`.** `fin` supplies a purpose for a performed action or describes a purpose phrase. It does not independently assert a decision to undertake V; even a future-oriented wish can have a purpose. Not a semantic equivalent of intending.

C. **Use a separate ordinary lexical verb for decide/commit and subordinate event complement.** Potentially more economical in grammar because 'decide' has uses that are not same-subject actions (decide that P; decide an outcome; collective decision). But existing grammar lacks a ratified subordinate complement frame that binds a decision to a future action. A new ordinary verb still requires valency/scope work.

D. **Candidate short same-subject servile `int` (international intention family).** `int-FIN V` represents a currently adopted plan/commitment to attempt/perform V; does **not** entail present attempt, past success, or present desire. The form is only a **candidate**, not a lexical approval; confirm pronunciation, collisions and recognizability independently. `int` would match the current servile syntax, but excludes decisions about other agents and full propositions until a separate syntax is defined. It must not duplicate `tent`.

## Decision or hypothesis

**Recommended for owner review:** narrow `vol` to desire (wanting) and reserve a distinct value for *adopted intention*. The most economical provisional prototype is **`int`** as a regular shared-subject servile, but it should only be approved after testing whether an ordinary decision verb would give broader compositional coverage with less total complexity.

Candidate semantics with `V` the same-subject dependent action:

- `voli V` = I want V; no decision/attempt/performance entailed.
- `inti V` = I have formed a genuine intention to do V; no attempt/performance entailed. Desire need not hold.
- `tenti V` = I actually try V; effort but no success entailed.
- `V-FIN` = V actually occurs (with its own event valency and TAM).

`int` is proposed as **intention to act**, not as a promise, prediction, likelihood estimate, guaranteed event or a mere desire. These should not collapse into one English-style modal. Intentions can be abandoned or frustrated. A decision to refrain is not equivalent to lacking an intention: `inti no V` differs from `no inti V`.

A strong ordinary default is: a deliberate `tent V` entails a **goal-directed intention operative in that attempt**, but not necessarily a durable prior plan. This may warrant an *event-local* goal/commitment predicate, not a lasting `int V` state; do not impose that every attempt presupposes a prior explicit conscious decision.

## Evaluation and evidence

Contrast probes recorded in `research/grammar/intention-desire-contrast-fixtures-001.json`. The following are **schematic**, not parser-recognized nor ratified:

1. `voli mov`, but `no inti mov`: desire without plan.
2. `inti mov`, but no ongoing `tent`: decided to move later, not started.
3. `inti no mov` vs `no inti mov`: intend to refrain vs no intention to move.
4. `tentdi mov`, unsuccessful movement: real attempt without achievement.
5. `movi` but no prior `int`: unplanned movement, whether reflex, accident or impulse.
6. `inti mov` while `no voli mov`: reluctant obligation accompanied by committed decision.
7. `debi mov` and `no inti mov`: obligation is not the agent's intention.
8. `auti mov` and `no inti mov`: permission is not intention.
9. `posi mov` and `no inti mov`: opportunity is not intention.
10. `inti mov` and later abandonment: past intention can be true even when action never follows.

## Consequences and compatibility

The lexical ambiguity of `vol` is exposed; changing its approved sense requires separate explicit ratification and source/index updates. Existing `tent` stays unchanged. Proposing `int` does not change parser MODALS, lexicon or source-linked indexes yet.

A generic all-agent intentionality marker (intentionally causing event E) should not be equated with intention to perform same-subject V. It requires event identity, responsible agent and causally downstream side effects. `int V` cannot directly assert an intention about someone else's action.

## Decision authority

Research initiated after the owner's instruction to continue examining additional serviles, 2026-11-13. **No approval of `int` or revision to `vol` has yet been given.**

## References

- `language/verb_specification.md`
- `docs/ldr/LDR-0020-attempt-servile-tent.md`
- `research/grammar/servile-inventory-audit-2026-11-13.md`
- `language/noun_case_system.md`
