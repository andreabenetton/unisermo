# UCUB-v2 — feasibility audit of 36 Italian-first communication targets

**Status: research-only; no new Unisermo root, valency, case, connector, translation, parser pass, semantic gold or benchmark has been ratified.** Date: 2026-11-13. Source: [36-case design](proposals/communicative_diversity_36.json) and [machine-readable per-case audit](proposals/communicative_diversity_36_feasibility_audit.json).

## Audit method and caveats

This is a **static source review**, not 36 executed parser tests or a formal mathematical proof of expressibility. References: `language/`, `research/lexicon/confirmed_lexicon.json`, `formalization/data/lexicon_index.json`, `formalization/GRAMMAR_COVERAGE.md`, accepted LDR-0019, 0023–0028, and proposed LDR-0018. The parser inventory is not an oracle about grammatical possibility, and source-attested examples are not all canonical confirmed-lexicon entries. Do not fill `unisermo` in the benchmark from a speculative gloss.

Classification:
- Lexical: **ready_or_attested** 6 (no obviously missing everyday concept but some example-only words); **missing_common** 15; **missing_many** 15.
- Grammar: **documented** 6 (only the core construction); **needs_semantic_review** 12; **requires_design** 18.
- Parser: **documented_subset_likely** 3; **partial_or_unverified** 12; **outside_documented_subset** 21. None of these is a tested parser pass.
- No translation is approved. Even **documented** grammar does not certify reference identity, temporal interpretation or lexical equivalence.

### Newly ratified capabilities that must not be counted as lexical or grammatical gaps

- `i kred P`, `i sap P`, `i vol P` and other lexically licensed bare-head finite-proposition complements are accepted (LDR-0023); the outer subject is expressed. `sap P` is factive under positive assertion, `kred P` is not.
- LDR-0024 accepts personless temporal operator heads (`posd`, `vold`, `sapd`) and impersonally interpreted propositional necessity `deb P`; this is not the personal duty `debi V`. Embedded tense is relative to evaluation time within that frame.
- `lik CARDINAL ORDINAL P` is already ratified for numerical likelihood, including 70% as `setdek senim`; no grammar-level >100% ban (LDR-0026). Qualitative vs exact probability uses the same `lik` scale (LDR-0025).
- Quantitative comparisons, `sirka` and `inter`, are accepted (LDR-0027); `gram` and `sekun`, and shared-unit interval ellipsis, are accepted (LDR-0028). A **minute** unit and event deadline semantics are *not* thereby ratified.
- Physical `fer` and `portar` with optional source/destination have ratified typed valencies (LDR-0014). Transport to a recipient does not entail completed delivery.
- `dokor` is transparently derivable from confirmed `dok` and agentive `-or`; `kuraror` does not automatically mean a credentialed medical doctor. `dom` (house), `amik` (friend), `student`, `vid`, `tik`, `tes` and some numeral forms are attested in normative examples, but `formalization/data/lexicon_index.json` records `example_only` for several of them. Do not misreport all of those as newly confirmed dictionary entries.
- `remov` means resume motion, not return home; `inmov` means maintain motion, not enter a room. `fer` means physical taking, not purchase; `kambi` remains a proposal, not canonical purchasing vocabulary.

## Case-level triage

