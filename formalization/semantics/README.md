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

The typed implementation supports a small simple-clause set of
explicit cases, free relators, WH questions, stative zero copulas
and imperatives.

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
