# Numerals

A formal specification of the cardinal numerals of the synthetic language. This document defines the digits 0–9, the powers of ten (`dek`, `sen`, `mila`, `mega`, `giga`), the rule by which compound numerals are formed, and the interaction of numerals with the noun phrase.

## Related documents

- The noun number system — including the rule that nouns normally remain bare after a numeral — is defined in [`noun_number_system.md`](noun_number_system.md).
- The case suffixes attach to the noun at the right edge of the noun phrase, as defined in [`noun_case_system.md`](noun_case_system.md).
- The phonotactic restriction that motivates `ter` instead of `*tri` (no initial CC clusters in the core vocabulary) is in [`vocabulary_design_rules.md`](vocabulary_design_rules.md) §3 Rule 2.

---

## 1. Design Goals

The numerals follow the same four priorities as the rest of the language:

1. **Compactness.** Ten digit names and `dek/sen` are three letters; the higher powers `mila/mega/giga` are four. International recognizability and stable morphemes take precedence over the shortest possible spelling. Oral information rate remains an empirical question.
2. **Recognizability.** Each form is adapted from internationally recognizable sources (Latin, Romance, Germanic), so a speaker of any major European language can guess most digits on first hearing.
3. **Regularity.** Compound numerals are built by simple concatenation — there are no irregular teens, no decade-specific stems, no special multiplicative forms.
4. **Auditory clarity and phonotactic safety.** All forms respect the safety rules of [`vocabulary_design_rules.md`](vocabulary_design_rules.md): no initial consonant clusters, no ambiguous `ng`, no reliance on fragile minimal pairs.

---

## 2. Base Forms

The **fifteen base forms** are ten decimal digits plus five decimal power words:

| Value | Form | Origin / rationale |
|---:|---|---|
| 0 | `nul` | null / nul |
| 1 | `uno` | uno / one |
| 2 | `bis` | bis; replaces rejected `duo` |
| 3 | `ter` | three / tre, adapted without initial cluster |
| 4 | `for` | four |
| 5 | `kin` | quinque, adapted |
| 6 | `ses` | seis / six |
| 7 | `set` | sette / sept |
| 8 | `oto` | otto / ocho |
| 9 | `nin` | nine / neun |
| 10 | `dek` | deca |
| 100 | `sen` | cent |
| 1,000 | `mila` | mille / mila; replaces historical `mil` |
| 1,000,000 | `mega` | international mega- |
| 1,000,000,000 | `giga` | international giga- |

The author **ratified `mila`, `mega`, `giga` on 24 October 2026**. `mil` is thereby **retired as a current spelling**, not retained as a variant. Older sources and frozen benchmark corpora retain their historical spelling. Unlike the twelve smaller forms, the three higher powers have four letters. Neither the three-letter forms nor the entire inventory are uniformly CVC (`uno`/`oto` are VCV). The language remains base-10, not base-15.

---

## 3. Composition Rules

Compound numerals are formed by concatenating the base forms in **big-endian order** (largest power first), with each "digit" preceding the power word it multiplies. There is no overt linker between components, and a compound numeral is written as **one orthographic word**, without spaces or hyphens. Thus `dekbis` = 12 and `bisdek` = 20.

### 3.1 Teens (11–19): `dek + digit`

| Value | Form |
|---|---|
| 11 | `dekuno` |
| 12 | `dekbis` |
| 13 | `dekter` |
| 19 | `deknin` |

### 3.2 Decades (20–90): `digit + dek`

| Value | Form |
|---|---|
| 20 | `bisdek` |
| 30 | `terdek` |
| 40 | `fordek` |
| 90 | `nindek` |

### 3.3 Decades + units (21–99): `digit + dek + digit`

| Value | Form |
|---|---|
| 21 | `bisdekuno` |
| 25 | `bisdekkin` |
| 99 | `nindeknin` |

### 3.4 Hundreds: `digit + sen`

The form for `100` is the bare word `sen` — `uno` is **not** prefixed.

| Value | Form |
|---|---|
| 100 | `sen` |
| 200 | `bissen` |
| 300 | `tersen` |
| 900 | `ninsen` |

### 3.5 Hundreds + decades + units

Components combine in big-endian order:

| Value | Form |
|---|---|
| 321 | `tersenbisdekuno` |
| 405 | `forsenkin` |
| 999 | `ninsennindeknin` |

### 3.6 Powers in groups of three decimal digits

Split a decimal integer into up to four groups: **billions, millions, thousands, units**. Each nonzero group coefficient (1..999) uses the **existing** digits + `sen` + `dek` spelling. Append `giga`, `mega` or `mila` to the higher groups; the final units group has no power word. Concatenate the groups in descending order as **one orthographic word**.

When a coefficient is exactly one, omit `uno` before its power. Omit every zero group entirely. Thus `megauno` = 1,000,001 and `megamila` = 1,001,000; neither `unomega` nor `meganulmila` is canonical.

