#!/usr/bin/env python3
from hashlib import sha256
from pathlib import Path

root = Path(__file__).resolve().parents[1]
snap = root / 'legacy' / 'original-language'
manifest = snap / 'SHA256SUMS'
for line in manifest.read_text().splitlines():
    digest, name = line.split(None, 1)
    name = name.strip()
    data = (snap / name).read_bytes()
    got = sha256(data).hexdigest()
    assert got == digest, f'immutable legacy snapshot changed: {name}'
print('legacy language snapshot integrity checks passed')
