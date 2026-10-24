# Semantic contrast pilot — preregistered development protocol (2026-10-24)

**Status at authoring: protocol fixed, no Qwen results used to choose these questions.** This is the next stage after schema repeatability in PR #5. It makes no changes to Unisermo grammar, spelling, lexicon or syntactic authorities.

## Motivation and narrow scope

The previous paired-schema experiments only tested recovery of eight grammatical slots from generated SVO clauses. Their aggregate performance did not establish that a model understood distinctions such as source vs destination, accompanying vs benefiting, universal quantification vs totality, spatial deixis, or caused vs spontaneous state transition.

The existing `formalization/parser/clause.py` handles a small SVO subset, not these broader semantic constructions. Rather than making a silently expanded parser, this pilot uses 30 **attested normative expressions**, contrasted two at a time, each accompanied by a targeted question in controlled English. The source file for every expression is recorded in `benchmarks/corpus/semantic-contrast-dev-001.jsonl` and checked programmatically. Such checks attest **wording**, not independent correctness of the researcher-authored meaning key.

This task can discriminate some semantic relations but remains a **forced-choice closed-form translation/entailment proxy**. It does not test conversational coreference, multi-sentence dialogue, or full discourse understanding. The presence of two expressions in an item does not make it a multi-clause text. `Y` in the examples is the explicit schematic agent variable already appearing in canonical documentation, not a new Unisermo word.

## Sample / balances

Exactly 30 development-only probes:

| Family | Questions |
| --- | ---: |
| Case and case-role distinctions | 6 |
| Analytic relators | 6 |
| Quantification and explicit quantity | 6 |
| Deixis and possessive reference | 6 |
| State transitions and focus/negation | 6 |

Each example is built out of **two examples already found in source specifications**. Key labels are balanced: 15 A, 15 B. Source citations and expected responses remain in the data file; they must never be sent to the tested model. Models receive only the expression pair and question, plus optional short guide.

## Conditions / hypothesis

Use a paired design, one isolated request per document and condition:

- **cold:** meaning selection without any grammatical or lexical primer.
- **guided:** the **same question and answer protocol** plus a short reusable normative reference guide (case/relator/quantifier/deixis/transition/focus summary and essential glosses), its full overhead charged on every request.

**Hypothesis:** the guide increases semantic choice accuracy in unfamiliar contrasts, potentially at additional prompt-token cost. The experiment is exploratory; no result from it will be treated as a general language-efficiency claim.

Outputs are required to be JSON objects of exactly `{"choice":"A"}` or `{"choice":"B"}`. Any invalid JSON, non-A/B choice, extra keys, or incomplete response is a format failure and is counted incorrect, with the error class retained. Scoring does not strip or reinterpret a wrong answer into a correct one.

## Model, budget and reporting

- Model request: `qwen/qwen3-32b` on OpenRouter using the existing `benchmarks.openrouter_runner.invoke`.
- Endpoint/client as implemented: non-thinking, `temperature=0.7`, `seed=23`, no provider fallback; actual response/provider IDs saved. Providers may ignore a supplied seed.
- 30 × 2 = **60 requests maximum**, `max_output=130` tokens per request; cumulative provider-reported spending stop at **USD 0.04** (reject missing or invalid cost). Execution begins only under an explicit once-only GitHub Actions commit marker.
- Persist every billable response and token/cost metadata immediately. On failure, the raw partial artifact is preserved but is **never scored or presented as a complete experiment**.
- Metrics: per-condition exact-semantic-choice accuracy, per-family score, JSON failures, discordant paired outcomes, input/output tokens, provider reported cost, USD per correct choice.
- Do not interpret 30 questions as independent observations from natural use; closely related minimal-pair examples exist. No statistical significance/p-values or confidence interval from a naive iid assumption. Compare counts descriptively.
- Preserve raw outputs, prompt digests, code commit and corpus SHA-256. Archive original artifact to a versioned evidence file only after confirming full call count and costs.

## Scientific limitations and decision criteria

- Source phrases are canonical *examples*, but their semantic answer keys were assigned by the experiment author, **pending independent bilingual review**.
- The English wording itself may cue the correct answer, making this partly a lexical/metalanguage competence task.
- A guide that explains a rule can help decode that rule but does not establish intuitive comprehension of unseen prose.
- Holdout is not touched and these 30 development items are permanently marked as seen after the run.
- If guided has higher accuracy, compare extra input tokens and USD per correct choice; do not equate lower token count with better communication efficiency.
- Before any generalization, extend to **complete multi-clause texts** that are independently authored/reviewed, specify reference resolution, and validate case/valency syntax. Do not invent new canonical anaphora or infer quantified scope where the canon leaves interpretation contextual.
- Neither good nor poor results automatically authorize any change to Unisermo.

