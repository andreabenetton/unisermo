"""One-shot limited OpenRouter study: twelve paired prompts total."""
import argparse,json,os,time
from pathlib import Path
from benchmarks.discourse_tense_replication import build,report
from benchmarks.openrouter_runner import invoke,MODELS,RateLimited
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);a=p.parse_args()
    secret=os.environ.get("OPENROUTER_API_KEY")
    if not secret or a.output.exists():raise ValueError("missing secret or existing output")
    prompts,truth=build()
    if len(prompts)!=12 or len(truth)!=6:raise ValueError("request cap")
    a.output.parent.mkdir(parents=True,exist_ok=True)
    rows=[]
    with a.output.open("x",encoding="utf8") as f:
        for q in prompts:
            for attempt in range(3):
                try:reply=invoke(secret,MODELS["qwen"],q,None,max_output=256);break
                except RateLimited:
                    if attempt==2:raise
                    time.sleep((8,25)[attempt])
            reply.update({"doc":q["doc"],"variant":q["variant"]})
            rows.append(reply)
            f.write(json.dumps(reply)+"\n");f.flush()
            print(len(rows),"/12",q["variant"],flush=True)
            time.sleep(1)
    a.output.with_suffix(".score.json").write_text(json.dumps(report(rows,truth),indent=2)+"\n")
if __name__=="__main__":main()
