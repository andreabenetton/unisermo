---
id: LDR-0013
title: Extend the locative -in to abstract proposition domains
status: Accepted
date: 2026-11-12
domain: grammar
supersedes: none
---

# LDR-0013 - Abstract-domain locative -in

## Context and problem

Unisermo already uses -in for location/containment ("in/at") and reserves
other grammatical functions for distinct core cases and free relators.
After ratifying aut permission and -de as the source of a grant, the
project owner asked to analyze abstract normative domains across other
fields. The proposal was one shared locative case -in for physical and
abstract domains, with a meaningful distinction between *where an
event happens* and *where a proposition is asserted/evaluated*.

The prior SVO-and-case grammar already allows fronting for emphasis.
Consequently, a fronted locative cannot simply be reinterpreted
unconditionally as a proposition-domain marker without breaking
previously ratified syntax.

## Alternatives

1. Add a new abstract-domain case suffix: rejected, because it
   duplicates the domain sense of the existing locative -in.
2. Co-opt pre-existing temporal tem or origin -de: rejected because
   temporal and source relations differ from a domain of evaluation.
3. Define "initial NP-in always scopes over the proposition":
   rejected because initial physical locatives are also legal after
   topicalization; surface position alone does not prove attachment.
4. Accept one locative for both physical and abstract domains, with
   two syntactic attachment levels, a conventional preposed
   proposition-domain frame for a *simple clause*, and explicitly
   acknowledged ambiguity when the nominal domain is dual-use:
   selected.

## Decision or hypothesis

**One already ratified suffix -in**, with no new morpheme, conveys
"in/at/within a reference domain". It can occur with spatial
locations, normative regimes, institutional contexts, academic or
technical disciplines, software/computation environments, simulated
or fictional worlds.

Two different construction types are distinguished:

- Event/predicate-attached local complement: movi domin =
  "I move in the house". This supplies the local setting of the
  event/predicate.
- Proposition-domain adjunct: [DOMAIN-NP-in] [SIMPLE CLAUSE P].
  A left-peripheral abstract domain before the subject if explicit
  (otherwise before the finite verb) defines where the *whole
  simple proposition P* is evaluated or holds. It applies to local
  predicate negation and ordinary predicate dependents, without
  directly negating the domain phrase.

Schematic placeholder examples; bracketed terms are NOT ratified words:

- [NORMA]-in auti umande mov: within the norm's domain, a person
  permits me to move. "umande" remains the source granting permission.
- [NORMA]-in no auti umande mov: within that domain, that person
  does not grant permission. The no applies to auti.
- [SISTEMA]-in faki: I act/make something within that system.
- [SIMULAZIONE]-in movi: I move inside a simulation; no factual
  assertion of movement beyond the simulated domain.

The semantic distinction is **syntactic attachment**, not
"initial placement always means domain". Because spatial
complements can be fronted, domin movi still permits the
topicalized event-locative reading. If a noun simultaneously
names a building, an organization, and/or its normative regime,
the written string may be genuinely ambiguous without additional
context. Preserve or explicitly resolve it; do not promise full
disambiguation merely from constituent position.

A domain does not necessarily cause, license, or provide
evidence for the proposition. It is distinct from ablative -de
(source), temporal relator tem, causal due, instrumental per,
manner mod, purposive fin, and benefactive pro. One proposition's
domain constrains the statement about P, not automatically
following coordinated or subordinate propositions.

## Evaluation and evidence

The owner explicitly ratified the proposed single -in design
on 2026-11-12: "ratificata". The proposal was limited to
ordinary single propositions. Documentary tests preserve spatial
locative readings, scope distinctions, placeholders, source
contrasts, and explicit exclusions; they do not constitute
an executable semantic proof or human comprehension evaluation.

## Consequences and compatibility

- No new grapheme, suffix, case or free relator.
- Existing -in case attachment to the head noun is unchanged.
- Local/event locatives and existing word-order fronting remain
  valid, and ambiguous dual-use locatives must remain ambiguous
  unless the expression resolves the intended attachment.
- The grammatical domain frame is limited to a single simple
  proposition. Composed statements (e/o/ma and other connectors),
  subordinate scope, nested or stacked domains, and temporal
  reinterpretations are not approved by this decision.
- The Phase 1 parser does not implement abstract-domain scope;
  unsupported syntax must not be silently accepted.

## Decision authority

Explicitly approved by the language owner on 12 November 2026:
"ratificata", referring to the preceding proposal for one -in
covering physical and abstract domains, with syntactically distinct
attachment and single-simple-clause scope. The refinements in this
record prevent a collision with previously ratified case fronting,
not new lexical or clausal ratifications.

## References

- `language/noun_case_system.md`
- `language/word_order.md`
- `language/verb_specification.md`
- `docs/ldr/LDR-0012-aut-permission-source.md`
- `research/grammar/confirmed_decisions.json`
- `formalization/semantics/README.md`
- `tests/test_abstract_locative_domain_ratification.py`
