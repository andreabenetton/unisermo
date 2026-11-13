# Temporal interval relations: seven-family design (proposed)

**Status: author-selected candidate forms; semantics and grammar NOT YET RATIFIED. 2026-11-13.** Research on PR #86. This proposal supersedes the earlier `ante/post` and endpoint-concatenation design **for research purposes**, without changing canonical `tem` or authorizing parser acceptance.

## Choice and motivation

User-selected forms: `pretem`, `tem`, `postem`, `sim`, `solap`, `simpre`, `simpost`. The long endpoint compounds (`postpretempre` etc.) are **abandoned**. Both BEFORE and AFTER remain independently expressible. `pretem` and `postem` are proposed derivations involving listed `pre-` and `pos-`; **productive derivation on function words is not canonically licensed**. Their acceptance would be a specific lexical decision, not a blanket grammar rule. The free word `tem` is already confirmed as *at/during + nominal time phrase*; clause-to-clause event relation and stricter interval semantics are NOT confirmed.

Assume two distinct, **bounded positive-duration event instances** A=[a0,a1], B=[b0,b1], a0<a1, b0<b1. Event instances must be identifiable and occur in a compatible temporal frame. Propositions with negation, hypotheticals, habituals, unbounded states, point events, modality and nested coordination require separate design. Each syntactic expression below is **metalanguage**: `A REL B` is not yet a licensed Unisermo sentence.

## Thirteen exhaustive, mutually exclusive Allen relations

| Allen ID | Condition | Proposed expression | Gloss |
| --- | --- | --- | --- |
| before | a1 < b0 | `A pretem B` | A wholly before B |
| meets | a1 = b0 | `A sim B` | A ends exactly when B starts |
| overlaps | a0 < b0 < a1 < b1 | `A solap B` | A starts first; overlaps part of B |
| starts | a0 = b0, a1 < b1 | `A simpre B` | same onset; A ends earlier |
| during | b0 < a0, a1 < b1 | `A tem B` **proposed narrow sense** | A strictly inside B |
| finishes | b0 < a0, a1 = b1 | `A simpost B` | same offset; A starts later |
| equals | a0 = b0, a1 = b1 | `A ekwal B` **candidate typed equality** | exactly same temporal extent |
| finished_by | a0 < b0, a1 = b1 | `B simpost A` | inverse of finishes |
| contains | a0 < b0, b1 < a1 | `B tem A` **proposed narrow sense** | inverse of during |
| started_by | a0 = b0, b1 < a1 | `B simpre A` | inverse of starts |
| overlapped_by | b0 < a0 < b1 < a1 | `B solap A` | inverse of overlaps |
| met_by | b1 = a0 | `B sim A` | inverse of meets |
| after | b1 < a0 | `A postem B` | A wholly after B |

`ekwal` is already a confirmed comparison word ('equal'), **not yet** an approved event-interval identity construction. Using `A ekwal B` to compare temporal spans without implying identity of events requires explicit typing/scope rules. So the table covers all 13 *semantically*, but **the 13th construction is not yet grammatically licensed**. Alternatives: dedicated event-time equality use of `ekwal` or two weak-containment assertions, which would require loosening `tem`.

## Non-negotiable disambiguations

- `sim` is directional **meets**, not vague simultaneous occurrence. `A sim B` is *not* equivalent to `B sim A`. Although the root suggests simultaneity, its specific argument roles need explicit teaching.
- `solap` is a **directional partial overlap**, not arbitrary intersection. `A solap B` is not equivalent to `B solap A`.
- `simpre` denotes shared START **plus A ending earlier**; `simpost` denotes shared END **plus A beginning later**. Bare onset equality alone would also permit complete equality, violating Allen's exclusive partition.
- `tem` currently covers 'during / at the time of' as a **prenominal** relator. It is not already a strict interval relation, and can naturally be used about a point or all-day time reference. Its proposed strict event-to-event meaning must be explicitly authorized, or replaced with a distinct narrow event-only word/typed construction.
- `postem` is orthographically `pos-` + `tem`, not `post-` + `em`; its final `t` comes from `tem`. Existing separate `pos` is the 'situational possibility' verb, not a temporal relator.
- A diagram of the seven canonical directional families does **not** mean 'all overlapping periods': before/meets/equals and starts/finishes belong to different boundary patterns.
- Equality of timestamps versus equality of event identity: different events may occupy exactly the same interval.

## Corpus examples (Italian meanings; not accepted Unisermo translations)

1. `A pretem B`: La colazione è finita prima che iniziasse il lavoro.
2. `A sim B`: Il primo turno finisce esattamente quando comincia il secondo.
3. `A solap B`: Ho iniziato a leggere prima che cominciasse la musica; ho smesso mentre la musica continuava.
4. `A simpre B`: La registrazione e la lezione sono iniziate insieme, ma la registrazione è terminata prima.
5. `A tem B`: La riunione è iniziata dopo l'inizio del turno ed è finita prima della sua conclusione.
6. `A simpost B`: La telefonata è iniziata durante il viaggio, e sono terminate insieme.
7. `A ekwal B`: La registrazione copre esattamente lo stesso intervallo della prova.
8–13. Invertire i due argomenti nelle relazioni (2–6), e usare `postem` per l'inversa di (1), secondo la tabella.

## Lexical screening: confirmed lexicon (138 entries)

No exact matches were found for `sim`, `solap`, `simpre`, `simpost`, `pretem`, `postem` in `research/lexicon/confirmed_lexicon.json` as of 2026-11-13. Existing `tem` and `pos` are confirmed, and `ekwal` is confirmed with a broader equality/comparison value. No spoken comprehension or grammar/parser test has been run. Not having an exact match is **not** sufficient for final lexical ratification; investigate spoken confusability of `sim` and whether `solap` is accessible beyond Romance speakers.

## Next ratification decisions

1. Should `tem` retain its broad canonical nominal 'during' meaning while adopting **strict** containment only with two bounded event clauses, or should the event–event relation also be broad?
2. Can `ekwal` explicitly compare the **time extents** of two events rather than the event identities? If not, choose a typed frame or new concise form.
3. Approve `sim` as *directional endpoint contact* rather than broad simultaneity, and accept `simpre`/`simpost` as exclusive relations (not onset/offset equality alone)?
4. Specify the syntax and precedence for `P REL Q` where P/Q are finite propositions, rather than treating letters A/B or Italian descriptions as valid Unisermo.
5. Test the word set orally and against parser capabilities before adding translations to UCUB-v2.

No canonical grammar, lexicon, parser or benchmark-gold translation is changed by this document.
