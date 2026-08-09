# Legacy Lexicon Audit

Status: audit against the current canonical phonology and confirmed lexical migrations.

Source: `language(1).zip`, SHA-256 `78ea47efca711a183d5a0b4bdea9024dc1992caed7a7b1a2ef9278520ee66951`.

## Scope

The machine audit scans all top-level legacy grammar documents (excluding the obsolete phonology document itself and meta README/CLAUDE files), extracts every token-like GlottoDelta form appearing in inline code, and classifies it against the current alphabet. This intentionally includes inflected/example forms so stale morphology is visible rather than silently ignored. A curated core inventory separates base lexical/grammatical items from generated examples.

## Summary

- `collision`: 3
- `confirmed_reinterpretation`: 1
- `confirmed_replacement`: 5
- `needs_revision`: 65
- `obsolete_morphology`: 9
- `obsolete_person_value`: 3
- `review_pronunciation`: 3
- `valid_check_hiatus`: 17
- `valid_orthography`: 267

## High-priority findings

### Lexical collisions

- `kom`: legacy question word **HOW** collides with confirmed root `kom` from Latin `cum/com-` (**with / together / com-**). Requires a future lexical decision; neither sense is silently reassigned here.
- `kur`: legacy question word **WHY** collides with confirmed root `kur` from Latin `cura` (**care / cure**). Requires a future lexical decision.
- `un`: legacy article material uses `un`, while current `un` is the second-person plural pronoun. The old article system is already non-canonical, but the form must not be re-imported with that meaning.

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
| `kom` | collision | `—` | collision: legacy kom = 'how'; confirmed lexical root kom = 'with/together, com-' |
| `kur` | collision | `—` | collision: legacy kur = 'why'; confirmed lexical root kur = 'care/cure' |
| `major` | confirmed_reinterpretation | `—` | confirmed spelling; current pronunciation /ma.jor/ |
| `nacion` | confirmed_replacement | `nation` | legacy form has a confirmed canonical replacement; adjacent vowels are canonical hiatus unless j/w is written |
| `o` | obsolete_person_value | `un` | legacy person value is obsolete; current corresponding form is un |
| `u` | obsolete_person_value | `in` | legacy person value is obsolete; current corresponding form is in |
| `un` | collision | `—` | collision: legacy un appears in article/indefinite discussion, while current un is the second-person plural pronoun |
| `ə` | obsolete_morphology | `an` | non-canonical character(s): ə; contains retired schwa / legacy six-person morphology; legacy person value is obsolete; current corresponding form is an |

## Full machine-readable inventory

See `legacy_full_lexicon_audit.json` for every extracted form, source documents, status, and issues. The full set is intentionally not flattened into this Markdown table because many entries are generated inflections or examples rather than independent dictionary roots.

## Interpretation

- `valid_orthography` means only that the spelling uses the current alphabet; it does **not** canonize the word or preserve its old semantics.
- `valid_check_hiatus` means the spelling is legal but adjacent vowels now have the explicit hiatus interpretation.
- `confirmed_replacement` is already resolved by a current lexical decision.
- `collision` needs a lexical decision because two meanings currently compete for the same form.
- `needs_revision`, `review_pronunciation`, and `obsolete_morphology` identify forms that cannot simply be imported unchanged.
