#!/usr/bin/env python3
"""Exact finite scan of canonical exponent-N high-digit source laws.

This run is discovery and finite certificate evidence only.  It enumerates
uniform public units for small balanced semiprimes and records exact fibre,
collision, gcd-event, and one-dimensional interval-discrepancy statistics for
the canonical high digit h and its normalized residue lambda = h/x (mod N).
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import math
from pathlib import Path


PAIRS = [
    (3, 5),
    (5, 7),
    (7, 11),
    (11, 13),
    (13, 17),
    (17, 19),
    (29, 31),
    (41, 43),
    (59, 61),
    (101, 103),
    (137, 139),
    (211, 223),
]


def tv_numerator(counts: collections.Counter[int], sample_count: int, modulus: int) -> int:
    """Return numerator of TV with denominator 2*sample_count*modulus."""
    return sum(abs(counts.get(value, 0) * modulus - sample_count) for value in range(modulus))


def star_discrepancy_numerator(values: list[int], modulus: int) -> tuple[int, int]:
    """Return exact star discrepancy as numerator/(m*modulus)."""
    ordered = sorted(values)
    sample_count = len(ordered)
    maximum = 0
    for index, value in enumerate(ordered, start=1):
        maximum = max(
            maximum,
            index * modulus - value * sample_count,
            value * sample_count - (index - 1) * modulus,
        )
    return maximum, sample_count * modulus


def summarize(values: list[int], modulus: int) -> dict[str, object]:
    counts = collections.Counter(values)
    sample_count = len(values)
    collision_numerator = sum(count * count for count in counts.values())
    tv_num = tv_numerator(counts, sample_count, modulus)
    discrepancy_num, discrepancy_den = star_discrepancy_numerator(values, modulus)
    return {
        "support_size": len(counts),
        "missing_values": modulus - len(counts),
        "max_fibre": max(counts.values()),
        "fibre_histogram": dict(sorted(collections.Counter(counts.values()).items())),
        "collision_probability": {
            "numerator": collision_numerator,
            "denominator": sample_count * sample_count,
            "float": collision_numerator / (sample_count * sample_count),
        },
        "uniform_collision_probability": {
            "numerator": 1,
            "denominator": modulus,
            "float": 1 / modulus,
        },
        "tv_from_uniform": {
            "numerator": tv_num,
            "denominator": 2 * sample_count * modulus,
            "float": tv_num / (2 * sample_count * modulus),
        },
        "star_discrepancy": {
            "numerator": discrepancy_num,
            "denominator": discrepancy_den,
            "float": discrepancy_num / discrepancy_den,
        },
        "mean_over_modulus": {
            "numerator": sum(values),
            "denominator": sample_count * modulus,
            "float": sum(values) / (sample_count * modulus),
        },
    }


def inspect(p: int, q: int) -> dict[str, object]:
    modulus = p * q
    units = [a for a in range(1, modulus) if math.gcd(a, modulus) == 1]
    xs: list[int] = []
    hs: list[int] = []
    lambdas: list[int] = []
    joint_pairs: set[tuple[int, int]] = set()
    gcd_h = collections.Counter()
    gcd_lambda = collections.Counter()

    for a in units:
        lifted = pow(a, modulus, modulus * modulus)
        x = lifted % modulus
        h = lifted // modulus
        lam = h * pow(x, -1, modulus) % modulus
        xs.append(x)
        hs.append(h)
        lambdas.append(lam)
        joint_pairs.add((x, h))
        gcd_h[math.gcd(h, modulus)] += 1
        gcd_lambda[math.gcd(lam, modulus)] += 1

        # Local Teichmueller and canonical reconstruction checks.
        assert lifted % (p * p) == pow(x % p, p, p * p)
        assert lifted % (q * q) == pow(x % q, q, q * q)
        assert h % modulus == x * lam % modulus

    assert len(joint_pairs) == len(units)
    power_is_permutation = len(set(xs)) == len(units)
    assert power_is_permutation == (math.gcd(modulus, math.lcm(p - 1, q - 1)) == 1)

    return {
        "p": p,
        "q": q,
        "N": modulus,
        "unit_count": len(units),
        "balanced": p < q < 2 * p,
        "power_is_permutation": power_is_permutation,
        "x_support_size": len(set(xs)),
        "h": summarize(hs, modulus),
        "lambda": summarize(lambdas, modulus),
        "gcd_h_counts": dict(sorted(gcd_h.items())),
        "gcd_lambda_counts": dict(sorted(gcd_lambda.items())),
        "proper_gcd_h_probability": {
            "numerator": gcd_h[p] + gcd_h[q],
            "denominator": len(units),
            "float": (gcd_h[p] + gcd_h[q]) / len(units),
        },
        "proper_gcd_lambda_probability": {
            "numerator": gcd_lambda[p] + gcd_lambda[q],
            "denominator": len(units),
            "float": (gcd_lambda[p] + gcd_lambda[q]) / len(units),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report = {
        "run": "F51-D01",
        "status": "PASS",
        "scope": "finite discovery/certificate only",
        "source_sha256": source_hash,
        "pairs": [inspect(p, q) for p, q in PAIRS],
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "output": str(output), "pairs": len(PAIRS)}))


if __name__ == "__main__":
    main()
