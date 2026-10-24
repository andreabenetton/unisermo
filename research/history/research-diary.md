# Unisermo research diary

This is the **living historical record** for a future methodological paper about the creation of Unisermo. Its scope is the project **from the earliest recoverable records onward**, not only current experiments. Never rewrite historical findings to fit subsequent results; append corrections explicitly.

## Evidence policy

- **Confirmed repository fact:** cite a named versioned source, commit, or Actions run.
- **Prior-conversation recollection:** indicate that the detail was recovered from conversation context and **has not been independently dated or verified** unless corroborated.
- **Inference/interpretation:** distinguish hypothesis from measured evidence.
- **Unknown:** record gaps; do not fill gaps with plausible stories.
- Use dates of **decisions**, **experiments**, and **documentation** separately when known; do not back-date an event based on when a file was written.
- Record study prompt/code revision, candidate selection, model/provider, corpus development/holdout status, outcomes, negative results, and cost; link raw artifacts where possible.
- Retain failed experiments and discarded hypotheses for the paper. A language-design decision is not validated simply because an LLM can decode an expression.
- GlottoDelta is a separate IPA atlas, not an alternative name for this language.
- The frozen holdout must remain excluded from iterative prompt tuning.

## Recoverable chronology

| Date / period | Entry | Evidence and confidence |
| --- | --- | --- |
| **24 May 2026** | Recovered original discussion on cases and complements: one ending per complement; 7 base cases plus 6 extended, corrected -s genitive and -de source; later revisions moved extended relations to free relators. | `research/history/cases-and-complements-design-history.md` and original May conversation snippets; full transcript not archived |
| Prior to 10 Aug 2026 — exact start unverified | Initial planning of an international, pronunciation-accessible, compositional auxiliary language, built with explicit decision records. The full earlier conversational history has **not** been exhaustively recovered. | Context reconstruction; early date and original rationale need first-party archival verification |
| **10 Aug 2026** | Confirmed baseline grammatical decision set: number-neutral bare nouns; optional `wi` plural; person/tense/aspect morphology; multiple noun cases including resultative; phonological and lexical constraints. | `research/grammar/confirmed_decisions.json` (`confirmed_on`); grammatical counts reported in an Oct 22 baseline audit |
| Aug–Oct 2026, finer dates unverified | Linguistic architecture expanded with explicit phoneme inventory, accent tolerance, Latin/international root exploration, productive compounds, and systematic numeral and kinship studies. Important caution: previously **proposed** kinship stems (`par`, `fil`, `av`, `avun`, etc.) were not all accepted as canonical, whereas the numeral system is documented. | `language/numerals.md`, `language/vocabulary_design_rules.md`, `research/lexicon/kinship-and-numerals-preservation.md` and earlier-conversation reconstruction |
| **22 Oct 2026** | **Unisermo** adopted as official language name; GlottoDelta kept as separate IPA atlas. Earlier local snapshot and rename reported in commit `8179564`. | Name change in project README, previous conversation/commit recollection |
| **22 Oct 2026** | Early 78-sentence tokenizer pilot: `o200k_base` reportedly 281 vs 315 reference tokens (−10.79%); `cl100k_base` 319 vs 315 (+1.27%). Mixed results demonstrated tokenizer-dependence and lack of proof of language efficiency. | Prior-conversation record; verify exact benchmark input sets in `benchmarks/` for publication |
| **23 Oct 2026** | Controlled root recognizability studies (candidate `dik`, `dir`, `dirig`) with Qwen/Gemma, including an open-ended inference follow-up. No reliable justification for replacing `dik` with `dir`. Human study deferred as GitHub issue #3. | `research/lexicon/open-inference-results-2026-10-23.md`, earlier GitHub Actions runs 39901560159 and 39902217811 |
| **23 Oct 2026** | 100-concept lexicon expansion screened as **experimental**, not canonical; candidate `mater`, `pater`, `infan` withdrawn for review against earlier relational kinship design. `jer` remains a general iteration/step counter, not a new genealogical numeral. | `research/lexicon/expansion-batch-001.json`, `research/lexicon/kinship-and-numerals-preservation.md` |
| **23 Oct 2026** | Productive-compound tests established: 12 cases, 3 already-confirmed controls, 9 hypothetical expressions. Qwen cold/rule/dictionary root segmentation 9/12, 10/12, 12/12. Gemma incomplete due to 429. | `research/lexicon/compound-inference-results-2026-10-23.md`; run 39905757760 |
| **23 Oct 2026** | Small dictionary repeated every request versus accumulating full conversational history: both 12/12 segmentations; repeated header 1,976 tokens, full history 6,182 tokens. This did **not** establish persistent model learning. | `research/lexicon/compound-context-results-2026-10-23.md`; run 39906292907 |
| **23 Oct 2026** | Per-document selective glossary vs whole 15-root research dictionary: 8/8 segmentation each; input 169 vs 178 tokens. Synthetic dictionary transport estimates for 100/1,000 entries were expressly **not** claims about 100/1,000 real roots. | `research/lexicon/document-primer-results-2026-10-23.md`, `research/lexicon/document-scaling-results-2026-10-23.md` |
| **23 Oct 2026** | Initial three-clause discourse grammatical-event extraction: 13/18 exact; verbose explanation of zero-marked present yielded 18/18 on the **same development examples**; compact instruction regressed to 13/18. Seven-prompt ablation had best compact result 16/18 (rule + examples or examples + procedure), full verbose earlier 18/18. | `research/lexicon/discourse-semantic-results-2026-10-23.md`, `research/lexicon/discourse-tense-clarification-results-2026-10-23.md`, `research/lexicon/discourse-tense-compact-results-2026-10-23.md`, `research/lexicon/discourse-tense-ablation-results-2026-10-23.md` |
| **24 Oct 2026** | Paired tense replication on different pro-drop development clauses: short 13/18, verbose 15/18; no perfect generalization. | `research/lexicon/discourse-tense-replication-results-2026-10-24.md`; run 40064982181 |
| **24 Oct 2026** | More diverse 24-clause operator/aspect task: original 15/24 exact events, all but nine grammatical-number output values correct. A scorer initially misread valid JSON arrays; corrected without new paid API calls. | `research/lexicon/operator-variety-results-2026-10-24.md`; run 40065657440 |
| **24 Oct 2026** | Explicit typed output specification on development set gave 22/24 exact; paired generic vs strict on **same** development set 16/24 vs 23/24; schema quality materially affects measured comprehension, but not validated on untouched holdout. | `research/lexicon/operator-schema-strict-results-2026-10-24.md`, `research/lexicon/operator-schema-paired-results-2026-10-24.md`; run 40071313036 |
| **24 Oct 2026** | Fresh paired schema replication with 24 previously unused development clauses: generic 18/24, strict 16/24. The previous strict-schema advantage failed to reproduce; no claim of universal superiority is warranted. | `research/history/experiment-2026-10-24-schema-replication.md`; run 40072804634 |
| **24 Oct 2026** | Living research diary initiated, including methodological provenance, limitations and reconstruction gaps; the next investigation uses newly selected clause combinations not in earlier operator/schema corpora. | This document, `research/history/source-ledger.md` and next experiment |

