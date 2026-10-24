# Tally API integration — Unisermo stage-1 human comprehension

**Status:** source-controlled **draft candidate**, not published, not independently judged. This does not alter Unisermo grammar or the four-model PR #16 evidence.

Official Tally API: https://developers.tally.so/api-reference/introduction . Tally API supports draft creation via `POST https://api.tally.so/forms`, `Authorization: Bearer <API_KEY>`, pinned `tally-version`, and response retrieval via `GET /forms/{id}/submissions`. Free account supported; 100 API requests/minute. Tally also offers an OAuth-enabled MCP server, `https://api.tally.so/mcp`, and an official ChatGPT integration.

The current connector environment does **not yet have access to the user's Tally account**. Therefore no live form has been created or published. Avoid posting personal keys in chat. Key generation: Tally > Settings > API keys; credentials apply to all resources the user can access, so store privately. A user can connect the official Tally Forms ChatGPT plugin as an alternative to manually handling a token.

## Stage-1 structure

`benchmarks/corpus/tally-spontaneous-pretest-v1.json` lists six short sentences with varied lexemes and simple syntax. Three derive directly from canonical published examples and three are source-composed, **still requiring linguistic review before publishing**. This is a diagnostic **pretest only**, not a frozen benchmark or independent human gold.

- Italian introductory instructions, no glossary or reference translation
- Six optional open-ended text interpretations (one per sentence), labeled by stable `SP###` IDs
- One optional 1–5 self-confidence rating per sentence
- No name/email/phone collection; encourage voluntary anonymous participation
- No requirement to identify grammatical case, tense, or individual morphemes
- Formal user study will need participant-language/exposure metadata, randomized order and a reviewed set of keys; do not quietly assume that optional text fields represent comprehension failures

The API builder intentionally requests `status: DRAFT` and keeps the generated question and source code versioned. No source meanings or reference keys are exposed to participants.

## Running locally

```bash
python -m unittest discover -s tests -p 'test_tally_pretest.py' -v
python -m benchmarks.tally_pretest --dry-run > /tmp/unisermo-tally-draft.json
# After reviewing and authorizing your Tally account:
export TALLY_API_KEY='YOUR_KEY_FROM_TALLY_ACCOUNT'
python -m benchmarks.tally_pretest --create-draft
unset TALLY_API_KEY
```

The script prints the resulting form ID and corpus SHA256 after a successful API request, not the key. A live create has **not** been tried yet: exact block hierarchy/required fields must be confirmed against Tally server validation or through the OAuth-connected plugin and corrected before publication if needed. Form publication must be an explicit separate step after reviewing its rendered appearance. `--dry-run` performs no API calls.

## Research safety and consent

Treat this as a noninvasive anonymous pilot, not a clinical or psychometric instrument. Display a short privacy statement before sharing publicly, and avoid collecting names, addresses, age or other unnecessary personal data. Separate author pretest responses from independent participant answers. Use Tally's built-in data-access permissions rather than exposing API keys or response exports in public GitHub history.
