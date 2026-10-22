#!/usr/bin/env python3
"""Audit token-like legacy Unisermo forms against the current alphabet.

Usage: python scripts/audit_legacy_lexicon.py PATH_TO_LEGACY_LANGUAGE_DIR
Prints a compact JSON summary. The committed detailed audit was generated from
language(1).zip and retained under research/lexicon/.
"""
from pathlib import Path
import sys, re, json
from collections import Counter

FORBIDDEN=set('chqxyə')

def audit(root: Path):
    occ={}
    for fp in root.glob('*.md'):
        if fp.name in {'alphabet_and_phonology.md','CLAUDE.md','README.md'}:
            continue
        txt=fp.read_text(encoding='utf-8')
        for m in re.finditer(r'`([^`\n]+)`',txt):
            span=m.group(1).lower().strip()
            if '.md' in span or '_' in span or '/' in span or '->' in span or '=' in span:
                continue
            for tok in re.findall(r'[a-zə]+(?:-[a-zə]+)?',span):
                occ.setdefault(tok,set()).add(fp.name)
    status=[]
    for form in occ:
        if 'ə' in form: s='obsolete_morphology'
        elif set(form)&FORBIDDEN or 'sh' in form: s='needs_revision'
        elif 'j' in form and form!='major': s='review_pronunciation'
        elif re.search(r'[aeiou]{2}',form): s='valid_check_hiatus'
        else: s='valid_orthography'
        status.append(s)
    return {'forms':len(occ),'summary':dict(Counter(status))}

if __name__=='__main__':
    if len(sys.argv)!=2:
        raise SystemExit('usage: audit_legacy_lexicon.py PATH_TO_LEGACY_LANGUAGE_DIR')
    print(json.dumps(audit(Path(sys.argv[1])),indent=2,sort_keys=True))
