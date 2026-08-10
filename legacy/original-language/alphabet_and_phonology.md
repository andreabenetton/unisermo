# Alphabet and Phonology

A formal specification of the alphabet and sound system of the synthetic language. This document defines the official letters, their canonical IPA values, the range of acceptable pronunciation variants, the rationale behind each decision, and the orthographic restrictions that preserve unambiguous reading and writing.

This specification is designed to interoperate with the verb system defined in `verb_specification.md`, where the six vowels also serve as person markers.

---

## 1. Design Principles

The alphabet and phonological inventory are governed by six core principles:

1. **One-to-one mapping.** Each written unit corresponds to exactly one phoneme, and each phoneme is written with exactly one fixed unit.
2. **Compact but expressive.** The inventory is kept small enough to be learnable in a single sitting, yet large enough to encode meaningful contrasts across roots and grammatical markers.
3. **Cross-linguistically recognizable.** Phonemes are chosen from sounds that occur in many of the world's most widely spoken languages, so that speakers of varied backgrounds can both produce and perceive them.
4. **No weak or unstable consonants.** Sounds that are typically dropped, lenited, or lost across dialects (e.g. /h/) are excluded, so that words are reliably heard.
5. **No regionally rare or difficult consonants.** Sounds that present serious difficulty for large speaker populations (e.g. clicks, ejectives, uvular fricatives as primary phonemes) are excluded.
6. **Controlled variation.** Some acoustic variation in realization is tolerated, but only when it does not destroy a phonemic contrast between two distinct letters.

---

## 2. Official Alphabet

The language has **24 written units**: **6 vowels** and **18 consonants**.

**Vowels:**

```
a  e  i  o  u  ə
```

**Consonants:**

```
p  b  t  d  k  g
m  n
f  v  s  z  sh
ts c  j
l  r
```

Important notes about written units:

- `sh` is a **single written unit** representing the single phoneme /ʃ/.
- `ts` is a **single written unit** representing the single phoneme /ts/.
- `c` represents **/tʃ/**, as in Italian `ciao` or English `church`. It never represents /k/.
- `j` represents **/dʒ/**, as in English `job` or Italian `gioco`. It never represents the IPA glide [j].
- There is **no letter `h`** and **no phoneme /h/**.
- There is **no `ng` phoneme** /ŋ/. The sequence `ng` is always read as two phonemes /n/ + /g/.
- There are **no letters `w` or `y`** in the current official inventory.
- The sound **/k/ is always written `k`**, never `c`.

---

## 3. Vowel Inventory

| Letter | Canonical IPA | Acceptable IPA variants | Not acceptable | Explanation |
|---|---|---|---|---|
| a | /a/ | [a], [ä], [ɑ], [ɐ] | [e], [o], [ə] | An open vowel. Front, central, or back realizations are all accepted as long as the result remains clearly low and unrounded, and distinct from /e/, /o/, and /ə/. |
| e | /e/ | [e], [ɛ] | [i], [a], [ə] | A front mid unrounded vowel. Slight opening to [ɛ] is permitted, but it must not collapse with /a/ or be heard as /i/ or /ə/. |
| i | /i/ | [i], [ɪ], [ɨ] | [e], [j] as consonant | A high unrounded vowel. May be slightly lax or centralized, but must remain clearly higher than /e/ and must never be reduced to a consonantal glide. |
| o | /o/ | [o], [ɔ] | [u], [a], [ə] | A back mid rounded vowel. Slight opening to [ɔ] is permitted, but it must not collapse with /u/ or /a/. |
| u | /u/ | [u], [ʊ], [ɯ] | [o], [w] as consonant | A high rounded back vowel. Slight laxing or loss of rounding is tolerated, but it must remain clearly higher than /o/ and must never be reduced to a consonantal glide. |
| ə | /ə/ | [ə], [ɘ], [ɜ], [ʌ] | [a], [e], [o] when clearly pronounced as full non-central vowels | A central vowel. It must remain perceptibly central and distinct from the five peripheral vowels above. |

