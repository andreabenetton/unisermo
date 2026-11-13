---
id: LDR-0017
title: Directional perspective of transfer verb don in elliptical UX labels
status: Proposed
date: 2026-11-13
domain: grammar
supersedes: none
---

# LDR-0017 — Transfer perspective for `don` and UX labels

## Context and problem

The project owner proposed using a single general transfer root, `don`, for transferring objects and messages, and directional labels `don ad` (send) / `don de` (receive). This reduces independent lexical roots. The purpose of this record is to specify a falsifiable, constrained design before changing normative grammar.

**Important:** `don`, free `ad`, and free `de` are NOT currently ratified by this LDR. Existing bound nominal suffixes `-ad` (recipient/destination) and `-de` (source) are ratified; they do not automatically license standalone words. Bound `ad-`/`de-` are phase prefixes (begin/stop) and must never be repurposed as send/receive. The bare lexical root is an existing imperative form, but the new tag construction needs explicit authorization.

## Alternatives

A. Lexicalize separate send/receive roots: simpler syntax, redundant transfer semantics.
B. Repurpose phase prefixes `addon`/`dedon`: **reject**, contradicts already ratified begin/cease semantics.
C. Fuse suffixes `donad`/`donde`: compact, but creates ambiguous new verb morphology conflicting with nominal case suffixes; more invasive.
D. **Candidate:** restricted postverbal free perspective tags `don ad`/`don de` in contextually recoverable ellipsis; no unrestricted new relator or prefix.
E. Two context-free `don` buttons: valid as imperative alone, but fails to distinguish inward/outward transfers for usability and accessibility.

## Precise experimental hypothesis

Treat `don` as a transfer-event verb, initially with a **completed effective-availability** interpretation, whose transferred theme may be physical or informational. It does NOT itself entail physical transport, ownership change, legal permission, comprehension, or belief. The transferred theme is in accusative `-em` when overt. In full clauses, nominal `-ad` marks destination and nominal `-de` marks source, retaining their existing meanings.

For the **two perspective-specific frames** of `don` (not general case grammar), when only the recipient or only the source is overt:
- `SUBJ don-FIN THEME-em RECIPIENT-ad`: subject = source/giver, recipient is RECIPIENT.
- `SUBJ don-FIN THEME-em SOURCE-de`: subject = recipient/receiver, source is SOURCE.

This alternation is a property of the proposed `don` valency, **not** something allowed for `portar`, `fer` or `aut`. Full `don THEME-em SOURCE-de RECIPIENT-ad` remains unspecified because the source/recipient endpoints do not determine what role the finite subject has. Do not implicitly assign one.

For **UX labels only**, in a context where the user is the relevant source or recipient and the theme is identified by interface context, permit an experimental *root + separate direction word* surface:
- `don ad` : **Send / give outward**, user = source, theme implicit.
- `don de` : **Receive inward**, user = recipient, theme implicit.

These tags encode the **perspective of the implied user**, not a second participant or a bound nominal argument. They are NOT licensed as freestanding noun-case words elsewhere; `donad`, `donde`, `addon de`, `i doni ad`, and arbitrary `V ad/de` remain outside this proposed minimum. No global rule that UX ellipsis changes the semantics of other verbs is implied.

## UX actions versus completed events

A button label is a **requested operation**, not a true assertion that delivery has already completed. Distinguish clearly:
- `don ad` = action/intent to send, not a status equivalent to "sent successfully".
- `don de` = action/intent to receive/retrieve, not a status equivalent to "received successfully".
- A confirmed successful transfer, a dispatch attempt, and an undelivered message remain separately reportable only after their aspect/event semantics are explicitly defined.

For communication, receipt of a message does not imply reading, understanding or agreement. For physical items, received availability does not imply legal title or physical transport by the giver.

## Explicit acceptance and falsification criteria

1. Preserve `admov` begin moving, `demov` stop moving, `adportar` begin carrying and `deportar` stop carrying; no negative transfer effect.
2. `don ad` and `don de` are interpreted distinctly in isolated UX labels **without relying on surrounding English translation**.
3. The distinction does not silently generalize to `portar ad`, `fer de`, `aut ad`, or `dok de`.
4. A complete transfer sentence with an overt source-only or destination-only phrase gets one unambiguous role assignment; double-endpoint surface is treated as underspecified.
5. Intent from a button click is never scored as evidence of success, and receiving a message does not entail comprehension.
6. Provide specific adjudication for lexical valency and separate UI label semantics before using examples in a scored LLM corpus.

## Test design

Draft contrast fixtures are maintained in `research/grammar/don-ux-probes-001.json`. These are **synthetic tests of the proposed semantics**, not parser outputs or gold-standard scored comprehension items. Before accepting, review the fixtures independently, test with native/learned-language readers and LLMs in isolated conditions, and compare alternative C.

## Consequences and compatibility

No modifications to current canonical `language/` files, `formalization/data/`, or the confirmed lexicon at proposed status. The proposal adds one candidate transfer root `don` and exactly two narrowly licensed prospective UX labels, without giving the nominal suffixes an unrestricted independent-word role. A later Accepted LDR would define lexical valency, omitted-theme rule and parser/UI handling before production use.

## Decision authority

Project owner requested the analysis of existing prefixes and the continuation of `don ad`/`don de` exploration. **No explicit acceptance of the final restricted operator design has yet been recorded.** This LDR is Proposed until approved.

## References

- `language/derivation.md`
- `language/verb_specification.md`
- `language/noun_case_system.md`
- `formalization/data/valency_frames.json`
- `research/grammar/don-ux-probes-001.json`
