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
