# UCUB-v2 — Temporal relations and reference: research RFC

**Status: PROPOSAL / UNRATIFIED. 13 November 2026.** This document contributes a design candidate to PR #86. No new word, syntax, temporal semantics, parser rule, or benchmark translation is canonized here. All examples containing `ante`, `post`, or clausal `tem` below are **schematic and MUST NOT be treated as accepted Unisermo or parser fixtures**. The capital letters P/Q/R are metalanguage, not words.

## 1. What already exists

Checked against `language/verb_specification.md`, `language/noun_case_system.md`, `language/questions.md`, `language/word_order.md`, `language/derivation.md`, `formalization/GRAMMAR_COVERAGE.md`, accepted LDR-0023/24/27/28 and the confirmed lexicon:

| Existing element | Canonical meaning / constraint | Does NOT by itself mean |
| --- | --- | --- |
| Finite `Ø / -d / -f` | present, past, future | event A before or after event B |
| Aspect `Ø / -e / -o` | simple, progressive, completed/perfect | already, still, then, or order across clauses |
| `tem NP` | at/during a **nominal** time expression (`tem dia` appears as an example) | while an entire **finite proposition** P |
| `-in` | location or abstract domain of reference | a temporal case or time-before/time-after |
| `kan` | interrogative **when?** | an already approved temporal subordinating conjunction |
| `se P alor Q` | condition and explicitly separated consequence | narrative event-after-event |
| `lim` | scoped boundary in *licensed* connector constructions | a freely insertable event/time boundary |
| `in-` / `ines` | phase persistence: continue to move / remain in a state | every pragmatic reading of still / not yet |
| `sekun`, `gram`, quantitative operators | numeric durations and scalar comparisons | deadline relative to an event, elapsed-time-of(A,B) |
| tensed propositional heads (LDR-0024) | embedded time relative to assessment time in specifically licensed frames | arbitrary general event–event ordering |

The verb root `pos` already means situational possibility, and the written `pos-` is also a listed bound derivational prefix: **do not reuse bare `pos` for after**. The historical mention of `pre-/pos-` among derivational prefixes does not license independent temporal connectives. `tem` is ratified as a free **nominal** relator, not a free clause connector. The parser's present support is narrower than the canonical language in other areas; do not conflate parser rejection with language impossibility.

## 2. Semantic goals: three conceptual relations with explicit BEFORE and AFTER

The purpose is to relate event times rather than add a tense/aspect slot. Abstract event clauses `P` and `Q` have their own actor, verbal aspect and tense.

### A. STRICT-BEFORE: candidate new free relation `ante`

**Preferred initial design**: `P ante Q` = the salient event denoted by P precedes the salient event denoted by Q. For a first precise, bounded subset **where both events have known start/end boundaries**, use `end(P) < start(Q)` (strict non-overlap); simultaneous boundaries and overlap are not silently "before".

`ante` is a candidate orthography derived from the international/Latin *ante* family. This preserves an explicit, independent BEFORE relation in the everyday vocabulary. The speaker should not be forced to invert the narrative just to say AFTER. The logically equivalent converse exists but does not replace a lexical AFTER expression.

**Important limitations**: natural-language "before" often targets *onset* rather than *completion*. For "I started reading before the phone rang", the P operand must denote **starting to read**, not the entire reading interval. This can be represented with independently specified event-phase semantics where available. Do not generalize `end(P) < start(Q)` to open-ended states, negated non-events, modal possibilities, or all discourse contexts until reviewed. Temporal anchoring of future/non-actual events is evaluated in the same modal/discourse world, not automatically asserted to have already occurred in reality.

### B. STRICT-AFTER: proposed free relation `post`

**Updated owner direction (13 November 2026):** retain BEFORE and AFTER as two independently accessible human concepts; do not make the listener/speaker reverse operands to express one of them. Suggested spellings: `ante` / `post`. This direction favors a **two-word symmetric temporal design** over the earlier one-primitive economy argument, but the interrogative suggestion `ante e post ?` is **not an explicit ratification of either spelling or syntax**.

Proposed `P post Q` = event P occurs after event Q; in the same restricted bounded-event interpretation, `end(Q) < start(P)`. Both forms are strict temporal relations for the initial design:
- `P ante Q` = P before Q.
- `Q post P` = Q after P (equivalent truth conditions, different preferred conceptual framing).
- `Q ante P` = Q before P, **not** the same as `Q post P`.

**Phonological/lexical caution:** `post` is orthographically permitted and internationally recognizable, but is just one final /t/ away from confirmed `pos` (situational possibility) and one /s/ away from confirmed `pot` (capacity). Some accents may reduce final /st/ clusters. These are **near-collisions**, not exact orthographic homonyms, and syntactic position often disambiguates, but a high-frequency temporal connector deserves explicit spoken-perception testing. `poste` (/pos.te/) is a candidate fallback if `post` proves too fragile. Neither is confirmed. Existing `pos` and bound `pos-` retain their original meanings. No proposal should rename the confirmed modal.

