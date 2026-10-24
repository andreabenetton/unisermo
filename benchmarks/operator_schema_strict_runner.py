"""Eight-call strict response schema pilot."""
import argparse,json,os,time
from pathlib import Path
from benchmarks.operator_schema_strict import build_strict
from benchmarks.operator_variety import score
from benchmarks.openrouter_runner import invoke,MODELS,RateLimited
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);a=p.parse_args()
    secret=os.environ.get("OPENROUTER_API_KEY")
    if not secret or a.output.exists():raise ValueError("secret missing or output exists")
    questions,key=build_strict()
    if len(questions)!=8:raise ValueError("request count cap")
    a.output.parent.mkdir(parents=True,exist_ok=True)
    rows=[]
    with a.output.open("x",encoding="utf8") as stream:
        for q in questions:
            for attempt in range(3):
                try:reply=invoke(secret,MODELS["qwen"],q,None,max_output=450);break
                except RateLimited:
                    if attempt==2:raise
                    time.sleep((8,25)[attempt])
            rows.append(reply);stream.write(json.dumps(reply)+"\n");stream.flush()
            print(len(rows),"/8",flush=True);time.sleep(1)
    report=score(key,rows)
    report["usage"]={f:sum((r.get("usage") or {}).get(f) or 0 for r in rows) for f in ("prompt_tokens","completion_tokens","cost")}
    a.output.with_suffix(".score.json").write_text(json.dumps(report,indent=2)+"\n")
if __name__=="__main__":main()
