---
id: LDR-0025
title: Unified gradable property semantics with qualitative or numerical degrees
status: Accepted
date: 2026-11-13
domain: semantics-grammar
supersedes: none
---

# LDR-0025 Unified qualitative and quantitative degrees

## Context and problem

A prospective probability root exposed an artificial dichotomy: 'P is likely' versus 'P has a degree of probability' was presented as if these required two lexical meanings. The author rejected that distinction as a **translation problem**, and explicitly ratified the unified scalar-property account.

## Alternatives

1. Separate 'probably' and 'probability' roots: rejected as redundant unless a genuinely distinct semantic function is later established.
2. A bare root with an independently enumerated fixed numeric threshold (e.g. `lik P` entails chance > 50%): rejected as a gratuitous lexical implication.
3. One gradable lexical property, capable of accepting qualitative and, where meaningful, quantitative specifications: **accepted**.
4. Make all properties measurable with numerical precision: rejected, since some scales have no agreed unit or reproducible measurement.

## Decision or hypothesis

**One scalar property has one lexical meaning**. The unmodified predicate can be translated idiomatically into the target language; translation variation is not evidence of distinct Unisermo meanings. Qualitative grading and precise numerical measurement specify the **same underlying scale**. Numerical degree must be semantically licensed by the property, its measurement unit/reference convention and value range. No new lexical duplication is needed merely because Italian/English distinguish an adjective/adverb from a noun of measurement.

Confirmed qualitative mechanisms remain `minu`, `pok`, `ase`, `mult`, `ekstrem` (degree), `suf` (threshold), `major/minor/ekwal/masim/minim` (comparison). Existing fractions/percentages `CARDINAL ORDINAL` remain the means of spelling numerical ratios: `kin senim` means five hundredths / 5%.

For an **eventual future probability property**, schematic noncanonical examples express one scale only:

- `LIK P`: property of P on the probability scale, no stipulated numeric percentage threshold.
- `pok LIK P`: small degree on that scale.
- `mult LIK P`: high degree on that scale.
- `LIK [kin senim] P`: numeric specification of the same scale, if a scoped attachment rule is separately approved.

**`LIK` above is a metavariable/candidate, not an adopted root**. In particular, the compact candidate `lik` is **still undecided**. These are semantic sketches, **not parseable canonical utterances** or a license to put a fraction in front of any arbitrary property. Quantitative attachments have not yet been ratified as a specific syntax.

A bare gradable predicate does not automatically entail a fixed percentage threshold (such as >50%) merely because its idiomatic translation says 'probable'. Context may govern a relative benchmark, without creating a second lexical sense. Nor does a modeled probability equal perceived certainty, logical possibility or observed frequency by definition.

## Evaluation and evidence

- Existing degree words apply to gradable qualities but do not encode exact numerical cutoffs.
- Existing cardinal/ordinal fraction notation covers 5/100 without new percent morphemes.
- `suf` expresses reaching a contextual threshold, not a particular point on a fixed scale.
- Stress tests: a small but nonzero degree; context-dependent thresholds; qualitative and numerical descriptions of the **same** property; numbers outside a property's permissible range; a comparison between two properties that are on distinct incomparable scales; event probability vs independent confidence in the estimate.
- The parser already handles bounded qualitative gradations and independent fraction parsing where ratified. No new root, property-value attachment syntax or propositional probability parser behavior is approved by this record. Existing tests must remain green.

## Consequences and compatibility

This is a **semantic typing/design principle**: properties may be gradable and may admit a numerical measurement **where appropriate**. It does not decree that every gradable quality has a natural unit; nor does it convert degree modifiers into numerals. It preserves qualitative intensities, threshold sufficiency and relative comparison as distinct operations on the **same property**. The still-pending lexical choice and exact scope/syntax of quantified probability are independent later decisions. Distinctions between genuinely different scales (objective risk, agent belief, confidence, observed frequency, logical possibility) are not erased.

## Decision authority

On 2026-11-13 the owner said 'non c'e' diversita di significato, e' solo un problema di traduzione per come la vedo io' in response to a proposed distinction between 'it is probable' and 'it has a probability', followed by 'esatto ratificato' in response to the explicit general principle: 'Ogni proprietà graduale di Unisermo può essere qualificata sia mediante modificatori qualitativi sia, quando la proprietà lo consente, mediante una misura quantitativa.' The same response left the specific lexical root `lik` to be decided. This record ratifies the **unified semantics**, not the candidate spelling or quantitative syntax.

## References

- `language/comparison.md`
- `language/numerals.md`
- `language/noun_number_system.md`
- `research/grammar/probability-quantification-candidate-audit-2026-11-13.md`
