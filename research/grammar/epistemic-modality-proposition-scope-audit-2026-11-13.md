# Epistemic possibility and necessity: proposition-scope audit (2026-11-13)

**Status:** research, not ratified.

## Central distinction

Unisermo's `pos` is circumstantial opportunity for the grammatical subject to act; `pot` is participant capacity; `deb` is normative duty. In 'perhaps the train arrived', 'it is probably raining', 'the train must have arrived given the evidence', the **speaker assesses truth of proposition P** rather than granting the actor an opportunity, capacity or duty. The actor may be absent, inanimate or have a different person from the speaker.

Existing `kred` (believe), `sert` (certain), `nam` (evidential justification) and `ergo` (inference) are relevant but do **not** by themselves establish a fully compositional syntax for 'possibly P / probably P / necessarily P' with P as independently scoped complete proposition. The availability of an adjective 'certain' is not evidence a unary certainty operator with defined scope and semantics exists.

## Minimal contrasts

1. I am permitted to leave (`aut`) vs perhaps I left (speaker probability).
2. I have a chance to leave (`pos`) vs perhaps somebody else left (speaker probability).
3. I am obliged to leave (`deb`) vs judging from evidence I must have left (epistemic necessity).
4. I can lift the stone (`pot`) vs the stone may have been lifted (speaker uncertainty).
5. The event is logically possible, yet the speaker believes it false.
6. The speaker believes P likely, yet P does not occur.
7. P is true, yet the speaker assigns low confidence.
8. P is statistically likely, yet the speaker cannot establish its truth.
9. P is necessarily true given premises, but not a normative duty.
10. The machine must cool to survive (physical/conditional necessity, not obligation).
11. I know P (`sap` content state) vs I am certain that P (confidence may differ from knowledge).
12. 'P because Q' (`due`) vs 'P, because I have evidence Q' (`nam`) vs 'Q, therefore P' (`ergo`).
13. Negated epistemic possibility NOT POSSIBLE(P) vs POSSIBLE(NOT P), not interchangeable.
14. Probably(P or Q) vs Probably(P) or Probably(Q), generally not equivalent.
15. Speaker likely(P) vs Agent likely(V), distinguished by embedding level.
16. Time of speaker assessment vs tense of embedded proposition.

## Architectures

A. **Reuse same-subject serviles** by overloading `pos/deb`. Reject: wrong subject and a harmful logical collapse between deontic, dynamic and epistemic modalities.

B. **Evidence/credence ordinary verbs**, e.g. `kred` + full content clause. Potentially expressive, but requires explicit clausal argument syntax and preserves distinction between assertion of belief by a participant vs speaker's truth-confidence qualification. Check possibility of using `sert` as a predicate without inventing new scope rules.

C. **New proposition-scope operators**, not necessarily serviles. Candidate system possible(P), probable(P), necessary(P), with explicit operand boundary (perhaps adapting existing `lim` but without changing its ratified roles). Cleanest scope if new syntax is justified. No new root is proposed or ratified yet.

D. **Probability as frequency / statistical property**. Useful only for event-types with repeatable distributions. Does not solve unique factual uncertainty ('perhaps the train arrived'), so cannot be the only solution.

## Recommendation

Prioritize distinct syntax for speaker epistemic evaluation of a **full proposition**. Do not approve extra ordinary servile roots before the syntax is known. The intention issue (`vol` vs proposed `int`) is separate and may be solved within shared-subject servile syntax. Negation and `lim` boundaries require explicit truth-conditional tests.

**No canonical grammar, parser or lexicon changes in this audit.**
