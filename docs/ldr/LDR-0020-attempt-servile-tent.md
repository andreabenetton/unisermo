---
id: LDR-0020
title: Ratify tent as a goal-directed attempt servile
status: Accepted
date: 2026-11-13
domain: grammar
supersedes: none
---

# LDR-0020 — Attempt servile tent

## Context and problem

The project owner requested a productive distinction between wanting an event, attempting it, and completing it across the language, instead of separately lexicalizing every deliberate/accidental verb pair. The owner observed that `tent` behaves like a servile and expressly instructed the assistant on 2026-11-13 to introduce it.

## Alternatives

1. Make `tent-` a bound aspect or intentionality prefix: rejected because attempting an event is not ordinary temporal aspect and does not ensure the event happens.
2. Reuse `vol`: insufficient, since merely desiring an event need not involve an effort.
3. Reuse `fin`: insufficient, since an action performed for a purpose need not constitute an attempt to carry out that purpose at that time.
4. Introduce `tent` as an ordinary finite servile governing an uninflected dependent verb: accepted, with existing local negation scope and subject sharing.

## Decision or hypothesis

`tent` means **undertake a real goal-directed attempt to perform or realize the dependent event**, and uses `[SUBJECT] [no] tent-FIN [no] BARE_VERB [DEPENDENT ARGUMENTS]`. The shared subject and finite TAM apply exactly as for other serviles. The action referred to by the dependent root is a goal and **not asserted to have occurred**. Attempting entails some effort but does not entail success, feasibility, competence, authorization, or knowing how.

Contrast `voli mov` (want to move), `tenti mov` (try to move), `movi` (move). `no tenti mov` denies undertaking an attempt; `tenti no mov` asserts a purposeful attempt to refrain from moving. There is no implication that failure occurred when someone makes an attempt, and failure to act is not proof of an attempt.

`tent` is distinct from `ten` ('hold/maintain constraint'), remains a four-letter word, and has no blanket causal or intentionality scope over other consequences of the subject's actions. A motion caused unintentionally by a successful attempt at something else remains unintended unless separately specified.

## Evaluation and evidence

Positive executable cases include: `tenti mov`, `tentdi mov`, `tentei mov`, `tenti portar akwaem`, `no tenti mov`, `tenti no mov`, `tenti adkap`. Reject bare `tenti`, unsupported dependent arguments, and stacked serviles such as `tenti voli mov` in the current parser subset. These are syntax/AST checks, not empirical proof of success or failure of real events.

The finite `tent` head contributes a recorded attempt event to the semantic AST, with `entails_attempt=true` and `entails_success=false`. The existing `no` before the head negates the attempt itself; the flag refers to the **positive lexical operator** and should not be interpreted as truth-conditional entailment in a *negated clause*. The truth-conditional interpretation still depends on head polarity.

## Consequences and compatibility

No new tense, aspect, case, causative or negative morphology is introduced. Other serviles remain unchanged. This does **not** retire `stud` and does not license chaining two serviles or a second subject. It does not specify a global intentionality flag. The closeness of `tent` and `ten` merits listening tests, but they are phonemically distinguishable.

## Decision authority

User: 'si introduciamolo e cerchiamo di capire se abbiamo bisogno di altri servili', following acceptance of the proposed servile interpretation of `tent`, on 2026-11-13. Approval applies only to `tent`, not to additional candidate serviles.

## References

- `language/verb_specification.md`
- `language/negation.md`
- `formalization/parser/proposition.py`
- `research/lexicon/confirmed_lexicon.json`
- `research/grammar/servile-inventory-audit-2026-11-13.md`
