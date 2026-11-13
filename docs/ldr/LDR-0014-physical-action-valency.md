---
id: LDR-0014
title: Distinct overt-object valencies for fer portar ten and kunten
status: Accepted
date: 2026-11-13
domain: grammar
supersedes: none
---

# LDR-0014 - Physical taking, transport, constraint and containment

## Context and problem

The 2026-10-25 lexicon already defined four non-interchangeable
physical-action roots: `fer` physically takes/grasp; `portar`
carries/transports; `ten` maintains a physical/control constraint
over time; `kunten` is a **lexicalized** spatial containment verb.
These roots had no complete ratified argument-frame inventory.
Unisermo has existing accusative `-em`, ablative `-de`,
allative `-ad` and locative `-in`. The parser must not
rely on spelling resemblance or treat all transitive patients as
the same semantic role.

The author requested analysis, reviewed RFC #64, then expressly
ratified its four proposed patterns and requested merge of
recent approved PRs on 2026-11-13.

## Decision or hypothesis

| Verb | Canonical overt frame | Argument roles |
|---|---|---|
| `fer` | `Y fer X-em [SOURCE-de]` | Y initiator/taker, X physically acquired/grasped, SOURCE physical origin |
| `portar` | `Y portar X-em [SOURCE-de] [DEST-ad]` | Y carrier, X transported cargo, SOURCE spatial origin, DEST toward-location |
| `ten` | `Y ten X-em` | Y constraint maintainer, X held or controlled entity |
| `kunten` | `CONTAINER kunten CONTENTS-em` | subject spatial container; object physically enclosed contents |

`-em` has one grammatical accusative function, but **four
verb-dependent thematic roles**. `SOURCE-de` on `fer`
denotes a physical source, **not necessarily a previous owner,
permitting authority or holder**. `portar` denotes an actual
carrying/transport event, with an optional direction marked
`DEST-ad` that **does not entail successful arrival**.
`ten` encodes constraint persistence without acquisition,
displacement or enclosure. `kunten` encodes physical
containment, *not* information inclusion or ownership;
its subject need not be volitional or animate.

The canonical citation examples are:

- `i feri portaem`: I physically take/grasp the door
- `i feri portaem umande`: I take the door from a person's
  physical vicinity, without asserting ownership
- `i portari portaem domad`: I carry the door toward a house
- `i portari portaem domde umanad`: I carry the door
  from a house toward a person
- `i teni portaem`: I hold/maintain control over the door
- `dom kuntena akwaem`: the house physically contains water

An independent event-locative `LOCATION-in` or canonical
free relator may modify these predicates, without becoming
an additional core patient role. Containment by `kunten`
does not require a redundant interior locative.

## Derivation and participant roles

Single regular phase prefixes `ad-/in-/de-/re-` preserve
the base participant-role schema while changing only the
phase of the action, and productive `kun-` preserves it
while adding association/jointness **without an obligatory
extra co-agent**. This applies to `fer`, `portar`
and `ten`, and to the lexicalized `kunten` where a
single phase affix is licensed. `kunten` itself **must
not** be analyzed compositionally as an ordinary
`kun-` + `ten` joint-holding event. No general
stacked-prefix valency inheritance is ratified.

## Consequences and compatibility

The **bounded parser** requires an overt object `X-em`
in each of these four frames, including modal complements.
This does **not** declare that object omission is impossible
in fluent Unisermo. Discourse/context-sensitive omission
remains an open grammatical design decision.

Physical source and allative destination are explicitly
optional **for the frames that license them**. They do
not imply permission, legal possession or arrival. Other
possible thematic roles, type checking, alternative case
orders, and mixed/stacked valency frames remain open.
The parser should fail closed on these, not extrapolate
movement cases to non-motion `ten` or `kunten`.

The parser must preserve separate `argument_roles`
metadata: taker/acquired entity, carrier/cargo, holder/
held entity, container/physical contents. That metadata
records the user's asserted relation, **not** a validated
fact about the world.

## Alternatives

1. Collapse `fer` and `portar` into "take/carry":
   rejected as contrary to existing semantics.
2. Let `ten` inherit motion source/destination:
   rejected; constraint persistence is not motion.
3. Treat `kunten` as generic associative joint holding:
   rejected, because its specialized physical containment
   sense was already ratified.
4. Derive four new case suffixes for four patient roles:
   rejected as unnecessary; existing case marking plus
   lexical valency yields compositional clarity.
5. Require no overt patient in the reference parser:
   deferred; object omission needs a separate decision.

## Evaluation and evidence

- Author's explicit approval 2026-11-13:
  "ratifica e fai merge delle PR recenti"
- Historical prior design:
  `research/grammar/physical_action_valency_rfc.md`
- Existing root decisions:
  `language/derivation.md`
- Canonical case system:
  `language/noun_case_system.md`

This accepted record is normative together with the three
current language specifications. It is not itself a semantic
world-model, nor a human comprehension evaluation.

## Decision authority

The owner explicitly approved these four candidate frames on
2026-11-13 by instructing: "ratifica e fai merge delle PR recenti".
The approval followed the detailed physical-action RFC and its
distinctions among physical origin, transport destination,
constraint and containment. Only the four overt-object frames,
their optional selected spatial complements and single-prefix
inheritance are accepted here. Discourse-conditioned omission,
unrestricted argument order and broader composition remain open.

## References

- `language/verb_specification.md`
- `language/derivation.md`
- `language/noun_case_system.md`
- `research/grammar/confirmed_decisions.json`
- `formalization/data/valency_frames.json`
- `tests/test_physical_action_valency.py`
