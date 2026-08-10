# Noun Case System

A formal specification of the noun case system of the synthetic language. This document defines the case suffixes, the rule by which they attach to noun phrases, and the phonological adjustments that govern their surface form.

## Related documents

- The official alphabet, phoneme inventory, and the rules forbidding /w/ and /y/ are defined in [`alphabet_and_phonology.md`](alphabet_and_phonology.md).
- The general principles of compactness, recognizability, regularity, and auditory clarity that motivate every design choice below are established in [`verb_specification.md`](verb_specification.md) (for the verb system) and [`vocabulary_design_rules.md`](vocabulary_design_rules.md) (for lexical roots).

This document introduces **no new phonemes** and no new grammatical categories beyond the case markers listed here.

---

## 1. Design Goals

The case system is built around the same four priorities as the rest of the language:

1. **Compactness.** The most frequent grammatical relations (subject, object, possession, location, direction) use the shortest markers.
2. **Recognizability.** Suffix forms are chosen so that speakers familiar with international roots (`de`, `ad`, `in`, `per`, `pro`, `tem`, `mod`, `fin`) can guess the meaning on first encounter.
3. **Regularity.** A single suffix marks each case. There are no irregular paradigms, no declension classes, and no agreement between noun and modifier.
4. **Auditory clarity.** The case marker is always the **final segment** of the noun phrase, so the listener can identify the grammatical role without backtracking.

---

## 2. Base Cases

The seven base cases cover the most frequent grammatical relations:

| Suffix | Function | Meaning |
|---|---|---|
| Ø | nominative / base | subject, dictionary form |
| `-em` | accusative | direct object |
| `-s` | genitive | possessive / of |
| `-de` | ablative | from / source / origin |
| `-ad` | allative / dative | to / toward / recipient |
| `-in` | locative | in / at / location |
| `-ko` | comitative | with / together with |

---

## 3. Extended Cases

The six extended cases cover relations that are useful but less frequent than the base set:

| Suffix | Function | Meaning |
|---|---|---|
| `-per` | instrumental / perlative | through / by means of |
| `-pro` | benefactive | for the benefit of |
| `-due` | causal | because of / due to |
| `-fin` | purposive | for the purpose of |
| `-tem` | temporal | at / during |
| `-mod` | modal / manner | in the manner of |

---

## 4. Worked Example: `dom` (house)

| Form | Meaning |
|---|---|
| `dom` | house / the house (as subject) |
| `domem` | the house (as direct object) |
| `doms` | house's / of the house |
| `domde` | from the house |
| `domad` | to the house |
| `domin` | in / at the house |
| `domko` | with the house |
| `domper` | through / by means of the house |
| `dompro` | for the benefit of the house |
| `domdue` | because of the house |
| `domfin` | for the purpose of the house |
| `domtem` | during / at the time of the house |
| `dommod` | in the manner / style of the house |

---

## 5. Attachment Rule

The case suffix attaches to the **noun phrase**, preferably to its **final word**:

```
bon dom-in        = in the good house
```

It does **not** attach to each modifier:

```
*bon-in dom-in   (incorrect)
```

**Consequence:** adjectives and other modifiers do **not** agree with the noun in case. The language has no declension agreement between modifiers and head nouns. The grammatical role of the entire noun phrase is signaled exactly once, at its right edge.

**Rationale.** Agreement would require every modifier to repeat the case marker, multiplying the morphology without adding information. Confining the marker to the final word of the noun phrase keeps the system compact, preserves the "marker is always final" parsing guarantee, and matches the same logic that places the person vowel at the end of every finite verb in [`verb_specification.md`](verb_specification.md).

**Interaction with derivation and the plural suffix.** When the noun also bears derivational morphology (`-er`, `-or`, `-ia`, `-it`, `-al`, `no-`, `anti-`) and/or the plural marker `-en`, the morpheme order is fixed as **root + derivation + plural + case** — for example, `dom-en-em` = "houses (object)", `fac-er-en-em` = "makers (object)". The case suffix always remains at the right edge. The full rules are in [`derivation.md`](derivation.md) and [`noun_number_system.md`](noun_number_system.md).

---

## 6. Genitive Usage

The genitive marker `-s` (or `-es` after sibilants — see §7.1) produces a possessive or descriptive modifier that **precedes the head noun** it modifies.

### 6.1 Word order

The genitive-marked noun phrase precedes the head noun. There is no overt linker between the modifier and the head; the genitive suffix on the modifier is the sole signal of the relationship.

| Form | Meaning |
|---|---|
| `amiks dom` | the friend's house |
| `mators part` | part of the motor |
| `doms port` | door of the house |

### 6.2 Personal possessives

Applying the genitive `-s` directly to a personal pronoun (see [`verb_specification.md`](verb_specification.md) for the person-vowel inventory) yields a possessive pronoun:

