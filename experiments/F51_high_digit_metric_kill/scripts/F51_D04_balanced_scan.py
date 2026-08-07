#!/usr/bin/env python3
"""Adversarial finite scan of interval discrepancy on balanced semiprimes."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def primes_through(limit: int) -> list[int]:
    answer = []
    for value in range(3, limit + 1, 2):
        if all(value % divisor for divisor in range(3, math.isqrt(value) + 1, 2)):
            answer.append(value)
    return answer


def star_discrepancy(values: list[int], modulus: int) -> float:
    values.sort()
    count = len(values)
    maximum = 0
    for index, value in enumerate(values, start=1):
        maximum = max(
            maximum,
            index * modulus - value * count,
            value * count - (index - 1) * modulus,
        )
    return maximum / (count * modulus)


def inspect(p: int, q: int) -> dict[str, object]:
    modulus = p * q
    hs = []
    lambdas = []
    for a in range(1, modulus):
        if math.gcd(a, modulus) != 1:
            continue
        lifted = pow(a, modulus, modulus * modulus)
        x = lifted % modulus
        h = lifted // modulus
        hs.append(h)
        lambdas.append(h * pow(x, -1, modulus) % modulus)
    h_discrepancy = star_discrepancy(hs, modulus)
    lambda_discrepancy = star_discrepancy(lambdas, modulus)
    return {
        "p": p,
        "q": q,
        "N": modulus,
        "h_discrepancy": h_discrepancy,
        "lambda_discrepancy": lambda_discrepancy,
        "h_scaled_by_p_minus_1": h_discrepancy * (p - 1),
        "lambda_scaled_by_p_minus_1": lambda_discrepancy * (p - 1),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--limit", type=int, default=101)
    args = parser.parse_args()
    primes = primes_through(2 * args.limit)
    rows = []
    for p in primes:
        if p > args.limit:
            break
        for q in primes:
            if p < q < 2 * p:
                rows.append(inspect(p, q))
    output = Path(args.output)
    report = {
        "run": "F51-D04",
        "status": "PASS",
        "scope": "finite discovery/certificate only",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "limit": args.limit,
        "pair_count": len(rows),
        "max_h_scaled": max(rows, key=lambda row: row["h_scaled_by_p_minus_1"]),
        "max_lambda_scaled": max(rows, key=lambda row: row["lambda_scaled_by_p_minus_1"]),
        "rows": rows,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "output": str(output), "pairs": len(rows)}))


if __name__ == "__main__":
    main()
