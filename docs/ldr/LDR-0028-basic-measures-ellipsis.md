---
id: LDR-0028
title: Basic measures with shared-unit interval ellipsis and gram/sekun
status: Accepted
date: 2026-11-13
domain: semantics-grammar
supersedes: none
---

# LDR-0028 Basic measurement syntax and interval unit ellipsis

## Context and problem

The author ratified the design principles A–H for measured quantities after adopting universal quantitative operators in LDR-0027: quantity + unit; invariant unit; existing numeric operators; productive SI prefix design; distinction between dimension and unit; future general dimensional operators for compound units; lexical review per unit; and typed external identifiers where necessary (e.g., currency codes). The author explicitly modified the proposal to **allow omission of the common measurement unit at the first endpoint of an interval**. The author also explicitly selected the canonical roots **gram** and **sekun** (not the earlier candidates garam/sekund).

## Alternatives

1. Require repeating units on both endpoints: rejected as unnecessarily verbose when they share the same unit.
2. Silently treat interval endpoints lacking a unit as dimensionless: rejected because the trailing unit explicitly determines the dimension of the entire interval.
3. Allow any juxtaposed root as a unit: rejected until independently lexicalized and confirmed.
4. Create ad-hoc probability/time/mass interval operators: rejected because LDR-0027 already specifies universal quantitative syntax.

## Decision or hypothesis

The canonical simple measurement pattern is:

```text
QUANTITY UNIT
```

The numeric `QUANTITY` may be an existing cardinal, a two-token rational fraction, or a universal quantitative modifier (e.g., `sirka`, `major`, `minor`, `no minor`, `no major`, `ekwal`). An invariant unit follows the completed numeric phrase. Neither numeral nor unit acquires agreement endings merely because the measured count changes.

**Intervals have two accepted surface variants**:

```text
inter Q1 UNIT e Q2 UNIT   # full
inter Q1 e Q2 UNIT        # elliptical: UNIT inherited by first endpoint
```

Both explicitly refer to the **same unit**. The second endpoint MUST carry its unit for the ellipsis rule to apply, with the first endpoint optionally repeating it. The parser preserves source spelling and records whether the first unit was omitted; it resolves the same canonical unit and physical dimension for both endpoints. If explicit units differ, parsing does **not** silently convert between them. The interval's internal `e` belongs to the measured range, not to clause coordination.

**Lexical ratifications**:
- `gram`: unit of mass, gram, internationally recognizable, canonical Unisermo spelling.
- `sekun`: unit of time duration, second, distinguished from the ordinal `bisim` ('second' as an order number).

Examples:
- `kin gram` = five grams.
- `sirka setdek gram` = about seventy grams.
- `no minor dek sekun` = at least ten seconds.
- `inter dek gram e bisdek gram` = between ten and twenty grams.
- `inter dek e bisdek gram` = same meaning with the first `gram` elided.
- `inter kin e dek sekun` = between five and ten seconds.
- `inter kin sekun e dek gram` = **not** licensed as a homogeneous measurement interval.

As with LDR-0026, the grammar does not reject a measurement solely because its numeric value would be implausible, hyperbolic, or physically impossible. It preserves the original rational number or cardinal value.

## Evaluation and evidence

A bounded, independently callable `parse_measurement_expression` recognizes simple measured values, existing quantitative relations and both homogeneous interval forms; it returns a typed measure/interval AST and an explicit `unit_ellipsis` flag. Test equivalence of the resolved unit for elliptical/full forms, preserve original surface, verify `gram` and `sekun` are distinct physical dimensions, and fail closed on missing trailing units, cross-unit intervals and unratified syntax. `parse_quantitative_expression` remains a dimensionless numerical-expression parser, avoiding accidental reinterpretation of preexisting quantitative expressions.

## Consequences and compatibility

The general design principles A–H are accepted at the architectural level; only the two named unit roots and basic measurement syntax are executable here. Other candidate roots (`metr`, `litr`, `kelvin`, etc.) have **not** been ratified in this turn. Productive SI prefixes, compound units, temperature-scale semantics, full dimension arithmetic and the previously proposed `mon CODE` monetary namespace remain for later lexical/syntactic ratifications. The ellipsis rule is **not** a general permission to omit the unit from arbitrary phrases or conjoin differently typed measures. Standard abbreviations and currency codes are not automatically lexical roots.

## Decision authority

The author wrote on 2026-11-13: 'principi approvati. 1 introduci elissi 2 gram sekun', responding directly to the proposed A–H measurement design, choosing shared-unit interval ellipsis and the exact root spellings `gram` and `sekun`.

## References

- `docs/ldr/LDR-0027-universal-quantitative-operators.md`
- `language/comparison.md`
- `language/numerals.md`
- `docs/ldr/LDR-0018-exchange-kambi-semantics.md`
