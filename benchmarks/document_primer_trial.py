"""Bounded comparison: one minimal document glossary versus full glossary."""
import json,os,argparse
from pathlib import Path
from benchmarks.document_primer import header,GLOSSES,RULE
from benchmarks.openrouter_runner import invoke,MODELS
WORDS=("aervok","umanplan","klartrak","sivplan","kurarvok","altsentr","sirkulager","basvok")
FORMAT='Return JSON with a "segments" object mapping each word to its two component roots and a "glosses" object mapping each word to a literal English gloss. Do not invent conventional meanings for ambiguous compositions.'
def build():
    small=header(WORDS)
    full=RULE+"\nRoots: "+"; ".join(k+"="+v for k,v in sorted(GLOSSES.items()))+"\nWords: "+", ".join(WORDS)
    return [("minimal",small["header"]),("full",full)]
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    key=os.environ.get("OPENROUTER_API_KEY","")
    if not key:raise ValueError("secret unavailable")
    if args.output.exists():raise ValueError("output exists")
    args.output.parent.mkdir(parents=True,exist_ok=True)
    expected=header(WORDS)["segments"]
    rows=[]
    with args.output.open("x",encoding="utf8") as f:
        for n,(label,body) in enumerate(build()):
            result=invoke(key,MODELS["qwen"],{"id":f"D{n+1:03d}","messages":[{"role":"user","content":body+"\n"+FORMAT}]},None,max_output=450)
            result["condition"]=label
            rows.append(result)
            f.write(json.dumps(result)+"\n")
            f.flush()
    summary=[]
    for r in rows:
        raw=r["answer"].strip()
        fence=chr(96)*3
        if raw.startswith(fence):
            lines=raw.splitlines()
            if len(lines)>2 and lines[0] in (fence,fence+"json") and lines[-1]==fence:
                raw="\n".join(lines[1:-1])
        try:obj=json.loads(raw)
        except (ValueError,TypeError):obj={}
        segments=obj.get("segments") if isinstance(obj,dict) else None
        correct=sum(isinstance(segments,dict) and segments.get(w)==expected[w] for w in WORDS)
        summary.append({"condition":r["condition"],"correct_segments":correct,"total":len(WORDS),
                        "usage":r.get("usage"),"gloss_semantics":"requires_manual_review"})
    args.output.with_suffix(".score.json").write_text(json.dumps({"results":summary},indent=2)+"\n")
if __name__=="__main__":main()