| ID | Meaning, abbreviated | Main blocking issue | Next step |
| --- | --- | --- | --- |
| 01 | Mother sees brother's house | attested-only house/see; possessor attachment | confirm lexicon provenance; review genitives |
| 02 | Maternal grandmother carries water | whose sister?; transport vs delivery | explicit co-reference |
| 03 | Cousin calls mother on arrival | when-clause; arriving and subject identity | temporal clause semantics |
| 04 | Carry water from house to friend | `portar` covered; home/friend example status | baseline physical valency |
| 05 | Station closer than hospital | missing location nouns + proximity; comparative parser | lexicalize property and parser check |
| 06 | Late train arrives after sunset | temporal sequencing + travel lexicon | general temporal design |
| 07 | This door open, that closed | attested deixis, `porta/aper/klus` | simple two-clause calibration |
| 08 | Keys on table, not in bag | surface location; local contrast scope | spatial and focus design |
| 09 | Window closed because cold | window/cold; weather-like predicate | distinguish state vs caused closure |
| 10 | Teacher teaches three students | `dokor` possible; teaching recipient valency | register frame, check student status |
| 11 | Know how to explain, not apply | lexicon and cross-clause object identity | approve roles and co-reference |
| 12 | Correct then send document | event order, document identity, missing nouns/verbs | event sequencing |
| 13 | Doctor treats patient | distinction occupational vs agentive; patient roles | medical lexicon/valency |
| 14 | Able to help but not permitted | `pot` vs `aut` available, help missing | modal contrast + reference |
| 15 | Walk despite pain | nominal concession, persistence of activity | concession/phase distinction |
| 16 | Sent message this morning | information transfer, 'this morning' | message lexicon + deixis |
| 17 | Answer clear, question ambiguous | quality ambiguous distinct from 'unclear' | communication lexicon |
| 18 | Said would not come; disbelief | speech complement `dik P`, future-in-past | reported speech |
| 19 | Illegal, not necessarily immoral | moral antonym and propositional `deb` domain | semantic scope review |
| 20 | Wait before entering | duty covered; event precedence, enter | reusable temporal constructs |
| 21 | Entry permitted; manager denied it | permission state vs act granting/denying | authority-event valency |
| 22 | Believe the result correct | `kred P` covered; factual correctness | precise correctness quality |
| 23 | Know change; not who changed it | embedded wh and change event | indirect question design |
| 24 | Thought knew; now knows why wrong | `pens P` and embedded why | attitude/wh temporal design |
| 25 | Returned because rain | rain; return is not `remov` | rain + return lexicon |
| 26 | If door shut, do not enter | conditional with imperative | imperative consequent scope |
| 27 | Though simple, not necessarily easy | easy vs simple, `no deb P` in concessive | modal-concessive composition |
| 28 | Three persons waiting in room | ordinary wait/room roots | easy lexical calibration |
| 29 | Two of five parcels heavier | subset / others, measurable comparison | partitive semantics |
| 30 | Vehicle arrives within 10 minutes at 70% | `lik` 70% covered; deadline, minute unit | temporal bound and quantity |
| 31 | How many books bought? | exchange/countervalue still proposed | don't silently equate take/buy |
| 32 | Why move chair from room? | chair/room, source valency on transitive `mov` | validate frame |
| 33 | Who authorized transfer, and when? | granting act and compound interrogative scope | event roles + coordinated wh |
| 34 | Met friend yesterday, then returned | yesterday, sequencing and return | temporal deixis |
| 35 | Believed already departed, still station | already/still, travel terms, co-reference | time/aspect and reference |
| 36 | Took, showed, then sent same document | sequentiality + identity of same object | narrative semantics |

**Note:** targets themselves are natural-language requirements, not literal output expectations. Examples 02, 03, 18, 23 and 36 may have unresolved referents in Italian. Resolve ambiguity *before* translating, not by choosing a convenient Unisermo reading afterward.

## Lexical expansion — concept priorities, not invented canon

Avoid 36 sentence-specific coinages. Separate *concept need* from *surface spelling* and only propose roots after corpus-frequency benefit, cross-language recognizability, phonological legality, collisions with confirmed and inflected forms, and argument-role specification.

| Priority | Semantic cluster to examine | Reuses / pitfalls |
| --- | --- | --- |
| P0 | Temporal relation: before, after, then, when-as-subordinator, yesterday, now, already, still, deadline | `tem` = at/during, not universally before/after; `kan` = interrogative when. Check if operators can be composed without new primitives |
| P0 | Information object and transfer: document, message, communicate/forward/send, show, answer/question, explain | `dik` means say, `vok` call; physical `portar` is not informational sending; potential general transfer lexical family needs review |
| P0 | Event/coreference: same referent across clauses, embedded wh, completed event then next event | These are **grammar/semantics** issues, not fixed by more nouns |
| P1 | Basic objects/places: room, window, table, bag, keys, chair, book, parcel, station, hospital | Broadly reusable basic nouns; audit `dom` and attested forms before selecting duplicates |
| P1 | Movement: enter, depart, arrive, return, meet, wait, walking | `mov` is generic; `inmov` is not enter; `remov` is not return |
| P1 | Properties: cold, near, ambiguous, factually correct, easy, simple, wrong, heavy | Do not map `klar` to both clear and unambiguous by fiat; `just` primarily justice |
| P1 | Human roles / abstract items: patient, physician, colleague, student, rule, result, problem, solution | Agentive -or is not equivalent to professional credentials |
| P2 | Travel/weather: train, vehicle, delay, sunset, rain | Could be postponed until core temporal machinery exists |
| P2 | Commerce: commercial acquisition, exchange, money/price, buy/sell | `kambi`/`kontra`/`mon` remain proposals in LDR-0018 |
| P2 | Quantities/measurements: minute, weight, time-window | `sekun` is confirmed; derive/lexicalize minute and weight separately |

