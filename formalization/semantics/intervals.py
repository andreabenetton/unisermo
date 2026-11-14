"""Exact Allen relations for bounded positive-duration temporal intervals.

This is independent of natural-language truth or event-reference resolution.
The parser exposes an abstract temporal relation; this utility verifies
concrete interval configurations only when endpoints have been supplied.
"""

from __future__ import annotations


def allen_relation(a_start, a_end, b_start, b_end) -> str:
    """Return the unique Allen relation of interval A relative to B.

    Endpoint values must share a strictly ordered comparable type.
    Zero-duration, reversed, incomparable or unbounded intervals are rejected.
    """
    try:
        if not a_start < a_end or not b_start < b_end:
            raise ValueError("Allen intervals must have positive duration")
        if a_end < b_start:
            return "before"
        if a_end == b_start:
            return "meets"
        if a_start < b_start < a_end < b_end:
            return "overlaps"
        if a_start == b_start and a_end < b_end:
            return "starts"
        if b_start < a_start and a_end < b_end:
            return "during"
        if b_start < a_start and a_end == b_end:
            return "finishes"
        if a_start == b_start and a_end == b_end:
            return "equals"
        if a_start < b_start and a_end == b_end:
            return "finished_by"
        if a_start < b_start and b_end < a_end:
            return "contains"
        if a_start == b_start and b_end < a_end:
            return "started_by"
        if b_start < a_start < b_end < a_end:
            return "overlapped_by"
        if b_end == a_start:
            return "met_by"
        if b_end < a_start:
            return "after"
    except TypeError as exc:
        raise ValueError("incomparable temporal endpoints") from exc
    raise ValueError("no Allen relation for supplied intervals")
