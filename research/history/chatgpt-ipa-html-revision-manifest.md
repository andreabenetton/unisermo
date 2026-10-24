# ChatGPT IPA atlas: recovered HTML revision inventory

**27 July 2026, prior to the first public GlottoDelta Git commit.** ChatGPT Library contains 39 HTML files with the `ipa_language_counts` basename created from 05:15:31 to 17:08:22 UTC. These are recoverable intermediate **file snapshots** from the ChatGPT phase, preceding the Git import at 17:59:16 UTC.

These files provide an observable revision trail, not necessarily a complete list of every conversation message or every local edit. Names describe intended changes and are **not sufficient evidence of implementation correctness** without individual file comparison.

| # | Created UTC | ChatGPT-generated HTML filename | Bytes | Independently calculated Git blob SHA (selected) |
|---:|---|---|---:|---|
| 1 | 05:15:31 | `ipa_language_counts.html` | 2797713 | c4a7b9be7939c26f0d6b7fb2b9e3e1ce1c772384 |
| 2 | 05:20:34 | `ipa_language_counts(1).html` | 2805863 | — |
| 3 | 05:33:59 | `ipa_language_counts(2).html` | 2818995 | — |
| 4 | 05:47:03 | `ipa_language_counts_language_selector_fixed.html` | 2820405 | — |
| 5 | 05:58:15 | `ipa_language_counts_demographics_corrected.html` | 2824514 | a20e5c2aa5ef8f1d88e39e797fd7fae3919c9a98 |
| 6 | 06:17:50 | `ipa_language_counts(3).html` | 2824818 | — |
| 7 | 09:08:25 | `ipa_language_counts_phoneme_variants.html` | 2828076 | — |
| 8 | 09:29:02 | `ipa_language_counts_verified_mappings.html` | 2832020 | — |
| 9 | 09:48:31 | `ipa_language_counts_georgian_complete.html` | 2841315 | e524f99c7c036d79db172ae34a893ca8352a2ac1 |
| 10 | 12:25:02 | `ipa_language_counts_with_audio.html` | 2848500 | — |
| 11 | 12:38:10 | `ipa_language_counts_conditional_coverage.html` | 2852345 | — |
| 12 | 12:46:53 | `ipa_language_counts_english.html` | 2852293 | — |
| 13 | 13:04:50 | `ipa_language_counts_language_verified.html` | 3017035 | — |
| 14 | 13:12:27 | `ipa_language_counts_pulmonic_layout.html` | 3045893 | — |
| 15 | 13:18:39 | `ipa_language_counts_manner_header_compact.html` | 3046250 | — |
| 16 | 13:24:32 | `ipa_language_counts_vowel_layout.html` | 3051718 | — |
| 17 | 13:33:46 | `ipa_language_counts_ipa_standard_layout.html` | 3056653 | — |
| 18 | 13:40:39 | `ipa_language_counts_vowel_compact_sources.html` | 3061172 | — |
| 19 | 13:53:21 | `ipa_language_counts_official_ipa_2026.html` | 3062315 | 1c87dee9995311d9f020523c260ef09ceb417d23 |
| 20 | 14:10:27 | `ipa_language_counts_vowel_five_headers.html` | 3063472 | — |
| 21 | 14:41:31 | `ipa_language_counts_vowel_13_columns.html` | 3063351 | — |
| 22 | 14:44:19 | `ipa_language_counts_vowel_12_columns.html` | 3062974 | — |
| 23 | 14:47:41 | `ipa_language_counts_vowel_11_columns.html` | 3062942 | — |
| 24 | 14:49:58 | `ipa_language_counts_vowel_oe_oe_shifted.html` | 3062896 | — |
| 25 | 14:56:32 | `ipa_language_counts_vowel_cell_highlights.html` | 3063591 | — |
| 26 | 15:02:12 | `ipa_language_counts_vowel_exact_width_no_autoplay.html` | 3064919 | — |
| 27 | 15:10:00 | `ipa_language_counts_legends_fixed.html` | 3065142 | — |
| 28 | 15:12:19 | `ipa_language_counts_vowel_legend_inner_yellow.html` | 3065148 | — |
| 29 | 15:25:25 | `ipa_language_counts_click_families.html` | 3071595 | — |
| 30 | 15:37:24 | `ipa_language_counts_verified_population.html` | 3073061 | — |
| 31 | 15:58:58 | `ipa_language_counts_p0_consonants_verified.html` | 3075743 | — |
| 32 | 16:10:13 | `ipa_language_counts_vowel_oe_shifted_left.html` | 3075743 | — |
| 33 | 16:11:38 | `ipa_language_counts_vowel_epsilon_oe_shifted_right.html` | 3075724 | — |
| 34 | 16:24:26 | `ipa_language_counts_priority_features.html` | 3100469 | 93d015dc552c50c67ce04c44fa4f054a51aa551e |
| 35 | 16:37:18 | `ipa_language_counts_iso_comparison_labels.html` | 3101219 | — |
| 36 | 16:39:04 | `ipa_language_counts_full_width_intro.html` | 3101229 | — |
| 37 | 16:43:23 | `ipa_language_counts_single_combo_inline_evidence.html` | 3103170 | — |
| 38 | 16:58:06 | `ipa_language_counts_five_audio_sources.html` | 3135951 | — |
| 39 | 17:08:22 | `ipa_language_counts_scroll_quality.html` | 3141880 | eab1b5ed7b5463a52202a6dd9bcd13a811af85c3 |

