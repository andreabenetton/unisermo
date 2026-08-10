# CLAUDE.md

Guidance for Claude when working on the synthetic language specification in this directory.

## Example-word verification (mandatory)

Whenever you introduce a word as an example — in any specification document or in a chat response — you must verify that it contains **only letters from the official alphabet** defined in `alphabet_and_phonology.md`:

```
a e i o u ə
p b t d k g
m n
f v s z
sh ts c j
l r
```

The digraphs `sh` and `ts` are single written units. The sequence `ng` is allowed only as the two phonemes /n/ + /g/.

Letters **not** in the inventory include: `h`, `w`, `y`, `q`, `x`, and any accented or non-Latin character.

If a candidate example word (typically an international root being adapted) contains a letter outside the inventory:

1. **Adapt it** according to `vocabulary_design_rules.md` §4 (Adaptation Rules for International Roots). For example: `h` → delete; `w` → `u` or delete; consonantal `y` → `i` or delete; `q` → `k`; `x` → `ks`; `ph` → `f`; `ch` /tʃ/ → `c`; `j` /ʒ/ in a source language → `j` /dʒ/ in this language.
2. **Explain the adaptation in the interactive output** to the user — name the source word, identify the forbidden letter(s), and state the chosen replacement. Do not silently rewrite a word, and never include an example that violates the alphabet without flagging it.

## Lexicon-consistency check (mandatory)

Whenever the user's message — or a draft you are producing — uses a term that already has a definition in the spec, you must:

1. **Use the existing definition.** Do not silently introduce a competing form. Look up the canonical form (with `grep -rn` across the spec, or by reading the relevant document — typically one of `verb_specification.md`, `noun_case_system.md`, `noun_number_system.md`, `numerals.md`, `articles.md`, `negation.md`, `questions.md`, `copula.md`, or `vocabulary_design_rules.md` §5) and write that form into the new document.
2. **Flag the inconsistency to the user in the interactive output.** Name the term, cite the existing definition (with file and section), state the form you are using, and ask whether the existing definition should stand or be revised.

Examples of inconsistencies to catch:

- A term used with a different form (`du` vs `duo`, `tri` vs `ter`, `ic` vs `tik` (previously `ti` vs `ic`), `un` vs `uno`, `kap` vs `ka`).
- A position rule that contradicts an established one (e.g. a particle that was previously sentence-initial now appearing sentence-finally).
- A word being reused for a meaning that would clash with an existing meaning (note that `es` legitimately has three roles — copula root, possessive "your sg.", free-form preposition "of" — these are documented; a fourth role would need to be flagged).

Never silently overwrite an established term; never silently accept a new spelling without first asking the user to confirm the change.
