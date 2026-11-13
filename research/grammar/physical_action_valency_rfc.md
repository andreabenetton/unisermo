# RFC — Physical action valency: fer, portar, ten, kunten

> **Status: PROPOSAL / NOT RATIFIED.** Prepared 2026-11-13 for the
> language owner's next explicit decision. This document is a design
> candidate, **not** a source of canonical grammar. Do not update
> `language/`, `research/grammar/confirmed_decisions.json`, the
> valency registry or executable parser from this RFC until approval.

## Established source constraints

This RFC preserves, without changing, the already accepted lexical
distinctions in `language/derivation.md` (Cognitive and physical-action
root families; Associative `kun-` and the `ten` family; Physical
opening and closing properties):

- `fer` = physically take/grasp. It must **not** acquire the
  Romance/Latin sense 'carry' by etymology.
- `portar` = physically carry/transport. It is different from
  `fer` and the `mov` displacement alternation.
- `ten` = hold/maintain a physical or control constraint **over
  time**. It does **not** assert arrival, acquisition or movement,
  and is different from `ines` state persistence.
- `kunten` = *lexically specialized* physical/spatial containment.
  It is **not** the compositional default interpretation of
  productive `kun-` on arbitrary verbs, nor generic abstract
  inclusion. The container need not be a volitional agent.
- `-em` is the existing accusative/direct-object case, `-ad`
  the existing allative/destination, `-de` the existing
  ablative/origin and `-in` the existing locative. Free relators
  retain their existing meanings. Case selection must not
  silently conflate physical origin with ownership or permission.

The existing parser reports these lexical roots as
`valency_evidence(...).status == "undetermined"`. Its earlier
generic SVO support is a **syntax subset**, not an accepted lexical
valency inventory for these roots.

## Recommended four minimum frames (require author ratification)

### A. Physical taking: fer

```text
Y-NOM FER-FIN X-em [SOURCE-de]
```

- **Y** = initiator/taker; **X-em** = entity grasped/taken.
- `SOURCE-de` optionally denotes the *physical source* of
  acquisition. It does not automatically denote a previous owner
  or granting authority.
- The event asserts physical grasp/acquisition, **not**
  sustained holding, transport, arrival, ownership transfer
  or authorization. Distinguish `fer` from `portar`,
  `ten` and `aut`.
- At minimum, one explicit patient `X-em` is required in the
  executable subset. Potential object omission in discourse
  remains open, rather than asserted ungrammatical.

Illustrations (all example nouns are already attested or indexed):

