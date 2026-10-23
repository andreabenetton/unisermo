"""Experimental per-document Unisermo root header.

No canonical lexical changes; unknown strings never infer new roots.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "formalization/data/lexicon_index.json"
GLOSSES = {"aer":"air","plan":"flat plane","alt":"up","bas":"down",
           "mov":"move","vok":"voice","uman":"human","siv":"citizen",
           "klar":"clear","sirkul":"circle","trak":"pull",
           "sentr":"center","ager":"act","kurar":"care","stru":"build"}
RULE = "Compound words join two lexical roots without a separator; context may leave meaning ambiguous."

def lexemes():
    data=json.loads(INDEX.read_text(encoding="utf8"))["entries"]
    return {e["form"]:e for e in data}

def header(words, allowed=None):
    allowed = set(GLOSSES) if allowed is None else set(allowed)
    words=list(words)
    if not words or len(words)>64:
        raise ValueError("expected 1..64 words")
    entries=lexemes()
    by_word={}
    roots=set()
    for word in words:
        if not word.isalpha() or not word.islower():
            raise ValueError("invalid surface")
        possibilities=[(a,b) for a in allowed for b in allowed if a+b==word]
        if len(possibilities)!=1:
            raise ValueError("unknown or ambiguous segmentation: "+word)
        a,b=possibilities[0]
        if any(x not in entries for x in (a,b)):
            raise ValueError("unknown component")
        by_word[word]=[a,b]
        roots.update((a,b))
    glossary="; ".join(k+"="+GLOSSES[k] for k in sorted(roots))
    text=RULE+"\nRoots: "+glossary+"\nWords: "+", ".join(words)
    return {"schema":"unisermo/document-primer@1","status":"experimental",
            "words":words,"segments":by_word,"roots":sorted(roots),
            "header":text,"canonical_changes":False}

def main():
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("words",nargs="+")
    p.add_argument("--output",type=Path)
    args=p.parse_args()
    result=header(args.words)
    text=json.dumps(result,indent=2,ensure_ascii=False)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding="utf8")
    else:print(text,end="")
if __name__=="__main__":main()
