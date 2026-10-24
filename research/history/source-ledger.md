# Unisermo historical source ledger

Purpose: make every future chronology/paper claim traceable. Confidence labels are **repo artifact**, **prior conversation**, **experiment raw artifact**, or **unverified**. The diary is an interpretive index; this ledger identifies primary records.

## Historical primary sources

| Record | What it supports | Reliability/remaining action |
| --- | --- | --- |
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