### 3.1 Vowels as person markers

The six vowels are not only phonological units; each one also functions as a **person marker** when it appears as the final segment of a finite verb. The full assignment of vowels to grammatical persons is defined in [`verb_specification.md`](verb_specification.md).

The phonological consequence is that the six vowel categories **must remain perceptibly distinct** at all times. A speaker who collapses, for instance, /e/ into /i/, or /o/ into /u/, or /ə/ into /a/, will not merely sound foreign — they will produce a different grammatical person. The acceptable-variant ranges above were chosen specifically so that no permitted realization of one vowel can be mistaken for the canonical realization of another.

---

## 4. Consonant Inventory

| Written form | Canonical IPA | Acceptable IPA variants | Not acceptable | Explanation |
|---|---|---|---|---|
| p | /p/ | [p], [pʰ] | [b], [f] | Voiceless bilabial stop. Aspiration is allowed but must not voice the consonant. |
| b | /b/ | [b], [b̥] if still distinct from /p/ | [p], [v] | Voiced bilabial stop. Partial devoicing is tolerated only as long as the contrast with /p/ is maintained. |
| t | /t/ | [t], [t̪], [tʰ] | [d], [ts], [tʃ] | Voiceless coronal stop. Dental or alveolar place is free; aspiration is allowed; it must not affricate into /ts/ or /tʃ/. |
| d | /d/ | [d], [d̪], [d̥] if still distinct from /t/ | [t], [z] | Voiced coronal stop. Place is free; partial devoicing is tolerated only as long as the contrast with /t/ is maintained. |
| k | /k/ | [k], [kʰ] | [g], [tʃ] | Voiceless velar stop. Aspiration is allowed. It must never palatalize into /tʃ/. |
| g | /g/ | [g], [ɡ], [g̊] if still distinct from /k/ | [k], [dʒ] | Voiced velar stop. Always **hard**: it never softens to /dʒ/, regardless of the following vowel. |
| m | /m/ | [m] | [n] | Bilabial nasal. Stable across positions. |
| n | /n/ | [n], [n̪] | [m], [ŋ] as a separate phoneme | Coronal nasal. Phonetic assimilation to a velar before /g/ or /k/ is not phonemic — see §6.2. |
| f | /f/ | [f] | [v], [p] | Voiceless labial fricative. Must remain a clear fricative, not a stop. |
| v | /v/ | [v], [ʋ], [β] if still distinct from /f/ | [f], [w] | Voiced labial fricative or approximant. It must never collapse into a /w/-like glide or into the vowel /u/. |
| s | /s/ | [s] | [z], [ʃ], [ts] | Voiceless coronal sibilant. Must not affricate or palatalize. |
| z | /z/ | [z], [z̥] if still distinct from /s/ | [s], [ʒ], [dz] | Voiced coronal sibilant. Partial devoicing is tolerated only as long as the contrast with /s/ is maintained. |
| sh | /ʃ/ | [ʃ], [ɕ] if still distinct from /s/ | [s], [tʃ], [ʒ] | Voiceless postalveolar fricative. A more palatal [ɕ] is tolerated but it must not merge with /s/ or affricate into /tʃ/. |
| ts | /ts/ | [ts], [t͡s] | [s], [tʃ], [z] | Voiceless coronal affricate, treated as one phoneme. It must remain crisp and distinct from /s/ and from /tʃ/. |
| c | /tʃ/ | [tʃ], [t͡ʃ], [tɕ] if still distinct from /ts/ | [k], [ʃ], [dʒ] | Voiceless postalveolar affricate. A more palatal [tɕ] is tolerated only if it stays distinct from /ts/. It is **never** /k/. |
| j | /dʒ/ | [dʒ], [d͡ʒ], [dʑ] if still distinct from /tʃ/ | [ʒ], [j], [tʃ] | Voiced counterpart of `c`. It is **never** an IPA glide [j], and it must not deaffricate into [ʒ]. |
| l | /l/ | [l], [ɫ] | [r], [ɾ] | Lateral approximant. Velarized "dark" [ɫ] is acceptable; rhotic realizations are not. |
| r | /r/ | [r], [ɾ], [ɹ], [ʁ] | [l], vowel-like coloring that deletes the consonant | A single rhotic category. Trill, tap, approximant, and uvular realizations are all accepted as long as a perceptible consonant remains and it is distinct from /l/. |

