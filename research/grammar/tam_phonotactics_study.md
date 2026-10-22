# TAM phonotactics study: consonantal aspect vs vowel aspect

Status: **confirmed and canonicalized**. The vowel-aspect proposal in this study was accepted on 2026-08-10; references to the “current” consonantal system below describe the pre-change baseline at the time the experiment was run.

This study originally compared the then-current finite-verb morphology with a proposed change that replaced consonantal aspect markers `n/b` with vowel markers `e/o` and moved aspect before time. The proposal was subsequently confirmed and is now canonical.

## Systems compared

Former canonical system (experimental baseline):

```text
root + time(0/d/f) + aspect(0/n/b) + person(i/u/a) + number(0/n)
```

Confirmed vowel-aspect system:

```text
root + aspect(0/e/o) + time(0/d/f) + person(i/u/a) + number(0/n)
```

A control order was also measured:

```text
root + time(0/d/f) + aspect(0/e/o) + person(i/u/a) + number(0/n)
```

The control checks whether putting vowel aspect **before** time really matters.

## Samples

Two samples are used.

1. `confirmed_plus_live`: 25 current confirmed lexical roots plus the live verb
   roots `mov`, `vid`, and copular `es` where they were not already present.
2. `currentized_seed74`: the 74-root provisional Latin/international seed, with
   every root that already has a confirmed replacement migrated to its current
   Unisermo form.

Each root generates all 54 finite cells:

```text
3 times x 3 aspects x 3 persons x 2 numbers = 54 forms
```

The script counts only vowel/consonant runs that contain morphology. Purely
lexical runs internal to the root are not counted as morphology-created runs.

## Main result

### 25-root current sample, 1,350 forms

| system | C>=2 | C>=3 | C>=4 | V>=2 | V>=3 | canonical collisions |
|---|---:|---:|---:|---:|---:|---:|
| former `T + n/b` | 87.1% | 48.0% | 5.3% | 0.4% | 0.0% | 0 |
| canonical `e/o + T` | 21.3% | 2.7% | 0.0% | 24.4% | 0.9% | 0 |
| control `T + e/o` | 64.0% | 8.0% | 0.0% | 67.1% | 0.9% | 0 |

Moving vowel aspect before time reduces morphology-created C>=3 runs from
48.0% to 2.7%, a relative reduction of about 94.4%. It also eliminates every
C>=4 run in this sample.

### Currentized 74-root seed, 3,996 forms

| system | C>=2 | C>=3 | C>=4 | V>=2 | V>=3 | canonical collisions |
|---|---:|---:|---:|---:|---:|---:|
| former `T + n/b` | 85.9% | 52.3% | 10.8% | 0.8% | 0.0% | 0 |
| canonical `e/o + T` | 20.7% | 5.4% | 0.0% | 26.0% | 1.5% | 0 |
| control `T + e/o` | 65.0% | 16.2% | 0.0% | 67.4% | 1.5% | 0 |

The larger seed confirms the same pattern. C>=3 runs fall from 52.3% to 5.4%,
a relative reduction of about 89.7%, and C>=4 runs again disappear entirely.

## Why aspect-before-time is better than time-before-aspect

With vowel aspect after time, the time consonant still contacts a consonant-final
root, while the aspect vowel contacts the person vowel in every tense.

For example:

```text
root + T + A + P
mov  + d + e + i -> movdei
```

This leaves a `vd` consonant contact and an `ei` hiatus.

With aspect before time:

```text
root + A + T + P
mov  + e + d + i -> movedi
```

The aspect vowel separates the root from the time consonant, while the time
consonant separates aspect from person. Only present aspect-marked forms, where
time is zero, contain the aspect-person hiatus.

This is why the control order has V>=2 in about 67% of all forms, versus only
24-26% when aspect precedes time.

## Examples

First-person singular `mov`:

| time/aspect | former consonantal | canonical vowel aspect before time |
|---|---|---|
| present simple | `movi` | `movi` |
| present progressive | `movni` | `movei` |
| present perfect | `movbi` | `movoi` |
| past simple | `movdi` | `movdi` |
| past progressive | `movdni` | `movedi` |
| past perfect | `movdbi` | `movodi` |
| future simple | `movfi` | `movfi` |
| future progressive | `movfni` | `movefi` |
| future perfect | `movfbi` | `movofi` |

The improvement is especially visible with `vid`:

