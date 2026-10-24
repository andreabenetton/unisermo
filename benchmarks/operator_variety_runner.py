"""Bounded eight-call OpenRouter experiment on diverse grammatical slots."""
import argparse,json,os,time
from pathlib import Path
from benchmarks.operator_variety import build,score
from benchmarks.openrouter_runner import invoke,MODELS,RateLimited
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);a=p.parse_args()
    secret=os.environ.get("OPENROUTER_API_KEY")
    if not secret or a.output.exists():raise ValueError("missing key or existing output")
    prompts,key=build()
    if len(prompts)!=8:raise ValueError("request cap")
    a.output.parent.mkdir(parents=True,exist_ok=True)
    responses=[]
    with a.output.open("x",encoding="utf8") as out:
        for question in prompts:
            for attempt in range(3):
                try:response=invoke(secret,MODELS["qwen"],question,None,max_output=450);break
                except RateLimited:
                    if attempt==2:raise
                    time.sleep((8,25)[attempt])
            responses.append(response)
            out.write(json.dumps(response)+"\n");out.flush()
            print("completed",len(responses),"/8",flush=True)
            time.sleep(1)
    report=score(key,responses)
    report["provider_usage"]={f:sum((x.get("usage") or {}).get(f) or 0 for x in responses) for f in ("prompt_tokens","completion_tokens","cost")}
    a.output.with_suffix(".score.json").write_text(json.dumps(report,indent=2)+"\n")
if __name__=="__main__":main()
