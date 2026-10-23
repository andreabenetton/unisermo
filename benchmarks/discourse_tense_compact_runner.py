"""Six-call replication with a more explicit present/preterite parsing instruction."""
import argparse,json,os,time
from pathlib import Path
from benchmarks.discourse_tense_compact import build_compact
from benchmarks.discourse_semantics import score
from benchmarks.openrouter_runner import invoke,MODELS,RateLimited
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);a=p.parse_args()
    key=os.environ.get("OPENROUTER_API_KEY")
    if not key:raise ValueError("no configured key")
    queries,truth=build_compact()
    if len(queries)!=6 or a.output.exists():raise ValueError("request cap or output exists")
    a.output.parent.mkdir(parents=True,exist_ok=True)
    results=[]
    with a.output.open("x",encoding="utf8") as out:
        for q in queries:
            for i in range(3):
                try:reply=invoke(key,MODELS["qwen"],q,None,max_output=256);break
                except RateLimited:
                    if i==2:raise
                    time.sleep((6,18)[i])
            results.append(reply);out.write(json.dumps(reply)+"\n");out.flush()
            print("completed",len(results),"/6",flush=True);time.sleep(1)
    report=score(truth,results)
    report["usage"]={k:sum((r.get("usage") or {}).get(k) or 0 for r in results) for k in ("prompt_tokens","completion_tokens","cost")}
    report["prompt_variant"]="compact_explicit_tense_rule"
    a.output.with_suffix(".score.json").write_text(json.dumps(report,indent=2)+"\n")
if __name__=="__main__":main()
