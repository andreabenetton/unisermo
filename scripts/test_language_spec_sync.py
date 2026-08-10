#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
lang = root / 'language'

checks = {
    'alphabet_and_phonology.md': ['21 official written units', '`j` represents the glide **/j/**', '`w` represents the glide **/w/**'],
    'verb_specification.md': ['root + TAM + person vowel + optional N', '`in`', '`un`', '`an`'],
    'noun_number_system.md': ['plural particle `wi`', 'former optional nominal plural suffix `-en` is obsolete'],
    'articles.md': ['cardinal numeral\n`uno`', 'no separate apocopated article `un`'],
    'questions.md': ['`kom` | wh | how', '`ker` | wh | why'],
    'comparison.md': ['`ekwal`', '/ma.jor/', '/e.kwal/'],
    'derivation.md': ['`-ia` remains canonical and is pronounced **/i.a/**', '`-it`', '`-itat`'],
}
for fn, needles in checks.items():
    text=(lang/fn).read_text()
    for needle in needles:
        assert needle in text, f'{fn}: missing {needle!r}'

# No active specification may use phonemic schwa as a live form.
for p in lang.glob('*.md'):
    if p.name == 'MIGRATION_HISTORY.md':
        continue
    text=p.read_text()
    # Historical discussion may name the word "schwa", but the character itself
    # is only tolerated in explicit removed-legacy examples in verb_specification.
    if p.name != 'verb_specification.md':
        assert 'ə' not in text, f'{p.name}: contains schwa character'

# Core retired spellings must not remain as current lexical examples.
for fn in ['questions.md','comparison.md','copula.md','derivation.md','numerals.md']:
    text=(lang/fn).read_text()
    for old in ['`fac`','`doc`','`nacion`','`cin`','`ekual`']:
        assert old not in text, f'{fn}: retired form {old}'

print('language specification sync checks passed')
