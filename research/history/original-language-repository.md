# Original language repository: historical provenance

> Primary source: https://github.com/andreabenetton/language

## Chronology

- The repository contains a single initial commit `bacc1a7a9aaaa18596120c6ea2812c927b33b0e3`, authored **8 August 2026 at 18:31:07 UTC**, titled *Initial commit: synthetic language specification*. This is the earliest currently verified **Git commit** for this source, not proof the project began on that date.
- The original specification's phonology, morphology, stress, declension, and vocabulary analyses were already assembled by then; this predates Unisermo's 10 August 2026 formalized migration.
- The Git-tracked source was subsequently preserved in Unisermo under `legacy/original-language/` in commit `c7b9f16f8fa7` on 10 August. Changes to the live Unisermo specification followed in commit `04dad808c53f`.

## Significant original documents

| Source | Design evidence |
| --- | --- |
| `alphabet_and_phonology.md` | Original 24 written units (including schwa, sh, ts, c=/tʃ/, j=/dʒ/), exclusion of /h/ and independent /ŋ/, phonemic contrasts and controlled allophones |
| `speaker_profiles/README.md` and 16 profile files | Language-by-language analysis for English, Mandarin, Japanese, Spanish, Arabic, Bengali, Portuguese, French, Indonesian/Malay, Hindi/Urdu, Russian, Korean, Vietnamese, Turkish, Tamil, and Telugu |
| `vocabulary_design_rules.md` | Risk reduction at the lexical level: avoid frequently confusable minimal pairs, particularly voicing contrasts for some groups |
| `verb_specification.md` | Older six-vowel personal marking system and rationale for compact regular conjugation |
| `noun_case_system.md` | Seven basic + six extended suffixal cases and attachment once at phrase right edge |
| `noun_number_system.md` | Historical plural suffix `-en`, later replaced by optional `wi` |
| `stress.md` | First syllable of lexical root stressed, stable across derivation and inflection; grammatical endings must not be elided |
| `README.md` | Project-wide map of the original grammar, including copula, questions, comparison, demonstratives and numbers |

## Why this matters

The source shows a **two-level international accessibility strategy** already present in the original design: (1) limit the inventory and allow pronunciation variation; (2) constrain frequent vocabulary to avoid contrasts that certain speakers systematically merge. It also preserves **alternative designs that were later abandoned**. This supports a methodological narrative, but the exact chronological sequence of the conversations that led to these documents has not been recovered.

**Caution:** the speaker-profile difficulty rankings and descriptions are expert hypotheses; they are not substitutes for validated typological databases or actual participant studies. The full conversational origin of each decision and any quantitative population/genealogy weighting remain research gaps.

## Primary evidence

- Original source commit: https://github.com/andreabenetton/language/commit/bacc1a7a9aaaa18596120c6ea2812c927b33b0e3
- Original speaker profile index: https://github.com/andreabenetton/language/tree/main/speaker_profiles
- Original alphabet: https://github.com/andreabenetton/language/blob/main/alphabet_and_phonology.md
- Original word-design rules: https://github.com/andreabenetton/language/blob/main/vocabulary_design_rules.md
- Original stress specification: https://github.com/andreabenetton/language/blob/main/stress.md

Paper-related follow-up: map each historical claim to this source commit, track later modifications separately, and verify sources behind cross-language prevalence/accessibility assertions before reporting them as empirical findings.
