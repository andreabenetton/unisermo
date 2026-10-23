# Productive-compound OpenRouter pilot — 2026-10-23

**Status: Qwen complete; Gemma incomplete. Canonical vocabulary unchanged.**

The bounded one-shot [GitHub Actions run](https://github.com/andreabenetton/unisermo/actions/runs/39905757760) used the 12-component experimental set in `research/lexicon/productive-compound-trials-001.json`. Each compound was requested in three isolated conditions: cold (no help), rule-only (transparent linker-free concatenation), and root dictionary (rule + explicit component meanings). No answer key was shown.

## Confirmed results for Qwen3 32B (DeepInfra)

| Condition | Valid machine-readable output | Correct ordered two-root segmentation | Input tokens | Output tokens | OpenRouter reported cost |
| --- | ---: | ---: | ---: | ---: | ---: |
| cold | 12/12 | **9/12** | 564 | 427 | $0.00016468 |
| rule-only | 12/12 | **10/12** | 768 | 364 | $0.00016336 |
| dictionary | 12/12 | **12/12** | 1,632 | 340 | $0.00022576 |
| **Total** | **36/36** | **31/36** | **2,964** | **1,131** | **$0.00055380** |

Raw responses plus JSON mechanical score in artifact `compound-qwen-39905757760`, ID `12481116156`. The strong improvement in segmentation with supplied roots is an initial practical signal for reusable compositional grammar, **not** demonstrated semantic understanding: the free-text glosses are recorded but not independently graded. Examples of incorrect no-gloss predictions included `kurarager` guessed as silly behavior and `bastrak` interpreted as cover + go. No canonical changes.

**Dictionary cost accounting:** the full root dictionary was repeated independently in all 12 requests, so the figures above are **repeated primer cost**, *not* a measured amortized one-time conversation. The summed tokens cannot be interpreted as performance after a model has memorized the language across requests.

## Gemma 3 27B: incomplete

Gemma stopped at OpenRouter **HTTP 429 for C010** after **9** completed cold-condition calls, including two bounded retry delays. The workflow saved all nine actual responses to artifact `compound-gemma-39905757760`, ID `12480183543` (no full-score JSON). They incurred approximately **$0.00023384** in provider-reported cost. **No cross-condition Gemma comparison is legitimate** for this run.

At least one Gemma response contained a fenced JSON answer *followed by explanatory prose*, with `finish_reason=length`; the strict scorer does not silently scrape embedded JSON from mixed prose. This is an additional output-format limitation requiring a separately declared policy, not evidence about segmentation accuracy.

## Interpretation and next steps

The initial Qwen result supports further investigation of transparent compounds: given a root glossary, the model correctly identifies the component boundaries even if it cannot recover every compound from cold spelling. This does **not** prove easier human acquisition, globally lower token cost, or one unique intended meaning.

Next tests should use an actually persistent model context with one-time priming, isolated sessions per condition, context-order controls and equivalent accounting of shared tokens; compare with repeated independent roots. Retry Gemma only after confirming provider rate-limit capacity and a predictable response-format policy; do not automate an unbounded retry loop. The deferred human spoken/written evaluation remains tracked in GitHub issue #3.

Source: `benchmarks/compound_inference.py`, `benchmarks/compound_inference_runner.py`, `research/lexicon/compositionality-evaluation-protocol.md`.
