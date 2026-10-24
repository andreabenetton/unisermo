# Full forensic audit: all 39 ChatGPT HTML atlas snapshots (27 July 2026)

**Audit date:** 24 October 2026. **All 39** original HTML attachments preserved in the user's ChatGPT Library were independently materialized as raw files and parsed programmatically. Library creation timestamps (UTC), basenames, SHA-1 *Git blob* hashes, and embedded source constants are recorded below. This supersedes the earlier **ten-checkpoint partial audit** without invalidating its individual observations.

## Method and invariants

- Read the complete raw bytes of 39 files (**116,918,112 bytes across all snapshots**), computing Git object identity as `SHA1("blob " + byte_length + NUL + original_bytes)`. This is not a file's ordinary SHA-1 digest.
- Extract `const DATA=...` as a JSON literal, serialize with stable key ordering for comparison, and enumerate IPA symbol keys, source attestations, distinct Glottocodes and mixed ISO-first research keys. This is static source inspection, **not browser execution or validation of external PHOIBLE/CLDR reference data**.
- **39 unique HTML Git blobs** and **one identical `DATA` JSON value in all 39**. Thus the 111 tracked IPA symbols and 49,600 source symbol-language attestation rows did **not** change among the 39 preserved ChatGPT outputs.
- Counting identities by nonempty Glottocode gives **2,176**; applying the **8 August research code's ISO-first fallback rule** to *every* source yields **2,122**. Those are different deduplication semantics applied to unchanged records, not automatically evidence of corpus shrinkage.
- The earliest file has **no embedded `SPEAKER_ESTIMATES` constant**. Beginning with snapshot **05** at **05:58:15 UTC**, the map has **384 keys**, sums to **8,786,359,971** estimated language speakers, and its JSON value **never changes thereafter**. This is a language-speaker exposure sum with potentially overlapping L1/L2, **not unique world inhabitants**.
- All later embedded literal dictionaries also remain unchanged **after first appearance** in the 39-snapshot sequence: `ORTHO_BY_ISO`, `LANGUAGE_PHONEME_MODELS`, `IPA_AUDIO_FILES`, `GEORGIAN_ALPHABET_ROWS`, `VERIFIED_LANGUAGE_PROFILES` and `VERIFIED_ORTHO`.
- Counts of rows and the **presence of named functions** are source-level observations. A function first present in the examined script does **not** prove it works correctly, and a later replacement/renaming does not mean a feature disappeared. Snapshot *file names* are historical hints, not proof of behavior.

### First verified appearance of each relevant structure

| Time UTC | Snapshot | Source-backed development |
| --- | --- | --- |
| **05:15:31** | 01 | Original 111-symbol / 49,600-row `DATA` corpus already exists. |
| **05:33:59** | 03 | Literal `ORTHO_BY_ISO` and a `speakerStats` identifier are present; demographic estimates not yet embedded. |
| **05:58:15** | 05 | `SPEAKER_ESTIMATES`: first 384-code demographic dictionary. |
| **09:08:25** | 07 | `languageSymbolState` source marker for symbol/language resolution. |
| **09:29:02** | 08 | `LANGUAGE_PHONEME_MODELS` first appears. |
| **12:25:02** | 10 | `IPA_AUDIO_FILES` first appears with 112 entries. |
| **12:38:10** | 11 | `GEORGIAN_ALPHABET_ROWS` first appears with 33 entries; an earlier Georgian coverage feature may have existed under another representation. |
| **13:04:50** | 13 | `VERIFIED_LANGUAGE_PROFILES` first appears with 40 entries together with `VERIFIED_ORTHO`. |
| **15:37:24** | 30 | `populationEligible` source marker appears to control inclusion in speaker-weighted results. |
| **16:24:26** | 34 | Comparison/`differencesOnly` code markers appear. |
| **17:08:22** | 39 | `updateQualityIndicators` source marker appears; the final Git baseline is **byte-identical** to this ChatGPT snapshot. |

The actual chronology is therefore **source corpus → demographic joins → phoneme/grapheme adjudication → audio/Georgian tables → profile verification → demographic eligibility → comparison/quality UX**, with many IPA table-layout refinements between major stages. **No observed change to the source phoneme inventory or its counts** during this period.

