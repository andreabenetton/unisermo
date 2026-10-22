# Frozen GlottoDelta atlas — research source

This repository includes an older local copy of the **GlottoDelta** IPA atlas
as a research input for **Unisermo** phonology studies. This atlas copy was
contained in the Unisermo archive dated 10 August 2026 and should not be
regarded as the currently maintained atlas.

**Authoritative atlas:** https://github.com/andreabenetton/glottodelta

The archived files retained for research are organized within
`vendor/glottodelta-atlas/`: its original `baseline/`, `public/`, `data/`,
`scripts/`, `package.json`, `docs/`, and generated data report. Atlas datasets and
browser app branding retain the original **GlottoDelta** name, including the
`glottodelta.com` URLs found in the frozen site.

All archived original file bytes are verified using
`vendor/glottodelta-atlas/docs/ORIGINAL_FILES.sha256` (the legacy language
sources listed in that historical manifest remain under `legacy/`).

The snapshot must not be updated automatically from a remote, nor pushed back
to the official GlottoDelta repository. The Unisermo repository has no Git
remote configured. The atlas README and contributor guidance were moved from
the root to `vendor/glottodelta-atlas/docs/` so that the root documents can describe
Unisermo without misrepresenting this offline reference copy.

Language-specific research dataset namespaces use `unisermo/…@1` from the
rename onward; atlas-produced dataset namespaces remain `glottodelta/…@1`.
The content of the phonetic atlas was not edited during the language rename.
