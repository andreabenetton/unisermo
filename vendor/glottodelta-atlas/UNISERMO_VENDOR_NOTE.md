# Historical GlottoDelta research snapshot (read-only)

This directory contains the **older** IPA atlas snapshot recovered with the
Unisermo repository. These are not the latest official GlottoDelta files.
The authoritative atlas is independently maintained at:
https://github.com/andreabenetton/glottodelta

All original snapshot assets, scripts, package metadata and historical docs
remain intact, including their original name and branding. This added note is
Unisermo-specific and not part of the original atlas. SHA256s in
`docs/ORIGINAL_FILES.sha256` record the pre-migration paths, resolved relative
to this directory except legacy/original-language entries (which remain at the
Unisermo repository root). See `tests/test_unisermo_identity.py`.

Use the atlas's own historical scripts from this directory only; never treat
the snapshot as a production deployment or push it to the official remote.
