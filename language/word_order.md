# Word Order

A formal specification of the default constituent order of the synthetic language, and the conditions under which that order may be relaxed.

## Related documents

- The verb's final person vowel encodes the subject and makes independent subject pronouns optional (pro-drop). See [`verb_specification.md`](verb_specification.md).
- Case suffixes mark the grammatical role of each noun phrase, which is what enables word-order freedom. See [`noun_case_system.md`](noun_case_system.md).
- Optional nominal plurality with `wi` is defined in [`noun_number_system.md`](noun_number_system.md).

This document introduces **no new morphemes** — only a syntactic rule.

---

## 1. Design Goal

The language must have:

- a **single unmarked default order**, so that ordinary prose flows in a predictable way and listeners can parse short utterances without scanning for case markers;
- a **release valve**, so that when a speaker wants to foreground a constituent for emphasis, the case suffixes are enough to keep the sentence unambiguous in any order.

---

## 2. Options Considered

| Option | Example gloss | Most familiar to |
|---|---|---|
| SVO | I see house | English, Romance languages, Mandarin |
| SOV | I house see | Japanese, Korean, Hindi/Urdu, Turkish |
| Free (case-driven) | subject/object marked, order free | possible, but less simple to teach |

---

## 3. Default Order: SVO

The unmarked order is **Subject – Verb – Object**.

```
i vidi domem
= I see the house
```

With a full noun subject:

```
amik vida domem
= the friend sees the house
```

**Pro-drop.** Independent subject pronouns are optional, because the verb's final person vowel already identifies the subject (see [`verb_specification.md`](verb_specification.md)). The bare form

```
vidi domem
```

is also a complete sentence meaning "I see the house" and is the more typical phrasing in connected speech. The explicit pronoun `i` is used for contrast, emphasis, or clarity.

---

## 4. Reordering for Emphasis

Because case suffixes unambiguously identify each noun phrase's grammatical role (see [`noun_case_system.md`](noun_case_system.md)), the SVO default may be relaxed when a speaker wants to foreground a particular constituent. The most common departure is **object fronting** for topicalization:

```
domem vidi i
= the house, I see
```

Here the object `domem` is fronted, but its `-em` suffix keeps it identifiable as the object regardless of where it sits in the sentence. Other orders (OVS, OSV, etc.) are likewise legal whenever the speaker has a reason to use them; the listener relies on the case suffixes, not on position, to assign roles.

**Rule.** SVO is the default. Any other order is marked: it carries pragmatic weight (emphasis, contrast, topicalization) that the speaker is presumed to intend.

---

## 5. Rationale

- **SVO is the most broadly familiar order** among the language's target speaker backgrounds: English, every Romance language, and Mandarin all use SVO as their basic order. Choosing it as the default minimizes the parsing effort for the largest contiguous group of learners.
- **A single fixed default keeps prose consistent.** Unmarked sentences look the same everywhere, which makes the language easier to read at a glance.
- **The case system provides the release valve.** Speakers from SOV backgrounds (Japanese, Korean, Hindi/Urdu, Turkish) or from free-order traditions are not forced to abandon their habits in emphatic or contrastive sentences; they can reorder freely whenever the case suffixes carry the load.

The combination — fixed SVO default plus permitted reordering — gives the regularity of a strict-order language together with the flexibility of a case-marked one, at no extra morphological cost.


## Conditional introducer `se` (ratified 24 October 2026)

`se` is the standalone conditional conjunction **IF**. It is distinct from confirmed free `si` YES and `no` NO/NOT. `se` introduces a condition clause P in a conditional relation between P and Q; the exact placement, boundary marking and nesting rules of complex conditionals are **not yet ratified**. Candidate structures `se P, Q` and `se P, tum Q` are **illustrative proposals**, not a new approved clausal parser grammar. `tum`/ `alor` (THEN), `ergo` (THEREFORE), `nisi` (UNLESS), `sin` (ELSE IF) and `sed` (BUT) remain under consideration. `se` does not by itself establish a counterfactual verbal mood.


## Connectives: `alor`, `ma`, `ergo` (ratified 24 October 2026)

Free-standing `alor` marks **THEN**, the consequent in a conditional relation introduced by ratified `se` (IF); `ma` is the ordinary adversative conjunction **BUT**; `ergo` introduces an inferential conclusion **THEREFORE / THUS**. They are distinct from each other and from already ratified `e` (AND) and `o` (OR).

Schematic illustrations (not claims of complete parser support): `se P, alor Q` ('if P, then Q'), `P ma Q` ('P but Q'), `P, ergo Q` ('P, therefore Q'). Full clausal grammar, nesting, precedence and whether `alor` may be omitted in every construction remain to be decided separately. `sed` and `tum` were alternatives considered, **not** ratified.


## Order of causal clauses (ratified 24 October 2026)

Both `P due Q` (effect followed by its causal explanation) and `due Q, P` (fronted causal clause followed by effect) are accepted. In either order Q is the cause and P the effect. `Q, ergo P` instead presents P as an inference/conclusion. General subordinate nesting and delimiter rules are not yet implemented in the restricted Phase 1 parser; no silent acceptance of unparsed forms is implied.


## Factual concessive `etsi` (ratified 24 October 2026)

`etsi` introduces an accepted/factual concession: `etsi P, Q` ('although P, Q') and `Q etsi P` ('Q, although P') are both permitted, with P the conceded proposition and Q the contrasting outcome. Distinguish conditional `se` (IF) and adversative `ma` (BUT). The hypothetical reading 'even if P were to happen' is not automatically ratified. The restricted Phase 1 parser does not yet implement compound concessive clauses.


## Hypothetical concessive `etsise` (ratified 24 October 2026)

The invariant **single-word** compound `etsise` = `etsi` (concessive) + `se` (hypothetical condition) denotes hypothetical **EVEN IF / EVEN SHOULD**. Both `etsise P, Q` ('even if P, Q') and `Q etsise P` ('Q, even if P') are grammatical. The speaker does **not assert that P is true or false**, unlike `etsi` which presents P as factual or accepted. The consequent Q is asserted to hold even in the eventuality P, not in all imaginable circumstances. `etsise` is a specifically licensed compound, **not** evidence that arbitrary connective strings may be fused. Complex subordinate-scope parsing remains outside the current restricted parser.


## Exception and conditional exception (ratified 24 October 2026)

`ekse` is a free invariant EXCEPT/EXCLUDING operator. The fused single-word `eksese` = `ekse` + `se` introduces a conditional exception, UNLESS / EXCEPT IF. The two clause orders `eksese P, Q` ('unless P, Q') and `Q eksese P` ('Q, unless P') are both valid. Unlike simple `se no P, Q` ('if not P, Q'), `eksese` signals that P is an exception to an expectation/rule associated with Q; it does not generally entail that Q must happen whenever P is false. Full syntactic handling of the general exclusion operator and nested subordinate clauses remains future parser work. The fused compound is specifically licensed and does not make arbitrary fusion productive.

## Ratified free coordination (24 October 2026)

`e` AND and `o` OR are free conjunction words, not bound verbal aspect vowels `-e` or `-o`. Mixed-connective scope and precedence are not yet specified.
