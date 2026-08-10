# Alphabet and Phonology

A formal specification of the alphabet and sound system of the synthetic language. This document defines the official written units, their canonical IPA values, acceptable pronunciation variants, **accentual and coalescent realizations**, accent-tolerant mergers, and the orthographic restrictions that preserve transparent reading and writing.

This specification is designed to interoperate with the person/number system in which `i`, `u`, and `a` mark first, second, and third person, plural is marked by the nasal morphophoneme `/N/` written `n`, and optional referential specificity may be marked by `-o` or `-e`.

---

## 1. Design Principles

The alphabet and phonological inventory are governed by eight core principles:

1. **One-to-one canonical mapping.** Each official letter corresponds to exactly one underlying phoneme, and each underlying phoneme has one official letter. Surface coalescence never changes the underlying parse.
2. **Compact but expressive.** The inventory is kept small enough to learn quickly, but large enough to preserve recognizable Latin and international roots.
3. **Population-aware and genealogy-aware.** Phonemes are favored when they are familiar to large speaker populations and are also well distributed across major independent language families.
4. **No weak independent consonants.** Sounds that are frequently lost or absent across large populations, especially `/h/`, are not used as independent phonemes.
5. **No unnecessary rare contrasts.** A sound may occur as an accentual or coalescent realization without receiving independent phoneme status.
6. **Controlled accent tolerance.** Predictable accent-driven substitutions are accepted where meaning remains recoverable. Grammar-critical contrasts must use the most robust part of the inventory.
7. **Protected lexical contrasts.** Some useful Latin-root contrasts are retained canonically even when particular accents may merge them. The lexicon should avoid minimal pairs that would become ambiguous under the explicitly accepted soft mergers.
8. **Root-by-root source adaptation.** Latin and international source spellings are not transliterated mechanically when their historical letters have divergent modern pronunciations. The canonical GlottoDelta form is chosen root by root to maximize international recognizability, phonological accessibility, and lexical distinctness.

The distinction between **source spelling**, **canonical GlottoDelta phoneme**, and **accepted surface realization** is fundamental. A source letter need not survive in the canonical spelling, and a pronunciation may be correct even when several adjacent canonical phonemes are realized as one coalesced sound.

---

## 2. Official Alphabet

The language has **21 official written units**: **5 vowels** and **16 consonants/glides**.

**Vowels:**

```text
a  e  i  o  u
```

**Consonants and glides:**

```text
p  b  t  d  k  g
m  n
f  v  s  z
l  r
j  w
```

Important notes:

