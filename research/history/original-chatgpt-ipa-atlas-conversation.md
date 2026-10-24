# Original ChatGPT IPA atlas conversation and GlottoDelta baseline

**Research log compiled 24 October 2026.** The user identified `andreabenetton/glottodelta/baseline/original.html` as the original application produced collaboratively in ChatGPT and later refined using Claude Code. A targeted prior-conversation search recovered dated **message-level excerpts** from the original ChatGPT session on **27 July 2026**. The complete export of the dialogue has **not** yet been obtained. However, **39 original ChatGPT-generated HTML snapshots are indexed in ChatGPT Library**; six key snapshots have been materialized and hashed, including the **exact final HTML file** imported into Git.

## Recovered conversation chronology (27 July 2026; UTC)

The first recovered user message (05:11:50 UTC) begins: **“sei in grado per ogni riquadro presente nella tabella https://www.internationalphoneticalphabet.org/ipa-sounds/ipa-chart-with-sounds/ di contare le lettere presenti in lingue diverse ?”** This exact phrase is a useful ChatGPT history-search anchor. Although the wording says “letters”, the session evolved into an explicit phoneme-versus-grapheme distinction.

| Approximate time | Provenance | Explicit requirement or milestone |
| --- | --- | --- |
| 05:11:50–05:11:57 | **User**, conversation search | Count distinct source languages that attest the phoneme for every cell in an IPA chart; avoid double counting and distinguish exact symbols. |
| 05:12:47 | **User** | Accepted a PHOIBLE-driven approach with source-traceable symbol inventories, language lists and geographic/family information. |
| **05:15:19** | **Assistant output** | First recovered generated file: `ipa_language_counts.html`. Its old conversation sandbox address is not a verified downloadable link in the present session. |
| 05:19:04 | **User** | When selecting a language, display its orthographic graphemes corresponding to the IPA phoneme, not only the IPA symbol. |
| 05:21:00–05:21:44 | **User** | Produce the interactive updated chart with spelling mappings and a speaker-weighted prevalence measure, and verify ISO/Glottocode and demographic joins. |
| 09:03:30 | **User** | Account for phonetic variants when relating IPA symbols to canonical language phonemes; adopt a many-to-many phoneme–grapheme mapping with explicit evidence. |
| 09:44:35 | **User** | Explicitly verify **all 33 modern Georgian graphemes**; add checks for whole-alphabet coverage and language-specific mappings. |
| 13:34:06–13:46:48 | **User** | Cite data sources and attribution/licensing, prefer the official International Phonetic Association chart for symbol inventory/layout; use third-party chart/media only where appropriate. |
| **13:40:14** | **Assistant output** | File `ipa_language_counts_vowel_compact_sources.html` documents an intermediate compact/source-accounting chart. |
| **13:52:53** | **Assistant output** | File `ipa_language_counts_official_ipa_2026.html` documents official IPA chart revision. |
| **14:10:06** | **Assistant output** | File `ipa_language_counts_vowel_five_headers.html`: assistant reported five vowel headings, 15 phoneme columns and 28 vowels, including validation of JavaScript. These are reported features, not a fresh audit of the file's bytes. |
| 16:24:05 | **Assistant output (recovered summary)** | At this stage the single-file application reportedly included evidence filters, two-language comparison, differences-only mode and a transparent L/P audit. This is assistant-reported implementation, corroborated by the recovered final HTML file and its Git-blob match. |

**Research caution:** these are indexed excerpts and paraphrases, **not** a verbatim complete transcript; do not invent missing intervening dialogue or an unverified chat URL. The first recovered user message is 05:11:50 UTC; an initial downloadable HTML is explicitly recorded at **05:15:19 UTC**. The final file cited in the chat is named `ipa_language_counts_scroll_quality.html` at **17:14:38 UTC**; its Library file was created **17:08:22 UTC** and has now been independently materialized and byte-compared with the Git baseline.

- **17:14:38 UTC**: latest working file identified in the ChatGPT conversation as `ipa_language_counts_scroll_quality.html`. This predates the 17:59 Git import. Its Git blob hash **matches** the GlottoDelta initial baseline.

## Historical HTML file recovery and independent verification

Library metadata locates **39 successive `ipa_language_counts*.html` artifacts** from 05:15:31 through 17:08:22 UTC on 27 July 2026. A complete filename/time/size inventory and six independently computed snapshot hashes are in [`chatgpt-ipa-html-revision-manifest.md`](chatgpt-ipa-html-revision-manifest.md).

The raw last ChatGPT file `ipa_language_counts_scroll_quality.html` (3,141,880 bytes) was materialized from the user's Library and passed to `git hash-object`: **`eab1b5ed7b5463a52202a6dd9bcd13a811af85c3`**, exactly equal to the blobs of **both** `glottodelta/baseline/original.html` and `glottodelta/public/index.html` in the first Git commit. Its SHA-256 is `93734e6d0c423b76d239b817e71d8f382cfd18d33c33204804a969bb5abcb252`. Thus **byte identity is demonstrated**, while the full conversational rationale still needs transcript export.

