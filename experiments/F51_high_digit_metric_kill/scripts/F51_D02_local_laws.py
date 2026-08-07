#!/usr/bin/env python3
"""Verify exact local carry laws and inspect hidden-factor marginals.

Finite discovery/certificate only. The exact assertions checked here are
proved separately in RESULT.md.
"""

from __future__ import annotations

import argparse
import collections
import cmath
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


def digit(unit: int, prime: int) -> int:
    return ((pow(unit, prime, prime * prime) - unit) // prime) % prime


def marginal_summary(values: list[int], prime: int) -> dict[str, object]:
    counts = collections.Counter(value % prime for value in values)
    total = len(values)
    collision_numerator = sum(count * count for count in counts.values())
    tv_numerator = sum(abs(prime * counts[residue] - total) for residue in range(prime))
    coefficients = []
    for frequency in range(1, prime):
        value = sum(
            count * cmath.exp(2j * math.pi * frequency * residue / prime)
            for residue, count in counts.items()
        ) / total
        coefficients.append((abs(value), frequency))
    maximum, maximizing_frequency = max(coefficients, default=(0.0, 0))
    parseval_nonzero = prime * collision_numerator / (total * total) - 1
    return {
        "count_min": min(counts.values()),
        "count_max": max(counts.values()),
        "max_point_probability": max(counts.values()) / total,
        "tv_from_uniform": tv_numerator / (2 * prime * total),
        "collision_probability": collision_numerator / (total * total),
        "nonzero_fourier_energy": parseval_nonzero,
        "max_nonzero_fourier_magnitude": maximum,
        "maximizing_frequency": maximizing_frequency,
    }


def inspect(p: int, q: int) -> dict[str, object]:
    modulus = p * q
    units = [x for x in range(1, modulus) if math.gcd(x, modulus) == 1]
    exponent_inverse = pow(modulus, -1, math.lcm(p - 1, q - 1))
    hs = []
    lambdas = []
    conditional_p_h = collections.Counter()
    conditional_p_lambda = collections.Counter()
    conditional_q_h = collections.Counter()
    conditional_q_lambda = collections.Counter()

    for x in units:
        a = pow(x, exponent_inverse, modulus)
        lifted = pow(a, modulus, modulus * modulus)
        assert lifted % modulus == x
        h = lifted // modulus
        lam = h * pow(x, -1, modulus) % modulus
        hs.append(h)
        lambdas.append(lam)

        u, k = x % p, x // p
        v, ell = x % q, x // q
        assert (q * h - (digit(u, p) - k)) % p == 0
        assert (q * u * lam - (digit(u, p) - k)) % p == 0
        assert (p * h - (digit(v, q) - ell)) % q == 0
        assert (p * v * lam - (digit(v, q) - ell)) % q == 0
        conditional_p_h[u, h % p] += 1
        conditional_p_lambda[u, lam % p] += 1
        conditional_q_h[v, h % q] += 1
        conditional_q_lambda[v, lam % q] += 1

    assert max(conditional_p_h.values()) <= 2
    assert max(conditional_p_lambda.values()) <= 2
    assert max(conditional_q_h.values()) <= 1
    assert max(conditional_q_lambda.values()) <= 1

    return {
        "p": p,
        "q": q,
        "N": modulus,
        "unit_count": len(units),
        "conditional_fibre_maxima": {
            "h_mod_p_given_x_mod_p": max(conditional_p_h.values()),
            "lambda_mod_p_given_x_mod_p": max(conditional_p_lambda.values()),
            "h_mod_q_given_x_mod_q": max(conditional_q_h.values()),
            "lambda_mod_q_given_x_mod_q": max(conditional_q_lambda.values()),
        },
        "h_mod_p": marginal_summary(hs, p),
        "h_mod_q": marginal_summary(hs, q),
        "lambda_mod_p": marginal_summary(lambdas, p),
        "lambda_mod_q": marginal_summary(lambdas, q),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    report = {
        "run": "F51-D02",
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
