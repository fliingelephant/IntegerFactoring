#!/usr/bin/env python3
"""Independent reproduction of F13's named fixed probes.

Approach-family ID: F13_teichmuller_lift_audit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


INSTANCES = [
    (3, 5),
    (3, 7),
    (5, 7),
    (7, 11),
    (11, 13),
    (13, 17),
    (101, 103),
    (1009, 1013),
    (10007, 10009),
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def two_stage_factor(defect: int, n: int) -> int | None:
    first = math.gcd(defect, n)
    if 1 < first < n:
        return first
    if first == n:
        second = math.gcd(defect // n, n)
        if 1 < second < n:
            return second
    return None


def record(p: int, q: int) -> dict[str, object]:
    n = p * q
    modulus = n * n
    units = [value for value in range(1, min(n, 65)) if math.gcd(value, n) == 1]
    pairs = [(left, right) for left in units[:12] for right in units[:12]]

    additive_hits = []
    for left, right in pairs:
        defect = (
            pow((left + right) % modulus, n, modulus)
            - pow(left, n, modulus)
            - pow(right, n, modulus)
        ) % modulus
        divisor = two_stage_factor(defect, n)
        if divisor is not None:
            additive_hits.append([left, right, divisor])

    iterated_hits = []
    high_digit_hits = []
    for base in units:
        current = pow(base, n, modulus)
        for iteration in range(1, 4):
            next_value = pow(current, n, modulus)
            divisor = math.gcd(next_value - current, n)
            if 1 < divisor < n:
                iterated_hits.append([base, iteration, divisor])
            high_digit = (current - current % n) // n
            divisor = math.gcd(high_digit, n)
            if 1 < divisor < n:
                high_digit_hits.append([base, iteration, divisor])
            current = next_value

    rounded_exponent = math.isqrt(4 * n)
    if rounded_exponent * rounded_exponent < 4 * n:
        rounded_exponent += 1
    rounded_hits = []
    for base in units:
        lifted = pow(base, n, modulus)
        assert pow(lifted, n + 1, modulus) == pow(lifted, p + q, modulus)
        defect = (
            pow(lifted, n + 1, modulus)
            - pow(lifted, rounded_exponent, modulus)
        ) % modulus
        divisor = math.gcd(defect, n)
        if 1 < divisor < n:
            rounded_hits.append([base, divisor])

    return {
        "p": p,
        "q": q,
        "N": n,
        "bases": len(units),
        "pairs": len(pairs),
        "ceil_2_sqrt_N": rounded_exponent,
        "p_plus_q": p + q,
        "additive_hits": additive_hits,
        "iterated_hits": iterated_hits,
        "high_digit_hits": high_digit_hits,
        "rounded_hits": rounded_hits,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()

    records = [record(p, q) for p, q in INSTANCES]
    assert all(not item["rounded_hits"] for item in records)
    assert all(item["ceil_2_sqrt_N"] == item["p_plus_q"] for item in records)

    expected_large_counts = {
        10403: (2, 0, 4, 0),
        1022117: (0, 3, 2, 0),
        100160063: (0, 0, 0, 0),
    }
    for item in records[-3:]:
        actual = (
            len(item["additive_hits"]),
            len(item["iterated_hits"]),
            len(item["high_digit_hits"]),
            len(item["rounded_hits"]),
        )
        assert actual == expected_large_counts[item["N"]]

    source = Path(__file__).resolve()
    output = {
        "approach_family": "F13_teichmuller_lift_audit",
        "status": "PASS",
        "records": records,
        "source": str(source),
        "source_sha256": sha256(source),
    }
    Path(arguments.output).write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
