# Vocabulary Design Rules

A formal specification of the vocabulary construction rules of the synthetic language. This document defines how lexical roots and high-frequency words must be shaped so that the language remains learnable, pronounceable, and unambiguous for speakers of the world's major language backgrounds.

## Related documents

This document builds on the rest of the specification and does not restate facts owned elsewhere:

- The official alphabet, canonical IPA values, acceptable variants, and spelling rules (`sh`, `ts`, `c`, `j`, no /h/, no /ŋ/, no `w`/`y`, etc.) are defined in [`alphabet_and_phonology.md`](alphabet_and_phonology.md).
- The person vowels (`i e a u o ə` → 1sg, 2sg, 3sg, 1pl, 2pl, 3pl) and the tense/aspect/mode markers (`d f n b m`) are defined in [`verb_specification.md`](verb_specification.md).
- The per-language compatibility analyses and the overall difficulty ranking are in [`speaker_profiles/`](speaker_profiles/).

This document introduces **no new phonemes, no new grammar, and no new vocabulary** beyond what is referenced from those sources.

---

## 1. Design Goal

The vocabulary should be shaped so that the language is:

1. **Compact.** The most frequent words and grammatical markers should be the shortest.
2. **Recognizable.** Lexical roots should often be adapted from internationally recognizable words.
3. **Regular.** Word formation should be predictable from a small number of rules.
4. **Auditorily clear.** Common words should not rely on fragile phonetic contrasts.
5. **Globally accessible.** Speakers of major language families should be able to learn and pronounce the vocabulary with minimal difficulty.

---

## 2. Main Principle

> **The alphabet may contain more contrasts than every speaker can produce perfectly. Therefore the vocabulary — especially its most frequent layer — must be designed so that the most frequent words do not differ only by contrasts that are difficult for large speaker populations.**

In practice this means:

- The sound inventory is allowed to be **moderately rich**.
- The core vocabulary must be **conservative**.
- The first **500–1000 words** should avoid fragile minimal pairs.

A contrast that is acceptable as an occasional dictionary distinction may still be inappropriate as the *only* difference between two everyday words. This principle is the foundation of every rule in this document.

The specific risks that motivate each rule below are documented in the per-language profiles in [`speaker_profiles/`](speaker_profiles/).

---

## 3. Core Vocabulary Construction Rules

### Rule 1: Avoid fragile minimal pairs in the core vocabulary

The first **500–1000 words** must not contain pairs that differ only by one fragile contrast.

**Fragile contrasts:**

- p / b
- t / d
- k / g
- f / v
- s / z
- c / j
- l / r
- a / ə
- e / i in unstressed or weak positions
- o / u in unstressed or weak positions
- s / sh
- s / ts
- sh / c
- ts / c
- final voiced / voiceless consonants
- single / double consonants

**Examples to avoid:**

| Avoid | Reason |
|---|---|
| `pa` vs `ba` | p/b is fragile for Arabic, Mandarin, Korean, Tamil |
| `fa` vs `va` | f/v is fragile for Arabic, Japanese, Korean, Spanish, Indonesian |
| `si` vs `zi` | s/z is fragile for Spanish, Japanese, Korean |
| `la` vs `ra` | l/r is fragile for Japanese and Korean |
| `mova` vs `movə` as unrelated lexical roots | a/ə is fragile |
| `rad` vs `rat` | final voicing is fragile for Russian and Korean |
| `sha` vs `sa` | s/sh is fragile for several groups |
| `tsa` vs `sa` | ts/s may simplify for some speakers |

When two candidate roots would land on a fragile pair, at least one must be replaced with a more contrastive form.

### Rule 2: Prefer simple syllable shapes

**Preferred shapes for core roots:**

- CV
- VC
- CVC
- CVCV

**Avoid in the core vocabulary:**

- CCV
- VCC
- CCVC
- CVCC
- CCC sequences

**Good examples:**

- `no`
- `si`
- `et`
- `in`
- `de`
- `ad`
- `fac`
- `mov`
- `kon`
- `vid`
- `sena`
- `tako`

**Bad examples for core vocabulary:**

- `strak`
- `sklon`
- `psa`
- `tspen`
- `frakt`

Complex onsets and codas may appear in technical or learned vocabulary, but never in the basic everyday layer.

### Rule 3: Roots may be consonant-final, but frequent finite forms should be vowel-final

The language allows compact roots such as:

- `mov` — to move
- `fac` — to do / make
- `vid` — to see
- `kon` — to know

But the **finite verb forms** that speakers actually utter usually end in a person vowel:

- `movi` — I move
- `move` — you move
- `mova` — he/she/it moves
- `movu` — we move
- `movo` — you (plural) move
- `movə` — they move

