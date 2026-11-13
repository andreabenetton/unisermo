---
id: LDR-0015
title: Synchronize already confirmed grammatical forms into the confirmed lexicon
status: Accepted
date: 2026-11-13
domain: lexicon
supersedes: none
---

# LDR-0015 — Synchronize already confirmed forms into the confirmed lexicon

## Context and problem

The confirmed lexical snapshot listed 108 forms while the parser's lexicon index had 143. Twenty of the 35 missing entries were explicitly marked `decision_attested_not_indexed`, with source links to current normative grammar. Fifteen others were marked `example_only`; some are historical or retired (notably `frat` and `mil`). Benchmark UCUB-001 exposed this discrepancy. The author directed that the confirmed lexicon be expanded to include material already on main.

## Alternatives

1. Leave all 35 outside the confirmed snapshot (inconsistent with existing normative decisions).
2. Unconditionally confirm all 35 (would reintroduce retired spellings and elevate mere examples).
3. **Chosen:** synchronize the 20 previously decision-attested forms, preserving 15 example-only entries in their existing nonconfirmed status.

## Decision

Add `ades, admov, bis, dees, demov, es, ines, inmov, jer, ka, mov, no, nul, omni, rees, remov, tot, traes, uno, wi` to `research/lexicon/confirmed_lexicon.json`, retaining normative source references and meanings. This is an inventory consistency change, **not new ratification of the underlying meanings**.

Do not promote the remaining example-only forms without explicit review, particularly historical `frat` and `mil`. Unlike these, canonical numerals `nul`, `bis`, `uno`, and the confirmed particle `wi` already have direct specification support.

## Evaluation and evidence

Review `formalization/data/lexicon_index.json` statuses and the cited current language documents. Expected count: 108 + 20 = **128** confirmed entries. No canonical grammar or parser changes. Run `python3 -m formalization build` and `python3 -m formalization validate`; check generated status and tests before merge. In particular, the four motion-phase verbs refer to onset/continuation/cessation/resumption of movement, **not spatial direction**, as stipulated by `language/verb_specification.md`.

## Consequences and compatibility

Existing test corpora remain immutable. New benchmark corpus provenance should be resolved against the updated confirmed list after this change is merged. Note the distinct 15 example-only forms are *not* thereby sanctioned. Syntax-only and lexical-valency gaps remain.

## Decision authority

User project owner explicitly instructed expansion of confirmed lexicon to include already present material from main on 2026-11-13. This record adopts the conservative subset consisting only of previously documented normative decisions; the example-only set is reserved for separate review.

## References

- `research/lexicon/confirmed_lexicon.json`
- `formalization/data/lexicon_index.json`
- `language/copula.md`
- `language/verb_specification.md`
- `language/numerals.md`
- `language/questions.md`
- `language/negation.md`
- `language/noun_number_system.md`
- `language/articles.md`
- `docs/ldr/README.md`
