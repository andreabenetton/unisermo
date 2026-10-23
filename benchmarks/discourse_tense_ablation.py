"""Ablation of three explanatory elements; original six clauses unchanged."""
from benchmarks.discourse_semantics import build
PARTS={
"zero":"Present tense has no tense marker; past tense inserts d between verb root and person suffix. ",
"examples":"Examples: pel+i=peli means present first person; pel+d+u=peldu means past second person. ",
"procedure":"For each finite verb, identify the root and final person suffix, then inspect the intervening position: d means past; no d means present. Final i is person, not past. "
}
VARIANTS={"zero_only":("zero",),"examples_only":("examples",),"procedure_only":("procedure",),
          "zero_examples":("zero","examples"),"zero_procedure":("zero","procedure"),
          "examples_procedure":("examples","procedure"),"all_three":("zero","examples","procedure")}
def build_variant(name):
    if name not in VARIANTS:raise ValueError("unknown ablation")
    q,key=build()
    prefix="".join(PARTS[k] for k in VARIANTS[name])
    for x in q:x["messages"][0]["content"]=prefix+x["messages"][0]["content"]
    return q,key
