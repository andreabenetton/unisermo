---
id: LDR-0024
title: Proposal for personless modal tense and propositional necessity
status: Proposed
date: 2026-11-13
domain: grammar
supersedes: none
---

# LDR-0024 — Personless modal tense and short propositional necessity

## Context and problem

The owner accepted (LDR-0023) explicit subject plus invariant bare head plus independently finite clause, e.g. `i vol u movu`, and confirmed impersonal epistemic `pos P` (LDR-0022). Open questions were whether `posd` and `vold` should take regular tense without person and whether `deb P` should provide a concise necessity construction instead of `no pos no P`. The owner instructed further investigation, **not explicit ratification of these proposals**.

## Alternatives

1. Use `no pos no P` exclusively for necessity. Logical duality holds under a shared modal accessibility domain, but frequent doubly negated speech is cumbersome. Unacceptable as the sole everyday necessity expression.
2. Use `deb P` for non-deontic propositional necessity, retaining `deb-FIN BARE_VERB` for subject obligation. No new root; distinct syntactic valency and modal domain, but ambiguity may persist unless sources/conditions are explicit. **Recommended for ratification** as a constrained distinct sense.
3. Add a separate short necessity root. Semantically explicit but increases lexical inventory. Hold pending evidence that `deb P` leads to unacceptable polysemy.
4. Express past assessment through a finite third-person head (`posda P`): invents a fictitious personal subject; not preferred.
5. Extend `ROOT + TENSE` without person for propositional serviles (`posd`, `vold`, `sapd`). Productive morphological economy with clear syntactic cues. **Recommended for ratification**, initially only tense Ø/d/f, not aspect.
6. Make dependent tense absolute relative to speech-time vs relative to modal assessment-time. **Recommend relative evaluation-time interpretation** for complement finite TAM in this frame. This needs explicit examples and semantic specification, because ordinary root-level tenses elsewhere continue to use their previously established anchoring rules.

## Decision or hypothesis (proposed only)

Personless propositional servile head:

```
[SUBJECT [no]] LICENSED_SERVILE_ROOT + TENSE(Ø/d/f) + FINITE_PROPOSITION
```

- `pos uman mova`: possible, relative to speech-time, that person moves.
- `posd uman movfa`: at a past assessment time it was possible that person move later relative to that time.
- `posd uman movda`: at a past assessment time it was possible that person had moved earlier than that time.
- `posf uman movda`: at a future assessment time it will be possible that person had moved before that future time.
- `i vold u movu`: at past time I wanted your movement contemporaneous with that past assessment.
- `i sapd u movda`: at past time I knew that your movement had already happened earlier. Factive knowledge applies to proposition at evaluated time if asserted positively.
- `i vold u movfa`: in the past I wanted your movement to take place after that desire.

Do **not** automatically extend aspect: `pose/poso` imply an unsolved distinction between ongoing, perfect and punctual modal states. Nor allow omission of an outer subject with `vol/int/tent/sap/kred`; the root-only head remains subjectless only where lexical semantics licenses an impersonal evaluation (`pos`, candidate `deb`).

If the short necessity proposal is accepted:

- `deb uman mova` = necessary that the person move/does move under the salient modal premises, **not** automatically a legal or moral obligation on the person.
- `debi mov` = I am obliged to move (existing personal normative reading).
- `no deb uman mova` = not necessary that the person move; not equivalent to impossible movement.
- `deb uman no mova` = necessary that the person not move, relative to the same modal domain.
- `no pos uman no mova` = equivalent to `deb uman mova` **only with fixed shared accessibility domain and nonempty admissible worlds**.
- Physical law, logical inference, normative rules and available evidence can yield different necessity judgments. The domain must be recoverable from context or expressly identified by an existing properly licensed domain construction; no universal shift of `deb` is implied.

No probability servile is ratified here. Existing `prob` lexeme means *morally good*, so it must **not** be silently reused for statistical/propositional probability. Potential `lik` remains merely a candidate; a probability operator should distinguish event likelihood from confidence/credence (`kred`), frequency, logical possibility and truth.

## Evaluation and evidence

See `research/grammar/personless-servile-tense-necessity-cases-2026-11-13.json` for diagnostic contrast pairs. Before approval/implementation, test:
- Temporal reference of nested modal and embedded predicates, including a past judgment of then-future event.
- Negative scope under both proposed `deb` and existing `pos`, and `lim` closure.
- Pronoun/no-pronoun valency; no accidental ambiguity with standard finite forms `posdi` / `voldi`.
- Non-factivity of `pos/deb/kred/vol` and positive factivity of `sap`.
- Interactions with explicit time phrases and independently ratified locative domain extension without silently broadening the parser.

All examples are **proposed, not executable canonical grammar**. The main parser must continue to reject `posd`, `vold` and bare `deb P` until explicit owner ratification.

## Consequences and compatibility

No new root or particle is needed for proposed past/future or necessity. A new optional-person morpheme slot is not being generalized to ordinary finite lexical verbs: only licensed propositional heads can be personless, preserving the existing finite morphology. The proposed temporal reference is an interpretation rule confined to the embedded proposition, and must be reviewed against existing general tense semantics before ratification. Longer compound propositions still follow existing `lim` boundary rules and fail-closed unsupported mixed scope.

## Decision authority

This is a design proposal in response to 'procediamo' on 2026-11-13, following the merge of LDR-0023. The owner previously proposed 'usare pos+suffisso passato ?' and expressed a preference for a short necessity servile, but did **not** explicitly ratify the exact temporal reference convention or new `deb` propositional semantics. This LDR remains **Proposed** until approval.

## References

- `docs/ldr/LDR-0022-bare-propositional-serviles.md`
- `docs/ldr/LDR-0023-subject-bare-servile.md`
- `language/verb_specification.md`
- `language/noun_case_system.md`
- `research/grammar/epistemic-modality-proposition-scope-audit-2026-11-13.md`