### High-yield first candidate batch: semantic concepts only

1. `ROOM`, `WINDOW`, `TABLE`, `DOCUMENT`, `MESSAGE`, `RULE`, `RESULT` (nouns).
2. `WAIT`, `ENTER`, `ARRIVE`, `RETURN_TO_PLACE`, `SEND_INFORMATION`, `SHOW`, `EXPLAIN`, `APPLY_RULE` (action frames).
3. `BEFORE_EVENT`, `AFTER_EVENT`, `WHEN_SUBORDINATE`, `NOW`, `YESTERDAY`, `ALREADY`, `STILL` (time/event relations).
4. `PROXIMITY`, `AMBIGUITY`, `FACTUAL_CORRECTNESS`, `EASE`, `SIMPLICITY` (properties).

These English uppercase names are semantic placeholders only, **not proposed written Unisermo forms**. Before adopting any root, check whether it reduces to an existing productive derivation without semantic loss. In particular, a standalone "learn" is deferred in LDR-0019 because `adsap` may encode knowledge acquisition.

## Grammar/semantic decisions to test before any ratification

1. **Time/event order.** A general relation of temporal precedence and an anchored deictic time inventory; avoid lexicalizing a special 'then' for each story. Disentangle completed aspect from before/after and from bounded deadlines.
2. **Propositional complements.** Existing `sap P/kred P` are licensed; `dik P` reported speech and `pens P` thinking require *lexical-valency* decisions. Embedded `kis/ker` questions are not licensed merely because direct questions exist.
3. **Reference/ellipsis.** Pronouns and genitives already exist, but semantic binding across 2–3 linked clauses is not executable. Define whether omission, repetition or explicit identity can be used without generating accidental ambiguity.
4. **Spatial contrast/focus.** "On X not in Y" requires location relation, constituent negation and pragmatic scope, not only the existing predicate `no`.
5. **Event valency.** Document destination/source/object roles for `dok`, `dik`, `kurar`, `mov` with origin, `aut` authority decisions and information transfer.
6. **Compound sentence forces.** Check `se P alor IMPERATIVE`, combinations of `etsi` and `no deb P`, paired questions and numeric-partitive comparisons without assuming fully general parser composition.
7. **Moral scope.** "Illegal but not necessarily immoral" needs exact moral property and modal domain; `no deb P` is not permission nor personal lack of duty.

## Recommended admission process for UCUB-v2

1. Record intended Italian meaning and clarify coreference/temporal assumptions independently.
2. Check `confirmed_lexicon.json` for each primitive, then `language/` for licensed productive derivation and source-attested examples; do not treat example-only as core ratification.
3. Record lexical missing concepts and grammar decisions independently. Prefer swapping out **some** scenarios with naturally distinct already-expressible situations for a first pilot, while keeping true gaps in the coverage backlog.
4. Ratify a small reusable lexical batch and frames as separate LDR(s), only with owner approval.
5. Compose complete Unisermo sentences; execute parser *after* composing; capture exact parser errors, not inferred success.
6. Obtain independent semantic equivalence review: one Unisermo passage per reviewer, blind free-translation preferred for primary comprehension; separate gold adjudication.
7. Freeze the benchmark after review, with explicit first-version admitted subset and separately documented excluded targets. Never silently backfill the historical 80-case diagnostic corpus.

## Recommendation

Use **two cohorts**: a small 8–12 case *readiness pilot* emphasizing different ordinary meanings and existing constructions, and a broader 36-target expressive coverage backlog. Keep UCUB-001 minimal-contrast regression separate; do not create new Tally forms from unresolved candidate translations. An Italian-first matrix is a development instrument, not language validation.
