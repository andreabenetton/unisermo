# Derivational Morphology

A formal specification of the derivational morpheme system of the synthetic language. Twenty morphemes — five suffixes (`-er`, `-or`, `-ia`, `-it`, `-al`) and fifteen prefixes (`no-`, `anti-`, `de-`, `re-`, `pre-`, `pos-`, `ko-`, `auto-`, `semi-`, `multi-`, `neo-`, `super-`, `sub-`, `mikro-`, `makro-`) — build new lexical items from existing roots, **before** any inflectional morphology (plural, case) is applied.

## Related documents

- The plural suffix `-en` and the gerund / plural overlap are in [`noun_number_system.md`](noun_number_system.md) (§3 and §4).
- The gerund (root + `-en` on a verb root) is defined in [`verb_specification.md`](verb_specification.md).
- The case suffixes that follow the plural are in [`noun_case_system.md`](noun_case_system.md).
- The prefix `no-` reuses the form of the sentential negation particle `no` from [`negation.md`](negation.md); spelling (attached vs free) distinguishes the two.
- The conjunction `or` (free word) shares its written form with the suffix `-or`; spelling distinguishes them.
- The phonotactic and adaptation rules that govern the choice of root forms are in [`vocabulary_design_rules.md`](vocabulary_design_rules.md) §3 and §4.

This document introduces **twenty derivational morphemes** (five suffixes and fifteen prefixes) plus the general rule that derivation precedes inflection.

---

## 1. Design Goal

- **Compactness.** Each morpheme is 1–3 letters.
- **Recognizability.** Forms are adapted from internationally familiar Latin / Romance / scientific affixes (`-or` instrument, `-ia` place, `-al` relational, `anti-` opposition).
- **Productivity.** A small inventory of derivational morphemes can produce a large vocabulary mechanically.
- **Regularity.** All derivational morphemes attach in a fixed slot, and the full word order — derivation, then plural, then case — is invariant.

---

## 2. General Rule: Morpheme Order

```
root + derivational suffix/prefix + plural + case
```

Build the lexical word first (root + derivation), **then** add plural `-en`, **then** add the case suffix. The case suffix always remains at the right edge of the noun phrase, in line with [`noun_case_system.md`](noun_case_system.md) §5.

**Worked example with `fac` + `-er`:**

| Form | Structure | Meaning |
|---|---|---|
| `facer` | fac-er | maker |
| `faceren` | fac-er-en | makers |
| `facerem` | fac-er-em | maker as object |
| `facerenem` | fac-er-en-em | makers as object |
| `facers` | fac-er-s | maker's / of the maker |
| `facerens` | fac-er-en-s | of the makers |
| `facerin` | fac-er-in | in / at the maker |
| `facerko` | fac-er-ko | with the maker |

---

## 3. Inventory

**Suffixes** (attach to the right of the root):

| Function | Affix | Example | Meaning |
|---|---|---|---|
| Person / agent | `-er` | `facer` | doer / maker |
| Tool / instrument / device | `-or` | `facor` | tool / device for making |
| Place / institution / field | `-ia` | `facia` | workshop / making-domain |
| Abstract quality | `-it` | `bonit` | goodness |
| Relational adjective | `-al` | `facal` | making-related / practical |

**Prefixes** (attach to the left of the root):

| Function | Affix | Example | Meaning |
|---|---|---|---|
| Simple opposite / non- | `no-` | `nobon` | not good / bad-ish |
| Active opposition | `anti-` | `antibon` | opposed to good |
| Removal / undoing / reversal | `de-` | `defac` | undo / unmake |
| Again / back | `re-` | `refac` | remake / do again |
| Before in time | `pre-` | `previd` | foresee / preview |
| After in time | `pos-` | `posvid` | hindsight |
| Together / co- | `ko-` | `kofac` | co-make / collaborate |
| Self- | `auto-` | `automov` | self-moving / automatic |
| Half / partly | `semi-` | `semibon` | half-good / mediocre |
| Many / multi- | `multi-` | `multifacal` | multi-functional |
| New / neo- | `neo-` | `neosistem` | new system |
| Above / excessive | `super-` | `superbon` | super-good / excellent |
| Under / insufficient | `sub-` | `subbon` | sub-par / not good enough |
| Small-scale | `mikro-` | `mikrosistem` | micro-system |
| Large-scale | `makro-` | `makrosistem` | macro-system |

