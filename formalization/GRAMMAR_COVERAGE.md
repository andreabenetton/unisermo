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
| Simple sentences | Preserves original SVO AST, finite agreement, accusative object, pronoun pro-drop, `ka`; adds selected cases and invariant relators | General SOV/OSV/topicalization and unrestricted lexical valency | `language/word_order.md` |
| Lexically constrained valency | Source-linked `mov` alternation, exact `traes` transition/result frames, `pel/trak X-em` force/patient frame (without displacement entailment), and explicit `es/ines/ades/dees/rees` quality/nominal-state predication; modal dependents share the validator | Remaining lexical roots lack ratified full valency: only minimal SVO/locative and free-relator syntax is parsed, with non-locative case roles rejected rather than guessed; no all-verb semantic certification | `language/derivation.md`, `language/verb_specification.md`, `language/copula.md`, `formalization/data/valency_frames.json` |
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
| Cause vs evidence vs inference | `P due Q` (Q finite), simple explicit `due Q, P` with comma, and nominal `due + NP` recognized as distinct constructs; `P nam Q` and `Q ergo P` retain different nodes | Fronted due without an explicit reliable simple-clause boundary, mixed or nested causal chains, causal truth and evidential validity | `language/noun_case_system.md`, `language/word_order.md` |
| Concessive/conditional | Explicit `se/etsi/etsise/eksese P alor Q`, bounded recursive pairing, simple postposed `etsi/etsise/eksese` | Subordination mixed with coordination, general `ekse` lexical exclusion, omitted `alor` for fronted templates | `language/word_order.md` |
| Purpose | `fin` + bare verb + simple object, or free relator + nominal NP | Other purpose-structure combinations and sufficiency thresholds `suf` | `language/noun_case_system.md` |
| Possession and focus | Typed personal genitives `is/us/as/ins/uns/ans` and referentially specific `aos/aes/anos/anes`, bounded prenominal genitive NPs, licensed postposed `part WHOLE-s`, NP-final `-si/-no` with distinct clause-negative focus | Nested/multiple possessor ambiguity, mixed focus + servile/whole-question/`no lim` scope, multiple focus per clause, postposed-genitive focus attachment | `language/negation.md`, `research/grammar/polarity_and_focus_clitics.md`, `language/noun_case_system.md`, `research/grammar/case_and_possession.md` |
| Comparison and degree | Some roots in lexicon; no complex degree parser | `major/minor/masim/minus`, `suf` threshold, manner of comparison | `language/comparison.md` |
| Productive derivation | Single-layer agent `-or`, instrument `-il`, domain `-ia`, abstract `-itat`, relational adjective `-al`, and bounded phase `in-/ad-/de-/re-`, joint-event `kun-`, restricted contrary `ne-`; case follows derived nouns, finite TAM follows derived verbs | Unlimited derivational stacking, lexicalized semantic reinterpretation, unratified roots and other prefixes | `language/derivation.md` |
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

## Focus and possession executable scope (2026-11-12)

The parser now records both the **focused constituent** and the **polarity**:
`i-si vidi` is additive focus without negation, while
`i-no vidi` is negative-additive focus with clause negative
polarity and `negation_type: negative_additive_focus`.
The latter is **not** the same AST as a free pre-verbal `no`,
and `i-no no vidi` is rejected as unratified stacking.

The hyphenated enclitic attaches to the last token of the entire
NP, e.g. `tik omni uman-no`; the nominal AST's `focus`
targets the complete constituent, not simply the head noun.
A lexical `analyze_word` analysis identifies the host token but
does **not** infer the full constituent's scope without parsing.
The implementation supports at most one focused NP in an ordinary
simple clause. Focus on modal, question-wide or wide-negation
structures remains **unimplemented**: these combinations are
rejected, not silently assigned semantics.

Personal possessives are parsed as genitive pronouns, not
independent gender-agreeing adjectives: `is domem` = my
house as a direct object; `tik umans domem` = the house of
this person as direct object. The new `possessor` subtree
preserves the genitive constituent separately from the possessed
noun's **own case**. The independently ratified part-whole
construction `part doms` places the genitive of the whole
after `part`, with its own `part_whole` relation node.
Only this explicitly attested part-whole frame is accepted
postnominally. Nested possessors, unspecified attachment and
postposed-genitive + focus are deliberately not yet resolved.

