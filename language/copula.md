# Copula and Zero-Copula

A formal specification of how the language handles the verb "to be": its omission in the present simple, its full conjugation as the regular verb `es`, and its use for existence, past, future, aspect, modality, and emphasis.

## Related documents

- The verb morphology (root + tense/aspect/mode marker + person vowel) that `es` follows is defined in [`verb_specification.md`](verb_specification.md).
- The personal possessive `es` (genitive of the 2nd-person-singular pronoun `e`) shares its written form with the bare copula root — see [`noun_case_system.md`](noun_case_system.md) §6.2.
- The free-form genitive preposition `es` ("of") is in [`vocabulary_design_rules.md`](vocabulary_design_rules.md) §5; these three uses of `es` are discussed together in §13 below.
- Negation follows the usual rule (`no` immediately before the verb); see [`negation.md`](negation.md).
- Question formation uses `ka` for polar questions and `k-` wh-words for content questions; see [`questions.md`](questions.md).
- The plural suffix `-en` and the cases in which subject number must be made explicit are in [`noun_number_system.md`](noun_number_system.md).
- The locative case `-in` is in [`noun_case_system.md`](noun_case_system.md).

This document introduces **one new verb root**, `es`, and the rule that allows its omission in the present simple.

---

## 1. Design Goal

The copula system must:

- Be **compact** in the present simple, where copula clauses are very high-frequency;
- Still express **tense, aspect, modality, and existence** when needed;
- Cover the multiple semantic functions of "to be" with a **single regular verb root**, consistent with the language's preference for regularity.

The solution: a regular verb root `es` whose present-tense forms are normally omitted.

---

## 2. The Functions of "to be"

In many languages, "to be" covers several distinct constructions:

| Function | Example (English) | Construction type |
|---|---|---|
| Quality | the house is good | adjectival predicate |
| Identity | the house is a building | nominal predicate |
| Location | the house is in the city | locative predicate |
| Existence | there is a house | existential |
| Past tense | the house was good | past copula |
| Future tense | the house will be good | future copula |

This language simplifies as follows:

- In the **present simple**, quality / identity / location predicates take **no copula**.
- For **past, future, aspect, modality, or existence**, the copula verb `es` is used.

---

## 3. The Copula Root: `es`

The verb root for "to be / exist" is **`es`**. It conjugates with the regular verb morphology (see [`verb_specification.md`](verb_specification.md)): **root + tense/aspect/mode marker + person vowel**.

Like every finite verb, its final vowel must agree with the subject. A form such as `*dom esdi bon` would mean "the house was-1sg good" — ill-formed because of the person mismatch. The correct form is `dom esda bon` ("the house was good") with 3sg `-a`.

---

## 4. Full Paradigm

The simple-aspect cells of the 3×4 verb grid for `es` are:

### Present (`es` + Ø + person)

| Form | Meaning |
|---|---|
| `esi` | I am |
| `ese` | you are |
| `esa` | he / she / it is |
| `esu` | we are |
| `eso` | you (pl.) are |
| `esə` | they are |

### Past (`es` + `d` + person)

| Form | Meaning |
|---|---|
| `esdi` | I was |
| `esde` | you were |
| `esda` | he / she / it was |
| `esdu` | we were |
| `esdo` | you (pl.) were |
| `esdə` | they were |

### Future (`es` + `f` + person)

| Form | Meaning |
|---|---|
| `esfi` | I will be |
| `esfe` | you will be |
| `esfa` | he / she / it will be |
| `esfu` | we will be |
| `esfo` | you (pl.) will be |
| `esfə` | they will be |

The remaining cells of the 3×4 grid — ongoing (`n`), completed (`b`), and able/potential (`m`), combined with each tense — follow the standard pattern: `esmi` = "I can be", `esfbi` = "I will have been", `esdnə` = "they were being", and so on (see [`verb_specification.md`](verb_specification.md) for the full grid).

---

## 5. Rule: Present Simple Zero Copula

In present-simple clauses whose predicate is an adjective, a noun, or a locative phrase, the copula is **omitted**:

```
dom bon              — the house is good        (adjectival predicate)
amik doktor          — the friend is a doctor   (nominal predicate)
dom in urb           — the house is in the city (locative predicate, analytic)
dom urbin            — the house is in the city (locative predicate, compact)
```

This is the default and preferred form in ordinary speech.

---

## 6. Explicit Present Copula for Emphasis

The copula may be inserted explicitly when the speaker wants emphasis, contrast, or clarity:

```
dom esa bon          — the house is good / the house really is good
amik esa doktor      — the friend is a doctor
```

Both forms are grammatical; only the pragmatic flavor differs.

---

## 7. Past and Future: Copula Required

Past and future copula meanings cannot be conveyed by zero-copula sentences, because there is no other element in the clause that can carry tense information. The copula verb must therefore appear:

| Form | Meaning |
|---|---|
| `dom bon` | the house is good |
| `dom esda bon` | the house was good |
| `dom esfa bon` | the house will be good |
| `domen esdə bon` | the houses were good |
| `domen esfə bon` | the houses will be good |

The same applies to any aspect or modality marker (ongoing, completed, able/potential): the copula is required because the marker has to attach to a verb.

---

## 8. Subject Number with Zero Copula

