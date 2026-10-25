# Connector audit remediation

## Remediation follow-up (2026-10-24)

Author approved canonical `ekse` and fused `eksese`, replacing the illegal spellings `ecce`/`eccese` in the active lexicon and grammar. The remediation branch `fix/connectives-three-issues-20261024` also includes independently ratified `e`/`o` and source-preserving duplicate-attestation behavior (confirmed `bon` remains confirmed, earlier example retained). This audit describes findings at earlier branch heads; the remediation is not a merge into main. Nested connective clause parsing, precedence, and semantic scope remain open.

Implementation checklist:
- Canonical forms `ekse` and `eksese` in lexical source and normative docs
- `e` / `o` included from PR #28
- Historical attestation of `bon` preserved while live index uses confirmed record
- Generated indexes updated and regression tests for all three changes
- Await CI confirmation before marking resolved