---

## Execution and observations — completed 2026-10-24

This section appends measured results **after** the preregistered study. It does not rewrite the planned outcomes or change the source corpus.

- [GitHub Actions experiment 40083465724](https://github.com/andreabenetton/unisermo/actions/runs/40083465724), successful 60/60 calls, artifact `semantic-contrast-40083465724`, ID `12555329023`.
- [GitHub Actions evidence-archive verification 40083656533](https://github.com/andreabenetton/unisermo/actions/runs/40083656533), successful hash/model/provider/cost/rescoring verification.
- Permanently retained original responses: [`benchmarks/evidence/semantic-contrast-2026-10-24-run40083465724.jsonl`](../../benchmarks/evidence/semantic-contrast-2026-10-24-run40083465724.jsonl).
- Original derived score: [`benchmarks/evidence/semantic-contrast-2026-10-24-run40083465724.score.json`](../../benchmarks/evidence/semantic-contrast-2026-10-24-run40083465724.score.json).
- Raw JSONL SHA-256: `5d0e6668fcc18b305f9bf37c49634277a51cfcf0a8a04576619ccf520c252e4f`.
- Corpus SHA-256: `b80c9a7380b4f3563de9b2b48863c3b32bce6b8ae3bd9e89848f10d230de0b32`.

The 60 API calls requested and received `qwen/qwen3-32b`, all 60 reported provider `DeepInfra` and `finish_reason=stop`; no invalid JSON formats or incomplete responses. Reported temperature/seed are request controls, not a guarantee that the provider executed them deterministically.

| Metric | Cold | Guided |
| --- | ---: | ---: |
| Semantic choices correct | **25/30 (83.33%)** | **27/30 (90.00%)** |
| Prompt tokens | 2,611 | 12,811 |
| Completion tokens | 270 | 270 |
| Total tokens | 2,881 | 13,081 |
| Provider-reported USD | 0.00028448 | 0.00110048 |
| USD per correct choice | 0.0000113792 | 0.0000407585 |
| Incorrect format responses | 0 | 0 |

Full run total **15,962 tokens**, **USD 0.00138496**, below the USD 0.04 stop bound. The guide improved the raw count by two choices, but generated **10,200 additional input tokens** and increased provider USD per correct choice by ~**3.58×**. The guided arm had about **4.54×** the total token use and **3.87×** the gross API bill of cold. All cost comparisons are for this exact dataset and model pricing, not English-vs-Unisermo comparisons.

### Family-level results

| Development family (6 each) | Cold | Guided |
| --- | ---: | ---: |
| Case/source/location/resultative | 4 | 6 |
| Analytic relators | 6 | 6 |
| Quantification | 6 | 6 |
| Deixis/possession | 3 | 5 |
| Transition/focus | 6 | 4 |
| **Total** | **25** | **27** |

Paired outcomes: **23** questions correct in both conditions, **4** only with guide, **2** only without guide, **1** incorrect in both. Discordant IDs are `SC002, SC004, SC020, SC024` (guided helped) and `SC026, SC029` (cold only); `SC022` was wrong in both.

A noteworthy **post-hoc potential response-position bias**: all five cold failures have `expected_choice=B` and the model returned `A`. As the keys were exactly balanced 15 A/15 B, the cold responses selected A twenty times and B ten times. In the guided arm, two failed B questions were answered A, and one failed A question was answered B. This positional tendency, the highly similar minimal pairs, and the deliberate fixed prompt format confound a purely semantic explanation of the gains. It should be investigated by mirroring A/B presentations on **new development items**, not by treating these exposed examples as a new validation set.

### Interpretation and scientific decision

**Do not promote a schema, change any Unisermo canonical rule, or infer superior general LLM communication efficiency.** The guide produced a small increase in score in exchange for a substantially larger total token cost; no statistical inference is claimed from these related, author-keyed 30 items. It is also not evidence that a model understands dialogue-level reference. Retain the negative result for the scientific paper.

**Next distinct stage (not executed here):** independently review semantic keys and produce compositional **complete sentences / discourse** with explicitly tracked subject/object identity, relational roles, quantity/scope and reference. Where multi-clause syntax or anaphora is not canonically defined, separate the unresolved grammar design question from the evaluation and do not create a fictitious gold answer. Compare prompt cost per correct *meaning-bearing proposition*, ideally also against concise controlled English with independently checked equivalence. The current 30 probes must remain marked as used development.
