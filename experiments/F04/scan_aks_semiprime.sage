#!/usr/bin/env sage
"""Compact exhaustive AKS-localization scan for one known semiprime.

The known factors are inputs only to classify CRT support.  This is finite
counterexample discovery/certification code, not a factoring algorithm.
"""

import argparse
import json
import math
import time


def aks_r(n, max_r):
    threshold = math.log2(n) ** 2
    for r in range(2, max_r + 1):
        if math.gcd(n, r) == 1 and Mod(n, r).multiplicative_order() > threshold:
            return r, int(Mod(n, r).multiplicative_order())
    raise RuntimeError(f"no AKS r <= {max_r}")


def semiprime_error_coefficients(r, a, characteristic, cofactor):
    """Return H_{r,a} mod characteristic using Frobenius localization.

    For N=characteristic*cofactor, H_N(X) is h_cofactor(X^characteristic),
    where h_m(Y)=(Y+a)^m-Y^m-a.  Since gcd(characteristic,r)=1 in the
    AKS stage, substitution permutes the r coefficient positions.
    """
    ring = PolynomialRing(GF(characteristic), "x")
    x = ring.gen()
    modulus = x**r - 1
    error = power_mod(x + ring(a), cofactor, modulus)
    error -= power_mod(x, cofactor, modulus)
    error -= ring(a)
    coefficients = [0] * r
    for j in range(r):
        coefficients[(characteristic * j) % r] = int(error[j])
    return coefficients


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=int, required=True)
    parser.add_argument("--q", type=int, required=True)
    parser.add_argument("--max-r", type=int, default=10000)
    parser.add_argument("--shift-limit", type=int)
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--exceptions-only", action="store_true")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    requested_q = args.q
    generated_q = int(previous_prime(2 * args.p)) if requested_q == 0 else requested_q
    p, q = sorted((args.p, generated_q))
    assert is_prime(p) and is_prime(q) and p != q
    n = p * q
    r, order = aks_r(n, args.max_r)
    shift_bound = math.floor(math.sqrt(euler_phi(r)) * math.log2(n))
    tested_bound = min(shift_bound, args.shift_limit or shift_bound)
    start = time.monotonic()
    records = []
    total_separators = 0
    total_zero_mod_p = 0
    total_zero_mod_q = 0
    total_zero_both = 0
    any_pass_fail = False
    for a in range(1, tested_bound + 1):
        coefficients_p = semiprime_error_coefficients(r, a, p, q)
        coefficients_q = semiprime_error_coefficients(r, a, q, p)
        separator_positions = [
            j
            for j, (cp, cq) in enumerate(zip(coefficients_p, coefficients_q))
            if (cp == 0) != (cq == 0)
        ]
        local_zero = [not any(coefficients_p), not any(coefficients_q)]
        zero_mod_p = sum(cp == 0 for cp in coefficients_p)
        zero_mod_q = sum(cq == 0 for cq in coefficients_q)
        zero_both = sum(
            cp == 0 and cq == 0
            for cp, cq in zip(coefficients_p, coefficients_q)
        )
        any_pass_fail |= local_zero[0] != local_zero[1]
        total_separators += len(separator_positions)
        total_zero_mod_p += zero_mod_p
        total_zero_mod_q += zero_mod_q
        total_zero_both += zero_both
        record = {
            "a": a,
            "local_zero_mod_p": local_zero[0],
            "local_zero_mod_q": local_zero[1],
            "zero_count_mod_p": zero_mod_p,
            "zero_count_mod_q": zero_mod_q,
            "zero_count_both": zero_both,
            "separator_count": len(separator_positions),
            "first_separator_position": (
                separator_positions[0] if separator_positions else None
            ),
        }
        if not args.exceptions_only or separator_positions or any(local_zero):
            records.append(record)
        if not args.quiet:
            print(
                f"a={a}/{tested_bound} pass=({local_zero[0]},{local_zero[1]}) "
                f"zeros=({zero_mod_p},{zero_mod_q},{zero_both}) "
                f"separators={len(separator_positions)}"
            )

    output = {
        "N": n,
        "p": p,
        "q": q,
        "q_generation": (
            "previous_prime(2*p)" if requested_q == 0 else "explicit"
        ),
        "r": r,
        "order": order,
        "log2_squared": math.log2(n) ** 2,
        "phi_r": int(euler_phi(r)),
        "shift_bound": shift_bound,
        "tested_shift_bound": tested_bound,
        "aks_trial_gcd_would_stop": p <= r,
        "any_pass_fail": any_pass_fail,
        "total_coefficients": tested_bound * r,
        "total_zero_mod_p": total_zero_mod_p,
        "total_zero_mod_q": total_zero_mod_q,
        "total_zero_both": total_zero_both,
        "total_separator_positions": total_separators,
        "elapsed_seconds": time.monotonic() - start,
        "shifts": records,
    }
    with open(args.output, "w") as handle:
        json.dump(output, handle, indent=2, default=int)
        handle.write("\n")


main()
