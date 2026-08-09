# Population-weighted genealogical phoneme support — top 10 families

> **Status:** experimental cross-family evidence. This report does not itself freeze or remove any GlottoDelta phoneme.

## Metric

`F` is now explicitly **population-weighted at the family level**. Each family's speaker-exposure proxy weights the unweighted share of its sampled distinct languages that support a target.

This is intentional: population measures the practical cost of excluding a large group, while the unweighted within-family share keeps a single mega-language from standing in for its whole genealogy. Existing `P_attested` remains the direct demographic-language metric; `F` adds genealogical structure.

CLDR-derived exposure estimates may include L1 and L2 speakers and overlap, so the exposure totals below are not unique-person counts.

## Family weights

| Rank | Family | Exposure proxy | Normalized F weight | Sample languages | Glottolog coverage |
|---:|---|---:|---:|---:|---:|
| 1 | Indo-European | 4,967,111,343 | 57.66% | 140 | 23.9% |
| 2 | Sino-Tibetan | 1,531,886,716 | 17.78% | 97 | 18.7% |
| 3 | Afro-Asiatic | 526,958,069 | 6.12% | 104 | 27.3% |
| 4 | Austronesian | 487,578,528 | 5.66% | 109 | 8.5% |
| 5 | Atlantic-Congo | 366,087,356 | 4.25% | 406 | 28.8% |
| 6 | Dravidian | 267,507,015 | 3.11% | 32 | 39.0% |
| 7 | Turkic | 157,553,241 | 1.83% | 21 | 48.8% |
| 8 | Japonic | 121,249,490 | 1.41% | 3 | 17.6% |
| 9 | Austroasiatic | 104,273,769 | 1.21% | 40 | 25.3% |
| 10 | Tai-Kadai | 84,083,291 | 0.98% | 19 | 20.0% |

## Target comparison

| Target | P_attested | L_family | F strict | F soft | Strict excluded exposure | Families >=80% | Families <50% |
|---|---:|---:|---:|---:|---:|---:|---:|
| /m/ | 100.0% | 97.0% | 99.1% | 99.1% | 0.07B | 10/10 | 0/10 |
| /i/ | 99.7% | 98.2% | 95.6% | 95.6% | 0.38B | 9/10 | 0/10 |
| /u/ | 99.5% | 94.5% | 95.5% | 95.5% | 0.39B | 10/10 | 0/10 |
| /j/ | 98.7% | 91.8% | 92.2% | 92.2% | 0.67B | 8/10 | 0/10 |
| /k/ | 94.4% | 92.4% | 91.6% | 91.6% | 0.72B | 8/10 | 1/10 |
| /p/ | 93.3% | 87.4% | 89.7% | 89.7% | 0.89B | 8/10 | 1/10 |
| /r/ | 96.9% | 75.2% | 89.0% | 95.2% | 0.95B | 6/10 | 1/10 |
| /a/ | 98.8% | 96.5% | 88.9% | 88.9% | 0.95B | 9/10 | 1/10 |
| /s/ | 97.4% | 71.4% | 88.9% | 88.9% | 0.96B | 8/10 | 0/10 |
| /b/ | 80.1% | 64.6% | 88.2% | 98.7% | 1.02B | 6/10 | 0/10 |
| /n/ | 93.3% | 85.9% | 87.8% | 87.8% | 1.05B | 8/10 | 0/10 |
| /ɡ/ | 75.3% | 58.4% | 87.1% | 98.4% | 1.11B | 6/10 | 1/10 |
| /e/ | 78.3% | 78.1% | 86.6% | 86.6% | 1.15B | 8/10 | 1/10 |
| /l/ | 92.5% | 73.8% | 86.0% | 95.2% | 1.20B | 9/10 | 1/10 |
| /o/ | 77.7% | 74.9% | 85.5% | 85.5% | 1.25B | 7/10 | 1/10 |
| /h/ | 72.1% | 60.1% | 74.0% | 74.0% | 2.24B | 3/10 | 0/10 |
| /t/ | 86.7% | 80.3% | 71.8% | 71.8% | 2.43B | 5/10 | 1/10 |
| /w/ | 91.4% | 86.4% | 70.8% | 70.8% | 2.52B | 5/10 | 1/10 |
| /d/ | 64.6% | 55.5% | 70.5% | 79.9% | 2.54B | 3/10 | 2/10 |
| /f/ | 92.7% | 49.2% | 66.5% | 66.5% | 2.89B | 3/10 | 5/10 |
| /ʃ/ | 89.9% | 41.1% | 65.7% | 96.5% | 2.95B | 1/10 | 5/10 |
| /ŋ/ | 79.1% | 65.2% | 63.4% | 63.4% | 3.16B | 5/10 | 2/10 |
| /v/ | 63.9% | 39.3% | 59.0% | 97.6% | 3.53B | 0/10 | 5/10 |
| /z/ | 59.9% | 31.6% | 57.8% | 89.5% | 3.63B | 0/10 | 4/10 |
| /ə/ | 67.6% | 29.9% | 50.1% | 50.1% | 4.30B | 0/10 | 5/10 |

