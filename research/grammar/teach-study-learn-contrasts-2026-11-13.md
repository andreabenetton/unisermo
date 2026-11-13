# Teaching, studying, learning: semantic contrast audit (2026-11-13)

**Status:** experimental research proposal; no ratification of a new learning root, no parser change.

## Existing approved semantic commitments

- `dok` = teach: teacher-side educational action. Does not entail successful learning by the addressee.
- `stud` = study: systematic/intentional engagement with material; approved by owner, currently incorporated in the **unmerged** lexical reconciliation PR #66, not yet in the default branch.
- `sap` = know / possess knowledge; also procedural know-how in its existing servile frame.
- `kap` = understand / cognitively grasp meaning.
- `pens` = think.
- Productive agent `-or`: `dokor` teacher; `studor` studier, with no automatic enrollment or credentials.

## Question: is 'learn' lexically primitive?

Two substantial hypotheses:

### H1: `adsap` = enter the state of knowing

Ratified `ad-` phase semantics mean begin/enter a base event or state; `sap` is a state of knowing. Thus `adsap` can be compositionally interpreted as the **onset of knowledge**, and can express a resultative 'come to know / learn a fact' when that is the intended event. This does NOT automatically name the process of acquiring knowledge or improving a capability over time. A sudden revelation can yield new knowledge without study; and studying can happen without eventual knowing.

We should test whether existing `adsap` or related `ades` state constructions cover *all* learning contexts; do not treat the fact that the morphology yields a valid form as proof it always matches 'learn'.

### H2: candidate `lern` = gain knowledge or competence

Propose `lern` for the **process/event of acquiring knowledge or competence**, irrespective of intentional study or outside teaching. Distinguish:
- learning may occur without explicit teaching (`dok`);
- learning may occur without deliberate studying (`stud`);
- teaching or studying may occur without learning;
- when a **completed successful** learning event is asserted, the learner has gained some new knowledge/competence; plain process morphology or unsuccessful attempts should not entail this result.
- understanding (`kap`) is not always equivalent to lasting knowledge (`sap`), and vice versa.

`lern` is a provisional form inspired by learn/lernen, with letters in canonical alphabet; do not claim phonological, collision, or recognition approval. It requires a lexical valency frame (learner = subject; acquired content/skill = object or another approved complement) before executable examples are canon.

### Decision criterion

Prefer **H1** if `adsap` and ordinary aspect/phase morphology express both the learning process and achievement without ambiguities; prefer **H2** if a distinct process of knowledge/skill acquisition remains expressively useful without bloating grammar. Avoid inventing special semantics for existing `ad-` merely to eliminate `lern`.

## Semantic contrasts for review

1. A teaches B mathematics for an hour; B learns nothing. `dok` true, success of learning false.
2. B studies a book; B learns nothing. `stud` true, successful learning false.
3. B learns a word by overhearing a conversation; B did not intentionally study. Learning true, `stud` false.
4. B knows a fact but cannot explain its reasoning. `sap` may hold, `kap` of explanation not entailed.
5. B understands an argument but forgets it tomorrow. `kap` at time t does not entail future `sap`.
6. A reads to B, and B already knew the information. `dok` or transmission can occur, but **new** acquisition not entailed.
7. A shows B a movement; B learns how to perform it. Procedure learning versus existing `sap + infinitive` know-how state.
8. B gradually acquires skill through repeated practice, then succeeds. Learning process has duration; `adsap` may mark the transition into know-how rather than every learning stage.
9. B suddenly discovers an answer without prior study. Change of knowledge state is true, systematic study false.
10. B claims to have learned something but it is false. Distinguish the speaker's assertion from factive acquisition.
11. B learned a skill but currently cannot execute it due to injury. Procedural knowledge `sap` may persist while physical capacity `pot` fails.
12. B has permission to teach but has never taught. `aut` does not entail `dok`.

## Role / valency proposals pending owner review

Do **not** assume that `dok X-em Y-ad` is canonical without an approved frame. Define teacher, learner and content roles separately, and specify which arguments may be omitted.

Teaching can be a directed action toward learner; its success is distinct from knowledge acquisition. Studying can select a topic or material; it does not require an instructor. Learning requires a distinct semantic role for acquired content/competence and should distinguish process and accomplished result. Try paired utterances with existing `sap` and `kap` before adding a new lexical primitive.

## Repository integration

This research document intentionally does not edit confirmed lexicon or grammatical sources. `stud` is proposed/ratified upstream on PR #66 and should not be reintroduced in another branch. No executable benchmark gold should be generated from these schematic contexts until relevant valencies are licensed.
