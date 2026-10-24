# 10 August 2026 — From `mov` to phase, state transition, causation and motion direction

**Retrospective audit date: 24 October 2026.** This case documents a sequence of **six independently dated Git decisions** and individually indexed messages from the original ChatGPT discussion. It is a historical investigation of the project later named Unisermo (not its then-current name). An indexed user/assistant message is a **message-level retrieval**, not a full exported verbatim transcript. Dates in all tables below are **UTC on 10 August 2026**.

## Why this episode matters

A root `mov` ("move") appears in the recovered **24 May 2026** early verbal examples. On 10 August the design evolved from one high-frequency root into an explicit **compositional semantic architecture** that distinguishes:

1. **State** and its phase: be / remain / enter / cease / resume.
2. **Motion and motion phase:** move / begin moving / continue moving / stop / resume moving.
3. **State change without source specification** versus **source-to-destination transition**.
4. **Transformation of an object** into a resulting state with a separately assigned predicative result.
5. **Undergoer motion** versus **causing a change in position** (same `mov` family, different argument frames).
6. **Application of force** (push/pull) versus successful displacement, and **direction** (up/down) versus onset/cessation.

The distinction is not a proof of an optimal lexicon. It is a historically documented design response to the objective of compact, productive communication **without merging incompatible meanings**.

## Contemporaneous user and assistant message anchors

The dated entries below come from retrieved, speaker-attributed **conversation-index evidence**. They establish **who expressed or accepted which proposition**; the index result is **not a complete transcript** and should not be presented as verbatim quotation.

