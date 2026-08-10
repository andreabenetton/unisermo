# Verb Specification

This document specifies the verb system of the language. It defines the dictionary form, the person-marking system, the tense/aspect/mode grid, the gerund, the imperative, negation, and the orthographic treatment of double consonants. Each section gives both the rules and the reasoning that motivates them.

## Core Design Goals

The verb system is built around four priorities:

1. **Compactness.** The most frequent grammatical information should use the shortest forms. Common categories — present tense, simple aspect, third person — should require little or no overt marking.
2. **Recognizability.** Lexical roots are often transformed from existing international words, so a speaker who already knows a European language has a chance of recognizing them on sight.
3. **Regularity.** Verb forms must be predictable. Once the root is known, every finite form can be derived mechanically without irregular paradigms or stem changes.
4. **Auditory clarity.** The single most important piece of grammatical information — *who is performing the action* — must always appear in the same, easily identifiable position so that the listener can parse it without backtracking.

These goals together pull the morphology toward a strictly suffixing, agglutinative shape with a fixed slot order.

## Verb Root

The dictionary form (the form listed in a lexicon) is the bare root. It also functions as the infinitive.

Examples:

| Root | Meaning |
|---|---|
| `mov` | to move |
| `fac` | to do / to make |

The root carries the lexical meaning. All finite forms are built by adding suffixes to it.

**Rationale.** Using the bare root as the infinitive removes the need for a dedicated infinitive marker (such as English *to* or Romance *-are/-ere/-ire*). This keeps the citation form maximally compact and makes morphological derivation transparent: every suffix in this document attaches directly to the bare root.

## Person Marking

Every finite verb ends in a vowel that identifies the grammatical subject. This vowel is the *person vowel*.

| Final vowel | Person | Pronoun meaning |
|---|---|---|
| `i` | 1st singular | I |
| `e` | 2nd singular | you (singular) |
| `a` | 3rd singular | he / she / it |
| `u` | 1st plural | we |
| `o` | 2nd plural | you (plural) |
| `ə` | 3rd plural | they |

Because the subject is already encoded in the final vowel, independent subject pronouns are usually unnecessary. The language is **pro-drop**: a sentence such as `movi` is a complete utterance meaning *I move*; no separate pronoun is required.

Examples with `mov` (to move) and `fac` (to do / to make):

| Form | Meaning | Form | Meaning |
|---|---|---|---|
| `movi` | I move | `faci` | I do / I make |
| `move` | you move | `face` | you do / you make |
| `mova` | he/she/it moves | `faca` | he/she/it does / makes |
| `movu` | we move | `facu` | we do / we make |
| `movo` | you (pl.) move | `faco` | you (pl.) do / make |
| `movə` | they move | `facə` | they do / they make |

**Rationale for placing the person vowel at the end.** The subject is the most frequently and most urgently parsed piece of grammatical information in a verb. By guaranteeing that the person marker is always the final segment of every finite verb, the listener can identify the subject without waiting to see how long the verb might be or scanning for an internal marker. The final-vowel rule is therefore an auditory clarity guarantee, not just a stylistic choice.

## Finite Verb Structure

Every finite verb is built from exactly three slots:

```
root + tense/aspect/mode marker + person vowel
```

The present simple has no tense/aspect marker, so it reduces to the two-slot form:

```
root + person vowel
```

Worked examples:

| Form | Decomposition | Meaning |
|---|---|---|
| `movi` | mov + Ø + i | I move |
| `faci` | fac + Ø + i | I do / I make |
| `movdi` | mov + d + i | I moved |
| `facdi` | fac + d + i | I did / I made |
| `movfi` | mov + f + i | I will move |
| `facfi` | fac + f + i | I will do / make |

**Rationale for the slot order.** A reasonable-looking alternative would be `root + person vowel + marker`. That order is rejected because it would push the person marker into the middle of the word, where its position would vary depending on how many tense/aspect/mode markers were attached. The chosen order keeps the person vowel rigorously final and keeps the tense/aspect/mode markers adjacent to the root they modify. Person is more central and more frequent than tense or aspect, so it earns the most stable, most easily identified slot — the last one.

## The 3×4 Tense / Aspect / Mode Grid

Finite verbs encode two grammatical dimensions in the marker slot:

- **Time** (rows): present, past, future.
- **Aspect / mode** (columns): simple, ongoing, completed, able / potential.

The basic marker inventory is:

- `d` — past
- `f` — future
- `n` — ongoing / progressive
- `b` — completed / perfect
- `m` — able / potential

A time marker (`d`, `f`, or none for the present) precedes an aspect/mode marker (`n`, `b`, `m`, or none for simple). The combined marker slot therefore looks like this:

| Time / Aspect | Simple | Ongoing | Completed | Able / potential |
|---|---|---|---|---|
| Present | Ø | `n` | `b` | `m` |
| Past | `d` | `dn` | `db` | `dm` |
| Future | `f` | `fn` | `fb` | `fm` |

Full conjugation of `mov` in the first person singular:

