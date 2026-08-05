#!/usr/bin/env sage
"""Exact F04 rank-separator scan on a specified semiprime.

For N=pq, this computes for every requested AKS shift a the two nullities

  deg gcd((Y+a)^q-Y^q-a, Y^r-1) over F_p,
  deg gcd((Y+a)^p-Y^p-a, Y^r-1) over F_q.

They equal the local nullities of multiplication by the global AKS error
H_a in F_p[X]/(X^r-1) and F_q[X]/(X^r-1), respectively, because
X -> X^p (respectively X -> X^q) is an algebra automorphism whenever
gcd(p,r)=gcd(q,r)=1.
"""

import argparse
import hashlib
import json
import math
import time


def exact_order(value, modulus):
    residue = 1
    for exponent in range(1, modulus + 1):
        residue = residue * (value % modulus) % modulus
        if residue == 1:
            return exponent
    raise AssertionError("multiplicative order exceeded modulus")


def first_aks_r(n, maximum):
    threshold = math.log2(n) ** 2
    for modulus in range(2, maximum + 1):
        if math.gcd(n, modulus) == 1:
            order = exact_order(n, modulus)
            if order > threshold:
                return modulus, order, threshold
    raise RuntimeError("no qualifying r in requested range")


def quotient_power(base, exponent, modulus):
    result = base.parent().one()
    while exponent:
        if exponent & 1:
            result = (result * base).mod(modulus)
        exponent >>= 1
        if exponent:
            base = (base * base).mod(modulus)
    return result


def scan_field(characteristic, cofactor, r, first_shift, last_shift):
    ring = PolynomialRing(GF(characteristic), "y")
    y = ring.gen()
    modulus = y**r - 1
    assert gcd(modulus, modulus.derivative()) == 1

    cyclotomic_order = exact_order(characteristic, r)
    expected_factor_degrees = [1] + [cyclotomic_order] * (
        (r - 1) // cyclotomic_order
    )
    actual_factor_degrees = sorted(
        [int(factor.degree()) for factor, multiplicity in modulus.factor()]
    )
    assert actual_factor_degrees == sorted(expected_factor_degrees)

    digest = hashlib.sha256()
    distribution = {}
    positive = []
    degrees = []
    started = time.monotonic()
    for a in range(first_shift, last_shift + 1):
        error = quotient_power(y + ring(a), cofactor, modulus)
        error -= y ** (cofactor % r)
        error -= ring(a)
        divisor = gcd(error, modulus)
        degree = int(divisor.degree())
        degrees.append(degree)
        digest.update(degree.to_bytes(4, "big"))
        distribution[str(degree)] = distribution.get(str(degree), 0) + 1
        if degree:
            positive.append(
                {
                    "a": a,
                    "gcd_degree": degree,
                    "gcd": str(divisor),
                }
            )
        if a % 100 == 0 or a == last_shift:
            print(
                f"characteristic={characteristic} shift={a}/{last_shift} "
                f"positive={len(positive)}",
                flush=True,
            )

    return {
        "characteristic": characteristic,
        "cofactor": cofactor,
        "characteristic_mod_r": characteristic % r,
        "gcd_characteristic_r": math.gcd(characteristic, r),
        "modulus_squarefree": True,
        "order_characteristic_mod_r": cyclotomic_order,
        "factor_degrees_xr_minus_1": actual_factor_degrees,
        "first_shift": first_shift,
        "last_shift": last_shift,
        "shift_count": last_shift - first_shift + 1,
        "gcd_degree_distribution": distribution,
        "positive_gcds": positive,
        "degree_sequence": degrees,
        "degree_sequence_sha256": digest.hexdigest(),
        "digest_encoding": "a increasing, gcd degree uint32 big-endian",
        "elapsed_seconds": time.monotonic() - started,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=int, required=True)
    parser.add_argument("--q", type=int, required=True)
    parser.add_argument("--max-r", type=int, default=10000)
    parser.add_argument("--first-shift", type=int, default=1)
    parser.add_argument("--last-shift", type=int)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    p, q = sorted((args.p, args.q))
    assert p != q and is_prime(p) and is_prime(q)
    n = p * q
    r, order, threshold = first_aks_r(n, args.max_r)
    phi_r = int(euler_phi(r))
    shift_expression = math.sqrt(phi_r) * math.log2(n)
    floor_shift_bound = math.floor(shift_expression)
    last_shift = args.last_shift or floor_shift_bound
    assert args.first_shift >= 1 and last_shift >= args.first_shift
    assert math.gcd(p, r) == math.gcd(q, r) == 1

    total_started = time.monotonic()
    scan_mod_p = scan_field(p, q, r, args.first_shift, last_shift)
    scan_mod_q = scan_field(q, p, r, args.first_shift, last_shift)
    mismatch_shifts = [
        a
        for a, dp, dq in zip(
            range(args.first_shift, last_shift + 1),
            scan_mod_p["degree_sequence"],
            scan_mod_q["degree_sequence"],
        )
        if dp != dq
    ]

    result = {
        "family": "F04_rankkill",
        "N": n,
        "p": p,
        "q": q,
        "product_verified": p * q == n,
        "factors_prime": True,
        "r": r,
        "order_N_mod_r": order,
        "log2_N_squared": threshold,
        "phi_r": phi_r,
        "shift_expression": shift_expression,
        "standard_floor_shift_bound": floor_shift_bound,
        "tested_first_shift": args.first_shift,
        "tested_last_shift": last_shift,
        "p_and_q_exceed_r": p > r and q > r,
        "scan_mod_p": scan_mod_p,
        "scan_mod_q": scan_mod_q,
        "unequal_local_degree_shifts": mismatch_shifts,
        "unequal_local_degree_count": len(mismatch_shifts),
        "elapsed_seconds": time.monotonic() - total_started,
    }
    with open(args.output, "w") as handle:
        json.dump(result, handle, indent=2, default=int)
        handle.write("\n")


main()