## Full artifact fingerprint manifest

Date on every row: **2026-07-27 UTC**. Hash = Git blob SHA-1 from original raw ChatGPT Library file, not necessarily a Git *commit* object.

| # | UTC time | ChatGPT Library original file | Git blob SHA-1 |
| ---: | --- | --- | --- |
| 01 | 05:15:31 | `ipa_language_counts.html` | `c4a7b9be7939c26f0d6b7fb2b9e3e1ce1c772384` |
| 02 | 05:20:34 | `ipa_language_counts(1).html` | `85aa0a4b51bf66d204780156a2b88e4a48a74c0b` |
| 03 | 05:33:59 | `ipa_language_counts(2).html` | `7cf5f5862b685565070dd0bb61b608881c3195e9` |
| 04 | 05:47:03 | `ipa_language_counts_language_selector_fixed.html` | `3c9f7c0bdfa41af09da1fb9f6fbf1d01867a36d2` |
| 05 | 05:58:15 | `ipa_language_counts_demographics_corrected.html` | `a20e5c2aa5ef8f1d88e39e797fd7fae3919c9a98` |
| 06 | 06:17:50 | `ipa_language_counts(3).html` | `8437afc81bebb9914c72b84925316ed1cb718c56` |
| 07 | 09:08:25 | `ipa_language_counts_phoneme_variants.html` | `34c87aed355378d5955dc93ab66a425ff867742d` |
| 08 | 09:29:02 | `ipa_language_counts_verified_mappings.html` | `4be6ae5a86a45f8bc00b82e8f888c10587dc301c` |
| 09 | 09:48:31 | `ipa_language_counts_georgian_complete.html` | `e524f99c7c036d79db172ae34a893ca8352a2ac1` |
| 10 | 12:25:02 | `ipa_language_counts_with_audio.html` | `4f93ed5d3276cc0c52dec9494ce3162aa96ab72c` |
| 11 | 12:38:10 | `ipa_language_counts_conditional_coverage.html` | `bd75f47bf4439d6a43107dd62316102b77775dd7` |
| 12 | 12:46:53 | `ipa_language_counts_english.html` | `d30ebe0d77d49f8579e48fd223f0b33b958670f0` |
| 13 | 13:04:50 | `ipa_language_counts_language_verified.html` | `45143506388e11bdf92c1ee3e72ac2a3bb90ae5b` |
| 14 | 13:12:27 | `ipa_language_counts_pulmonic_layout.html` | `ea8c23ce6a5c837fd7f0242cf14385eb5eee17b9` |
| 15 | 13:18:39 | `ipa_language_counts_manner_header_compact.html` | `d6d3ac97fb6bcf29b54d9aaea710e2b7b05ef057` |
| 16 | 13:24:32 | `ipa_language_counts_vowel_layout.html` | `5942c1393096909b3415faf51c2b8fdf81dae653` |
| 17 | 13:33:46 | `ipa_language_counts_ipa_standard_layout.html` | `60cbaed4ae7e13a10bb643aea793d4cd318093a4` |
| 18 | 13:40:39 | `ipa_language_counts_vowel_compact_sources.html` | `8d1284c5821267d2abf1162e6a1351b34323d356` |
| 19 | 13:53:21 | `ipa_language_counts_official_ipa_2026.html` | `1c87dee9995311d9f020523c260ef09ceb417d23` |
| 20 | 14:10:27 | `ipa_language_counts_vowel_five_headers.html` | `70037a7c76199600e2ab44179fdbcc62b1766db6` |
| 21 | 14:41:31 | `ipa_language_counts_vowel_13_columns.html` | `8e9e775bc1755a5ea965718a85e5f9c09aa200e3` |
| 22 | 14:44:19 | `ipa_language_counts_vowel_12_columns.html` | `27f601fd268c66763ee0fd80db9bdb329f0f7776` |
| 23 | 14:47:41 | `ipa_language_counts_vowel_11_columns.html` | `b4a23ac80b09202e3d2bc12ddf47b500aa48497e` |
| 24 | 14:49:58 | `ipa_language_counts_vowel_oe_oe_shifted.html` | `f2f2cf0a04deeb800dd7a6317e381e034f609508` |
| 25 | 14:56:32 | `ipa_language_counts_vowel_cell_highlights.html` | `34c965c794c11da7febb87d87fea7d1ade5d9b69` |
| 26 | 15:02:12 | `ipa_language_counts_vowel_exact_width_no_autoplay.html` | `eeca938fc1a46be358f5cf8a81cc3dfb2c707adf` |
| 27 | 15:10:00 | `ipa_language_counts_legends_fixed.html` | `e74647fe336969f88f1ed3a8ae3761ea719b6de5` |
| 28 | 15:12:19 | `ipa_language_counts_vowel_legend_inner_yellow.html` | `baffeae35ab590609cb5d7b76f5e8281e86c1b3f` |
| 29 | 15:25:25 | `ipa_language_counts_click_families.html` | `95e8fe8ca07480df2f1533c94c7c66aa127db129` |
| 30 | 15:37:24 | `ipa_language_counts_verified_population.html` | `7ce730ebf71567ce31e3312502327bf84e4d07ac` |
| 31 | 15:58:58 | `ipa_language_counts_p0_consonants_verified.html` | `ffdc1d4cdc52107e69152710481b3164cc49421d` |
| 32 | 16:10:13 | `ipa_language_counts_vowel_oe_shifted_left.html` | `cb5ebc0d24eb0612c122a7249e3c850215ca488c` |
| 33 | 16:11:38 | `ipa_language_counts_vowel_epsilon_oe_shifted_right.html` | `3abcd5acb3e65266e7000a44fd3f7ac109982123` |
| 34 | 16:24:26 | `ipa_language_counts_priority_features.html` | `93d015dc552c50c67ce04c44fa4f054a51aa551e` |
| 35 | 16:37:18 | `ipa_language_counts_iso_comparison_labels.html` | `8efb107d47cc18e7c5e119d419fb62de1e925e4d` |
| 36 | 16:39:04 | `ipa_language_counts_full_width_intro.html` | `b3efdfa95212dac64a212f66b2ed85fd6d8fb30b` |
| 37 | 16:43:23 | `ipa_language_counts_single_combo_inline_evidence.html` | `70e1a79afecc4b153c730fcded391c2474576623` |
| 38 | 16:58:06 | `ipa_language_counts_five_audio_sources.html` | `db03534e74a059a30edd5709d7dbb18cec5324a6` |
| 39 | 17:08:22 | `ipa_language_counts_scroll_quality.html` | `eab1b5ed7b5463a52202a6dd9bcd13a811af85c3` |

