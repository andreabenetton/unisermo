---
id: LDR-0018
title: Exchange and commercial transfer without buy/sell lexical duplication
status: Proposed
date: 2026-11-13
domain: lexical-semantics
supersedes: none
---

# LDR-0018 — Exchange semantics and the candidate root `kambi`

## Context and problem

The author established a design preference for general compositional verbs instead of two opaque roots for converse descriptions of the same event: prospective `don` for giving/receiving and transmission of physical or informational objects. A further candidate is `kambi` (exchange), intended to make buy/sell, barter and other reciprocal transfers describable without individual 'buy' and 'sell' roots.

**No ratification:** `kambi`, `don`, the lexical value of money or price, and any exchange-specific valency in this document remain proposed. Current canonical `-em`, `-ad`, `-de`, free `kun`, `per`, `pro`, and motion/transfer distinctions must not silently change.

## Alternatives

1. Lexicalize separate `buy` and `sell` roots. Direct to translate, but duplicates viewpoint on a single exchange.
2. Treat commercial exchange as `don` twice. Keeps lexical count low but needs to bind two transfers into *one* transaction; two unrelated giving clauses do not entail conditional exchange/payment.
3. Adopt a generic `kambi` = participate in a reciprocal exchange. Base event semantics are useful independently of exactly which goods are exchanged, but the full two-theme frame requires specification.
4. Overload existing `per`, `kun`, `pro` or nominal `-de/-ad` to encode consideration. **Reject as an implicit default:** `per` is means/instrument, `kun` is comitative, `pro` benefactive, and `-ad/-de` destinations/sources. A payment-for relation is not automatically one of these.
5. Add a dedicated countervalue relator or a tightly constrained valency construction. A possible later solution, **not adopted here**, is an explicit reciprocal-theme operator. Its morphology should be decided only after examples and ambiguity analysis.

## Decision or hypothesis

The author-preferred proposal is a prospective exchange verb with two independently typed theme roles; acceptance of parser implementation is deferred. See the detailed owner-selected syntax below.

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

## Owner-selected candidate syntax (2026-11-13)

The project owner selected the **surface order** `kambi kontra Y X-em` over `kambi X-em kontra Y`, and proposed the following monetary ellipsis: when the `kontra Y` countervalue phrase is omitted from a `kambi` clause, interpret it as `kontra mon` (exchange for money / sale). This section records that specific design preference, not unreviewed adoption of all valency/parser details.

Candidate frame:
```text
[ACTOR-NOM] kambi-FIN [kun COUNTERPART] [kontra INCOMING_COUNTERVALUE] OUTGOING_THEME-em
```
The preferred base order for the two themes is **`kontra Y` before `X-em`**; relative positioning of optional `kun` and full finite-verb complements follows general word order where legal and requires testing. `kontra` is a new **free countervalue relator** (not the existing `anti-` opposition prefix or `per` instrumental); `mon` = money is a *candidate* root, not claimed confirmed.

Semantic roles:
- Subject = participant giving X and receiving Y.
- `X-em` = what the subject provides.
- `kontra Y` = what the subject receives as reciprocal consideration.
- `kun Z` = exchange counterparty (candidate extension of ordinary comitative).

Examples **schematic, not canonical**, with `libr` = book, `mon` = money, and `akwa` = water:
- `i kambi kontra akwa librem` — I trade a book for water.
- `i kambi kontra mon librem` — I sell a book for money.
- `i kambi librem` — I sell a book; implicit countervalue is money.
- `i kambi kontra libr monem` — I buy a book by paying money.
- `i kambi monem` — I exchange money for money (NOT 'I buy'): **ordinary currency exchange / forex** is a concrete valid instance. The monetary-default reading is meaningful, not an anomaly.

**Default scope and limits:**
1. The monetary default is a **lexical omission rule specific to `kambi`**, not a generic rule for all missing complements or all exchanges.
2. The omitted countervalue defaults **only when `X-em` is overt**. Bare `kambi`, `kambi kun Z`, and `kambi kontra Y` do not automatically inherit a complete sell/buy reading until separate ellipsis rules exist.
3. The default denotes *money as the type of consideration*, not its amount, payment time, or evidence of payment. Exact money amount/price will require further syntax.
4. A buyer must still explicitly encode both money as outgoing theme and purchased goods as incoming countervalue. The default never converts `kambi monem` into 'buy'.
5. The plain finite predicate's completed-event interpretation and the distinction between an offer, an agreement, payment and final delivery remain open; do not claim a completed transaction from a UX imperative.
6. `kontra` and `mon` must pass lexical collision and orthographic validation prior to addition to confirmed lexicon.
7. Since `kontra Y` is unmarked for nominal case, the syntactic category and NP boundaries must be formally specified; the proposal treats `kontra` as introducing a relator phrase with nominal base form (not a second nominative subject).

