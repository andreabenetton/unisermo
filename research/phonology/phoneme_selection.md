# Phoneme selection study — working report

> **Status:** decisions 1–6 below were confirmed by the project owner on 2026-08-08. The full phoneme inventory is not yet frozen because the affricate and family/macroarea studies remain open.

## Method

The frozen GlottoDelta baseline contains **2122** deduplicated source languages and **384** demographic-language entries, with a CLDR-derived weighted base of **8,786,359,971**. This base is a weighting universe, not a claim about unique world population.

`P_attested` in this study is deliberately different from the production UI's `P`: it asks whether a demographic language has an attested member of a target realization family. It does **not** require GlottoDelta's green/amber orthography adjudication. `L_family` uses all source-attested languages.

A target is a canonical phoneme plus a narrow acceptable realization family. The families are broad enough to avoid treating, for example, every rhotic as a new sound to learn, but are kept disjoint where possible so coverage is not inflated by double-counting one realization as two target vowels.

## Individual target coverage

| Target | Canonical | P_attested | L_family |
|---|---:|---:|---:|
| a | /a/ | 98.8% | 96.5% |
| e | /e/ | 78.3% | 78.1% |
| i | /i/ | 99.7% | 98.2% |
| o | /o/ | 77.7% | 74.9% |
| u | /u/ | 99.5% | 94.5% |
| schwa | /ə/ | 67.6% | 29.9% |
| p | /p/ | 93.3% | 87.4% |
| b | /b/ | 80.1% | 64.6% |
| t | /t/ | 86.7% | 80.3% |
| d | /d/ | 64.6% | 55.5% |
| k | /k/ | 94.4% | 92.4% |
| g | /ɡ/ | 75.3% | 58.4% |
| m | /m/ | 100.0% | 97.0% |
| n | /n/ | 93.3% | 85.9% |
| f | /f/ | 92.7% | 49.2% |
| v | /v/ | 63.9% | 39.3% |
| s | /s/ | 97.4% | 71.4% |
| z | /z/ | 59.9% | 31.6% |
| sh | /ʃ/ | 89.9% | 41.1% |
| l | /l/ | 92.5% | 73.8% |
| r | /r/ | 96.9% | 75.2% |
| y | /j/ | 98.7% | 91.8% |
| w | /w/ | 91.4% | 86.4% |
| h | /h/ | 72.1% | 60.1% |
| ng | /ŋ/ | 79.1% | 65.2% |

## Inventory candidates

`P0` means zero unfamiliar target categories; `P1`/`P2` allow at most one/two. These are **inventory compatibility proxies**, not comprehension rates.

| Candidate | N | P0 | P1 | P2 | mean missing | L0 |
|---|---:|---:|---:|---:|---:|---:|
| current_simple_21 | 21 | 31.3% | 45.8% | 54.2% | 2.98 | 2.2% |
| no_schwa_20 | 20 | 37.4% | 49.3% | 64.0% | 2.65 | 5.6% |
| latin17 | 17 | 50.0% | 63.9% | 70.2% | 1.79 | 16.7% |
| latin17_yw | 19 | 45.4% | 62.1% | 69.4% | 1.89 | 15.1% |
| lexical22_yw | 22 | 32.9% | 47.8% | 63.5% | 2.75 | 4.8% |
| grammar6 | 6 | 96.1% | 98.2% | 99.8% | 0.06 | 58.3% |
| grammar8 | 8 | 89.9% | 92.4% | 99.5% | 0.18 | 51.1% |
| grammar10 | 10 | 87.0% | 91.2% | 94.7% | 0.28 | 39.5% |

### Result 1 — contrastive schwa is currently a poor trade

Removing contrastive /ə/ raises P0 from **31.3%** to **37.4%**, P2 from **54.2%** to **64.0%**, and reduces weighted mean missing categories from **2.98** to **2.65**. A sixth vowel raises the theoretical choice capacity by only **0.263 bits per vowel choice**.

**Working recommendation:** remove /ə/ as a contrastive vowel; still allow [ə] as an unstressed reduction/allophone where it cannot change lexical or grammatical identity. The written grapheme question therefore disappears unless later evidence reintroduces contrastive schwa.

### Result 2 — /j/ and /w/ deserve serious inclusion

The glide target /j/ reaches **98.7% P_attested / 91.8% L_family**; /w/ reaches **91.4% / 86.4%**. By comparison, strict /v/ is **63.9% / 39.3%** and /z/ **59.9% / 31.6%**. The glides also have a plausible time-efficiency role because they can resolve hiatus without forcing a full extra syllable.

### Result 3 — fragile contrasts should not carry critical grammar

| Contrast | P_attested with both | L with both |
|---|---:|---:|
| p / b | 73.6% | 56.0% |
| t / d | 61.2% | 51.8% |
| k / g | 73.4% | 54.9% |
| f / v | 63.4% | 30.9% |
| s / z | 59.9% | 31.1% |
| s / sh | 88.0% | 35.0% |
| l / r | 90.1% | 59.8% |
| e / i | 78.2% | 77.3% |
| o / u | 77.6% | 71.2% |
| y / w | 91.3% | 83.2% |

