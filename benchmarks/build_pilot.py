"""Build a reproducible *draft* parallel corpus, tested against the reference grammar.

English labels are authored candidate translations, NOT professionally validated.
No claim of semantic equivalence is implied until independent bilingual review.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from formalization.core import Unisermo

OUT = ROOT / 'benchmarks/corpus/pilot.jsonl'
LANG = Unisermo()
PERSONS = { (1, 'singular'): 'I', (2, 'singular'): 'you', (3, 'singular'): 'they (one person)',
            (1, 'plural'): 'we', (2, 'plural'): 'you (plural)', (3, 'plural'): 'they' }

# The corpus deliberately contains repeated inflections: it is only a technical
# pilot, not representative language-model evaluation material.
VERB_CASES = [
    ('dik', 'say', 'said', 'will say', 'am saying', 'was saying', 'have said', 'had said', 'will have said'),
    ('mov', 'move', 'moved', 'will move', 'am moving', 'was moving', 'have moved', 'had moved', 'will have moved'),
]
rows=[]

def add(unisermo: str, english: str, feature: dict, group: str, status: str, reference: str) -> None:
    # fail closed: every sentence must have exactly the intended structure
    actual = LANG.parse_sentence(unisermo)
    pred = actual['predicate']
    for key, val in feature.items():
        if key in ('interrogative','negative'):
            if actual[key] != val: raise ValueError((unisermo,key,val,actual[key]))
        elif key == 'object_lemma':
            if actual['object'] is None or actual['object']['lemma'] != val: raise ValueError(unisermo)
        elif pred.get(key) != val:
            raise ValueError((unisermo,key,val,pred.get(key)))
    rows.append({'id': f'P{len(rows)+1:03d}', 'unisermo':unisermo, 'english':english,
                 'grammatical_intent':feature, 'group':group, 'review_status':'draft_parser_verified',
                 'attestation':status, 'source':reference, 'split':'holdout' if len(rows)%5==4 else 'development'})

for root, base, past, future, progressive, past_prog, perfect, past_perfect, future_perfect in VERB_CASES:
    # Avoid free-standing gender assumptions; English subject is explicit in full sentences.
    for person, number, subject in [(1,'singular','I'),(2,'singular','You'),(1,'plural','We'),(3,'plural','They')]:
        for tense, aspect, pred in [
            ('present','simple', base if subject != 'They' else base),
            ('past','simple',past),
            ('future','simple',future),
            ('present','progressive',progressive),
            ('past','progressive',past_prog),
            ('present','perfect',perfect),
            ('past','perfect',past_perfect),
            ('future','perfect',future_perfect),
        ]:
            form=LANG.generate_verb(root,tense,aspect,person,number)
            # English auxiliaries differ by subject: do not fabricate a verbatim translation.
            if aspect != 'simple' or tense != 'present':
                if subject == 'I': phrase=pred.replace('am ','am ').replace('have ','have ')
                elif subject == 'You' or subject in ('We','They'):
                    phrase=pred.replace('am ', 'are ').replace('was ', 'were ')
                else: raise RuntimeError()
                if tense=='present' and aspect=='perfect' and subject=='They': phrase=phrase
            else:phrase=pred
            english=f'{subject} {phrase}.'
            feature={'lemma':root, 'person':person, 'number':number, 'tense':tense, 'aspect':aspect}
            status=LANG.lexicon[root]['status']
            add(form+'.',english,feature,'finite-paradigm',status,'language/verb_specification.md')

# Clause-level cases; these are controlled paraphrases, not a naturalistic corpus.
for root, english_verb in [('vid','see'),('pel','push'),('trak','pull')]:
    for obj,english_obj in [('akwa','water'),('frat','a brother'),('aerplan','an airplane')]:
        surface=LANG.generate_verb(root)+' '+LANG.generate_noun(obj,'accusative')+'.'
        add(surface,f'I {english_verb} {english_obj}.',
            {'lemma':root,'person':1,'tense':'present','aspect':'simple','object_lemma':obj},
            'svo-object',LANG.lexicon[root]['status'],'language/word_order.md')

for sentence, english, keys in [
 ('no vidi akwaem.','I do not see water.',{'negative':True,'lemma':'vid','object_lemma':'akwa'}),
 ('ka vidi akwaem?','Do I see water?',{'interrogative':True,'lemma':'vid','object_lemma':'akwa'}),
 ('ka no vidi akwaem?','Do I not see water?',{'interrogative':True,'negative':True,'lemma':'vid','object_lemma':'akwa'}),
 ('i vidi akwaem.','I see water.',{'lemma':'vid','object_lemma':'akwa'}),
 ('u vidu akwaem.','You see water.',{'lemma':'vid','person':2,'object_lemma':'akwa'}),
 ('wi uman vidan akwaem.','They see water.',{'lemma':'vid','person':3,'number':'plural','object_lemma':'akwa'}),
]:
    # The final row is incompatible: wi uman does not uniquely refer to 'they' and parser
    # checks agreement only for pronouns. Exclude until phrase semantics are reviewed.
    if sentence.startswith('wi uman'):continue
    add(sentence,english,keys,'clause-operators',LANG.lexicon['vid']['status'],'language/questions.md;language/negation.md')

# Keep everything deterministic and fail rather than overwrite silently in --check mode.
content=''.join(json.dumps(row,ensure_ascii=False,sort_keys=True)+'\n' for row in rows)
if '--check' in sys.argv:
    if not OUT.exists() or OUT.read_text()!=content: raise SystemExit('pilot corpus out of sync')
else:
    OUT.write_text(content)
print(f'pilot corpus: {len(rows)} parser-verified draft pairs; SHA256 {hashlib.sha256(content.encode()).hexdigest()[:16]}')
