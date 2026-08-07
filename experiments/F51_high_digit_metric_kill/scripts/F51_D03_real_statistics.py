#!/usr/bin/env python3
"""Inspect canonical real moments and fixed interval statistics.

Finite discovery/certificate only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
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


def fraction_record(value: Fraction) -> dict[str, object]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "float": float(value),
    }


def summarize(values: list[int], modulus: int) -> dict[str, object]:
    count = len(values)
    mean = Fraction(sum(values), count)
    second = Fraction(sum(value * value for value in values), count)
    variance = second - mean * mean
    uniform_mean = Fraction(modulus - 1, 2)
    uniform_variance = Fraction(modulus * modulus - 1, 12)
    thresholds = {}
    for numerator, denominator in [(1, 4), (1, 3), (1, 2), (2, 3), (3, 4)]:
        cutoff = (numerator * modulus + denominator - 1) // denominator
        mass = Fraction(sum(value < cutoff for value in values), count)
        uniform_mass = Fraction(cutoff, modulus)
        thresholds[f"{numerator}/{denominator}"] = {
            "cutoff": cutoff,
            "mass": fraction_record(mass),
            "uniform_mass": fraction_record(uniform_mass),
            "signed_error": fraction_record(mass - uniform_mass),
        }
    return {
        "mean": fraction_record(mean),
        "mean_minus_uniform": fraction_record(mean - uniform_mean),
        "variance_over_N2": fraction_record(variance / (modulus * modulus)),
        "uniform_variance_over_N2": fraction_record(uniform_variance / (modulus * modulus)),
        "variance_error_over_N2": fraction_record((variance - uniform_variance) / (modulus * modulus)),
        "thresholds": thresholds,
    }


def inspect(p: int, q: int) -> dict[str, object]:
    modulus = p * q
    hs = []
    lambdas = []
    by_x = {}
    for a in range(1, modulus):
        if math.gcd(a, modulus) != 1:
            continue
        lifted = pow(a, modulus, modulus * modulus)
        x = lifted % modulus
        h = lifted // modulus
        lam = h * pow(x, -1, modulus) % modulus
        hs.append(h)
        lambdas.append(lam)
        by_x[x] = h
    assert len(by_x) == (p - 1) * (q - 1)
    for x, h in by_x.items():
        assert by_x[modulus - x] == modulus - 1 - h
    return {
        "p": p,
        "q": q,
        "N": modulus,
        "unit_count": len(hs),
        "reflection_law_checked": True,
        "h": summarize(hs, modulus),
        "lambda": summarize(lambdas, modulus),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    report = {
        "run": "F51-D03",
        "status": "PASS",
        "scope": "finite discovery/certificate only",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "pairs": [inspect(p, q) for p, q in PAIRS],
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "output": str(output), "pairs": len(PAIRS)}))


if __name__ == "__main__":
    main()
