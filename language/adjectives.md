# Adjectives

A formal specification of how adjectives modify nouns in the synthetic language: where they sit relative to the noun, and how they interact with case and plural marking.

## Related documents

- The rule that case suffixes attach to the noun and that modifiers do not agree is defined in [`noun_case_system.md`](noun_case_system.md) §4.
- The optional plural particle `wi` precedes the noun phrase and does not trigger modifier agreement; see [`noun_number_system.md`](noun_number_system.md).
- The default constituent order (SVO) is in [`word_order.md`](word_order.md).
- Other pre-nominal modifiers — determiners, genitives, numerals — follow the same modifier-before-head pattern documented here (see [`articles.md`](articles.md), [`numerals.md`](numerals.md), [`noun_case_system.md`](noun_case_system.md) §6.1).

This document introduces **no new morphemes** — only the placement rule for adjectives.

---

## 1. Design Goal

The adjective rule must be:

- **compact** — modifiers add information without adding morphology;
- **predictable** — every adjective sits in the same position relative to its head noun;
- **broadly familiar** — the chosen order should match the strongest set of target speaker backgrounds.

---

## 2. Options Considered

| Order | Example | Most familiar to |
|---|---|---|
| Adjective before noun | big house | English, Mandarin, Turkish, Japanese (Adj-N is the norm in Japanese), German |
| Adjective after noun | house big | Romance languages, Arabic, Indonesian, Vietnamese |

---

## 3. The Choice: Adjective Before Noun

The unmarked order is **adjective + noun**:

```
bon dom
= good house
```

This matches the order used in English, Mandarin, Turkish, Japanese, and German, and is consistent with the other modifier-before-head patterns already established in the language (determiners precede the noun, genitives precede the head, numerals precede the noun).

---

## 4. Interaction with Case and Plural

A synthetic case suffix attaches once to the head noun; optional plural `wi` precedes the phrase. Adjectives **do not agree** with the noun in case or number.

| Form | Meaning |
|---|---|
| `bon dom` | a good house / the good house |
| `bon domem` | a good house (direct object) |
| `wi bon dom` | good houses, explicitly plural |
| `wi bon domem` | good houses (direct object), explicitly plural |
| `bon domin` | in the good house |

The adjective `bon` is invariant in all of these. Case attaches to the head noun, while explicit nominal plural is the separate pre-nominal particle `wi`.

**Stacking modifiers.** When more than one modifier appears, all of them sit before the noun and none of them inflect; case still applies once at the noun-phrase edge, while optional plural `wi` precedes the phrase:

| Form | Meaning |
|---|---|
| `tik bon dom` | this good house |
| `bis bon dom` | two good houses |
| `amiks bon dom` | the friend's good house |

**Order of stacked modifiers.** When several pre-nominal modifiers co-occur, their relative order is fixed:

```
(genitive/possessive) + demonstrative + numeral + adjective + noun
```

| Form | Meaning |
|---|---|
| `tik bis bon dom` | these two good houses |
| `amiks tik bis bon dom` | the friend's these two good houses |

A genitive or possessive phrase, when present, sits at the very front of the noun phrase; the demonstrative, numeral, and adjective then follow in that order, with the head noun last. As always, synthetic case attaches only to the head noun; `wi` is a separate pre-nominal plural particle and is normally omitted when a numeral already gives quantity.

---

## 5. Rationale

- Adjective-before-noun is the unmarked order in several of the language's largest target speaker populations (English, Mandarin, Turkish, Japanese, German). Choosing it as the default minimizes parsing effort for that group.
- It is consistent with every other modifier-head pattern already in the language — determiners, genitives, numerals — so a learner only needs to internalize one rule: *modifiers come before the noun*.
- The no-agreement rule keeps adjectives morphologically trivial: a learner who knows the adjective root knows every form of it. There are no declension classes and no irregular agreement.
- Together, the fixed position and the absence of agreement mean that an adjective adds meaning without adding any morphological work.
