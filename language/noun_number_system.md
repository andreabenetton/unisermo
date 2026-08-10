# Noun Number System

A formal specification of how grammatical number is encoded in the synthetic language. Number is carried primarily by the finite verb (through the person vowel); nouns are number-neutral by default and take an optional plural suffix `-en` when explicit plurality is needed.

## Related documents

- Person vowels and their number values are defined in [`verb_specification.md`](verb_specification.md).
- The case suffixes and the noun-phrase attachment rule are defined in [`noun_case_system.md`](noun_case_system.md).
- The pronouns derived from the person vowels are referenced in [`vocabulary_design_rules.md`](vocabulary_design_rules.md) §5.

This document introduces **one new morpheme** — the plural suffix `-en` — and the rule by which it combines with the case suffixes.

---

## 1. Design Principle

Nouns are **number-neutral by default**. The bare noun `dom` denotes "house" or "the house concept" without committing to singular or plural.

The finite verb already encodes subject number through the person vowel (see [`verb_specification.md`](verb_specification.md)):

| Verb ending | Person | Number |
|---|---|---|
| `-i` | I | singular |
| `-e` | you | singular |
| `-a` | he / she / it | singular |
| `-u` | we | plural |
| `-o` | you (pl.) | plural |
| `-ə` | they | plural |

When the subject's number is already visible from the verb, the noun itself need not be marked. This keeps short, frequent sentences compact:

| Sentence | Meaning |
|---|---|
| `amik mova` | the friend moves |
| `amik movə` | the friends move |
| `dom gran` | the house is big / the houses are big (ambiguous — zero copula, no verb to carry number) |
| `domen gran` | the houses are big (explicit plural on the noun) |

The bare noun `amik` is not pluralized to `amiken` because the verb ending `-ə` already says the subject is plural. By contrast, the predicative `dom gran` has no verb at all (zero copula, see [`copula.md`](copula.md) §8), so the number signal must come from the noun itself if it matters.

---

## 2. When Explicit Number Marking Is Needed

A noun must carry the plural marker when:

- the noun is **not the subject** (the verb does not mark object number);
- there is **no finite verb** (lists, titles, labels, dictionary headings);
- the speaker wants to **emphasize plurality** despite the verb already showing it;
- the **object's** plurality is contrastive (e.g. "I see houses" vs. "I see a house").

For these cases, the language provides a plural noun suffix.

---

## 3. The Plural Suffix `-en`

The plural noun marker is **`-en`**.

| Reason | Explanation |
|---|---|
| Pronounceable | Works after both consonants and vowels. |
| Robust | Built from `e` and `n`, both safe sounds (see [`vocabulary_design_rules.md`](vocabulary_design_rules.md), Rule 6 Level A). |
| Not confused with the genitive | The genitive is `-s` (or `-es` after sibilants); the plural is `-en`. |
| Not confused with person vowels | The verb person markers are single vowels (`i e a u o ə`); the plural is a full syllable `-en`. |
| Moderately recognizable | Resembles plural / collective endings in several languages without copying any one too closely. |

Examples:

| Singular | Plural |
|---|---|
| `dom` | `domen` |
| `amik` | `amiken` |
| `man` | `manen` |
| `lib` | `liben` |
| `person` | `personen` |

**Note on overlap with the gerund.** The verbal-noun (gerund) suffix `-en` defined in [`verb_specification.md`](verb_specification.md) attaches to verb roots; the plural `-en` attaches to noun roots. Because roots carry an inherent category, the two cannot collide on the same word: `moven` (from verb root `mov`) is the gerund "moving", while `domen` (from noun root `dom`) is the plural "houses".

---

## 4. Morpheme Order: root + plural + case

When a noun bears a plural marker and a case suffix, the order is fixed:

```
noun root + plural marker + case suffix
```

If the noun also carries derivational morphology, the full order is:

```
noun root + derivational suffix + plural marker + case suffix
```

For example: `fac-er-en-em` = "makers (object)". The case suffix remains at the right edge of the noun phrase, in keeping with the attachment rule of [`noun_case_system.md`](noun_case_system.md) §5. See [`derivation.md`](derivation.md) for the derivational morphemes.

Combined examples:

