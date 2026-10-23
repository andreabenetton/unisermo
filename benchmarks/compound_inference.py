"""Controlled compound-understanding experiment; no normative changes."""
import json
from pathlib import Path
DATA=Path(__file__).resolve().parents[1]/"research/lexicon/productive-compound-trials-001.json"
GLOSS={"aer":"air","plan":"plane","alt":"up","mov":"move","bas":"down","siv":"citizen","vok":"voice","sirkul":"circle","kurar":"care","ager":"act","klar":"clear","stru":"structure","sentr":"center","uman":"human","trak":"pull"}
RULE="Unisermo compounds concatenate two roots without a linker. Meanings may be ambiguous."
def build():
    cases=json.loads(DATA.read_text())["cases"]
    prompts=[];key=[]
    for mode in ("cold","rule_only","dictionary"):
        for c in cases:
            uid=f"C{len(prompts)+1:03d}"
            intro=RULE if mode!="cold" else ""
            if mode=="dictionary": intro+=" Root dictionary: "+", ".join(k+"="+v for k,v in GLOSS.items())
            prompt=intro+"\nInterpret this Unisermo form: "+c["surface"]+'\nReply with JSON: {"parts":["root1","root2"],"gloss":"literal meaning","ambiguous":true}.'
            prompts.append({"id":uid,"messages":[{"role":"user","content":prompt}]})
            key.append({"id":uid,"mode":mode,"case":c["id"],"parts":c["components"],"ambiguity":c["ambiguity"]})
    return prompts,key
def score(key,answers):
    seen={a["id"]:a for a in answers}
    if len(seen)!=len(answers) or set(seen)!={k["id"] for k in key}:raise ValueError("missing or duplicate answers")
    groups={};details=[]
    for k in key:
        response=seen[k["id"]]
        raw=response.get("answer","").strip()
        if raw.startswith(chr(96)*3):
            lines=raw.splitlines()
            if len(lines)>2 and lines[0] in (chr(96)*3,chr(96)*3+"json") and lines[-1]==chr(96)*3:raw="\n".join(lines[1:-1])
        try: parsed=json.loads(raw)
        except (TypeError,ValueError):parsed=None
        valid=isinstance(parsed,dict) and isinstance(parsed.get("parts"),list) and isinstance(parsed.get("gloss"),str) and isinstance(parsed.get("ambiguous"),bool)
        accurate=valid and parsed["parts"]==k["parts"]
        group=groups.setdefault(k["mode"],{"total":0,"json_valid":0,"segmented":0,"input_tokens":0,"output_tokens":0,"cost":0})
        group["total"]+=1;group["json_valid"]+=int(valid);group["segmented"]+=int(accurate)
        usage=response.get("usage") or {}
        group["input_tokens"]+=usage.get("prompt_tokens") or 0
        group["output_tokens"]+=usage.get("completion_tokens") or 0
        group["cost"]+=usage.get("cost") or 0
        details.append({"id":k["id"],"mode":k["mode"],"case":k["case"],"segments_correct":bool(accurate),"gloss":parsed.get("gloss") if valid else None,"ambiguous":parsed.get("ambiguous") if valid else None})
    return {"groups":groups,"details":details,"limitation":"No automatic grading of English gloss semantic correctness; glossary repeated in each isolated request."}
