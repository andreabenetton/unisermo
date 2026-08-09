# Quantitative study: what should written `c` mean?

## Scope

This is a lexical/orthographic audit of the frozen provisional `latin_roots_seed.json`. It tests whether adding a written `c` as a soft category is justified by preservation of Latin/international root shapes. It is **not** a phoneme-prevalence study and the 74-root seed is **not** a frequency corpus.

For reproducibility, a `c` immediately before `e` or `i` is classed as a **soft-context** occurrence. Non-final `c` elsewhere is **hard-context**. Final `c` is reported separately because truncated roots such as `fac-`, `doc-`, and `voc-` can show derivative alternations in descendant languages; when a strategy requires a fixed bare-root reading, final `c` is mapped with /k/.

## Distribution of `c` in the 74-root seed

- Roots: **74**.
- Roots containing `c`: **20/74 = 27.0%**.
- Total `c` occurrences: **21**.
- Soft-context (`ce/ci`): **4/21 = 19.0%**.
- Hard-context: **11/21 = 52.4%**.
- Final `c`: **6/21 = 28.6%**.
- Hard-or-final combined: **17/21 = 81.0%**.

Soft-context roots are `centr`, `cert`, the first `c` of `circul`, and `civ`. Hard-context examples include `cap`, `clar`, `com`, `cur`, `dict`, and `struct`; final examples include `fac`, `doc`, `loc`, `spec`, and `voc`.

## Strategy comparison

| Strategy | Exact roots retained | Exact c-roots retained | Total edit distance | Mean similarity | Canonical collisions |
|---|---:|---:|---:|---:|---:|
| c = soft category [ts~tsh~s]; hard/final c -> k | 57/74 (77.0%) | 3/20 (15.0%) | 17 | 93.5% | 0 |
| no c; soft c -> s; hard/final c -> k | 54/74 (73.0%) | 0/20 (0.0%) | 21 | 92.2% | 0 |
| no c; soft c -> tj; hard/final c -> k | 54/74 (73.0%) | 0/20 (0.0%) | 25 | 91.4% | 0 |
| c = /k/; soft c -> s | 70/74 (94.6%) | 16/20 (80.0%) | 4 | 98.7% | 0 |
| contextual c: soft before e/i, /k/ elsewhere | 74/74 (100.0%) | 20/20 (100.0%) | 0 | 100.0% | 0 |

### Root-by-root effect on the 20 `c`-bearing roots

| Seed root | soft `c` `[ts~tʃ~s]` | no `c` (`s/k`) | `c=/k/` |
|---|---|---|---|
| `act` | `akt` | `akt` | `act` |
| `cad` | `kad` | `kad` | `cad` |
| `cap` | `kap` | `kap` | `cap` |
| `centr` | `centr` | `sentr` | `sentr` |
| `cert` | `cert` | `sert` | `sert` |
| `circul` | `cirkul` | `sirkul` | `sircul` |
| `civ` | `civ` | `siv` | `siv` |
| `clar` | `klar` | `klar` | `clar` |
| `com` | `kom` | `kom` | `com` |
| `cred` | `kred` | `kred` | `cred` |
| `cur` | `kur` | `kur` | `cur` |
| `dec` | `dek` | `dek` | `dec` |
| `dict` | `dikt` | `dikt` | `dict` |
| `direct` | `direkt` | `direkt` | `direct` |
| `doc` | `dok` | `dok` | `doc` |
| `fac` | `fak` | `fak` | `fac` |
| `loc` | `lok` | `lok` | `loc` |
| `spec` | `spek` | `spek` | `spec` |
| `struct` | `strukt` | `strukt` | `struct` |
| `voc` | `vok` | `vok` | `voc` |

### Proposed soft `c` = `[ts ~ tʃ ~ s]`

If `c` is reserved for the soft category and hard/final Latin `c` is normalized to `k`, only **3/20 = 15.0%** of the roots containing `c` remain exactly unchanged. Across the whole seed, **57/74 = 77.0%** remain exact.

Compared with simply having **no `c`** and writing soft-context `c` as `s`, soft `c` saves only **3 exact root spellings** and **4 character substitutions** in this seed.

The soft-`c` strategy creates **0 canonical root collisions**. Allowing its `[s]` accent realization also creates **0 collisions within this 74-root seed**. Thus collision risk is not the immediate problem here; the main cost is that most Latin `c` occurrences are not soft-context occurrences.

### What if all inherited `c` spellings were kept but `c` were always soft?

That would put **17/21 = 81.0%** of the current `c` occurrences into a hard-or-final context, affecting **17/20 = 85.0%** of the `c`-bearing roots. In other words, an always-soft `c` cannot preserve both spelling and the current root-level sound structure for most of the seed.

### The orthographically strongest alternative

If `c` represented /k/ and soft-context `c` were rewritten `s`, **70/74 = 94.6%** of all roots would stay exactly unchanged. This is much stronger for Latin-root preservation than soft `c`. But it is compatible with the project's one-to-one spelling principle only if `k` ceases to be a second spelling of /k/; that is a separate orthographic decision, not a result of this test.

A traditional contextual `c` would preserve 100% of spellings, but it directly violates the current fixed grapheme-to-phoneme principle by making `c` context-dependent.

## Preliminary conclusion

On the current 74-root seed, **adding `c` specifically as a soft `[ts ~ tʃ ~ s]` category has a small lexical-recognition payoff**. Only 19.0% of `c` occurrences are in the simple `ce/ci` soft context, and relative to the no-`c` + `s/k` solution the new grapheme preserves only three additional roots exactly. The proposal is collision-safe in this seed, but the benefit is too small to justify freezing `c` yet.

Before a final orthographic decision, this test should be repeated on the planned 300–500-root Latin/international candidate lexicon. If the same ratio persists, the quantitative evidence would favor **no soft `c` phoneme/grapheme**; if preserving Latin spelling is prioritized strongly enough to keep `c`, the data currently favor investigating **`c` for /k/** (with `k` correspondingly reconsidered) rather than `c` for the soft category.
