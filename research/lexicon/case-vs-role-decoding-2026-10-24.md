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
