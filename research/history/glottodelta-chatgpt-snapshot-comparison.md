> **Superseded coverage notice (24 October 2026):** This report verified **10** of the 39 ChatGPT snapshots. The [new all-39 audit](glottodelta-39-snapshot-audit.md) independently materializes every raw file, supplies 39 Git blob hashes, and identifies **earlier** source introductions: audio by 12:25, Georgian 33-row table by 12:38, and 40 profiles by 13:04. Read this ten-checkpoint document as an intermediate research result, not the latest complete inventory.

# GlottoDelta original ChatGPT snapshot comparison

Research audit dated 24 October 2026. Ten of the 39 original July 27 ChatGPT HTML snapshots were independently materialized from the user's file Library, parsed for source constants, and hashed as Git blobs. This is an artifact-level comparison, not the complete transcript or browser functional test.

## Source-corpus invariant

All 10 audited snapshots contain 111 IPA symbol keys and 49,600 phoneme-language attestation rows, including 2,176 distinct nonempty Glottocodes. The six tracked counts are unchanged: /ə/ 533, /h/ 1,258, /ŋ/ 1,424, /j/ 1,993, /w/ 1,883, and /ʃ/ 782. These counts were present in the first recovered snapshot at 05:15:31 UTC, before any of the later inspected UI revisions.

## Evolution verified at ten checkpoints

| Time UTC | Filename | Code evidence |
| --- | --- | --- |
| 05:15:31 | ipa_language_counts.html | Original DATA, 111 symbols; no SPEAKER_ESTIMATES constant |
| 05:58:15 | ipa_language_counts_demographics_corrected.html | 384 speaker estimates added |
| 09:08:25 | ipa_language_counts_phoneme_variants.html | languageSymbolState introduced by this checkpoint |
| 09:29:02 | ipa_language_counts_verified_mappings.html | Verification-oriented mapping source |
| 09:48:31 | ipa_language_counts_georgian_complete.html | Georgian coverage discussed; no later GEORGIAN_ALPHABET_ROWS constant yet |
| 13:04:50 | ipa_language_counts_language_verified.html | 33-letter Georgian constant, 40 verified-profile entries, 112 audio map entries |
| 13:53:21 | ipa_language_counts_official_ipa_2026.html | Official IPA version in revised UI |
| 15:37:24 | ipa_language_counts_verified_population.html | populationEligible function explicitly present |
| 16:24:26 | ipa_language_counts_priority_features.html | differencesOnly and renderComparison present |
| 17:08:22 | ipa_language_counts_scroll_quality.html | Final ChatGPT file, Git blob eab1b5ed7b5463a52202a6dd9bcd13a811af85c3 |

All ten checkpoints retain the original DATA symbol counts. Beginning with the 05:58 checkpoint, the sum of the 384 speaker estimates is 8,786,359,971. This is a speaker-exposure proxy, **not a count of unique people**. Introduction timestamps above are upper bounds: 29 intermediate snapshots have not been analyzed at the same code level.

## Reconciled denominators

The original HTML yields 2,176 distinct nonempty Glottocodes plus one unnamed-code identity. The 8 August phoneme study instead reports **2,122 distinct source languages**. These are different deduplication rules, not necessarily different datasets. The archived study script `scripts/analyze_phoneme_inventory.py` uses the ISO code as primary identity, and otherwise falls back to Glottocode or name (for missing, `mis`, or `und` ISO codes). Applying that exact ISO-first rule to the *first* 05:15 HTML produces **2,122** keys. The choice of denominator is critical to reproducing all L and P values.

## Provenance and limitations

Raw checkpoints were materialized from ChatGPT Library and compared via JSON assignment extraction and `git hash-object`; the full 39-file manifest is in `chatgpt-ipa-html-revision-manifest.md`. A field name's absence is not evidence that a function could not have existed under other code; for instance the 09:48 Georgian-complete snapshot predates the later `GEORGIAN_ALPHABET_ROWS` representation. The 39 filenames document evolving intent, not guaranteed functional correctness. The full conversational transcript must still be recovered. Never conflate UI P, research P_attested, unique Glottocodes and ISO-first language identities.

Primary source: https://github.com/andreabenetton/glottodelta/blob/main/baseline/original.html

Deduplication source: https://github.com/andreabenetton/unisermo/blob/73110321a6f1c4eeb5e8bd71b03efdea52020c36/scripts/analyze_phoneme_inventory.py
