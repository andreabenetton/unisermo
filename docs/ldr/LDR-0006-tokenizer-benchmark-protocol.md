---
id: LDR-0006
title: Establish exploratory tokenizer benchmark protocol
status: Experimental
date: 2026-10-22
domain: llm-efficiency
supersedes: none
---

# LDR-0006 — Exploratory tokenizer benchmark protocol

## Context and problem

Tokenization efficiency may differ dramatically from linguistic concision.
Before changing Unisermo roots or morphology, we need reproducible measurements
that do not conflate byte length, token count and LLM comprehension. The
Phase 1 morphology corpus is not a semantically validated translation corpus.

## Alternatives

1. Estimate tokens from characters/words: rejected as misleading for BPE tokenizers.
2. Measure only single isolated inflections: insufficient contextual evidence.
3. Develop a controlled parallel pilot of phrases, require real tokenizer
   implementations, and mark all translations unreviewed until independently
   validated (selected for exploratory work).
4. Immediately fine-tune a model: premature without semantic and tokenizer baselines.

## Decision or hypothesis

Implement a **research-only** deterministic paired-input benchmark under
`benchmarks/`. Start with a small synthetic morphology-heavy corpus whose
Unisermo clauses pass the reference parser. Include precise English draft
counterparts, lexical attestation, intended grammar, and a split field.
Never substitute bytes, letters or whitespace pieces for model token counts.
Evaluate UTF-8 exactly as written, including punctuation and whitespace.
No language rules, weights from LDR-0002, or vocabulary are modified.

## Evaluation and evidence

Count tokens from real tokenizer versions (`tiktoken` o200k_base / cl100k_base,
local SentencePiece .model, or HF tokenizer.json). Record tokenizer identifier,
package version, vocabulary file SHA256 where applicable, corpus SHA256,
per-row counts and grouped totals. Percentage input-token reduction is
`100*(1 - sum(Unisermo tokens)/sum(English tokens))` on a fixed sample, when
English token totals are nonzero. No statistical inference on a synthetic
pilot. Do not search over the holdout split when selecting candidates.

Require separate human translation review and meaning-preservation checks
before using the counts as evidence of language superiority. For future task
experiments, measure response accuracy, initial instruction overhead,
retry costs, output tokens, latency, and model/version information.

Falsification: if real tokenizer counts show no savings or English controlled
prose is more efficient, report that result without modifying the corpus.

## Consequences and compatibility

A machine-runnable benchmark is available independently of paid model APIs,
but initial results are not valid evidence of semantic parity. Missing
external tokenizers produce explicit errors, never invented token counts.
The preliminary corpus is narrow and requires broader texts, independent
review, and real model evaluations in later iterations.

## Decision authority

Experimental methodology, not an approved language change. The project owner
approved beginning Phase 2; corpus translations, tokenizers, and any
conclusions remain subject to review. This LDR records implementation and
hypothesis, not acceptance of a numeric efficiency claim.

## References

- `docs/ldr/LDR-0002-lexical-efficiency-scoring.md`
- `docs/ldr/LDR-0003-semantics-preservation.md`
- `benchmarks/README.md`
- `benchmarks/run.py`
- `benchmarks/corpus/pilot.jsonl`

## Implementation note — 2026-10-22

The official [`openai/tiktoken`](https://github.com/openai/tiktoken) package
was identified as the reference implementation for the initial OpenAI encoder
measurements, and the installation is pinned to PyPI version `0.14.0` in
`benchmarks/requirements-openai.txt`. `o200k_base` and `cl100k_base` can be
measured together using `python -m benchmarks measure-openai --include-draft`.
The benchmark records a reproducible SHA-256 of the encoder's actual BPE merge
ranks (using an internal `tiktoken` attribute **only to fingerprint the ranks**).
For comparability across future library releases, the package version and
fingerprint must both be retained. A workflow exists for later opt-in execution
on GitHub Actions, but no GitHub remote is configured for Unisermo and no
remote benchmark has yet been run.

The current execution environment could not install the official package due
to lack of network access; therefore **there are no genuine OpenAI token-count
results in this archive**. This note documents implementation status, not a
change to the experimental hypothesis or acceptance of efficiency claims.