---

## 4. `-er` — Person / Agent

`-er` = the person associated with the action or role expressed by the root.

| Root | Derived | Meaning |
|---|---|---|
| `fac` (to do / make) | `facer` | maker / doer |
| `vid` (to see) | `vider` | viewer / seer |
| `mov` (to move) | `mover` | mover / one who moves |
| `doc` (to teach) | `docer` | teacher |

With inflection:

| Form | Meaning |
|---|---|
| `faceren` | makers |
| `viderem` | the viewer (as direct object) |

---

## 5. `-or` — Tool / Instrument / Device

`-or` = the tool, device, mechanism, or instrument associated with the action.

| Root | Derived | Meaning |
|---|---|---|
| `fac` | `facor` | tool / device for making |
| `vid` | `vidor` | viewer device / visual instrument |
| `mov` | `movor` | motor / mover-machine |
| `sek` (to cut) | `sekor` | cutter / cutting tool |

**Critical contrast with `-er`:** `-er` is a *person*, `-or` is a *tool*.

- `facer` = person who makes
- `facor` = tool that makes

The pair is robust because `e` and `o` are well-distinguished vowels (see [`alphabet_and_phonology.md`](alphabet_and_phonology.md) §3).

**Spelling note: `or` (free word) vs `-or` (suffix).** The conjunction `or` (in [`vocabulary_design_rules.md`](vocabulary_design_rules.md) §5) is a free-standing word; the suffix `-or` is attached. Spelling resolves the form:

- `fac or mov` = "do or move" (conjunction)
- `facor` = "device for making" (suffix)

---

## 6. `-ia` — Place / Institution / Field

`-ia` = place, institution, field, or domain connected to the root.

| Root | Derived | Meaning |
|---|---|---|
| `fac` | `facia` | workshop / making-domain |
| `doc` | `docia` | school / teaching institution |
| `med` (to heal) | `media` | medical place / clinic |
| `komer` (trade) | `komeria` | market / commerce-place |

`-ia` covers both **physical places** (`facia` = workshop) and **abstract fields** (`docia` = the educational domain). Context resolves which reading applies. If a future distinction becomes useful, a dedicated root for "place" can be added; for now `-ia` carries both senses.

---

## 7. `-it` — Abstract Quality

`-it` = abstract quality, state, or property. Most commonly applied to adjectives.

| Base | Derived | Meaning |
|---|---|---|
| `bon` (good) | `bonit` | goodness |
| `gran` (big) | `granit` | size / greatness |
| `vel` (fast) | `velit` | speed / quickness |
| `klar` (clear) | `klarit` | clarity |

Examples in context:

```
bon dom              — good house
doms bonit           — the goodness of the house
```

---

## 8. `-al` — Relational Adjective

`-al` = "related to" / "belonging to" / "characterized by". Internationally recognizable from Latin / Romance / English `-al`.

| Base | Derived | Meaning |
|---|---|---|
| `fac` | `facal` | making-related / practical / productive |
| `dom` (house) | `domal` | domestic / house-related |
| `nacion` (nation) | `nacional` | national |
| `person` (person) | `personal` | personal |

`-al` should be read broadly as **"related to X"**, not narrowed to "good for X" or any specific evaluative reading. The interpretation is contextual:

```
facal = related to making / functional / productive (per context)
```

---

## 9. `no-` — Simple Opposite

`no-` (prefix) = "not, non-, un-". The neutral, descriptive opposite — what something is *not*, without implying active opposition.

| Base | Derived | Meaning |
|---|---|---|
| `bon` | `nobon` | not good / bad-ish |
| `klar` | `noklar` | unclear |
| `posib` (possible) | `noposib` | impossible |
| `vid` | `novid` | not see / blind (only if lexicalized) |

**Distinction from the sentential particle `no`** (see [`negation.md`](negation.md)). The free-standing `no` negates a verb or predicate; the prefix `no-` negates a single lexical item. Spelling distinguishes them:

- `no bon` = "not good" (free particle, sentential negation)
- `nobon` = "not-good / bad-ish" (lexical negation, attached prefix)

Sharing one form across both functions keeps the language compact; the writing system always disambiguates.

---

## 10. `anti-` — Active Opposition

