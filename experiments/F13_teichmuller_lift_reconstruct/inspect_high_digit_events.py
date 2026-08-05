#!/usr/bin/env python3
"""Inspect directional canonical-high-digit separation events."""

from __future__ import annotations

import collections
import json
import math


def tau(value: int, modulus: int) -> int:
    return pow(value, modulus, modulus * modulus)


def high_digit(value: int, modulus: int) -> int:
    value %= modulus * modulus
    return (value - value % modulus) // modulus


def inspect(p: int, q: int) -> dict[str, object]:
    modulus = p * q
    p_only_by_x: collections.Counter[int] = collections.Counter()
    q_only_by_y: collections.Counter[int] = collections.Counter()
    p_only_rows = []
    q_only_rows = []
    for a in range(modulus):
        if math.gcd(a, modulus) != 1:
            continue
        first = tau(a, modulus)
        second = tau(first, modulus)
        difference = (high_digit(second, modulus) - high_digit(first, modulus)) % modulus
        equal_p = difference % p == 0
        equal_q = difference % q == 0
        x = first % p
        y = first % q
        if equal_p and not equal_q:
            p_only_by_x[x] += 1
            p_only_rows.append((x, y, first % modulus, high_digit(first, modulus), high_digit(second, modulus)))
        if equal_q and not equal_p:
            q_only_by_y[y] += 1
            q_only_rows.append((x, y, first % modulus, high_digit(first, modulus), high_digit(second, modulus)))
    return {
        "p": p,
        "q": q,
        "p_only_count": len(p_only_rows),
        "q_only_count": len(q_only_rows),
        "max_p_only_per_x": max(p_only_by_x.values(), default=0),
        "max_q_only_per_y": max(q_only_by_y.values(), default=0),
        "p_only_by_x": dict(sorted(p_only_by_x.items())),
        "q_only_by_y": dict(sorted(q_only_by_y.items())),
        "p_only_rows": p_only_rows,
        "q_only_rows": q_only_rows,
    }


def main() -> None:
    print(json.dumps([inspect(7, 13), inspect(13, 17), inspect(17, 19), inspect(19, 23)], indent=2))


if __name__ == "__main__":
    main()