Voicing and fricative contrasts are valuable for preserving international roots, but their joint availability is materially lower than the strongest targets. This supports a split policy: robust contrasts for grammar; additional **soft lexical contrasts** where the protected lexicon forbids dangerous minimal pairs.

### Accent-tolerant production experiment

If lexical accents are allowed to merge selected fragile contrasts (b→p, d→t, g→k, v→f/w, z→s, ʃ→s, l↔r) **without permitting those mergers to create protected minimal pairs**, the 22-target lexical candidate reaches **57.7% production-P0**, **68.4% P1**, and **89.0% P2**, with weighted mean missing categories **1.18**. This is a production-accessibility model only; it does not prove that listeners can perceive every canonical contrast.

## Grammar core search

The search fixes /a i u/ and asks which additional target families maximize strict P0, then P1/P2, for total inventories of 6–10 categories. This is a statistical bound, not an automatic design recommendation.

| N | Best strict target set | P0 | P1 | P2 |
|---:|---|---:|---:|---:|
| 6 | a i u m s y | 96.1% | 98.2% | 99.8% |
| 7 | a i u m s r y | 93.8% | 98.0% | 99.3% |
| 8 | a i u p k m s y | 89.9% | 92.4% | 99.5% |
| 9 | a i u p k m n s y | 89.0% | 91.5% | 94.9% |
| 10 | a i u p k m n s r y | 87.0% | 91.2% | 94.7% |

The important design signal is not the exact winning set; it is that **grammar can be built from a much smaller, more globally robust contrast inventory than the lexicon**. A three-vowel grammatical subsystem /a i u/ is especially attractive, while the lexicon can retain /e o/ for Latin/international compatibility.

## Latin/international root pressure — provisional seed

The current seed has **74** roots. It is intentionally small and must be expanded before final lexical decisions.

Most demanded target categories in the seed:

`r` 29, `e` 24, `k` 21, `i` 20, `t` 19, `n` 19, `a` 16, `o` 16, `m` 16, `d` 14, `v` 14, `l` 10, `s` 10, `u` 8, `p` 8.

| Candidate | Exact segment coverage | Mean missing types/root | Main pressure |
|---|---:|---:|---|
| current_simple_21 | 97.3% | 0.03 | w:1, h:1 |
| no_schwa_20 | 97.3% | 0.03 | w:1, h:1 |
| latin17 | 78.4% | 0.22 | v:14, w:1, h:1 |
| latin17_yw | 79.7% | 0.20 | v:14, h:1 |
| lexical22_yw | 98.6% | 0.01 | h:1 |

The seed should be read as a **pressure detector**. In particular it quantifies how often dropping /v/, /g/, /d/, /h/ or /w/ forces adaptation of highly recognizable stems; it does not yet assign frequency weights to those stems.

## Complex segments /ts tʃ dʒ/ — resolved

The dedicated `affricate_study.md` resolves all three as **non-independent phonemes**: `/t+s/ → [ts]`, `/t+j/ → [tj ~ tʃ]`, and `/d+j/ → [dj ~ dʒ]`. Transparent sequence pronunciations remain valid. This exploits retained `/j/`, preserves useful surface affricates, and avoids counting an affricate as a free one-unit timing shortcut.

Whole-base component familiarity measured in that study is **86.3% P / 63.1% L** for `/t+s/`, **86.2% / 74.2%** for `/t+j/`, and **64.0% / 51.6%** for `/d+j/`. Direct affricate evidence is reported separately on the curated-profile denominator.

## Confirmed design constraints — 2026-08-08

1. **Schwa:** drop contrastive /ə/; allow [ə] only as a non-contrastive reduction/allophone.
2. **Vowel architecture:** lexical /a e i o u/; reserve /a i u/ as the safest pool for grammar-critical endings/particles where practical.
3. **Glides:** retain canonical /j/; carry /w/ as the strong default lexical candidate pending the final inventory-wide check. Choose spelling later, separately from IPA.
4. **Rhotic policy:** retain one /r/ category but allow a broad rhotic realization family; do not prescribe trill vs tap vs approximant vs uvular realization.
5. **Soft lexical contrasts:** continue evaluating /b d ɡ v z ʃ/ as canonical lexical contrasts, but prohibit grammar-critical distinctions and protected minimal pairs that depend only on a fragile merger pair.
6. **Affricates:** no independent /ts tʃ dʒ/ phonemes. Use /t+s/, /t+j/, /d+j/ with optional fast/coalescent [ts], [tʃ], [dʒ] realizations; transparent sequence pronunciations remain valid.

## Still required before final phoneme freeze

The remaining major quantitative dimension before the full inventory freeze is **Glottolog family/macroarea dispersion (F)**, because the normalized local snapshot does not contain genealogy/area tables. The complex-segment study for `/ts tʃ dʒ/` is complete and no longer blocks the inventory.

These confirmed constraints are recorded in the local repository, but they do not alter GlottoDelta's production L/P semantics. Synchronization into the separate auxiliary-language specification remains a distinct step.
