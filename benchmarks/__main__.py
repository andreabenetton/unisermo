"""Benchmark CLI. Counts use real tokenizers only; draft status is explicit."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from .run import run, readiness
from .tokenizers import TiktokenCounter, SentencePieceCounter, HFJsonCounter

OPENAI_ENCODINGS = ('o200k_base', 'cl100k_base')


def write_report(result: dict, path: Path | None) -> None:
    payload = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + '\n'
    if path is None:
        print(payload, end='')
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(payload, encoding='utf-8')
        print(f'written {path}')


def main() -> None:
    p = argparse.ArgumentParser(description='Unisermo Phase 2 tokenizer pilot; only real model tokenizers')
    sub = p.add_subparsers(dest='command', required=True)
    sub.add_parser('readiness', help='machine-readable pilot status (no fake token measurements)')
    m = sub.add_parser('measure', help='count tokens for paired inputs')
    source = m.add_mutually_exclusive_group(required=True)
    source.add_argument('--tiktoken', metavar='ENCODING', help='e.g. o200k_base or cl100k_base')
    source.add_argument('--sentencepiece', metavar='PATH', help='local SentencePiece model')
    source.add_argument('--hf-json', metavar='PATH', help='local Hugging Face tokenizer.json')
    m.add_argument('--include-draft', action='store_true', help='explicitly allow unreviewed pilot translations')
    m.add_argument('--output', type=Path, help='path to JSON report (prints to stdout if omitted)')
    suite = sub.add_parser('measure-openai', help='measure o200k_base and cl100k_base from official tiktoken')
    suite.add_argument('--include-draft', action='store_true', help='required for this unreviewed pilot corpus')
    suite.add_argument('--output-dir', type=Path, default=Path('benchmarks/reports'))
    args = p.parse_args()
    if args.command == 'readiness':
        write_report(readiness(), None)
        return
    if not args.include_draft:
        p.error('pilot contains unreviewed English translations; pass --include-draft for exploratory testing')
    try:
        if args.command == 'measure-openai':
            # Load both encodings before writing anything, preventing a misleading
            # half-complete "suite" when one of the vocabularies is unavailable.
            counters = [TiktokenCounter(name) for name in OPENAI_ENCODINGS]
            results = [run(counter) for counter in counters]
            for name, result in zip(OPENAI_ENCODINGS, results):
                write_report(result, args.output_dir / f'{name}-pilot.json')
            return
        counter = (TiktokenCounter(args.tiktoken) if args.tiktoken else
                   SentencePieceCounter(args.sentencepiece) if args.sentencepiece else
                   HFJsonCounter(args.hf_json))
        write_report(run(counter), args.output)
    except (RuntimeError, FileNotFoundError) as exc:
        p.exit(2, f'tokenizer unavailable: {exc}\n')


if __name__ == '__main__':
    main()