| Form | Structure | Meaning |
|---|---|---|
| `dom` | dom | house |
| `domen` | dom-en | houses |
| `domem` | dom-em | house (object) |
| `domenem` | dom-en-em | houses (object) |
| `doms` | dom-s | house's / of the house |
| `domens` | dom-en-s | of the houses |
| `domde` | dom-de | from the house |
| `domende` | dom-en-de | from the houses |
| `domin` | dom-in | in the house |
| `domenin` | dom-en-in | in the houses |

This combination is fully regular: every noun, every plural marker, and every case suffix combine without exception.

---

## 5. Subject Nouns: Plural Optional

For subject nouns, the finite verb is normally sufficient to convey plurality:

| Sentence | Meaning |
|---|---|
| `amik mova` | the friend moves |
| `amik movə` | the friends move |
| `amiken movə` | the friends move (explicit / emphatic) |

The compact form `amik movə` is the default. The explicit form `amiken movə` is used when the speaker wants to underscore plurality — for example, when contrasting with a singular reading established earlier in the discourse.

---

## 6. Object Nouns: Plural Marked When It Matters

The verb encodes only the subject's number, not the object's. Plural objects therefore require `-en` when plurality is meaningful:

| Sentence | Meaning |
|---|---|
| `vidi domem` | I see the house / a house |
| `vidi domenem` | I see houses |
| `faci objektem` | I make the object |
| `faci objektenem` | I make objects |

When the object's number is irrelevant or generic, the bare singular form is acceptable.

---

## 7. With Numerals and Quantifiers: Plural Optional

When a numeral or quantifier already conveys plurality, `-en` is optional and usually omitted:

| Compact | Explicit | Meaning |
|---|---|---|
| `duo dom` | `duo domen` | two houses |
| `ter amik` | `ter amiken` | three friends |
| `mult dom` | `mult domen` | many houses |
| `al dom` | `al domen` | all houses |

**Rule:** After numerals and quantity words, `-en` is **optional and usually omitted**. It may be added for emphasis or in formal registers. The full list of cardinal numerals is in [`numerals.md`](numerals.md).

**The basic quantifiers.** The language has two core quantifier words:

| Quantifier | Meaning |
|---|---|
| `mult` | many / much |
| `al` | all |

Both are modifiers: they precede the noun, do not inflect, and leave `-en` optional on the noun (`mult dom` / `mult domen`; `al dom` / `al domen`). Two written-form overlaps are resolved by attachment, exactly as elsewhere in the language:

- `al` (free quantifier "all") is distinct from the bound relational suffix `-al` (see [`derivation.md`](derivation.md));
- `mult` (free quantifier "many") is the free-standing counterpart of the bound prefix `multi-` ("many-, multi-").

In both cases a space / attachment, not the spelling, distinguishes the two — the same convention used for `no` vs `no-` and `or` vs `-or`.

---

## 8. Pronouns: No Plural Suffix

The one-letter pronouns inherited from the person-vowel system already encode number:

| Form | Meaning |
|---|---|
| `i` | I |
| `e` | you (singular) |
| `a` | he / she / it |
| `u` | we |
| `o` | you (plural) |
| `ə` | they |

Therefore, **do not** form `*ien`, `*uen`, `*əen`. The pronoun system already handles number.

---

## 9. Summary of Plural Rules

1. Nouns are number-neutral by default: `dom` = house / house-concept.
2. The plural marker is `-en`: `domen` = houses.
3. In finite clauses, subject number is normally marked by the verb ending: `amik mova` (the friend moves) vs. `amik movə` (the friends move).
4. Subject plural `-en` is optional when the verb already marks plural: `amik movə` (compact) vs. `amiken movə` (explicit).
5. Object plural must be marked with `-en` when plurality matters: `vidi domem` (I see the house) vs. `vidi domenem` (I see houses).
6. With numerals and quantifiers, `-en` is optional and usually omitted: `duo dom` (two houses), `mult dom` (many houses).
7. When a noun has both plural and case, the order is **root + plural + case**: `domenem` = houses (object).
8. Pronouns do not take `-en`.

---

## 10. Final Philosophy

The language uses `-en` as the plural noun marker, combined with the morpheme order **root + plural + case**, but treats plural marking as **unnecessary on the subject when the finite verb already shows plural**. This yields compact, idiomatic sentences such as:

```
amik movə         — friends move
```

while still permitting full precision when it matters:

```
vidi amikenem     — I see friends
```