## Verified byte identity

The Library's `ipa_language_counts_scroll_quality.html` (created 17:08:22 UTC) was materialized as **the original raw file bytes** and independently hashed with `git hash-object`: `eab1b5ed7b5463a52202a6dd9bcd13a811af85c3`. This exactly matches the Git blob for `glottodelta/baseline/original.html` **and** the first imported `public/index.html`, confirmed from initial commit `bd25974983e3f5f160659851880147876488c1ca`. Size in all three: **3,141,880 bytes**. The SHA-256 of the actual ChatGPT file is `93734e6d0c423b76d239b817e71d8f382cfd18d33c33204804a969bb5abcb252`.

Thus the ChatGPT phase's final file was imported into GlottoDelta **byte-for-byte**, not merely as a similar reconstruction. Five earlier snapshots also had raw bytes materialized and Git blob hashes computed (see table).

## Content-level checks on materialized checkpoints

The checks below inspect literal code markers in the original saved HTML files; **absence of a particular variable name does not prove absence of a feature under another implementation**.

| Checkpoint | Raw bytes | `SPEAKER_ESTIMATES` | `GEORGIAN_ALPHABET_ROWS` | `VERIFIED_LANGUAGE_PROFILES` | `IPA_AUDIO_FILES` | `differencesOnly` |
| --- | ---: | :---: | :---: | :---: | :---: | :---: |
| 05:15 first HTML | 2,797,713 | No | No | No | No | No |
| 05:58 demographics-corrected | 2,824,514 | Yes | No | No | No | No |
| 09:48 Georgian-complete | 2,841,315 | Yes | No | No | No | No |
| 13:53 official IPA | 3,062,315 | Yes | Yes | Yes | Yes | No |
| 16:24 priority features | 3,100,469 | Yes | Yes | Yes | Yes | Yes |
| 17:08 final baseline | 3,141,880 | Yes | Yes | Yes | Yes | Yes |

These checkpoint inspections complement the dated user requests and demonstrate that the final research tool accumulated new data structures, verification machinery, playback and comparison features during its ChatGPT phase, **before the Git import**. The fully faithful account still requires the conversation transcript and detailed diff inspection, not just marker presence.

## Research implications

1. The earliest recovered version is **05:15 UTC**. Its size is 2,797,713 bytes and Git blob SHA `c4a7b9be7939c26f0d6b7fb2b9e3e1ce1c772384`.
2. Subsequent file versions have searchable names such as `demographics_corrected`, `phoneme_variants`, `verified_mappings`, `georgian_complete`, `official_ipa_2026`, `verified_population`, `priority_features` and `scroll_quality`. These offer precise search anchors for the corresponding conversation messages.
3. This pre-Git sequence is distinct from the Claude Code commits that reorganized the app **after** the first Git import; do not attribute the original 39 HTML revisions to Claude.
4. The 39-version list is **not** a benchmark dataset of linguistic outcomes. It documents research/tool construction, including corrections and methodological refinement; it still needs detailed semantic inspection and chat transcript cross-matching for the paper.
5. The raw historical files currently remain in ChatGPT Library. Before publication, export or archive them in a durable versioned store with provenance and permissions, avoiding an unwieldy 100+MB binary Git snapshot without a retention policy.

See `research/history/original-chatgpt-ipa-atlas-conversation.md` for dated user requirements and `research/history/glottodelta-git-archaeology.md` for subsequent code changes.
