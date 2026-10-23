"""Run paired open-ended sentence inference, bounded and fail-closed."""
from __future__ import annotations
import argparse,json,os,time
from pathlib import Path
from benchmarks.open_inference import build,score
from benchmarks.openrouter_runner import invoke,MODELS,RateLimited

def execute(model: str,key: str,out:Path):
    if model not in MODELS.values():raise ValueError("unapproved model")
    if not key:raise ValueError("secret missing")
    if out.exists():raise ValueError("refusing overwrite")
    questions,reference=build()
    if len(questions)!=48:raise ValueError("request bound violated")
    out.parent.mkdir(parents=True,exist_ok=True)
    results=[]
    with out.open("x",encoding="utf8") as f:
        for question in questions:
            for attempt in range(3):
                try:
                    r=invoke(key,model,question,None,max_output=96)
                    break
                except RateLimited:
                    if attempt==2:raise
                    time.sleep((8,25)[attempt])
            results.append(r)
            f.write(json.dumps(r,ensure_ascii=False)+"\n")
            f.flush()
            print(f"{model} completed {len(results)}/48",flush=True)
            time.sleep(1)
    report=score(reference,results,model)
    out.with_suffix(".score.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf8")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--model",choices=list(MODELS.values()),required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    execute(args.model,os.getenv("OPENROUTER_API_KEY",""),args.output)
if __name__=="__main__":main()