---

## 5. Rationale for Major Choices

### 5.1 No /h/

The sound /h/ is excluded from the inventory. Cross-linguistically, /h/ is one of the weakest and most unstable consonants: it is frequently dropped at word boundaries, lenited intervocalically, lost entirely in fast speech, and absent from the inventories of many large language families. Because this language prioritizes **reliable perception** (principle 4), admitting /h/ would create a class of words whose initial segment is unreliably present. /h/ is therefore not a phoneme of the language, and the letter `h` does not exist in the alphabet.

### 5.2 No /ŋ/ written as `ng`

The phoneme /ŋ/ is excluded. The most natural way to spell /ŋ/ in a Latin alphabet — the digraph `ng` — creates a structural ambiguity, because the same digraph could also be read as the two-phoneme sequence /n/ + /g/. Languages that admit both readings (e.g. English `singer` vs. `finger`) require speakers to memorize which is which on a per-word basis, violating principle 1 (one-to-one mapping).

In this language, `n` followed by `g` is **always pronounced as two phonemes /nɡ/**. There is no /ŋ/.

Examples:

- `naga` = /naga/
- `sang` = /sang/
- The pronunciation /saŋ/ does not exist.

Phonetic assimilation of [n] toward [ŋ] before a velar is a natural artifact of articulation and is not penalized, but it has no phonemic status: the underlying segment is always /n/ + /g/.

### 5.3 `c` = /tʃ/

The letter `c` is assigned to /tʃ/. This gives a **compact one-letter spelling** for a high-frequency affricate, satisfying the compactness principle and avoiding the digraph `ch`.

Examples:

- `ca` = /tʃa/
- `ce` = /tʃe/
- `ci` = /tʃi/
- `co` = /tʃo/
- `cu` = /tʃu/
- `cə` = /tʃə/

The letter `c` **never means /k/**. The sound /k/ is always written `k`, regardless of the following vowel. This eliminates the soft-c/hard-c ambiguity found in many European orthographies.

### 5.4 `j` = /dʒ/

The letter `j` is the **voiced counterpart** of `c`:

- `c` = /tʃ/
- `j` = /dʒ/

This yields a clean voiceless/voiced pair, in keeping with the symmetry already present across the stop and fricative series. The letter `j` is never used for the IPA glide [j] (which has no phonemic status in this language).

### 5.5 `sh` = /ʃ/

The digraph `sh` is retained because /ʃ/ is a common, recognizable, and easily produced fricative across many language backgrounds. An alternative single-letter spelling (e.g. `x`) was considered but not adopted in the current orthography; `sh` is more transparently readable to the broadest set of speakers. As a digraph it is treated as one written unit and one phoneme.

### 5.6 `ts` = /ts/

The digraph `ts` is **a single phoneme**, not an accidental /t/ + /s/ sequence. /ts/ is admitted because it is crisp, perceptually clear, and reliably distinct from both /s/ and /tʃ/. Treating it as a unitary unit avoids irregular parsing in morphologically derived forms and gives the affricate series a complete voiceless inventory: /ts/ alongside /tʃ/.

---

## 6. Contrast Rules

Accepted variants are tolerated **only when they do not collapse a phonemic contrast**. The acceptable-variant ranges in the tables above are upper bounds on tolerance, not licenses to merge categories. If a particular speaker's realization of one letter happens to fall within the canonical range of another, the realization is not acceptable for that speaker, regardless of whether it appears in the abstract variant list.

Examples:

- A speaker may pronounce `p` as [pʰ], but it must remain distinct from `b`.
- A speaker may pronounce `e` as [ɛ], but it must remain distinct from `a`.
- A speaker may pronounce `r` as [ɾ], [r], [ɹ], or [ʁ], but it must remain distinct from `l`.
- A speaker may pronounce `v` as [ʋ], but it must not become identical to the vowel /u/ or to a removed /w/ sound.

This rule applies symmetrically to all consonant and vowel pairs: tolerance is granted for ease of pronunciation, never at the cost of meaning.

---

## 7. Double Consonants

When morphology brings two identical consonants into contact, they are **written double** and **preferably pronounced as a long (geminated) consonant**, in the style of Italian.

Example, from the verb root `vid` ("to see"):

- `vid` = to see (bare root / imperative)
- `vidi` = I see
- `viddi` = I saw

`viddi` is pronounced approximately /vidːi/.

Gemination here arises naturally from the morphology: the past-tense marker `-d-` attached to a root ending in `d` produces the surface sequence `dd`. The double letter is **always written**, so that morphological boundaries remain transparent.

To keep gemination from becoming a perceptual burden, the language **avoids basic lexical pairs whose members differ only by consonant length** (e.g. a hypothetical minimal pair `kata` vs. `katta` distinguishing two unrelated roots). Where contrast must be made, the language prefers a different segment rather than a length distinction. This preserves the morphological transparency that gemination provides without forcing learners to perceive length as a phonemic feature in root vocabulary.

---

## 8. Orthographic Restrictions

The following restrictions hold absolutely:

1. **No silent letters.** Every written unit corresponds to a pronounced segment.
2. **No letter has multiple unrelated sounds.** Each letter maps to exactly one phoneme category.
3. **`k` is always /k/.**
4. **`g` is always hard /g/.** It never softens to /dʒ/, regardless of the following vowel.
5. **`c` is always /tʃ/.** It never means /k/.
6. **`j` is always /dʒ/.** It is never the IPA glide [j].
7. **`sh` is always /ʃ/** and is a single written unit.
8. **`ts` is always /ts/** and is a single written unit.
9. **There is no /h/.**
10. **There is no /ŋ/.**
11. **The sequence `ng` is always /nɡ/** — two phonemes, never one.
12. **The sequence `ch` is not part of the official alphabet,** because /tʃ/ is written `c`.

---

## 9. Examples

| Written | IPA |
|---|---|
| fac | /fatʃ/ |
| faci | /fatʃi/ |
| facdi | /fatʃdi/ or careful /fatʃ.di/ |
| mov | /mov/ |
| movi | /movi/ |
| movdi | /movdi/ |
| cati | /tʃati/ |
| jata | /dʒata/ |
| shena | /ʃena/ |
| tseno | /tseno/ |
| naga | /naga/ |
| sang | /sang/ |

Note that in `facdi` and `movdi`, the past-tense marker `-d-` of the verb system attaches directly to a consonant-final root. The resulting cluster is pronounced as written; an optional light syllable break may be used for clarity in careful speech, but no vowel is inserted.

Note also that `sang` is /sang/ — two phonemes /n/ + /g/ — never /saŋ/.

---

## 10. Final Summary

The complete official alphabet of the language, in canonical order, with its canonical IPA values:

| Written form | IPA |
|---|---|
| a | /a/ |
| e | /e/ |
| i | /i/ |
| o | /o/ |
| u | /u/ |
| ə | /ə/ |
| p | /p/ |
| b | /b/ |
| t | /t/ |
| d | /d/ |
| k | /k/ |
| g | /g/ |
| m | /m/ |
| n | /n/ |
| f | /f/ |
| v | /v/ |
| s | /s/ |
| z | /z/ |
| sh | /ʃ/ |
| ts | /ts/ |
| c | /tʃ/ |
| j | /dʒ/ |
| l | /l/ |
| r | /r/ |

Six vowels, eighteen consonants, twenty-four written units in total. Every word in the language is built from this inventory and read according to the rules above.
