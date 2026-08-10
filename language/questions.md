# Questions

A formal specification of how questions are formed in the synthetic language. The language has a dedicated **question-word class** (all forms beginning with `k-`) and two question types: **polar** (yes/no) and **content** (wh-).

## Related documents

- The default constituent order (SVO) and the case-licensed reordering rule that licenses wh-fronting are in [`word_order.md`](word_order.md).
- The case suffixes that attach to pronominal wh-words are in [`noun_case_system.md`](noun_case_system.md).
- The negation particle `no` (which can combine with questions, e.g. `ka no vide?` = "don't you see?") is in [`negation.md`](negation.md).

This document introduces **ten new lexical items** — one polar question particle and nine content question words.

---

## 1. Design Goal

The question system is built around three priorities:

1. **A recognizable class.** Every question word begins with **`k-`**, so a listener identifies the utterance as a question immediately from the first segment.
2. **Compactness.** The polar marker is two letters (`ka`); every wh-word is exactly three letters (CVC).
3. **Regularity.** All polar questions use the same marker; all content questions use one of nine wh-words; both types use a fixed default position.

---

## 2. Inventory

| Form | Type | Meaning |
|---|---|---|
| `ka` | polar | yes/no question marker |
| `kid` | wh | what |
| `kis` | wh | who |
| `kos` | wh | where |
| `kud` | wh | from where |
| `kan` | wh | when |
| `kom` | wh | how |
| `kur` | wh | why |
| `kot` | wh | how many |
| `kal` | wh | what kind |

The wh-words fall into three sub-groups based on syntactic behavior:

| Sub-group | Members | Behavior |
|---|---|---|
| Pronominal | `kid`, `kis` | Function as noun phrases; take case suffixes (e.g. `kidem` = "what (object)"). |
| Adverbial | `kos`, `kud`, `kan`, `kom`, `kur` | Already lexicalized with their role (location, source, time, manner, reason); do not take case suffixes. |
| Modifier | `kot`, `kal` | Precede the noun, like other modifiers; the case suffix attaches to the noun. |

---

## 3. Polar (Yes/No) Questions

A yes/no question is formed by placing **`ka`** at the **start of the clause**. The rest of the sentence retains its normal SVO shape and morphology.

```
ka vide?              — do you see?
ka vide domem?        — do you see the house?
ka amik vida domem?   — does the friend see the house?
ka amik movə?         — do the friends move?  (plural inferred from -ə on the verb)
```

Combined with negation (see [`negation.md`](negation.md)):

```
ka no vide?           — don't you see?
ka no vide domem?     — don't you see the house?
```

---

## 4. Content (Wh-) Questions

A content question is formed by placing the appropriate wh-word at the **start of the clause**. The wh-word takes the form appropriate to its syntactic role:

- if it is a **pronominal** wh-word (`kid`, `kis`), it bears the case suffix matching the role it questions;
- if it is an **adverbial** wh-word (`kos`, `kud`, `kan`, `kom`, `kur`), it appears in its bare form;
- if it is a **modifier** wh-word (`kot`, `kal`), it sits before the noun it questions, with the noun bearing the case appropriate to the sentence.

### 4.1 Pronominal wh-words

```
kis vida?             — who sees?              (kis = subject, nominative)
kidem vide?           — what do you see?       (kidem = object, accusative)
kides domem?          — whose house?           (kides = "of whom"; sibilant rule
                                                gives -es after kis: kis + -es)
kidad movdə?          — to what did they move? (kidad = allative on kid)
```

### 4.2 Adverbial wh-words

These already encode their grammatical role and appear in bare form:

```
kos movə?             — where do they move?
kud movə?             — from where do they move?
kan movdi?            — when did I move?
kom faci?             — how do I make (it)?
kur facdi?            — why did I do (it)?
```

Adverbial wh-words are **invariant across tense, aspect, and person**: only the verb changes, while the wh-word keeps its bare form — compare present `kom faci?` ("how do I make it?") with past `kom facdi?` ("how did I make it?").

### 4.3 Modifier wh-words

`kot` and `kal` precede the noun, like `duo`, `bon`, or `tik`. Plural marking and case marking attach to the noun:

```
kot domen vide?       — how many houses do you see?
kot domenem vide?     — how many houses do you see? (object explicit)
kal dom vide?         — what kind of house do you see?
kal domem vide?       — what kind of house do you see? (object explicit)
```

The plural suffix `-en` is optional after `kot` (since "how many" already implies plurality), following the same rule as after numerals (see [`noun_number_system.md`](noun_number_system.md) §7): `kot dom` and `kot domen` are both valid.

---

## 5. Combining with Negation

`ka` and any wh-word may be combined with the negation particle `no` (see [`negation.md`](negation.md)). The negation particle keeps its rule — immediately before the verb — regardless of the question type:

```
ka no vide?           — don't you see?
kidem no vide?        — what don't you see?
kis no vida?          — who doesn't see?
```

---

## 6. Rationale

- The shared `k-` onset makes question status audible from the first segment, which matters most in spontaneous speech and in noisy environments.
- Choosing **clause-initial position** for both `ka` and wh-words gives the language a single, easily taught rule: *the question marker comes first.* This is the most familiar pattern across the target speaker backgrounds (English, Romance, Russian, German, Arabic, Hindi/Urdu all front question elements).
- Speakers from in-situ-wh backgrounds (Mandarin, Japanese, Korean) can still recognize the wh-word from its `k-` onset, and they can rely on the case suffixes on `kid` and `kis` to track grammatical roles even though the position is fronted.
- Compact two-letter `ka` matches the very high frequency of polar questions; three-letter CVC wh-words match the rhythm of the cardinal numerals (see [`numerals.md`](numerals.md)) and stay phonotactically simple.
- Reusing existing systems — case suffixes on `kid` / `kis`, modifier-before-noun for `kot` / `kal`, the negation particle `no` — means the question system introduces no new morphology, only new lexical items.

---

## Design choices flagged for review

The user's specification listed the ten question words and their meanings but did not fix their syntactic position. The two positional choices made in this document are design proposals:

1. **`ka` sentence-initial** (rather than sentence-final like Japanese / Mandarin / Korean question particles).
2. **Wh-words fronted to clause-initial position** (rather than in-situ like Mandarin / Japanese).

Both choices favor the largest single block of target speaker backgrounds (English, Romance, Russian, German, Arabic, Hindi/Urdu) and unify the polar and content question rules under "question marker first." If a sentence-final `ka` or in-situ wh-words are preferred instead, this document should be revised accordingly.
