# Two-model replication: Qwen3 32B × Gemma 3 27B (protocol, 2026-10-24)

**Prerecorded before the paired paid API execution.** The prior case/role test (PR #13) was Qwen-only, so no model-family generalization is justified from its 16/24 case and 15/24 role outcomes. Following the author's request for at least two models, this study runs a *new paired execution* with two different architecture families.

## Model selection

- **Qwen:** `qwen/qwen3-32b` (32.8B dense), already studied as a one-model preliminary.
- **Google Gemma:** `google/gemma-3-27b-it` (27B), already listed in the repository's `benchmarks.openrouter_runner.MODELS` as an approved alternative.
- Source pricing and availability checked on OpenRouter before registration; both published endpoints available as of 2026-10-24.
- Prefer **one common inference service**, OpenRouter provider `DeepInfra` explicitly pinned, `allow_fallbacks=false`, `data_collection=deny`. Pinning provider helps reduce deployment differences but does not equalize architectures, quantization, sampling implementation, tokenizer or training.

## Locked stimuli and procedure

Exactly the **same development-only 12 two-clause documents** from `benchmarks/corpus/case-role-dev-001.jsonl` and **the same existing 24 base questions** (12 documents × case and role tasks); no new gold key and no holdout. For each document/condition, both model families are prompted with **byte-identical user message content**, with the same JSON contract and guide. The questions, subject and suffix morphology, grammatical roles and research-derived labels are unchanged.

Unlike the original Qwen-only caller, the cross-model caller avoids a hidden `/no_think` suffix in the user message, because that suffix would create unequal effective prompts across families. **This is a new run**, and its Qwen results must not be silently conflated with the previous Qwen run: the latter had an extra `/no_think` token and may have used different provider routing/temperature handling.

Common requested decoding controls: **temperature 0.7, seed 23, maximum output 340 tokens, no streaming, provider DeepInfra**. Qwen receives `reasoning.enabled=false` (no analogous Gemma switch). Provider honoring of seed and reasoning settings cannot be presumed. Actual model and provider identifiers, response IDs, token use and cost are saved for every call. Within-document model request order is alternated; case/role order is also balanced. Each call is isolated.

Total **48 billable calls** (24 per model), with a cumulative **USD 0.03 *observed cost* cutoff** checked after each response. It is *not* a hard pre-billing budget. A failed or truncated trial retains raw completed responses but is not scored as a complete experiment. No retry except limited 429 backoff.

## Scores specified before execution

For each model and each task, report:

- Primary: clauses with exact **verb root + two original-order argument stems and labels** (24 per condition).
- Secondary: correct individual arguments (48), exact stems (48), exact labels (48), invalid output format, label confusions, breakdown by the three licensed frame families (8 clauses each).
- Paired **model-agreement matrix** per task at the clause level: both correct, Qwen only, Gemma only, neither correct. Twelve two-sentence documents are the natural dependence groups, so individual clause counts must not be treated as independent general-population trials.
- Provider cost and input/output tokens **per model and task**, normalized USD per strictly correct clause (undefined on zero successful clauses).
- Preserve the raw responses and their SHA256, corpus SHA256, exact prompt hashes, verified machine rescoring and versioned files before analyzing the result.

No p-value or general model-families claim on 12 highly templated document clusters. A cross-model consensus failure is a higher-priority diagnostic for future **independently authored** sentences, but it can still arise from shared English glosses, annotation bias, similar training, or flawed machine-derived gold.

## Methodological rule for Unisermo experiments going forward

All subsequent **substantive LLM interpretation and comparative efficiency claims** should normally include *at least two architecture families*, use the same new stimuli and comparable decoding/response contracts, and report per-model outcomes rather than pooled accuracy alone. For final publication, two are a **minimum**, not sufficient independent validation: expand to a third model family if resources allow, independently adjudicate meaning keys, use a true frozen holdout, and include a reviewed controlled-English comparator and total communication costs. Model identifiers and dates must be fixed to avoid silent substitutions.

Existing conclusions from single-model runs remain recorded as such, not discarded or retroactively upgraded. No canonical edits, no holdout access, no human-approved semantic meanings claimed; new sentence review tally still **0/24**.

---

## Registered operational amendment — after first execution failed, before follow-up

**Run [40091590850](https://github.com/andreabenetton/unisermo/actions/runs/40091590850) did NOT complete the preregistered two-model trial.** It saved only **14/48** answers before OpenRouter/DeepInfra returned repeated **HTTP 429** on a Gemma request. More importantly, all **seven Qwen calls** among the 14 had `finish_reason=length` and **empty visible content**: disabling Qwen reasoning only via API `reasoning.enabled=false` without its prior `/no_think` prompt marker failed under this provider. These calls were billed and are **not semantically scored as evidence that Qwen cannot interpret Unisermo**. Gemma successfully returned valid content and `finish_reason=stop` on the other seven calls. The original failed artifact is `two-model-case-role-40091590850` (ID `12559033997`).

An attempted strict-prefix recovery job [40091922563](https://github.com/andreabenetton/unisermo/actions/runs/40091922563) *correctly rejected* the partial file because those Qwen completions were not successful. No new API calls were made by that job. The recovery script will not weaken this safety check or reinterpret empty Qwen responses as valid.

**Amended exploratory design (not equivalent to the preregistered identical-effective-prompt trial):** preserve the original **24 valid Qwen3 32B replies** from [run 40090842899](https://github.com/andreabenetton/unisermo/actions/runs/40090842899), which used the same frozen case/role questions and `/no_think` as a model-specific decoding control. Preserve the **seven valid Gemma replies** from run 40091590850 without rebilling, then execute just the remaining **17 Gemma requests** under the identical Gemma prompt/settings as those seven. Both model families therefore see the same task text and grammar reference, but Qwen has an additional model-specific nonthinking marker. It is **not literally the same effective prompt**. Compare per-model quality and errors descriptively; attribute no difference solely to learned linguistic competence.

The original preregistration above remains untouched and *must not* be rewritten as if the controlled trial succeeded. All conclusions from the salvaged comparison must be identified as **exploratory**, since the method was amended after observing the operational failures. Raw source artifacts, request hashes and all costs must be preserved. The existing frozen holdout and canonical language are still untouched.

New runner: `benchmarks/gemma_case_role_followup.py`; archive the resulting complete 24-answer Gemma set, original Qwen corpus and paired descriptive score as distinct, versioned evidence. Any future strong model-family conclusion requires **a newly preregistered** independent corpus with robust model-specific nonthinking controls and human-approved semantics.

---

## Interrupted Gemma follow-up (19/24) and exact resumption gate

The Gemma-only follow-up [run 40092124879](https://github.com/andreabenetton/unisermo/actions/runs/40092124879) **was cancelled at its 45-minute job timeout**, after completing 19 of 24 required Gemma answers. Its response JSONL was uploaded as artifact `gemma-case-role-followup-40092124879` (ID `12560587008`), even though there is **no complete score JSON**. A direct archive inspection confirmed **19 valid `finish_reason=stop` Gemma records**, last `CR010_role`, and cumulative recorded provider USD **0.00092784**. The runner encountered repeated DeepInfra HTTP 429; job completion must not be inferred from artifact upload alone.

A source-controlled resume implementation now validates the entire stored 19-response ordered prefix against the original frozen `gemma_plan()` (model, provider, response finish state, question identity and SHA-256 of prompt), and compares the first seven stored answers against the unchanged initial 14-response partial run. It refuses to overwrite or re-bill those 19. The remaining five Gemma requests are executed by [run 40097642521](https://github.com/andreabenetton/unisermo/actions/runs/40097642521) using the **same model and DeepInfra-only route**, preserving comparability with the first nineteen. The extra job does not retrospectively make the original failed 48-call same-prompt experiment a success. It is an explicitly amended follow-up with the already documented Qwen `/no_think` control difference.

Raw and scored files will be assessed only if Gemma reaches **24/24** with independently verified request IDs, response model/provider, SHA-256 of original/corpus, and recomputed paired scores. Historical failures are retained as first-class reproducibility evidence. No Unisermo language authority, corpus or holdout changes were made.

---

## Final completed exploratory two-family comparison — 24 October 2026

**Completed recovery and independently verified archival:** [GitHub Actions 40097642521](https://github.com/andreabenetton/unisermo/actions/runs/40097642521) restored the original **19 Gemma replies** and obtained the remaining **5**, yielding **24/24 valid Gemma calls**. [GitHub Actions 40097951414](https://github.com/andreabenetton/unisermo/actions/runs/40097951414) then verified the 19-record prefix byte-for-byte as JSON objects, exact request IDs/order, Qwen and Gemma returned model IDs, all DeepInfra provider IDs and `finish_reason=stop`, SHA-256, accumulated cost, and recomputed complete scores. It committed both original raw and score files into this research branch:

- [`benchmarks/evidence/gemma-case-role-2026-10-24-final.jsonl`](../../benchmarks/evidence/gemma-case-role-2026-10-24-final.jsonl); SHA-256 `9bfb0109399669d13dc3c0c307897bb64e1c33897989f809842dd0140e0012eb`.
- [`benchmarks/evidence/gemma-case-role-2026-10-24-final.score.json`](../../benchmarks/evidence/gemma-case-role-2026-10-24-final.score.json), containing the complete Qwen/Gemma agreement matrix, individual event predictions, per-family counts and billing.
- Original Qwen response file `benchmarks/evidence/case-role-2026-10-24-run40090842899.jsonl` SHA-256 `c55cd847cd2522f8857432e0121c990f39064a78335fccd5e5fa28e9430695e6`. The unchanged source corpus SHA-256 is `0d8c6a10f7cb8b4545654208af9cfbf8af65f870b0e2e6334c7adc9e6df4a1fb`.

**This is an amended exploratory comparison, NOT completion of the initially preregistered strict byte-identical two-model experiment.** Both model families completed the same original 12 documents × two labeling conditions, but Qwen from its earlier successful run included the model-specific `/no_think` control suffix and the responses were gathered in different runs; Gemma's model requests were pinned to DeepInfra while Qwen's actual provider was DeepInfra via automatic routing. Conclusions must preserve this distinction and cannot be described as an isolated model architecture experiment.

### Exact registered-style scores on the unchanged development corpus

| Metric | Qwen3 32B, case | Gemma3 27B, case | Qwen3 32B, role | Gemma3 27B, role |
| --- | ---: | ---: | ---: | ---: |
| **Exact two-argument clauses** | **16/24** | **8/24** | **15/24** | **7/24** |
| Arguments with both stem and label correct | 35/48 | 24/48 | 39/48 | 22/48 |
| Exact stems | 38/48 | 32/48 | 43/48 | 32/48 |
| Exact labels | 37/48 | 37/48 | 44/48 | 38/48 |
| JSON envelope/cardinality failures | 0/12 | 0/12 | 0/12 | 0/12 |
| Prompt tokens | 4,208 | 4,233 | 4,160 | 4,209 |
| Completion tokens | 1,531 | 1,608 | 1,474 | 1,521 |
| Total tokens | 5,739 | 5,841 | 5,634 | 5,730 |
| Provider USD | 0.00076532 | 0.00059592 | 0.00074552 | 0.00058008 |
| USD per exact clause | 0.0000478325 | 0.0000744900 | 0.0000497013 | 0.0000828686 |

Across **both conditions** (two tasks on the **same** twenty-four clauses), Qwen obtained **31/48** strict clause-task successes vs Gemma **15/48**. This is not 48 independent natural-language texts. Model provider cost across the two conditions was Qwen **USD 0.00151084**, Gemma **USD 0.00117600**; do not treat lower gross Gemma API cost as lower communication cost at equivalent accuracy.

### Which meanings were recovered by each model?

| Outcome among same 24 clauses | Morphological case task | Semantic role task |
| --- | ---: | ---: |
| Both models correct | **8** | **5** |
| Qwen only | 8 | 10 |
| Gemma only | 0 | **2** |
| Both wrong | 8 | 7 |

| Canonical frame family (8 clauses each) | Qwen case | Gemma case | Qwen role | Gemma role |
| --- | ---: | ---: | ---: | ---: |
| Motion with explicit allative destination | 7 | 4 | 5 | 7 |
| Noncausative `traes` transition (`-ad/-de`) | 1 | **0** | 4 | **0** |
| Causative `traes` result (`-em/-da`) | 8 | 4 | 6 | **0** |

The strongest **common concern** is the noncausative two-state `traes` representation. Even when the model is explicitly told its case/role guide, neither family is consistently accurate on the transition frame; Gemma scored 0/8 in both variants, Qwen 1/8 and 4/8. Yet source-defined case/role labels and complete clause naturalness still await independent linguistic validation. Shared confusion does not uniquely distinguish language ambiguity from incorrect gold, prompt effects, insufficient training exposure, or the task's arbitrary ontology.

In the **movement-role** task, Gemma scored 7/8 vs Qwen's 5/8; aggregate Qwen superiority therefore does not translate to every construction. Two role-annotation clauses were solved only by Gemma. Preserve these as potentially informative counterexamples rather than optimizing exclusively for the best overall model.

### Research decision

- Adopt [two-family evaluation policy](../methodology/multimodel-evaluation-policy.md) for new substantive semantic/LLM efficiency studies. This comparison provides useful **cross-model failure diagnostics**, not independently validated Unisermo understanding.
- No change to accepted Unisermo morphology, case names, phonology, pronouns, lexicon, `traes` semantics or syntactic authority.
- Retain 0/24 **human-approved** new case/role keys. Their adjudication, naturalness/valency validation and then a controlled English-equivalent comparison are prerequisites for any publication-grade language efficiency conclusion.
- Later tests require genuinely new independent stimuli, prior registration, robust model-specific control handling, an untouched final holdout and, preferably, a third model family. Preserve *all* original failed jobs (14/48, 19/24) and their partial evidence instead of silently replacing them with completed results.
