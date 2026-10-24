# 10 August 2026: the double redesign of finite tense–aspect marking

**Historical reconstruction:** 24 October 2026. This case is exceptionally traceable because it joins a research study, raw machine-readable comparisons, contemporary conversation-index entries with speaker/date, a rejection of an intermediate design, and an eventual canonical Git commit. This file describes an **engineering/design episode**, not a completed human phonetic experiment.

## Question and successive alternatives

**Initial motivation:** The language's 2025 founding objective, confirmed by the author in October 2026, was to convey more information in less time. By May 2026 the verbal root/person structure had already been debated. The legacy original grammar (preserved in [`language`, 8 August](https://github.com/andreabenetton/language/blob/bacc1a7a9aaaa18596120c6ea2812c927b33b0e3/verb_specification.md)) used 6 distinct final person vowels including schwa, plus single-consonant time/aspect/mode markers; after the 8 August phonological simplification it needed to work with **three person vowels `i/u/a` plus plural `N`**.

**Three competing 10 August arrangements:**

| Model | Structure | Aspect | Time | Status |
| --- | --- | --- | --- | --- |
| A: consonantal aspect | `ROOT + TIME + ASPECT + PERSON + NUMBER` | `Ø/n/b` | `Ø/d/f` | Formally canonized **06:32:48**, later retired |
| B: vowel aspect, after time (control) | `ROOT + TIME + ASPECT + PERSON + NUMBER` | `Ø/e/o` | `Ø/d/f` | **Experimental control** only |
| C: vowel aspect, before time | `ROOT + ASPECT + TIME + PERSON + NUMBER` | `Ø/e/o` | `Ø/d/f` | Confirmed by user **07:17:27**, canonized **07:26:33** |

The time slot stayed constant throughout. The original `m` ability/potential synthetic mode was also retired in A, replaced by analytic servile/modal verbs plus an infinitive; this **separate** change should not be mistaken for a consequence of vowel-aspect testing.

## Primary evidence and absolute UTC sequence