`anti-` (prefix) = "against, anti-, opposing". Stronger than `no-`: it implies active opposition rather than mere absence.

| Base | Derived | Meaning |
|---|---|---|
| `milit` (war / military) | `antimilit` | anti-war / anti-military |
| `sistem` (system) | `antisistem` | anti-system |
| `relig` (religion) | `antirelig` | anti-religion |
| `bon` | `antibon` | opposed to good |

**Contrast with `no-`:**

| Form | Meaning |
|---|---|
| `nobon` | not good (descriptive — what it isn't) |
| `antibon` | opposed to good (oppositional — actively against) |

---

## 11. Additional Prefixes

The following thirteen prefixes extend the system. Each attaches to the left of the root, in the same morphological slot as `no-` and `anti-`, and combines freely with the suffixes already defined.

### 11.1 `de-` — Removal / Undoing / Reversal

`de-` (prefix) = removal, undoing, or reversal of the action expressed by the root.

| Root | Derived | Meaning |
|---|---|---|
| `fac` | `defac` | undo / unmake |
| `mov` | `demov` | remove / displace |
| `kon` (to know) | `dekon` | unlearn (if lexicalized) |

**Spelling note: `de-` (prefix) vs `de` (free preposition "from").** Spelling distinguishes them:
- `de dom` = "from the house" (free preposition)
- `defac` = "undo" (prefix, attached)

### 11.2 `re-` — Again / Back

`re-` (prefix) = repetition or reversal of position.

| Root | Derived | Meaning |
|---|---|---|
| `fac` | `refac` | remake / do again |
| `vid` | `revid` | see again / review |
| `mov` | `remov` | move again / move back |

### 11.3 `pre-` — Before

`pre-` (prefix) = before in time or position.

| Root | Derived | Meaning |
|---|---|---|
| `vid` | `previd` | foresee / preview |
| `fac` | `prefac` | pre-make / produce in advance |
| `sek` | `presek` | pre-cut |

**Phonotactic note.** `pre-` begins with the consonant cluster `pr-`, which violates the core-vocabulary preference for simple onsets (see [`vocabulary_design_rules.md`](vocabulary_design_rules.md) Rule 2). It is accepted here for international recognizability, following the same precedent as `gran` and `klar`.

### 11.4 `pos-` — After

`pos-` (prefix) = after in time or position.

| Root | Derived | Meaning |
|---|---|---|
| `vid` | `posvid` | hindsight / view-after |
| `fac` | `posfac` | post-make / produce after |

### 11.5 `ko-` — Together / Co-

`ko-` (prefix) = together / joint / co-.

| Root | Derived | Meaning |
|---|---|---|
| `fac` | `kofac` | co-make / collaborate |
| `vid` | `kovid` | view together |
| `mov` | `komov` | co-move |

**Spelling note: `ko-` (prefix) vs `-ko` (comitative case suffix).** The comitative case suffix `-ko` ("with") attaches to nouns at the right edge; the prefix `ko-` attaches to the left edge of a root. Both express "togetherness" but at different morphological positions, which is intentional parallelism:
- `domko` = "with the house" (case suffix on the noun)
- `kofac` = "co-make" (prefix on the verb root)

### 11.6 `auto-` — Self-

`auto-` (prefix) = self / acting on itself.

| Root | Derived | Meaning |
|---|---|---|
| `mov` | `automov` | self-moving / automobile |
| `fac` | `autofac` | self-making / automatic |
| `vid` | `autovid` | self-view / introspection |

### 11.7 `semi-` — Half / Partly

`semi-` (prefix) = half / partly. Most commonly applied to adjectives.

| Base | Derived | Meaning |
|---|---|---|
| `bon` | `semibon` | half-good / mediocre |
| `gran` | `semigran` | half-big / medium-sized |
| `klar` | `semiklar` | partly clear |

### 11.8 `multi-` — Many / Multi-

`multi-` (prefix) = many / multiple.

| Root | Derived | Meaning |
|---|---|---|
| `dom` | `multidom` | multi-house / complex |
| `person` | `multiperson` | multi-person |
| `facal` | `multifacal` | multi-functional |

**Note.** The free quantifier `mult` ("many", defined in [`noun_number_system.md`](noun_number_system.md) §7) is related but distinct: `mult` is a free word that precedes a noun, whereas `multi-` is a bound prefix attached to a root. The two are distinguished by attachment, exactly like `no` vs `no-` and `or` vs `-or`.

### 11.9 `neo-` — New

`neo-` (prefix) = new / recent variant of.

| Root | Derived | Meaning |
|---|---|---|
| `sistem` | `neosistem` | new system |
| `dom` | `neodom` | new house |
| `nacion` | `neonacion` | new nation |

### 11.10 `super-` — Above / Excessive

`super-` (prefix) = above, beyond, or excessively.

| Base | Derived | Meaning |
|---|---|---|
| `bon` | `superbon` | super-good / excellent |
| `vel` | `supervel` | super-fast |
| `gran` | `supergran` | super-big |

### 11.11 `sub-` — Under / Insufficient

`sub-` (prefix) = below, under, or insufficiently.

| Base | Derived | Meaning |
|---|---|---|
| `bon` | `subbon` | sub-par / not good enough |
| `gran` | `subgran` | sub-big / smaller than expected |

### 11.12 `mikro-` — Small-scale

`mikro-` (prefix) = small in scale.

| Root | Derived | Meaning |
|---|---|---|
| `sistem` | `mikrosistem` | micro-system |
| `dom` | `mikrodom` | micro-house / tiny house |

### 11.13 `makro-` — Large-scale

`makro-` (prefix) = large in scale.

| Root | Derived | Meaning |
|---|---|---|
| `sistem` | `makrosistem` | macro-system |
| `dom` | `makrodom` | macro-house / large complex |

---

## 12. The `-en` Overlap (Gerund vs Plural)

The morpheme `-en` is reused for two distinct functions:

| Attachment | Function | Result |
|---|---|---|
| **verb root** + `-en` | action noun / gerund | `moven` = "moving / movement" (verb `mov`) |
| **noun root** + `-en` | plural | `domen` = "houses" (noun `dom`) |

Because each root carries an **inherent category** (verb or noun), the same `-en` cannot mean two different things on the same word. The full rule, with its rationale, is in:

- [`verb_specification.md`](verb_specification.md) — gerund formation;
- [`noun_number_system.md`](noun_number_system.md) §3 — plural, with the explicit overlap note.

This document does not redefine the rule; it merely flags the connection between the gerund and the rest of the derivational system, since the gerund is itself a derivational process (verb → noun).

---

## 13. Worked Example: the Full Set for `fac`

| Form | Structure | Meaning |
|---|---|---|
| `fac` | root | to do / make |
| `facen` | fac + en (gerund, verb root) | doing / making (the act of) |
| `facer` | fac + er | doer / maker |
| `facor` | fac + or | tool / device for making |
| `facia` | fac + ia | workshop / making-domain |
| `facal` | fac + al | practical / making-related |
| `nofacal` | no- + fac + al | not practical |
| `antifacal` | anti- + fac + al | opposed to practical / productive function |
| `defac` | de- + fac | undo / unmake |
| `refac` | re- + fac | remake / do again |
| `prefac` | pre- + fac | pre-make / make in advance |
| `posfac` | pos- + fac | post-make / make after |
| `kofac` | ko- + fac | co-make / collaborate |
| `autofac` | auto- + fac | self-making / automatic |

The same set is in principle available for every root — though not every cell is necessarily lexicalized in actual usage. Multiple affixes can stack (e.g. `refacer` = "remaker", `autofacor` = "automatic tool").

---

## 14. Summary

**Suffixes:**

```
-er    = person / agent
-or    = tool / instrument / device
-ia    = place / institution / field
-it    = abstract quality
-al    = adjective: related to
```

**Prefixes:**

```
no-    = not / non- / un- (simple opposite)
anti-  = against / anti- (active opposition)
de-    = remove / undo / reverse
re-    = again / back / re-
pre-   = before / pre-
pos-   = after / post-
ko-    = co- / together
auto-  = self-
semi-  = half / partly
multi- = many / multi-
neo-   = new / neo-
super- = above / excessive
sub-   = under / insufficient
mikro- = small-scale
makro- = large-scale
```

General rule: **root + derivation + plural + case**. Build the lexical word first; then add plural and case as needed. The case suffix is always at the right edge; the plural is always immediately before it; derivational suffixes sit immediately after the root; derivational prefixes sit immediately before the root. Multiple prefixes and suffixes can stack in principle, in their respective slots.
