# Demonstratives

A formal specification of the demonstrative system of the synthetic language. The language has **three demonstratives** marking three degrees of deictic distance, with **no gender distinction**. This document is authoritative for the demonstrative system; it supersedes the earlier binary `ic` / `ta` proposal in favor of the three-grade `tik` / `tes` / `tan` series defined here.

## Related documents

- Demonstratives are optional precision tools; the bare noun remains the default. See [`articles.md`](articles.md) for the no-obligatory-articles rule.
- Demonstratives precede the noun and remain invariant, like other modifiers. See [`adjectives.md`](adjectives.md) for the modifier rule, and [`noun_case_system.md`](noun_case_system.md) §5 for the case-attachment rule.
- Vowel-only contrasts in core vocabulary are avoided per [`vocabulary_design_rules.md`](vocabulary_design_rules.md) Rule 1 and Rule 6 — which motivates the three-letter forms below.

This document introduces **three demonstratives**: `tik` (this), `tes` (that near you), `tan` (that, far from both).

---

## 1. Design Goal

- **Three deictic grades**, modeled on the Latin distinction `hic` / `iste` / `ille`.
- **No gender distinction.** One form covers every referent (person or thing, regardless of natural gender).
- **Auditory robustness.** Each form is distinguished from the others by both vowel and final consonant, not by vowel alone.
- **Compactness.** Each form is three letters, CVC.

---

## 2. The Three Grades

The system encodes three degrees of distance from the speech-act participants:

| Distance | Latin (for comparison) | English gloss | Meaning |
|---|---|---|---|
| Near speaker | `hic / haec / hoc` | this | proximal |
| Near listener | `iste / ista / istud` | that (near you / yours) | medial |
| Far from both | `ille / illa / illud` | that (over there) | distal |

In this language the three grades are encoded by three dedicated forms, with **no gender distinction**:

| Grade | Form | Meaning |
|---|---|---|
| Proximal (near speaker) | `tik` | this |
| Medial (near listener) | `tes` | that (near you) |
| Distal (far from both) | `tan` | that (far) |

Each form differs from the others in both **vowel** and **final consonant**, so the three-way contrast is robust even for speakers whose native phonology produces less reliable vowel distinctions (see [`vocabulary_design_rules.md`](vocabulary_design_rules.md) Rule 1).

---

## 3. Worked Examples

Demonstratives precede the noun, following the modifier-before-head pattern used throughout the grammar (see [`adjectives.md`](adjectives.md)).

| Italian | Form | English |
|---|---|---|
| questo uomo | `tik vir` | this man |
| codesto uomo / quell'uomo vicino a te | `tes vir` | that man (near you) |
| quell'uomo | `tan vir` | that man (over there) |
| questa casa | `tik dom` | this house |
| codesta casa | `tes dom` | that house (near you) |
| quella casa | `tan dom` | that house (over there) |

---

## 4. Interaction with Case, Plural, and Other Modifiers

Like all other modifiers, demonstratives are **invariant**: they do not inflect for case, number, or any other category. Case and plural attach to the noun, which sits at the right edge of the noun phrase (see [`noun_case_system.md`](noun_case_system.md) §5 and [`noun_number_system.md`](noun_number_system.md) §4).

| Form | Meaning |
|---|---|
| `tik dom` | this house |
| `tik domem` | this house (direct object) |
| `tik domen` | these houses |
| `tik domenem` | these houses (direct object) |
| `tan doms` | of that house / that house's |
| `tes domin` | in that house (near you) |

Demonstratives can stack with adjectives and other modifiers, all of which sit before the noun without inflecting:

```
tik bon dom    — this good house
tan duo domen  — those two houses
```

---

## 5. Why Three Letters (Not Two)

A simpler series would distinguish the three forms by vowel alone:

| Compact proposal | Meaning |
|---|---|
| `ti` | this |
| `te` | that (near you) |
| `ta` | that (far) |

This is rejected because the language tries to avoid core-vocabulary contrasts that depend solely on vowel-letters (see [`vocabulary_design_rules.md`](vocabulary_design_rules.md) Rule 1, which lists `e / i` and `a / ə` and other vowel-only pairs as fragile for many target backgrounds). Demonstratives are high-frequency words, so they deserve a more robust distinction.

The chosen series adds a second distinguishing feature — the final consonant — so each form changes both vowel **and** coda:

```
tik   /   tes   /   tan
```

A more directly latinate series was also considered:

| Latin | Adapted | Issue |
|---|---|---|
| `hic / hoc` | `ik` | loses `h` (correct per the alphabet), but two letters only |
| `iste` | `ist` | final cluster `st` is harder than a simple coda |
| `ille` | `ile` | acceptable |

The resulting `ik` / `ist` / `ile` set is less regular and less acoustically balanced than `tik` / `tes` / `tan`, so the latter is preferred.

---

## 6. Rule

> **Demonstrative + noun.** The demonstrative precedes the noun. The demonstrative does not inflect; case and plural attach to the noun.

Examples with case:

```
tik domem      — this house as direct object
tan doms       — of that house / that house's
tes domin      — in that house (near you)
```

---

## 7. Rationale

- Three grades give the language Latin-style deictic precision, which is useful in conversations involving multiple participants where "this" / "that" alone would be ambiguous.
- No gender keeps the system uniform with the rest of the language, in which modifiers (adjectives, articles, demonstratives, genitives, numerals) all remain invariant.
- The chosen forms `tik` / `tes` / `tan` retain the latinate `t-` onset (recognizable from Romance demonstratives) while giving each form a distinct vowel-and-coda profile, making them robust for speakers from many backgrounds.
- Three letters per form match the rhythm of the cardinal numerals (see [`numerals.md`](numerals.md)) and stay phonotactically simple (CVC, no clusters).
