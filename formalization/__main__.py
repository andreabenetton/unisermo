"""CLI: python3 -m formalization [build|validate|analyze|sentence|generate|noun|participle]."""
import argparse
import json
from .core import Unisermo
from .build import run


def main() -> None:
    p = argparse.ArgumentParser(description="Unisermo Phase 1 deterministic reference tools")
    sub = p.add_subparsers(dest="command", required=True)
    build = sub.add_parser("build", help="recreate derived indexes and morphology corpus")
    build.add_argument("--check", action="store_true", help="verify generated files have no drift")
    sub.add_parser("validate", help="run Phase 1 invariant checks")
    word = sub.add_parser("analyze", help="enumerate all recognized word analyses")
    word.add_argument("word")
    sentence = sub.add_parser("sentence", help="parse supported SVO sentence; fail closed outside subset")
    sentence.add_argument("text")
    verb = sub.add_parser("generate", help="generate a finite verb")
    verb.add_argument("lemma")
    verb.add_argument("--tense", default="present")
    verb.add_argument("--aspect", default="simple")
    verb.add_argument("--person", type=int, default=1)
    verb.add_argument("--number", default="singular")
    noun = sub.add_parser("noun", help="generate a nominal case form")
    noun.add_argument("lemma")
    noun.add_argument("--case", default="nominative")
    kinship = sub.add_parser("kinship", help="decode a confirmed/productive genealogy as a typed path")
    kinship.add_argument("word")
    participle = sub.add_parser("participle", help="generate a -it resultative")
    participle.add_argument("lemma")
    args = p.parse_args()
    if args.command == "build":
        run(check=args.check)
    elif args.command == "validate":
        from .validate import validate
        validate()
    else:
        language = Unisermo()
        if args.command == "kinship":
            result = language.parse_kinship(args.word)
            if result is None:
                p.error("unknown, unsupported or ambiguous kinship relation")
        elif args.command == "analyze": result = language.analyze_word(args.word)
        elif args.command == "sentence": result = language.parse_sentence(args.text)
        elif args.command == "generate": result = language.generate_verb(args.lemma, args.tense, args.aspect, args.person, args.number)
        elif args.command == "noun": result = language.generate_noun(args.lemma, args.case)
        else: result = language.generate_participle(args.lemma)
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
