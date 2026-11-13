# UCUB-001: human review of **63 unique Unisermo meanings**

**CURRENT PROTOCOL — 13 November 2026.** The user rejected the earlier human entailment questionnaire. This is a **translation-equivalence audit**, not a quiz about what follows logically from a statement.

## Why 63 rather than 80?

UCUB-001 retains **80 paired model-inference cases** in the frozen `corpus.jsonl`, but those cases contain only **63 distinct full Unisermo passages**. Repeated passages were paired with different hypotheses (for instance `i vidi akwaem.` appears five times). Such repetition is useful for *LLM inference* but counterproductive for *human meaning verification*. The revised human form presents every unique full passage **once only**, never with several competing logical hypotheses.

Source: `unique_translation_review_63.jsonl` (63 lines), with `unique_translation_review_manifest.json` recording the unchanged UCUB-001 source corpus SHA-256 and level counts.

The deduplication key is the exact **complete Unisermo passage** (not a single clause within a 3-clause discourse). The row uses its **first** originating UCUB case to determine the proposed Italian wording; `source_ids` preserves the full one-to-many mapping to 80 benchmark items. One duplicate passage had two slightly different English paraphrases about a roughly 70% probability; both are preserved in `english_variants` and **one** Italian candidate is presented to the reviewer. The candidate Italian meanings have NOT been ratified or independently validated.

## What reviewers see

- **One** Unisermo sentence/passage and **one** **candidate Italian meaning**.
- One multiple-choice question: **Sì, corrisponde / No, non corrisponde / Parzialmente, ambiguo / Non riesco a valutarlo**.
- One **optional** free-text space for a corrected meaning or explanation of the ambiguity.
- A reviewer pseudonym shared across all four forms and an independence declaration.
- An Italian explanation of the task and choices on the first page; each form has page groups of approximately four passages.
- **No** authored logical gold label, **no** logical hypotheses, **no** repeated passage, **no** compulsory free translation on already clear cases.

Reviewers may consult the canonical grammar, but should not see the corpus labels, AI responses or other reviewers' judgments. Being shown the proposed meaning makes this a **candidate-equivalence assessment**, not a blind independent translation; report it accurately as such.

## Published Tally questionnaires

| Level | Distinct passages | Tally form |
| --- | ---: | --- |
| L1 | 14 | https://tally.so/r/DqkEyX |
| L2 | 16 | https://tally.so/r/zEyRoZ |
| L3 | 14 | https://tally.so/r/5XjgDv |
| L4 | 19 | https://tally.so/r/dba41D |
| **Total** | **63** | 4 existing forms updated in place |

Existing form URLs were preserved. As checked before replacement, they had **0 submissions**; the obsolete logical question pages were removed and the same forms republished. Review responses are collected inside Tally, not in handwritten JSON. Case IDs in the question titles support a later mapping from Tally submissions back to the exact source passages.

## Review methodology

1. Engage at least two independent humans who can assess Unisermo morphology/semantics by consulting its ratified grammar. Each reviewer completes the four forms with a consistent pseudonymous code, without consulting other reviewers, authored labels or model outputs.
2. Export/collect Tally submissions and validate that each of the 63 `id` values has exactly one choice per person. Capture the optional proposed corrections. The four forms constitute one reviewer record; do not treat them as four independent reviewers.
3. Classify cases with either `No`, `Parzialmente`, `Non riesco a valutarlo`, or reviewer disagreement as **needing adjudication**. Two `Sì` judgments support an equivalence, but do not alone prove all grammatical ambiguities are resolved. Inspect known source-grounded flags from `preaudit-flags.json` with an adjudicator **after** gathering responses.
4. Track every accepted correction in a **new version** of the review dataset with attribution and rationale. Keep the original frozen UCUB-001 source texts, English controls and gold labels unchanged unless an explicitly versioned benchmark corrigendum is approved.
5. This review only checks passage↔Italian proposed-meaning equivalence. It does **not** independently validate the **80 logical inference gold labels** nor the 80 English controls used in the model benchmark. Any public comprehension claims still require suitable separate validation of those components.

## Compatibility and historical protocol

The older `review.py`/two-stage **80-case entailment labeling** protocol remains available for reproducibility and optional future research. Its initial documentation is archived in `REVIEW_ENTAILMENT_ARCHIVE.md`; it is **no longer the human-facing review process**. In particular, do **not** generate or distribute its JSON reviewer packets as the default user workflow.

The next **model evaluation** can still use the preregistered 16-case balanced development screen (G03, G06, G12, G16) and the original 80-case inference task, after the relevant semantic issues have been adjudicated.
