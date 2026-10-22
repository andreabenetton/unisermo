---
id: LDR-0007
title: Preserve measured tokenizer baseline and define diagnostic review
status: Experimental
date: 2026-10-22
domain: llm-efficiency
supersedes: none
---

# LDR-0007 — Tokenization diagnostic baseline

## Context and problem

The first GitHub Actions pilot completed on 2026-10-22, run 39832551377,
commit `9dc3e6c6d07d672a02328ee10d5a287ecea21a15`. Its artifacts contain
78 paired-input observations using official `tiktoken:0.14.0` tokenizers. The
corpus has 64 finite paradigms, nine object clauses and five operator clauses;
English renderings remain unreviewed. A raw total alone is misleading.

## Alternatives

1. Declare Unisermo superior from aggregate counts — rejected; biased sample,
   unreviewed bilingual equivalences and absent model tests.
2. Change roots and suffixes immediately — rejected; the holdout and tokenizer
   differences make this premature.
3. Archive original measured reports; generate a repeatable per-example and
   per-group diagnostic; audit translations before extending claims — selected.

## Decision or hypothesis

Preserve the immutable original report JSONs under `benchmarks/evidence/` with
GitHub run provenance. Add `benchmarks/diagnostics.py`, rejecting reports whose
SHA-256 corpus fingerprint or row IDs differ from the current pilot. Rank
examples **only on the development split**. Use the holdout strictly for an
aggregate readout; never rank it to choose revised spellings.

The program identifies probable review issues but **cannot** certify semantic
equivalence. Token-segmentation claims must be backed by a real tokenizer:
report-level token totals cannot reveal internal BPE merges. Add optional
`--segment-openai` to record actual token IDs and decoded token bytes when
`tiktoken` and its vocabulary files are available.

## Evaluation and evidence

GitHub Actions: https://github.com/andreabenetton/unisermo/actions/runs/39832551377

The archived `o200k_base` report measures 315 English vs 281 Unisermo input
tokens, reduction 10.794%. The archived `cl100k_base` report measures 315
English vs 319 Unisermo, reduction -1.270%. These numbers describe only this
pilot corpus, not general-language efficiency.

The group differences indicate why aggregate claims are unstable: finite
paradigms account for 64/78 pairs. On o200k the nine SVO pairs cost six extra
tokens relative to English, while five operator examples cost two extra.
On cl100k the respective penalties are nine and eleven tokens. These groups
must be expanded before linguistic changes are assessed.

## Semantic audit and expansion plan

Review all 78 draft equivalences for agent/number, aspect, time reference,
referents, article/definiteness, modality, negation and scope; have a reviewer
sign off individual pairs. English `you` is number-underdetermined, for
example, and explicit pronouns may not preserve the same pragmatics as pro-drop.
Archive approvals separately; do not change `review_status` to
`human_verified` automatically.

Target a second, **balanced and independently reviewed** corpus of 1,000 pairs
before producing a general comparison:

| Category | Target |
| --- | ---: |
| Basic clauses with objects | 180 |
| Negation, questions, operators, conditionals | 150 |
| Temporal and aspectual contrasts | 150 |
| Reference, case, number and quantification | 140 |
| Dialogue and pragmatic context | 120 |
| Technical and multi-agent communication | 160 |
| Complex discourse and ambiguity controls | 100 |
| **Total** | **1000** |

These are proposed quotas, **not** newly generated examples. New pairs must
pass parser validation where supported; parser success is not translation
approval. Use a frozen evaluation set for model comprehension and an unseen
holdout before tuning. Compare against controlled/concise English as well as
ordinary English, and count instruction overhead and correction attempts.

## Falsification and limitations

Any result that fails after translation review or on a balanced unseen set
must be reported, not selectively excluded. The pilot cannot measure model
accuracy, inference costs or statistically significant advantage.

## Consequences and compatibility

No changes to canonical morphology, spelling or lexical roots. Future proposals
may cite this baseline but need separate experimental LDRs before adoption.

## Decision authority

Research-only diagnostic extension of the owner-approved Phase 2. Neither
results nor corpus quotas represent approved language-design changes.

## References

- `docs/ldr/LDR-0006-tokenizer-benchmark-protocol.md`
- `benchmarks/evidence/`
- `benchmarks/diagnostics.py`
- `benchmarks/reports/diagnostic-pilot.json`
