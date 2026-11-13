---
id: LDR-0019
title: Compositional knowledge acquisition via the sap phase family
status: Accepted
date: 2026-11-13
domain: semantics-grammar
supersedes: none
---

# LDR-0019 — Knowledge state, acquisition, retention, loss, reacquisition

## Context and problem

Following exploration of `dok` teach, `stud` study, `sap` know, `kap` understand and a provisional `lern` root, the project owner requested a **sap-first systematic analysis** parallel to the compositional `mov` family. This proposal tests whether `sap` plus pre-existing phase and aspect operators can capture "learn" without adding a primitive.

**Decision authority:** On 2026-11-13, the owner instructed implementation of the five recommended extensions. This approves frames A/B, phase-acquisition readings, the independence of `dok` and `stud`, and deferral of `lern`. The generic causative remains unratified.

## Observations from normative specification

1. `sap` is an independently confirmed verb meaning possess knowledge. Existing `sap + bare verb` expresses *know how to V* (procedural knowledge).
2. `ad-`, `in-`, `de-`, `re-` are already confirmed phase morphemes: enter/begin, remain/continue, leave/cease, return/resume. The phase family `adsap`, `insap`, `desap`, `resap` is explicitly listed in `language/derivation.md`.
3. `-e-` progressive and `-o-` completed/perfect are independent TAM slots. `adsapei` parses `ad-sap-e-i`.
4. The intransitive/transitive **causative** alternation of `mov` is *root-specific*, and must NOT be applied mechanically to `sap`.
5. `dok` describes teaching activity, not a guaranteed learning result; `stud` describes study activity, not a guaranteed acquisition result.

## Alternatives

1. Introduce an independent `lern` root for learning; defer because the existing `sap` phase family may cover successful acquisition.
2. Extend content/procedural knowledge frames uniformly to the phase family (accepted).
3. Reuse `mov` zero-marked causative for `sap` (rejected due to argument ambiguity).

## Decision or hypothesis

The `sap` family licenses nominal knowledge content in accusative and a bare verb as shared-subject know-how complement. The learner/knower remains subject in both frames.

## Proposed lexical-valency frames

These frames would **extend** the existing procedural frame from `sap` to its regular phase derivatives, preserving the learner/knower as subject and the content role as complement.

### A: Propositional or nominal knowledge

```text
LEARNER/KNOWER-NOM KNOWLEDGE-HEAD CONTENT-em
```

A content NP in accusative names the fact, information, subject matter or concept that the subject knows or comes to know. It is **never** the person caused to learn. This applies to `sap`, `adsap`, `insap`, `desap`, `resap`; the precise lexical category of a *proposition* as opposed to a nominal concept is deferred. If CONTENT is an information object, knowing its *existence* vs knowing *what it says* must be disambiguated before assigning gold.

### B: Procedural knowledge (extended from ratified sap + bare verb)

```text
LEARNER/KNOWER-NOM KNOWLEDGE-HEAD BARE_LEXICAL_VERB
```

The dependent bare verb denotes the action whose **know-how** is possessed/acquired/retained/lost/regained. It shares the head subject, as in the established `sapi mov`. The dependent verb is NOT a second finite predicate and is NOT interpreted as an action performed merely because the knower knows how to perform it. Compound subject roles should be distinguished from implicit argument roles of the dependent action.

Proposed regular interpretations:
- `sapi dok` = I know how to teach (existing ratified frame).
- `adsapi dok` = I acquire know-how to teach.
- `adsapei dok` = I am in the process of acquiring know-how to teach; does not entail I can already teach or that I will ultimately succeed.
- `insapi dok` = I continue to know how to teach.
- `desapi dok` = I cease to know how to teach.
- `resapi dok` = I regain know-how to teach.

### C: No generic causative via bare accusative

`Y adsap PERSON-em` MUST NOT be interpreted as 'Y teaches PERSON' or 'Y makes PERSON learn'. In frame A, accusative is **content**, not learner; in frame B, bare verb is **procedure**. A future causative across stative roots (not only sap) requires a distinct, regular construction or explicit morphological operator, and an independently specified semantic entailment.

