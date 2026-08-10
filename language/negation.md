# Negation

A formal specification of the negation system of the synthetic language. Negation is expressed **analytically** — by a separate particle `no` placed immediately before the verb — rather than morphologically through an affix on the verb itself.

## Related documents

- The verb root, person vowels, and tense/aspect/mode markers that `no` precedes are defined in [`verb_specification.md`](verb_specification.md).
- The default constituent order (SVO) into which the negated verb fits, and the rules for pro-drop and reordering, are in [`word_order.md`](word_order.md).

This document introduces **no new morphemes** — only the rule that fixes the position of the existing particle `no`.

---

## 1. Design Goal

The negation rule must be:

- **Compact.** A single short particle handles every kind of negation.
- **Regular.** The same form `no` and the same position cover finite verbs, imperatives, and every tense/aspect/mode combination.
- **Unambiguous.** The particle's position is fixed, so a listener always knows what is being negated.

---

## 2. The Rule: `no` Immediately Before the Verb

Negation is expressed by placing the particle **`no`** immediately before the verb that is being negated. The verb itself is not modified.

```
no movi          — I do not move
no vidi domem    — I do not see the house
```

The rule applies to every tense/aspect/mode form (see the 3×4 grid in [`verb_specification.md`](verb_specification.md)):

| Affirmative | Negated | Meaning |
|---|---|---|
| `movi` | `no movi` | I do not move |
| `movdi` | `no movdi` | I did not move |
| `movfi` | `no movfi` | I will not move |
| `faci` | `no faci` | I do not do |
| `facbi` | `no facbi` | I have not done |

In an SVO sentence with a full object, `no` still sits immediately before the verb; the object's default post-verbal position is unchanged:

```
no vidi domem    — I do not see the house
```

---

## 3. Negation of the Imperative

The negative imperative is formed by the same rule: `no` is placed immediately before the bare verb root.

| Form | Meaning |
|---|---|
| `no mov!` | do not move! |
| `no fac!` | do not do it! / do not make it! |

There is no dedicated prohibitive form — the same particle `no` is reused for both finite and imperative negation, keeping the system uniform.

---

## 4. Interaction with Pro-Drop and Reordering

**Pro-drop.** Subject pronouns are optional (the verb's final vowel already encodes the subject — see [`verb_specification.md`](verb_specification.md)). `no` always sits with the verb regardless of whether the subject pronoun is present:

```
no movi          — I do not move (pro-drop)
i no movi        — I do not move (explicit subject pronoun)
```

**Reordering for emphasis.** When the sentence is reordered for emphasis (see [`word_order.md`](word_order.md) §4), `no` continues to attach to the verb wherever the verb sits:

```
domem no vidi    — the house, I do not see
```

The rule is therefore *positional relative to the verb*, not positional relative to the sentence as a whole.

---

## 5. Rationale

- An analytic particle is simpler than a verbal affix: it adds no new slot to the verb morphology, no new combinatorial possibilities, and no irregular interactions with the tense/aspect/mode markers.
- A single particle covers all polarities — finite, imperative, with or without an object, with or without an explicit subject — so the learner internalizes one rule rather than several.
- Placing `no` immediately before the verb keeps the scope of negation unambiguous: the negated constituent is always the verb that follows, never some other element of the sentence.
