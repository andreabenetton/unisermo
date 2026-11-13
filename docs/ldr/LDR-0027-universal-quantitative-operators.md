---
id: LDR-0027
title: General quantitative comparisons, approximation and intervals
status: Accepted
date: 2026-11-13
domain: semantics-grammar
supersedes: none
---

# LDR-0027 Universal quantitative operators

## Context and problem

The owner asked for a universal algebra of numerical quantities, rather than separate expressions for probability, ages, counts, duration, distance, prices and similar measurable properties. The author approved the six-part design consisting of the prior comparatives plus two short roots for approximation and intervals.

## Alternatives

1. Separate roots for >=, <=, !=: rejected in favor of existing local `no` plus `major/minor/ekwal`.
2. New roots particular to probability or to every unit of measurement: rejected.
3. A specific numeric tolerance imposed on every 'about N': rejected because approximate bounds are contextual.
4. A dedicated opening/closing notation for open and closed interval endpoints: rejected as an initial requirement, because existing comparison operators can express boundaries.
5. One set of reusable quantitative operators: **accepted**.

## Decision or hypothesis

Where a grammatical context expects a **quantity**, existing comparisons are also licensed as quantitative relations directly preceding the compared numerical expression:

- `ekwal N` = exactly/equal to N.
- `major N` = greater than N.
- `minor N` = less than N.
- `no minor N` = not less than / at least N, inclusive lower bound.
- `no major N` = not greater than / at most N, inclusive upper bound.
- `no ekwal N` = not equal to N.

The `no` inside these constructs negates **the quantitative comparator**, not the whole surrounding proposition; this is a semantic scope rule. The existing adjective comparison `major PROPERTY dan B` remains unchanged. These are the same comparative roots with a specifically licensed numerical valency.

**Two accepted roots**:

- `sirka N` = about/approximately N. The tolerance/precision is determined by conversational context, not a fixed percentage. Approximation does not itself state the speaker's epistemic uncertainty.
- `inter A e B` = between quantitative endpoints A and B. The internal `e` connects **the two quantities** rather than two clauses. Inclusion/exclusion of endpoints is context-dependent; when it matters, independent lower/upper constraints using `major/minor/no minor/no major` can make bounds explicit.

Here `N`, `A`, `B` are existing numeric expressions, initially canonical cardinals and analytic `CARDINAL ORDINAL` fractions. This shared quantitative structure can restrict nominal counts or specify a scalar measure. In the immediately established `lik` frame, it replaces the plain exact fraction in the same numerical slot. Examples:

- `sirka setdek` = approximately 70.
- `major setdek` = greater than 70.
- `no minor setdek` = at least 70.
- `inter sesdek e setdek` = between 60 and 70.
- `lik sirka setdek senim uman mova` = roughly 70% likelihood of P.
- `lik no minor setdek senim uman mova` = probability of P at least 70%.
- `lik inter sesdek senim e setdek senim uman mova` = probability of P between 60% and 70%.
- `sirka setdek uman movan` = approximately seventy people move (count modifier).
- `inter sesdek e setdek uman movan` = between sixty and seventy people move (count modifier).

`lik setdek uman movan` remains the independent older interpretation 'it is likely that seventy people move', with `setdek` a nominal count, not a numeric probability. This disambiguation depends on explicit quantitative operators or a two-token fraction. The construction does not impose an upper bound of 100%, even for likelihood: people's hyperbolic statements remain grammatically valid, as ratified in LDR-0026.

The quantitative expression can be read independently via a typed grammar; the parser must preserve the original operator and numeric values without assuming a mathematical or pragmatic validation result.

## Evaluation and evidence

Tests must distinguish the interval's internal `e` from a subsequent proposition connector `e`; confirm open/inclusive comparisons and the `no` scope; ensure exact fraction representation is preserved without normalization or upper bound; and maintain older comparison, nominal quantification and `lik` behavior. Existing adjective comparisons and local negation must not be reinterpreted as numeric when their operands are qualitative.

Numerical operators may be applied to cardinal counts and preexisting fractions. They do not automatically license arbitrary decimal notation, unit symbols, signed numeric tokens, combined nested ranges, or dimensional arithmetic. The formal parser provides an independently callable `parse_quantitative_expression`, plus restricted attachment to numeric `lik` and basic nominal counts. More general measure units require separate lexical and syntactic decisions.

## Consequences and compatibility

One reusable quantitative system serves all numerical domains: new roots `sirka` and `inter` plus existing `major/minor/ekwal`, `no` and `e`. No new number morphology or measurement units. No conflation between approximation of a value and uncertainty that the value is true. Propositions retain ordinary Boolean `e` once a well-formed interval has consumed its internal connector. The parser intentionally does not judge mathematical feasibility (e.g. '200% likely').

## Decision authority

Author, 2026-11-13: 'perfetto ratificato', responding to explicit proposals A–F: extend `major/minor/ekwal` to numeric relations; compose `no minor/no major`; add `sirka` for approximation; add `inter` for intervals; express precise inclusivity/exclusivity via existing comparators; apply one general pattern across quantitative domains. This ratifies the above framework, not a new unrelated root or universal parser for all possible measurement units.

## References

- `language/comparison.md`
- `language/numerals.md`
- `language/noun_number_system.md`
- `docs/ldr/LDR-0025-unified-gradable-properties.md`
- `docs/ldr/LDR-0026-numerical-likelihood-hyperbole.md`
