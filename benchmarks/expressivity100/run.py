"""Reproducible offline expressivity audit; semantic judgments are reviewable."""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path
from formalization.core import Unisermo

SOURCE = Path(__file__).resolve().parent / "cases.json"

def execute():
    samples = json.loads(SOURCE.read_text(encoding="utf-8"))["cases"]
    assert len(samples) == 100
    assert len({c["id"] for c in samples}) == 100
    assert len({c["italian"] for c in samples}) == 100
    domains = Counter(c["domain"] for c in samples)
    assert len(domains) == 10 and set(domains.values()) == {10}, domains
    grammar = Unisermo()
    results = []
    for c in samples:
        assert c["coverage"] in {"exact", "partial", "gap"}, c
        assert bool(c["unisermo"]) == (c["coverage"] != "gap"), c
        result = dict(c)
        result.update(parser_accepts=None, parser_kind=None, parser_error=None)
        if c["unisermo"]:
            try:
                ast = grammar.parse_sentence(c["unisermo"])
                result["parser_accepts"] = True
                result["parser_kind"] = ast.get("kind")
            except Exception as exc:
                result["parser_accepts"] = False
                result["parser_error"] = type(exc).__name__ + ": " + str(exc)
        results.append(result)
    return results

def report(results):
    totals = Counter(c["coverage"] for c in results)
    candidates = [c for c in results if c["unisermo"]]
    accepted = [c for c in candidates if c["parser_accepts"]]
    failed = [c for c in candidates if not c["parser_accepts"]]
    rows = [
        "# Unisermo Expressivity-100 — rapporto sperimentale",
        "",
        "Campione intenzionale di dieci domini, dieci situazioni per dominio. "
        "Le valutazioni semantiche sono proposte da sottoporre a revisione umana; "
        "non sono misure oggettive di competenza dei parlanti. "
        "Il parser verifica la riconoscibilità formale, non la fedeltà della traduzione.",
        "",
        "- Copertura fedele proposta: **" + str(totals["exact"]) + "/100**",
        "- Parafrasi parziali: **" + str(totals["partial"]) + "/100**",
        "- Lacune: **" + str(totals["gap"]) + "/100**",
        "- Forme accettate dal parser: **" + str(len(accepted)) + "/" + str(len(candidates)) + "**",
        "",
        "## Matrice di verifica", "",
        "| Giudizio semantico | Parser accetta | Parser rifiuta | Non proposto |",
        "|---|---:|---:|---:|",
    ]
    for status in ("exact","partial","gap"):
        sub = [x for x in results if x["coverage"] == status]
        rows.append("| " + status + " | " +
                    " | ".join(str(sum(x["parser_accepts"] is v for x in sub))
                               for v in (True,False,None)) + " |")
    rows.extend(["", "## Tutte le 100 frasi", ""])
    for domain in dict.fromkeys(c["domain"] for c in results):
        rows.extend(["### " + domain, "",
                     "| ID | Italiano | Unisermo candidato | Giudizio | Parser | Osservazione |",
                     "|---|---|---|---|---|---|"])
        for c in results:
            if c["domain"] != domain:
                continue
            quoted = chr(96) + c["unisermo"] + chr(96) if c["unisermo"] else "—"
            parser = ("—" if c["parser_accepts"] is None else
                      "OK" if c["parser_accepts"] else "RIFIUTA")
            rows.append("| " + " | ".join(
                str(x).replace("|","\\|") for x in
                (c["id"],c["italian"],quoted,c["coverage"],parser,c["note"])) + " |")
        rows.append("")
    rows.extend(["## Espressioni non riconosciute dal parser", ""])
    for c in failed:
        rows.append("- **" + c["id"] + "** " + chr(96) + c["unisermo"] + chr(96) +
                    " (" + c["coverage"] + "): " + c["parser_error"])
    if not failed:
        rows.append("Nessuna.")
    rows.append("")
    summary = ("EXPRESSIVITY_100 semantic exact=" + str(totals["exact"]) +
               " partial=" + str(totals["partial"]) +
               " gap=" + str(totals["gap"]) +
               " parser accepted=" + str(len(accepted)) + "/" + str(len(candidates)) +
               " rejected=" + str(len(failed)))
    print(summary)
    for c in failed:
        print("REJECTED " + c["id"] + " " + c["coverage"] + " " + c["unisermo"] +
              " :: " + c["parser_error"])
    for domain in dict.fromkeys(c["domain"] for c in results):
        rs=[c for c in results if c["domain"] == domain]
        print("DOMAIN " + domain + " exact=" + str(sum(c["coverage"]=="exact" for c in rs)) +
              " partial=" + str(sum(c["coverage"]=="partial" for c in rs)) +
              " gap=" + str(sum(c["coverage"]=="gap" for c in rs)) +
              " parsed=" + str(sum(c["parser_accepts"] is True for c in rs)))
    return "\n".join(rows) + "\n"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",default="benchmarks/expressivity100/RESULTS.md")
    parser.add_argument("--json",default="benchmarks/expressivity100/results.json")
    args = parser.parse_args()
    samples = execute()
    Path(args.output).write_text(report(samples),encoding="utf-8")
    Path(args.json).write_text(json.dumps(samples,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

if __name__ == "__main__":
    main()
