# Semantic schema confound: case tags versus role tags (24 October 2026)

**Pre-experiment registration.** No external model answers from this prospective corpus were inspected when the prompts, scoring and cases were frozen. All samples are **development-only**; the frozen holdout and Unisermo canon remain unchanged.

## Motivating retrospective audit (original PR #12)

Source: original responses and machine scores under `benchmarks/evidence/relational-frame-2026-10-24-run40089793501.*`. Re-read the original Qwen3 JSON answers, not merely the aggregated score.

| Prior full-role pilot outcome (eight transition clauses) | Cold | Guided |
| --- | ---: | ---: |
| Destination-state lexical value found in **either** `destination` or `result_state` | **8/8** | **7/8** |
| Final-state lexeme incorrectly placed in `result_state` with `destination=null` | **8/8** | **7/8** |
| Causative clauses (eight): result lexeme found in `result_state` or `destination` | **8/8** | **8/8** |
| Causative clauses: fabricated explicit `source_state` | **6/8** | **4/8** |

This retrospective analysis introduces **new descriptive metrics after observing the data**, so they must not replace the original preregistered 0/24 cold and 4/24 guided twelve-field exact outcomes. A correct endpoint lexical value does **not** establish correct grammatical case, causativity, unique theme/causer role or whole-proposition comprehension. In particular, the `theme` label for the subject of noncausative `traes` is a research annotation, not independently confirmed.

The key question is whether Qwen handles **morphological suffix identification** differently from **mapping those suffixes and verb frames to semantic roles**.

## Prospective dataset and design

`benchmarks/corpus/case-role-dev-001.jsonl`: 12 documents with two complete clauses each, 24 **new surface clauses relative to the previous RF001–RF012 corpus**, equally divided across the three existing canonical frames. Same roots, lexical examples and templates have been seen in other development studies: the clauses are *not* independent linguistic holdout items. The deterministic parser `formalization/semantics/relational_frames.py` checks each clause and supplies the two-case/two-role labels (not a human-certified semantic reference).

The 24 clauses are presented once per arm, paired into 12 two-clause documents. A short **identical normative grammar reference** is provided in both arms (so this is *not* cold comprehension):

1. **case:** return each original postverbal nominal's stem and morphological case, using `accusative/dative_allative/ablative/resultative`.
2. **role:** return each original postverbal nominal's stem and semantic role, using `patient/destination/source/result`.

The two prompts have **identical input clauses, grammar primer and JSON shape**, differing in the requested interpretation of the `tag` field and allowed labels. Both output:
`{"events":[{"verb":"traes","args":[{"stem":"solid","tag":"..."},{"stem":"likwid","tag":"..."}]},...]}`
with exactly two events per document and two args per event. No answer key is embedded in prompts. The subject role, tense/aspect, referent binding, quantifier scope, pragmatics and sentence-to-sentence discourse are deliberately **not scored** to isolate complement attachment and meaning-role projection. `-in` remains outside these source-licensed verb frames.

## Preregistered outcomes

- Primary: exact **verb + two correctly stemmed and tagged arguments** per clause (24 per condition). This is a different metric from PR #12's all-twelve-field proposition score.
- Secondary: exact arguments (48 per condition); stems and tags separately (48 each); wrong-tag confusion pairs; JSON structure failures; paired two-clause document outcomes; model usage and USD per exact clause.
- Missing or wrongly typed keys, extra keys, reversed arguments or invalid JSON invalidate an event/field exactly as implemented; no posthoc correction, no automatic remapping `-ad` destination to `-da` result.
- The two output tasks are not interchangeable performance measures: case labels are largely surface forms, while semantic roles require valency and frame context. A difference is **descriptive evidence about decoding tasks**, not an isolated causal effect of ontology labeling, and does not prove that a model understands source language.
- Report pairwise outcomes and family differences descriptively. Twelve correlated documents are not 48 independent propositions; no sample-level significance claims.
- Cost: per-arm input/completion tokens, provider-reported USD, USD per strictly correct clause, with no cross-study equivalence assumption.

Operational constraints: Qwen3 32B via existing OpenRouter helper, requested temperature 0.7, seed 23, reasoning disabled and no provider fallback; actual returned model/provider logged, seed may be ignored. Maximum **24 billable API calls**, **340 requested max completion tokens** each, and cumulative **USD 0.02 observed-cost stop** after each billable response, not an absolute prepaid budget. Raw answers are persisted before scoring; partial runs cannot masquerade as complete ones. Freeze code, corpus and protocol before the one-shot workflow begins.

## Scientific boundary and reviewer checklist

This is machine-gold grammar and semantic projection from accepted written examples. **Independent human review is still 0/24** for these new sentences. A separate reviewer must inspect canonical sources and judge whether each example is licensed and whether its case/role target is semantically natural, *without being told the model's result*. Track whether a label describes morphosyntax or broader conceptual equivalence; in particular, causative `result` and noncausative `destination` might share everyday English paraphrases while having distinct grammatical suffixes. The study intentionally preserves that distinction.

