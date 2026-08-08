# Person-marker vowel study

> **Status:** research recommendation, not yet project-owner-confirmed. The six previously confirmed phoneme constraints are already on local `main`; this study remains on `phoneme-study` until confirmed.

## Question

Compare the two maximally simple mappings proposed for singular person marking:

| Person | Option A | Option B |
|---|---:|---:|
| 1st | `i` | `a` |
| 2nd | `u` | `u` |
| 3rd | `a` | `i` |

Both options use the same robust three-vowel subsystem `/a i u/`, so GlottoDelta inventory coverage and segment discriminability are identical. The decision therefore depends on learnability/iconicity rather than phoneme availability.

## Recommendation: Option A — `i / u / a`

Use:

- 1st person: `i`
- 2nd person: `u`
- 3rd person: `a`

### Why

1. **Deictic iconicity gives `i` and `a` a non-English rationale.** Cross-linguistic work on demonstratives reports a recurrent tendency for high/front vowels, especially `/i/`, to mark proximal reference and low/back vowels, especially `/a/`, to mark distal reference. The speaker is the deictic center; third person is outside the speaker–addressee pair. This makes `i → 1st` and `a → 3rd` a plausible iconic mapping rather than an arbitrary mnemonic.
2. **`u → 2nd` is strong in both proposals.** It has useful mnemonic support in English `you` and many familiar `tu/du/u`-type second-person forms, while remaining maximally separated from `/i/` and `/a/` in vowel space.
3. **The English advantage of `a/u/i` is weaker than it first appears.** Spoken English `I` is a diphthong rather than `/a/`, while written `I` directly supports `i → 1st`; `/i/ → 3rd` fits `he/she` but not the full English third-person set (`it/they`). The project goal is global learnability, so this partial English mnemonic should not override a broader deictic pattern.
4. **The mapping forms an interpretable vowel triangle:** front/high `i` = speaker/proximal, back/high `u` = addressee, low/open `a` = external/third. This gives the system an internal explanation that can be taught without reference to any one source language.

### Evidence note

Relevant sources for the deictic sound-symbolism rationale:

- Hartmut Traunmüller, *Sound symbolism in deictic words* (2000), Stockholm University. The study examines demonstratives and first/second-person pronouns and reports systematic sound-symbolic tendencies.
- Sonja Dahlgren & Seppo Kittilä, *A phonological typology of demonstratives: a study in iconicity* (Linguistics, 2026). The typology reports front/high vowels as common in proximal demonstratives and back/low vowels as common in distal demonstratives, continuing earlier findings by Woodworth and Traunmüller.

This evidence is a design prior, not proof that grammatical person itself universally maps to these vowels.

## Plural marker — next decision

The proposed architecture is one plural consonant shared by all persons:

- 1SG `i`
- 2SG `u`
- 3SG `a`
- 1PL `i + C`
- 2PL `u + C`
- 3PL `a + C`

`n` is the leading candidate for `C`, but it is **not confirmed yet**.

Why `n` leads:

- nasals are cross-linguistically unusually permissive in codas;
- restricted word-final coda systems frequently preserve a nasal even when they exclude obstruents;
- an alveolar nasal is a plausible written/canonical target while allowing a deliberately broad final-nasal accent realization if testing supports it;
- it keeps number orthogonal to person: one invariant plural feature appended to all three vowels.

Before confirmation, test two implementations:

1. **strict `/n/`**: canonical and required alveolar nasal;
2. **final nasal category `/N/` written `n`**: canonical `[n]`, but accent-tolerant `[n ~ m ~ ŋ ~ ɴ]` where no grammatical contrast is lost.

The second may be substantially more universal and compatible with languages whose only native final consonant is a placeless or assimilating nasal.