## Largest strict exclusion contributors by target

- /ə/: Indo-European 50.7% support -> 2.45B exposure-equivalent gap; Sino-Tibetan 64.9% support -> 0.54B exposure-equivalent gap; Austronesian 37.6% support -> 0.30B exposure-equivalent gap.
- /z/: Indo-European 63.6% support -> 1.81B exposure-equivalent gap; Sino-Tibetan 56.7% support -> 0.66B exposure-equivalent gap; Austronesian 11.0% support -> 0.43B exposure-equivalent gap.
- /v/: Indo-European 72.1% support -> 1.38B exposure-equivalent gap; Sino-Tibetan 29.9% support -> 1.07B exposure-equivalent gap; Austronesian 32.1% support -> 0.33B exposure-equivalent gap.
- /ŋ/: Indo-European 50.7% support -> 2.45B exposure-equivalent gap; Afro-Asiatic 47.1% support -> 0.28B exposure-equivalent gap; Sino-Tibetan 92.8% support -> 0.11B exposure-equivalent gap.
- /ʃ/: Indo-European 78.6% support -> 1.06B exposure-equivalent gap; Sino-Tibetan 52.6% support -> 0.73B exposure-equivalent gap; Austronesian 12.8% support -> 0.42B exposure-equivalent gap.
- /f/: Indo-European 77.9% support -> 1.10B exposure-equivalent gap; Sino-Tibetan 33.0% support -> 1.03B exposure-equivalent gap; Austronesian 41.3% support -> 0.29B exposure-equivalent gap.
- /d/: Indo-European 70.7% support -> 1.45B exposure-equivalent gap; Sino-Tibetan 61.9% support -> 0.58B exposure-equivalent gap; Austronesian 67.0% support -> 0.16B exposure-equivalent gap.
- /w/: Indo-European 62.9% support -> 1.84B exposure-equivalent gap; Sino-Tibetan 78.4% support -> 0.33B exposure-equivalent gap; Turkic 33.3% support -> 0.11B exposure-equivalent gap.
- /t/: Indo-European 67.1% support -> 1.63B exposure-equivalent gap; Sino-Tibetan 74.2% support -> 0.39B exposure-equivalent gap; Austronesian 78.9% support -> 0.10B exposure-equivalent gap.
- /h/: Indo-European 72.9% support -> 1.35B exposure-equivalent gap; Sino-Tibetan 82.5% support -> 0.27B exposure-equivalent gap; Austronesian 68.8% support -> 0.15B exposure-equivalent gap.
- /o/: Indo-European 85.7% support -> 0.71B exposure-equivalent gap; Afro-Asiatic 65.4% support -> 0.18B exposure-equivalent gap; Sino-Tibetan 93.8% support -> 0.09B exposure-equivalent gap.
- /l/: Indo-European 85.7% support -> 0.71B exposure-equivalent gap; Sino-Tibetan 91.8% support -> 0.13B exposure-equivalent gap; Japonic 0.0% support -> 0.12B exposure-equivalent gap.
- /e/: Indo-European 85.7% support -> 0.71B exposure-equivalent gap; Afro-Asiatic 74.0% support -> 0.14B exposure-equivalent gap; Austronesian 81.7% support -> 0.09B exposure-equivalent gap.
- /ɡ/: Indo-European 91.4% support -> 0.43B exposure-equivalent gap; Sino-Tibetan 81.4% support -> 0.28B exposure-equivalent gap; Austronesian 70.6% support -> 0.14B exposure-equivalent gap.
- /n/: Indo-European 90.0% support -> 0.50B exposure-equivalent gap; Sino-Tibetan 80.4% support -> 0.30B exposure-equivalent gap; Afro-Asiatic 89.4% support -> 0.06B exposure-equivalent gap.
- /b/: Indo-European 90.7% support -> 0.46B exposure-equivalent gap; Sino-Tibetan 82.5% support -> 0.27B exposure-equivalent gap; Austronesian 74.3% support -> 0.13B exposure-equivalent gap.
- /s/: Indo-European 88.6% support -> 0.57B exposure-equivalent gap; Sino-Tibetan 88.7% support -> 0.17B exposure-equivalent gap; Afro-Asiatic 89.4% support -> 0.06B exposure-equivalent gap.
- /a/: Indo-European 85.0% support -> 0.75B exposure-equivalent gap; Japonic 33.3% support -> 0.08B exposure-equivalent gap; Sino-Tibetan 95.9% support -> 0.06B exposure-equivalent gap.
- /r/: Sino-Tibetan 80.4% support -> 0.30B exposure-equivalent gap; Indo-European 95.0% support -> 0.25B exposure-equivalent gap; Atlantic-Congo 58.6% support -> 0.15B exposure-equivalent gap.
- /p/: Indo-European 90.0% support -> 0.50B exposure-equivalent gap; Afro-Asiatic 68.3% support -> 0.17B exposure-equivalent gap; Japonic 33.3% support -> 0.08B exposure-equivalent gap.
- /k/: Indo-European 90.0% support -> 0.50B exposure-equivalent gap; Japonic 33.3% support -> 0.08B exposure-equivalent gap; Turkic 71.4% support -> 0.05B exposure-equivalent gap.
- /j/: Sino-Tibetan 85.6% support -> 0.22B exposure-equivalent gap; Indo-European 95.7% support -> 0.21B exposure-equivalent gap; Austronesian 73.4% support -> 0.13B exposure-equivalent gap.
- /u/: Indo-European 94.3% support -> 0.28B exposure-equivalent gap; Afro-Asiatic 88.5% support -> 0.06B exposure-equivalent gap; Turkic 85.7% support -> 0.02B exposure-equivalent gap.
- /i/: Indo-European 95.0% support -> 0.25B exposure-equivalent gap; Afro-Asiatic 88.5% support -> 0.06B exposure-equivalent gap; Japonic 66.7% support -> 0.04B exposure-equivalent gap.
- /m/: Indo-European 99.3% support -> 0.04B exposure-equivalent gap; Sino-Tibetan 99.0% support -> 0.02B exposure-equivalent gap; Afro-Asiatic 97.1% support -> 0.02B exposure-equivalent gap.

## Interpretation rule

A high `P_attested` says the sound is common in heavily spoken languages. A high population-weighted `F` says that support is also broad inside the large genealogical groups. For final inventory decisions, phonemes should be preferred when both are strong; a low `F` or a large exclusion contribution from one major family is a warning even if global `P` is high.
