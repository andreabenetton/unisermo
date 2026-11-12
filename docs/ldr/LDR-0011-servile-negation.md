---
id: LDR-0011
title: Short servile roots and local modal negation scope
status: Accepted
date: 2026-11-12
domain: grammar
supersedes: none
---

# LDR-0011 - Short servile roots and local modal negation scope

## Context and problem

Unisermo already selects an analytic finite-servile + bare verb-root
construction rather than synthetic modal TAM morphology. The individual
servile roots had not been ratified. Separately, ordinary preverbal no
marks local predicate negation. Without two operator scopes, "not obliged
to act" risks being conflated with "obliged not to act."

The owner explicitly preferred short roots and approved the expressive
contrast between external possibility, internal capacity and practical
know-how, together with obligation and volition.

## Alternatives

1. Collapse possibility and ability into one short root: rejected because
   external opportunity and actor capacity can differ.
2. Retain a synthetic TAM ability marker: rejected by the previous modal-m
   retirement.
3. Invent distinct negation particles for modality and dependent action:
   rejected as unnecessary.
4. Ratify short analytic heads pos/deb/vol/pot, retain sap as knowledge,
   license its know-how complement frame, and interpret free no by the
   predicate position: selected.

## Decision or hypothesis

Accepted roots: pos = situational possibility/opportunity; deb =
normative obligation; vol = desire/volition; pot = participant
ability/capacity. Previously confirmed sap continues to mean possess
knowledge and, with a bare infinitive complement, specifically means
knowing how to perform the action.

All servile heads are ordinary finite verbs (root + aspect + time +
person vowel + optional N). The dependent verbal root stays
uninflected and shares the servile subject; pro-drop remains available.

For any licensed servile M and dependent action V:

- no M-i V = NOT M(V): negation of the modality.
- M-i no V = M(NOT V): negation of the dependent action.

Examples: no debi mov = not required to move; debi no mov = required
not to move. No inference of a prohibition from the former is licensed.
The corresponding position distinction applies to pos, vol, pot, and
sap know-how frames, without implying that all are truth-functional
operators with identical entailments.

Permission or authorization is not automatically conveyed by pos,
and physical necessity or inevitability is not automatically conveyed
by deb. Multi-negation, nested servile complements, alternate subjects,
subordinate modal scope, and interaction with the separately ratified
no lim construction remain outside this decision.

## Evaluation and evidence

2026-11-12 project-owner response approving the four-root distinction
because it adds expressive power; previous approval of the analytic
servile construction; preceding conversational confirmation that the
position of no should distinguish the two readings. Source-linked
documentary tests assert form inventory and scope contrast. These
tests do not verify human interpretation or constitute executable
compound-clause semantics.

## Consequences and compatibility

No new phonemes or modal TAM markers. No old roots are redefined:
sap retains ordinary lexical knowing while adding a governed bare-root
know-how complement. Four new root lexemes use the canonical alphabet.
The existing narrow Phase 1 parser deliberately does not implement
servile complement ASTs or mixed modal scope; unsupported syntax is
not to be silently accepted.

## Decision authority

The owner ratified the servile-position negation proposal with "si"
on 2026-11-12 and approved the pos/deb/vol/pot contrast with
"mi piace come distinzione, introduce espressivita" in the same
conversation. Decision scope is limited to the five head/complement
frames and explicitly described local-negation placements.

## References

- `language/verb_specification.md`
- `language/negation.md`
- `research/lexicon/confirmed_lexicon.json`
- `research/grammar/confirmed_decisions.json`
- `docs/ldr/LDR-0010-wide-scope-negation.md`
- `tests/test_servile_negation_ratification.py`
