# Language specification migration history

The files in this directory are the **live, editable language specification**.
They were initialized verbatim from `language(1).zip` on 2026-08-10 so that
subsequent changes are visible in Git history.

The immutable source snapshot is preserved at `legacy/original-language/`.
Research notes and quantitative evidence remain under `research/`.

## History repair note

Earlier confirmed design work was recorded primarily under `research/` rather
than being applied directly to the original Markdown specification. On
2026-08-10 the repository structure was repaired without rewriting old Git
history: the originals were imported verbatim, copied here, and the already
confirmed decisions were then applied in explicit migration commits. This
preserves an honest audit trail from the original documents to the current
specification without fabricating retroactive commits.

## Current migration commits

- `c7b9f16` — original Markdown imported verbatim and copied to `language/`
- `04dad80` — current phonology, person/number, finite verb architecture and lexical adaptation applied
- subsequent migration commit — remaining confirmed grammar and lexicon decisions applied

Use `git diff c7b9f16 -- language/` to inspect the evolution from the imported
originals, or compare a live file directly with its immutable counterpart under
`legacy/original-language/`.
