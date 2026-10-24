# Full-proposition meaning recovery — development protocol (2026-10-24)

**Status: preregistered before paid model calls.** Canonical specification is unchanged. This stage builds on the A/B trials in PR #7 and #8 but asks the LLM to **reconstruct complete SVO proposition meanings**, rather than choose an option A or B.

## Source-grounded scope

Current formalization implements only `[ka] [subject NP] [no] finite verb [accusative NP]`. The live specifications support SVO clauses, explicit pronoun subjects, pro-drop, accusative objects, morphological time/aspect, negation, questions, demonstratives, plural particles, numerals/quantifiers, and the lexical meanings of `vid` (see), `pel` (push), `trak` (pull), `mov` (move). The verb `mov` licenses transitive use, while `pel` and `trak` describe forces but do **not** imply displacement. We do not equate those predicates.

**The experiment deliberately excludes** relational adjuncts, source/destination case arguments beyond the object, `traes` causative or source/destination frames, free relators, full lexical valency, zero copulas, unbound focus enclitics, wh-questions, elliptical argument binding, coreference and full discourse scope. Their legitimacy in Unisermo is not denied; the present runtime does not validate them. No new syntax or anaphora rule is introduced.

## Frozen development pack

`benchmarks/corpus/proposition-dev-001.jsonl` freezes **12 documents** of **2 complete independent SVO propositions**, 24 unique surface clauses; each document notes its source grammar documents, research stratum and no-coreference declaration. Some constituent words and even complete example sentences may have appeared previously in language specifications or pilot corpora: **these are not genuinely unseen linguistic items and never count as holdout**.

The machine gold is produced by existing `formalization.core.Unisermo.parse_sentence`, with a deliberately constrained semantic projection `benchmarks.proposition_meaning.meaning`. These exactly ten fields must be returned per clause:

`action, agent, agent_number, patient, patient_quantity, patient_deixis, tense, aspect, polarity, speech_act`.

The normalized action names (`see`, `push`, `pull`, `move`) and person/quantity/deictic labels are **research annotations**. In particular:

- A bare object noun is `patient_quantity=unspecified`, **not** assumed singular or definite.
- `omni` is normalized `all_members` but no distributive/collective scope is invented.
- `nul` is `zero` as a nominal quantity, separate from `no` as sentential negation.
- Speakers/listeners can be interpreted from first and second person; third-person pronoun referent identity is excluded.
- Each sentence is an **independent proposition**. Juxtaposition does not imply a discourse coreference relation.
- `dom` and `vid` are marked **example-only/attested** in the generated source index; inclusion does not ratify their lexical status.
- The existing parser's mechanical acceptance is not independent semantic validation, naturalness adjudication or proof of full lexical valency.

Any unsupported sentence or unexpected feature combination must fail closed in corpus validation.

## Comparison protocol

Each two-clause document is sent once under each isolated condition (24 calls total; two complete propositions per response):

- `cold`: shared strict ten-field output contract, no grammar or lexicon reference.
- `guided`: **same** strict output contract plus reusable short grammar and lexical guide; overhead charged for every request.

Both require exactly `{"events":[{...},{...}]}` (the events must be in sentence order). Missing or wrong typed fields and extra keys count as incorrect; malformed JSON or wrong event cardinality yields zero exact events for that document. Do not salvage natural-language narrative answers.

**Primary descriptive metric:** fully correct ten-field propositions out of 24 per condition; **secondary:** per-field errors, paired two-sentence document score, response structure failures, observed provider USD and tokens, USD per exactly correct proposition. These 12 documents, not 48 separate sentences, form the natural cluster for comparison. No significance claim or independent test-set performance claim is justified.

OpenRouter helper requests `qwen/qwen3-32b`, temperature 0.7, seed 23, reasoning disabled and `/no_think`, max 520 completion tokens per response, no provider fallback, provider not pinned. Record returned model/provider/usage IDs and hashes; provider may ignore seed. **Maximum 24 requests**, cumulative *observed* provider-reported USD stop at **$0.02**; the check happens after an individual billed call and is not a prepaid hard ceiling. Persist each response before processing; partial outcomes are not scored as complete.

## Scientific limitations and next gate

Gold fields reflect normative forms and a restricted executable parser **without independent human adjudication**. English equivalences are annotations, not independently reviewed translations. The comparison **does not test English-vs-Unisermo efficiency** or conversation-level meaning, because there is no validated controlled English baseline and no anaphoric links. If decoding appears successful, next:
1. request independent review of all 24 sentence meanings, valency, naturalness, and the ten-field representation;
2. construct additional controlled propositions in genuinely new development documents, ideally with source/destination and beneficiary roles after dedicated valency/parser validation;
3. only then design genuinely connected multi-sentence texts with explicit reference inventory and licensed anaphora, plus a separately reviewed English comparator;
4. freeze an independent holdout before final selection and avoid further tuning on it.