| Time (10 August 2026 UTC) | Record | What it establishes | Evidence quality |
| --- | --- | --- | --- |
| **06:32:48** | [Git `84f3a891`](https://github.com/andreabenetton/unisermo/commit/84f3a891e0abefc3f76c5bd801605c3f52946078), *Close finite verb tense-aspect system* | Official 3×3 tense/aspect, `TIME(Ø/d/f) + ASPECT(Ø/n/b)`, modal `m` retired | **Direct immutable Git**, high |
| **07:13:38** | Dated original-conversation **assistant** index | Reports simulations over **25 roots/1,350 forms and 74 roots/3,996 forms**, comparing consonant clusters, vowel hiatus and canonical collisions | **Contemporaneous conversation-index extract**, full wording unarchived |
| **07:17:27** | Dated original-conversation **user** index | Explicit acceptance of `ROOT + ASPECT + TIME + PERSON + NUMBER`, aspects `Ø/e/o`, times `Ø/d/f`, persons `i/u/a`, plural `n` | **User decision**, contemporaneous timestamp, full verbatim unarchived |
| **07:18:28** | [Git `eff48c08`](https://github.com/andreabenetton/unisermo/commit/eff48c08cdc4c64f60d98f9e04b51baf12dd13d6), *Study vowel aspect TAM phonotactics* | Saves the **experimental** comparative analysis `tam_phonotactics_study.md`, JSON, script; not yet canonical within this study | Direct immutable Git, high |
| **07:26:33** | [Git `13a1d4fe`](https://github.com/andreabenetton/unisermo/commit/13a1d4febe0ae571cc0f63057575fac41994afd7), *Canonize vowel aspect before tense* | Migrates live grammar and machine decisions to vowel `e/o`, **aspect before tense**, with hiatus protection | Direct immutable Git, high |
| **07:27:08** | Dated original-conversation **assistant** index | Reports canonical result and example `dik-e-d-i = dikedi`, explicit noncoalescent hiatus and lexical R vs R+e/o check | Contemporaneous assistant report, corroborated by commit content |

**Causal caution:** The assistant index at 07:13 precedes the 07:18 *research commit*, so the simulation may already have been run before it was committed. Git creation date is not the first moment calculations existed. Conversely, contemporaneous acceptance and subsequent canonical commit strongly support the decision chain but do not establish a complete unabridged debate. The raw 07:17 user statement must not be represented as a literal quotation without full transcript.

## Recovered quantitative comparison: 5,346 generated forms in two non-independent samples

The [contemporaneous study](https://github.com/andreabenetton/unisermo/blob/eff48c08cdc4c64f60d98f9e04b51baf12dd13d6/research/grammar/tam_phonotactics_study.md) generated **54 cells per root**: 3 times × 3 aspects × 3 persons × 2 numbers. Samples were **25 current/confirmed and live roots (1,350 forms)** and a **currentized 74-root Latin/international provisional seed (3,996 forms)**. These samples overlap and must **not** be called 5,346 statistically independent speech observations.

| 25-root / 1,350-form subset | A consonant aspect | B vowel aspect after time | C vowel aspect before time |
| --- | ---: | ---: | ---: |
| Forms containing morphology-created consonant runs of 3+ | **48.0%** | 8.0% | **2.7%** |
| Forms containing consonant runs of 4+ | 5.3% | 0% | 0% |
| Forms containing vowel runs of 2+ | 0.4% | **67.1%** | **24.4%** |
| Canonical orthographic surface collisions inside sample | **0** | **0** | **0** |

| 74-root / 3,996-form provisional seed | A consonant aspect | B vowel aspect after time | C vowel aspect before time |
| --- | ---: | ---: | ---: |
| Consonant runs of 3+ | **52.3%** | 16.2% | **5.4%** |
| Consonant runs of 4+ | 10.8% | 0% | 0% |
| Vowel runs of 2+ | 0.8% | **67.4%** | **26.0%** |
| Canonical orthographic surface collisions inside sample | **0** | **0** | **0** |

These are **computed graphemic/phonotactic run statistics**, not measured milliseconds of pronunciation, L2 articulation error rates, phonemic intelligibility or discourse efficiency. “Zero collisions” is strictly **within the enumerated tested root inventories** under canonical spelling; it does not prove the absence of any future lexical conflict.

**Example (first person):**

| Meaning / configuration | A consonantal `T+A` | C vocalic `A+T` |
| --- | --- | --- |
| `mov`, present progressive | `movni` | `movei` |
| `mov`, past progressive | `movdni` | `movedi` |
| `vid`, past progressive | `viddni` | `videdi` |
| `mov`, future perfect | `movfbi` | `movofi` |

Why the **order** matters: `mov+d+e+i = movdei` (control B) still has a root–time consonant contact and an `e+i` hiatus, whereas `mov+e+d+i = movedi` (C) uses the aspect vowel to separate root-final consonant and tense consonant, and the tense consonant to separate aspect and person vowels. Present aspect forms with zero tense retain hiatus.

## Alternatives, vulnerabilities, and countermeasures

1. **Alternative B rejected:** Putting vowel aspect after tense improved clusters relative to A, but created vowel adjacency in roughly **two-thirds** of forms. C placed aspect before tense, preserving a large phonotactic gain while reducing adjacent vowels.
2. **Mid-vowel identification tradeoff:** The analysis reports source-phoneme attestation estimates for `e` and `o` somewhat below `n` and `b`; they were **not selected because of superior isolated phoneme population coverage**. The benefit was **serial/morphotactic combination**. The pair `e/o` avoids using `i/u/a` already reserved for persons.
3. **Accent risk:** The model investigated an expressly *noncanonical* worst case: aspect `e→i`, `o→u`, followed by equal-vowel coalescence. Forms such as `movei` could then collapse to `movi`, destroying aspect information. In the 25-root sample, the generated diagnosis listed **100 colliding surface strings** and **200 affected paradigmatic bundles** under those assumptions. They do **not** represent observed accent errors or currently legal pronunciations.
4. **Adopted protection:** The canonical [`finite_verb_structure.md`](https://github.com/andreabenetton/unisermo/blob/13a1d4febe0ae571cc0f63057575fac41994afd7/research/grammar/finite_verb_structure.md) requires aspect `e/o` to remain recoverably distinct from persons `i/u/a`; present aspect–person vowel adjacency is **hiatus**, not unmarked fusion.
5. **Future root risk:** A hypothetical lexical pair `R` and `R+e` or `R+o` could duplicate an aspect-marked surface; `mov` vs hypothetical `move` would both permit written `movei`. The source explicitly requires guarding future root introductions against those shadow pairs; no such pair was observed in either sample at study time.
6. **Unmeasured cost:** More hiatus can take longer to articulate and may be misperceived across L1 groups. The study establishes neither faster speaking time nor higher semantic information per second.

## Classification for a future scientific paper

- **Contemporaneous source measurements:** number of forms, run counts, canonical collision counts; reproduced only to the degree documented in archived script and JSON, not independently executed in this note.
- **Historical design decisions:** user-confirmed C at 07:17; Git canonical adoption 07:26; former A **was** canonical for ~54 minutes before being superseded.
- **Hypotheses:** long consonant clusters are harder to pronounce internationally; replacing them with appropriately placed vowels might improve practical speaking flow; forced hiatus and protected `e/o` preserve comprehension.
- **Not demonstrated:** changes in human speech time, meaning-equivalent propositions per minute, generalization to full lexical inventory, human listening accuracy, sample representativeness or information-theoretic efficiency.
- **Critical scientific lesson:** the design responded to a **measured engineering proxy**, tested two alternatives and a control, and **explicitly engineered against a predicted failure**. This is an unusually informative account of a rejected intermediate system and a selected trade-off; it must not be compressed into the statement “the verbal system was simplified on 10 August”.

## Primary resources

- [Consonantal TAM first codified, 06:32](https://github.com/andreabenetton/unisermo/commit/84f3a891e0abefc3f76c5bd801605c3f52946078)
- [Study commit, 07:18](https://github.com/andreabenetton/unisermo/commit/eff48c08cdc4c64f60d98f9e04b51baf12dd13d6), [report](https://github.com/andreabenetton/unisermo/blob/eff48c08cdc4c64f60d98f9e04b51baf12dd13d6/research/grammar/tam_phonotactics_study.md), [machine results](https://github.com/andreabenetton/unisermo/blob/eff48c08cdc4c64f60d98f9e04b51baf12dd13d6/research/grammar/tam_phonotactics_results.json), [analysis source](https://github.com/andreabenetton/unisermo/blob/eff48c08cdc4c64f60d98f9e04b51baf12dd13d6/scripts/analyze_tam_phonotactics.py)
- [Vowel-aspect canonical adoption, 07:26](https://github.com/andreabenetton/unisermo/commit/13a1d4febe0ae571cc0f63057575fac41994afd7)
- [Early May morphological proposals](may-august-morphology-decision-chain.md)
- [Founding objective with author testimony](founding-objective-and-efficiency-measures.md)
