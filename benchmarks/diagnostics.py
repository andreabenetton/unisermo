"""Inspect measured tokenizer reports without inventing tokenizer splits.

A report with per-row *counts* cannot disclose which substrings were merged.
Use optional real tiktoken encoders for actual segmentation diagnostics.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from .run import load_corpus, PILOT


def analyze(reports: list[dict], corpus: list[dict], corpus_bytes: bytes) -> dict:
    digest = hashlib.sha256(corpus_bytes).hexdigest()
    index = {r['id']:r for r in corpus}
    if len(index) != len(corpus):raise ValueError('duplicated corpus IDs')
    results = {'corpus_sha256':digest, 'pairs':len(corpus), 'encodings':{},'review':{}}
    for report in reports:
        name = report['encoding']
        if report['corpus_sha256'] != digest:raise ValueError(f'{name}: corpus fingerprint mismatch')
        if set(x['id'] for x in report['pairs']) != set(index):raise ValueError(f'{name}: rows mismatch')
        by_group=defaultdict(list)
        annotated=[]
        for item in report['pairs']:
            row=index[item['id']]
            change=item['unisermo_tokens']-item['english_tokens']
            enriched={'id':item['id'],'group':row['group'],'split':row['split'],
                      'unisermo':row['unisermo'],'english':row['english'],
                      'english_tokens':item['english_tokens'], 'unisermo_tokens':item['unisermo_tokens'],
                      'extra_tokens':change}
            annotated.append(enriched)
            by_group[row['group']].append(enriched)
        groups={}
        for key, entries in sorted(by_group.items()):
            u=sum(e['unisermo_tokens'] for e in entries)
            e=sum(e['english_tokens'] for e in entries)
            groups[key]={'pairs':len(entries),'unisermo_tokens':u,'english_tokens':e,
                         'extra_tokens':u-e,'reduction_pct':round(100*(1-u/e),3) if e else None}
        dev=[x for x in annotated if x['split']=='development']
        results['encodings'][name]={
            'implementation':report['implementation'],
            'overall':report['overall'], 'groups':groups,
            'development_worst':sorted(dev,key=lambda x:(-x['extra_tokens'],x['id']))[:15],
            'development_best':sorted(dev,key=lambda x:(x['extra_tokens'],x['id']))[:15],
            'holdout_policy':'no ranking or optimization on holdout; aggregate metrics only',
            'holdout_aggregate':report['splits']['holdout'],
        }
    # Structural audit, not human bilingual approval.
    for row in corpus:
        problems=[]
        if row.get('review_status')!='human_verified': problems.append('translation_not_independently_verified')
        if row['group']=='finite-paradigm':
            tense=row['grammatical_intent']['tense'];aspect=row['grammatical_intent']['aspect']
            en=row['english'].lower()
            if aspect=='perfect' and tense=='present' and not any(x in en for x in ['have ','has ']):
                problems.append('verify_english_perfect_aspect')
            if row['grammatical_intent']['person']==2:
                problems.append('english_you_number_underspecified')
        if row['unisermo'].startswith('i ') or row['unisermo'].startswith('u '):
            problems.append('verify_optional_explicit_subject_parity')
        results['review'][row['id']]={'group':row['group'],'flags':problems,'review_status':'pending_independent_review',
                                      'english':row['english'],'unisermo':row['unisermo']}
    return results


def real_segmentation(encoding: str, forms: list[str]) -> dict:
    from .tokenizers import TiktokenCounter
    counter=TiktokenCounter(encoding)
    enc=counter.encoder
    return {'encoding':encoding,'implementation':counter.implementation,'vocab_sha256':counter.vocab_sha256,
            'forms':[{'text':form,'token_ids':enc.encode(form,disallowed_special=()),
                      'token_pieces':[enc.decode_single_token_bytes(t).decode('utf-8','backslashreplace')
                                      for t in enc.encode(form,disallowed_special=())]}
                     for form in forms]}


def main():
    p=argparse.ArgumentParser(description='Unisermo tokenization diagnostic')
    p.add_argument('--reports',type=Path,nargs='+',required=True)
    p.add_argument('--corpus',type=Path,default=PILOT)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--segment-openai',action='store_true',help='requires official tiktoken encodings')
    args=p.parse_args()
    reports=[json.loads(x.read_text()) for x in args.reports]
    corpus=load_corpus(args.corpus)
    result=analyze(reports,corpus,args.corpus.read_bytes())
    if args.segment_openai:
        from formalization.core import Unisermo
        lang=Unisermo()
        # A bounded list of *actual* roots and inflections. Token boundaries must be real.
        forms=sorted({r['grammatical_intent']['lemma'] for r in corpus if 'lemma' in r['grammatical_intent']})
        forms=sorted(set(forms)|{x.strip('.?!') for r in corpus for x in r['unisermo'].split() if x.strip('.?!') in lang.lexicon})
        forms=forms[:80]
        result['segmentation']={name:real_segmentation(name,forms) for name in result['encodings']}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
    print(f'Written {args.output}: {len(corpus)} paired rows; {len(reports)} real-tokenizer reports')

if __name__=='__main__': main()
