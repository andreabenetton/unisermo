"""Auditable paired-input token counts. No LLM comprehension claims here."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from statistics import mean
from typing import Any
from .tokenizers import Tokenizer

ROOT=Path(__file__).resolve().parents[1]
PILOT=ROOT/'benchmarks/corpus/pilot.jsonl'


def load_corpus(path: Path=PILOT)->list[dict[str,Any]]:
    rows=[json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
    if not rows or len({r['id'] for r in rows})!=len(rows):
        raise ValueError('empty corpus or duplicate ids')
    for r in rows:
        for key in ('id','unisermo','english','grammatical_intent','review_status','split','group'):
            if key not in r:raise ValueError(f"{r.get('id','?')}: missing {key}")
        if r['split'] not in {'development','holdout'}:raise ValueError('invalid split')
        if not r['english'] or not r['unisermo']:raise ValueError('empty text')
    return rows


def summarize(rows:list[dict], key:str)->dict[str,Any]:
    n=len(rows)
    if not n: return {'samples':0,'english_tokens':0,'unisermo_tokens':0,'reduction_pct':None}
    english=sum(r['english_tokens'] for r in rows)
    unisermo=sum(r['unisermo_tokens'] for r in rows)
    return {'samples':n, 'english_tokens':english, 'unisermo_tokens':unisermo,
            'reduction_pct':round(100*(1-unisermo/english),3) if english else None,
            'mean_english_tokens':round(english/n,3),
            'mean_unisermo_tokens':round(unisermo/n,3)}


def evaluate(counter:Tokenizer, corpus:list[dict], digest:str)->dict[str,Any]:
    pairs=[]
    for r in corpus:
        e=counter.count(r['english'])
        u=counter.count(r['unisermo'])
        if not isinstance(e,int) or not isinstance(u,int) or e<=0 or u<=0:
            raise ValueError('token counter must yield positive integer token counts')
        pairs.append({'id':r['id'],'split':r['split'],'group':r['group'],
                      'english_tokens':e,'unisermo_tokens':u,'delta':u-e,
                      'review_status':r['review_status']})
    return {'encoding':counter.name, 'implementation':counter.implementation,
            'tokenizer_sha256':getattr(counter,'vocab_sha256',None),
            'corpus_sha256':digest,
            'review_status':'not_human_verified' if any(r['review_status']!='human_verified' for r in corpus) else 'human_verified',
            'scope':'paired input token counts only; not full task cost, semantic correctness, or inference output',
            'overall':summarize(pairs, 'overall'),
            'splits':{s:summarize([r for r in pairs if r['split']==s],s) for s in ('development','holdout')},
            'groups':{g:summarize([r for r in pairs if r['group']==g],g) for g in sorted({r['group'] for r in pairs})},
            'pairs':pairs}


def run(counter:Tokenizer,path:Path=PILOT)->dict[str,Any]:
    raw=path.read_bytes()
    return evaluate(counter,load_corpus(path),hashlib.sha256(raw).hexdigest())


def readiness(path:Path=PILOT)->dict[str,Any]:
    import importlib.util
    c=load_corpus(path)
    return {'phase':'tokenizer pilot (Phase 2)',
            'corpus_records':len(c),
            'groups':{g:sum(1 for r in c if r['group']==g) for g in sorted({r['group'] for r in c})},
            'development_records':sum(1 for r in c if r['split']=='development'),
            'holdout_records':sum(1 for r in c if r['split']=='holdout'),
            'human_reviewed':sum(1 for r in c if r['review_status']=='human_verified'),
            'parser_verified':sum(1 for r in c if r['review_status']=='draft_parser_verified'),
            'tokenizer_availability':{m:bool(importlib.util.find_spec(m)) for m in ('tiktoken','tokenizers','sentencepiece')},
            'actual_token_counts':None,
            'reason':'No real tokenizer was executed for this report; raw corpus and engine remain ready.',
            'limits':['Pilot consists of morphology-biased examples',
                      'English renderings are drafted, not independently reviewed',
                      'Tokenizer counts alone do not measure LLM comprehension, inference output or full task cost']}