| Time / Aspect | Simple | Ongoing | Completed | Able / potential |
|---|---|---|---|---|
| Present | `movi` = I move | `movni` = I am moving | `movbi` = I have moved | `movmi` = I can move |
| Past | `movdi` = I moved | `movdni` = I was moving | `movdbi` = I had moved | `movdmi` = I could move |
| Future | `movfi` = I will move | `movfni` = I will be moving | `movfbi` = I will have moved | `movfmi` = I will be able to move |

The same grid applied to `fac`:

| Time / Aspect | Simple | Ongoing | Completed | Able / potential |
|---|---|---|---|---|
| Present | `faci` = I do | `facni` = I am doing | `facbi` = I have done | `facmi` = I can do |
| Past | `facdi` = I did | `facdni` = I was doing | `facdbi` = I had done | `facdmi` = I could do |
| Future | `facfi` = I will do | `facfni` = I will be doing | `facfbi` = I will have done | `facfmi` = I will be able to do |

**Rationale for separating time from aspect/mode.** Only three values are genuine time references: present, past, future. The other four values — simple, ongoing, completed, able/potential — describe *how* the action unfolds, not *when* it happens. Splitting these into two orthogonal dimensions yields 3 × 4 = 12 forms from only five markers, and the meaning of any combination is always the sum of its parts. This avoids inflating the system with dozens of unrelated tense labels (as natural languages often do) while still giving learners and speakers full expressive power.

## Gerund / Verbal Noun

The gerund — the verbal noun naming the action itself — is formed by adding `-en` to the root:

```
root + en
```

Examples:

| Root | Gerund | Meaning |
|---|---|---|
| `mov` | `moven` | moving / the act of moving |
| `fac` | `facen` | doing / making / the act of doing |

**Rationale.** The gerund sits outside the finite verb grid because it does not assert that someone is performing the action; it merely names the action. Because it carries no subject, it takes no person vowel, and because it is not anchored in time, it takes no tense marker. Giving it a dedicated suffix `-en` keeps it formally distinct from any cell of the 3×4 grid and prevents it from being confused with a finite form.

## Imperative

The affirmative imperative is the bare root:

| Form | Meaning |
|---|---|
| `mov!` | move! |
| `fac!` | do it! / make it! |

The negative imperative is formed by placing the general negation particle `no` immediately before the bare root (e.g. `no mov!` = "do not move!"). The full rule is in [`negation.md`](negation.md).

**Rationale.** Commands are high-frequency utterances, often spoken under time pressure, and the addressee is virtually always clear from context. Stripping the imperative down to the bare root is the most extreme application of the compactness goal: nothing is added that the situation already supplies. The negative imperative simply reuses the general negation particle rather than introducing a dedicated prohibitive form, which keeps the system regular.

## Negation

Negation is expressed analytically: the particle `no` is placed immediately before the verb, and the verb itself is not modified. The full negation rule — including its application to every tense/aspect/mode form, to imperatives, and to reordered sentences — is defined in [`negation.md`](negation.md).

## Double Consonants

When the morphology brings two identical consonants into contact across a morpheme boundary, both consonants are written.

Example with `vid` (to see):

| Form | Decomposition | Meaning |
|---|---|---|
| `vidi` | vid + Ø + i | I see |
| `viddi` | vid + d + i | I saw |

The pronunciation rule for the resulting double consonant — Italian-style gemination — and the constraint that unrelated roots must not be distinguished by consonant length are defined in [`alphabet_and_phonology.md`](alphabet_and_phonology.md). This section specifies only the morphological mechanism.

**Rationale.**

- Writing the double consonant preserves a compact spelling — no epenthetic vowel is inserted to break the cluster.
- It makes the morphology transparent: a reader can still see the root `vid` and the past marker `d` standing side by side.
- It keeps the suffix inventory uniform: `d` is always written `d`, regardless of what consonant the root ends in.

## Summary

The verb system can be summarized in a few lines:

- The bare root is the dictionary form and the infinitive (`mov`, `fac`).
- Every finite verb has the shape **root + tense/aspect/mode marker + person vowel**.
- The final vowel always marks the subject: `i`, `e`, `a`, `u`, `o`, `ə` for the six persons.
- Time is marked by `d` (past), `f` (future), or nothing (present).
- Aspect/mode is marked by `n` (ongoing), `b` (completed), `m` (able/potential), or nothing (simple).
- Time and aspect/mode combine freely into a 3×4 grid of twelve regular forms.
- The gerund / verbal noun is **root + `en`** and stands outside the finite grid.
- The imperative is the bare root; the negative imperative is `no` + bare root.
- Finite verbs are negated with the particle `no` placed before the verb.
- Identical consonants meeting across a morpheme boundary are written double and pronounced as a single long consonant.

The result is a verb system in which a single root expands mechanically into twelve finite forms across all six persons (seventy-two finite forms in total), plus a gerund and an imperative, with no irregular paradigms and a guaranteed final-vowel signal for the subject.
