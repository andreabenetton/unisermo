"""Measure selective lexical headers against growing artificial decoy dictionaries.
Only the confirmed/attested roots in document words are real; padding is synthetic.
This is a transport/token-scaling test, never semantic language validation.
"""
import argparse,json,hashlib
from pathlib import Path
from benchmarks.document_primer import header,GLOSSES,RULE
ROOT=Path(__file__).resolve().parents[1]
WORDS=("aervok","umanplan","klartrak","sivplan","kurarvok","altsentr","sirkulager","basvok")
ALPHABET="abdefgijklmoprstuvz"
def synthetic_roots(count):
    values=[];occupied=set(GLOSSES)
    for n in range(count*4+100):
        digits=[];x=n
        for _ in range(5):digits.append(ALPHABET[x%len(ALPHABET)]);x//=len(ALPHABET)
        form="".join(reversed(digits))
        if form not in occupied:
            values.append((form,"benchmark-only artificial token "+str(n)))
            occupied.add(form)
            if len(values)==count:break
    if len(values)!=count:raise ValueError("insufficient placeholder forms")
    return values
def build(size):
    if size not in (100,1000):raise ValueError("sizes only 100 or 1000")
    minimal=header(WORDS)
    if len(GLOSSES)>size:raise ValueError("too few dictionary slots")
    padded={**GLOSSES,**dict(synthetic_roots(size-len(GLOSSES)))}
    full=RULE+"\nRoots: "+"; ".join(k+"="+v for k,v in sorted(padded.items()))+"\nWords: "+", ".join(WORDS)
    return {"size":size,"minimal":minimal["header"],"full":full,"words":list(WORDS),
            "placeholder_count":size-len(GLOSSES),"real_glossary_count":len(GLOSSES)}
def analyze():
    import tiktoken
    encodings=("o200k_base","cl100k_base")
    rows=[]
    for size in (100,1000):
        x=build(size)
        for enc in encodings:
            encoder=tiktoken.get_encoding(enc)
            a=len(encoder.encode(x["minimal"]));b=len(encoder.encode(x["full"]))
            rows.append({"entries":size,"encoding":enc,"minimal_tokens":a,"padded_tokens":b,
                         "padding_tokens":b-a,"ratio":round(b/a,2),
                         "fake_entries":x["placeholder_count"]})
    return {"schema":"unisermo/scaling-simulation@1","status":"synthetic_padding_not_real_lexicon",
            "document_words":list(WORDS),"tokenizer_results":rows,
            "disclaimer":"Artificial unused entries have placeholder definitions and serve only for tokenizer transport overhead; no claimed lexical meaning or LLM comprehension at 100/1000 real roots."}
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);a=p.parse_args()
    report=analyze();a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print(json.dumps(report["tokenizer_results"]))
if __name__=="__main__":main()
