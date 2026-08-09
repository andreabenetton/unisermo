# Person and number marker study

> **Status:** design decision selected after GlottoDelta inventory testing and cross-linguistic phonotactic review. The research branch contains the evidence; once merged, the compact person/number paradigm is canonical for subsequent grammar experiments.

## Decision

Use a three-vowel person system and one nasal number morphophoneme. In the neutral paradigm it is final:

| Person | Singular | Plural |
|---|---:|---:|
| 1st | `i` | `in` |
| 2nd | `u` | `un` |
| 3rd | `a` | `an` |

Interpretation:

- `i` = first person
- `u` = second person
- `a` = third person
- written `n` = plural morphophoneme /N/

The plural marker is best analysed as a nasal **morphophoneme /N/**, written consistently as `n`, with default realization [n]. In neutral person/number forms it is word-final. Place variation `[n ~ ɳ ~ m ~ ŋ ~ ɴ]` is accent-tolerant and never grammatical: it may not create a number or person contrast. A later confirmed referential-specificity suffix may follow /N/, so /N/ can be medial specifically in forms such as `ano` and `ane`; see `optional_gender_study.md`.

This avoids requiring six contrastive person vowels and keeps number orthogonal to person.

## Why `i / u / a`

The two candidate assignments `i/u/a` and `a/u/i` have identical GlottoDelta inventory coverage because they use the same three phonemes. The choice is therefore mnemonic/structural rather than availability-driven.

`i/u/a` is retained because it gives a language-independent internal map: high/front `i` for the speaker/deictic centre, back/high `u` for the addressee, and open `a` for the external third person. The English mnemonic for `a/u/i` is partial and is not strong enough to dominate a global design.


## Interaction with optional referential specificity

A later confirmed design choice adds optional semantic/referential specificity suffixes without introducing grammatical gender:

- neutral / unspecified: zero marking;
- masculine or male-specific reference: `-o`;
- feminine or female-specific reference: `-e`.

These suffixes follow person and number. Thus third person is `a / ao / ae` in the singular and `an / ano / ane` in the plural. The ordering is **person + plural N + optional specificity marker**. This is the sole confirmed context in which the plural /N/ is intentionally medial. The neutral forms remain valid in all contexts, and no agreement is triggered elsewhere in the grammar.

## Inventory result for the three person vowels

Using the broad, disjoint vowel families in `phoneme_targets.json`, the complete `/a i u/` subsystem is available to:

- **98.70%** of the demographic speaker base (`P_attested`)
- **91.19%** of the 2,122 source-attested languages (`L0`)

This is an exceptionally robust grammatical subsystem.

## Why plural `n` should be a place-tolerant /N/

A strictly alveolar `n` is good but leaves unnecessary coverage on the table:

| plural production target | P_attested | L | P0 with `/a i u/` | L0 with `/a i u/` |
|---|---:|---:|---:|---:|
| strict `n` (`n ~ ɳ`) | 93.30% | 85.86% | 92.56% | 78.46% |
| **final nasal /N/, written `n`** | **99.97%** | **97.74%** | **98.67%** | **88.97%** |
| fixed `m` | 99.95% | 96.98% | 98.65% | 88.45% |
| fixed `s` | 97.37% | 71.44% | 96.76% | 64.99% |
| fixed `k` | 94.36% | 92.41% | 93.16% | 84.83% |

The place-tolerant nasal loses only **0.03 percentage points** of demographic P0 compared with the three-vowel person subsystem alone. In practical inventory-familiarity terms, plural marking is almost free.

A fixed `m` is statistically close, but /N/ is preferable because its grammatical identity is *nasality*, not place. That lets speakers preserve the plural feature using the native final-nasal realization their phonology already supports while the orthography remains invariant `n`.

## Why `in / un / an`, not `ni / nu / na`

The universal attraction of CV syllables is real. WALS notes that CV is the syllable type found in every language and that adding a final consonant is an increase in syllable complexity. However, this grammar does not attach person markers to an empty string: they follow lexical/TAM material, which very often ends in a consonant.

Under the current suffix architecture:

- `stem + person vowel + N` gives `...iN / ...uN / ...aN` and introduces **zero new consonant-consonant boundaries**;
- `stem + N + person vowel` gives `...Ni / ...Nu / ...Na` and, on the 74-root Latin/international seed across present plus the five existing consonantal TAM contexts, creates a C+N boundary in **440 of 444 contexts (99.10%)**.

Examples:

- `act + iN` vs `act + Ni`
- `actd + iN` vs `actd + Ni`
- `movf + uN` vs `movf + Nu`

So `VN` accepts one highly privileged final coda but protects the morphology from internal clusters. `NV` keeps an open final syllable only by pushing a cluster/coda problem to the preceding boundary in almost every tested context.

For this morphology, **person first, plural second** is the safer ordering.

## External phonotactic evidence

WALS, Ian Maddieson, *Syllable Structure*, Chapter 12: CV is reported as the syllable type occurring in every language; 61/486 sampled languages are classified as simple, 274 as moderately complex, and 151 as complex. Source: https://wals.info/chapter/12

Martin Krämer & Draga Zec (2020), *Nasal consonants, sonority and syllable phonotactics: the dual nasal hypothesis*, *Phonology* 37(1), DOI 10.1017/S0952675720000032: in their restricted-coda survey, nasals occur in **97.9%** of the word-final coda inventories; **24.7%** of those systems allow nasals as the only word-final consonant class. The authors characterize nasals as the most phonotactically versatile consonants in their cross-linguistic study. Source: https://doi.org/10.1017/S0952675720000032

These typological numbers are evidence about phonotactic class behaviour, not a claim that every individual speaker can produce every final nasal without adaptation.

## Accent policy for plural /N/

Canonical pronunciation is [n]. Accepted place realizations are `[n ~ ɳ ~ m ~ ŋ ~ ɴ]` when they preserve the plural category. They are not separate phonemes and must never distinguish lexical items or grammatical forms.

No deletion of /N/ is accepted, because deletion would neutralize singular/plural. If later speaker testing shows that open-syllable repair is necessary for some populations, a non-contrastive release vowel can be tested separately; it is not part of the canonical morphology at this stage.

## Reproducibility

Run:

```bash
python3 scripts/analyze_person_number.py
python3 scripts/test_person_number.py
```

Machine-readable results are in `research/phonology/person_number_results.json`.
