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

---

## Executed results — 24 October 2026 (appended after preregistration)

**Completed trial:** [GitHub Actions 40089793501](https://github.com/andreabenetton/unisermo/actions/runs/40089793501) — **24/24 isolated Qwen3 32B requests** completed; the provider returned **DeepInfra** and `finish_reason=stop` on all calls. [Archive and independent rescore run 40089983998](https://github.com/andreabenetton/unisermo/actions/runs/40089983998) succeeded and verified the 24 original response IDs/order, model/provider, raw/corpus hashes, accumulated cost and recomputed scores.

**Permanent original data:**
- [`benchmarks/evidence/relational-frame-2026-10-24-run40089793501.jsonl`](../../benchmarks/evidence/relational-frame-2026-10-24-run40089793501.jsonl), raw SHA256 `135a414555471d467dcd8c2a546bbd05756790aaa4b4306d1c091d56a16c4076`.
- [`benchmarks/evidence/relational-frame-2026-10-24-run40089793501.score.json`](../../benchmarks/evidence/relational-frame-2026-10-24-run40089793501.score.json), corpus SHA256 `cf4d3f1b5f3c5aff65b518f27bc86e0fec9f6ffe37878f5ee0ad0c9e33fba9ab`.

| Preregistered metric | Cold | Guided |
| --- | ---: | ---: |
| **Exact all-twelve-field propositions** | **0/24 (0%)** | **4/24 (16.67%)** |
| Correct typed semantic fields | 201/288 (69.79%) | 226/288 (78.47%) |
| JSON format errors | 0/12 | 0/12 |
| Input tokens | 2,427 | 5,295 |
| Completion tokens | 2,503 | 2,485 |
| Total tokens | 4,930 | 7,780 |
| Provider-reported USD | 0.00089500 | 0.00111940 |
| USD per exact proposition | undefined (zero exact) | 0.00027985 |

**Grand total: 12,710 tokens, USD 0.00201440**, within the observed $0.02 ceiling (not a hard prepaid limit).

### Result by frame family (eight propositions each)

| Frame | Cold exact | Guided exact |
| --- | ---: | ---: |
| Motion `mov`: explicit object and `-ad` destination | 0/8 | 4/8 |
| `traes`: destination `-ad`, source `-de` | 0/8 | 0/8 |
| Causative `traes`: object `-em`, result `-da` | 0/8 | 0/8 |

### Error anatomy — preserve the distinctions

The 87 cold and 62 guided feature-slot errors are NOT equivalent to as many independently sampled semantic failures. They cluster by the **two-clause** development document. Guided field errors primarily involve `destination` (9), `result_state` (8), `frame` (8), `source_state` (7), `subject_role` (7), `tense` (7), and `aspect` (7). Cold had notably more errors in `tense` (15), `destination` (14), `frame` (11) and `subject_role` (10). All errors count against the original strict schema, and **none** of the 24 response JSON objects had a wrapper/cardinality failure.

The pair `akwa traesa solidad likwidde` is illuminating. The model often recognized `likwid` as the origin and `solid` as the end state, but encoded `solid` as `result_state` instead of `destination`. The current machine schema intentionally represents the `-ad` destination as distinct from causative `-da` result; these two categories are grammatically distinct **in the source**, yet the language-model output may reflect a broader conceptual paraphrase. We should not retroactively equate the two fields to manufacture a higher strict score; nor should we claim a human-confirmed communication failure in every such event.

A second recurrent problem is falsely identifying the intransitive `traes` **theme** as a **causer** and inventing an explicit patient. In other instances the model inferred an unsupported liquid initial state for causative transformation. These are distinct from the nominal suffixes alone, and demonstrate why role and valency constraints matter.

**Scientific limitation:** the prototype's `theme` annotation for an explicit subject of intransitive two-state `traes`, and the grammatical naturalness of the new generated complete sentences, have **not** been approved by any independent human reviewer. See [24-item review sheet](relational-frames-human-review-2026-10-24.md): **0/24 approved**. The meaning representation is a *source-grounded experimental ontology*, not a universally validated formal semantics.

**Decision:** retain this negative result unchanged; do not modify accepted `-ad`, `-de`, `-da`, `-in`, lexical or syntactic rules on these data. The guided prompt helps strict field recovery but does not make full relational decoding reliable. A follow-up should first independently adjudicate theme/causer interpretations, then factor grammatical-role accuracy from output-ontology compliance and test genuinely new source-reviewed complete sentences. Connected discourse, controlled English and total communication-cost comparisons remain pending.