In normal verbal clauses, the subject's number is signaled by the person vowel on the verb (`-a` 3sg vs `-ə` 3pl, etc. — see [`noun_number_system.md`](noun_number_system.md)). In a zero-copula clause, no verb is present, so the number signal is missing:

```
dom bon              — the house is good / the houses are good (ambiguous)
```

If the plural reading must be made explicit, the language provides two options.

**Option A — Mark the plural on the noun:**

```
domen bon            — the houses are good
```

**Option B — Use the explicit copula:**

```
dom esə bon          — the houses are good
domen esə bon        — the houses are good (both noun and copula marked)
```

**Rule.** In zero-copula present sentences, subject number may remain implicit. If plurality must be explicit, use `-en`, the explicit copula, or both.

---

## 9. Negation

Negation follows the usual rule from [`negation.md`](negation.md): the particle `no` sits immediately before the verb. In a zero-copula clause, since there is no verb, `no` sits immediately before the predicate.

**Zero-copula negation:**

```
dom no bon           — the house is not good
amik no doktor       — the friend is not a doctor
```

**Tensed copula negation:**

```
dom no esa bon       — the house is not good (with explicit present)
dom no esda bon      — the house was not good
dom no esfa bon      — the house will not be good
```

**Rule.**

- Present zero-copula: **subject + `no` + predicate**.
- Tensed copula: **subject + `no` + es-form + predicate**.

---

## 10. Questions

Question formation follows [`questions.md`](questions.md), extended naturally to zero-copula clauses (which are questioned without any copula at all).

**Polar (yes/no) questions** — `ka` at the start of the clause:

```
ka dom bon?          — is the house good?
ka dom esda bon?     — was the house good?
ka dom esfa bon?     — will the house be good?
```

**Content (wh-) questions** — wh-word fronted to the start:

```
kid dom?             — what is the house?
kos dom?             — where is the house?
kos esa dom?         — where is the house? (explicit copula, more emphatic)
```

For "where is the house?", the zero-copula form `kos dom?` is preferred for compactness; the explicit `kos esa dom?` is available when the copula needs to be heard.

---

## 11. Existential: Always Use `es`

For "there is / there are" meanings, the copula is **always used** (it is the only verbal element in the clause):

```
esa dom              — there is a house
esə dom              — there are houses
esda dom             — there was a house
esdə dom             — there were houses
esfa dom             — there will be a house
esfə dom             — there will be houses
```

Here `es` is not a zero-omittable copula but a genuine existential verb. No separate word for "there is" is introduced; one root covers both the copular and the existential functions.

---

## 12. Locative Predicates

Locative predicates follow the same pattern as adjectival and nominal predicates.

**Present (zero-copula preferred):**

```
dom urbin            — the house is in the city
dom esa urbin        — the house is in the city (explicit emphasis)
```

**Past and future (copula required):**

```
dom esda urbin       — the house was in the city
dom esfa urbin       — the house will be in the city
```

---

## 13. The Three Uses of `es`

The written form `es` has three distinct grammatical roles in the language:

| Use | Role | Defined in |
|---|---|---|
| Copula root | "to be / exist"; bare `es` and conjugated forms (`esi`, `esda`, …) | this document |
| Personal possessive | "your (sg.) / of you"; from `e` (you sg.) + genitive `-s` | [`noun_case_system.md`](noun_case_system.md) §6.2 |
| Free-form genitive preposition | "of" (analytic alternative to the suffix `-s`) | [`vocabulary_design_rules.md`](vocabulary_design_rules.md) §5 |

**Disambiguation.**

- The **conjugated forms** (`esi`, `ese`, `esa`, `esu`, `eso`, `esə`, `esdi`, …, `esfi`, …) are unambiguous: only the copula has them.
- The **bare form `es`** is potentially ambiguous, but in practice context resolves it:
  - `es dom` is "your house" (possessive) or "of the house" (free preposition); a bare existential reading is implausible because the existential uses a conjugated form (`esa dom`).
  - `es!` is the imperative "be! / exist!".
  - `esen` is the gerund "being / existence".

For pedagogical writing, the possessive may be hyphenated as `e-s dom` to make the morphology explicit, but the standard written form is `es dom`.

The ambiguity is accepted: `es` is too short, useful, and recognizable to displace, and the contexts in which the three uses overlap are easily resolved.

---

## 14. Summary Rules

1. **Present simple copula is normally omitted.**
   `dom bon` = the house is good.
2. **Explicit present copula is allowed for emphasis or clarity.**
   `dom esa bon` = the house is good / really is good.
3. **Past, future, aspect, and modality require the copula.**
   `dom esda bon` = the house was good.
   `dom esfa bon` = the house will be good.
4. **Existential meaning always uses `es`.**
   `esa dom` = there is a house.
   `esə dom` = there are houses.
5. **In zero-copula sentences, plural subject marking is optional.**
   `dom bon` = the house is good / the houses are good.
   `domen bon` = the houses are good.
6. **If plurality must be explicit, use `-en` or the explicit copula.**
   `domen bon` = the houses are good.
   `dom esə bon` = the houses are good.

This combination keeps the language compact in the most frequent construction (present-tense identity / quality / location statements) while preserving full expressive power for tense, aspect, modality, and existence.
