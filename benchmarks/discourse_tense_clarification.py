"""Controlled morphology instruction contrast on unchanged discourse documents."""
from benchmarks.discourse_semantics import build,score
EXPLICIT=("Important finite-verb rule: Unisermo present tense has ZERO tense marker. "
          "The person ending follows the verb root directly: pel+i=peli (present first person), "
          "trak+i=traki, vid+i=vidi. The PAST tense inserts d BEFORE the person ending: "
          "pel+d+u=peldu (past second person), trakdu, viddu. "
          "Do NOT interpret a final i by itself as past: it marks person 1. "
          "For each verb, first identify the lemma, then check whether d occurs immediately "
          "between that lemma and its person ending. No d means present; d means past. ")
def enhanced():
    questions,key=build()
    for q in questions:
        m=q["messages"][0]
        # Only add explanatory context; leave the original six clauses and output format untouched.
        m["content"]=EXPLICIT+m["content"]
    return questions,key
