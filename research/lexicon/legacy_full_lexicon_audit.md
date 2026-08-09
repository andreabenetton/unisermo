# Legacy Lexicon Audit

Status: audit against the current canonical phonology and confirmed lexical migrations.

Source: `language(1).zip`, SHA-256 `78ea47efca711a183d5a0b4bdea9024dc1992caed7a7b1a2ef9278520ee66951`.

## Scope

The machine audit scans all top-level legacy grammar documents (excluding the obsolete phonology document itself and meta README/CLAUDE files), extracts every token-like GlottoDelta form appearing in inline code, and classifies it against the current alphabet. This intentionally includes inflected/example forms so stale morphology is visible rather than silently ignored. A curated core inventory separates base lexical/grammatical items from generated examples.

## Summary

The original machine audit found three lexical collisions. All three are now resolved by canonical decisions:

- `kom` remains **HOW**; Latin `cum/com-` is `kun`.
- legacy `kur` **WHY** becomes `ker`; Latin `cura` is `kurar`.
- there is no indefinite article `un`; optional indefinite singularity uses the full numeral/determiner `uno`, while `un` remains the 2PL person form.

The machine-readable JSON has been updated with these resolutions while preserving the remaining phonology/morphology flags.

## High-priority findings

### Resolved lexical collisions

- `kom` is canonical **HOW**; the lexical root from Latin `cum/com-` is now `kun`.
- `ker` is canonical **WHY**; legacy `kur` with that meaning is retired, and the Latin `cura` lexical family uses `kurar`.
- `uno` is both numeral **ONE** and optional indefinite-singular determiner. There is no separate article `un`; `un` remains 2PL.

### Confirmed migrations detected

- `cin` -> `kin`
- `doc` -> `dots`
- `ekual` -> `ekwal`
- `fac` -> `fak`
- `nacion` -> `nation`

### Obsolete schwa/person forms

Any legacy form containing `ə` is obsolete. The current person system is `i/u/a` plus optional plural `/N/`, not six person vowels.

### Legacy `sh` and `j`

- Legacy `sh` cannot remain as a phonemic unit because `h` is not in the canonical alphabet; intended /sh/-like material must be reviewed as `sj` with `[sj~sh]` realization.
- Written `j` is now canonical /j/. Any legacy lexical item whose `j` intended /dzh/ requires review. `major` is already explicitly confirmed unchanged and is pronounced /ma.jor/.

### Adjacent vowels

Adjacent vowel letters are valid but are read as hiatus. Thus legacy `-ia` remains orthographically legal as /i.a/; this audit does not convert it to `-ja` automatically.

## Core inventory requiring attention

| Legacy form | Status | Canonical/replacement | Notes |
|---|---|---|---|
| `cin` | confirmed_replacement | `kin` | legacy form has a confirmed canonical replacement |
| `doc` | confirmed_replacement | `dots` | legacy form has a confirmed canonical replacement |
| `e` | obsolete_person_value | `u` | legacy person value is obsolete; current corresponding form is u |
| `ekual` | confirmed_replacement | `ekwal` | legacy comparison word replaced by ekwal /e.kwal/ |
| `fac` | confirmed_replacement | `fak` | legacy form has a confirmed canonical replacement |
| `kom` | valid_orthography | `—` | canonical HOW retained; lexical com-family moved to `kun` |
| `kur` | confirmed_replacement | `ker` | legacy WHY replaced by `ker`; care/cure root is `kurar` |
| `major` | confirmed_reinterpretation | `—` | confirmed spelling; current pronunciation /ma.jor/ |
| `nacion` | confirmed_replacement | `nation` | legacy form has a confirmed canonical replacement; adjacent vowels are canonical hiatus unless j/w is written |
| `o` | obsolete_person_value | `un` | legacy person value is obsolete; current corresponding form is un |
| `u` | obsolete_person_value | `in` | legacy person value is obsolete; current corresponding form is in |
| `un` | obsolete_legacy_reference | `uno` | no article `un`; optional indefinite determiner is `uno`; `un` remains 2PL |
| `ə` | obsolete_morphology | `an` | non-canonical character(s): ə; contains retired schwa / legacy six-person morphology; legacy person value is obsolete; current corresponding form is an |

## Full machine-readable inventory

See `legacy_full_lexicon_audit.json` for every extracted form, source documents, status, and issues. The full set is intentionally not flattened into this Markdown table because many entries are generated inflections or examples rather than independent dictionary roots.

## Interpretation

- `valid_orthography` means only that the spelling uses the current alphabet; it does **not** canonize the word or preserve its old semantics.
- `valid_check_hiatus` means the spelling is legal but adjacent vowels now have the explicit hiatus interpretation.
- `confirmed_replacement` is already resolved by a current lexical decision.
- `obsolete_legacy_reference` marks a stale legacy form/reference superseded by an already confirmed current form.
- `needs_revision`, `review_pronunciation`, and `obsolete_morphology` identify forms that cannot simply be imported unchanged.
