"""Bounded paired schema study (16 OpenRouter calls)."""
import argparse,json,os,time
from pathlib import Path
from benchmarks.operator_schema_fresh import build,summarize
from benchmarks.openrouter_runner import invoke,MODELS,RateLimited
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);a=p.parse_args()
    key=os.environ.get("OPENROUTER_API_KEY")
    if not key or a.output.exists():raise ValueError("secret unavailable or output exists")
    requests,answers=build()
    if len(requests)!=16:raise ValueError("request cap")
    a.output.parent.mkdir(parents=True,exist_ok=True)
    rows=[]
    with a.output.open("x",encoding="utf8") as output:
        for q in requests:
            for attempt in range(3):
                try:response=invoke(key,MODELS["qwen"],q,None,max_output=450);break
                except RateLimited:
                    if attempt==2:raise
                    time.sleep((8,25)[attempt])
            response.update({"doc":q["doc"],"condition":q["condition"]})
            rows.append(response);output.write(json.dumps(response)+"\n");output.flush()
            print(len(rows),"/16",flush=True);time.sleep(1)
    a.output.with_suffix(".score.json").write_text(json.dumps(summarize(rows,answers),indent=2)+"\n")
if __name__=="__main__":main()