```text
current:   viddni, viddbi, vidfni, vidfbi
proposal:  videdi, vidodi, videfi, vidofi
```

The current past-progressive form contains `ddn`; the proposal replaces it with
an alternating sequence centered on vowels.

## Root-final vowel cost

The proposed system creates more vowel adjacency. This is concentrated in
predictable locations.

Current inventories contain very few vowel-final roots:

- current 25-root sample: 1 (`stru`)
- currentized 74-root seed: 5 (`audi`, `bi`, `equ`, `medi`, `stru`)

No root in either sample ends in `e` or `o`.

For `stru`:

```text
strui   simple present
struei  progressive present
struoi  perfect present
struedi progressive past
struodi perfect past
```

Triple-vowel runs therefore occur only with a small vowel-final subset and only
in present aspect-marked forms. They occur in 0.9% of the current-sample forms
and 1.5% of seed forms.

## Surface collisions

There are **zero canonical surface collisions** in either sample under the
current system or the `e/o` proposal.

There are also no current root pairs of the form `R` vs `R+e` or `R` vs `R+o`.
Such pairs would be dangerous under vowel aspect. For example, if both `mov`
and `move` were lexical roots, then:

```text
mov + e + i = movei
move + 0 + i = movei
```

Therefore a vowel-aspect system should add a lexical collision check for future
roots that differ only by final aspect vowel `e/o`.

## Accessibility of the vowel opposition

The family-dispersion study on branch `family-dispersion-study`
(`3c837f5f0d96ad5d5a00d7fd47cf52a8207259ea`) gives the following strict
population/family scores for the relevant phonemes:

| phoneme | P_attested | population-weighted family support F |
|---|---:|---:|
| `n` | 93.3% | 87.8% |
| `b` | 80.1% | 88.2% |
| `e` | 78.3% | 86.6% |
| `o` | 77.7% | 85.5% |

Thus `e/o` are not individually more universal than `n/b`. The benefit is not
phoneme inventory coverage; the benefit is **syntagmatic phonotactics**: vowels
break the clusters created when several consonantal morphemes are concatenated.

Among all five-vowel pairs, `e/o` have a unique structural advantage: they are
the only two vowels outside the person-vowel set `i/u/a`. Therefore they create
no canonical aspect=person identical-vowel sequence. Any pair using `i`, `u`,
or `a` would overlap directly with at least one person marker.

## Accent-risk diagnostic

Current phonology allows optional `-e/-o` specificity vowels to approach
`[i]/[u]` in accents without stable mid vowels, provided grammatical information
remains recoverable. If the same tolerance were extended to grammar-critical
aspect vowels, a specific present-tense vulnerability appears.

Worst-case diagnostic assumptions:

1. aspect `e -> i` and aspect `o -> u`;
2. identical adjacent aspect/person vowels coalesce.

Then:

```text
movei -> movii -> movi
movou -> movuu -> movu
```

The progressive first-person present could collapse into simple first person,
and the perfect second-person present could collapse into simple second person.
The same applies to their plural forms.

This affects 4 aspect-marked cells out of 54 cells per root (7.4%) under that
worst-case combination of raising plus hiatus coalescence. The diagnostic is not
a canonical pronunciation rule; it identifies the condition the grammar must
explicitly prevent if `e/o` become obligatory aspect markers.

## Interpretation

The quantitative result is asymmetric:

- **Strong gain:** drastic reduction of morphology-created consonant clusters.
- **Moderate cost:** predictable vowel hiatus, mostly exactly two vowels.
- **Small lexical cost today:** no actual `R`/`R+e,o` collisions in either root
  inventory tested.
- **Real accent-design issue:** grammar-critical `e/o` cannot be allowed both to
  raise into person vowels and then coalesce with those person vowels.

Purely phonotactically, `root + aspect(e/o) + time(d/f) + person + number` is
clearly superior to the former consonantal `root + time + aspect(n/b) + ...`
system on the tested inventories. This result is now canonical.

The design question was resolved affirmatively: Unisermo makes the mid-vowel contrast `e/o` obligatory for finite aspect when overt. The phonology therefore requires aspect `e/o` to remain recoverably distinct from person `i/u/a`, and aspect-person hiatus may not be lost through coalescence when that would erase aspect.

## Reproduction

Run:

```text
python3 scripts/analyze_tam_phonotactics.py
```

Machine-readable output:

`research/grammar/tam_phonotactics_results.json`
