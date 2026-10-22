# Unisermo Language Design Records (LDRs)

Language Design Records preserve *why* Unisermo adopts or tests a choice. They
are inspired by Architecture Decision Records (ADRs), but cover phonology,
morphology, syntax, semantics, lexical policy, human usability, model behavior,
and evaluation methodology. The historical rationale matters as much as the
outcome: **do not replace it with a decontextualized implementation rule.**

## Lifecycle

- `Draft`: incomplete record under preparation.
- `Proposed`: decision is specified, but not ratified; cannot change normative
  language behavior.
- `Experimental`: testable hypothesis with an evaluation plan. Neither its
  model nor its parameters have normative standing.
- `Accepted`: ratified decision; language-affecting changes must be reflected in
  the canonical specification, machine-readable rules and tests as applicable.
- `Rejected`: considered and not adopted; keep rationale and test evidence.
- `Superseded`: replaced; link to the successor rather than deleting history.

Status is **not** confidence: a proposal can be well supported, while an
accepted decision may need later revision. The author of a record cannot
silently declare a linguistic choice accepted. Acceptance needs explicit
project-owner approval, captured in the `Decision authority` section or a
reference to the corresponding discussion/commit. Governance and documentation
conventions explicitly authorized by the owner may be accepted directly.

## Authoring and review rules

1. Allocate an immutable sequential `LDR-NNNN` identifier and create one
   Markdown file using `TEMPLATE.md`; keep YAML-like scalar frontmatter keys
   `id`, `title`, `status`, `date`, `domain`, `supersedes`.
2. Separate **observations**, **assumptions**, **alternatives**, **decision or
   hypothesis**, **trade-offs**, **falsification criteria**, and **evidence**.
   Include links to source specifications, corpus data and tests, when known.
3. Mathematical objectives require definitions, normalization, direction,
   constraints, units, and parameter-calibration method. A symbolic formula
   is not evidence of a measured efficiency gain.
4. Do not rewrite old LDRs to reflect new conclusions. Add an LDR that
   supersedes them and explain what changed. Typos and broken links may be
   fixed in place without changing the decision.
5. Keep unconfirmed lexemes and unattested forms clearly marked. LDRs
   must not silently ratify entries in `formalization/data/attested_forms.json`.
6. Run `python3 -m formalization build`, then `python3 -m formalization validate`.
   The generated `formalization/data/ldr_registry.json` is a search index;
   the LDR Markdown files are authoritative for recorded rationale.

## Existing linguistic decisions

The 42 grammar decisions in `research/grammar/confirmed_decisions.json` and 13
phonological decisions in `research/phonology/confirmed_decisions.json` predate
LDRs. They remain confirmed and are indexed by the formalization pipeline,
with their original source and content hash. **Do not fabricate 55 retrospective
LDR rationales** from those short decision statements. Backfill individual
LDRs only after reviewing the associated studies or historical conversation.

## Initial records

- [LDR-0001: Adopt LDRs](LDR-0001-language-design-records.md) — Accepted
- [LDR-0002: Lexical efficiency scoring](LDR-0002-lexical-efficiency-scoring.md) — Experimental
- [LDR-0003: Preserve semantics during optimization](LDR-0003-semantics-preservation.md) — Accepted
- [LDR-0004: Migrate normative sources to structured data](LDR-0004-formal-source-of-truth.md) — Proposed
- [LDR-0005: Repository boundaries](LDR-0005-repository-boundaries.md) — Accepted
- [LDR-0006: Tokenizer benchmark protocol](LDR-0006-tokenizer-benchmark-protocol.md) — Experimental
