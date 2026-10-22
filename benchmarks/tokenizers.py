"""Adapters for real, versioned tokenizer implementations.

Do not replace model token counts with whitespace/character approximations.
"""
from __future__ import annotations
from pathlib import Path
from typing import Protocol
import hashlib
import importlib.metadata


class Tokenizer(Protocol):
    name: str
    implementation: str
    def count(self, text: str) -> int: ...


def _tiktoken_vocab_digest(encoder: object) -> str:
    """Hash the actual mergeable BPE vocabulary, not just its advertised name.

    tiktoken currently provides no public encoding checksum API. Access its
    internal merge table *only for provenance*, never for token computation.
    The encoded bytes and ranks are serialized canonically so the same table
    hashes identically regardless of dict insertion order.
    """
    try:
        ranks = encoder._mergeable_ranks
    except AttributeError as exc:
        raise RuntimeError('tiktoken does not expose a BPE merge table for audit') from exc
    digest = hashlib.sha256()
    for token, rank in sorted(ranks.items(), key=lambda pair: (pair[1], pair[0])):
        if not isinstance(token, bytes) or not isinstance(rank, int):
            raise TypeError('unexpected tiktoken vocabulary representation')
        digest.update(rank.to_bytes(8, 'big'))
        digest.update(len(token).to_bytes(4, 'big'))
        digest.update(token)
    return digest.hexdigest()


class TiktokenCounter:
    def __init__(self, encoding: str):
        try:
            import tiktoken
        except ImportError as e:
            raise RuntimeError(
                'tiktoken is not installed; install benchmarks/requirements-openai.txt '
                '(upstream: https://github.com/openai/tiktoken)'
            ) from e
        try:
            self.encoder = tiktoken.get_encoding(encoding)
        except Exception as e:
            raise RuntimeError(
                f'Cannot load tiktoken encoding {encoding}. Initial vocabulary '
                f'load may need network access or a populated TIKTOKEN_CACHE_DIR: {e}'
            ) from e
        self.name = encoding
        self.implementation = 'tiktoken:' + importlib.metadata.version('tiktoken')
        self.vocab_sha256 = _tiktoken_vocab_digest(self.encoder)

    def count(self, text: str) -> int:
        return len(self.encoder.encode(text, disallowed_special=()))


class SentencePieceCounter:
    def __init__(self, path: str):
        try:
            import sentencepiece
        except ImportError as e:
            raise RuntimeError('Install sentencepiece for a local .model tokenizer') from e
        p = Path(path)
        if not p.is_file():
            raise FileNotFoundError(p)
        self.encoder = sentencepiece.SentencePieceProcessor(model_file=str(p))
        self.name = p.name
        self.implementation = 'sentencepiece:' + importlib.metadata.version('sentencepiece')
        self.vocab_sha256 = hashlib.sha256(p.read_bytes()).hexdigest()

    def count(self, text: str) -> int:
        return len(self.encoder.encode(text))


class HFJsonCounter:
    def __init__(self, path: str):
        try:
            from tokenizers import Tokenizer as HFTokenizer
        except ImportError as e:
            raise RuntimeError('Install optional dependency tokenizers for local HuggingFace JSON files') from e
        p = Path(path)
        if not p.is_file():
            raise FileNotFoundError(p)
        self.encoder = HFTokenizer.from_file(str(p))
        self.name = p.name
        self.implementation = 'tokenizers:' + importlib.metadata.version('tokenizers')
        self.vocab_sha256 = hashlib.sha256(p.read_bytes()).hexdigest()

    def count(self, text: str) -> int:
        return len(self.encoder.encode(text).ids)