This is helpful for speakers of Japanese, Telugu, Korean, Vietnamese, and other languages where vowel-final forms are easier to produce and parse.

### Rule 4: Final grammatical vowels must never reduce

The six final vowels of finite verbs encode the grammatical subject (see [`verb_specification.md`](verb_specification.md) for the full assignment).

These vowels carry grammatical meaning. Therefore:

- `movi` ≠ `move`
- `mova` ≠ `movə`
- `movu` ≠ `movo`

**Rule:** Final person vowels in finite verbs must be **fully pronounced**. They must never be reduced, deleted, or centralized. This constraint binds both speakers and the lexical designer: no root may be coined that would compete with a person-marked verb form for the same auditory shape.

### Rule 5: Use `ə` mainly as a grammatical vowel

The vowel `ə` is useful because it marks 3rd plural in the verb system (see [`verb_specification.md`](verb_specification.md)):

- `movə` — they move
- `facə` — they do / make

However, `ə` is unstable for many language backgrounds (it may be deleted, centralized, or perceived as `a`, `e`, or `o`).

**Rule:**

- `ə` is legal.
- `ə` is primarily **grammatical**.
- Avoid heavy use of `ə` inside core lexical roots.
- Final verbal `ə` must never be deleted.

### Rule 6: Classify sounds into safety levels

Sounds in the inventory fall into three safety levels for purposes of vocabulary design.

| Level | Sounds | Use in core vocabulary |
|---|---|---|
| **A — Safest** | a e i o u; p t k; m n; f s | Use freely. Use `l` and `r` carefully (they are Level A in inventory terms but may not be safely contrasted with each other — see Rule 1). |
| **B — Usable, but not as fragile minimal contrasts** | b d g; sh; ts; c; j; ə; l/r contrasted with each other | May appear in core vocabulary, but must not be the *sole* difference between two everyday words. |
| **C — Legal but cautious in core vocabulary** | v; z | Legal phonemes, but should not carry critical distinctions in the first vocabulary layer because they are difficult or unstable for many large speaker populations. |

**Explanation:** /v/ and /z/ remain part of the official alphabet — they are needed for adapting international roots and for completing the voiced/voiceless symmetry — but the first vocabulary layer should not lean on them. A word that requires a listener to reliably distinguish /v/ from /f/, or /z/ from /s/, in order to be understood, is a poor candidate for everyday vocabulary.

### Rule 7: Grammatical markers should use robust sounds

The verb system uses short single-consonant tense/aspect/mode markers, defined in [`verb_specification.md`](verb_specification.md).

**Notes on robustness:**

- `n` and `m` are very robust.
- `f` is relatively robust.
- `d` and `b` are compact and useful but depend on voicing, so the surrounding morphology must make them clear.
- The final person vowel — itself protected by Rule 4 — helps make the form identifiable even when the marker consonant is partially devoiced or weakly articulated.

This is the reason the verb system's structure is **root + tense/aspect/mode marker + person vowel**: the protected final vowel guarantees that the marker has a clear syllabic anchor.

### Rule 8: Morphological clusters are allowed, but should be pronounceable in clear syllables

Examples drawn from the verb system:

- `movdi` — I moved
- `facdi` — I did / made
- `movdni` — I was moving
- `movfbi` — I will have moved

These may be pronounced with **clear morpheme separation** when needed for intelligibility:

| Written | Clear pronunciation |
|---|---|
| `movdi` | mov-di |
| `facdi` | fac-di |
| `movdni` | mov-d-ni |
| `movfbi` | mov-f-bi |

**Rule:** Morpheme boundaries may be pronounced with clear syllable separation. **No extra written vowel is added.** The cluster is real; the syllabic break is a pronunciation aid, not a spelling change.

### Rule 9: Avoid core roots distinguished only by final voicing

**Avoid pairs such as:**

- `rad` / `rat`
- `bag` / `bak`
- `mov` / `mof`
- `zad` / `sat`

**Reason:** Russian, Korean, Vietnamese, and other speaker groups may devoice or neutralize final consonants. A pair of core roots distinguished only by final voicing would be heard as a single word by a large fraction of the target audience.

### Rule 10: Do not use double consonants to distinguish unrelated core roots

Double consonants may arise naturally from morphology, and this is welcome (see [`verb_specification.md`](verb_specification.md) for the morphological mechanism and [`alphabet_and_phonology.md`](alphabet_and_phonology.md) for the pronunciation rule):

- `vid` — to see
- `vidi` — I see
- `viddi` — I saw

But **avoid unrelated lexical pairs** such as:

- `mala` = X
- `malla` = Y