No new final consonant-cluster prohibition is inferred from the alphabet specification; review of intelligibility under accent variants is still required.

### C. DURING/OVERLAP: extend **existing** `tem` to clauses

Existing, canonical: `P ... tem TIME_NP` or `tem TIME_NP` as an adjunct, with nominal time expression.

**Proposed extension**: `P tem Q`, where Q is a finite event/state proposition. It encodes that the salient occurrence or state of P has nonzero temporal **overlap** with Q (the precise 'at/during' interpretation depends on the event's time scale). It **does not** say P caused Q, happened because of Q, followed Q, or was wholly contained in Q's duration. Full temporal containment may require a later explicit scope/extent marker.

This is a new **valency/syntax** for an existing free word, not another root and not a claim that the current parser supports it. A point event inside a durative event is a natural application. Simultaneous onset is a stronger condition than overlapping intervals; do not assign it automatically.

### C. "When": resolve its sense, not a single translation token

Italian *quando* can mean:
- Interrogative when? — existing `kan` (**ratified**).
- While / at the time P occurs — candidate `P tem Q` overlap (**not ratified for clauses**).
- Conditional/habitual 'whenever P' — distinct from purely temporal coincidence; existing `se` expresses an **if** condition but its general habitual/universal frequency is not automatically ratified.
- 'As soon as P' — an **event boundary + minimal-delay** relation, not mere `tem`.
- 'After P' — ordering of events, possible inversion of candidate `ante`.

Do not make `kan` simultaneously a direct interrogative, indirect interrogative, and temporal subordinator by fiat.

## 3. Chronology vs aspect, phase and expectation

- `-o` (completed/perfect) does **not** entail earlier-than-expected `already`. "Had departed" is not necessarily "had *already* departed".
- `inmov` and `ines STATE` can express persistence, which covers a **subset** of 'still' readings. "Still" can convey prior continuity, persistence contrary to expectation, or a discourse contrast; avoid defining these pragmatic readings merely by morphology.
- `dees` can mark departure from a state, but does not automatically provide the full sense of 'not anymore' with a specified reference moment.
- "Yesterday", "today", "this morning", "now" need an **utterance-time anchor + conventional interval**. Past `-d` alone cannot choose a calendar day.
- "Within ten minutes" needs a **bound on elapsed time between an anchor and an event**. The accepted quantitative expressions and `sekun` provide duration values but not a general operator for elapsed-time(A,B), and minute is not a currently approved unit.
- "Only after" contains a **focus/exclusion** or minimal temporal threshold not automatically supplied by ordinary event ordering.

These are separate gaps: **temporal order (before/after)**, **temporal overlap**, **deictic anchor**, **elapsed duration bound**, and **expectational/discourse adverbs**. Keep them separate to avoid ad hoc overloading of `-o`, `in-`, `tem` or `no`.

## 4. Proposed initial syntax and parser boundary (not approved)

**Schematic forms; P and Q are single event-bearing finite clauses**:

```text
P ante Q     -- P precedes Q (bounded-event subset)
Q post P     -- Q follows P (same ordering; independently available wording)
P tem Q      -- event/state intervals of P and Q overlap (new clausal tem)
```

The bare `P ante Q` is an **infix** temporal relation, unlike the existing **prenominal** `tem NP`; clausal `tem` is a proposed extension by analogy with dual nominal/clausal `due`. In a future syntax, choose a single explicit relationship node rather than giving `ante` or `post` arbitrary precedence over `e`, `o`, `ma`, `due`, `se`, etc.

Suggested AST model only after ratification:
```json
{
  "type": "temporal_relation",
  "relation": "strict_before | strict_after | overlap",
  "left": "<finite-clause-ast>",
  "right": "<finite-clause-ast>",
  "reference_semantics": "bounded-events-only for strict_before",
  "semantic_validation": "not_inferred_by_parser"
}
```

**Fail-closed initial subset**: single finite clauses with independently identifiable event referents. Do not silently accept `P ante Q e R`, nested `se/etsi` + temporal expressions, bare wide `no lim` across temporal operators, negated *absence* clauses as event anchors, embedded interrogatives, conditional imperatives, or `ante` + a bare nominal time point unless distinct operand typing/scope is specified. Event–event temporal syntax and event–time-NP syntax are *not* interchangeable by assumption. A parser success should report structural acceptability, not that an event occurred or a natural-language 'already' implication is correct.

**Positive contrasts to eventually test** (metalanguage, not valid Unisermo sentences):
- P before Q vs P after Q should be distinct and mutually inconsistent for single non-overlapping bounded event **instances**.
- P before Q and Q after P should be truth-conditionally equivalent, while retaining distinct lexical/conceptual viewpoints.
- P during Q is compatible with P beginning before Q finishes; it doesn't force strict precedence.
- "P happened, and Q happened" does not entail an ordering.
- Both past-tense P and past-tense Q do not entail which happened first.
- Completed P doesn't entail "P already happened earlier than expected".
- P before Q does not entail Q caused P, nor vice versa.
- A negated non-event is not automatically an event instance.
- Reported time relative to past assessment (LDR-0024) is not automatically relative to today's speech moment.

## 5. Which of the 36 targets benefit, and which remain blocked?

| UCD2 | Need | What the proposed basic relations would fix | Remaining issues |
| --- | --- | --- | --- |
| 03 | "called when he arrived" | `tem` overlap **if** the intended anchor is co-occurrence | identify actor; arrival root; point/boundary sense of when |
| 06 | "arrive after sunset" | `arrival-event post sunset-event` in event/event formulation | lexical sunset/train/delay; time-noun syntax if using a noun; future and conditional scope |
| 12 | "after correcting, sent document" | `sending-event post correcting-event` if correction completed first | document/informational send; object identity |
| 16 | "sent this morning" | nominal `tem` may be relevant | current-day morning as a temporal anchor; informative transfer |
| 18 | "said he wouldn't come" | none directly | reported speech, future relative to past speech, referents |
| 20 | "wait before entering" | wait-event `ante` entry-event conceptually | obligation over event sequence, wait/enter roots |
| 24 | "now understands" | none directly | `now` deictic anchor, knowledge/causal indirect question |
| 30 | "within ten minutes" | none directly | elapsed-time deadline and unit, arrival |
| 34 | "met friend yesterday, then returned" | return-event `post` meet-event | yesterday/return/information roles |
| 35 | "already left, still at station" | persistence phase may cover a subset | already expectation, still reference, station/depart |
| 36 | "took, showed, and only after sent" | take `ante` show; send `post` show | triple coreference, **only after**, lexical transfer |

This proposal reduces several structural gaps but does **not** make all 36 scenarios currently expressible, and does not imply complete model comprehension.

## 6. Updated choice architecture and recommendation

The owner explicitly prefers **two conceptually distinct ways of expressing temporal order**: BEFORE and AFTER. Although AFTER is the logical inverse of BEFORE, that logical redundancy is not a linguistic defect. Speaker and listener can choose the event as the grammatical anchor without mental operand inversion.

| Design | New lexical candidates | New proposed clausal relations | Benefits | Risks |
| --- | ---: | ---: | --- | --- |
| **A (preferred on owner direction)** `ante` + `post` + clausal `tem` | 2 | 3 | natural direct before/after wording; structurally symmetric; maintains clausal overlap | `post` near `pos`/`pot`; test accent robustness |
| B: `ante` + `poste` + clausal `tem` | 2 | 3 | retains both perspectives; safer phonetic distance from `pos` | extra syllable; less terse |
| C: `ante` + clausal `tem` only | 1 | 2 | one fewer word | rejected as default: requires reversing operands to say after |
| D: use TAM and phase as event order | 0 | ad hoc | briefly appears concise | does not specify independent ordering |

**Recommendation pending explicit form ratification**: adopt conceptually independent BEFORE and AFTER (owner preference), screen `ante` and `post` for lexical and spoken collisions, and extend `tem` to clausal overlap only after semantic review. Keep bounded-event strict semantics as the initial hypothesis, not a universal meaning for every natural-language before/after sentence.

### Open decisions that should be settled deliberately

1. Is strict `end(P) < start(Q)` the preferred **unmarked** event-order semantics, or should before attach only to a pragmatically selected landmark (e.g., onset)? Strong default avoids ambiguity but forces explicit onset framing when events overlap.
2. Direct AFTER is now the user's stated design preference; decide whether the surface root `post` remains sufficiently distinct from `pos` and `pot` in spoken use, or select `poste` after screening.
3. How do event-time **nominal anchors** ("after sunset") compose with clauses without an unwarranted new general nominalized-event suffix?
4. How do temporal expressions take scope under `no`, `pos/deb`, `se`, conditionals and `lim`?
5. Do we need an optional relation for immediate succession ('as soon as') distinct from ordinary before?

### Next empirical step

Create 8–12 **non-benchmark** diagnostic trials: bounded event pairs in past/present/future, converse after, temporally overlapping event/state, onset-before-overlap, and interpretation of "already"/"still" as controls. Collect free Italian interpretations, not repeated Italian alternatives. For any actual Unisermo samples, first ratify the relation forms, perform phonological/collision screening, run the parser, then obtain independent gold-equivalence review. Keep UCUB-v2 target file with `unisermo: null`.
