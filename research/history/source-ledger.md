# Unisermo historical source ledger

Purpose: make every future chronology/paper claim traceable. Confidence labels are **repo artifact**, **prior conversation**, **experiment raw artifact**, or **unverified**. The diary is an interpretive index; this ledger identifies primary records.

## Historical primary sources

| Record | What it supports | Reliability/remaining action |
| --- | --- | --- |
| `research/history/chatgpt-ipa-html-revision-manifest.md` | Full Library-created file manifest of **39 successive 27 July 2026 HTML snapshots**, with six materialized blob hashes | Library file metadata and locally computed Git blob hashes; full verbatim chat transcript still not exported |
| `research/history/original-chatgpt-ipa-atlas-conversation.md` | Recovered July 27 original ChatGPT requirements for the IPA app, with dated message-level excerpts | Prior-conversation retrieval; complete transcript still needed; HTML artifact fingerprint independently verified |
| [`glottodelta/baseline/original.html`](https://github.com/andreabenetton/glottodelta/blob/main/baseline/original.html) | Frozen initial web application from the ChatGPT phase, before Claude Code refinements | Git blob `eab1b5ed7b5463a52202a6dd9bcd13a811af85c3`; first repository commit `bd25974983e3`, 27 July 17:59 UTC; identical blob to first `public/index.html` **and independently identical to retrieved ChatGPT Library final HTML file** |
| Recovered conversation fragments, 22 May 2026 | Original discussion of Georgian phoneme–grapheme correspondences, /h/, /ŋ/, /ə/, glides and affricates | Dated prior-conversation summaries; full thread still to be exported |
| `research/grammar/confirmed_decisions.json` | Date-stamped 10 Aug 2026 grammar confirmation and individual decisions | Repo artifact; inspect entire file for any paper |
| `language/verb_specification.md`, `language/numerals.md`, `language/vocabulary_design_rules.md` | Normative linguistic rules and examples | Repo artifacts; file history needed for dates of adoption |
| `formalization/data/morphology.json`, `formalization/data/lexicon_index.json` | Current parser/generator contracts and accepted/attested indexes | Current state, not proof of historical adoption date |
| `research/lexicon/confirmed_lexicon.json` | Confirmed lexicon at file revision | Verify Git history for each lexical decision |
| `research/lexicon/kinship-and-numerals-preservation.md` | Record of user correction about earlier relationship and number systems | Retrospective; compare with original conversations |
| `research/lexicon/expansion-batch-001.json` | Experimental 100-concept review, not canonical word addition | Research only |
| `research/lexicon/*results*.md` | Pilot reports and stated limitations | Secondary summaries; back-check raw outputs/commits |
| `benchmarks/corpus/*.jsonl` | Reproducible structured benchmark inputs and splits | Machine-checked ≠ semantic human-validated |
| GitHub Actions links in `research/history/research-diary.md` | Execution and experimental source artifacts | Actions artifacts may expire (30 days); preserve for paper |
| Chat history reconstruction before 10 Aug 2026 | Earliest motivation, rejected options and genealogy of decisions | **Gaps remain; do not fabricate chronology** |
| Commit `8179564` recalled in conversation | October name change and separation from GlottoDelta | Verify commit metadata before paper |

| [Frozen-baseline implementation audit](glottodelta-original-baseline-audit.md) | Static parsing of `DATA`, `SPEAKER_ESTIMATES`, verified orthography profiles, Georgian graphemes, L/P functions and quality score; contrasts with old/new language inventory | **High confidence** in reported frozen-source content; not independent validation of demographics, IPA sampling or causal role in choices. Includes caveat that speaker denominator exceeds deduplicated persons. |

| [August phonology decision chain](august-phonology-decision-chain.md) | Direct immutable SHA recovery of commits `7311032`, `011247a`, `9aa7b49`, `8bb979b` in **Unisermo** with original alternatives, model scores, decisions and open assumptions | **Verified commit objects**. Quantitative metrics are research models, not validated human intelligibility. Chat-to-commit causation remains partially inferred. |
| [Ten original ChatGPT HTML snapshots](glottodelta-chatgpt-snapshot-comparison.md) | Direct Library file checkpoint comparison, invariant corpus, code changes and ISO-first denominator reconciliation | **Verified raw-file audit** of 10 out of 39 snapshots. 2,122 ISO-first research languages must not be conflated with raw Glottocode identities. |

## Required per-entry data for all new research

- Date/time UTC, event type, source link and source commit hash
- Research question and prior hypothesis, including possible negative outcome
- Dataset identity and exact development/held-out split
- Toolchain, model version, provider, seed, prompting variant, pricing, known retries
- Measurements and unscored raw data locations
- Confounders, threats to validity, failed runs, and corrections to earlier reports
- Canonical decision impact (typically **none** for experiments)
- Author review and status: `observed`, `proposed`, `accepted`, or `retracted`

Do not collapse a past exploratory conversation into a later confirmed design decision. Citation of a model answer alone is not proof of linguistic equivalence.
