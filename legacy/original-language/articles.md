# Articles

A formal specification of how (in)definiteness is handled in the synthetic language. The language has **no obligatory articles**; precision is added only when context demands it, via two optional determiner words.

## Related documents

- The bare noun is number-neutral and unmarked for definiteness. See [`noun_number_system.md`](noun_number_system.md).
- The relationship between the determiner `un` and the numeral `uno` is referenced from [`numerals.md`](numerals.md).
- Determiners precede the noun, in line with the modifier–head order used throughout the grammar (see [`noun_case_system.md`](noun_case_system.md) §5 and [`word_order.md`](word_order.md)).

This document introduces **one optional determiner**: the use of the existing numeral `uno` (one / a) as an indefinite-singular determiner. The three demonstratives `tik` (this) / `tes` (that near you) / `tan` (that, far) are documented separately in [`demonstratives.md`](demonstratives.md).

---

## 1. Design Goal

The article system is minimal:

1. **No obligatory articles.** Many target speaker backgrounds — Russian, Mandarin, Japanese, Korean, Indonesian, Bengali, Tamil, Telugu, Vietnamese — function without articles, and learners from those traditions should not be forced to insert article-words they would never produce in their native language.
2. **Optional precision.** When context fails to disambiguate, the speaker may add `uno` (one / a) for indefinite singularity, or one of the demonstratives `tik` / `tes` / `tan` (see [`demonstratives.md`](demonstratives.md)) for deixis.
3. **Compactness.** All optional determiners are short (2–3 letters) and used only when needed.

---

## 2. Options Considered

| Choice | Effect |
|---|---|
| No articles | Simpler. Matches Russian / Mandarin / Japanese style. |
| Definite article only | Distinguishes "house" from "the house". |
| Definite + indefinite | More precise; more complex. |

---

## 3. The Choice: No Obligatory Articles

The bare noun is **unmarked for definiteness**. Therefore:

```
dom
```

can mean **"house"**, **"a house"**, or **"the house"**, depending on context. The listener resolves the reading from discourse, prior reference, and surrounding information.

This is consistent with the bare noun being number-neutral by default (see [`noun_number_system.md`](noun_number_system.md)): the language leaves both number and definiteness implicit unless the speaker chooses to mark them.

---

## 4. The Indefinite Determiner `uno`

When indefinite-singular precision is required, the language reuses the cardinal numeral `uno` directly as a determiner, placed before the noun in line with the modifier–head order used throughout the grammar.

| Form | Meaning | Example | Gloss |
|---|---|---|---|
| `uno` | one / a | `uno dom` | one house / a house |

The determiner is **optional**: the bare `dom` remains a valid form for "house / a house / the house" when context is sufficient.

For deictic precision (this / that), see the three demonstratives `tik` / `tes` / `tan` in [`demonstratives.md`](demonstratives.md).

### 4.1 `uno` as both numeral and indefinite determiner

The form `uno` serves two roles without modification:

- as a **cardinal numeral** (= 1), used in counting and in compound numerals such as `dek uno` (11) — see [`numerals.md`](numerals.md);
- as an **indefinite-singular determiner** before a noun: `uno dom` = "a house" / "one house".

No separate apocopated form is introduced. The two uses are distinguished by context — whether `uno` precedes a noun phrase (determiner) or stands in a numeral expression (cardinal).

---

## 5. Rationale

- Many of the language's target speaker backgrounds lack obligatory articles entirely. Imposing them would add a foreign grammatical burden without expanding the language's expressive range.
- Speakers from article-using backgrounds (English, Romance, German) can still mark indefiniteness with `uno` (this document), or deixis with `tik` / `tes` / `tan` (see [`demonstratives.md`](demonstratives.md)), when they wish. No construction in the language *requires* them to do so.
- Reusing the numeral `uno` directly as the indefinite-singular determiner matches the cross-linguistic pattern in which the word for "one" doubles as the indefinite article (French *un*, Italian *uno / un*, Spanish *uno / un*, German *ein*). Keeping the full form rather than introducing an apocopated variant avoids adding a separate root for a near-identical meaning.
