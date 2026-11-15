# Proposed SI prefix morphology for Unisermo (2026-11-13)

**Status: research proposal only — SI prefix spellings and productive parser behavior are NOT yet ratified.**

## Canonical baseline checked

- Cardinal 1000 is **`mila`**, the sole canonical numeral power 10^3; legacy `mil` is retired (`language/numerals.md`).
- Cardinal 10^6 `mega` and 10^9 `giga` are already canonical as numeral powers.
- Ratified measurement unit roots are `gram` (mass) and `sekun` (duration) (`docs/ldr/LDR-0028-basic-measures-ellipsis.md`).
- General measurement expression uses QUANTITY UNIT; homogeneous intervals can elide the unit at their first endpoint.
- The official alphabet excludes c, h and x. Every candidate below uses only canonical Unisermo letters.
- Prefix morphology is approved **in principle** by the owner (LDR-0028), but no individual prefix surface or parser procedure was ratified at that time.

## Proposed core metric-prefix shortlist (new approval needed)

| Candidate | Power | Example gram | Example sekun | Status |
| --- | ---: | --- | --- | --- |
| `giga-` | +9 | `gigagram` | `gigasekun` | proposed unit-prefix use; `giga` already confirmed numeral |
| `mega-` | +6 | `megagram` | `megasekun` | proposed unit-prefix use; `mega` already confirmed numeral |
| `kilo-` | +3 | `kilogram` | `kilosekun` | proposed root |
| none | 0 | `gram` | `sekun` | existing confirmed units |
| `senti-` | -2 | `sentigram` | `sentisekun` | proposed root |
| `mili-` | -3 | `miligram` | `milisekun` | proposed root |
| `mikro-` | -6 | `mikrogram` | `mikrosekun` | proposed root |
| `nano-` | -9 | `nanogram` | `nanosekun` | proposed root |

The complete standard SI list, beyond the core shortlist (including deca, hecto, deci, pico, femto, atto, zepto, yocto, ronto, quecto, tera, peta, exa, zetta, yotta, ronna, quetta), is NOT rejected but requires orthographic/phonotactic/collision review. Conventional SI symbols and ISO currency codes are external notation, not automatically roots.

## Proposed rules and outstanding choices

1. **Distinct categories**: `mila` retains cardinal 1000; `kilo-` has the SI unit-prefix factor 1000. No redefinition of `mila`.
2. **Fused word**: one prefix directly precedes a confirmed unit root; `kilogram` is written without spaces or hyphen. Prefix alone is not a measurement noun.
3. **One prefix per unit**: no stacked `kilomiligram` until explicitly reviewed.
4. **Typed AST**: root_unit, dimension, prefix spelling, decimal exponent, scale factor, original surface and quantity are independent fields; do not rewrite `mila gram` into `uno kilogram` during parsing.
5. **Equivalence without obligatory normalization**: `mila gram` and `uno kilogram` share underlying mass magnitude, but preserve distinct original expressions and their rhetorical/precision context.
6. **Interval unit ellipsis**: `inter dek e bisdek kilogram` uses `kilogram` at both endpoints; do not implicitly infer `gram` for the first endpoint. Explicit mismatched prefixes/units need an independently defined conversion scope and should not silently compare or normalize.
7. **Dimensions matter**: `gram` measures mass, `sekun` time; metric prefixes do not change the physical dimension.
8. **No property bounds**: do not reject physically unlikely or hyperbolic values as syntax errors.
9. **SI coherence**: `kilogram` is the SI base unit of mass although `gram` supplies the ordinary lexical root and prefixed morphology. Under eventual canonicalization, `kilogram` = 1000 `gram` exactly; special consideration required for SI rules about prefixing `kilogram` (e.g. use `miligram` rather than stacking prefixes).
10. **Source-language collision audit**: candidate `mili-` vs canonical `mila` (different semantic types and suffix sounds) deserves oral comprehension testing. `senti-` should not be mistaken for the numeral `sen`.

## Example comparisons (schematic pending approval)

- `mila gram` = 1000 grams.
- `uno kilogram` = 1 kilogram (=1000 g).
- `bis kilogram` = 2 kilograms.
- `uno miligram` = 1 milligram (1/1000 g).
- `inter dek e bisdek kilogram` = between 10 and 20 kilograms (elliptic first unit).
- `sirka kin milisekun` = about five milliseconds.

## Specific owner ratification still required

- Confirm `kilo, mili, senti, mikro, nano` as productive prefixes and whether `mega/giga` may simultaneously be numerals and SI prefixes.
- Decide if the system should recognize the **complete** ISO/CGPM SI prefix set (24 prefix levels, including extreme large/small), rather than initially the small core.
- Define if mixed compatible units in explicit intervals may be supported once conversion is ratified; no conversion is silently enabled by this proposal.

No canonical lexicon, generated index, grammar or executable parser changed in this research branch.
