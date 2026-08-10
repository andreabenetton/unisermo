# Vocabulary Design Rules

This document defines how lexical forms are selected under the current
GlottoDelta phonology. The historical rules are preserved in
`legacy/original-language/vocabulary_design_rules.md`.

## 1. Allowed phonemes and letters

Every canonical lexical root is written with:

```text
a e i o u
p b t d k g m n f v s z l r j w
```

No canonical root contains source `c`, `h`, unitary `sh`, phonemic schwa, or a
separate affricate letter.

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
| `cap` | `kap` |
| `centr` | `sentrum` |
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
| `doc` | `dots` |
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
