"""Review probes: parser checks only; not new linguistic ratifications."""
from formalization.core import Unisermo
import json

u = Unisermo()
probes = [
    ("genitive_wheels_exist", "biks bis roda esan"),
    ("genitive_wheels_partial_np", "biks bis roda"),
    ("mother_teaches_own_child", "gene doka genes filem"),
    ("sister_teaches_cousin", "adele doka filadelgenem"),
    ("nephew_child_of_sibling", "filadel mova"),
    ("one_bicycle_not_moving", "bik no mova"),
    ("two_cars_are_not_moving", "bis kar no movan"),
    ("two_cars_remain_fixed", "bis kar inesan fiks"),
    ("build_with_stru", "uman strua portaem"),
    ("build_with_fak", "uman faka portaem"),
    ("toward_station_as_unratified", "tren mova stasionad"),
    ("wheels_belonging_to_bicycle", "biks roda esan"),
    ("locative_bicycle_road", "bik esa karviain"),
    ("nephew_as_object", "uman vida filadelem"),
    ("prefix_mini_existing", "minibus mova"),
]
for label, surface in probes:
    try:
        ast = u.parse_sentence(surface)
        row = {"probe":label, "form":surface, "accepts":True,
               "kind":ast.get("kind"),"subject":ast.get("subject"),"predicate":ast.get("predicate")}
    except Exception as e:
        row = {"probe":label,"form":surface,"accepts":False,"error":str(e)}
    print("PROBE " + json.dumps(row, ensure_ascii=False))
for word in ("filadel", "filadelem", "biks", "genes", "roda", "strua",
             "omni", "ekse", "sekun", "senotodek", "sed", "sidil"):
    analyses=u.analyze_word(word)["analyses"]
    print("WORD " + json.dumps({"form":word,"analyses":analyses},ensure_ascii=False))
