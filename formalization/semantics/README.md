# Semantics boundary

The current `formalization.parser` returns morphology and a restricted SVO clause AST.
It is **not** a complete semantic interpreter. Ambiguity is preserved at word level.

A future owner-approved LDR must define referent tracking, negation scope,
quantification, presuppositions, valency and logical-form serialization.
No LLM-efficiency claim may imply semantic equivalence from morphology alone.