No change to the normative `language/` files, seven-case inventory, lexical decisions or original result archives is allowed as part of this pilot. Next gate after the analysis is independent review, then a richer controlled English comparator with explicitly checked semantic equivalence, and only after a ratified referential model should connected discourse be scored.

---

## Prospective run completed — observed results, 2026-10-24

**Execution:** [Qwen3 paired experimental run 40090842899](https://github.com/andreabenetton/unisermo/actions/runs/40090842899) completed all 24 responses. Returned model `qwen/qwen3-32b`, provider DeepInfra in all requests, all `finish_reason=stop`. Source-provenance / scorer tests passed in [run 40090809826](https://github.com/andreabenetton/unisermo/actions/runs/40090809826) and updated posthoc diagnostics passed in [run 40090933318](https://github.com/andreabenetton/unisermo/actions/runs/40090933318). An initial offline test run exposed a wrong `doc` vs `id` dictionary key in the scorer; this implementation error was fixed and verified *before* paid execution, without revising the corpus or prompts.

The full original artifact `case-role-40090842899` (ID `12558578960`) was independently downloaded, checked and rescored in [archive job 40090996422](https://github.com/andreabenetton/unisermo/actions/runs/40090996422). Preserved original bytes:
- [`benchmarks/evidence/case-role-2026-10-24-run40090842899.jsonl`](../../benchmarks/evidence/case-role-2026-10-24-run40090842899.jsonl), raw SHA-256 `c55cd847cd2522f8857432e0121c990f39064a78335fccd5e5fa28e9430695e6`.
- [`benchmarks/evidence/case-role-2026-10-24-run40090842899.score.json`](../../benchmarks/evidence/case-role-2026-10-24-run40090842899.score.json), corpus SHA-256 `0d8c6a10f7cb8b4545654208af9cfbf8af65f870b0e2e6334c7adc9e6df4a1fb`.

| Registered measure | Morphological **case** arm | Semantic **role** arm |
| --- | ---: | ---: |
| **Exact two-argument complete clauses** | **16/24 (66.67%)** | **15/24 (62.5%)** |
| Arguments with BOTH stem and label correct | 35/48 | 39/48 |
| Exact argument stems alone | 38/48 | 43/48 |
| Exact argument labels alone | 37/48 | 44/48 |
| Invalid JSON envelopes | 0/12 | 0/12 |
| Input tokens | 4,208 | 4,160 |
| Completion tokens | 1,531 | 1,474 |
| Total tokens | 5,739 | 5,634 |
| Provider USD | 0.00076532 | 0.00074552 |
| USD / strict correct clause | 0.0000478325 | 0.0000497013 |

Whole experiment **11,373 tokens**, observed provider USD **0.00151084**, well under the USD 0.02 stop.

### Source-frame stratification: eight clauses per family

| Family | Case arm exact | Role arm exact |
| --- | ---: | ---: |
| `mov` patient `-em` + destination `-ad` | **7/8** | **5/8** |
| Noncausative `traes` destination `-ad` + source `-de` | **1/8** | **4/8** |
| Causative `traes` patient `-em` + result `-da` | **8/8** | **6/8** |

The surface-case arm made **4** `ablative → resultative` confusions, **4** `dative_allative → accusative`, plus three other tag confusions. The role arm made **3** `source → result` and **1** `destination → result` confusions. The role arm recovered more **labels** and **stems** than the case arm, yet one fewer strictly correct complete clause. Failures still include incorrectly retained noun suffixes as part of a stem, not merely relation interpretation.

This clarifies the earlier failure but does not imply an inverted hierarchy of cognitive complexity: the two arms ask different questions, provide the model with the operative rules, have different permissible label vocabularies, and use familiar templated development constructions. It is **not** a direct comparison of general semantic recognition to morphological understanding or to controlled English.

### Historical diagnostic and next decisions

`benchmarks/relational_frame_diagnostics.py` and `tests/test_relational_frame_diagnostics.py` now reproduce from the **unchanged original PR #12 JSONL** the posthoc counts motivating this trial, with their retrospective status made explicit. The original strict scoring of 0/24 cold, 4/24 guided is **not recalculated or replaced**.

**Independent semantic-key approval: 0/24** new clauses. [Review worksheet](case-role-human-review-2026-10-24.md) requires separate human judgments for morphological cases and licensed semantic roles. Because the normativity and the exact theme/causer entailments of the new full finite sentences remain under independent review, avoid presenting these machine gold scores as validated communicative correctness.

**Decision gate:** do not change the seven-case system, `traes` meanings, lexical entries, grammar or holdout. The next strongest step is independent adjudication of the constructed case/role gold, then independently reviewed English paraphrases and a genuinely semantic equivalence test in which both messages and total token/prompt/correction costs are controlled. A separate scored axis for *formal output-schema compliance* should be retained, rather than retrospectively erasing failure cases.