## Historical decisions requiring special preservation

**Numerals:** `nul, uno, bis, ter, for, kin, ses, set, oto, nin, dek, sen, mil`; compounds such as `dekbis`, `bisdekkin`; `jer` for repetitions/steps. See `language/numerals.md`, rather than re-inventing the system.

**Kinship:** prior conversational design favored gender-neutral relational bases with productive gender suffixes; the status of each proposed root varies. Canonical `frat` must not be removed without a formal decision. See the kinship preservation file.

**Research design:** reproducibility, objective grammar parser checks and model experiments are separate from native-speaker intelligibility, human pronounceability, pragmatic compositional interpretation, and valid cross-language translation.

## Open historical recovery tasks

1. Recover the full 24 May 2026 conversation and any still-earlier discussions; the case-system discussion now establishes a May date but not necessarily project inception. Do not assert a project founding date prematurely.
2. Recover original comparison of lexical genealogies/modern worldwide language distributions and decisions about international recognizability.
3. Reconstruct the exact date and rationale for each numeral, kinship, and major morphosyntactic decision rather than relying on an October snapshot.
4. Identify discarded word candidates and rejected grammatical systems, with decision rationale and provenance.
5. Archive stable copies of paid experimental raw outputs **before** GitHub Actions artifact retention expires.
6. Prepare methodology, threats to validity, preregistration and separation of development versus true held-out evaluation for the paper.

## Paper-oriented structure

Suggested sections: problem and motivation; design constraints; phonological and lexical evidence; grammatical design and compositional productivity; decisions and counterfactuals; machine-readable formalization; experiment chronology with failures and negative results; quantitative decoding/cost evidence; human study; limitations, reproducibility and reflections. These are **planned paper sections**, not completed scientific claims.