No results should authorize a canonical change or efficiency advantage claim by themselves. Archive the original raw responses and scores after a successful run and append—not overwrite—this preregistration.

---

## Measured outcome — executed and archived 2026-10-24

**Execution:** [GitHub Actions 40086484557](https://github.com/andreabenetton/unisermo/actions/runs/40086484557) completed all 24 Qwen requests; [archive/rescore verification 40086662928](https://github.com/andreabenetton/unisermo/actions/runs/40086662928) succeeded. Original artifact `proposition-meaning-40086484557` (ID `12557605311`) is retained verbatim in the repository:

- [Raw responses](../../benchmarks/evidence/proposition-meaning-2026-10-24-run40086484557.jsonl), SHA256 `ce0880dd234727b40d34b94e118803234ec266bb3ecbd7200aeb5bc1d3040037`.
- [Original exact score](../../benchmarks/evidence/proposition-meaning-2026-10-24-run40086484557.score.json); source corpus SHA256 `d0876b7ec4cee2d06465338b7ba0b6fbd7eff627502cf9f7fa28e286ebd8b892`.
- All returned `qwen/qwen3-32b` via `DeepInfra`, with all 24 `finish_reason=stop`. Requests were bounded and no holdout or canonical language file was changed.

| Preregistered metric | Cold | Guided |
| --- | ---: | ---: |
| **Exact full ten-field propositions** | **0/24 (0%)** | **15/24 (62.5%)** |
| Documents matching required JSON envelope | 12/12 | 11/12 |
| Strictly scored correctly typed field slots | 188/240 | 206/240 |
| Prompt tokens | 2,301 | 5,037 |
| Completion tokens | 2,202 | 2,196 |
| Total tokens | 4,503 | 7,233 |
| Provider-reported USD | 0.00080064 | 0.00101784 |
| USD per fully correct proposition | Undefined (0 successes) | 0.000067856 |

Entire run: **11,736 tokens** and **USD 0.00181848**, below USD 0.02 observed-cost guard.

### Per-feature strict-format error counts

| Feature | Cold errors / 24 | Guided errors / 24 |
| --- | ---: | ---: |
| Action | 6 | 2 |
| Agent identity / speech participant | 10 | 7 |
| Agent grammatical number | 6 | 4 |
| Patient lexical identity | 7 | 2 |
| Patient quantity | 4 | 4 |
| Patient deixis | 4 | 2 |
| Tense | 13 | 5 |
| Aspect | 2 | 4 |
| Polarity | 0 | 2 |
| Speech act | 0 | 2 |

**Interpretation nuance:** Cold 0/24 is a conjunction over ten fields; it does NOT mean zero extracted correct features. Under the registered scorer, cold obtains 188/240 field slots correct; tense and agent identification are major weaknesses. The two-clause-document grouping remains relevant; the 24 events are not independent natural-language samples.

**Format sensitivity:** Guided document `P001` returns an unwrapped pure JSON array. Manual inspection of the original response confirms that **both ten-field event objects match the machine reference perfectly**, but the preregistered decoder requires `{"events":[...]}`. It therefore assigns 0/2 for this document and 20 field failures. **A non-preregistered exploratory alternative** accepting both raw arrays and wrapped objects would yield **17/24 (70.83%) guided exact propositions**, not the official 15/24. Do not silently change the protocol or retroactively re-score the primary metric. Conversely, accept neither extraneous prose nor incorrect field values as exact semantic reconstruction.

Guided failures cluster in particular documents: `P003` (explicit plural participant identity/number), `P010` (combined tense/aspect and subject parsing), with partial losses in `P004`, `P009`, `P012`. In `P010`, model output incorrectly reported `speaker`/singular for the first-person plural subject and `third` as an agent label for the second-person plural subject, among other errors. The guide is not a guarantee of full semantic decoding.

### Scientific conclusion / next gated stage

The short reference guide substantially increases exact decoding on this *small parser-compatible development subset*, at 1.27× gross provider cost (7,233 vs 4,503 total tokens, ~1.61×). But there is **no defined cold USD-per-correct estimate** when cold has zero exact outcomes; do not present infinite/finite cost ratios as general efficiency claims. These machine-gold propositions were **not checked by an independent human reviewer** (see [review sheet](proposition-meaning-human-review-sheet-2026-10-24.md): 0/24 approved).

This is evidence of controlled role, quantity and grammatical-feature reconstruction under supplied instructions, not validated comprehension of connected text, pronoun anaphora, distributive scope, modal/peripheral relations or the full language. No English comparison, human readability test or final token-efficiency estimate was performed.

**Research direction:** review complete sentence meanings; separate semantic accuracy from output-format compliance; test targeted person/number and TAM ambiguities in *new* development texts; formalize/source-validate additional valency and relational frames **without** changing the canon merely to fit a benchmark; introduce genuinely connected discourse only after a referential model is ratified. Preserve previous negative trials and this failure report in the research diary.