## Interpretation of 'learning'

An event of completed acquisition of knowledge is naturally expressible via `adsap`. Progressive `adsapei` can describe an ongoing **transition toward** knowledge and does NOT entail the resulting knowledge has been attained at the reference time. Some long-term skill development may be imperfectly captured by a phase-of-state transition; identify counterexamples before concluding `lern` is unnecessary universally.

- `stud` = study / deliberate systematic engagement: can happen without `adsap`.
- `dok` = teach: can happen without `adsap` by learner.
- `adsap` = knowledge acquisition: may happen without `stud` or `dok`.
- `kap` = understand: not necessarily equal to lasting `sap`.
- `desap` = loss of knowledge: contextual 'forget', but need not indicate psychological cause or short-term lapse in recall.
- `resap` = renewed possession of knowledge: contextual 'remember', 'relearn', but not always one or the other.

## Morphological controls

`adsapi = ad + sap + i` (present 1sg).
`adsapei = ad + sap + e + i` (progressive 1sg).
`adsapdi = ad + sap + d + i` (past simple 1sg; do not gloss automatically as English present perfect).
`adsapoi = ad + sap + o + i` (completed/perfect aspect 1sg).

No separate verbal morpheme is approved for *learning activity* or a separate `lern` root. The fact that one can construct a derivation does not license all of its proposed argument types. Nothing here should change phase morphology.

## Evaluation and evidence

The approved design is associated with 16 experimental contrast probes; execution of parser tests and formalization validation is tracked separately. No assertion of empirical LLM success is made.

## Falsifiable contrast criteria

1. `dok` can be true while learner `adsap` is false.
2. `stud` can be true while `adsap` is false.
3. `adsap` can be true without `dok` or `stud`.
4. `adsapei` can hold while completed acquisition is false.
5. `sapi V` does not entail `V` was performed, nor physical `poti V` or circumstantial `posi V`.
6. `desap` does not entail never having known.
7. `resap` presupposes prior knowledge and an interruption (though not its cause).
8. `kap` and `sap` differ on comprehension versus knowledge possession.
9. `sap CONTENT-em` must not parse as causation of CONTENT or make a different actor learn.
10. `adsap V` must be identifiable as a single headed procedural-knowledge construction, not two independent verbs.

## Open issues

- Do nominal-content knowledge complements need explicit subtypes for known-fact vs familiar-with subject matter? 
- How are full *that P* factual subordinate clauses represented using the existing clause-linking system? Do not invent new complementizers here.
- Does entry into procedural know-how always represent a telic achievement, or can progressive phase onset be temporally extended?
- Is `adsap` sufficient for all ordinary learning contexts, including implicit statistical learning that has no clearly stable know-how?
- How to express causing another person to know, distinct from teaching?
- Whether the language allows omission of an overt content complement without ambiguity; baseline proposal requires overt complement in parser tests except canonical `sap V`.

## Consequences and compatibility

This narrows the parser to two knowledge-specific roles without adding a general causative or the root `lern`; it preserves `dok` and `stud` as separate activities and leaves propositional subordinate knowledge complements for a later decision.

## Implementation / evaluation gates

Before owner acceptance: review semantic frames, consult the existing parser categories for bare verbs vs content NP, ensure collision-free cases, and independently verify 16 contrasts in `research/grammar/sap-family-contrasts-001.json`.

Implementation includes a normative valency section in `language/verb_specification.md`, machine-readable frames in `formalization/data/valency_frames.json`, and a bounded parser extension with regression tests. Full build/validation is required before claiming executable verification.

## Decision authority

The owner approved proceeding with the five enumerated valency decisions on 2026-11-13. This LDR records their acceptance. The generic causative remains outside the ratification.

## References

- `language/verb_specification.md`
- `language/derivation.md`
- `formalization/data/valency_frames.json`
- `docs/ldr/LDR-0011-servile-negation.md`