The syntax and monetary-default policy were explicitly proposed by the owner; on 2026-11-13 the owner also explicitly affirmed that `kambi monem` covers money-for-money exchange such as forex, with currency identities and amounts to be expressed by further complements. The broader language change is retained as **Proposed** pending complete valency and grammar review.

## Typed currency identifiers: proposed `mon` namespace (owner clarification, 2026-11-13)

The project owner clarified that `mon` is intended not only to mean money but to **disambiguate ISO currency codes from unrelated Unisermo lexemes** (for example, a hypothetical ordinary root `eur`). Do **not** drop `mon` merely because a currency code is internationally recognizable. This differs from the earlier proposal that parsed `uno EUR-em` as an ordinary case-inflected lexeme.

**Experimental typed monetary noun phrase** (case on the head `mon`, not the ISO code; uppercase code treated as an external standardized identifier rather than a Unisermo lexical root):

```text
mon uno EUR                 = one euro (base)
mon-em uno EUR              = one euro as direct object
kontra mon uno USD          = in exchange for one US dollar
kambi kontra mon uno USD mon-em uno EUR
                             = exchange one euro for one US dollar
```

The printed contiguous orthography is `monem uno EUR`; `mon-em` above only illustrates morphology. Currency code may accidentally match an ordinary root without collision because it is syntactically licensed only after `mon`. The participant role is still unambiguous: the `kontra` phrase denotes **incoming countervalue** and the accusative `monem uno EUR` denotes **outgoing money**.

This is a **proposed typed nominal construction**, NOT an already ratified universal exception to the existing head-final noun phrase and case-attachment rules. Its exact parse (type-marker head + quantity + external identifier), numbers other than `uno`, decimals, additional currency modifiers, lowercase spelling, and interaction with ordinary NP word-order rules need explicit grammar and parser design before acceptance. The ISO label is an external code, not a lexical entry, and should not be passed through Unisermo morphology.

**Design tension to resolve:** the user originally wrote `kambi monem uno usd kontra uno eur`. Under the owner-selected `kambi kontra Y X-em` semantics, that order and assignment denote giving dollars and receiving euros (the opposite of 'give EUR, receive USD'). It is valuable to preserve the typed `mon` insight while ordering the final recommended exchange sentence as `kambi kontra mon uno USD monem uno EUR` for give EUR / receive USD.

## Bounded typed-currency phrase grammar (implementation proposal)

**Status:** experimental parser-facing specification, not an exception already adopted into the canonical noun-phrase system. The owner explicitly endorsed `mon` as a currency-code namespace to prevent lexical collisions and requested implementation exploration. The more general grammar remains under review.

### Proposed orthography and AST

Use `mon` as a **typed nominal head**, followed by a **quantity** and an **external ISO 4217 identifier**. Unlike ordinary Unisermo NPs, this special construction is *head-initial* and takes the synthetic case suffix on `mon`, not on the ISO code.

```ebnf
CurrencyPhrase(case) = MoneyHead(case) Quantity ISO4217 ;
MoneyHead(base)      = "mon" ;
MoneyHead(accusative)= "monem" ;
Quantity             = UnisermoCardinal ;  // in initial tests: uno, bis, dek, ...
ISO4217              = UPPERCASE_ASCII_LETTER UPPERCASE_ASCII_LETTER UPPERCASE_ASCII_LETTER ;
```

The regular grammar still governs free relator phrases: `kontra` + currency phrase in base form. `monem` marks the *outgoing theme*, while `kontra mon` marks the *incoming consideration*. Proposed core exchange order:

```ebnf
Exchange        = "kambi" Incoming? Outgoing ;
Incoming        = "kontra" (CurrencyPhrase(base) | OrdinaryNounPhrase(base)) ;
Outgoing        = CurrencyPhrase(accusative) | OrdinaryNounPhrase(accusative) ;
```

