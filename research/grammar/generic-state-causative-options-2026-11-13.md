# Generic causation of states: follow-up options (2026-11-13)

**Status: research proposal; NOT ratified.** This document records design options following acceptance of the `sap` family content/procedural valency (LDR-0019).

## Existing tools and what they actually say

- `mov` licenses a root-specific zero-marked alternation between motion of the subject and motion caused by an external subject, with the moved entity in `-em`. The approved grammar explicitly does **not** make this universal.
- `traes` already has a ratified causative transformation frame `Y traes X-em RESULT-da`, where `RESULT-da` is a *state or nominal/predicative role* achieved by X, not an event or ordinary recipient.
- `adsap` expresses the subject entering the state of knowing; its nominal accusative is the **known content**, never the person being caused to learn.
- `dok` is instructional action, not successful acquired knowledge.
- `sap + bare V` gives procedural know-how. Making someone *know how to V* is not automatically the same as making them perform V.

## Frame evaluation

### Option A — Reuse and generalize existing `traes` resultative predication (preferred to test)

```
CAUSER traes LEARNER-em KNOWLEDGE-STATE-da
```

For this to encode `causer makes learner know CONTENT`, the language must first define a productive **state-denoting predicate or nominalization** of the whole `sap CONTENT-em` proposition. The existing resultative `-da` cannot attach to an arbitrary full finite or infinitive clause as if it were a normal noun. A single `sapda` result would be underspecified (know *what*?) and `sap` is currently a verb root, not an automatically licensed resultative property.

Crucial questions: Can state clauses or state nouns be formed compositionally without inventing a new root? Does applying `traes` to an achieved knowledge state entail successful acquisition (yes, if its resulting state is actually established)? Can the construction also handle `kap`, `pot`, `san` under one general rule?

### Option B — Analytic event-level causative (new general operator)

```
CAUSE CAUSER [SUBORDINATE: LEARNER adsap CONTENT-em]
```

A distinct causative relator/verb connects a causer with a proposition; it could be productive for any event, not just knowledge. It is more general but needs explicit subject binding, clausal scope, negation, tense/aspect ordering and counterfactual vs successful causation. No such operator is ratified here. Avoid adopting one from a single `sap` example.

### Option C — Zero-marked transitivity of every state/change root (reject)

`CAUSER adsap LEARNER-em` is ambiguous with the already accepted content accusative `KNOWER adsap CONTENT-em`. The same issue can recur for other roots and breaks the fail-closed valency approach. Do not silently replicate `mov`'s root-specific causative frame.

## Minimum tests before owner decision

1. T teaches P, but P never learns: `dok` true, successful causation false.
2. T causes P to acquire concept C: `causation` true and P's `adsap` result true.
3. P spontaneously acquires C, T is only present: `adsap` true, caused-by-T false.
4. T makes P rehearse C, but P doesn't acquire it: study/teaching may occur, successful causation false.
5. T causes P to forget C: generic causation of `desap`, not 'teach forgetting'.
6. T causes P to understand C: generic causation of `kap`, independent of knowing.
7. T intends P to learn but fails: intention not causation.
8. T persuades P to act but P decides not to: communicative influence not actual action.
9. T causes P to learn how to teach: requires binding to `adsap dok`, not actual `dok`.
10. Two stages: T makes P study and P independently learns later; do not infer direct successful causation of learning from temporal succession.

## Provisional recommendation

Prefer a *general construction that reuses* `traes` and `-da` for **result states** if the predicate can be stated without encoding a new root-specific exception. Keep the more general event-level causative separate if later necessary. No new root, grammar change, or parser support is authorized by this research file.
