---
id: LDR-0005
title: Separate Unisermo implementation from frozen GlottoDelta atlas
status: Accepted
date: 2026-10-22
domain: governance
supersedes: none
---

# LDR-0005 — Separate repository boundaries

## Context and problem

The recovered Unisermo Git repository contained both its language design and a
historical GlottoDelta web atlas snapshot in the same top-level directories.
The project owner requested an ordered repository layout with a strict boundary:
the authoritative GlottoDelta atlas remains maintained independently on GitHub.

## Alternatives

1. Leave all research and atlas assets at the root: minimal migration but ambiguous ownership.
2. Delete the atlas snapshot: saves space but breaks phonology experiment reproducibility.
3. Move original atlas assets unchanged to `vendor/glottodelta-atlas/`, with explicit paths,
   and move Unisermo test scripts to `tests/` (selected).

## Decision or hypothesis

Adopt top-level directories `language/`, `research/`, `formalization/`,
`benchmarks/`, `tests/`, `scripts/`, `docs/`, `legacy/`, and `vendor/`.
`vendor/glottodelta-atlas/` remains read-only reference material, never the
publication source or upstream for the current atlas. Historical atlas bytes
stay unchanged; any deliberate refresh requires a new owner-reviewed change.
Parser/generator code is placed in dedicated modules while `formalization.core`
retains the stable API. Source-of-truth migration proposed in LDR-0004 is
unchanged, not silently accepted by this refactor.

## Evaluation and evidence

- Validate SHA256s in `vendor/glottodelta-atlas/docs/ORIGINAL_FILES.sha256`.
  Resolve legacy paths under `legacy/`, atlas paths under `vendor/glottodelta-atlas/`.
- Run the formalization suite, the historical snapshot integrity tests, and the
  phonology tests. Keep Git history intact, with no configured remote.
- Do not edit the frozen original atlas README, sources, binaries, or scripts;
  changes to Unisermo research tools may update their input paths.

## Consequences and compatibility

The layout is clearer, but callers using the old `scripts/test_*.py` paths must
update to `tests/test_*.py`; atlas commands run from the vendor directory.
Existing `python3 -m formalization` commands remain compatible. Git history
continues to hold prior layouts and branches. The current atlas is only on its
independent GitHub repository, not in this ZIP.

## Decision authority

Accepted as a repository governance change at the project owner's explicit
request of 2026-10-22 to reorganize the repository and keep the GlottoDelta
atlas independent and authoritative on GitHub.

## References

- `README.md`
- `docs/ATLAS_SNAPSHOT.md`
- `tests/test_unisermo_identity.py`
- `formalization/core.py`
