#!/usr/bin/env python3
"""Enumerate F13 lift-map claims for small prime pairs.

This is an independent finite checker, not a proof.  It deliberately computes
the canonical base-N high digit exactly as specified in the task.
"""

from __future__ import annotations

import json
import math


def tau(value: int, modulus: int) -> int:
    return pow(value, modulus, modulus * modulus)


def high_digit(value: int, modulus: int) -> int:
    canonical = value % (modulus * modulus)
    low = canonical % modulus
    return ((canonical - low) // modulus) % modulus


def category(value: int, prime: int) -> int:
    if value % prime:
        return 0
    if value % (prime * prime):
        return 1
    return 2


def additive_counts(p: int, q: int) -> dict[str, list[int]]:
    modulus = p * q
    counts_p = [0, 0, 0]
    counts_q = [0, 0, 0]
    for x in range(1, p):
        defect = (pow(x + 1, modulus, p * p) - pow(x, modulus, p * p) - 1) % (p * p)
        counts_p[category(defect, p)] += 1
    for x in range(1, q):
        defect = (pow(x + 1, modulus, q * q) - pow(x, modulus, q * q) - 1) % (q * q)
        counts_q[category(defect, q)] += 1
    return {"p": counts_p, "q": counts_q}


def iterate_counts(p: int, q: int, comparisons: int = 3) -> list[dict[str, int]]:
    modulus = p * q
    units = [a for a in range(modulus) if math.gcd(a, modulus) == 1]
    states = [tau(a, modulus) for a in units]
    answer = []
    for index in range(1, comparisons + 1):
        next_states = [tau(value, modulus) for value in states]
        full_p = full_q = full_success = 0
        high_p = high_q = high_success = 0
        for value, next_value in zip(states, next_states, strict=True):
            difference = (next_value - value) % (modulus * modulus)
            equal_p = difference % (p * p) == 0
            equal_q = difference % (q * q) == 0
            full_p += equal_p
            full_q += equal_q
            full_success += equal_p != equal_q

            high_difference = (high_digit(next_value, modulus) - high_digit(value, modulus)) % modulus
            high_equal_p = high_difference % p == 0
            high_equal_q = high_difference % q == 0
            high_p += high_equal_p
            high_q += high_equal_q
            high_success += high_equal_p != high_equal_q
        answer.append(
            {
                "comparison": index,
                "unit_count": len(units),
                "full_equal_p": full_p,
                "full_equal_q": full_q,
                "full_success": full_success,
                "high_equal_p": high_p,
                "high_equal_q": high_q,
                "high_success": high_success,
            }
        )
        states = next_states
    return answer


def main() -> None:
    pairs = [(3, 5), (5, 7), (7, 11), (7, 13), (11, 13), (13, 17), (13, 19), (17, 19), (19, 23)]
    report = []
    for p, q in pairs:
        report.append(
            {
                "p": p,
                "q": q,
                "balanced": p < q < 2 * p,
                "additive_counts": additive_counts(p, q),
                "iterate_counts": iterate_counts(p, q),
            }
        )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
