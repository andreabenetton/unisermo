# GlottoDelta as a methodological precursor: Git archaeology

Verified 24 October 2026 via connected GitHub repository `andreabenetton/glottodelta`. This is a **separate IPA atlas**, but its data and design work plausibly supported the phonological decisions for the later constructed language. The causal connection is a hypothesis until supported by the original discussions.

## Chronological anchors from commits

| Date UTC | Commit | Evidence |
|---|---|---|
| 27 July 2026 17:59 | `bd25974983e3` | First Git commit imports an already working **single-file IPA atlas** and scaffolds the site. Consequently, the design and data work began **before this commit**, at an unknown earlier date. |
| 27 July 2026 18:31 | `9d632d9aaa2a` | Include all PHOIBLE-attested languages in language-count metric L; avoid treating demographic-only speaker share P as if full phoneme coverage were known. |
| 27 July 2026 18:34 | `213ba194cbc5` | UI explicitly surfaces demographic-certainty and source provenance. |
| 27 July 2026 18:43 | `41973ec8b2ac` | Correct language-identity mismatch in search, selection and comparison. |
| 27 July 2026 18:14 | `bc575d67a614` | Data pipeline normalizes language inventories and identifiers. |
| 28 July 2026 03:56 | `89c1b67acbd5` | Supplementary speaker, language and orthography evidence plus audit/UI improvements. |
| 28 July 2026 05:14 | `24ed70978923` | Explicit map of documented allophones, **distinct** from phoneme inventories. |
| 28 July 2026 05:18 | `71b6c4244dd9` | Separate phonemic versus phonetic views, enabling inspection of accent-realization variability without confusing it with phonemic membership. |
| 28 July 2026 05:03 | `2fe4f9677b4a` | Curated historical language entries, excluded from L/P statistics to avoid distorting measurements. |

All timestamps above refer to **repository commits**, not the initial construction of the atlas or to dates of Unisermo linguistic decisions.

## Data provenance and methodology

`glottodelta/README.md` and `docs/data-report.md` identify three data families: PHOIBLE inventories, Glottolog identities, CLDR-derived demographic estimates. Atlas fields:

- **L:** number of source-attested languages exhibiting a phoneme.
- **P:** speaker-population share among languages with verified demographic matches, **not** among all languages and not all humanity.
- Source report: 111 IPA symbols, **2,122** unique languages, **384** with usable speaker estimates and **1,738** without. Therefore claims like “phoneme X is used by Y% of the world” need denominator and missingness caveats.
- Documented allophones: 3,054 (sound, language) pairs over 100 symbols, from PHOIBLE 2.0.1 sources; **displayed separately** and not allowed to inflate phonemic L/P. The data-report itself notes 835/2,186 languages have available allophonic documentation.

## Relevance for the history of Unisermo

This provides an empirical **tooling context** for the international-phoneme selection discussions: inventory prevalence, population weighting, differences between phoneme and allophone, orthography compatibility, and known data-quality hazards were being implemented **27–28 July**, **before** the original `andreabenetton/language` commit of 8 August and its transfer into Unisermo on 10 August.

The GlottoDelta commit sequence **does not prove** it determined any particular Unisermo letter or phoneme choice. In particular, the six-vowel 24-unit original specification may have been drafted before or alongside the atlas, and the date of the original discussions remains open. Original `baseline/original.html` was **already working** at the first Git commit, so the prehistory may be earlier than July.

## Sources and next forensic tasks

- https://github.com/andreabenetton/glottodelta/commits/main
- https://github.com/andreabenetton/glottodelta/blob/main/docs/data-report.md
- https://github.com/andreabenetton/glottodelta/blob/main/README.md
- https://github.com/andreabenetton/glottodelta/blob/main/baseline/original.html
- https://github.com/andreabenetton/glottodelta/commit/bd25974983e3
- https://github.com/andreabenetton/glottodelta/commit/24ed70978923
- https://github.com/andreabenetton/glottodelta/commit/71b6c4244dd9

To establish direct influence, compare dated language-design discussion with GlottoDelta's original baseline and verify actual phoneme-specific statistics invoked in selecting/rejecting /ə/, /h/, /ŋ/, affricates, j and w. Preserve corrections and missing data rather than extrapolating globally.
