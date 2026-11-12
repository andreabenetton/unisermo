# Canonical grammar -> executable parser coverage

**Implementation inventory:** 2026-11-12.  
**Authority:** `language/` and `research/grammar/confirmed_decisions.json`
are normative; this matrix documents *parser support* only. It does not
canonize new words or rules. The original SVO AST for formerly supported
sentences stays backward compatible.

**Public interfaces:**
`Unisermo.parse_sentence(text)`,
`Unisermo.parse_proposition(text)`, and
`python3 -m formalization proposition "..." `.
The `sentence` CLI remains available as an alias to the typed parser.
Conformance: `tests/test_proposition_parser.py`; legacy morphology,
numeral, kinship and corpus tests still run.

## Coverage matrix

| Canonical area | Executable subset | Unsupported / unresolved | Main source |
|---|---|---|---|
| Alphabet, finite TAM/person/number | Confirmed regular `root+aspect+tense+person+number` and legacy accepted example roots; newly categorized `verb_root` entries recognized | Full productive phase/derivational paradigm | `language/verb_specification.md` |
| Seven nominal cases | Confirmed noun heads, nominalized participles, limited arguments with `-em/-ad/-de/-in` and special `-da` result | General lexical valency, all case stacking/order permutations | `language/noun_case_system.md` |
| Quantification | Existing canonical cardinal, ordinal, factor, fraction and percentage parser; one simple modifier at noun phrase level | Mixed numerals and modifiers without explicit rule; fraction NPs inside ordinary clauses | `language/numerals.md` |
| Kinship | Existing typed relation path, licensed `NUMjer` repetition | Arbitrarily deep or ambiguous kinship paths outside guarded subset | `language/kinship.md` |
| Simple sentences | Preserves original SVO AST, finite agreement, accusative object, pronoun pro-drop, `ka`; adds selected cases and invariant relators | General SOV/OSV/topicalization and arbitrary valency | `language/word_order.md` |
| Modal/servile complements | Single finite `pos/deb/vol/pot/sap/aut` + one bare verb root; distinct `no HEAD ROOT` and `HEAD no ROOT` | Nested serviles, stacked negation, independent subordinate subjects or unratified permission operators | `language/verb_specification.md`, `language/negation.md` |
| Source of permission | `aut SOURCE-de VERB`, source precedes action; action's own later source stays separate | More than one granting source; authority verification and normative domain inference | LDR-0012 |
| Zero copula | Limited stative quality head and explicit subject, including `tik no bel` | Full predicate noun-class system, adverbial comparatives and other copular argument frames | `language/copula.md` |
| Locative domains | Postverbal spatial `NP-in`; preposed `NP-in P` represented with *undetermined* attachment | Semantic disambiguation of physical event vs institution/rule/domain by position alone | LDR-0013 |
| Questions | Polar `ka`; limited licensed wh forms in simple clauses | General wh argument composition and whole-compound questions | `language/questions.md` |
| Imperative | Bare known verb root, optionally `no`, with `!` | Imperative valency, complex imperative clauses | `language/verb_specification.md` |
| Local negation | `no` on a finite predicate; distinct head/action negation in a modal | Focus clitic negative scope, arbitrary double negation | `language/negation.md` |
| Wide negation | `no lim` over the licensed truth-conditional `e/o` expression | Wide `no lim` over `ma/due/nam/ergo` or subordinate and modal scope | LDR-0010 |
| Free `e/o/ma` connectors | Right-associative, separate additive/inclusive/adversative typed nodes | Semantic/pragmatic explanation of adversativity; arbitrary mixed subordinate scope | `language/word_order.md` |
| Exclusive initial `o` | `o P o Q [o R...]` => n-ary exactly-one; right-association of final alternatives | Universal semantic Boolean evaluation and unrestricted nested XOR syntax | `language/word_order.md` |
| Explicit closing `lim` | Prior expression closes immediately before following connector; can combine with `no lim` | Arbitrary bracket syntax, parentheses and unratified scope crossing | `language/word_order.md` |
| Cause vs evidence vs inference | `P due Q` (Q finite) distinct from `P nam Q` and `Q ergo P`; `due + NP` recognized as nominal relator | Fronted `due Q, P` boundary in ambiguous free-form text; causal truth and evidential validity | `language/noun_case_system.md`, `language/word_order.md` |
| Concessive/conditional | Explicit `se/etsi/etsise/eksese P alor Q`, bounded recursive pairing, simple postposed `etsi/etsise/eksese` | Subordination mixed with coordination, general `ekse` lexical exclusion, omitted `alor` for fronted templates | `language/word_order.md` |
| Purpose | `fin` + bare verb + simple object, or free relator + nominal NP | Other purpose-structure combinations and sufficiency thresholds `suf` | `language/noun_case_system.md` |
| Possession and focus | Existing normal case and basic pronouns; word-level focus clitic meaning is ratified but not parsed | Focus enclitic `-si/-no` scope and unrestricted prenominal genitive association | `language/negation.md`, `language/noun_case_system.md` |
| Comparison and degree | Some roots in lexicon; no complex degree parser | `major/minor/masim/minus`, `suf` threshold, manner of comparison | `language/comparison.md` |
| Productive derivation | Explicit confirmed root/compound lexemes and existing nominalized participles | General recursive derivation; phase `ad-/de-/in-/re-`, agent `-or`, instrument `-il`, abstract `-itat` as freely generated parses | `language/derivation.md` |
| Full semantics | **Not implemented**: typed syntax only | Referent identity, truth tables, deontic authorization worlds, pragmatic entailments, causal verification, LLM interpretation | `formalization/semantics/README.md` |

## Safety and compatibility invariants

1. **Lexical roles:** use original confirmed lexical categories plus
   curated parser-role metadata in `formalization/data/lexical_roles.json`.
   Historical `example_only` and `decision_attested_not_indexed`
   entries retain their provenance and are not auto-ratified.
2. **Preserve the operator chosen:** `ma` is not rewritten as
   `e`; `nam` is not rewritten as factual `due`;
   an `exclusive_choice` is never represented as a parity-XOR.
3. **No false domain resolution:** a preposed locative is annotated
   with `attachment: undetermined` if its spatial versus
   proposition-domain interpretation cannot be established.
4. **Finite semantic boundaries:** enforce a maximum 128 words and
   16 structural recursion levels as parser safety limits, not
   linguistic prohibitions. Punctuation does not create `lim`
   or `alor` scope.
5. **Fail closed:** reject unsupported question-wide scope,
   missing `alor`, invalid `lim`, `no lim` over discourse
   operators, mixed subordinate/coordination, and unrecognized
   lexical predicates. No undocumented grammar is inferred.
6. **Backwards-compatible SVO AST:** simple `vidi domem`,
   `ka i no diki domem?`, `vidi bisim domem`, etc. retain
   their original outer node shapes and fields for benchmarks.

## Recommended continuation

Prioritize **controlled focus enclitics**, **typed possessive
and genitive noun phrases**, **reusable productive derivation** and
**non-ambiguous argument/valency schemas**. Each addition should
extend this matrix and add positive/negative executable tests;
no new lexemes or grammatical rules should be silently introduced.
