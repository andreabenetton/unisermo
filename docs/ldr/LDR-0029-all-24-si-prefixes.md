---
id: LDR-0029
title: All 24 SI decimal prefixes with milli double-l and typed unit attachment
status: Accepted
date: 2026-11-13
domain: semantics-grammar
supersedes: none
---

# LDR-0029 — Complete SI prefixes

## Context and problem

The project already ratified the decimal cardinal `mila` = 1000 and typed measurement units `gram` and `sekun`. The author requested **all official SI prefixes**, and explicitly chose **`milli-` over `mili-`**. The approved general measurement principles in LDR-0028 include productive metric prefix morphology.

The official source is the BIPM International System of Units, 9th edition, version 3.02, Table 7, identifying 24 prefixes from 10^30 to 10^-30 including the four introduced in 2022.

## Alternatives

1. Reuse the cardinal `mila` as the 10^3 unit prefix: rejected, because a numeric power and an attached unit multiplier have distinct roles and international `kilo-` is already recognizable.
2. Simplify `milli` to `mili`: rejected by the author; preserve international double-l spelling. The accepted Unisermo gemination rule permits consecutive identical consonants and tolerant realization.
3. Only support the most common eight SI prefixes: rejected by owner request to canonize the complete set.
4. Translate external SI symbols directly as standalone words: rejected; symbols are standards-based typed notation, not automatically Unisermo roots.
5. Permit stacked prefixes: rejected as contrary to the SI rule forbidding compound prefixes.

## Decision

The complete **24-form** invariant Unisermo prefix inventory is:

| Official name | SI symbol | Exponent | Canonical Unisermo prefix |
| --- | --- | ---: | --- |
| quetta | Q | +30 | `kwetta-` |
| ronna | R | +27 | `ronna-` |
| yotta | Y | +24 | `jotta-` |
| zetta | Z | +21 | `zetta-` |
| exa | E | +18 | `eksa-` |
| peta | P | +15 | `peta-` |
| tera | T | +12 | `tera-` |
| giga | G | +9 | `giga-` |
| mega | M | +6 | `mega-` |
| kilo | k | +3 | `kilo-` |
| hecto | h | +2 | `ekto-` |
| deca | da | +1 | `deka-` |
| deci | d | -1 | `desi-` |
| centi | c | -2 | `senti-` |
| milli | m | -3 | `milli-` |
| micro | µ | -6 | `mikro-` |
| nano | n | -9 | `nano-` |
| pico | p | -12 | `piko-` |
| femto | f | -15 | `femto-` |
| atto | a | -18 | `atto-` |
| zepto | z | -21 | `zepto-` |
| yocto | y | -24 | `jokto-` |
| ronto | r | -27 | `ronto-` |
| quecto | q | -30 | `kwekto-` |

Each canonical form uses only the official alphabet; `kw` adapts source `qu`, `j` source initial y, `k` source c before a/o, `s` soft c, and `eks` source ex. The double letters of `milli`, `atto`, `ronna`, `kwetta`, `jotta`, `zetta` are preserved; the written contrast never depends on forcing unfamiliar speakers to produce length perfectly.

**Grammar**: `PREF UNIT` is one fused orthographic word, exactly **one** confirmed SI prefix followed by **one** independently ratified base unit root. The prefix cannot stand alone as a measurement. No stacked prefixes or invented compound units. Productive `mega/giga` remain also cardinal power roots under their existing independent numerical roles. `mila` stays the unique numeral '1000', not a unit prefix. SI symbols are kept unchanged in external notation, with capitalization significant.

**Examples**:
- `mila gram` and `uno kilogram` are equal in physical magnitude (1000 gram).
- `bis kilogram` = 2000 gram.
- `uno milligram` = 0.001 gram.
- `kin mikrogram` = 5 microgram.
- `sirka kin millisekun` = approximately 5 milliseconds.
- `inter dek e bisdek kilogram` = between 10 and 20 kilograms, with shared-unit ellipsis. The first endpoint inherits the complete unit *including* its prefix.
- `inter dek kilogram e bisdek kilogram` = same interval with both units repeated.
- `kilomilligram` is **invalid** (two prefixes).
- `miligram` is **not** a canonical spelling (missing the second l).

An SI prefix modifies the unit's scale, **not** the magnitude of a preceding numeral; `mila gram` is number 1000 plus gram, whereas `uno kilogram` is number 1 plus unit kilo+gram. Numerically equivalent expressions preserve distinct surface forms and structure; they are never silently rewritten. The scale uses an **exact decimal exponent** and integral numerator/denominator rather than lossy floating-point approximations. The decimal magnitude must never be bounded to an arbitrary domain; hyperbole remains parseable.

The official SI reference also notes that prefixes may be attached to unit names as one word, and composite prefixes cannot be created by concatenating two prefixes. This applies to `gram` and `sekun` as the only currently confirmed unit roots. `kilogram` is the standard SI base unit of mass, even though the linguistic composition of the Unisermo word is kilo+gram: this fact does not license prefixing `kilogram` with yet another prefix.

## Evaluation and evidence

- Unit-prefixed parser must recognize each of the 24 values, positive and negative.
- AST: `prefix`, `root`, `dimension`, `decimal_exponent`, exact rational `scale_numerator/scale_denominator`, and `si_symbol`.
- `parse_measurement_expression` supports the already ratified scalar operators and both full and elliptical homogeneous intervals when the **surface unit is identical**. The parser does not silently convert differently prefixed endpoints; cross-unit conversion requires separate treatment.
- Existing cardinal and fraction parsers stay unchanged, notably `mila` = 1000.
- Negative tests include `miligram`, stacked `kilomilligram`, unknown roots, standalone `kilo` as a unit, unsupported SI symbols inside Unisermo orthography, and mixed interval units.

## Consequences and compatibility

The linguistic morphology is general for all **confirmed** unit roots and **all** 24 confirmed decimal SI prefixes. Only `gram` and `sekun` have been accepted as base units to date. Future candidates `metr`, `litr` etc. are *not* accepted by their appearance in a demonstration. Unit compounding, conversion in mixed-unit intervals, decimals and external currency identifiers remain separate decisions. Parser invariants and source indexing are covered by a new CI workflow.

## Decision authority

On 2026-11-13 the owner wrote: 'mili o milli ? forse e' meglio il secondo. canonizza tutti prefissi si.' The choice is recorded as `milli-`, and the explicit request confirms all 24 official SI prefixes with Unisermo phonological adaptations.

## References

- https://www.bipm.org/en/measurement-units/si-prefixes/
- https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf
- `docs/ldr/LDR-0028-basic-measures-ellipsis.md`
- `language/alphabet_and_phonology.md`
- `language/numerals.md`