- `i feri portaem` = I take/grasp the door.
- `i feri portaem umande` = I take the door from a person
  (not necessarily that person's property).

**Open choice A:** Does `SOURCE-de` belong to the ordinary
`fer` frame as proposed, or should it remain an untyped
independent ablative adjunct until explicitly validated?

### B. Physical carrying: portar

```text
Y-NOM PORTAR-FIN X-em [SOURCE-de] [DEST-ad]
```

- **Y** = carrier; **X-em** = carried cargo/theme.
- Optional `SOURCE-de` and `DEST-ad` encode spatial origin
  and destination **of the carrying event**.
- Unlike `fer`, `portar` denotes carrying/transport activity.
  `DEST-ad` means 'to/toward', **not** proof of arrival.
  No source or destination is mandatory.
- The lexical distinction with the transitive `mov` is
  maintained: carrying involves accompanying/transporting
  cargo; `mov` only specifies displacement.

Examples:

- `i portari portaem` = I carry the door.
- `i portari portaem domad` = I carry the door
  toward the house.
- `i portari portaem domde umanad` = I carry the
  door from the house toward the person.

**Open choice B:** Are the two spatial arguments both
licensed as optional governed complements (proposed), or should
their syntax remain generic spatial adjuncts, with only `X-em`
approved as an obligatory lexical argument?

### C. Holding/maintaining a constraint: ten

```text
Y-NOM TEN-FIN X-em
```

- **Y** = maintainer/controller; **X-em** = entity held
  under a physical or control constraint.
- The frame describes **continued constraint over time**;
  it need not involve physical acquisition, transport, a
  contained volume, or ownership. The holder need not
  be human.
- A normal `LOCATION-in` may locate the assertion/event
  as an adjunct, but this does not create a special
  containment argument for `ten`.
- `-de` is **not** automatically the origin of a maintained
  constraint, and `-ad` is **not** automatically a
  destination of a non-motion `ten` event.

Example: `i teni portaem` = I hold the door.

### D. Physical containment: kunten

```text
CONTAINER-NOM KUNTEN-FIN CONTENTS-em
```

- **Subject** = physical container, spatial enclosure or
  entity imposing spatial bounds. It is **not** necessarily
  a human or intentional agent.
- **CONTENTS-em** = entity physically contained.
- The assertion is about the contents' location **within
  the container's spatial bounds**, not ownership,
  cognitive understanding, abstract part-whole relations,
  or grasping an object.
- A separate `LOCATION-in` adjunct can state where
  the containing event/state holds. It is not automatically
  a second *interior-of* argument, and its attachment may
  need clarification.
- No inherent `DEST-ad` or `SOURCE-de` is introduced
  by containment alone.

Example: `dom kuntena akwaem` = the house contains water
physically.

**Open choice C:** Should `kunten` require an explicit
accusative contents NP in the parser subset (proposed), or
license bare existential 'contain something' without one?
Neither choice follows automatically from lexical meaning.

## Derived verbs and prefix inheritance

Once the base valency frames are accepted, a **single
already-ratified phase prefix** (ad-/in-/de-/re-) can
preserve the same base participant roles while changing
the *phase* of the event. Likewise the productive
associative `kun-` changes jointness/association of
the base event but does **not** add a mandatory co-agent
or create an automatic containment sense.

Proposed safe default:

- `adfer X-em`, `inportar X-em`, `deten X-em`
  preserve the base's accusative entity.
- A lexicalized `kunten` keeps its special containment
  frame, and is **not** re-parsed as an ordinary instance
  of `kun-` + `ten`.
- More than one productive prefix on the same verb is
  outside the parser's current bounded derivation scope.
- Valency inheritance for *all* derivational combinations
  is **not** implied; no silent unrestricted inheritance.

## Proposed parser contract, pending approval

```text
fer     object=required; X-em=taken_theme; source-de=optional
portar  object=required; X-em=cargo; source-de/dest-ad=optional
ten     object=required; X-em=constraint_target
kunten  object=required; X-em=physical_contents
```

A `-in` event-location adjunct and existing invariant free
relators remain independent modifiers. An accusative object
must not gain the same semantic label on all four verbs;
the **lexical predicate determines its thematic role**.

The parser should record each accepted frame in the
source-linked `formalization/data/valency_frames.json`,
attach an explicit `valency` and `argument_roles` AST
record, use one shared validator for finite and servile
dependents, and add both accepted/rejected executable
fixtures. **Do not** add these entries as `documented`
until their grammar status changes from PROPOSAL to
ACCEPTED.

## What remains intentionally open

1. Object omission and how the implicit object is
   recovered from discourse.
2. Whether `fer` physical origin `-de` is governed or
   merely an adjunct, and whether it presupposes a
   previously established physical hold.
3. Whether `portar` origin and destination are lexical
   complements or generic adjuncts.
4. Valency of motion during `ten`/`kunten`; ownership,
   authority, permission and containment are **not**
   inferable from these verbs.
5. General participant type systems, semantic plausibility,
   stacking, mixed case orders and nested modal scopes.

## Authorization boundary

This RFC responds to an instruction to **proceed with
analysis of the four verb families**, not an explicit
ratification of the particular new argument mappings.
It should remain a **draft PR**, unmerged, until the
language owner confirms or amends the proposals.
