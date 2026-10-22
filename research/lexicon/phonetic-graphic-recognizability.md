# Phonetic versus graphic recognizability: initial root review

Status: research observations; no change to canonical Unisermo vocabulary. Owner discussion: 2026-10-22. Related: LDR-0008.

## sentr / kentr

Retain `sentr`. Evaluate auditory recognizability independently of written similarity. For English *center* /ˈsɛntər/ and French *centre* /sɑ̃tʁ/, the initial consonant corresponds to Unisermo `s`; the alternate `kentr` does not preserve those modern pronunciations. Other descendant forms and the role of phoneme realization must be evaluated per language; the available examples alone are not population-weighted evidence.

For candidates, measure separately:
- R_sound: expected recognizability when spoken, using the standard Unisermo pronunciation.
- R_written: expected recognizability when read, given known scripts and spellings.
- International coverage: contemporary language population and genealogical dispersion; do not count etymological origin as comprehension.

An experimental combination can be written R = lambda*R_sound + (1-lambda)*R_written, but lambda and both measurements remain **unset**.

## kurar / kur

Retain `kurar` pending new evidence. `kur` would be shorter, but shortening must be motivated by usage frequency and validated against current function words, derived and inflected forms, and admitted accent mergers. Historical conflicts motivated earlier choices; do not assume those conflicts remain identical after the updated interrogative `ker`.

## dik

Retain `dik`: compact, productive in regular derivations and expressing a common communicative action. Still measure actual frequency and tokenizer cost rather than claiming quantitative advantage.

## Next experiment

Collect contemporary written and spoken frequency, phonological and visual cognate matches across target languages, and full-paradigm collision results. Use Kaikki's Latin data as lexicographic input, not evidence of recognition. No language rule is changed by this review.

## Inventory-first comparison: excluded source phonemes

Candidate selection MUST first map source-language pronunciations to **canonical Unisermo phoneme sequences**. Source spelling and source phonemes are evidence, never additional Unisermo units. In particular Italian `ce` often represents /tʃe/, but /tʃ/ is **not** an independent Unisermo phoneme. The genuine simple-root choice for this family is `se` (/se/) versus `ke` (/ke/), not Italian-style `ce`. A transparent `tj` /t+j/ sequence is theoretically permitted and may surface as [tʃ], but does not grant independent status to /tʃ/; it must be assessed explicitly and is not an implicit default spelling.

Apply the same principle across the entire source-language inventory. Current excluded independent phonemes include /h/, /ʃ/, /ŋ/, /ɲ/, /ə/ and /ts/, /tʃ/, /dʒ/ as unitary affricates. Some sounds may arise as licensed coalescent or accent realizations of `sj`, `gn`, `ts`, `tj`, `dj`; these are underlying sequences, not extra phonemes. Never create phonemic distinctions on the basis of such surface realizations.

For each modern-language comparator store separately:
1. original script and spelling;
2. attested source pronunciation (IPA), variety and source;
3. candidate Unisermo form and its **canonical** phoneme sequence;
4. explicitly licensed surface variants, if relevant;
5. sound similarity after adaptation and independent visual spelling similarity;
6. phonotactic validity and collision status, including allowed accent mergers.

Compare only candidate forms that pass the inventory gate, and do not rank invalid spellings or treat a source phoneme absent from Unisermo as available. This is a methodological clarification of existing canonical phonology, not a change to it.
