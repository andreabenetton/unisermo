# Connective-system audit — 2026-10-24

Scope: normative grammar, confirmed lexicon, generated lexical and rule indexes, restricted parser, open PR dependency graph, and current CI. **No new language decisions are ratified by this audit.** Neither old historical source data nor semantic decisions may be changed to make an implementation test green.

## Findings (severity / evidence / action)

### C1 — Illegal letters in ratified exception words (blocking)

The author explicitly ratified `ecce` and `eccese` as exception and conditional-exception markers, but `formalization/data/morphology.json` defines alphabet `aeioupbtdkgmnfvszlrjw` with **no c**. Both new forms contain `c`; `formalization/build.py` rejects forms whose letters are absent from the accepted alphabet. Normative `language/vocabulary_design_rules.md` says source c is adapted **root by root**, not mechanically. This creates a real contradiction across approved specifications. Proposed *for author review only*: `ekse` ('except') and fused `eksese` ('unless'), both in the accepted alphabet. The user has **not** ratified any spelling change. Do not insert a c into the alphabet or rename lexical entries without approval.

### C2 — Parallel PR branch excludes independent conjunction ratification

PR #28 `feature/coordination-e-o-20261024` includes confirmed standalone conjunctions `e` AND and `o` OR, plus a fix for historically attested `bon`. It is not an ancestor of the PR #30→#31→#32→#33→#35→#36→#38 stacked branch. The #38 index does not include `e` and `o`. This is a branch topology / merge integration defect, **not** a retracting of either author decision. Resolve at integration time, after CI verification, preserving all independently ratified decisions.

### C3 — Duplicate attestation blocks generated-index validation

`formalization/data/attested_forms.json` contains a historical `bon` example and `research/lexicon/confirmed_lexicon.json` later confirms `bon`. In the #38 ancestry, `formalization/build.py` currently raises `ValueError: attested duplicate of confirmed core: bon` rather than retaining the historical attestation and emitting confirmed current status. PR #28 contains a provenance-preserving fix which needs integration to the other branch. Do not delete the original attestation.

### M1 — Parser explicitly lacks compound clauses

`formalization/parser/clause.py` supports a single finite-verb SVO clause, `[ka] [S-NP] [no] finite-V [OBJ-NP]`. A `se P, alor Q` sentence has multiple finite clauses; no coordination/causal/concessive/exception parse rules exist yet. Current ratification documents semantics and licensed orders; it is **not** implementation. Extend parser with explicit typed AST nodes only after the unresolved boundary/scope questions are decided. Maintain fail-closed behavior.

### M2 — Precedence and scope still underspecified

The existing grammar licenses stand-alone `e`, `o`, `se`, `alor`, `ma`, `ergo`, `due`, `nam`, `etsi`, `etsise`, `ecce`, `eccese`, and their simple cited patterns; but does not ratify precedence for mixed conjunctions (e.g. P e Q o R), associativity, nested conditionals, how omission of `alor` is delimited, or punctuation-only scope. No silent conventional operator precedence should be assumed.

### M3 — Meaning categories must not collapse

- `due`: factual real-world causation; nominal and finite-clause use, P due Q or due Q, P.
- `nam`: evidence or reason *adduced by speaker* for assertion P, not real-world cause nor guaranteed proof.
- `ergo`: inference/conclusion introduced from prior material.
- `etsi`: factual/accepted concession.
- `etsise`: hypothetical concession, antecedent not asserted true or false.
- `ecce`: general exclusion; `eccese`: conditional exception, different from `se no`.
- `se`: conditional; `alor`: consequent marker; `ma`: adversative contrast; `e` additive conjunction, `o` disjunction.

A grammar or AST must preserve these meaning categories, clause roles, factivity/assertion commitments, and modality, without treating `due` as evidential proof.

### M4 — Open semantic details

The following still require explicit author decisions rather than inferred ratification:
- Whether ordinary `o` is inclusive or exclusive where interpretation matters.
- Precedence/parenthesization and nesting for mixed coordinate and subordinate structures.
- Boundaries and optionality of `alor`, especially when nested.
- Exact semantic/operator scope of free `ecce` inside noun phrases.
- Scope and validation of `nam` as evidence marker (assertion vs quoted assertion).
- How to mark counterfactuality and hypothetical eventuality independently of `etsise`.
- Whether `se no`, `ma se`, `o se` are merely transparent compositions or licensed higher-order constructions; they were proposed but **not explicitly ratified** as whole constructions.

## CI status observed

At the #38 head SHA `cdb2dbfa0092ef50d0f4453ed7fab32b683c6146`, GitHub Actions lists `Numeral grammar and parser` and `Kinship parser regression` as **failed**, while `OpenAI tokenizer pilot` was **successful**. This audit does not call the failing branch validated. Independently, the invalid `c` spellings are demonstrably incompatible with the current alphabet.

## Recommended integration order (not authorization to merge)

1. Ask author to reconcile `ecce` / `eccese` spelling with the ratified 21-phoneme alphabet.
2. Integrate PR #28's independent e/o ratification and provenance-preserving duplicate handling into the connector stack.
3. Rebuild generated indexes using the actual generator and compare exact output; run full unit tests and GitHub CI.
4. Specify explicit coordination scope, nesting, clause boundaries and typed AST before implementing a full multi-clause parser.
5. Merge only after explicit author instruction.