| Decimal value | Canonical form | Analysis |
| ---: | --- | --- |
| 1,000 | `mila` | one thousand |
| 10,000 | `dekmila` | ten thousand |
| 100,000 | `senmila` | hundred thousand |
| 1,000,000 | `mega` | one million |
| 10,000,000 | `dekmega` | ten million |
| 100,000,000 | `senmega` | hundred million |
| 1,000,000,000 | `giga` | one billion (10^9, short scale) |
| 10,000,000,000 | `dekgiga` | ten billion |
| 100,000,000,000 | `sengiga` | hundred billion |
| 2,026 | `bismilabisdekses` | two thousand + twenty-six |
| 9,999 | `ninmilaninsennindeknin` | nine thousand + nine hundred ninety-nine |
| 20,345,006 | `bisdekmegatersenfordekkinmilases` | 20 million + 345 thousand + six |
| 999,999,999,999 | `ninsennindekningiganinsennindekninmeganinsennindekninmilaninsennindeknin` | 999 × each of giga, mega, mila, and 999 |

### 3.7 Domain, canonicality and exceptional forms

The formal cardinal range is **0 through 999,999,999,999**. Every value has exactly one canonical fused spelling. `nul` alone denotes zero; no silent zero place becomes an overt `nul` component. The power words `giga`, `mega`, `mila`, `sen`, `dek` must appear in descending order, with no duplicates or redundant `uno` multiplier. `mil` is no longer a legal contemporary cardinal component.

The parser is **compositional**, indexing only 999 possible three-digit group coefficients. It does not enumerate a trillion integers. The signed integers, fractions, decimals, ordinals, measures and powers larger than `giga` need separate explicit approval; they are not inferred from this rule.

The numeral still precedes an uninflected number-neutral noun; nominal case is marked on the noun, not on the numeral. The accepted `NUMjer` general iteration counter automatically inherits the larger **positive** numerical domain; the separate kinship parser retains its own smaller safe bound on path expansion.

---

## 4. Iteration and step counter `jer`

`jer` is the canonical grammatical counter for an **occurrence, iteration, or step in a repeatable relation or process**. It is not restricted to genealogy.

A cardinal numeral combines directly before `jer`, and the result is written as one word:

```
bisjer = two times; two iterations; two steps
terjer = three times; three iterations; three steps
forjer = four times; four iterations; four steps
```

`NUMjer` may itself be the first component of a larger transparent compound. When it modifies an iterable relation, it specifies how many applications or relational steps are traversed. The whole lexicalized compound is written as one word, just like compound numerals. For example, in a genealogical system a form of the structural type `bisjerROOT` means ROOT reached after two applications/steps; a larger compound such as `adelbisjerROOT` remains fused when it denotes one kinship term. The precise lexical roots used for individual kinship relations are defined separately from the general meaning of `jer`.

In the now-confirmed [kinship system](kinship.md), applying `gen` (parent) twice gives **`bisjergen` = grandparent (gender-neutral)**; applying it three times gives **`terjergen` = great-grandparent (gender-neutral)**. These examples follow the original August genealogical design. **Typed-relation scope (24 October 2026):** `NUMjer+R` repeats the complete relational link `R`. Thus `bisjergene` repeats **mother-of** twice and denotes **mother's mother** (not every grandmother), while `bisjergeno` repeats **father-of** twice and denotes **father's father** (not every grandfather). To describe all four precise branches unambiguously, use the two-link compounds `genegene` (maternal grandmother), `genegeno` (paternal grandmother), `genogene` (maternal grandfather), `genogeno` (paternal grandfather). These are read **rightmost link first**, in accordance with [`kinship.md`](kinship.md). `bisjergen` remains the generic grandparent.

`jer` therefore means neither “ordinal” nor “genealogical degree” by itself. `bisjer` is the general expression “two times / two steps”; genealogy is one application of that general iteration mechanism.

---

## 5. Use with Nouns

The numeral **precedes the noun**. Because the numeral already conveys plurality, the noun normally remains in its bare (number-neutral) form (see [`noun_number_system.md`](noun_number_system.md) §7):

```
bis dom        — two houses
```

The old plural suffix `-en` is obsolete. After a numeral the noun remains bare because quantity is already explicit; `wi` is normally omitted as redundant:

```
bis dom        - two houses
```

When the noun phrase takes case, the case suffix attaches to the noun, which sits at the right edge of the phrase (see [`noun_case_system.md`](noun_case_system.md) §4):

```
bis dom        — two houses
bis domem      — two houses (as direct object)
vidi bis domem — I see two houses
```

Numerals themselves do not inflect for case or number.

---

## 6. Notes

- `uno` is the free numeral **one** but is omitted immediately before `dek`, `sen`, `mila`, `mega` and `giga` when the multiplier would be one.
- `ter` rather than `tri` reflects the no-initial-CC core-root policy.
- `kin` is canonical /kin/.
- Twelve base forms (ten digits, `dek`, `sen`) are three letters, but not all CVC. The three ratified higher powers `mila`, `mega`, `giga` are four.
- Original `mil` forms and old experimental benchmarks are history only and should not be silently rewritten.

---

## 7. Summary

```
0..9    nul uno bis ter for kin ses set oto nin
10      dek
100     sen
1000    mila
1000000 mega
1000000000 giga
```

Write positive integers as descending three-digit groups with `giga`, `mega`, `mila`, then a bare 0..999 units group. Omit all zero groups and the coefficient `uno` before each power. After a numeral the noun remains bare; case suffixes attach to the noun, never to a numeral. The whole numerical word is fused.
