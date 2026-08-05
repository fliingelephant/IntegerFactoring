#!/usr/bin/env sage
"""Exhaust the complete local-shift distributions for N=271*293."""

import argparse
import json
import time


P = 271
Q = 293
R = 269


def quotient_power(base, exponent, modulus):
    result = base.parent().one()
    while exponent:
        if exponent & 1:
            result = (result * base).mod(modulus)
        exponent >>= 1
        if exponent:
            base = (base * base).mod(modulus)
    return result


def scan(characteristic, cofactor):
    ring = PolynomialRing(GF(characteristic), "y")
    y = ring.gen()
    modulus = y**R - 1
    degrees = []
    exceptions = []
    for a in range(characteristic):
        error = quotient_power(y + ring(a), cofactor, modulus)
        error -= y ** (cofactor % R)
        error -= ring(a)
        degree = int(gcd(error, modulus).degree())
        degrees.append(degree)
        if degree:
            exceptions.append({"a": a, "degree": degree})
    return {
        "characteristic": characteristic,
        "cofactor": cofactor,
        "degree_distribution": {
            str(d): degrees.count(d) for d in sorted(set(degrees))
        },
        "positive_residues": exceptions,
        "degree_sequence": degrees,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    started = time.monotonic()
    scan_p = scan(P, Q)
    scan_q = scan(Q, P)
    mismatch_pairs = sum(
        count_p * count_q
        for degree_p, count_p in (
            (int(degree), count)
            for degree, count in scan_p["degree_distribution"].items()
        )
        for degree_q, count_q in (
            (int(degree), count)
            for degree, count in scan_q["degree_distribution"].items()
        )
        if degree_p != degree_q
    )
    result = {
        "family": "F04_rankkill",
        "N": P * Q,
        "r": R,
        "scan_mod_p": scan_p,
        "scan_mod_q": scan_q,
        "uniform_crt_shift_rank_mismatch_count": mismatch_pairs,
        "uniform_crt_shift_total": P * Q,
        "uniform_crt_shift_rank_mismatch_probability_exact": (
            f"{mismatch_pairs}/{P * Q}"
        ),
        "uniform_crt_shift_rank_mismatch_probability_float": (
            float(mismatch_pairs) / float(P * Q)
        ),
        "elapsed_seconds": time.monotonic() - started,
    }
    with open(args.output, "w") as handle:
        json.dump(result, handle, indent=2, default=int)
        handle.write("\n")


main()
