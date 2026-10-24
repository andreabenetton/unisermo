# Numerals

A formal specification of the cardinal numerals of the synthetic language. This document defines the digits 0–9, the powers of ten (`dek`, `sen`, `mil`), the rule by which compound numerals are formed, and the interaction of numerals with the noun phrase.

## Related documents

- The noun number system — including the rule that nouns normally remain bare after a numeral — is defined in [`noun_number_system.md`](noun_number_system.md).
- The case suffixes attach to the noun at the right edge of the noun phrase, as defined in [`noun_case_system.md`](noun_case_system.md).
- The phonotactic restriction that motivates `ter` instead of `*tri` (no initial CC clusters in the core vocabulary) is in [`vocabulary_design_rules.md`](vocabulary_design_rules.md) §3 Rule 2.

---

## 1. Design Goals

The numerals follow the same four priorities as the rest of the language:

1. **Compactness.** Every base numeral is exactly three letters (CVC), giving a uniform rhythm and a minimum-length encoding for the digits.
2. **Recognizability.** Each form is adapted from internationally recognizable sources (Latin, Romance, Germanic), so a speaker of any major European language can guess most digits on first hearing.
3. **Regularity.** Compound numerals are built by simple concatenation — there are no irregular teens, no decade-specific stems, no special multiplicative forms.
4. **Auditory clarity and phonotactic safety.** All forms respect the safety rules of [`vocabulary_design_rules.md`](vocabulary_design_rules.md): no initial consonant clusters, no ambiguous `ng`, no reliance on fragile minimal pairs.

---

## 2. Base Forms

The thirteen base numerals are:

| Value | Form | Source / logic |
|---|---|---|
| 0 | `nul` | null / nul |
| 1 | `uno` | uno / un / one |
| 2 | `bis` | bis / due |
| 3 | `ter` | three / tre / tri, but with no initial `tr` cluster |
| 4 | `for` | four / for |
| 5 | `kin` | quinque / kinque / kinq, adapted as `kin` |
| 6 | `ses` | seis / six |
| 7 | `set` | sette / sept / siete |
| 8 | `oto` | otto / ocho / octo simplified |
| 9 | `nin` | nine / neun-like |
| 10 | `dek` | deca / decimal |
| 100 | `sen` | cent / cento |
| 1000 | `mil` | mille / mil |

All forms are three letters of CVC shape. Each respects the alphabet defined in [`alphabet_and_phonology.md`](alphabet_and_phonology.md) and the syllable rules of [`vocabulary_design_rules.md`](vocabulary_design_rules.md).

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

### 3.6 Thousands: `digit + mil`

The form for `1000` is the bare word `mil` — `uno` is **not** prefixed.

| Value | Form |
|---|---|
| 1000 | `mil` |
| 2000 | `bismil` |
| 9000 | `ninmil` |

Larger compounds continue the same big-endian, linker-free pattern and remain one orthographic word: `mil + (hundreds) + (decades) + (units)`.

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

In the now-confirmed [kinship system](kinship.md), applying `gen` (parent) twice gives **`bisjergen` = grandparent (gender-neutral)**; applying it three times gives **`terjergen` = great-grandparent (gender-neutral)**. These examples follow the original August genealogical design. The distinction between an individual's gender and the sex of each **intermediate** parent link is not specified by the general `jer` construction; forms such as `bisjergeno` therefore remain unratified pending a scope rule.

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

- The form for `1` is `uno`. It is **not** prefixed to `sen` or `mil` (so `100 = sen`, not `*uno sen`; `1000 = mil`, not `*uno mil`).
- The form for `3` is `ter`, not `*tri`, because initial CC clusters are disallowed in the core vocabulary (see [`vocabulary_design_rules.md`](vocabulary_design_rules.md) §3 Rule 2).
- The form `kin` is canonical /kin/.
- All base numerals are three letters; this is intentional and gives the digit set a uniform CVC rhythm.

---

## 7. Summary

```
nul  = 0
uno  = 1
bis  = 2
ter  = 3
for  = 4
kin  = 5
ses  = 6
set  = 7
oto  = 8
nin  = 9
dek  = 10
sen  = 100
mil  = 1000
```

Composition: big-endian concatenation into one orthographic word, with each digit preceding the power word it multiplies. `uno` is omitted before `sen` and `mil`. After a numeral, the noun stays bare; obsolete nominal `-en` is not used.
