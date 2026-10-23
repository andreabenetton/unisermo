"""Compare isolated glossary repetition with full-history conversational context."""
import os,json,time,argparse
from pathlib import Path
from benchmarks.compound_inference import GLOSS,RULE,score
from benchmarks.openrouter_runner import invoke,RateLimited,MODELS
from benchmarks.productive_compounds import SOURCE
PRIMER=RULE+" Root dictionary: "+", ".join(k+"="+v for k,v in GLOSS.items())
FORMAT='Reply in JSON only: {"parts":["root1","root2"],"gloss":"literal meaning","ambiguous":true}.'
def build():
    cases=json.loads(SOURCE.read_text())["cases"]
    requests=[];key=[]
    for mode in ("repeated_dictionary","history_dictionary"):
        for i,c in enumerate(cases):
            ident=f"H{len(requests)+1:03d}"
            question="Interpret the Unisermo compound "+c["surface"]+". "+FORMAT
            requests.append({"id":ident,"mode":mode,"question":question,"index":i,"case":c})
            key.append({"id":ident,"mode":mode,"case":c["id"],"parts":c["components"]})
    return requests,key
def run(model,out):
    secret=os.environ.get("OPENROUTER_API_KEY","")
    if not secret:raise ValueError("repository secret missing")
    if model!=MODELS["qwen"]:raise ValueError("Qwen only for first controlled session pilot")
    items,key=build()
    if len(items)!=24:raise ValueError("request cap violated")
    if out.exists():raise ValueError("output exists")
    out.parent.mkdir(parents=True,exist_ok=True)
    history=[{"role":"system","content":PRIMER+" Follow this dictionary for subsequent questions."}]
    rows=[]
    with out.open("x",encoding="utf8") as handle:
        for item in items:
            if item["mode"]=="repeated_dictionary":
                messages=[{"role":"system","content":PRIMER},{"role":"user","content":item["question"]}]
            else:
                messages=history+[{"role":"user","content":item["question"]}]
            for attempt in range(3):
                try: response=invoke(secret,model,{"id":item["id"],"messages":messages},None,max_output=144);break
                except RateLimited:
                    if attempt==2:raise
                    time.sleep((8,25)[attempt])
            response["mode"]=item["mode"];response["case"]=item["case"]["id"]
            rows.append(response)
            handle.write(json.dumps(response)+"\n");handle.flush()
            if item["mode"]=="history_dictionary":
                history=messages+[{"role":"assistant","content":response["answer"]}]
            print(model,item["mode"],item["index"]+1,"/12",flush=True)
            time.sleep(1.2)
    report=score(key,rows)
    report["model"]=model
    report["method"]="full-history conversation re-sent every turn; costs provider-reported, no context caching assumed"
    out.with_suffix(".score.json").write_text(json.dumps(report,indent=2)+"\n")
def main():
    p=argparse.ArgumentParser();p.add_argument("--model",required=True);p.add_argument("--output",type=Path,required=True)
    a=p.parse_args();run(a.model,a.output)
if __name__=="__main__":main()
