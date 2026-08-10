# Stress and Accent

A formal specification of how lexical stress (word accent) is assigned in the synthetic language. The rule is **root stress**: the first syllable of the root carries the main accent, and inflectional and derivational morphemes do not move it.

## Related documents

- The morpheme order **root + derivation + plural + case** — which defines what "the root" is for stress purposes — is established in [`derivation.md`](derivation.md), [`noun_number_system.md`](noun_number_system.md), and [`noun_case_system.md`](noun_case_system.md).
- The verb structure **root + tense/aspect/mode marker + person vowel** is in [`verb_specification.md`](verb_specification.md).
- The rule that final person vowels must not reduce — which interacts with stress — is in [`vocabulary_design_rules.md`](vocabulary_design_rules.md) §3 Rule 4 and [`noun_number_system.md`](noun_number_system.md) §1.
- The language is non-tonal; tone never carries lexical or grammatical contrast (see [`word_order.md`](word_order.md) §5 and the Vietnamese speaker profile).

This document introduces **one rule** — root stress — and no new morphology.

---

## 1. Design Goal

- **Predictable.** A learner needs to know only one rule to place the accent on any word, regardless of how many morphemes it has.
- **Protect the root.** The lexically meaningful core of every word stays in the same acoustic position, no matter how many suffixes or prefixes attach. This keeps roots recognizable across all their inflected and derived forms.
- **No interaction with reduction.** Stress does not authorize the reduction or deletion of unstressed syllables — every final grammatical vowel must remain fully pronounced (see §6 below).
- **Compatible with many backgrounds.** Speakers from languages with root-initial or fixed-position stress (Czech, Finnish, Hungarian, Latvian, Estonian, Icelandic) apply the rule immediately. Speakers from tonal or pitch-accent traditions (Mandarin, Vietnamese, Japanese, Korean) apply a single, simple positional rule rather than learning a complex stress assignment system.

---

## 2. Options Considered

| Option | Behavior | Issue |
|---|---|---|
| **Root stress** (chosen) | First syllable of the root, fixed across all inflected and derived forms. | Requires identifying the root, but the root is always identifiable from the rules in [`derivation.md`](derivation.md). |
| Penultimate stress | Falls on the second-to-last syllable, shifts when suffixes attach. | "Simpler" in isolation, but moves around as morphology is added, blurring the root's prosodic identity. |
| Final stress | Falls on the last syllable, shifts with suffixes. | Same drawback as penultimate; also conflicts with the protected final vowel for grammar (see §6). |

Root stress is chosen because it **protects the root** in every inflected form.

---

## 3. The Rule

> **Stress falls on the first syllable of the root.** All other syllables — whether contributed by suffixes (`-er`, `-or`, `-ia`, `-it`, `-al`, `-en`, case suffixes, tense/aspect/mode markers, person vowels) or by prefixes (`no-`, `anti-`, `de-`, `re-`, `pre-`, `pos-`, `ko-`, `auto-`, `semi-`, `multi-`, `neo-`, `super-`, `sub-`, `mikro-`, `makro-`) — are **unstressed**.

The rule is positional and absolute: identify the root, find its first syllable, accent it. There are no exceptions and no irregular paradigms.

---

## 4. Notation Used in This Document

To show stress clearly, this document uses two conventions in its examples:

- **`CAPITAL LETTERS`** mark the stressed syllable.
- **Hyphens** mark syllable / morpheme boundaries.

So `MO-vi` indicates that `movi` is pronounced with the stress on the first syllable `MO`, and `-vi` is unstressed.

These conventions are pedagogical: the language's standard orthography does not write stress marks.

---

## 5. Worked Examples

### 5.1 Suffix-only forms

| Form | Stress | Meaning |
|---|---|---|
| `movi` | MO-vi | I move |
| `movdi` | MOV-di | I moved |
| `movdni` | MOV-dni | I was moving |
| `movfbi` | MOV-fbi | I will have moved |
| `dom` | DOM | house |
| `domen` | DO-men | houses |
| `domenem` | DO-men-em | houses (object) |
| `domenes` | DO-men-es | of the houses |
| `facer` | FA-cer | maker |
| `faceren` | FA-cer-en | makers |
| `facerenem` | FA-cer-en-em | makers (object) |

In each case the root (`mov`, `dom`, `fac`) keeps the accent on its first syllable, and every suffix that follows stays unstressed.