## Source validity and future work

- Git hash correctness independently cross-checkable for the final file in [GlottoDelta original baseline](https://github.com/andreabenetton/glottodelta/blob/main/baseline/original.html), initial commit [`bd25974983e3`](https://github.com/andreabenetton/glottodelta/commit/bd25974983e3f5f160659851880147876488c1ca). The previous manifest also independently hashes selected intermediate snapshots.
- Dates are **file-creation timestamps**, not guaranteed user-decision timestamps; the *first appearing source feature* is an upper bound on introduction time.
- A preserved original source table is not an independently established empirical ground truth. The browser's source choices, denominator conditions and interpretation of `P` are **design choices** separate from the original inventory facts.
- Source content counts remained constant while code evolved. Do not confuse this with later post-import **normalization, supplemental phonology data, or separate user-facing app versions**.
- This analysis does **not** recover every step of the original conversation: exact prompts, rejected reasons and explicit user sign-off must be corroborated against first-party chat turns.
- Detailed cross-snapshot source parsing supports the versioned comparison in [`glottodelta-chatgpt-snapshot-comparison.md`](glottodelta-chatgpt-snapshot-comparison.md), which used only ten snapshots and therefore could not pinpoint the earlier audio or Georgian-table introduction.

**Data handling:** the raw 39 HTML file bytes were **not** committed to Unisermo: they remain first-party ChatGPT Library attachments and the final frozen file resides in GlottoDelta. This report commits the artifact *identities* and observed signatures, preserving reproducibility for an authorized researcher with access to those original snapshots.
