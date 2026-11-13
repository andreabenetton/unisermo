# Typed parser and semantic interpretation boundary

The deterministic `formalization.parser.proposition` now emits a
**source-constrained typed proposition AST** in a bounded subset of the
accepted grammar. The ordinary Phase 1 SVO analysis remains stable for
previously supported sentences. See
[GRAMMAR_COVERAGE.md](../GRAMMAR_COVERAGE.md).

## Grammar structures currently represented

- Ordinary `no` is local; `no lim` negates the whole licensed
  truth-conditional `e/o` expression; a later `lim` closes the
  current operand before the next connector.
- `e` AND, inclusive `o` OR, adversative `ma`, and
  initial-`o` n-ary **exactly-one** choice have distinct node types
  and roles. Three-way exclusive choice is not binary XOR parity.
- `due` is factual cause, `nam` evidence or justification,
  and `ergo` an inference. They remain different typed relations
  rather than a Boolean connector with guessed truth conditions.
- Anteposed `se/etsi/etsise/eksese ... alor ...` and selected
  postposed concessives/exceptions are represented with subordinate
  and matrix operands. Nested explicit `alor` pairing is supported.
- One finite servile (`pos/deb/vol/pot/sap/aut`) takes one
  uninflected verbal action, with negation stored either on the head
  or the dependent action. `aut SOURCE-de ROOT` retains a separate
  source-of-permission slot.
- Local event locatives are distinguished from a preposed locative
  that **might** frame a whole proposition: the latter is marked
  `attachment: undetermined` instead of claiming semantic clarity
  that the spoken surface does not supply.

- NP-final focus `-si/-no` is stored with explicit focused
  constituent attachment; negative-additive `-no` supplies
  negative clause polarity without becoming an ordinary free
  `no` predicate negator. Typed personal genitives and the
  explicitly ratified `part WHOLE-s` relation preserve
  possession and part-whole structures without inferring legal
  or physical ownership.

The typed implementation supports a small simple-clause set of
explicit cases, free relators, WH questions, stative zero copulas
and imperatives.

The source-constrained morphology parser also retains a derived
form's lexical base, affix and operation, distinguishing a productively
derived noun from an instrument/agent's actual real-world referent.
The `mov` valency role is not an assertion of physical causation;
the `traes` frames are typed argument configurations.

The documented force/patient frame `pel/trak X-em`
explicitly records **no entailment of successful displacement**.
The typed `es` state predicate is **not** an accusative object:
a form such as `adesi aper` identifies entry into a state
without inventing a new argument case. Missing per-verb case
licensing for other roots is openly classified
`undetermined`, not inferred from word meaning or affix
spelling.

Accepted LDR-0014 distinguishes the roles of direct
`X-em` participants in `fer`, `portar`, `ten`
and `kunten`. The parser emits `argument_roles`
for taking from a physical source, carrying toward a
destination, maintaining constraint and spatial
containment. These are **speaker-asserted roles**, not
a verified model of possession, authority, successful
arrival or physical plausibility. `kunten` explicitly
retains its specialized lexical containment rather
than generic joint `ten`. Contextual object omission
is not inferred and remains an open design decision.

## Semantics that are NOT yet implemented

No unrestricted lexical valency, world-model truth evaluation, referent
tracking, discourse-pragmatic inference, modal accessibility-world
reasoning, deontic authority resolution, institutional-domain
disambiguation, presupposition engine, unrestricted subordinate and
coordination interaction, full typed logical-form serialization, or
guarantee of English paraphrase equivalence is present.

The parser cannot infer that a `due`-related event really caused
another event; it can **only preserve the operator chosen by the
speaker**. Likewise, `nam` marks a stated reason, not necessarily
a true or valid proof. `aut` encodes that a permission relation was
asserted, not that an actual authority legally granted permission.

The four accepted grammatical records (LDR-0010 through LDR-0013)
remain normative unchanged. These executable additions do not
ratify unsupported nested modal negation, broad `no lim` over
discourse operators, question-wide compound scope, or arbitrary
domain/locative inference.