## Immutable Git-level trace of the app

- Git repository `andreabenetton/glottodelta`, initial commit [`bd25974983e3f5f160659851880147876488c1ca`](https://github.com/andreabenetton/glottodelta/commit/bd25974983e3f5f160659851880147876488c1ca), **27 July 2026 17:59:16 UTC**, imports a working HTML app.
- Its **`baseline/original.html` and `public/index.html` refer to the identical Git blob** `eab1b5ed7b5463a52202a6dd9bcd13a811af85c3` (3,141,880 bytes), verified in the first commit's recursive tree. This establishes identical repository content, and **independent bit-for-bit comparison against the recovered ChatGPT file now confirms the same blob**.
- The same Git blob remains at `baseline/original.html` in the inspected main branch; the baseline is a retained reference rather than Claude Code's subsequent restructured app.
- The original document has approximately 1,638 lines, contains license/IPA source-date metadata (`2026-07-27`), PHOIBLE-based symbol-language lists, `SPEAKER_ESTIMATES`, `GEORGIAN_ALPHABET_ROWS`, `VERIFIED_LANGUAGE_PROFILES`, `ORTHO_BY_ISO`, IPA audio mappings, and comparison/audit UI.
- Explicit UI explanation in the baseline: **L** represents source-attested languages while **P** is restricted to demographically linked verified/curated and qualified alternative mappings. Unresolved source attestations are not silently promoted into population percentages. The evidence filter does not rewrite underlying L/P values.
- The baseline reports the Georgian verified language profile covers all 33 letters.
- Git changes after the initial import, including normalized data, allophone view and improvements in evidence handling, document the **later implementation evolution** and must not be retroactively attributed to the initial ChatGPT deliverable unless already present in this blob.

## How this changes Unisermo's intellectual history

The IPA atlas was **not a later by-product** of a finished constructed language. Its central user requirements had already been articulated in this earlier ChatGPT conversation, with numeric phoneme coverage, population weighting, orthodox IPA notation, family/geographic distribution, and scripts/graphemes as first-class issues. This creates a documented research-method stage between the early May constructed-language discussions and August formal specifications.

At the same time, project order is nuanced:

1. **22 May 2026**, recovered **separate** language-design conversations: the user explored international grapheme–phoneme correspondence, including Georgian; the artificial-language inventory underwent explicit discussions of /h/, /ŋ/, /ə/, `c=/tʃ/`, `sh`, `ts`, and `j`. This predates the dedicated **July 27 atlas-building chat**. These are previously indexed conversational records, not source Git commits.
2. **27 July 2026**, dedicated interactive IPA atlas designed in ChatGPT and imported into GlottoDelta at 17:59 UTC.
3. **8 August 2026**, first published Git commit of `andreabenetton/language` with a complete original language grammar and phonology.
4. **10 August 2026**, older specification imported into the successor repository and live language redesign recorded through commits.
5. **22 October 2026**, renaming of the language to Unisermo.

The evolving atlas **likely informed** cross-language phoneme evaluation, as its purpose matches the user's design goals. A particular language-design decision can only be called *caused by the atlas data* after a matching conversation, citation or calculation is retrieved.

## Evidence links and reproducibility

- [Frozen GlottoDelta baseline](https://github.com/andreabenetton/glottodelta/blob/main/baseline/original.html)
- [Original initial Git commit](https://github.com/andreabenetton/glottodelta/commit/bd25974983e3f5f160659851880147876488c1ca)
- [GlottoDelta current readme / methodology](https://github.com/andreabenetton/glottodelta/blob/main/README.md)
- [Later source quality report](https://github.com/andreabenetton/glottodelta/blob/main/docs/data-report.md) — describes later-normalized data; do **not** presume these later counts were the same in the initial HTML.
- [Earlier GlottoDelta commit archaeology](glottodelta-git-archaeology.md)
- [Earlier conversational and commit correlations](conversation-commit-correlation.md)

## Remaining tasks for publication

1. Export the full July 27 ChatGPT transcript and preserve the 39 recovered HTML snapshots; the final emitted HTML content fingerprint has already been independently verified.
2. Recover the separate **May 22** discussions on initial phoneme selection and Georgian orthography; timestamp the chronology before May 24's case discussion.
3. Identify and verify the first source and computation behind any population-weighted claims used to select/reject each sound.
4. Map each relevant later GlottoDelta commit to its actual conversation where possible; **a relevant commit is a search lead, not proof that any particular conversation preceded it**.
5. Make a systematic May→July→August comparison of phonemes, graphemes and morphological person marking, including decisions reversed.
