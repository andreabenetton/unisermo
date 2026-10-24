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
