---
id: LDR-0002
title: Explore multi-objective lexical efficiency scoring
status: Experimental
date: 2026-10-22
domain: llm-efficiency
supersedes: none
---

# LDR-0002 — Explore multi-objective lexical efficiency scoring

## Context and problem

Unisermo selects Latin/international lexical roots while optimizing human
recognizability and pronounceability. A form that is short in characters may
require more model tokens than a longer but familiar form. Token count alone
may also reward ambiguous or poorly understood expressions. The project owner
requested that the multi-objective proposal from the design discussion be
formalized rather than left as an undocumented heuristic.

## Alternatives

1. Choose the shortest written word (reject as an evaluation method: characters
   are not tokenizer tokens).
2. Minimize token count alone (insufficient: meaning, pronunciation and model
   comprehension can deteriorate).
3. Use a symbolic weighted multi-objective score, subject to semantic and
   linguistic constraints (the experimental hypothesis).
4. Use a Pareto frontier or hard-threshold constrained optimization instead of
   a scalar score (valid control alternative for evaluation).

## Decision or hypothesis

Test the following **proposed** scoring function; it is **not** a canonical
lexical selection rule:

\[
S(w) = \alpha R(w) + \beta P(w) + \gamma T(w) + \delta U(w)
\]

`w` denotes a *candidate expression of a fixed intended meaning in context*,
not an arbitrary word divorced from its syntax. All component directions are
chosen so larger means better:

- `R(w)`: recognizability across target human-language populations.
- `P(w)`: pronounceability under the accepted Unisermo phonology.
- `T(w)`: tokenizer efficiency across specified model/tokenizer families for
  *semantically equivalent full expressions*; never infer from character count.
- `U(w)`: semantic unambiguity / comprehensibility, measured separately for
  human readers and LLMs where feasible.

`alpha`, `beta`, `gamma`, and `delta` are **unset**. The functions' measurement
scales and normalization ranges are **unset**. No numerical optimum or claimed
percentage improvement currently follows from this equation. A scalar score
must never compensate for a failed semantic-fidelity or phonotactic constraint.

## Evaluation and evidence

- Before scoring, define comparable intended meanings and context, coverage of
  inflected paradigms, tokenizer versions, model versions, and representative
  target language populations.
- Require semantic-fidelity and phonotactic gates. Report raw component
  measurements before any normalization or weighting.
- On disjoint development and held-out corpora, compare weighted-score
  selection to a Pareto approach and to current canonical forms.
- Measure full task cost (input tokens, instructions, output tokens, error and
  retry rate), not just a tokenizer's segmentation of isolated words.
- Estimate weights via an explicitly documented calibration set and sensitivity
  analysis; reserve the held-out set for validation.
- Falsify the hypothesis if gains in token count disappear after counting
  instructional overhead or if comprehension/meaning preservation worsens.

## Consequences and compatibility

All existing Unisermo roots remain unchanged. Scoring is research-only until
specific component definitions, corpus, weights, and outcome evidence are
published and a later LDR accepts a lexical change. Tokenizer-specific gaming
must not undermine human usage or other models.

## Decision authority

Experimental only. No lexical scoring weights or resulting root choices have
been approved as normative as of 2026-10-22.

## References

- `language/vocabulary_design_rules.md`
- `research/lexicon/confirmed_lexicon.json`
- `docs/ldr/LDR-0003-semantics-preservation.md`
