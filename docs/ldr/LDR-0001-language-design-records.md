---
id: LDR-0001
title: Adopt Language Design Records
status: Accepted
date: 2026-10-22
domain: governance
supersedes: none
---

# LDR-0001 — Adopt Language Design Records

## Context and problem

Unisermo has a long research history, confirmed rules in JSON, mutable live
Markdown specifications, and design arguments that previously remained in chat
threads. Merely preserving the current answer loses the competing options,
assumptions and reasons that led to it.

## Alternatives

- Keep only decisions in `research/*/confirmed_decisions.json`: compact, but
  omits context, rejected alternatives, and test requirements.
- Use an unstructured design journal: easy to write, hard to search or validate.
- Use ADR-like Language Design Records (selected): immutable IDs, status,
  reasoning, testability and traceability.

## Decision or hypothesis

Use version-controlled **Language Design Records (LDRs)** for consequential
linguistic or model-efficiency design decisions and experiments. A record is
required before an experimental optimization is promoted into the language
canon. An LDR does **not** replace the reference grammar or lexicon.

## Evaluation and evidence

Enforce filename/ID uniqueness, lifecycle status, consistent frontmatter and
source-path integrity. Keep a generated index. A proposed or experimental LDR
must not itself change accepted morphology, syntax or lexical forms.

## Consequences and compatibility

Research decisions become reviewable and durable. This introduces a small
writing/validation cost. Existing confirmed decisions retain their original
status and source; no retrospective approval narrative is invented.

## Decision authority

Accepted as a project-process convention following the project owner's explicit
request on 2026-10-22 to formalize discussion reasoning with ADR-style LDRs.

## References

- `docs/ldr/README.md`
- `research/grammar/confirmed_decisions.json`
- `research/phonology/confirmed_decisions.json`
