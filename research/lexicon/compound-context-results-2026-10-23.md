# Unisermo compound primer: repeated dictionary vs multi-turn context (2026-10-23)

**Completed real OpenRouter run**: https://github.com/andreabenetton/unisermo/actions/runs/39906292907

Qwen3 32B, 12 previously registered compounds, two conditions (24 calls total). This experiment is bounded, research-only, and leaves all canonical entries unchanged.

| Metric | Isolated repeated glossary | Multi-turn full-history conversation |
| --- | ---: | ---: |
| Actual requests | 12 | 12 |
| Strict valid JSON | 12 | 12 |
| Exact two-component segmentation | 12 | 12 |
| Input tokens billed | 1680 | 5916 |
| Output tokens billed | 296 | 266 |
| Total tokens billed | 1976 | 6182 |
| Provider reported cost (USD) | 0.00021728 | 0.00054776 |

Multi-turn costs 2.52x as much USD and 3.13x total billed tokens as isolated repeated-root-glossary prompting for the twelve-word sequence at this model/provider. Note multi-turn output was slightly shorter; cost increase arose from input history.

### Method and interpretation

- Baseline: one new isolated request per word, with a compact system root dictionary and composition rule each time.
- Multi-turn: one initial system root dictionary followed by twelve consecutive user requests, with each preceding assistant reply appended. The **full history is sent to OpenRouter on every API call**. This is context retention, not fine-tuning or permanent learned memory.
- The Qwen runner was corrected to preserve the entire messages array when adding its non-thinking directive to the final user request.
- We did not request nor verify prompt caching; no amortized cache discounts are assumed.
- Both strategies achieve 12/12 segmentation, but this is a narrow deterministic metric. Gloss meaning/ambiguity is not independently semantically graded.
- The twelve compounds are a mix of three already canonical and nine synthetic experimental expressions; no synthesis of independent conventional meanings is justified.
- Both conditions were tested in fixed sequence (baseline followed by conversation), with one model/provider and without randomized order or repeated seeds. Results are preliminary, not statistically generalizable.
- A compressed persistent system instruction plus *only the current question* would resemble the baseline, not a true multi-turn retained conversation. A model-side persistent cache or hosted fine-tuning is a distinct engineering approach whose cost must be measured separately.

Artifacts: `compound-context-qwen-39906292907`, GitHub Actions artifact ID `12480836794`, includes real answers and score JSON. Code: `benchmarks/compound_context_runner.py`, shared `benchmarks/openrouter_runner.py`.

**Design takeaway:** preserve productive word composition for human/systematic language economy, but avoid assuming accumulated stateless API chat history is cheaper than repeating a modest static primer. The more relevant optimization is a *minimal reusable grammar+lexicon header*, selected/compressed according to the task, and an empirical cold-start-vs-primed inference study on unseen compounds. Human evaluation remains deferred in issue #3.
