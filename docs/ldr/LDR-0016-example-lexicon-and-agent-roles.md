---
id: LDR-0016
title: Resolve example-only lexemes and adopt compositional agent labels
status: Accepted
date: 2026-11-13
domain: lexicon
supersedes: none
---

# LDR-0016 — Example-only lexical review and study root

## Context and problem

In the 2026-11-13 alignment of the 108-entry confirmed lexical list with parser-attested entries, twenty decision-attested forms were already synchronized in LDR-0015. Fifteen `example_only` items remained: `amik, dom, doktor, frat, likwid, mil, multi, san, solid, student, tan, ter, tes, tik, vid`. Several are used in the canonical grammar but never entered into the confirmed list; `frat` and `mil` are historical spellings. `doktor` and `student` are opaque role labels contrary to the confirmed agentive suffix `-or`.

## Alternatives

1. Promote all fifteen as opaque lexemes (rejected: reintroduces historical forms and weakens compositional design).
2. Keep all fifteen merely as examples (rejected: prevents current specifications and the confirmed list from agreeing).
3. Promote eleven still-valid examples; retain historical forms only in historical sources; replace opaque agent labels with transparently derived forms; ratify a study root (chosen).

## Accepted decision

- Confirm eleven already-used live examples: `amik, dom, likwid, multi, san, solid, tan, ter, tes, tik, vid`, preserving the meanings in their current documentation.
- Keep `frat` and `mil` **retired**: canonical `adel/adelo/adele` and `mila` remain authoritative.
- Do **not** confirm `doktor` or `student` as unanalyzed roots.
- Ratify **`stud`** as the verb root *study*, distinct from `sap` (know), `kap` (understand), and `pens` (think). `studor` is the regular `stud+-or` person who studies, without an enrollment entailment.
- Use **`kuraror`** (`kurar+-or`) for the person who cares/cures, without a medical license entailment; `dokor` (`dok+-or`) means teacher. Do not treat the familiar English doctor as a reason to reverse the canonical root meaning.
- Adopt `tik`, `tes`, `tan` as spelled in the **current normative** `language/demonstratives.md`. Earlier draft alternatives are not silently merged into the confirmed list.
- Existing productive morphology applies to `stud` and `kurar`; there is no new suffix or agentive subgrammar.

This reconciles the previously proposed 20 additions with 12 additional confirmed lexical **entries** (11 live exemplars + `stud`), giving **140 entries** in the confirmed list. Transparent `kuraror`, `studor`, `dokor` need not each be introduced as separate primitive roots.

## Evaluation and evidence

Sources: current `language/demonstratives.md`, `language/numerals.md`, `language/copula.md`, `language/derivation.md`, `language/noun_case_system.md`, and `formalization/data/lexicon_index.json`. The user explicitly approved proceeding with the reviewed 15 entries and the latest derived-agent corrections on 2026-11-13.

Before merging, run `python3 -m formalization build`, `python3 -m formalization validate`, and applicable tests, inspect generated-data deltas and ensure historical corpora remain untouched. Search current live documents for any leftover `doktor` or `student` examples and replace only where they mean the agent roles; do not perform blanket rewrites of historical quotes. Ensure parser category and derivation behavior is consistent with the lexical source. No model benchmark scores are implied.

## Consequences and compatibility

The lexical inventory becomes more consistent and agent nouns compositional. `studor` need not mean institutional student, and `kuraror` need not mean professionally licensed physician. Documents or parser snapshots containing historical example-only labels must be reviewed, not silently interpreted as confirmed modern words.

## Decision authority

Explicit author/project-owner approval in conversation, 2026-11-13.

## References

- `docs/ldr/LDR-0015-confirmed-lexicon-sync.md`
- `research/lexicon/agent-roles-care-study-2026-11-13.md`
- `research/lexicon/confirmed_lexicon.json`
- `language/derivation.md`
- `language/demonstratives.md`
