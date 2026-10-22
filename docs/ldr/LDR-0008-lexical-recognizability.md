---
id: LDR-0008
title: Contemporary recognizability and lexical economy
status: Experimental
date: 2026-10-22
domain: lexicon
supersedes: none
---

# LDR-0008 — Lexical recognizability and economy

## Context and problem
Latin origin is useful only when modern speakers can recognize a related word in its intended meaning. High-frequency concepts should tend to receive shorter forms. Shorten roots where distinctness and readability survive.

## Alternatives
Retain etymologically closest Latin forms; minimize written length only; or measure modern recognizability, frequency, collision risk and token cost. Choose the last as an experimental method.

## Decision or hypothesis
Extend experimental LDR-0002 with frequency-length fitness F and collision risk C:

S(w) = alpha R(w) + beta P(w) + gamma T(w) + delta U(w) + epsilon F(w) - zeta C(w)

Weights and metric scales remain unset. Severe semantic, grammatical or pronunciation collisions disqualify candidates regardless of score. Frequency concerns modern meaning across spoken, written and technical communication, not ancient Latin word frequencies.

## Evaluation and evidence
Use https://kaikki.org/dictionary/Latin/index.html for Latin etymons and Wiktextract for documented modern lexical relatives. Dictionary presence is not speaker recognition or usage frequency. Measure multilingual current corpora and compare actual recognizability, phonotactics, full paradigms, near-collisions under accepted accent mergers, and tokenizer segmentation in semantically equivalent sentences. Preserve uncertainty and an unseen holdout.

## Consequences and compatibility
No canonical root is changed. Each accepted root change requires independent semantic checks, evidence and an additional approved LDR.

## Decision authority
User's guiding principles are recorded; numerical scores and root substitutions are not approved.

## References
- docs/ldr/LDR-0002-lexical-efficiency-scoring.md
- language/vocabulary_design_rules.md
- research/lexicon/confirmed_lexicon.json
