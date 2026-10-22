---
id: LDR-0004
title: Migrate normative rules to machine-readable sources
status: Proposed
date: 2026-10-22
domain: formalization
supersedes: none
---

# LDR-0004 — Migrate normative rules to machine-readable sources

## Context and problem

The current source of truth is `language/` together with confirmed decisions
in `research/`. Independent JSON and prose editing can introduce drift.
Machine-readable rules would permit deterministic generation, validation and
corpus construction, but premature migration might drop linguistic nuance.

## Alternatives

- Keep all norms in Markdown indefinitely; add checkers only.
- Immediately declare JSON normative and replace prose (risk: lost constraints).
- Build a source-linked executable **mirror**, then migrate rule by rule after
  parity and explicit acceptance (recommended, but not yet ratified).

## Decision or hypothesis

Propose a staged migration: document normative provenance; generate indexes and
regression tests from existing decisions; for each proven-equivalent rule,
explicitly approve its structured source of truth and regenerate or
cross-check prose. Until that approval, the live Markdown plus confirmed
research records remain normative; executable subsets are derived mirrors.

## Evaluation and evidence

Track each proposed migrated rule by source ID/hash, examples, coverage and
parity tests. Identify anything not encoded (scope, allomorphy, derivation,
syntactic alternation). A changing JSON value without a corresponding approved
LDR and specification update is a validation failure, not a silent migration.

## Consequences and compatibility

Prevents two competing silent authorities. Full migration remains an open
architectural choice requiring additional approval and better coverage.

## Decision authority

Proposed for future review; not accepted and not permission to rewrite the
existing specification automatically.

## References

- `language/README.md`
- `research/grammar/confirmed_decisions.json`
- `formalization/data/morphology.json`
