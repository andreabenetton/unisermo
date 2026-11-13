<!-- Historical protocol: superseded by the user on 2026-11-13. -->

> **ARCHIVE — not the current human-facing review.** This earlier 80-case entailment/contradiction procedure was rejected as inappropriate for validating Unisermo meanings. Its original text is retained only for provenance; do not distribute its JSON packets to reviewers.

# UCUB-001 — independent semantic review and four-level next test

**Corpus status: 80/80 parser-valid; 0/80 independently human-reviewed; no gold label or original corpus record has been changed by this protocol.**

## Objectives and restrictions

The corpus author and the parser are **not independent semantic reviewers**. Previously tested models (Qwen and Gemma) cannot independently validate the same gold labels against which they are being evaluated: such model-as-judge use would risk circularity. Model feedback may only triage cases; it is **not** counted as independent human verification. An external reviewer who has seen the author's gold or the model predictions must disclose that exposure; their contribution is not blind.

The reference grammar is found in `language/` and Accepted records in `docs/ldr/`. Reviewers may consult the grammar, but **not** the authored `build.py`, `corpus.jsonl`, `preaudit-flags.json`, prior model predictions or gold scores before finishing the blind first phase. Reviewers must use their own reading of Unisermo, not infer that accepted parser syntax guarantees a particular meaning.

The canonical corpus manifest is `benchmarks/ucub001/manifest.json` and its SHA-256 fingerprints exactly which revision the forms review. Existing gold remains "author draft" until two independent humans and an adjudicator complete the gate; the repository cannot mechanically verify real-world reviewer independence.

## Stage 1 — blind semantics

Generate an **80-case blind packet** which includes only case ID, level, Unisermo source and English hypothesis (no original English translation, gold, group, or holdout designation):

- Command: `python -m benchmarks.ucub001.review packet --stage semantic --output /tmp/ucub-semantic.jsonl`.
- Give it to two **independent human reviewers** with access to the canonical grammar, without the source answer keys.
- They must translate each Unisermo sentence independently; decide whether it entails, contradicts or fails to determine the hypothesis; record a short rationale and any uncertainty.
- Neither reviewer should consult the other reviewer before their own first-pass responses are locked.

## Stage 2 — translation equivalence

Once Stage 1 is locked, supply the second packet, which reveals the **draft English** but still hides gold, group and split:

- Command: `python -m benchmarks.ucub001.review packet --stage equivalence --output /tmp/ucub-equivalence.jsonl`.
- Each reviewer marks the draft English **equivalent**, **not_equivalent**, or **uncertain** compared to the Unisermo. They retain their independently authored translation.
- Source references and the known issues in `preaudit-flags.json` are for the **curator/adjudicator after** blind review; avoid anchoring reviewers before their judgment.

## Completed reviewer submissions

Create a BLANK 80-case review form for each reviewer:

- `python -m benchmarks.ucub001.review init --reviewer-id external-reviewer-1 --output /tmp/reviewer-1.json`
- `python -m benchmarks.ucub001.review init --reviewer-id external-reviewer-2 --output /tmp/reviewer-2.json`

The initialized form intentionally has **no labels, translations or rationales prefilled** and its independent-human declaration is **false by default**. Each reviewer must complete all 80 records, assign `label` (one of `entailed`, `contradicted`, `undetermined`, `uncertain`), `own_translation`, `english_equivalence`, `confidence` (1–5), `rationale` and any `ambiguity`. Fill `reviewed_at_utc` and independently attest `independent_of_corpus_author=true`. This is not proof of actual independence; the curator must verify it outside the software.

After submissions exist:

- `python -m benchmarks.ucub001.review aggregate --review-a /tmp/reviewer-1.json --review-b /tmp/reviewer-2.json --output /tmp/ucub-review-aggregate.json`

The tool validates full coverage, exact corpus digest, mutually distinct reviewer IDs and response schema. It then reports three states, **agreed_draft_gold**, **agreed_but_draft_gold_disputed**, or **requires_adjudication**. Even 80/80 agreements produce **awaiting_formal_signoff**, *not* automatic semantic certification; an adjudicator must confirm independent reviewer identities, missing contextual assumptions and issues in the preliminary curator risk registry. Archive the source files, review timestamps and original digest outside provider prompts.

**Never replace** the original `ucub-001@1` gold or English silently. Any adjudicated language/translation/label corrections belong in a versioned corrected dataset with a new digest, a review changelog, and explicit provenance. The **prior first-smoke evidence** must keep pointing at the original corpus hash.

## Preliminary curator audit: not human-independent validation

See `preaudit-flags.json` for source-grounded hypotheses, not verdicts. The first pass identifies issues with:
- Specificity of personal pronouns in an English control.
- Context-dependent modal domains (especially `pos` vs `deb`).
- Knowledge vs belief, whose entailment relation is not fully settled as a lexical guarantee.
- Bare `lik` vs English 'probable' thresholds.
- Approximate quantities and interval endpoint inclusivity.
- Unresolved reference to the same `uman` across discourse clauses.
- 200% rhetorical statements, where English 'claimed likelihood' can change a proposition into a speech-act report.

These flags **do not change any accepted grammar rule**. Any newly discovered lexical principle requires a separate ratification; benchmark weaknesses should normally be addressed at the test level, not by silently adjusting the language to improve model scores.

## Stage 3 — pre-registered development screening across all four levels

The old smoke asked four variants of only G01 (L1). Instead of `--limit 16`, which would take four early L1 groups, the runner now supports **`--sample balanced16`**:

- `python -m benchmarks.ucub001.runner prepare --sample balanced16 --condition cold --split development --allow-unreviewed --output /tmp/ucub-balanced-cold.jsonl`
- The same command with `lexicon`, `grammar` and `english` makes four identical-ID, 16-case development arms.
- Selection deterministically picks **one full four-contrast family per level** by a fixed hash of group ID and constant seed. It **excludes G01** (already used in the smoke), never reads gold labels, and **never accesses the holdout**. Code revision and manifest SHA identify the exact selection.
- Scoring with `--sample balanced16` requires the complete same-case set, unless partial scoring is explicitly authorized.
- This is a *preregistered experiment design*, not a hosted run. **Do not run the paid model matrix** until the relevant reviewed cases and English equivalents pass the human gate. Any early unreviewed use must remain explicitly marked exploratory and cannot justify general claims.

## Advancement criteria

1. Two independent human submissions for all 80 cases; disagreements resolved by a curator/adjudicator, including the flagged cases.
2. Every accepted gold label supported by a formal explanation and agreed English equivalent; incompatible statements are not silently assigned false labels.
3. A **versioned** reviewed corpus digest, pair-group-safe frozen holdout and an unmodified definition of evaluation conditions.
4. Run a balanced 16-case development screening on Qwen/Gemma and all four conditions; store every answer, actual provider/returned model, tokens, costs, and **separately** raw-JSON formatting compliance vs recovered semantic correctness.
5. Only afterward consider full 64 development cases and unlock the 16 held-out cases. Keep provider failures separate from model invalid formats.

No independent review responses have been received or fabricated in this stage.
