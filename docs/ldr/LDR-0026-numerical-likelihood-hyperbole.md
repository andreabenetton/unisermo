---
id: LDR-0026
title: Numerical likelihood using existing fractions without semantic range filtering
status: Accepted
date: 2026-11-13
domain: semantics-grammar
supersedes: none
---

# LDR-0026 — Numerical likelihood fractions, with rhetorical hyperbole

## Context and problem

After ratifying `lik` as one gradable propositional probability property, the author approved the specific numeric attachment syntax `lik FRACTION FINITE_PROPOSITION`. In doing so, the author explicitly rejected imposing the mathematical bound 0%–100% **as a grammatical/parser constraint**: people use hyperbole and other nonliteral numerical claims, and a language parser must preserve what was said instead of treating a rhetorical claim as syntactically illegal.

## Alternatives

1. Reject a parsed fraction if numerator exceeds denominator. Rejected: confuses grammar with mathematical modeling and excludes rhetorical hyperbole such as 200% certain.
2. Add a dedicated percentage suffix or a nominal 'probability' root. Rejected: existing `CARDINAL ORDINAL` fractions and `lik` already express the structure.
3. Parse existing fractions exactly, without semantic range filtering. **Accepted.**
4. Mix numeric fractions and qualitative modifiers in a single construction. Deferred: degree attachment scope and cross-qualification need explicit independent rules.

## Decision or hypothesis

The ratified quantitative likelihood frame is:

```text
[no] lik CARDINAL ORDINAL FINITE_PROPOSITION
```

The cardinal plus ordinal denominator is precisely the existing two-token fraction grammar (denominator ≥2). It follows `lik` and precedes the full finite propositional operand. The proposition retains its own subject, verbal person and TAM. A positive numeric construction asserts that the specified degree applies to P; a free `no` directly before `lik` denies that numeric claim, not P itself. An embedded `no` continues to negate P. Unmarked `lik P` and existing `pok lik P`, `mult lik P` remain valid qualitative constructions of the **same** single property.

Examples:

- `lik kin senim uman mova` = likelihood of someone's movement is five hundredths (5%).
- `lik setdek senim uman mova` = likelihood of someone's movement is 70%.
- `lik uno bisim uman mova` = likelihood is one half.
- `lik ter forim uman mova` = likelihood is three quarters.
- `lik bissen senim uman mova` = '200% likelihood' is **grammatically legal** even when mathematically outside the ordinary probability range; do not delete, clamp or normalize the assertion.
- `no lik setdek senim uman mova` = denial that the degree for P is 70%, not an assertion that P has probability 30%.
- `lik setdek senim uman no mova` = 70% assigned to the negation of the embedded event.
- `lik setdek senim uman mova lim e vida` = likelihood assertion about movement, **and** assertion of seeing; ordinary closing `lim` ends the left operand before a connective.
- `lik setdek senim uman mova e vida` = the numeric degree qualifies the full following conjunction by the already accepted propositional-scope convention.

The fraction's exact numerator/denominator and original spelling remain in the AST. **Syntactic validity is independent of mathematical feasibility, contextual sincerity, rhetorical emphasis or the numerical probability axioms.** The reference parser has **no >100% prohibition**. Existing rules of the fraction grammar remain (no negative numerals or denominator 0/1), and this decision does not silently extend the underlying numeral inventory.

The still-open **general** concepts of approximations, intervals, ranges and inequalities (e.g. 'approximately 70%', 'between 60% and 70%', 'at least 70%') must be treated across numerical expressions and measurable properties, not introduced as probability-specific ad hoc syntax.

## Evaluation and evidence

The parser must preserve exact regular fractions, including improper fractions, and their original representation. It must not infer truth of P, invent an automatic 1-P complement from negation of the numeric degree, enforce a <=1 bound, or accept nonexistent fraction morphology. Regression cases include 0%, 5%, 50%, 70%, 100%, 200%, and 5/3, with both negative scopes, Boolean coordination and explicit `lim` boundaries. It must continue to reject mixed qualitative-plus-numeric likelihood until those structures are ratified. The AST represents the numerical claim, not a probability-model verdict.

## Consequences and compatibility

No new root, fraction syntax, numeral suffix or arbitrary numerical scale is created. This adds only a scoped combination of two previously canonical structures, `lik P` and `CARDINAL ORDINAL`. An independent later design record should define approximations/intervals/inequalities as general linguistic operations, potentially reusable with `lik` and other measurable qualities. A numerical claim can be mathematically infeasible and still valid spoken/written Unisermo.

## Decision authority

On 2026-11-13 the owner responded to the specific `lik FRAZIONE PROPOSIZIONE-FINITA` proposal: 'nel parser non introdurre questa limitazione: "il dominio quantitativo è limitato all'intervallo da 0% a 100%" anche se formalmente valida per un computer o un aia, gli umani ricorrono ad iperboli. sintassi ratificata. stime e intervalli sono concetti generali che dovremo affrontare'. This explicitly accepts the numeric likelihood syntax, prohibits semantic range filtering in its parser, and leaves approximations and intervals to a general subsequent design.

## References

- `language/comparison.md`
- `language/numerals.md`
- `language/word_order.md`
- `docs/ldr/LDR-0025-unified-gradable-properties.md`
- `formalization/parser/proposition.py`