| Form | Decomposition | Meaning |
|---|---|---|
| `is` | i + s | my / of me |
| `es` | e + s | your (sg.) / of you |
| `as` | a + s | his / her / its |
| `us` | u + s | our |
| `os` | o + s | your (pl.) |
| `əs` | ə + s | their |

These possessives follow the same word-order rule as other genitives:

| Form | Meaning |
|---|---|
| `is dom` | my house |
| `es dom` | your house |
| `as dom` | his/her/its house |
| `us dom` | our house |
| `os dom` | your (pl.) house |
| `əs dom` | their house |

**Rationale.** No separate possessive paradigm is needed. The personal pronouns are simply nominal forms, and the genitive marker applies to them in the same regular way it applies to any noun.

### 6.3 Possessives with plural and case

The possessive is a separate word that precedes the head noun; it does not itself inflect. The head noun carries its own plural and case marking in the regular **root + plural + case** order (see [`noun_number_system.md`](noun_number_system.md) §4):

| Form | Structure | Meaning |
|---|---|---|
| `is dom` | is · dom | my house |
| `is domen` | is · dom-en | my houses |
| `is domem` | is · dom-em | my house (object) |
| `is domenem` | is · dom-en-em | my houses (object) |
| `as domenin` | as · dom-en-in | in his/her houses |

The number and case suffixes attach to the head noun, never to the possessive word.

---

## 7. Phonological Notes

### 7.1 Genitive `-s` / `-es`

The genitive normally surfaces as `-s`. After a stem ending in a sibilant (`s`, `z`, `sh`, `ts`, `c`, `j`), a support vowel is inserted and the suffix surfaces as `-es`. This avoids hard sibilant clusters such as `*facs`, `*shashs`, `*tsens` that would be difficult to perceive or produce.

| Base | Genitive |
|---|---|
| `dom` | `doms` |
| `amik` | `amiks` |
| `fac` | `faces` |
| `shas` | `shases` |
| `tsen` | `tsenes` |

**Rule:** Use `-es` when the stem ends in any of `s`, `z`, `sh`, `ts`, `c`, `j`. Use `-s` otherwise.

### 7.2 Causal `-due`

The alphabet does not contain the letters `w` or `y` (see [`alphabet_and_phonology.md`](alphabet_and_phonology.md)). The sequence `ue` in `-due` is therefore pronounced as **two syllables**:

```
-due = /du.e/
```

So:

```
domdue = /dom.du.e/
```

This is acceptable. The suffix is slightly longer than the others, but its meaning ("because of / due to") is less basic than direct object, possession, direction, and location, so the additional length is justified by the principle that word length should be approximately inverse to frequency (see [`vocabulary_design_rules.md`](vocabulary_design_rules.md) §5).

---

## 8. Analytic and Compact Forms

Several of the case suffixes have an alternative **free form** — a separate two- or three-letter word used as a preposition before the noun. The two are equivalent in meaning; the choice between them is stylistic.

| Function | Free form | Suffix |
|---|---|---|
| in / at | `in` | `-in` |
| of | `es` | `-s` |
| to / toward | `ad` | `-ad` |
| from | `de` | `-de` |
| through / by means of | `per` | `-per` |

In normal speech the **suffix form is preferred**, because it is more compact and keeps the case marker at the right edge of the noun phrase (see §5):

| Analytic | Compact |
|---|---|
| `in dom` | `domin` |
| `es dom` | `doms` |
| `ad dom` | `domad` |
| `de dom` | `domde` |
| `per man` | `manper` |

The free forms remain available for emphasis or for a more analytic phrasing. The remaining case suffixes (`-em`, `-ko`, `-pro`, `-due`, `-fin`, `-tem`, `-mod`) have no free-form equivalents in the current specification.

**Rationale.** The free forms `in`, `es`, `ad`, `de`, `per` are also listed in [`vocabulary_design_rules.md`](vocabulary_design_rules.md) §5 as recommended short grammatical words drawn from international sources. Recognizing that they encode exactly the same relations as the corresponding case suffixes lets a speaker familiar with European prepositional patterns transfer their habit directly, while a learner who prefers the strict suffix system can use the compact form throughout. Both are correct.

---

## 9. Final Case System

```
BASE:
Ø    = base / subject
-em  = direct object
-s   = genitive / possessive / of
-de  = from / source / origin
-ad  = to / toward / recipient
-in  = in / at / location
-ko  = with / together with

EXTENDED:
-per = through / by means of
-pro = for the benefit of
-due = because of / due to
-fin = for the purpose of
-tem = at / during
-mod = in the manner of
```

The system is **compact** for frequent relations and **explicit** for less frequent ones. Combined with the noun-phrase attachment rule, it gives the language a complete and unambiguous nominal morphology without introducing declension classes or modifier agreement.