**Rule:** Double consonants exist primarily for **morphological transparency**, not as a major lexical contrast in the core vocabulary. A learner should never need to perceive consonant length to tell two unrelated everyday words apart.

---

## 4. Adaptation Rules for International Roots

International roots are an explicit design strategy: where a meaning is widely associated with a recognizable form in many languages, the lexicon should reuse that form, adapted to the inventory.

### 4.1 Consonant adaptation

| Source sound / spelling | Adaptation |
|---|---|
| hard `c`, `q` | `k` |
| English/French `ch` /tʃ/ | `c` |
| Italian `c` in *ciao* | `c` |
| English `j`, Italian `g` in *gioco* | `j` |
| `sh`, Italian `sc` in *scena* | `sh` |
| `x` = /ks/ | `ks`, but avoid word-initial `ks` in core vocabulary |
| `ph` | `f` |
| `th` /θ ð/ | `t`, `d`, or `s` depending on source word |
| `h` | delete |
| `ng` /ŋ/ | `n` or `n` + `g`, but never /ŋ/ |
| `w` | `u` or delete |
| consonantal `y` /j/ | `i` or delete |

### 4.2 Vowel adaptation

| Source vowel area | Adaptation |
|---|---|
| /æ ɑ ɒ/ | `a` |
| /e ɛ/ | `e` |
| /i ɪ/ | `i` |
| /o ɔ/ | `o` |
| /u ʊ ɯ/ | `u` |
| central reduced vowel | `ə` only if needed |

**Rule:** Do not attempt to preserve fine vowel distinctions from the source language. All source vowels are projected onto the six-vowel system: **a e i o u ə**. The adapted form is the canonical form of the root; the source word's prosody, length, and diphthongs are not preserved.

---

## 5. Frequency and Compactness

The most frequent meanings should receive the shortest forms.

**One-letter forms are reserved for person vowels** (defined in [`verb_specification.md`](verb_specification.md)). These six single-letter forms double as the corresponding subject pronouns when needed in isolation: `i` (I), `e` (you sg.), `a` (he/she/it), `u` (we), `o` (you pl.), `ə` (they).

**Two- and three-letter forms** should be used for common grammatical words. The following are recommended fixed forms:

| Meaning | Form | Rationale |
|---|---|---|
| and | `et` | recognizable from Latin/French and compact |
| no / not | `no` | international and compact |
| yes | `si` | recognizable from Romance languages |
| in / at | `in` | international; equivalent to case suffix `-in` |
| of | `es` | equivalent to case suffix `-s` |
| from | `de` | Romance/international; equivalent to case suffix `-de` |
| to / toward | `ad` | Latin, compact; equivalent to case suffix `-ad` |
| but | `ma` | Romance, especially Italian |
| if | `if` | English, compact |
| or | `or` | English, compact |
| through / by means of | `per` | Latin/Romance, recognizable; equivalent to case suffix `-per` |

The forms `in`, `es`, `ad`, `de`, `per` may be used either as free-standing prepositions (analytic style) or as the corresponding case suffixes on the noun (compact style). The compact form is preferred in normal speech; see [`noun_case_system.md`](noun_case_system.md) §8 for the alternation rule.

Note that `et` for "and" is acceptable even though it ends in /t/. Some speakers may pronounce it with a light support vowel in careful speech, but the standard written and citation form remains `et`. The same tolerance applies to other VC and CVC grammatical words: a faint epenthetic vowel is an accent, not a change in form.

Longer forms are reserved for less frequent or more specific meanings, in keeping with the compactness principle: word length should be approximately inverse to frequency.

---

## 6. Final Recommended Philosophy

The vocabulary should follow these principles:

1. **Shortest forms for the most frequent meanings.**
2. **Recognizable roots adapted from existing languages.**
3. **No fragile minimal pairs in the core vocabulary.**
4. **Simple syllable shapes first** (CV, VC, CVC, CVCV).
5. **Final verb vowels must be clear.**
6. **`ə` is mainly grammatical.**
7. **`v` and `z` are legal but should not dominate the first vocabulary layer.**
8. **`l` and `r` are both legal, but core words should not differ only by l/r.**
9. **Voicing contrasts are legal, but should not carry high-frequency distinctions alone.**
10. **Clusters are tolerated in morphology, but avoided in basic roots.**
11. **The language is non-tonal.**
12. **Pronunciation variation is accepted as long as it does not collapse important contrasts.**

Together with [`alphabet_and_phonology.md`](alphabet_and_phonology.md), [`verb_specification.md`](verb_specification.md), and the per-language profiles in [`speaker_profiles/`](speaker_profiles/), these rules define the boundary within which the lexicon of the synthetic language must be built. Any candidate root, grammatical word, or adapted international term that violates these rules must be revised before entering the core vocabulary.
