# Vocabulary Design Rules

This document defines how lexical forms are selected under the current
Unisermo phonology. The historical rules are preserved in
`legacy/original-language/vocabulary_design_rules.md`.

## 1. Allowed phonemes and letters

Every canonical lexical root is written with:

```text
a e i o u
p b t d k g m n f v s z l r j w
```

No canonical root contains source `c`, `h`, `x`, unitary `sh`, phonemic schwa, or a
separate affricate letter. The letter `x` is not an official Unisermo grapheme;
source `x` must be adapted root by root using only canonical units.

## 2. Glides and vowel sequences

`j=/j/` and `w=/w/` are consonantal glides.

Adjacent vowels remain vowels:

- `ia` = `/i.a/`
- `ua` = `/u.a/`

If a glide is intended, write it explicitly:

- `ja` = `/ja/`
- `wa` = `/wa/`

## 3. Coalescent sequences

The following underlying sequences may coalesce in fluent speech:

- `ts` = `/t+s/` → `[ts]`
- `tj` = `/t+j/` → `[tj ~ tʃ]`
- `dj` = `/d+j/` → `[dj ~ dʒ]`
- `sj` = `/s+j/` → `[sj ~ ʃ]`
- `gn` = `/g+n/` → `[gn ~ ɲ]`

The spelling always preserves the underlying sequence.

## 4. Source `c`

Source Latin/international `c` has no automatic conversion. Choose the lexical
adaptation root by root according to recognizability, accessibility,
genealogical dispersion, and collision risk. Possible outcomes include `k`,
`s`, `j`, and `tj`.

Once selected, the canonical spelling is stable.

## 5. Source /dʒ/

Canonical `j` never means /dʒ/. A source /dʒ/ may be represented by `dj`
(`/d+j/`, optionally `[dʒ]`) or by another root-specific adaptation such as
`j`, `g`, or `z` when the wider international root family favors it.

## 6. Accent-tolerant soft mergers

Canonical spelling preserves `b d g v z`, while these accent mergers are
accepted where no ambiguity is created:

- `b→p`
- `d→t`
- `g→k`
- `z→s`
- `v→[f]` or `[w]`; `[v~ʋ~β]` preferred when available
- broad rhotic realizations `[r~ɾ~ɹ~ʁ]`

Avoid fragile everyday minimal pairs whose only distinction disappears under
an accepted soft merger.

## 7. Confirmed migrated roots

| Historical/root family | Canonical root |
|---|---|
| `act` | `ager` |
| `cad` | `kad` |
| `cap` | `kap` (reassigned to cognitive 'understand'; no longer physical 'take') |
| `centr` | `sentr` |
| `cert` | `sert` |
| `circul` | `sirkul` |
| `civ` | `siv` |
| `clar` | `klar` |
| `com` | `kun` |
| `cred` | `kred` |
| `cur` | `kurar` |
| `dec` | `dek` |
| `dict` | `dik` |
| `direct` | `dirig` |
| `doc` | `dok` |
| `fac` | `fak` |
| `loc` | `lok` |
| `spec` | `spets` |
| `struct` | `stru` |
| `voc` | `vok` |
| old `cin` | `kin` |
| `nacion` | `nation` |

Other confirmed lexical items affected by the new phonology include:

- `major` remains `major`, now `/ma.jor/`
- `ekwal` = `/e.kwal/`
- `kom` = how?
- `ker` = why?

## 8. One-letter grammar forms

The single-letter personal pronouns/markers are `i`, `u`, and `a`. Plural adds
`n`: `in`, `un`, `an`.

No lexical root should be introduced that creates avoidable ambiguity with
these grammar forms.

## 9. Semantic specificity and exclusion of catch-all roots (author ratification 2026-11-14)

**Lexical roots are not required to provide a word-for-word equivalent to every
word in an existing natural language.** If a source-language word collects
different semantic categories, translate the *contextually intended category*,
not the source-language word as an undifferentiated sign.

A proposed root must have:
- a positive, testable semantic definition and explicit contrasts to near-neighbours;
- coherent referents or event frames, including any critical argument roles;
- evidence it cannot be rendered faithfully using existing roots, derived forms,
  or already approved grammar, without undue semantic loss;
- no unnecessary use as a generic placeholder for concept, proposal, plan,
  opinion, prediction, mental image, discovery or hunch.

**Explicit non-ratification: `ide` and any generic synonym meaning all senses of
Italian `idea` / English `idea` are excluded from the canonical vocabulary.**
Do not automatically introduce an equally broad synonym under another spelling.
A narrowly defined future root for a *specific* notion (e.g. submitted proposal)
is a separate semantic decision, not a reinstatement of generic "idea".

This principle concerns **heterogeneous polysemy**, not abstraction or useful
generality as such. Existing coherent roots such as `uman`, `mov`, `kon`,
`pens`, `kred`, `kap`, `sap` and `int` remain available under their
approved meanings. `kon` remains the concept noun and `-kon` remains
productive for concept-of-X; neither means generic idea, inspiration, hunch or
proposal. The Italian word `intuizione` likewise must be disambiguated by
epistemic status and process before any new root is adopted.

**Translator/benchmark rule:** Annotate the sense of each polysemous source
term before choosing a Unisermo realization. Mark unresolved cases as semantic
gaps rather than filling them with a generic word. A parser recognizing a form
does not certify its intended meaning.
