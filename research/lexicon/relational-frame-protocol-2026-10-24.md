# Source-licensed relational frames: implementation and development protocol

Date: 2026-10-24. **Status: pre-registered before any paid model calls in this stage.** Earlier SVO proposition findings are archived in PR #10, which this work builds upon. No grammar or lexicon changes are authorized.

## Scope / normative evidence

The pre-existing [motion valency](../../language/verb_specification.md) licenses `Y mov X-em DEST-ad`, i.e. an agent moves a patient toward a destination. The existing [copular/transformative specification](../../language/copula.md) and [noun cases](../../language/noun_case_system.md) license `traes DEST-ad SOURCE-de` (transition between an explicit source and destination state) and `Y traes X-em RESULT-da` (causer transforms an object into the resulting state).

`formalization/semantics/relational_frames.py` implements **only these three valency templates**, requiring one finite verb, explicit subject, two exactly case-marked complements in canonical order and no extra material. The `mov` phase family is allowed by source-level inheritance; this initial LLM corpus only instantiates `mov` and `traes`. The parser labels the subject of the two-state transition `theme`, which is a **machine research interpretation subject to independent semantic/valency review**; the source establishes destination/source roles, but does not independently establish all agent/theme semantics for new generated complete sentences.

The synthetic case **locative `-in` is canonically valid at the word level**, but no verb-specific locative construction is admitted in this narrow three-frame parser. This is a **software-scope restriction, not a language prohibition**. In particular, the parser does not infer `-in` can replace `-ad` in the moving-to frame. Free relators (`kun`, `pro`, etc.), beneficiary valency, full copular predication, elliptical subject, interclausal anaphora and unusual word order remain unimplemented here. Core `parse_sentence` remains unchanged to preserve backwards compatibility.

## Corpus and machine gold

`benchmarks/corpus/relational-frames-dev-001.jsonl` contains 12 two-sentence development documents, four per frame family, 24 distinct full finite clauses. Their vocabulary includes canonically confirmed and **example-only** nouns/predicates; no example-only lexeme gains confirmed status. The role-scoring adapter `benchmarks/relational_frame_meaning.py` rejects any statement without exactly one uniquely valid construction, and admits only unmodified bare nominals or explicit pronoun subjects. This purposely avoids partial scoring that discards plural/deictic meaning while claiming a full proposition match. Nominal `-ad`, `-de`, `-da` are scored as distinct roles, not as synonyms.

Every event must contain 12 typed fields:
`frame, subject, subject_role, predicate, patient, destination, source_state, result_state, tense, aspect, person, number`.
Absent roles are **JSON null** rather than fabricated meanings. The subject value is an explicit form (`i`, `u`, `in`, `un`, `uman`, `akwa`); it is not a bound referent ID. Model output must be `{"events":[...two exact objects...]}`, rejecting arrays missing the wrapper, extra keys, incorrect types or wrong ordering.

**All 24 machine keys are unreviewed.** An independent linguist should evaluate whether the generated complete sentences, source-defined frames and theme/causer labels express the intended propositions. No AI-based self-adjudication will be presented as independent approval.

## Hypothesis and fixed paired comparison

Qwen3 32B through OpenRouter; 12 isolated requests without a language primer (`cold`) and 12 with a fixed concise grammar/lexicon/valency guide (`guided`), counterbalanced condition request order by document.

Primary outcome: exact full twelve-field meaning for each of 24 propositions per condition. Secondary: per-field error profile; failure to produce required JSON shape (scored as zero for each clause in its document); individual document differences; tokens consumed; total provider cost and cost per complete correct meaning. The independent unit for descriptive comparison is the two-sentence document, **not** 48 iid clauses. No significance testing or population-level claim follows from 12 templated document clusters.

Existing helper requests temperature 0.7, seed 23, non-thinking, no provider fallback; returned model/provider and usage captured. Provider seed determinism is not guaranteed. Max 650 generation tokens per request, max 24 calls, **USD 0.02 cumulative observed-cost stop** (checked after each billable response; not a prepaid guarantee). Each response is written immediately, including on a later failure. Partial files are archived but cannot produce a successful complete experiment score.

Source code, corpus and protocol are committed **before** paid execution. Raw original responses and score will be verified and archived under versioned `benchmarks/evidence` paths after a completed run.

## Decision gate

Do not modify the language canon based on this study. Do not claim proof of general language comprehension or greater efficiency than English: there is **no independently verified English-equivalent dataset** or connected discourse baseline, and `-in`/beneficiary/adjunct semantics are deliberately out of this specific valency inventory.

Retain success, failure and scoring artifacts. Next prerequisites: independent human meaning/valency review, a reviewed English-equivalent set, distinct format-vs-semantic accuracy reporting, and a ratified referential model before multi-sentence anaphora claims.
