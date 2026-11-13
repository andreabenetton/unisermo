# UCUB: content-diversity reset — proposal (not ratified)

**Status: RESEARCH DRAFT, 13 November 2026. Do not populate human-facing Tally questionnaires or report comprehension results from this file yet.** This proposal responds to the owner's observation that all reviewed Unisermo passages look essentially alike.

## Diagnosis: the flaw is in sampling, not layout

The original `corpus.jsonl` has 80 **inference** cases but only 63 unique complete Unisermo passages. Deduplicating to 63 did not make them semantically varied: many are minimal contrasts in which `no`, tense, a person vowel or a numerical probability is the only change.

Measured on the **63 unique** complete passages in `unique_translation_review_63.jsonl`:

| Metric | Observed |
| --- | ---: |
| Complete unique passages | 63 |
| Whitespace word tokens (all clauses) | 373 |
| Unique surface word types | 41 |
| Average word tokens per full passage | 5.92 |
| Passages containing substring `akwa` | 36/63 |
| Passages containing substring `mov` | 36/63 |
| Passages containing standalone first-person pronoun `i` | 48/63 |
| Confirmed lexicon entries (`lexicon_index.json`) | 138 |
| Confirmed `verb` or `verb_root` entries | 26 |
| Confirmed entries categorized `noun` | 20 |
| Confirmed SI prefix entries within that 138 | 24 |

The confirmed index contains useful grammatical primitives but insufficient **common event/object vocabulary** to construct genuinely natural narratives across family, travel, workplace, health, messaging, decisions, uncertainty and everyday life without new lexical choices. This is a **content and lexicon coverage gap**, not a need for more artificial permutations of `vidi akwaem`.

## Two separate purposes, two separate corpora

**A. Diagnostic grammar/logic regression (existing UCUB-001).** Keep 80 controlled minimal contrasts to study negation, modality, quantifiers and entailment. It is an instrument for pinpointing an error, not a representative portrait of how Unisermo communicates.

**B. Natural communicative coverage (proposed UCUB-v2).** Select naturally varied **meanings and scenarios first in Italian**; only then translate into ratified Unisermo, checking parser and semantics. Each Unisermo passage appears **once** in human translation review; no human is asked to solve repeated logical alternatives for the same passage.

Neither corpus by itself demonstrates that Unisermo exceeds English in logical understanding or token efficiency. Model tests still require comparable controls, independent meaning checks and reproducible prompts.

## Italian-first candidate set

See [`proposals/communicative_diversity_36.json`](proposals/communicative_diversity_36.json): **36 distinct, untranscribed Italian meaning targets spanning 12 domains**. They are *requirements on future expressive coverage*, **not** Unisermo sentences, approved roots or finished translations. 11 examples are L1, 12 L2, 6 L3, 7 L4; re-balance only after lexical expressibility assessment. All cases have `unisermo: null` and `parser_verified: false` by design.

| Domain | Example of proposed Italian-first meaning | Key construction to audit |
| --- | --- | --- |
| Family | Mia madre vede la casa di mio fratello. | Possessives, relational kinship |
| Travel | Se il treno parte in ritardo, arriveremo dopo il tramonto. | Conditional + time relations |
| Household | Ho lasciato le chiavi sul tavolo, non nella borsa. | Locatives, negation, focus |
| Work/learning | So spiegare la regola, ma non so applicarla. | Know-how and co-reference |
| Care | Posso aiutarla, ma non sono autorizzato a farlo. | Capacity vs explicit permission |
| Communication | Mi ha detto che non sarebbe venuto, ma io non gli ho creduto. | Reported speech and belief |
| Normative distinctions | È illegale, ma non necessariamente immorale. | Law vs ethics, necessity |
| Epistemic claims | So che il documento è cambiato, ma non so chi l'abbia modificato. | Factivity and embedded question |
| Conditions | Se la porta è chiusa, non entrare. | Conditional and prohibitive imperative |
| Quantities | Due dei cinque pacchi pesano più degli altri. | Partitive and comparison |
| Questions | Chi ha autorizzato il trasferimento e in quale momento? | Wh and permission attribution |
| Short narrative | Ho preso il documento, l'ho mostrato a mia sorella e solo dopo l'ho spedito. | Event order, pronoun identity |

**Caution:** many of these semantic targets cannot currently be claimed expressible in the ratified grammar. This is intentional: it measures the gap instead of hiding it behind repetitive but valid clauses. Do not translate gaps by inventing unratified Unisermo vocabulary and treating it as canonical.

## Implementation pipeline, with explicit gates

1. **Intention coverage:** select or revise natural Italian scenarios, with a matrix of subject matter and grammatical structures. Avoid repetitive settings (same water, door, house, motion, vision) dominating the corpus.
2. **Lexical/structural feasibility audit:** for each Italian item classify (a) expressible with existing canonical lexicon and grammar, (b) grammar supports it but a root must be ratified, (c) grammatical structure itself is not yet ratified, or (d) genuine ambiguity requires a design decision. List required roots separately from required grammar decisions.
3. **Lexicon ratification:** prioritize the minimum natural, reusable roots that cover many scenarios, rather than inventing one root per sentence. Follow existing lexical-audit procedures and author approval; never put proposed roots in the confirmed lexicon automatically.
4. **Unisermo drafting:** use the accepted grammar to compose one full passage per scenario, record source and gloss, parse-test every sentence. A parser success confirms structure only; semantic equivalence is still reviewed by humans. A case that cannot be expressed should be **replaced or explicitly marked out of coverage**, not silently simplified to an unrelated claim.
5. **Human review UX:** one passage and one candidate Italian meaning, one equivalence choice, optional rewrite; interleave domains on each page so nearby cases have different situations. Use 1–4 clauses depending on intended difficulty, rather than increasing length merely by repeating facts.
6. **Reference validation:** at least two independent reviewers assess each candidate and adjudicate disagreements or ambiguities; keep original judgments and change logs. Optionally add an intentionally **incorrect** translation control for a *different* Unisermo passage, never reveal the control to reviewers or show a passage twice.
7. **Model pilot:** compare English and Unisermo versions under predeclared Cold/Lexicon/Grammar conditions on semantically diverse items, then diagnostic minimal pairs as a separate supplementary score. Freeze prompts, model, generation settings, and held-out cases. Report accuracy plus formatting compliance and tokens/cost per correct understanding.

### Suggested readiness conditions before refreshing the Tally questionnaires

- At least **10 substantively distinct communicative domains** included.
- No exact Unisermo passage repeated; no block of four adjacent passages differing in only one morpheme.
- No single content noun/verb or micro-scenario appears in a disproportionate share of cases (propose a roughly 15–20% ceiling per core root, subject to justified exceptions).
- At least five different sentence functions: assertions, descriptions, inquiries, commands/requests and multi-clause explanations; include varied persons, numbers, locations and time reference.
- Explicit audit of normal-life lexical adequacy and of parser unsupported structures; parser validity and lexical ratification recorded **separately**.
- Meaning-review labels must not be obtained from the parser or from the same models being benchmarked.

**Decision required before any permanent new grammar/lexicon or reviewed corpus:** accept/modify the domain matrix and decide which lexical gaps are worth filling first. This draft is a research direction, not a ratification request or a replacement to UCUB-001.

## Current forms

The four existing Italian Tally forms at `DqkEyX`, `zEyRoZ`, `5XjgDv`, `dba41D` are still the **old narrow 63-phrase prototype**; they are not suitable for claims about general comprehension. Do not link them as a representative, diverse evaluation until they are rebuilt from independently reviewed content.

