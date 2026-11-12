---
id: LDR-0012
title: Unified permission and authorization with aut and ablative source
status: Accepted
date: 2026-11-12
domain: grammar
supersedes: none
---

# LDR-0012 - Unified permission and authorization using aut

## Context and problem

The project already ratified separate situational possibility pos,
capacity pot, procedural knowledge sap, obligation deb and volition vol.
Permission or authorization is a distinct normative modal relation.
The question was whether formal authorization and ordinary permission
require separate roots. The owner rejected that extra lexical division
provided existing complements can identify the source of the permission.

The existing ablative -de denotes an origin/source, including non-spatial
source states in state transitions. The existing analytic servile frame
places a conjugated modal head before an uninflected dependent verb.
In ordinary motion clauses, -de can also mark the spatial origin of the
movement; leaving a new grant source unpositioned would be ambiguous.

## Alternatives

1. Keep separate roots for permission and formal authorization:
   rejected as unnecessary lexical complexity.
2. Use pos for both opportunity and permission: rejected because
   circumstantial possibility does not entail normative permission.
3. Introduce a new source/authority relator: rejected because -de
   already means "from/source/origin".
4. Ratify one finite root aut for both permission and authorization,
   with optional ablative granting-source immediately after the modal
   head and before its bare lexical complement: selected.

## Decision or hypothesis

The short root aut (a-u-t, no h) is a regular, inflected servile verb
denoting permission or authorization to act. Its broad normative sense
covers informal permission and formal grants alike; qualifiers convey
the relevant person or normative source. It does not automatically mean
external feasibility (pos) or physical competence (pot). It implies
neither actual action nor that any grantor has formal jurisdiction.

Canonical simple action frame:

    [subject] [no] AUT-FINITE [SOURCE-NP-de] [no] VERB-ROOT [ARGUMENTS...]

- auti mov = I am permitted to move.
- auti umande mov = a person permits me to move.
- no auti umande mov = I lack permission from that person to move.
- auti umande no mov = that person permits me not to move.
- auti umande mov domde = a person permits me to move from the house;
  umande is the grant source in the aut-head slot while domde belongs
  to the dependent movement clause as its spatial source.

The source is optional and uses the existing ablative -de, not a
new suffix. The source-bearing slot is the specific permitted
exception to strict modal-head/dependent-verb adjacency; it does not
turn -de into an authority-case in arbitrary other frames.
With no source phrase in that slot, an ablative following mov cannot
automatically be reassigned as the grantor. The scope of no follows
the existing modal rule: no auti V denies permission, auti no V
allows refraining. Lack of permission does not automatically assert
a positive prohibition (debi no V), nor does the lack of an obligation
(no debi V) automatically assert positive permission. Source-qualified
denial concerns the named source only.

This decision does NOT ratify the use of locative -in for legal,
institutional, social or other abstract normative domains. Those
cross-domain locative rules are reserved for another design stage.
No generic productive aut- prefix and no alternative spelling with h
is introduced.

## Evaluation and evidence

Owner discussion 12 November 2026: the author accepted one lexical
meaning for permission and authorization, because source complements
can provide any needed distinction, and instructed implementation.
The unambiguous finite-modal-head/source-slot/lexical-root order
preserves distinct roles for an authority-source and a physical
source of movement. Documentary regressions check the approved
examples, the lexical decision and generated registry hashes.
Human comprehension and full typed semantic parsing remain untested.

## Consequences and compatibility

One short root with three canonical graphemes is added, with existing
finite TAM morphology. No new case or relator; the use of -de remains
an origin/source relation with frame-specific argument attachment.
A governed, pre-infinitive source phrase is narrowly licensed for aut.
Previous local negation and no lim remain untouched. Formalization
Phase 1 does not implement servile complements or this source slot
and must fail closed on unsupported constructions.

## Decision authority

Explicitly approved by the project owner on 2026-11-12, following the
proposal to ratify aut with a -de source and to leave the abstract
scope of -in for separate discussion: "procedi poi affrontiamo il
tema in anche in altri ambiti". Accepted decision does not include
abstract locative extensions.

## References

- `language/verb_specification.md`
- `language/noun_case_system.md`
- `language/negation.md`
- `research/grammar/confirmed_decisions.json`
- `research/lexicon/confirmed_lexicon.json`
- `docs/ldr/LDR-0011-servile-negation.md`
- `tests/test_permission_aut_ratification.py`
