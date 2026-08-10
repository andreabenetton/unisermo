# Numerals

A formal specification of the cardinal numerals of the synthetic language. This document defines the digits 0–9, the powers of ten (`dek`, `sen`, `mil`), the rule by which compound numerals are formed, and the interaction of numerals with the noun phrase.

## Related documents

- The noun number system — including the rule that the plural suffix `-en` is optional after a numeral — is defined in [`noun_number_system.md`](noun_number_system.md).
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
| 2 | `duo` | duo / due |
| 3 | `ter` | three / tre / tri, but with no initial `tr` cluster |
| 4 | `for` | four / for |
| 5 | `cin` | cinque / cinq (initial `c` = /tʃ/) |
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

Compound numerals are formed by concatenating the base forms in **big-endian order** (largest power first), with each "digit" preceding the power word it multiplies. There is no overt linker between components.

### 3.1 Teens (11–19): `dek + digit`

| Value | Form |
|---|---|
| 11 | `dek uno` |
| 12 | `dek duo` |
| 13 | `dek ter` |
| 19 | `dek nin` |

### 3.2 Decades (20–90): `digit + dek`

| Value | Form |
|---|---|
| 20 | `duo dek` |
| 30 | `ter dek` |
| 40 | `for dek` |
| 90 | `nin dek` |

### 3.3 Decades + units (21–99): `digit + dek + digit`

| Value | Form |
|---|---|
| 21 | `duo dek uno` |
| 25 | `duo dek cin` |
| 99 | `nin dek nin` |

### 3.4 Hundreds: `digit + sen`

The form for `100` is the bare word `sen` — `uno` is **not** prefixed.

| Value | Form |
|---|---|
| 100 | `sen` |
| 200 | `duo sen` |
| 300 | `ter sen` |
| 900 | `nin sen` |

### 3.5 Hundreds + decades + units

Components combine in big-endian order:

| Value | Form |
|---|---|
| 321 | `ter sen duo dek uno` |
| 405 | `for sen cin` |
| 999 | `nin sen nin dek nin` |

### 3.6 Thousands: `digit + mil`

The form for `1000` is the bare word `mil` — `uno` is **not** prefixed.

| Value | Form |
|---|---|
| 1000 | `mil` |
| 2000 | `duo mil` |
| 9000 | `nin mil` |

Larger compounds continue the same big-endian, linker-free pattern: `mil + (hundreds) + (decades) + (units)`.

---

## 4. Use with Nouns

The numeral **precedes the noun**. Because the numeral already conveys plurality, the noun normally remains in its bare (number-neutral) form (see [`noun_number_system.md`](noun_number_system.md) §7):

```
duo dom        — two houses
```

The plural suffix `-en` is **optional and usually omitted** after a numeral, but may be added for emphasis or in formal registers:

```
duo dom        (compact, default)
duo domen      (explicit, emphatic)
```

When the noun phrase takes case, the case suffix attaches to the noun, which sits at the right edge of the phrase (see [`noun_case_system.md`](noun_case_system.md) §5):

```
duo dom        — two houses
duo domem      — two houses (as direct object)
vidi duo domem — I see two houses
```

Numerals themselves do not inflect for case or number.

---

## 5. Notes

- The form for `1` is `uno`. It is **not** prefixed to `sen` or `mil` (so `100 = sen`, not `*uno sen`; `1000 = mil`, not `*uno mil`).
- The form for `3` is `ter`, not `*tri`, because initial CC clusters are disallowed in the core vocabulary (see [`vocabulary_design_rules.md`](vocabulary_design_rules.md) §3 Rule 2).
- The form `cin` is pronounced /tʃin/, since `c` = /tʃ/ in the alphabet (see [`alphabet_and_phonology.md`](alphabet_and_phonology.md)).
- All base numerals are three letters; this is intentional and gives the digit set a uniform CVC rhythm.

---

## 6. Summary

```
nul  = 0
uno  = 1
duo  = 2
ter  = 3
for  = 4
cin  = 5
ses  = 6
set  = 7
oto  = 8
nin  = 9
dek  = 10
sen  = 100
mil  = 1000
```

Composition: big-endian concatenation, with each digit preceding the power word it multiplies. `uno` is omitted before `sen` and `mil`. After a numeral, the noun stays bare; `-en` is optional and usually omitted.
