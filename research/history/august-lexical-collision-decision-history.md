# 9–10 August 2026: lexical collision resolution and root-by-root international adaptation

**Reconstructed 24 October 2026.** This case documents how **compact, recognizable forms** were constrained by the need to preserve unambiguous grammar and productive morphology. Inputs: speaker-attributed indexed user and assistant messages from 9 August (original full transcript not archived), versioned immutable Git commits, legacy lexicon audits, and the first 8 August `language` specification. An indexed message summary is **not** a verbatim transcript.

## Design question and historical context

The author-confirmed 2025 founding objective was **more information in less time**. The preserved [8 August 2026 original vocabulary rules](https://github.com/andreabenetton/language/blob/bacc1a7a9aaaa18596120c6ea2812c927b33b0e3/vocabulary_design_rules.md) already made this a **multi-objective** design problem: compact and recognizable roots, phonotactic safety, predictable inflection, and fewer *fragile* minimal pairs among frequent words. The May 24 dialogue also documents the author's decision **not** to eliminate some potentially vulnerable contrasts (f/v and l/r), preferring lexical separation in high-frequency words.

The August simplification removed official letter `c` and reassigned `j` from /dʒ/ to glide /j/. This rendered numerous inherited *surface forms* and spelling-derived roots inappropriate. The [20-item original c-root audit](https://github.com/andreabenetton/unisermo/blob/16d899da5e68a2328c5018f16c12ddc8bcd4f7d3/research/lexicon/legacy_c_root_audit.md) **explicitly rejects automatic letter-by-letter conversion**; roots are evaluated individually.

### Contemporaneous messages and immutable Git anchors

| UTC (9 Aug 2026) | Actor/source | Recoverable episode | Confidence |
| --- | --- | --- | --- |
| **20:23:57** | [Git `16d899da`](https://github.com/andreabenetton/unisermo/commit/16d899da5e68a2328c5018f16c12ddc8bcd4f7d3) | Starts canonical core lexical and grammar migration; preserves research-side confirmed lexicon and diagnostics for old `c` roots. | Direct Git |
| **20:45:35** | **User original message index** | Confirms individual changes such as `cin→kin`, `doc→dots`, `fac→fak`, `dik`, `cur→kurar`; treats homonym collisions **word by word**. | Dated user conversation index, full text unexported |
| **20:47:35** | [Git `0beab462`](https://github.com/andreabenetton/unisermo/commit/0beab4622f235d43fb774cc8f9d98db69aa57701) | Separates participial/resultative `-it` from new abstract-quality `-itat`, resolves further obsolete lexical roots. | Direct Git |
| **20:51:23** | **User original message index** | Confirms finite layout `root + TAM + person vowel + optional N`; requests a comprehensive legacy-lexicon audit. | Dated user index |
| **20:57:08** | [Git `0b4856d5`](https://github.com/andreabenetton/unisermo/commit/0b4856d544345e7cebea023bd92006ebf76032de) | Commits verb layout + systematic legacy collision/orthography inventory with counts and examples. | Direct Git |
| **21:03:17** | **User original message index** | Confirms preserving `kom` as HOW, moving com-/together to `kun`, assigning `ker` to WHY and `kurar` to CARE, retaining `-ia` as /i.a/; requires clarification of the indefinite article. | Dated user index, topical match with following commit |
| **21:05:39** | [Git `d5d9ed7c`](https://github.com/andreabenetton/unisermo/commit/d5d9ed7c650e0c5ace90abf6487d15ec67e033a2) | Canonizes `kom / ker / kun / kurar`, optional `uno` as both cardinal and indefinite determiner; no separate article `un`; keeps `-ia` with **hiatus /i.a/**. | Direct Git |
| **21:05:53** | Assistant original message index | Reports those changes and notes `un` remains second-person plural, not an article. | Dated output corroborated by Git |
| **10 Aug 06:15:08** | [Git `b0bb2045`](https://github.com/andreabenetton/unisermo/commit/b0bb20456a36e6044eee85f674cb9896e4c19b2e) | Replaces `om` human/person with `uman`, aligning `umano/umane` and `umanitat`. | Direct Git |
| **10 Aug 13:44:38** | [Git `385d63a4`](https://github.com/andreabenetton/unisermo/commit/385d63a4895b2de65de62a645b7a8196bd915b14) | Derivation redesign: agent `-er→-or`; instrument `-or→-il`; fixes `dots→dok` and `sentrum→sentr`. | Direct Git |
| **10 Aug 16:24:59** | [Git `4d19263d`](https://github.com/andreabenetton/unisermo/commit/4d19263da58802bd184774b3d1463714c50979dc) | Numeral 2 globally `duo→bis`, preserving older proposals in history. | Direct Git |

**Do not compress distinct states:** `doc→dots` is a confirmed **9 August intermediate**; `dots→dok` follows on **10 August**. Similarly, `kom` was briefly at risk of collision with a com-/together lexical root and kept its grammatical meaning *only after* assigning the latter to `kun`. Historic 8 August `kur`=WHY eventually becomes `ker` so `kurar` may name care/cure.

## Three concrete collision mechanisms

**1. Competing meanings on identical short forms.** The [legacy full audit](https://github.com/andreabenetton/unisermo/blob/0b4856d544345e7cebea023bd92006ebf76032de/research/lexicon/legacy_full_lexicon_audit.md) found:

| Conflict | Competing uses | Documented treatment |
| --- | --- | --- |
| `kom` | Old HOW word versus Latin cum/com- lexical family “with/together” | Keep grammatical `kom`, adopt lexical/relational `kun` |
| `kur` | Old WHY question word versus Latin cura family “care” | WHY becomes `ker`, CARE becomes `kurar` |
| `un` | Former shortened indefinite article versus new second-person plural pronoun | No separate article `un`; reuse optional `uno` numeral/determiner |

These are **observed lexical-design collisions within the documented old/new paradigms**, not empirical counts of human mishearings.

**2. Spelling and phoneme reassignment.** The source map admits many potential realizations of former `c`: for example `fac→fak`, `cin→kin`, `nacion→nation`, `ekual→ekwal`, while `major` retains its spelling but changes from the old affricate `j=/dʒ/` to new glide pronunciation /ma.jor/. Such migrations are **not** produced by one universal `c→k` transform; retaining international recognizability sometimes requires *changing* letters or morphology rather than blindly shortening a root.

**3. Derivational ambiguity.** The old `-it` (abstract) was retired in favor of `-itat`; productive `-it` reserved for verbal participial/resultatives. Agentive and instrumental families later become distinct **`-or` (person) vs `-il` (tool)**, instead of historical `-er` vs `-or`. The `-ia` derivation is retained as two vowels /i.a/ and cannot silently become /ja/ just because `j` now has glide status. These are **semantic and structural** disambiguations, not measures of speaking speed.

The 9 August audit had **3** entries classified `collision`, **5** `confirmed_replacement`, **65** `needs_revision`, among other categories. It scanned token-like examples in legacy documents, including inflected strings, **not a corpus of independently approved lexical roots**. Its category tallies should never be presented as frequencies of actual misunderstandings.

## Evidence classes and chronology boundaries

- The **user decision** at 20:45/20:51/21:03 is recovered from speaker-attributed indexed old messages; it correlates closely in timestamp and content with primary Git objects. Without full transcripts, do **not** invent extra rejected alternatives or user quotes.
- The **directly versioned documents** prove implementation and changes, but do not prove the author undertook a listener test or that shortened roots were universally recognizable.
- The **root-by-root policy** reflects an explicit tradeoff of economy, frequency, morphological uniqueness, phonetic access and recognizability; a formal weighted numerical objective function is **not documented** for every lexical item.
- The **10 August numeral `duo→bis`** is a particularly clear example of a later choice that overrides an earlier attested, recognizable form. The Git commit verifies the change, not the exact conversation rationale; do not infer it from similarity to any single natural-language form.
- At the time the project was still known under working names; call it the **language later named Unisermo**, without anachronistically placing the name in original messages.

## Implication for the eventual methodology paper

Unisermo was not simply generated by selecting the shortest strings from an unconstrained artificial vocabulary. The surviving artifacts show **candidate roots adapted from cross-language/Latin patterns, morphological constraints, audibility/collision checks and explicit human selections**. The first six-vowel design, the later global sound-system revision and repeated root repairs establish **iterative constraint satisfaction**, although any quantitative claim that the resulting words optimize real-world communicative efficiency remains to be tested. Pair this case study with [10 August TAM phonotactics](august-tam-phonotactics-decision-history.md) and [founding objective](founding-objective-and-efficiency-measures.md).