### 5.2 Forms with prefixes

The same rule applies when one or more prefixes attach: the root, not the prefix, takes the stress.

| Form | Stress | Meaning |
|---|---|---|
| `defac` | de-FAC | undo |
| `refac` | re-FAC | remake |
| `prefac` | pre-FAC | pre-make |
| `kofac` | ko-FAC | co-make |
| `automov` | au-to-MOV | self-moving / automatic |
| `multifacal` | mul-ti-FA-cal | multi-functional |
| `mikrosistem` | mi-kro-SIS-tem | micro-system |
| `antifacal` | an-ti-FA-cal | opposed to practical |

The principle remains: regardless of how many syllables of prefix material precede the root, the accent lands on the root's first syllable.

### 5.3 Multi-syllable function words

Function words that are themselves multi-syllabic (`major`, `minor`, `masim`, `minus`, `ekual`, etc.) are treated as their own "roots" and follow the same rule:

| Form | Stress | Meaning |
|---|---|---|
| `major` | MA-jor | comparative more |
| `minor` | MI-nor | comparative less |
| `masim` | MA-sim | superlative most |
| `minus` | MI-nus | superlative least |
| `ekual` | E-ku-al | equal / as |
| `uno` | U-no | one / a |
| `duo` | DU-o | two |

### 5.4 Monosyllabic words

Single-syllable roots and function words carry the accent on their one and only syllable: `dom`, `mov`, `vid`, `fac`, `ka`, `kid`, `kis`, `no`, `et`, `in`, `de`, `ad`, `or`, `if`. No notation is needed.

### 5.5 Compound numerals

Multi-word numerals (see [`numerals.md`](numerals.md)) are sequences of independent words, and **each word keeps its own root stress**. There is no phrase-level reduction or single primary accent across the sequence:

| Numeral | Stress | Value |
|---|---|---|
| `duo dek uno` | DU-o · DEK · U-no | twenty-one |
| `ter sen` | TER · SEN | three hundred |

Each numeral word is stressed on the first syllable of its own root; none is subordinated to another.

---

## 6. Interaction with Unstressed Final Vowels

Several rules elsewhere in the spec require that **final grammatical vowels remain fully pronounced**, never reduced or centralized:

- The person vowel on every finite verb (see [`vocabulary_design_rules.md`](vocabulary_design_rules.md) §3 Rule 4 and [`verb_specification.md`](verb_specification.md));
- The 3rd-person-plural marker `-ə` in particular (see [`noun_number_system.md`](noun_number_system.md) §1);
- Case suffixes such as `-em`, `-de`, `-ad`, `-in`, `-ko`, `-pro`, `-due`, `-fin`, `-tem`, `-mod`.

These requirements must be **respected even though the relevant syllables are unstressed**. This language explicitly rejects the English / Russian / Portuguese pattern in which unstressed syllables reduce toward [ə] or are deleted. Unstressed ≠ reduced; the root is acoustically prominent, but the rest of the word still articulates every vowel clearly.

For example, in `MO-vi` the accent is on `MO`, but the final `i` (which marks 1st singular) must be heard distinctly. Reducing `MO-vi` to something like ['mo.və] would destroy the person agreement and produce a different grammatical meaning.

---

## 7. Rationale

- **Root protection.** A native speaker of the language hears every form of `fac` — `fac`, `faci`, `facdi`, `facer`, `defac`, `kofac`, `autofac`, `multifacal` — with the same acoustic prominence on `fa`. This makes the root unmistakable and supports rapid recognition of vocabulary, even in unfamiliar derived forms.
- **One simple rule.** Penultimate stress is also simple, but it forces the stress to wander as morphology is added; the learner must compute syllable count for every form. Root stress requires only that the learner identify the root, which the morphological rules already make trivial.
- **No reduction.** Because unstressed syllables are not reduced, grammatical contrasts carried in suffixes (person, tense, case, plural) survive intact. Stress and grammar do not compete for prominence.
- **Broad cross-linguistic compatibility.** Fixed-position stress is found in many of the language's target backgrounds (Czech, Finnish, Hungarian, Latvian, Estonian, Icelandic — first-syllable stress; Turkish — typically final but predictable). Speakers from tonal and pitch-accent languages (Mandarin, Vietnamese, Japanese, Korean) face a single, mechanical positional rule rather than a complex assignment system.
