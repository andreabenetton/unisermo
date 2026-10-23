"""Bounded 42-request Qwen trial for seven morphology prompt variants."""
import argparse,json,os,time
from pathlib import Path
from benchmarks.discourse_tense_ablation import VARIANTS,build_variant
from benchmarks.discourse_semantics import score
from benchmarks.openrouter_runner import invoke,MODELS,RateLimited
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);a=p.parse_args()
    key=os.environ.get("OPENROUTER_API_KEY")
    if not key:raise ValueError("missing secret")
    if a.output.exists():raise ValueError("output exists")
    a.output.parent.mkdir(parents=True,exist_ok=True)
    rows=[]
    with a.output.open("x",encoding="utf8") as out:
        for name in VARIANTS:
            qs,truth=build_variant(name)
            if len(qs)!=6:raise ValueError("unexpected request count")
            current=[]
            for q in qs:
                for attempt in range(3):
                    try:r=invoke(key,MODELS["qwen"],q,None,max_output=256);break
                    except RateLimited:
                        if attempt==2:raise
                        time.sleep((8,25)[attempt])
                r["variant"]=name;current.append(r);out.write(json.dumps(r)+"\n");out.flush()
                time.sleep(1)
            result=score(truth,current)
            result["variant"]=name
            result["usage"]={k:sum((r.get("usage") or {}).get(k) or 0 for r in current) for k in ("prompt_tokens","completion_tokens","cost")}
            rows.append(result)
            print(name,result["correct_events"],"/18",flush=True)
    a.output.with_suffix(".score.json").write_text(json.dumps({"variants":rows,"experimental":True},indent=2)+"\n")
if __name__=="__main__":main()
