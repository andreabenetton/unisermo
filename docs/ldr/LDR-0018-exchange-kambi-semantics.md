---
id: LDR-0018
title: Exchange and commercial transfer without buy/sell lexical duplication
status: Proposed
date: 2026-11-13
domain: lexical-semantics
supersedes: none
---

# LDR-0018 — Exchange semantics and the candidate root `kambi`

## Context

The author established a design preference for general compositional verbs instead of two opaque roots for converse descriptions of the same event: prospective `don` for giving/receiving and transmission of physical or informational objects. A further candidate is `kambi` (exchange), intended to make buy/sell, barter and other reciprocal transfers describable without individual 'buy' and 'sell' roots.

**No ratification:** `kambi`, `don`, the lexical value of money or price, and any exchange-specific valency in this document remain proposed. Current canonical `-em`, `-ad`, `-de`, free `kun`, `per`, `pro`, and motion/transfer distinctions must not silently change.

## Alternatives

1. Lexicalize separate `buy` and `sell` roots. Direct to translate, but duplicates viewpoint on a single exchange.
2. Treat commercial exchange as `don` twice. Keeps lexical count low but needs to bind two transfers into *one* transaction; two unrelated giving clauses do not entail conditional exchange/payment.
3. Adopt a generic `kambi` = participate in a reciprocal exchange. Base event semantics are useful independently of exactly which goods are exchanged, but the full two-theme frame requires specification.
4. Overload existing `per`, `kun`, `pro` or nominal `-de/-ad` to encode consideration. **Reject as an implicit default:** `per` is means/instrument, `kun` is comitative, `pro` benefactive, and `-ad/-de` destinations/sources. A payment-for relation is not automatically one of these.
5. Add a dedicated countervalue relator or a tightly constrained valency construction. A possible later solution, **not adopted here**, is an explicit reciprocal-theme operator. Its morphology should be decided only after examples and ambiguity analysis.

## Proposed event semantics

An exchange between participants A and B of themes X and Y involves **two linked transfers**:
- A transfers X to B;
- B transfers Y to A;
- the two transfers are connected as reciprocal consideration of a single exchange arrangement.

The event may be a **completed exchange** or merely an **offer / planned transaction**. `kambi` alone should *not* conflates these. Until aspectual event semantics and completion are approved, avoid making inferences about performed delivery or payment from command labels.

Typical role mapping: actor A contributes X and receives Y; counterpart B contributes Y and receives X. The inverse viewpoint (B's account of the same exchange) swaps which theme is supplied and which is obtained. This is more complex than `don` because there are two theme roles.

**Proposed minimal phrase:** `A kambi kun B` = A exchanges with B (the items unspecified), but this requires author confirmation that existing comitative `kun` can denote the counterparty of this reciprocal event and that a bare-objectless frame is grammatical for this verb. Do not treat it as a canonical assertion or a parser pass.

**Schematic complete proposition:** `EXCHANGE(A,B,X,Y)` with A/B participants and X/Y outgoing themes, not yet a valid Unisermo sentence. It must not be rendered as `kambi X-em Y-em` (two accusatives) or `kambi X-em per Y` (means misread as countervalue) by default. An eventual frame should assign X and Y to *distinct, unambiguous roles*.

## Relations to nearby verbs

- `don`: transfers one theme from source to recipient. No inherent compensation. Having two `don` statements may imply two completed transfers but does not by itself prove they were agreed as an exchange.
- `portar`: physically carries cargo; does not entail legal title, purchase, payment, or arrival.
- `fer`: physically takes/grasp; does not entail entitlement or price paid.
- `prest`: temporary transfer with an obligation or expectation of restitution. Returning the **same item** is not the exchange of two separate items, and might merit composition rather than `kambi`.
- `vend`: commercial sale/purchase would be an exchange with a **monetary consideration**; a monetary root and explicit payment role are not currently approved.
- `dok`: teaching/learning remain nonconverse event outcomes; do not generalize `kambi` to every semantically paired verb.

## UX considerations

Do not yet introduce `kambi ad` / `kambi de`. Unlike the one-theme `don` flow, the direction of *which theme* matters; exchange is reciprocal in both directions. Bare `kambi` (exchange) might be a more honest single button if the user interface clearly identifies the two offers. `buy` and `sell` labels require a monetary frame and participant viewpoint.

## Testable questions

1. Does `kambi` without objects convey a reciprocal event rather than mere unilateral giving?
2. Can a recipient/counterparty be expressed using already ratified comitative `kun` without changing the syntax of `kun`?
3. Which construction explicitly labels **outgoing theme X** versus **incoming countervalue Y** with minimal added grammar?
4. What is the semantic distinction among *offer*, *agreement*, *execution* and *completed exchange*?
5. Is the price paid, merely owed, or only offered? No payment or delivery completion is inferred without a precisely ratified predicate.
6. Can the same frame express barter and sale by substituting a money-like object, without extra 'buy/sell' roots?
7. Can a model distinguish an exchange event from two unrelated transfers of goods between the same two people?

## Falsification / acceptance criteria

Before ratification, document at least 12 minimal contrast examples, including barter, a paid sale, a failed delivery, a partial exchange, a loan, two unrelated gifts, and a canceled exchange. Independent reviewers should identify actor, counterparty, X and Y identically and separate facts from goals. Exact parser support must be explicitly added and tested after approval; a truth-value gold should be reviewed independently of parser output.

## Decision authority

Owner requested exploration of `kambi` after analyzing `don`, `prest` and `vend`. This document captures an option, **not approval of lexical forms or new case roles**.

## References

- `language/noun_case_system.md`
- `language/derivation.md`
- `language/word_order.md`
- `formalization/data/valency_frames.json`
- `docs/ldr/LDR-0014-physical-action-valency.md`
