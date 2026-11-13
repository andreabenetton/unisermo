# Don: transfer perspective, UX command labels, and existing morphology

**Status: Experimental proposal, NOT ratified. 2026-11-13.**

## Source audit

The canonical `ad-/in-/de-/re-` bound prefix family denotes event **phase**: begin, continue, cease, resume (`language/derivation.md`, `language/verb_specification.md`). It does **not** encode allative/ablative direction, so `addon` would mean *begin to transfer*, `dedon` *cease transferring*, and **not** 'send'/'receive'. Existing `-ad` and `-de` are **bound nominal case suffixes**, not already independent free particles.

Bare verb roots are canonical imperatives. The user raised the UX example of an outgoing transfer button versus an incoming transfer button, suggesting `don ad` and `don de`. Those are **new elliptical constructions** and must not be represented as already grammatical.

## Candidate semantic base

`don` = transfer an item/information from a source to a recipient. Transfer-of-availability is a provisional common meaning; it does not inherently convey physical transportation, change of legal ownership, comprehension, or an automatic authorization. Decide whether `don` asserts **completed delivery** or **dispatch/attempt** before using it for a UI command that reports completed action.

Two participant perspectives:
- outgoing: actor/speaker acts as SOURCE, recipient identified with nominal `-ad`;
- incoming: actor/speaker acts as DESTINATION, source identified with nominal `-de`.

This alternating subject role is a **lexically licensed frame of `don`**, not a universal implication of `-ad/-de`.

Complete schematic clauses (not canon until root and valency approved):
- `i doni PAKE-em UMAN-ad` = I transfer a package to a person.
- `i doni PAKE-em UMAN-de` = I receive a package from a person.
- `i doni MESAJ-em UMAN-ad` = I transfer a message to a person.
- `i doni MESAJ-em UMAN-de` = I receive a message from a person.

The uppercase object labels are placeholders, **not ratified lexemes**. As originally specified, the double-sided `DON X-em A-de B-ad` leaves actor perspective unresolved; keep outside the licensed frame pending explicit treatment.

## UX microcopy alternatives

| Design | Outgoing button | Incoming button | Linguistic consequence |
|---|---|---|---|
| A: Elliptic free particles | `don ad` | `don de` | New optional **free directional/perspective words** `ad` and `de`; their distribution must be restricted or defined generally. Potential conflict with existing homographic bound case suffix and clause complement adjacency. |
| B: Perspective derivation | `donad` | `donde` | New **verbal derivational suffixes** `-ad/-de`; collide with nominal case meanings, require morphology precedence rules and productive scope definition. |
| C: Abstract complete imperative | `don DEST-ad` | `don SOURCE-de` | Uses existing noun cases and bare imperative, but requires a real context-known noun; placeholders are not UI copy and omission of X needs specific rule. |
| D: Context alone | `don` | `don` | No new grammar, but lacks distinction without interface cues, weak for accessibility and standalone labels. |

**Recommendation:** explore A as the *smallest orthographic UX change* and compare against B; but do **not** ratify A without deciding if `ad/de` are licensed only as tightly scoped postverbal perspective tags on a bounded class of converse verbs or if they are general free relators. A general new free relator could create avoidable redundancy with the noun cases. Do not imply all transfer verbs are reversible.

## Comparative semantic tests

- `don`: physical or informational transfer, no requirement that a message is comprehended. Explicit distinction between attempted dispatch and effective availability must be settled.
- `portar`: spatial transport with `-de/-ad` adjuncts, which **do not** change the subject's carrier role; spatial source/destination alone cannot produce 'receive'.
- `fer`: physical taking from a source, no entailment of ownership transfer; must not be conflated with `don`.
- `dok` teaching vs learning: not converse descriptions of one guaranteed outcome.
- `aut`: permission grant source `-de` is an existing verb-specific source slot and must not be reinterpreted as universal actor reversibility.
- `prest`, `vend`: investigate after `don`; loan includes a return condition, sale includes compensation and economic conditions. An extra condition may not always be expressible using only cases.

## Questions for acceptance

1. Is the UX notation `don ad` / `don de` an **elliptical construction for two command labels** or an operator productive across full clauses?
2. If full clauses, where does the perspective marker appear relative to objects, TAM, negation, modal heads and case-marked endpoints?
3. May `don` be used with **no overt object** in imperatives/UX, or is omitted object licensed only when recoverable from interface context?
4. Does `don` assert transfer completion, and what label describes an **attempted** but undelivered message?
5. How are source and recipient both represented without role ambiguity?

No modifications to `language/`, confirmed lexicon, parser or benchmark scoring should follow solely from this document. Any ratification should be recorded in a new LDR with owner approval, then tested against existing phase morphology and `aut/fer/portar` valences.
