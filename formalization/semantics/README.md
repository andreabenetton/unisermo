# Semantics boundary

The current `formalization.parser` returns morphology and a restricted SVO clause AST.
It is **not** a complete semantic interpreter. Ambiguity is preserved at word level.

A future owner-approved LDR must define referent tracking, negation scope,
quantification, presuppositions, valency and logical-form serialization.
No LLM-efficiency claim may imply semantic equivalence from morphology alone.

The author-ratified `no lim` wide-scope grammatical construction covers a
restricted truth-conditional `e/o` clause subset (see `language/negation.md`).
This remains **a normative documentary rule, not executable parser support**.
The current Phase 1 sentence parser must continue to reject unsupported
compound or wide-negation input; LDR-0010 tracks the decision boundary.

Servile verbs use an accepted finite modal/know-how head plus a bare root.
The 2026-11-12 ratification distinguishes `no [finite servile] ROOT`
(negation of the modal/know-how relation) from `[finite servile] no ROOT`
(modality of a negated dependent action). This remains a normative grammar
rule and is **not** implemented by the restricted Phase 1 parser; see
LDR-0011 and `language/verb_specification.md`.
