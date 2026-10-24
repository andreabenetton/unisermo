# Counterbalanced A/B semantic recognition — prospective study (24 October 2026)

**Status at registration:** protocol fixed before paid calls; outcomes unknown. The previous 30-item pilot is already exposed development data and is *not* treated as validation.

## Motivation

The initial source-grounded semantic contrast study (PR #7; [run 40083465724](https://github.com/andreabenetton/unisermo/actions/runs/40083465724)) produced cold 25/30 vs guided 27/30; every one of its five cold errors selected A with B correct. That pattern suggests potential **position bias**, but it could also arise from particular question phrasing, answer order and interaction with the meaning being tested. We must explicitly intervene on the choice's position before inferring a semantic failure.

## Pre-registered design

- **20 newly paired contrasts** (4 each: case, relator, quantity, deixis/possession, transition/focus). Every expression is previously *attested* in a current normative document, but may have appeared individually in earlier experiments. New *pairs*, not an unseen lexicon or an untouched holdout.
- Source: `benchmarks/corpus/semantic-order-dev-001.jsonl`; two expressions and the author-assigned target meaning for each; sources cited per pair. Automatic verification checks that the unordered pairs were not previously in `semantic-contrast-dev-001`.
- **Two conditions:** cold (no linguistic primer); guided (same guide as previous study). Identical answer instructions and question within each pair.
- **Two orderings:** target as A, distractor as B; then target as B, distractor as A.
- Total **20 × 2 conditions × 2 orderings = 80 isolated Qwen3 32B API calls**; a four-arm cyclic order distributes condition and orientation across request positions. Original response order and request hashes are retained.
- The scorer knows targets, but API prompts contain **no target labels** or source citations.
- Model: `qwen/qwen3-32b` through OpenRouter's existing helper (requested temperature 0.7, seed 23, reasoning disabled, no provider fallback; provider not pinned; returned IDs recorded). Seeds are requested, not proof of deterministic provider behavior.
- Maximum 130 generation tokens per call, **80 billable requests maximum**, stop making further requests when cumulative **observed** provider-reported cost reaches **USD 0.03** (a post-response check, *not* an absolute pre-billing ceiling).
- All actual responses are appended to raw JSONL before scoring and preserved on failure. Only a complete 80-call set is scored. Freeze code, corpus and guide at the execution commit; no tuning on this new pack during execution.

## Scoring / interpretation (registered before results)

For each condition and **each unordered expression pair**:

1. **Both correct (semantic-invariant):** chooses the same target expression in both orientations (A first / B second). This is the strongest forced-choice evidence per question.
2. **Both incorrect (distractor-invariant):** chooses the same wrong expression across reversed orientations. This is a stable *meaning error*, **not** evidence of an A-position bias.
3. **Always A / always B:** chooses the *position label* regardless of which expression occupies it, with exactly one of the two choices correct. This is evidence of **positional stickiness** on that item, not a proof of a global systematic bias.
4. **Format / other:** JSON failure or another scoring anomaly, never silently corrected.

Report presentation-level correct count out of 40 per condition, **both-correct pair** count out of 20 (primary), per-family results, always-A vs always-B, both-wrong and format failures; consumption, provider cost and **USD per pair decoded correctly in both orders**. Compare guided/cold outcomes at the pair level; no iid significance test on 80 correlated presentations.

## Human adjudication protocol

The question meanings are **researcher-authored and pending independent review**. Canonical source attestation alone does not certify that the contrast is unambiguous, natural or context-free.

Before publication, an independent reviewer (preferably qualified in linguistics) must examine the full relevant normative passages, the exact pair and English question *without seeing model responses*, and mark each ID:

- `approved`: target has the intended semantic contrast under the normative specification.
- `ambiguous`: two candidates or scope remain plausible; record alternative readings.
- `invalid`: wording or intended interpretation contradicts the norm; include rationale.
- `requires_context`: too underspecified to score.
- `unreviewed`: review pending.

Record reviewer's role, source version/date, item ID, decision, confidence, and comments. Never label AI self-review as independent human review. Report unreviewed results as **provisional**; keep rejected items for historical analysis rather than retrospectively hiding them. All decisions must be made independently of and before using a final unseen holdout. A separate future phase will assess complete propositions and discourse reference, but only after syntax and semantic commitments are defined.

## Threats to validity

Questions reuse familiar lexical forms and English metalanguage, so recognition is not cold natural conversation. Eighty observations comprise only twenty meaning clusters; provider variability is not isolated with one answer per arm. Swapping order detects positional tendencies, but cannot prove why a particular answer was selected. The guide may bias interpretation as well as raise accuracy and costs. **No changes to accepted Unisermo canon, morphology, lexicon, cases or kinship** and no holdout touched.

## Archived evidence plan

After successful execution: verify raw answer count, prompt digests, returned model and use/cost metadata; retain the **original** JSONL and score in `benchmarks/evidence`, append results to this record and the historical diary, and cite GitHub run/commit IDs. Do not rewrite this preregistered section to reflect outcomes.

---

## Executed observations — appended after preregistration on 2026-10-24

**GitHub provenance**

- [Actual Qwen3 experiment](https://github.com/andreabenetton/unisermo/actions/runs/40085726322): successfully completed all **80** isolated requests from the preregistered development questions. Original Actions artifact `semantic-order-40085726322` (ID `12556773816`).
- [Archive and re-scoring verification](https://github.com/andreabenetton/unisermo/actions/runs/40085913875): successfully re-read the saved JSONL and verified 80 unique request IDs/order, prompt digests, model and provider, raw/corpus SHA256, provider cost and the full scored comparison.
- [Original 80 responses](../../benchmarks/evidence/semantic-order-2026-10-24-run40085726322.jsonl) (SHA256 `a761032d2478feca319d46fb263714bfb4a1e68d92c197b9e99a5fd4b2f86717`).
- [Machine-readable score and paired outcomes](../../benchmarks/evidence/semantic-order-2026-10-24-run40085726322.score.json); source corpus SHA256 `c7218177da3b8179078af3d9aec672b29b41bec594fad47b1e4d695afe85f928`.
- Qwen request/response model `qwen/qwen3-32b`, provider **DeepInfra** in all 80 results, all `finish_reason=stop`, no format failures. Temperature 0.7/seed 23, no-thinking flags were *requested*; provider-level deterministic treatment not established.

### Outcomes

| Measure | Cold | Guided |
| --- | ---: | ---: |
| Individual presentations correct | **31/40 (77.5%)** | **38/40 (95.0%)** |
| **Contrast pairs correct in both A/B orientations** (primary) | **12/20 (60%)** | **18/20 (90%)** |
| Same wrong expression under both orientations | 1/20 | 0/20 |
| Same literal A label after swap (position sticking) | 6/20 | 2/20 |
| Same literal B label after swap | 1/20 | 0/20 |
| Invalid response format | 0 | 0 |
| Input tokens | 3,534 | 17,134 |
| Output tokens | 360 | 360 |
| **Total tokens** | **3,894** | **17,494** |
| Provider-reported USD | **0.00038352** | **0.00147152** |
| USD per correct presentation | 0.0000123716 | 0.0000387242 |
| **USD per pair correct in both orientations** | **0.00003196** | **0.0000817511** |

**Total observed USD 0.00185504**, 21,388 tokens, far below the USD 0.03 observed-spend guard. While the guide improved strict two-order correctness by six items, it incurred about **2.56 times higher provider cost per fully stable correct meaning pair**, on this specific test. Gross guided API cost was about 3.84 times cold cost. This is not end-to-end human/LLM communication efficiency, where reference documents might be shared and their overhead amortized.

### By family

| Four semantic pairs each | Cold: both orientations correct | Guided: both orientations correct |
| --- | ---: | ---: |
| Case | 0/4 | 4/4 |
| Analytic relators | 4/4 | 4/4 |
| Quantity | 4/4 | 4/4 |
| Deixis / possession | 0/4 | 4/4 |
| Transition / focus | 4/4 | 2/4 |
| **Overall** | **12/20** | **18/20** |

Six cases shifted from **always-A** in cold to **target-invariant** under guidance; one previous stable distractor preference and one always-B switched to target-invariant as well. Ten remained correct in both conditions. Two previously target-invariant transition/focus questions (OR019, OR020) switched to **always-A** in the guided arm.

**Important separation of errors:** cold results exhibit **six positional A-sticking cases and one B-sticking case**, alongside one genuinely stable distractor choice (OR002). A sticky position label is *not* itself a robust semantic error, whereas following an incorrect expression through A/B inversion is evidence of consistent selection of a different semantic candidate. Neither pattern proves the model's internal cause with one sample per arm.

### Interpretation and prospective decision

- The earlier all-five-failures-A observation should not be stated as an identified global positional bias. The counterbalanced data reveal per-item positional sticking, disproportionately at A (cold 6 vs 1 B), under a small, non-naturalistic development corpus. This supports *further* controls rather than a causal or population-level conclusion.
- The guide's advantage is **concentrated in case/deixis**, while its **two regressions concern focus**. Testing a *selective* guide on genuinely new development constructs, with guide transport amortization, is more informative than optimizing prompts on these exposed 20 items.
- All 20 author-assigned gold keys are **still awaiting independent human adjudication**. The review procedure and 20-row form reside in `research/lexicon/semantic-key-review-worksheet-2026-10-24.md`; it explicitly records **0/20 independently approved**. Automatic source-attestation and AI analysis do **not** count as such review.
- All questions remain development-only. The frozen holdout was not accessed, and no normative language rules, case distinctions, roots, kinship or numerals were changed.
- The next scientific gate is **authoritative full-proposition semantic validation** with explicit case/valency and referential modeling. If multi-clause anaphora, quantifier scope or valency remain underspecified in the current canon, register that as a language-design gap rather than inventing a test answer. Include reviewed concise English equivalences and charge prompt overhead/corrections, not just tokens on successful outputs.

This result is a documented intermediate stage for the eventual scientific paper, **not** an established Unisermo language advantage.
