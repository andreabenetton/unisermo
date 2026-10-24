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

## Prospective same-development-document repeatability — completed 2026-10-24

**This section supersedes the earlier "not yet executed" status for the prospective trial, without rewriting that earlier planning record.** The model comparison is still development research, not unseen holdout evidence and not independent validation of conveyed meaning.

- GitHub Actions successful run: [40081219392](https://github.com/andreabenetton/unisermo/actions/runs/40081219392).
- Artifact: `schema-repeatability-40081219392` (artifact ID `12554673900`); responses and computed score permanently retained in:
  - [32 original OpenRouter responses](../../benchmarks/evidence/schema-repeatability-2026-10-24-run40081219392.jsonl)
  - [original machine-readable scored results](../../benchmarks/evidence/schema-repeatability-2026-10-24-run40081219392.score.json)
- Original response JSONL SHA-256: `1cc3b41c5e946a1292da428194461dfe66ed4e7dbdf3d16a45e2f5f565296b2c`.
- Source corpus SHA-256: `724f02e8fb9fb437dd80f772c5fd418d0eae8baf8bca2cfd02dbb65eabacc6b0`.
- Archival Actions run: [40081646513](https://github.com/andreabenetton/unisermo/actions/runs/40081646513), verifies the raw checksum, expected model, number of calls and score before committing the evidence verbatim.

### Execution

Exactly 32 isolated API requests: 8 parser-verified development documents (H001–H008) × generic/strict × 2 repetitions. The exact same historical prompts were used in both repetitions of each condition. Condition order was balanced and alternated between repetitions; the two repetitions were not temporally randomized or independent sampling from a language population. Model request `qwen/qwen3-32b`; all returned model IDs `qwen/qwen3-32b`, all provider metadata `DeepInfra`, and all 32 finish reasons `stop`. The existing OpenRouter client requested `temperature=0.7`, `seed=23`, disabled reasoning and appended `/no_think`; whether the provider implements seed exactly is not established. No format failures were observed.

| Measure | Generic | Strict |
| --- | ---: | ---: |
| Repetition 1 exact eight-field events | 17/24 | 20/24 |
| Repetition 2 exact eight-field events | 15/24 | 19/24 |
| Combined exact events | **32/48** | **39/48** |
| Correctness fraction | 66.67% | 81.25% |
| Same eight feature values between repetitions | 22/24 | 23/24 |
| Correct in both repetitions | 15/24 | 19/24 |
| Input tokens | 3,866 | 4,874 |
| Output tokens | 3,258 | 3,374 |
| Total tokens | 7,124 | 8,248 |
| Provider-reported USD | 0.00122152 | 0.00133464 |
| USD per exact eight-field event | 0.0000381725 | 0.0000342215 |

**Total reported cost USD 0.00255616**; the execution cap was 32 requests and USD 0.02 cumulative observed cost. The stricter condition used more total tokens and more gross dollars, but in these repeated *structural* tests cost less per correctly decoded eight-field event. That is not yet a measurement of cost per semantically communicated proposition.

### Error concentration and inference

- Generic field-error totals: tense **8**, interrogative **6**, aspect **2**. H006 mislabelled all three future verbs as past in both repeats; H008 mislabelled all three nonquestions as questions in both repeats. These are clustered failures, not independent nine or six example observations.
- Strict field-error totals: aspect **6**, tense **3**; a small number of document/root positions account for these errors.
- Combined per-document strict-minus-generic event differences, with **both** repetitions as one block: `[-2, 2, 0, -1, -2, 6, -2, 6]`.
- Exploratory two-sided eight-document paired sign-flip p-value **0.53125**, with document-cluster bootstrap 95% accuracy-difference interval **[-0.2083, 0.5417]**. This interval crosses zero widely. Fixed-source document and prompt sampling and the small number of independent clusters prevent general claims.
- The preceding run 40072804634 on these same H documents reported generic **18/24**, strict **16/24**. The new two repetitions returned **17/24 vs 20/24** and **15/24 vs 19/24**. The provider label and model ID were DeepInfra / qwen/qwen3-32b in both runs; this comparison still does not isolate changes in backend implementation, queueing, model nondeterminism or provider-side seed handling.

**Decision:** No schema is selected as normatively preferred; no Unisermo morphology, root or grammar changes. The hypothesis that schema precision universally improves inference remains **unsupported**, while the particular document-level failure modes are worthy of specific future trials.

**Next research stage:** freeze this particular H pack as *used development*, enlarge the development space with independently checked examples of cases/complements, reference, scope, quantification and multi-sentence interpretation, and measure meaning recovery as well as structural slot extraction. Pre-register scoring and a disjoint holdout before tuning again; also consider different model/provider configurations. Avoid using these repeatedly viewed eight documents as a confirmation set.
