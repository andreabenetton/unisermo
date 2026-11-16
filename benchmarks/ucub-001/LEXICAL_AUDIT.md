# UCUB-001 lexical audit — 2026-11-13

**Status:** Experimental assessment, no lexical ratifications.

## Ground-truth inventory distinction

- `research/lexicon/confirmed_lexicon.json` has **108 entries**, including function words, numerals, compounds, derivations and degree markers; 108 is **not** a count of independently usable lexical roots.
- `formalization/data/lexicon_index.json` contains **143 entries**: **35** are outside the 108-entry confirmed list and can have `decision_attested_not_indexed` or `example_only` status. Such entries are NOT automatically newly confirmed.
- In current UCUB candidates, **`vid`, `mov`, `dom` are absent from `confirmed_lexicon.json`** but are attested in parser's index. Their source/status must be tracked. Do not label them confirmed merely because the parser accepts them.
- The current candidates use approximately a dozen distinct content roots, far less than the canon already offers, and overuse `vid/mov/dom`. This is a design weakness, not proof that the language needs new vocabulary.

## Existing canonical coverage relevant to testing

| Function | Existing forms (illustrative) | Research opportunity |
|---|---|---|
| Physical action | `fer`, `portar`, `ten`, `kunten`, `pel`, `trak` | Acquisition vs transport vs holding vs containment; non-entailments |
| Mental/cognitive | `kap`, `pens`, `sap`, `kred` | Understanding, belief, knowledge, thinking are not interchangeable |
| Modal/servile | `pos`, `deb`, `vol`, `pot`, `aut`, `sap` | Ability vs opportunity vs permission vs obligation |
| Speech/teaching | `dik`, `dok`, `vok` | Subject and object-role contrasts once valencies are confirmed |
| Qualities | `bon`, `bel`, `just`, `legal`, `apt`, `klar`, `medi` | Negative vs contrary, degree and comparison |
| Kinship | `gen`, `geno`, `gene`, `adel`, `adelo`, `adele`, `fil`, kinship compounds | Genitive scope, family-relationship direction |
| Entities | `uman`, `porta`, `part`, `akwa`, `aerplan` | Agent, patient, cargo, containment, part/whole |
| Connectives | `e`, `o`, `se`, `alor`, `ma`, `due`, `nam`, `ergo`, `etsi`, `etsise`, `eksese` | Entailment vs evidence vs real causation; avoid unratified scope |
| Derivation | `-or`, `-il`, `-al`, `-it`, `-itat`; prefix `ne-` | Novel composition with accepted productive morphology |

## Concrete gaps to assess before ratification

1. **Time and event reference:** limited unambiguous noun inventory for days, events, and temporal anchors. The relator `tem` exists, but rich narrative time references need a controlled list.
2. **Everyday physical objects/locations:** there are few neutral, independently confirmed patient/goal/location nouns for swapping while holding valency fixed; `dom` is only example-attested in the parser index.
3. **Communication and information entities:** propositions, messages, statements, information artifacts are not yet densely represented by confirmed standalone noun roots, which limits discourse-reference tests.
4. **Distinct individuals and identity tracking:** role-neutral nouns/pronominal referencing are present, but named distinct entities and reference-recovery conventions must be carefully verified before testing rich anaphora.
5. **Lexical valency coverage:** many confirmed action roots lack individually ratified argument frames. This is a *semantic/valency gap*, not necessarily a shortage of words.

## Decision

**Do not ratify new words solely to inflate this benchmark.** First enlarge the *used* lexical subset with existing canon and use the valency frames already approved. Create a separate, non-normative proposal list for genuinely necessary missing lexemes. Any adopted term needs a separate LDR and explicit author acceptance.

## Candidate quality alerts

- Current `candidates.jsonl` is a **draft**, not 80 independently validated semantic cases.
- Level 1 emphasizes TAM and a few verbs; it does **not yet satisfy** the protocol's promised genitive/derivation breadth.
- Level 3 repeatedly tests only a small inventory of `e/o/no lim` propositions; broaden valid implication patterns before scored tests.
- Level 4 has only a small number of source clauses rearranged into short documents; it does **not yet demonstrate** cross-sentence reference tracking.
- `UC020` exercises ratified `fer` physical acquisition and `porta` as its object; it does not imply ownership or permission.
- A split with 60 development/20 holdout has been restored, and complete minimal-pair families remain in a single split, **but the grouping itself needs semantic/template-leakage review**.
- English equivalence and parser verification remain unreviewed. In particular, do not use automated exact-answer scoring as a substitute for independent semantic gold review.

## Next implementation gates

(1) Add candidate-level lexical provenance (`confirmed_lexicon` vs `decision_attested_not_indexed` vs `example_only`), (2) generate a deterministic validation report, (3) diversify across *ratified frames*, (4) conduct independently reviewed English equivalents, (5) freeze prompts and holdout only after audit.
