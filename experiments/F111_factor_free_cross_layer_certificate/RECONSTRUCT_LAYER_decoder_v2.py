#!/usr/bin/env python3
"""Versioned correction to the independent frozen-layer decoder.

Version 1 built and validated the exact gcd basis, but its nullspace routine
inserted echelon rows before removing lower pivot columns.  This file keeps
the entire version-1 replay and replaces only that binary-linear-algebra step.
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import RECONSTRUCT_LAYER_decoder_v1 as decoder


def row_reduce_and_kernel(rows: list[int], column_count: int) -> tuple[dict[int, int], list[int]]:
    """Return reduced pivot rows and a canonical full nullspace basis."""
    pivots: dict[int, int] = {}
    for source_row in rows:
        row = source_row
        for pivot in sorted(pivots, reverse=True):
            if (row >> pivot) & 1:
                row ^= pivots[pivot]
        if row:
            pivots[row.bit_length() - 1] = row

    # Echelon rows can contain lower pivot columns.  Clear them from low to
    # high so each row becomes reduced before it is used on higher rows.
    ordered_pivots = sorted(pivots)
    for pivot in ordered_pivots:
        pivot_row = pivots[pivot]
        for higher_pivot in ordered_pivots:
            if higher_pivot > pivot and ((pivots[higher_pivot] >> pivot) & 1):
                pivots[higher_pivot] ^= pivot_row

    free_columns = [index for index in range(column_count) if index not in pivots]
    kernel = []
    for free_column in free_columns:
        vector = 1 << free_column
        for pivot, row in pivots.items():
            if (row >> free_column) & 1:
                vector |= 1 << pivot
        kernel.append(vector)
    return pivots, kernel


decoder.row_reduce_and_kernel = row_reduce_and_kernel


if __name__ == "__main__":
    raise SystemExit(decoder.main())
