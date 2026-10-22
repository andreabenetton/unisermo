#!/usr/bin/env python3
"""Regression check: distinguish Unisermo from the frozen GlottoDelta atlas."""
from pathlib import Path
from hashlib import sha256
import json

ROOT = Path(__file__).resolve().parents[1]

ATLAS = ROOT / 'vendor' / 'glottodelta-atlas'

def resolve_snapshot_file(relative: str) -> Path:
    # The legacy language files remain in place; all original atlas files moved without content edits.
    return ROOT / relative if relative.startswith('legacy/') else ATLAS / relative


def test_unisermo_branding_and_schemas() -> None:
    assert '# Unisermo' in (ROOT / 'README.md').read_text(encoding='utf-8')
    assert '# Unisermo' in (ROOT / 'CLAUDE.md').read_text(encoding='utf-8')
    assert '# Unisermo' in (ROOT / 'language' / 'README.md').read_text(encoding='utf-8')
    for relative in ('research/grammar/confirmed_decisions.json',
                     'research/phonology/confirmed_decisions.json',
                     'research/lexicon/confirmed_lexicon.json'):
        value = json.loads((ROOT / relative).read_text(encoding='utf-8'))
        assert value['schema'].startswith('unisermo/'), relative
    for file in (ROOT / 'language').glob('*.md'):
        if file.name == 'MIGRATION_HISTORY.md':
            continue  # History notes may document the former name.
        assert 'GlottoDelta' not in file.read_text(encoding='utf-8'), file


def test_glottodelta_snapshot_unmodified() -> None:
    manifest = ROOT / 'vendor' / 'glottodelta-atlas' / 'docs' / 'ORIGINAL_FILES.sha256'
    for line in manifest.read_text(encoding='utf-8').splitlines():
        digest, path = line.split('  ', 1)
        assert sha256(resolve_snapshot_file(path).read_bytes()).hexdigest() == digest, path
    assert 'Glottodelta' in (ROOT / 'vendor' / 'glottodelta-atlas' / 'docs' / 'README.md').read_text(encoding='utf-8')
    assert 'glottodelta.com' in (ROOT / 'vendor' / 'glottodelta-atlas' / 'public' / 'sitemap.xml').read_text(encoding='utf-8')

if __name__ == '__main__':
    test_unisermo_branding_and_schemas()
    test_glottodelta_snapshot_unmodified()
    print('Unisermo identity and GlottoDelta snapshot checks passed')
