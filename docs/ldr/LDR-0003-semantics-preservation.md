---
id: LDR-0003
title: Preserve accepted semantics during LLM optimization
status: Accepted
date: 2026-10-22
domain: compatibility
supersedes: none
---

# LDR-0003 — Preserve accepted semantics during LLM optimization

## Context and problem

A compact candidate can lower token count while changing tense, aspect,
reference, negation scope, argument roles, or degree of certainty. The Phase 1
formalization is intended to model the current language, not to redesign it.

## Alternatives

- Replace canonical forms during formalization (risk: regression without a
  stable baseline).
- Keep the accepted language stable; test opt-in profiles separately and
  require explicit review for incompatible changes (selected).

## Decision or hypothesis

Preserve all currently confirmed Unisermo forms and semantic distinctions while
establishing the formal reference baseline. Candidate LLM profiles and compact
spellings are **non-normative experiments** until demonstrated equivalent and
explicitly accepted in a separate LDR. Where the grammar genuinely permits
multiple readings, the parser must preserve alternatives or reject unsupported
input rather than invent a single interpretation.

## Evaluation and evidence

Round-trip morphological tests, scoped negative tests, source-linked examples,
meaning-pair judgments and controlled task success must precede optimization.
All parser-supported constructs must have documented limitations; the reference
parser must fail closed on input outside its supported subset.

## Consequences and compatibility

Optimization may be slower, but measurements will compare against a stable
baseline. Historical files and the GlottoDelta atlas snapshot remain untouched.

## Decision authority

Accepted as a preservation and implementation invariant for the approved Phase 1
formalization, not as approval of any new lexical or grammatical form.

## References

- `language/verb_specification.md`
- `language/noun_case_system.md`
- `formalization/data/morphology.json`
