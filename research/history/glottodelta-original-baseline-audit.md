# GlottoDelta frozen ChatGPT baseline: quantitative and implementation audit (24 October 2026)

## Scope and provenance

This audit inspects the actual source of [`baseline/original.html`](https://github.com/andreabenetton/glottodelta/blob/main/baseline/original.html), not the reworked GlottoDelta UI, its later normalized exports, or recollections of what the original application did. The file was imported with initial Git commit [`bd25974983e3f5f160659851880147876488c1ca`](https://github.com/andreabenetton/glottodelta/commit/bd25974983e3f5f160659851880147876488c1ca), 27 July 2026 at 17:59:16 UTC. The previously recovered final ChatGPT HTML file is **byte-identical** to this blob: Git blob `eab1b5ed7b5463a52202a6dd9bcd13a811af85c3`, 3,141,880 bytes. Consult `original-chatgpt-ipa-atlas-conversation.md` and `chatgpt-ipa-html-revision-manifest.md` for the independent Library-file verification and 39 pre-import snapshots.

Method: inspect bounded portions of a very large HTML file, enumerate JavaScript declarations and visible headings, parse JSON literal assignments directly from the original file, and compute counts. This is **static source inspection**, not a browser interaction or independent reexecution of PHOIBLE/CLDR ETL. Any discrepancy with later `docs/data-report.md` needs version-by-version reconciliation rather than silent replacement.

## Observed structure and controls

- Standalone English-language HTML/CSS/JavaScript app with embedded language/phoneme tables. Main heading: *Demographically weighted distribution of IPA symbols*. The HTML includes IPA/licence attribution and date metadata for 27 July 2026.
- Visible sections: pulmonic consonants; vowels; non-pulmonic consonants (including clicks, voiced implosives and ejectives); other IPA symbols; writing-system coverage; sources/licensing; data provenance; and a phoneme audit.
- On symbol selection, a drawer shows attesting languages, ISO and representative Glottocode, phoneme–grapheme correspondences, speaker estimates, source-audit status and phoneme audio samples.
- Language-selection and two-language comparison modes; comparison differences-only option; source-evidence filters; quality/confidence displays. Orthographic statuses appear as mapped (green), alternative realization (amber), source-attested but unresolved (blue), and absent (red).
- Source includes `IPA_AUDIO_FILES` and configurable audio-source mappings. A dedicated Georgian alphabet table is present. These features are in the frozen ChatGPT deliverable: do **not** attribute them to the later Claude Code migration.
- This baseline should not be confused with the later separate systematic **allophone** data audit and phonemic/phonetic toggle introduced by the 28 July commits.

## Dataset inspection

| Static-source observable | Baseline result | Meaning / limitation |
| --- | ---: | --- |
| `DATA` symbol keys | **111** | IPA keys displayed/stored, not 111 canonical Unisermo phonemes |
| Symbol–language attestation rows summed across `DATA` | **49,600** | Repeated source-language entries across symbols; not unique languages |
| Distinct nonempty Glottocodes within `DATA` | **2,176** | One more data identity lacks a Glottocode; approximately **2,177** dataset language identities by fallback key |
| Distinct nonempty ISO codes in the source symbol-language rows | **2,095** | Identifiers in source rows, not demographically verified language count |
| `SPEAKER_ESTIMATES` keys | **384** | ISO estimates in baseline demographic map |
| ISO codes linked both to the phoneme dataset and speaker estimates | **384** | Denominator population set for `P` |
| Sum of those 384 estimated speaker counts (`SPEAKER_BASE`) | **8,786,359,971** | **Not a verified count of unique world residents**; must not be presented as world population |
| `GEORGIAN_ALPHABET_ROWS` | **33** distinct Georgian letters | The preserved Mkhedruli profile covers all 33 modern graphemes |
| `VERIFIED_LANGUAGE_PROFILES` | **40** language/orthography profile entries | An *internal code label*, not proof of independent, peer-reviewed validation |

Source: inspect `const DATA`, `const SPEAKER_ESTIMATES`, `const DEMOGRAPHIC_ISO`, `const SPEAKER_BASE`, `const GEORGIAN_ALPHABET_ROWS`, and `const VERIFIED_LANGUAGE_PROFILES` in the frozen HTML. The 40 profile status values comprise 19 `verified-complete`, 14 `verified-contextual`, 4 `verified-partial`, and three single-entry variants (`verified-complete-basic`, `verified-complete-modern`, `verified-romanization`). These are the application's own categories.

### Distinguish *L*, stored percentage, and *P*

1. **L / `DATA[symbol].count`**: number of source-attested distinct languages for the symbol. `DATA[symbol].inventories` instead counts inventory attestations/records, which may exceed the number of languages. `DATA[symbol].pct` is the percentage against the source-language baseline (approximately 2,177 identities), **not the speaker-weighted P percentage**.
2. **P / `speakerStats(...).pct`**: sum of demographic speaker estimates for *eligible* attesting ISO languages, divided by `SPEAKER_BASE` across all 384 linked ISO languages. For a symbol, eligibility is conditional on `languageSymbolState(...).state` being `mapped` or `variant`; `attested` without an orthography/realization mapping is explicitly excluded from P. The HTML's audit displays exactly which included and excluded languages contribute.
3. A language can be attested in PHOIBLE without having a demographically linked ISO record; one ISO can refer to several document varieties. The `P` statistic is therefore **conditional on available identity joins, demographic estimates and mapping decisions**. It is not automatically the share of all people worldwide who can reliably hear or produce a sound.
4. The baseline's `updateQualityIndicators` defines an internally chosen heuristic score `0.55 × verifiedShare + 0.30 × populationCoverage + 0.15 × sourceDepth`, with category thresholds 0.45 and 0.75. **These weights and thresholds are engineering/design assumptions, not fitted or empirically validated confidence probabilities.**

### Example symbol data frozen on 27 July

Values below are `DATA[symbol].count` (L) and **stored source-language percentage**, not P. They were read directly from the ChatGPT-origin baseline; do not silently substitute later-normalized counts:

| IPA | L | Stored % | Interpretive question |
| --- | ---: | ---: | --- |
| `/a/` | 1,983 | 91.1 | Peripheral vowel used in both architectures |
| `/i/` | 2,076 | 95.4 | Later grammar-critical person marker |
| `/u/` | 1,992 | 91.5 | Later grammar-critical person marker |
| `/ə/` | 533 | 24.5 | Present as sixth grammatical vowel in the 8 Aug historical system, retired by 10 Aug |
| `/h/` | 1,258 | 57.8 | **Excluded** despite broad inventory attestation: counts alone cannot explain its rejection |
| `/ŋ/` | 1,424 | 65.4 | **Excluded** despite broad attestation: contrast with spelling/segmentation constraints |
| `/ʃ/` | 782 | 35.9 | Initially independent `sh`, later non-phonemic as a stand-alone inventory member |
| `/j/` | 1,993 | 91.5 | Excluded as a glide in old alphabet, accepted as written `j` later |
| `/w/` | 1,883 | 86.5 | Absent from old alphabet, accepted in 21-letter inventory |
| `/f/` | 968 | 44.5 | Retained; contrasts with `/v/` but lexical pairs discouraged |
| `/v/` | 617 | 28.3 | Retained despite less frequent attestation |
| `/l/` | 1,582 | 72.7 | Retained even as l/r mergers were contemplated |
| `/r/` | 1,099 | 50.5 | Retained even as l/r mergers were contemplated |

**Do not interpret absent exact string keys `ts`, `tʃ` or `dʒ` as evidence those sounds occur in zero languages.** The 111-key baseline data is an IPA-symbol selection/normalization, and affricate representations require a source-level inventory reconciliation before comparing across systems.

The surprising combinations are valuable **research questions**, not retroactive causal proof. For example, if the designers already rejected `/ŋ/` on 22 May, its July attestation count could not have caused that original rejection; at most it could inform a subsequent reevaluation or justification.

## Evidence classes for the future paper

| Claim | Class | Evidence standard / status |
| --- | --- | --- |
| A Git-frozen, user-requested interactive IPA atlas existed before 27 July 17:59 UTC | **Direct artifact + dated conversation**, high | Initial commit; independent snapshot-blob identity; indexed original-session excerpts |
| The baseline embeds 111 IPA keys, 384 speaker estimates, 33 Georgian letters and comparison/audit UI | **Static verified source content**, high | Parsed literal tables and source functions; not a functional/browser QA claim |
| `L`, `P`, mapping state and quality-score arithmetic | **Source-code implementation**, high | Functions in baseline; external dataset quality and adequacy not independently validated |
| A particular phoneme was selected **because of** this atlas or `P` statistic | **Unverified historical causality** | Requires a dated discussion invoking specific number, comparison, or source |
| Cross-language pronunciation and lexical recognition are better because of these phoneme choices | **Hypothesis** | Requires human perception/production experiments; UI counts alone are inadequate |
| Later normalized dataset counts apply unchanged to the initial HTML | **Not established** | Later GlottoDelta report documents different normalization; version separation required |

## Next tests / gaps

- Obtain exact transcript excerpts where PHOIBLE counts (or the conditional demographic P) were used to decide `/ə/`, `/ŋ/`, `/h/`, `/j/`, `/w/`, `sh`, `ts`, `c`, or `j`.
- Establish the demographic source, time frame, overlap and multiple-L1/L2 counting properties of the 384 speaker figures; **never label their sum the world population**.
- Diff the **39** pre-Git HTML snapshots by semantic structures and UI functions rather than relying on filenames or byte-size changes, matching milestones to dated ChatGPT user messages.
- Reconcile the baseline's ~2,177 source identities with GlottoDelta's later normalized report of 2,122 languages; note selection/deduplication and source-version effects rather than asserting a data regression.
- Correlate commits to chats only when both sides are explicitly anchored. An absent conversation or an unreachable abbreviated local Git SHA is not positive proof of a decision.

## Primary references

- [Frozen baseline HTML](https://github.com/andreabenetton/glottodelta/blob/main/baseline/original.html)
- [Initial Git import](https://github.com/andreabenetton/glottodelta/commit/bd25974983e3f5f160659851880147876488c1ca)
- [Original 27 July ChatGPT session reconstruction](original-chatgpt-ipa-atlas-conversation.md)
- [39-file revision manifest](chatgpt-ipa-html-revision-manifest.md)
- [Pre-/post-import Git archaeology](glottodelta-git-archaeology.md)
