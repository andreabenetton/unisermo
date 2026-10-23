"""Compact tense primer on the same six benchmark documents."""
from benchmarks.discourse_semantics import build
COMPACT="Verb = root + optional tense d (past; absent = present) + person suffix i (1st) or u (2nd). Example: peli=present; peldu=past. "
def build_compact():
    questions,key=build()
    for question in questions:
        question["messages"][0]["content"]=COMPACT+question["messages"][0]["content"]
    return questions,key
