"""Bounded six-request test of discourse semantic slots."""
import argparse,json,os,time
from pathlib import Path
from benchmarks.discourse_semantics import build,score
from benchmarks.openrouter_runner import invoke,MODELS,RateLimited
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);a=p.parse_args()
    key=os.getenv("OPENROUTER_API_KEY","")
    if not key:raise ValueError("secret not configured")
    q,answers=build()
    if len(q)!=6:raise ValueError("request cap")
    if a.output.exists():raise ValueError("output exists")
    a.output.parent.mkdir(parents=True,exist_ok=True)
    rows=[]
    with a.output.open("x",encoding="utf8") as out:
        for request in q:
            for attempt in range(3):
                try:result=invoke(key,MODELS["qwen"],request,None,max_output=256);break
                except RateLimited:
                    if attempt==2:raise
                    time.sleep([6,18][attempt])
            rows.append(result);out.write(json.dumps(result)+"\n");out.flush()
            print("Completed",len(rows),"/6",flush=True)
            time.sleep(1)
    result=score(answers,rows)
    result["reported_usage"]={f:sum((r.get("usage") or {}).get(f) or 0 for r in rows) for f in ("prompt_tokens","completion_tokens","cost")}
    a.output.with_suffix(".score.json").write_text(json.dumps(result,indent=2)+"\n")
if __name__=="__main__":main()