Positive and negative fixtures live in
`tests/test_focus_genitive_parser.py`. Parser implementation
does **not** create new lexemes or a new possessive suffix.

## Derivation and valency implementation (2026-11-13)

`generate_verb`, `generate_noun` and `analyze_word` now
share a bounded derivative resolver:

- `fakor`, `fakil`, `fakia`, `klaritat`,
  `umanitat` are productive **nominal** lexemes; the
  case is attached after derivation: `fakorem`,
  `fakias`, `klaritatem`.
- `fakal` is a relational **adjective**, not a noun or
  finite verb, and may be the only adjectival modifier
  in a restricted simple NP.
- `refak`, `adfak`, `infak`, `defak`
  and `kunfak` are compositional **verbs**;
  finite and resultative morphology remains regular.
- `nebel` is a bounded semantic antonym of a
  confirmed opposable quality. Arbitrary
  `ne-` + nominal, e.g. `nedom`, is not licensed.

Lexicalized words such as `major`, `kunten` and
`nelegal` retain indexed lexical meanings. The
source-derived form's status identifies whether its
base is a confirmed lexeme or only a normative
attestation. The lexicon itself is **unchanged**.

A source-linked valency table
(`formalization/data/valency_frames.json`) formalizes
the attested `mov` intransitive/causative alternation
and the two exact `traes` constructions. Other verbs
still require source-specific valency design.
`tests/test_productive_derivation_valency.py`
includes positive and negative executable examples.

## Evidence-based lexical valency, iteration 2 (2026-11-13)

The typed parser now differentiates **documented lexical frames**
from **unknown lexical frames**, not just syntactically case-marked
noun phrases. `Unisermo.valency_evidence(lemma)` returns
`status: documented` and a source for `mov`, `traes`,
`pel/trak` and the explicit `es` state family, or
`status: undetermined` for other verbal roots.
The executable audit CLI `python3 -m formalization valency --all`
lists every indexed verbal root with its recorded evidence status;
`python3 -m formalization valency pel` queries one root.

Documented constructions in the executable subset:

- `peli domem`, `traki domem`: explicit `X-em` is a
  force/patient role. Neither statement **entails displacement**.
  A local `-in` or ordinary free relator may be added as an
  independent adjunct; an unratified motion destination `-ad`
  is not inferred from a pushing/pulling verb.
- `i esi`: explicit existential copula. `dom esa bon`:
  explicit quality copula; `esi domin`: simple locative
  predicate. Phase verbs require a state: `adesi aper`,
  `inesi klus`, `deesi bon`, `reesi uman`. These retain
  their meaning as entry, persistence, exit, and resumption
  rather than receiving a new direct object case. The same
  bounded structure can occur under a servile head:
  `debi ades aper`.
- Earlier `mov` and `traes` frames are unchanged and
  remain checked by the same registry.

For `fer`, `portar`, `pens`, `kap`, `dik`,
`vid`, `fak`, `dok`, `ten` and similar roots,
the lexicon defines **meaning**, but a complete per-verb
argument-role inventory has **not** been ratified. The parser
preserves previously supported elementary SVO direct objects,
locative adjuncts and existing free relators, while refusing
unsupported `DEST-ad`, `SOURCE-de` and special result
case attachments rather than claiming that any verb licenses
them. This is a **parser coverage restriction**, not a
statement that all excluded sentences are ungrammatical
Unisermo.

All status and source data are in
`formalization/data/valency_frames.json`, with executable
positive/negative conformance in
`tests/test_verified_lexical_valency.py`. No new roots,
constructions or semantic restrictions have been ratified.

## Recommended continuation

The attested `pel/trak` force and `es` state frames are
implemented alongside `mov` and `traes`. Next prioritize
**author ratification of still-undetermined verbal argument frames**
before enforcing their valency; then **explicit semantic attachment
for complex nominal modifiers** and focus interactions with
serviles and compound clauses. Each addition needs positive and
negative conformance tests; an executable parser cannot invent
normative case semantics.