- `j` represents the glide **/j/**, approximately English `y` in *yes* or Italian `i` in *ieri* when consonantal.
- `w` represents the glide **/w/**.
- `k` always represents **/k/**.
- `g` always represents hard **/g/**.
- There is no letter `h` and no phoneme `/h/`.
- There is no independent phoneme `/ŋ/`.
- There is no independent phoneme `/ɲ/`.
- There is no independent phoneme `/ʃ/` and no official unit `sh`.
- `/ts/`, `/tʃ/`, and `/dʒ/` are not independent phonemes. They may arise from the transparent sequences `ts`, `tj`, and `dj`.
- The sequence `gn` is underlyingly `/g+n/`; `[ɲ]` is an accepted coalescent realization.

---

## 3. Vowel Inventory

| Letter | Canonical IPA | Ordinary accepted variants | Accentual/non-contrastive possibilities | Constraint |
|---|---|---|---|---|
| `a` | /a/ | [a], [ä], [ɑ], [ɐ] | light centralization toward [ɐ] | Must remain recoverable as the low vowel, especially when grammar-critical. |
| `e` | /e/ | [e], [ɛ] | moderate opening or accentual raising where identity remains recoverable | In the optional specificity suffix `-e`, accents without stable mid vowels may raise it toward [i]. |
| `i` | /i/ | [i], [ɪ], [ɨ] | slight centralization | As a grammar-critical first-person marker it must remain distinct from `u` and `a`. |
| `o` | /o/ | [o], [ɔ] | moderate opening or accentual raising where identity remains recoverable | In the optional specificity suffix `-o`, accents without stable mid vowels may raise it toward [u]. |
| `u` | /u/ | [u], [ʊ], [ɯ] | slight loss of rounding | As a grammar-critical second-person marker it must remain distinct from `i` and `a`. |

### 3.1 Person, number, and optional referential specificity

The grammar-critical person vowels are:

| Person | Singular | Plural |
|---|---|---|
| 1st | `i` | `in` |
| 2nd | `u` | `un` |
| 3rd | `a` | `an` |

The plural `n` represents the nasal morphophoneme **/N/**. Its default realization is `[n]`, but place of articulation is accent-tolerant; see §6.3.

Optional referential specificity is zero-marked by default:

- neutral / unspecified: zero marking;
- masculine or male-specific: `-o`;
- feminine or female-specific: `-e`.

For third person:

- `a` = neutral singular
- `ao` = masculine singular
- `ae` = feminine singular
- `an` = neutral plural
- `ano` = masculine plural
- `ane` = feminine plural

The morphological order is:

```text
person + plural N + optional specificity marker
```

The suffixes `-e` and `-o` are semantic/referential markers, not grammatical gender classes, and they never trigger obligatory agreement.

In accents without stable mid vowels, canonical `-e` may approach `[i]` and canonical `-o` may approach `[u]`. The front/back distinction must remain recoverable whenever specificity is intentionally expressed. If the two would collapse, the neutral form or a lexical paraphrase remains available.

---

## 4. Consonant and Glide Inventory

The table distinguishes ordinary phonetic variation from **soft accent mergers**. A soft merger is permitted only where the word remains recoverable and no protected lexical or grammatical contrast is destroyed.

| Letter | Canonical IPA | Ordinary accepted variants | Soft accent possibilities | Notes |
|---|---|---|---|---|
| `p` | /p/ | [p], [pʰ] | — | Voiceless bilabial stop. |
| `b` | /b/ | [b], partially devoiced [b̥] | [p] | Canonically distinct from `p`, but the lexicon should tolerate `b→p` accents where possible. |
| `t` | /t/ | [t], [t̪], [tʰ] | — | Dental or alveolar realization is free. |
| `d` | /d/ | [d], [d̪], partially devoiced [d̥] | [t] | Canonically distinct from `t`; `d→t` may occur in an accent where no protected contrast is lost. |
| `k` | /k/ | [k], [kʰ] | — | Always velar; it never has a separate soft-c value. |
| `g` | /g/ | [g], [ɡ], partially devoiced [g̊] | [k] | Always hard canonically. `g→k` is an accepted soft accent merger where recoverable. |
| `m` | /m/ | [m] | — | Bilabial nasal. |
| `n` | /n/ | [n], [n̪] | place assimilation before nearby consonants | `[ŋ]` may occur before velars without becoming a phoneme. The grammatical `/N/` has broader tolerance; see §6.3. |
| `f` | /f/ | [f] | — | Voiceless labial fricative. |
| `v` | /v/ | [v], [ʋ], [β] | [f] or [w] in accents that merge the contrast | `v` is retained for Latin/international root recognizability. Prefer [v~ʋ~β] when possible. |
| `s` | /s/ | [s] | — | `[ʃ]` may arise from coalescence with following `j`; see §6.2. |
| `z` | /z/ | [z], partially devoiced [z̥] | [s] | `z` is retained canonically, while `z→s` is an accepted soft merger where unambiguous. |
| `l` | /l/ | [l], [ɫ] | — | Lateral approximant. |
| `r` | /r/ | [r], [ɾ], [ɹ], [ʁ] | — | One broad rhotic category; no particular rhotic articulation is privileged. |
| `j` | /j/ | [j] | — | Palatal glide. It is **not** /dʒ/. |
| `w` | /w/ | [w], [u̯] | — | Labial-velar glide. Canonically distinct from both `v` and vowel `u`. |

---

## 5. Rationale for Major Choices

### 5.1 Five-vowel system

The canonical vowel system is `/a e i o u/`. These five vowels provide the complete vowel inventory for lexical and grammatical forms.

The grammar reserves the highly robust `/i u a/` subsystem for person marking. Mid vowels `/e o/` remain useful for lexical transparency and for optional referential-specificity suffixes.

### 5.2 No independent /h/

`/h/` is excluded as an independent phoneme. It is weak, frequently absent, and often lost in speech across major populations. Removing it costs little Latin-root information compared with the perceptual instability it introduces.

There is therefore no official `h` letter.

### 5.3 No independent /ŋ/

`/ŋ/` is not an independent lexical phoneme. A velar nasal may nevertheless appear in two legitimate ways:

1. **phonetic place assimilation**, for example underlying `/n+g/` or `/n+k/` realized approximately `[ŋg]` or `[ŋk]`;
2. **the plural morphophoneme `/N/`**, whose place is intentionally accent-tolerant.

The spelling always preserves the underlying structure. Thus `ng` means `/n+g/`, not a separate `/ŋ/` letter or phoneme.

### 5.4 `j` and `w` are canonical glides

`j` is /j/ and `w` is /w/. Both are retained because they are broadly useful for international roots and for transparent phonological sequences.

This also allows common surface sounds to arise without enlarging the phoneme inventory: `tj` and `dj` can coalesce to `[tʃ]` and `[dʒ]`.

### 5.5 Affricates are sequences, not phonemes

The language has no independent `/ts tʃ dʒ/` phonemes.

Canonical structure and accepted fluent realizations are:

```text
ts = /t+s/  → [ts]
tj = /t+j/  → [tj ~ tʃ]
dj = /d+j/  → [dj ~ dʒ]
```

The transparent sequence pronunciation is always valid. Coalescence is optional and carries no independent lexical or grammatical contrast.

### 5.6 No independent /ʃ/

`/ʃ/` is not part of the canonical inventory. Where speakers naturally palatalize a sequence `/s+j/`, the surface realization may approach or become `[ʃ]`:

```text
sj = /s+j/ → [sj ~ ʃ]
```

This gives speakers access to the familiar sound without requiring every speaker to maintain a separate `/s/ : /ʃ/` contrast.

### 5.7 No independent /ɲ/: `gn` remains /g+n/

The Italian-like palatal nasal `[ɲ]` is accepted as a **coalescent realization**, not as a phoneme.

Canonical structure:

```text
gn = /g+n/
```

Accepted realizations include:

```text
[gn]  careful/transparent
[ɲ]   coalescent
```

Therefore roots such as `magn-`, `sign-`, `dign-`, or `kogn-` can preserve a recognizable `gn` structure without requiring `/ɲ/` from all speakers.

No word may contrast solely by `/gn/` versus an independent `/ɲ/`, because independent `/ɲ/` does not exist.

### 5.8 Soft voiced contrasts are retained for root recognizability

`b d g v z` are retained canonically because removing them would substantially deform Latin and international roots. However, their voicing/frication contrasts are not suitable for fragile grammar-critical oppositions.

The accepted directional accent mergers are:

```text
b → p
d → t
g → k
z → s
v → f or w
```

These are pronunciation tolerances, not spelling changes. Canonical spelling remains stable.

The lexicon should avoid basic minimal pairs that differ only by one of these soft contrasts when the accepted merger would make the pair ambiguous.

### 5.9 Latin-source `c` is adapted root by root

The letter `c` is **not** part of the official GlottoDelta alphabet and has no fixed GlottoDelta phonemic value. A `c` found in a Latin or international source form is therefore treated as **source orthography**, not as an instruction for pronunciation.

There is **no universal conversion rule** such as “Latin `c` always becomes `k`”, “`c` before `e/i` always becomes `s`”, or “soft `c` always becomes `tj`”. Instead, each candidate root is evaluated individually. Where a source `c` corresponds to divergent international pronunciations, the canonical GlottoDelta root may represent it with one of the existing official sequences:

```text
k   = /k/
s   = /s/
j   = /j/
tj  = /t+j/ -> [tj ~ tʃ]
```

The choice is made by comparing at least four criteria:

1. **International recognizability:** which form best preserves recognition across the major descendant and international vocabulary traditions relevant to that root.
2. **Population accessibility:** which form uses phonemes and contrasts that are robust for the largest relevant speaker populations.
3. **Genealogical dispersion:** which form avoids imposing a difficult contrast on major independent language families.
4. **Lexical distinctness:** which form avoids collisions or dangerous near-collisions with other GlottoDelta roots, including under accepted accent mergers.

Thus a source root such as `CENT-` is not automatically assigned a form by spelling rule. Candidate adaptations such as `kent-`, `sent-`, `jent-`, and `tjent-` may be compared, and the lexicon selects the form that gives the best overall balance. The same procedure applies independently to `CIV-`, `CERT-`, `CIRC-`, and other roots containing historical `c`.

This is a **lexical adaptation rule**, not a pronunciation exception. Once a GlottoDelta root has been selected and entered into the lexicon, its canonical spelling follows the ordinary one-letter/one-phoneme rules of this document. For example, a root selected with `tj` is underlyingly `/t+j/`; `[tʃ]` is merely an accepted coalescent realization.

### 5.10 Source /dʒ/ and recurrent divergent Romance outcomes

The canonical letter `j` always represents the palatal glide **/j/**. It **never** has the phonemic value /dʒ/, even when a source language writes a similar sound with `j`, `g`, or another letter.

GlottoDelta does not introduce a separate /dʒ/ phoneme. When a Latin-derived, Romance, or international candidate root contains /dʒ/ in one important source language, the form is therefore **not transliterated mechanically**. The lexicon compares the wider Latin and international root family and chooses the most useful canonical adaptation. Possible outcomes include:

```text
dj  = /d+j/ -> [dj ~ dʒ]
j   = /j/
g   = /g/
z   = /z/
or an etymologically/internationally motivated form that avoids /dʒ/ altogether
```

`dj` is the structurally faithful choice when preserving the affricate-like character materially improves recognizability. The spelling remains transparently two phonemes `/d+j/`, while speakers may realize the sequence coalescently as `[dʒ]`.

`j` may be selected **root by root** when the glide gives a simpler and more internationally recognizable form, or when an affricated realization is not important to identifying the lexical family. In that case the canonical phoneme is genuinely /j/: pronouncing it as /dʒ/ is not required by the spelling.

`g` may be selected when the Latin or broader international family is more transparently recognized with a hard velar form. `z` is also available when a sibilant adaptation gives the best cross-linguistic compromise, although it is not an automatic substitute for /dʒ/. A root may instead be based on an etymological or international form in which the /dʒ/ problem does not arise at all.

For example, a lexical family in the area of `GEN-/GENT-` may require comparison among candidates such as `gent-`, `jent-`, `djent-`, or a sibilant adaptation rather than simply copying the pronunciation of one modern Romance language. The same principle applies to other roots whose Romance descendants diverge between velar, palatal, affricate, glide, or sibilant outcomes.

This situation is expected to occur **frequently during root construction**, because the purpose of GlottoDelta is not to reproduce the phonology of any single Neo-Latin language. Historical palatalization and later sound changes have often caused related Latin-derived words to diverge substantially across Romance and international vocabularies. Therefore the treatment of /dʒ/ is part of a **general recurrent lexical-adaptation procedure**, alongside the treatment of source `c`, rather than a special exception for a handful of words.

For each affected root, the decision must consider at least international recognizability, population accessibility, genealogical dispersion, preservation of the Latin/international lexical family, phonotactic simplicity, and lexical distinctness under accepted accent mergers. Once a canonical GlottoDelta root is selected, its spelling is fixed and ordinary GlottoDelta pronunciation rules apply.

---

## 6. Accentual and Coalescent Realizations

This section is normative. These realizations are **accepted pronunciations of canonical forms**, not additional phonemes.

### 6.1 Accentual realizations of individual phonemes

Common accepted accent behavior includes:

- `b /b/ → [p]`
- `d /d/ → [t]`
- `g /g/ → [k]`
- `z /z/ → [s]`
- `v /v/ → [ʋ ~ β]`, and in merger accents possibly `[f]` or `[w]`
- `r /r/ → [r ~ ɾ ~ ɹ ~ ʁ]`

These variants must not be used to create grammatical distinctions. Grammar-critical contrasts are designed around more robust categories.

### 6.2 Coalescent realizations of sequences

Adjacent canonical phonemes may fuse in fluent speech:

| Written sequence | Underlying | Transparent realization | Accepted coalescent realization |
|---|---|---|---|
| `ts` | /t+s/ | [ts] as a close sequence | [t͡s] |
| `tj` | /t+j/ | [tj] | [tʃ], [t͡ʃ] |
| `dj` | /d+j/ | [dj] | [dʒ], [d͡ʒ] |
| `sj` | /s+j/ | [sj] | [ʃ] |
| `gn` | /g+n/ | [gn] | [ɲ] |
| `nk` | /n+k/ | [nk] | [ŋk] |
| `ng` | /n+g/ | [ng] | [ŋg] |

The written sequence always reveals the canonical phonological structure. A coalesced pronunciation never creates a new letter, new phoneme, or new grammatical category.

### 6.3 Accentual realization of plural /N/

Plural is written `n` after the person vowel but analyzed as the nasal morphophoneme `/N/`.

Canonical realization:

```text
/N/ → [n]
```

Accepted accent realizations:

```text
[n ~ ɳ ~ m ~ ŋ ~ ɴ]
```

Place of articulation is non-contrastive. `/N/` may not be deleted, because deletion would erase the singular/plural distinction.

In neutral plural forms it is normally final (`in`, `un`, `an`). It may be medial specifically before the optional specificity suffixes, as in `ano` and `ane`.

### 6.4 What accent tolerance does not permit

Accent tolerance is broad, but not unlimited:

- no required grammatical distinction may disappear;
- `/N/` may change place but may not disappear;
- `i`, `u`, and `a` must remain recoverably distinct when they mark person;
- optional `-e` and `-o` may raise toward `[i]` and `[u]`, but may not collapse with each other when specificity is intended;
- coalescence may simplify a sequence phonetically, but spelling and underlying analysis remain unchanged;
- the canonical lexicon should avoid protected minimal pairs that become indistinguishable under explicitly accepted soft mergers.

---

## 7. Double Consonants

When morphology brings two identical consonants into contact, they are written double. A long or geminated pronunciation is preferred where natural, but speakers who do not use contrastive consonant length may realize the sequence with a clear boundary or ordinary-length consonant when meaning remains recoverable.

Example from the root `vid` (“to see”):

- `vid` = bare root
- `vidi` = first-person present form
- `viddi` = form in which a `d`-initial grammatical suffix follows a `d`-final root

A careful realization of `viddi` may contain `[dː]`; an accent that does not naturally geminate may preserve the morphological sequence without relying on consonant length as a lexical contrast.

The language avoids unrelated lexical minimal pairs distinguished only by consonant length.

---

## 8. Orthographic Restrictions

The following restrictions are canonical:

1. **No silent letters.** Every official letter represents an underlying phoneme.
2. **One official letter per canonical phoneme.** Surface coalescence does not alter spelling.
3. `k` is always /k/. The letter `c` is not part of the official alphabet and has no automatic GlottoDelta pronunciation. Source-form `c` is adapted **root by root** to `k`, `s`, `j`, or `tj` according to §5.9.
4. Once a root has been canonically selected, its spelling is fixed; the root-by-root adaptation rule does not create contextual pronunciation rules inside GlottoDelta.
5. `g` is always hard /g/ canonically.
6. `j` is always the glide /j/; it is never an independent /dʒ/ phoneme. A source or Romance realization /dʒ/ is handled **root by root** according to §5.10; possible canonical outcomes include `dj`, `j`, `g`, `z`, or an etymologically/internationally motivated form that avoids /dʒ/.
7. `w` is always /w/.
8. There is no `h` and no independent /h/.
9. There is no independent /ŋ/.
10. There is no independent /ɲ/.
11. There is no official `sh` phoneme/unit and no independent /ʃ/.
12. `ts` is always parsed as `t+s`, never as a separate phoneme.
13. `tj` is always parsed as `t+j`, even when pronounced [tʃ].
14. `dj` is always parsed as `d+j`, even when pronounced [dʒ].
15. `gn` is always parsed as `g+n`, even when pronounced [ɲ].
16. `ng` is always parsed as `n+g`; velar assimilation does not create a separate `/ŋ/` phoneme.
17. Accepted accent mergers affect pronunciation only; they do not change canonical spelling.

---

## 9. Examples

| Written | Canonical analysis | Accepted realizations |
|---|---|---|
| `fak` | /fak/ | [fak] |
| `movi` | /movi/ | [movi], accentually [moʋi], and where unambiguous [mofi] or [mowi] |
| `vidi` | /vidi/ | [vidi], accentually [viti] where recoverable |
| `tsena` | /t+s+e+n+a/ | [tsena], [t͡sena] |
| `tjana` | /t+j+a+n+a/ | [tjana], [tʃana] |
| `djana` | /d+j+a+n+a/ | [djana], [dʒana] |
| `sjena` | /s+j+e+n+a/ | [sjena], [ʃena] |
| `magna` | /m+a+g+n+a/ | [magna], [maɲa] |
| `signa` | /s+i+g+n+a/ | [signa], [siɲa] |
| `nka` | /n+k+a/ | [nka], [ŋka] |
| `nga` | /n+g+a/ | [nga], [ŋga] |
| `an` | /a+N/ | [an], accentually [aŋ], [am], [aɳ], [aɴ] |
| `ano` | /a+N+o/ | default [ano], with accent-tolerant nasal place and possible `o→[u]` where specificity remains recoverable |
| `ane` | /a+N+e/ | default [ane], with accent-tolerant nasal place and possible `e→[i]` where specificity remains recoverable |

The examples distinguish **canonical analysis** from **surface realization**. The written form always preserves the canonical sequence even when fluent speech coalesces it.

---

## 10. Final Summary

The official canonical inventory contains **21 phonemes**.

### Vowels

| Written | IPA |
|---|---|
| `a` | /a/ |
| `e` | /e/ |
| `i` | /i/ |
| `o` | /o/ |
| `u` | /u/ |

### Consonants and glides

| Written | IPA |
|---|---|
| `p` | /p/ |
| `b` | /b/ |
| `t` | /t/ |
| `d` | /d/ |
| `k` | /k/ |
| `g` | /g/ |
| `m` | /m/ |
| `n` | /n/ |
| `f` | /f/ |
| `v` | /v/ |
| `s` | /s/ |
| `z` | /z/ |
| `l` | /l/ |
| `r` | /r/ |
| `j` | /j/ |
| `w` | /w/ |

### Not independent phonemes

The following sounds may occur phonetically but are **not independent canonical phonemes**:

| Surface sound | Canonical source |
|---|---|
| `[ŋ]` | nasal assimilation or realization of grammatical `/N/` |
| `[ɲ]` | coalescent realization of `gn = /g+n/` |
| `[ʃ]` | coalescent realization of `sj = /s+j/` |
| `[ts]` | close/coalescent realization of `ts = /t+s/` |
| `[tʃ]` | coalescent realization of `tj = /t+j/` |
| `[dʒ]` | coalescent realization of `dj = /d+j/` |

Thus the language keeps a compact canonical inventory while preserving useful Latin/international root structure and allowing a broad range of natural accents.
