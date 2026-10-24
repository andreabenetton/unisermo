# Schema repeatability: retrospective analysis and next experiment (2026-10-24)

Status: **development research only**, not language-design evidence and not a held-out validation.

## Historical evidence audited

- [Paired schema run 40071313036](https://github.com/andreabenetton/unisermo/actions/runs/40071313036), artifact `paired-schema-40071313036` (12551770970), source `schema-variety-002.jsonl`: generic 16/24, strict 23/24.
- [Fresh development run 40072804634](https://github.com/andreabenetton/unisermo/actions/runs/40072804634), artifact `schema-fresh-40072804634` (12551833368), source `schema-replication-003.jsonl`: generic 18/24, strict 16/24.

Reinspection of original 16 JSON responses per run confirms every answer decodes as either a JSON array or an object containing an events array. There were **no format failures** in these runs. Schema choice also changes the output envelope (generic array vs strict object), so the treatment bundles multiple changes.

| Run | Generic errors | Strict errors | Document-level strict−generic differences |
| --- | --- | --- | --- |
| Initial paired | tense 5, person 3 | aspect 1 | +3, −1, +1, +3, 0, 0, 0, +1 |
| Fresh replication | tense 4, aspect 2 | tense 2, aspect 3, interrogative 3 | 0, +1, −3, −1, −1, +3, −1, 0 |

Per-document sign-flip exploratory tests (8 clusters, two-sided, 256 sign assignments) yield p=0.25 and p=0.8125 respectively. The 95% document-cluster percentile bootstraps for strict−generic event-accuracy differences are approximately [0, 0.625] and [−0.458, 0.292]. This does not establish equivalence, nor does it prove superiority. In particular, all three H003 interrogative errors in the strict arm share one document and cannot be interpreted as three independent failures. The original scorer is sufficient for counting feature differences, but not for detecting dependence among errors. Note that the displayed uncertainty summaries are exploratory and conditional on the selected development documents.

### Reproduction (offline, no paid API calls)

Download both ZIP artifacts from GitHub Actions, extract raw JSONL, then from the repository root:

```sh
python -m benchmarks.schema_repeatability --corpus benchmarks/corpus/schema-variety-002.jsonl --responses /path/to/paired-schema.jsonl
python -m benchmarks.schema_repeatability --corpus benchmarks/corpus/schema-replication-003.jsonl --responses /path/to/schema-fresh.jsonl
python -m unittest tests.test_schema_repeatability -v
```

The new analyzer verifies document/condition completeness, accepts the two known answer envelopes, checks all eight field values **and their exact JSON/Python types** (so bool is not accepted as integer person), reports original field errors separately from structural failures, and uses document-level uncertainty. It never reads a holdout.

## Corpus reuse audit

The five development packs `discourse-001`, `tense-replication-002`, `operator-variety-001`, `schema-variety-002` and `schema-replication-003` use 108 **nonoverlapping source IDs** from the 144-row `expansion-001` dataset, leaving 36 not used in those five packs. This is ID-level disjointness only; the same three verbs and noun vocabulary, near-identical templates, and possible repeats across other pilots prevent a claim of independent semantic validation. Remaining 36 source rows: pro_drop 15, subject 12, negative 3, polar 6, with limited TAM patterns. Do **not** call them independent holdout.

## Next prospective stage: response variability (not yet executed)

**Hypothesis:** within-condition variation and document-template interaction explain a substantial part of the apparently reversed schema advantage.

**Controlled design:** repeat the *same* 8 development documents twice under each condition (32 API calls total), alternating or randomized order, with model ID, provider, temperature, prompt, score version, decoding settings, request and response identifiers captured. Do not edit prompts between replicates. Hold JSON handling and scoring identical across conditions. Bound `max_output`, total calls and a USD budget at implementation time. The existing original run can be treated as retrospective evidence, but not silently as an interchangeable repeated randomized trial.

**Primary outcome:** per-document exact-eight-field accuracy; report document-cluster paired differences and within-document per-condition disagreement. Secondary: error taxonomy, valid output structure, request/completion tokens, USD cost, and USD per correctly decoded event. Report operational denominator separately if documents with zero exact events. Confidence intervals must account for repeated answers from the same document.

**Decision gate:** do not modify grammar or select a preferred schema on these eight documents alone. Replicate any improvement on genuinely diverse *new development* documents first, then freeze a meaningful holdout for later independent validation. For semantic comprehension, expand tasks to case/complement structures, quantified reference, scope and discourse, with separately human-verified meaning; structural slot recovery alone is not enough.

No canonical lexicon, case, numeral, kinship, or morphology updates are authorized by these results.