| UTC | Speaker | Recovered idea / decision | Independent corroboration |
| --- | --- | --- | --- |
| **13:46:04** | User | The Italian verb *guarire* illustrates ambiguity between an **intransitive recovery** and a **transitive healer-causes-recovery** reading; attention to who undergoes the change versus who causes it. | Original-message index; related conceptual antecedent only, not proof it *caused* all subsequent constructions |
| **13:46:04** | Assistant | Proposes not conflating recovering/becoming well with caring for or curing somebody, and separating valency/causation. | Assistant response index; not a confirmed design commitment |
| **14:06:37–14:07:13** | User | Rejects hyphens for fused phase families; accepts `ades`, `dees` as contiguous forms. | [Phase-family commit, 14:11](https://github.com/andreabenetton/unisermo/commit/51be6a882a97d4a4cc4f75458ddb1b4ec373c1c9) |
| **14:21:22** | User | Explicitly adopts `traes DEST-ad SOURCE-de`, with `-ad` destination, `-de` source; `ades X` reserved for simpler BECOME with no source asserted. | [Transition commit, 14:22](https://github.com/andreabenetton/unisermo/commit/16250c8b225daf2425112e21690ae0b2ccab2362) |
| **14:35:00** | User | Explicitly accepts `Y traes X-em RESULT-da`: cause Y transforms object X and `-da` identifies its resulting state/class/property. | [Resultative case commit, 14:36](https://github.com/andreabenetton/unisermo/commit/53df8ba04e5d04ef9794c62c357a712567f86123) |
| **14:45:16** | User | Accepts intransitive `X mov` and transitive `Y mov X-em` for displacement. | [Valency commit, 14:47](https://github.com/andreabenetton/unisermo/commit/9ce8c0c4facc7df742d88ad63ee50562038e4c80) |
| **14:48:02** | Assistant | Explains `pel`/ `trak` as separate push/pull roots, not interchangeable with successful displacement expressed through `mov`. | Assistant index; see subsequent user acceptance |
| **14:50:00** | User | Canonizes `pel` PUSH and `trak` PULL; demands a distinction between applied force and actual motion. | [Force/manner commit, 14:57](https://github.com/andreabenetton/unisermo/commit/141667e94c198e404958ef1010df057bda553d0e) |

No independently located **original user message** has yet been attached to the **15:41** vertical-motion decision; the Git commit is the primary source for that later expansion. The full original conversation needs archiving before claiming exact psychological motivation or precise unrecorded intermediate candidates.

## Canonical Git sequence: six separate stages, not one event

| UTC | Git SHA | Committed decision | Important non-equivalence |
| --- | --- | --- | --- |
| **14:11:24** | [`51be6a8`](https://github.com/andreabenetton/unisermo/commit/51be6a882a97d4a4cc4f75458ddb1b4ec373c1c9) | Fused `in-`, `ad-`, `de-`, `re-` on `es` and `mov`; `ines, ades, dees, rees`; `inmov, admov, demov, remov`. | Lexical/event phase `inmov` is **not** the finite progressive aspect `e`. `ades` avoids collision with possessive `aes`. |
| **14:22:42** | [`16250c8`](https://github.com/andreabenetton/unisermo/commit/16250c8b225daf2425112e21690ae0b2ccab2362) | Two-pole intransitive transition `traes DEST-ad SOURCE-de`. | Source and destination remain distinct; does **not** require a new case and does **not** mean causation by an external agent. |
| **14:36:39** | [`53df8ba`](https://github.com/andreabenetton/unisermo/commit/53df8ba04e5d04ef9794c62c357a712567f86123) | Adds the **seventh synthetic case**, predicative/transformative `-da`; `Y traes X-em RESULT-da`. | Resulting property `-da` is **not** ordinary allative destination `-ad`, source `-de`, or a general copula marker. |
| **14:47:30** | [`9ce8c0c`](https://github.com/andreabenetton/unisermo/commit/9ce8c0c4facc7df742d88ad63ee50562038e4c80) | `X mov` vs `Y mov X-em`, optional direction `DEST-ad`; same valency alternation for phase family. | Causes actual motion/displacement; transitive `inmov` means keep X moving, not lexical PUSH/PULL. |
| **14:57:40** | [`141667e`](https://github.com/andreabenetton/unisermo/commit/141667e94c198e404958ef1010df057bda553d0e) | Independent `pel` PUSH, `trak` PULL lexical force/manner roots. | One can push/pull something which **does not move**. |
| **15:41:11** | [`8bb979b`](https://github.com/andreabenetton/unisermo/commit/8bb979bf5e55f4a1ba713ecfe30e5b5d6c0ec1a6) | `alt/bas` axis; analytic `mov altad / mov basad`, fused `altmov / basmov`. | UP/DOWN **direction** is not BEGIN/STOP **phase** (`admov/demov`). |

### A minimal semantic contrast set, sourced from canonical language examples

These example types are included in versioned specification commits above, *not* modern translations invented for this analysis:

| Construction | Distinct information encoded |
| --- | --- |
| `es san` / `ines san` / `ades san` / `dees san` / `rees san` | Is healthy / remains healthy / becomes healthy / ceases to be healthy / becomes healthy again |
| `ades solid` | Becomes solid; source not specified |
| `traes solidad likwidde` | Passes from liquid to solid; names both states |
| `Y traes akwaem solidda` | Y transforms water into a resulting solid state; identifies causer and affected entity |
| `X mov` / `Y mov X-em` | X moves / Y causes X to move (valency alternation) |
| `Y pel X-em` / `Y trak X-em` | Y pushes / pulls X, without entailing X changes location |
| `mov altad` / `altmov` | Analytic directional phrase versus lexicalized transparent upward-motion compound |

Do **not** treat `traes DEST-ad SOURCE-de` and `Y traes X-em RESULT-da` as synonymous transformations: they are separate **argument structures** with different semantic commitments.

## Rejected or deliberately separated interpretations

1. **Hyphenated lexical phase forms** were rejected by the user (14:06–14:07); fused forms remain distinct from any editorial morphological analysis written with a hyphen.
2. **`aes` as BECOME** would collide with canonical possessed third-person `aes`; `ades` avoids that specific form collision (14:11 committed rationale).
3. **`dees X` as 'become opposite of X'** is not entailed by the design: it only marks ceasing to be X.
4. **Generic `ades` for a two-state comparison** was insufficient when **both source and target** needed assertion. `traes` with the existing `-de/-ad` fills that semantic gap.
5. **Allative `-ad` for a resulting object property** was deliberately distinguished from `-da` in the causative frame, explaining the **six → seven synthetic cases** transition later that afternoon.
6. **Treating `pel` and `trak` as guaranteed movement** was rejected as a lexical entailment; they express force/manner.
7. **Confusing phase with direction:** `admov` does not mean 'go upward' and `demov` does not mean 'go downward'. `altmov/basmov` separately express vertical direction.
8. **Reusing May's earlier proposed `-da` 'from' meaning** is not supported. On 24 May `-de` was fixed as SOURCE; on 10 August `-da` was introduced as resulting predicative. They are unrelated **functional proposals that happen to share surface spelling**.

## What is measured and what remains hypothetical?

**Directly documented:**
- Exact Git history and the canonical semantic distinctions; dated user-message confirmation for five of the phases/stages.
- A **productive design mechanism**: reuse `mov/es`, four phase prefixes, existing source/destination cases, and separate resultative.
- Interaction of orthographic collision avoidance and semantic precision (`ades` vs `aes`, `-ad` vs `-da`).

**Historical interpretation / hypothesis:** Such a compositional system may reduce the number of arbitrary roots a learner must memorize without sacrificing core semantic distinctions. **No contemporaneous controlled lexical-learning, spoken time, or human interpretation data** supports that as an achieved result.

**Next archival questions:**
- Export full 10 August original conversation around 13:46–15:41, especially discarded proposed verbal forms and author choices not captured in the message index.
- Trace May 24 `mov` through its early roots and verify whether the later phase-family notation was ever anticipated explicitly before August.
- Assess the independent human cost of mastering productive phase operators; distinguish morphological compositionality from ambiguity resolution and pronunciation.
- Preserve **first Git commit** and **user acceptance** separately; their timestamps are different evidence classes.

## Sources

- [May original verb/case record](may-august-morphology-decision-chain.md)
- [Nominal case 13 → 6 → 7 record](cases-and-complements-design-history.md)
- [TAM experiment and its non-equivalence to phase operators](august-tam-phonotactics-decision-history.md)
- [Original 2025 information-rate objective and testimony](founding-objective-and-efficiency-measures.md)
- Six immutable primary commits linked in the chronological table.