Here `kambi` is a schematic root/imperative placeholder; normal finite forms will be needed for declarative sentences. Omitted Incoming defaults to `kontra mon` **semantically** when Outgoing is present. That means the countervalue kind is money but amount and currency are unspecified; the parser MUST NOT synthesize a fictional `uno` or currency code. A typed `mon` without quantity/code should represent a generic money concept and must be separately licensed if needed in full clauses.

**Example:**
`kambi kontra mon uno USD monem uno EUR`
= give one euro and receive one US dollar, as reciprocal exchange.

To avoid false conclusions, this example expresses a **1:1 nominal amount exchange**, not a claim that 1 EUR currently equals 1 USD in market value or that a broker would perform the deal at that rate.

### Boundaries / namespace safety

- A code is an external **typed identifier** only in the licensed `mon [quantity] CODE` construction; in other contexts its same letter sequence could be an ordinary lexeme or a parser error.
- Preserve the standardized three-letter uppercase spelling as external data. Currency codes do **not** become new Unisermo roots and never receive Unisermo case suffixes.
- `EURem` is not a valid replacement for `monem uno EUR`.
- A three-letter uppercase shape is only a **lexical precheck**; production validation should verify real ISO 4217 codes from a versioned canonical registry. Do not silently accept arbitrary `XYZ` as a real currency.
- Provisional surface syntax requires an explicit Unisermo quantity; decimal/fractional money amounts and currency-code validation/version pinning remain open.
- Keep an ordinary noun whose form matches a currency code distinguishable from the code; a future root `eur` does not alter `mon uno EUR`.
- Do not introduce global case-after-prefix movement. Ordinary noun phrases remain head-final and case-marked on their usual head.
- A parser should store outgoing/incoming separately, e.g. `{type:"exchange",outgoing:{type:"money",quantity:"uno",code:"EUR"},incoming:{type:"money",quantity:"uno",code:"USD"}}`. The monetary default is `{type:"money",quantity:null,code:null,implicit:true}`.
- The `kontra` relator is a *prospective* new lexical item. Test for collisions and decide its general or restricted use before canonization.

### Example and contrast table

| Surface (experimental) | Expected interpretation |
| --- | --- |
| `kambi kontra mon uno USD monem uno EUR` | pay 1 EUR, receive 1 USD |
| `kambi kontra mon uno EUR monem uno USD` | pay 1 USD, receive 1 EUR |
| `kambi monem uno EUR` | pay euros, receive unspecified money; forex possible |
| `kambi librem` | give a book for unspecified money; ordinary sale reading |
| `kambi kontra libr monem uno EUR` | pay 1 EUR to receive book |
| `kambi kontra mon uno USD monem uno USD` | exchange 1 USD for 1 USD, valid type but economically trivial |
| `kambi kontra mon uno usd monem uno EUR` | rejected by strict uppercase-code profile |
| `kambi kontra mon uno XYZ monem uno EUR` | syntactically plausible shape but code registry must confirm XYZ |
| `kambi kontra mon uno USD uno EURem` | rejected: no typed money head on the outgoing theme |

### Open decision

A globally *canonical* case-bearing monetary noun phrase should be defined in one place. The prefix-head pattern chosen here is intentionally scoped to the ISO-currency namespace; whether other standardized identifiers should use a related schema requires a later LDR, rather than automatic generalization.

## Evaluation and evidence

The prospective frames have been analyzed with English-level semantic contrast scenarios and typed-money fixtures. No successful grammar/parser validation is yet claimed. The scenario files are not gold-standard Unisermo sentences.

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

## Consequences and compatibility

Keep the existing seven-case inventory unchanged; introduce no arbitrary new meanings for `kun` or `per`. The currency-code namespace is deliberately bounded, and the parser lacks a ratified executable exchange frame pending implementation and adjudication.

## Decision authority

Owner requested exploration of `kambi` after analyzing `don`, `prest` and `vend`. This document captures an option, **not approval of lexical forms or new case roles**.

## References

- `language/noun_case_system.md`
- `language/derivation.md`
- `language/word_order.md`
- `formalization/data/valency_frames.json`
- `docs/ldr/LDR-0014-physical-action-valency.md`
