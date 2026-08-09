# Glottolog 5.3 pinned research inputs

This directory contains the frozen inputs used by `scripts/analyze_family_inventory.py`.

- `tree_glottolog_newick.txt` — official Glottolog 5.3 Newick forest from the Glottolog release downloads. This is the **primary genealogy source** for top-level assignment.
- `languages.csv` — Glottolog-CLDF 5.3 LanguageTable supplied when the study was resumed. It is used only for macroarea metadata, dialect-to-language normalization, and diagnostics of non-genealogical top-level categories; it does **not** override the Newick genealogy.

Release pin:

- Glottolog: 5.3
- Git tag: `glottolog/glottolog` `v5.3`
- Tagged commit: `eb7d58221bea745a21cb7b96582118e990a295c2`
- Release date: 2026-03-02
- Re-verified as the current Glottolog release: 2026-08-09

Glottolog's download page states that the published data are created from the curated `glottolog/glottolog` GitHub repository. The primary mapping therefore follows the release Newick forest rather than treating the derived CLDF `Family_ID` column as the genealogy authority.

Source references:

- Glottolog release downloads: https://glottolog.org/meta/downloads
- Curated repository: https://github.com/glottolog/glottolog
- Release tag: https://github.com/glottolog/glottolog/releases/tag/v5.3

Pinned file SHA-256 values are recorded in generated `research/phonology/family_inventory.json`.
