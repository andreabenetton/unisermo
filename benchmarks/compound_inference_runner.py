"""Bounded OpenRouter study: 12 compounds x 3 conditions x 2 models."""
import json,os,time,argparse
from pathlib import Path
from benchmarks.compound_inference import build,score
from benchmarks.openrouter_runner import invoke,RateLimited,MODELS
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--model",required=True,choices=list(MODELS.values()))
    parser.add_argument("--output",required=True,type=Path)
    a=parser.parse_args()
    key=os.environ.get("OPENROUTER_API_KEY","")
    if not key:raise ValueError("OPENROUTER_API_KEY missing")
    prompts,answers=build()
    if len(prompts)!=36:raise ValueError("unsafe request count")
    a.output.parent.mkdir(parents=True,exist_ok=True)
    if a.output.exists():raise ValueError("output already exists")
    results=[]
    with a.output.open("x",encoding="utf8") as f:
        for q in prompts:
            for attempt in range(3):
                try:
                    result=invoke(key,a.model,q,None,max_output=144)
                    break
                except RateLimited:
                    if attempt==2:raise
                    time.sleep((8,25)[attempt])
            results.append(result)
            f.write(json.dumps(result,ensure_ascii=False)+"\n");f.flush()
            print(f"{a.model}: {len(results)}/36",flush=True)
            time.sleep(1)
    report=score(answers,results)
    report["model"]=a.model
    a.output.with_suffix(".score.json").write_text(json.dumps(report,indent=2)+"\n")
if __name__=="__main__": main()
