"""Open-ended lexical inference on paired Unisermo clauses.

The model outputs its own English verb lemma; there are NO answer choices.
Mechanical lexical scoring is a limited diagnostic, not a semantic judge.
"""
from __future__ import annotations
import json
import re
from collections import defaultdict
from formalization.core import Unisermo
from benchmarks.root_semantic_guard import shadow_reference_language

CASES = (
    ("i {verb} amikem.", "simple", "present", 1, "singular"),
    ("u {verb} tik amikem.", "simple", "present", 2, "singular"),
    ("a no {verb} fakitem.", "simple", "present", 3, "singular"),
    ("ka i {verb} amikem?", "simple", "present", 1, "singular"),
    ("in {verb} fakitem.", "simple", "past", 1, "plural"),
    ("un no {verb} amikem.", "progressive", "present", 2, "plural"),
    ("ka an {verb} tik fakitem?", "simple", "future", 3, "plural"),
    ("i {verb} amikem.", "perfect", "past", 1, "singular"),
)
ROOTS = (("dik", "say"), ("dir", "say"), ("dirig", "direct"))
VALID = {"say": {"say", "tell", "state", "utter", "express"},
         "direct": {"direct", "guide", "lead", "steer"}}
PROMPT = (
    "You are reading a sentence from Unisermo, a planned language. "
    "Its regular finite verb form is ROOT + aspect (empty=simple, e=ongoing, "
    "o=completed) + tense (empty=present, d=past, f=future) + person "
    "(i=I, u=you, a=he/she/they) + n when plural. "
    "The subject may be a pronoun i/u/a/in/un/an. "
    "Other words: amik=friend, fakit=thing done/fact, tik=this, "
    "no=negation, ka=yes/no question, -em=object marker. "
    "Identify the MAIN VERB'S basic lexical meaning in English. "
    "Do not invent meanings. Respond only JSON with exactly "
    '{"verb":"one English base-form verb"}. No multiple choice.'
)
GLOSSARY = "Controlled temporary dictionary: dik=to say/tell; dir=to say/tell (experimental); dirig=to direct/guide. "
def inflect(root, aspect, tense, person, number, morph):
    f=morph["finite"]
    return root+f["aspect"][aspect]+f["tense"][tense]+f["person"][str(person)]+f["number"][number]

def build():
    canonical=Unisermo()
    alternate=shadow_reference_language()
    questions=[]; key=[]
    for condition in ("unglossed", "glossary"):
        for i,(template,aspect,tense,person,number) in enumerate(CASES):
            for root,meaning in ROOTS:
                verb=inflect(root,aspect,tense,person,number,canonical.morph)
                sentence=template.format(verb=verb)
                parser=alternate if root=="dir" else canonical
                parsed=parser.parse_sentence(sentence)
                pred=parsed["predicate"]
                assert pred["lemma"]==root and pred["aspect"]==aspect and pred["tense"]==tense
                assert pred["person"]==person and pred["number"]==number
                ident=f"O{len(questions)+1:03d}"
                prompt=(PROMPT + ("\n"+GLOSSARY if condition=="glossary" else "")
                        +"\nSentence: "+sentence)
                questions.append({"id":ident,"condition":condition,
                    "split":"development" if i<6 else "reserved",
                    "messages":[{"role":"user","content":prompt}],
                    "response_format":"open_verb_json"})
                key.append({"id":ident,"condition":condition,
                    "split":"development" if i<6 else "reserved",
                    "case_index":i,"root":root,"meaning":meaning,"sentence":sentence})
    assert len(questions)==48
    return questions,key

def extract(answer):
    try:
        value=json.loads(answer)
        if not isinstance(value,dict) or set(value)!={"verb"} or not isinstance(value["verb"],str):
            return None
        s=value["verb"].lower().strip()
        if re.fullmatch(r"[a-z]+",s):
            return s
    except (TypeError,ValueError):
        pass
    return None

def score(key,responses,model):
    expected={x["id"]:x for x in key}
    observed={}
    for x in responses:
        if x["id"] not in expected or x["id"] in observed:
            raise ValueError("duplicate or unknown answer ID")
        observed[x["id"]]=x["answer"]
    if set(observed)!=set(expected):
        raise ValueError("incomplete response coverage")
    totals=defaultdict(lambda: {"total":0,"recognized":0,"invalid_format":0,"other_verbs":{}})
    paired=defaultdict(dict)
    for k in key:
        label=(k["split"],k["condition"],k["root"])
        cell=totals[label]
        cell["total"]+=1
        lemma=extract(observed[k["id"]])
        valid=lemma in VALID[k["meaning"]]
        cell["recognized"]+=int(valid)
        cell["invalid_format"]+=int(lemma is None)
        if lemma is not None and not valid:
            cell["other_verbs"][lemma]=cell["other_verbs"].get(lemma,0)+1
        if k["root"] in ("dir","dik"):
            paired[(k["split"],k["condition"],k["case_index"])][k["root"]]=valid
    groups=[{"split":s,"condition":c,"root":r,**v} for (s,c,r),v in sorted(totals.items())]
    comparison=[]
    for (split,condition,index),cells in sorted(paired.items()):
        if set(cells)!={"dik","dir"}:raise ValueError("unpaired comparison")
        comparison.append({"split":split,"condition":condition,"case_index":index,
                           "dik_success":cells["dik"],"dir_success":cells["dir"]})
    return {"schema":"unisermo/open-inference-score@1",
            "model":model,"trial_count":len(key),
            "groups":groups,"paired":comparison,
            "limits":["Curated lemma synonym whitelist; manual review required for all free responses.",
              "The supplied morphology and object glosses make this a controlled reading task.",
              "No human spoken or written recognizability is measured.",
              "The reserved split must not be used to tune candidate spelling.",
              "Corpus sentences are grammar-valid but naturalness and sense selection remain unreviewed."]}
