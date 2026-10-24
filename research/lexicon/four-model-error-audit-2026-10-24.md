# Four-model shared-error review (2026-10-24)

**Status:** source-grounded post-result analysis, NOT independent human review. Human approvals: **0/24**. Retain original gold and scores unchanged.

## Source authority

`language/copula.md` sections 6–7 and `language/noun_case_system.md` sections 3–4 distinguish noncausative `traes DEST-ad SOURCE-de` (destination allative, source ablative) from causative `Y traes X-em RESULT-da` (patient accusative, resulting predicate resultative). Accordingly `solidad` is `solid` plus `-ad`, while `solidda` is `solid` plus `-da`. Canonical source examples define the argument patterns; naturalness of generated finite complete clauses remains unreviewed.

## Exact four-family shared failures

Three case-task failures, CR006.1 `akwa traesfa solidad likwidde.`, CR007.1 `akwa traesoda solidad likwidde.`, CR008.1 `akwa traesefa solidad likwidde.`. All require `(solid,dative_allative),(likwid,ablative)`.

One role-task failure: **CR007.1**, requiring `(solid,destination),(likwid,source)`. These are four clause-task failures, **only three unique sentences**, with identical predicate root and noun complements but different TAM. Do not treat as four independent linguistic constructions.

## Recorded outputs for CR007.1

| Model | Case-task output | Role-task output | Distinction |
| --- | --- | --- | --- |
| Qwen3 32B | `akwa:accusative; solid:resultative` | `solid:destination; likwid:result` | Misattached or missing argument and incorrect labels |
| Gemma 3 27B | `solidad:resultative; likwidde:ablative` | `solidad:destination; likwidde:source` | Lemma retains suffix; case-task additionally mislabels destination |
| Mistral Small 3.2 | `solid:resultative; likwid:ablative` | `solid:result; likwid:source` | Lemmas correct but allative destination mislabeled as result |
| GPT-OSS 20B | `solidad:dative_allative; likwidde:ablative` | `solidad:destination; likwidde:source` | **Correct case and role labels; only stem-normalization incorrect** |

These patterns were read directly from archived machine scores: `benchmarks/evidence/mistral-gptoss-case-role-2026-10-24.score.json` and `benchmarks/evidence/gemma-case-role-2026-10-24-final.score.json`. This audit is **post-hoc**. It does NOT change preregistered exact-match accuracy and does NOT prove the models' natural-language understanding.

**Scientific implication:** it is incorrect to interpret all four strict failures as four identical misunderstandings of Unisermo. Extracting head lemmas and assigning case/semantic roles must be scored separately. In particular GPT-OSS labels are correct on the disputed clause despite failing strict whole-clause extraction.

## Independent review gate

Before publication, have a qualified reviewer annotate the 24 original sentences **without inspecting this post-result analysis**. Use `research/lexicon/case-role-human-review-2026-10-24.md`. Record grammatical naturalness, source licensing of finite subject and TAM combinations, nominal case segmentation, source/destination/result meanings and the faithfulness of the machine representation. Accept **approved / ambiguous / invalid / requires_context**, cite source passages, document any loss of blinding.

Focus on CR006.1, CR007.1, CR008.1 and compare corresponding `uman` transition items and causative counterparts. No canonical change, holdout use or human approval is implied.
