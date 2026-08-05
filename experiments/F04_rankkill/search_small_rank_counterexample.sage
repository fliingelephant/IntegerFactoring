#!/usr/bin/env sage
"""Search the smallest semiprime in a finite box defeating F04 rank scans.

Candidates are ordered by N=pq.  A candidate is in the AKS hard regime only
when the standard preliminary gcd scan through r cannot already expose p or q,
so this script requires p,q>r.  It then exhausts all standard shifts and the
adjacent ceiling shift, comparing the two exact local gcd degrees.
"""

import argparse
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
                return modulus, order
    return None


def quotient_power(base, exponent, modulus):
    result = base.parent().one()
    while exponent:
        if exponent & 1:
            result = (result * base).mod(modulus)
        exponent >>= 1
        if exponent:
            base = (base * base).mod(modulus)
    return result


def degree_sequence(characteristic, cofactor, r, last_shift):
    ring = PolynomialRing(GF(characteristic), "y")
    y = ring.gen()
    modulus = y**r - 1
    assert gcd(modulus, modulus.derivative()) == 1
    sequence = []
    for a in range(1, last_shift + 1):
        error = quotient_power(y + ring(a), cofactor, modulus)
        error -= y ** (cofactor % r)
        error -= ring(a)
        sequence.append(int(gcd(error, modulus).degree()))
    return sequence


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-factor", type=int, required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    primes = [int(p) for p in prime_range(2, args.max_factor + 1)]
    pairs = sorted(
        (p * q, p, q)
        for i, p in enumerate(primes)
        for q in primes[i + 1 :]
    )
    parameter_candidates = []
    fully_scanned = []
    skipped_small_factor = 0
    started = time.monotonic()
    winner = None

    for n, p, q in pairs:
        threshold = math.log2(n) ** 2
        # ord_r(N) <= phi(r) <= r-1, so a hard-regime r<p can exist only
        # when p > threshold+1.
        if p <= threshold + 1:
            skipped_small_factor += 1
            continue
        selected = first_aks_r(n, p - 1)
        if selected is None:
            continue
        r, order = selected
        assert p > r and q > r
        shift_expression = math.sqrt(int(euler_phi(r))) * math.log2(n)
        floor_bound = math.floor(shift_expression)
        tested_bound = math.ceil(shift_expression)
        parameter_candidates.append(
            {
                "N": n,
                "p": p,
                "q": q,
                "r": r,
                "order": order,
                "threshold": threshold,
                "floor_shift_bound": floor_bound,
                "tested_through_ceiling": tested_bound,
            }
        )
        degrees_p = degree_sequence(p, q, r, tested_bound)
        degrees_q = degree_sequence(q, p, r, tested_bound)
        mismatches = [
            a
            for a, dp, dq in zip(
                range(1, tested_bound + 1), degrees_p, degrees_q
            )
            if dp != dq
        ]
        record = {
            **parameter_candidates[-1],
            "degree_distribution_mod_p": {
                str(d): degrees_p.count(d) for d in sorted(set(degrees_p))
            },
            "degree_distribution_mod_q": {
                str(d): degrees_q.count(d) for d in sorted(set(degrees_q))
            },
            "mismatch_shifts": mismatches,
            "degree_sequence_mod_p": degrees_p,
            "degree_sequence_mod_q": degrees_q,
        }
        fully_scanned.append(record)
        print(
            f"N={n} p={p} q={q} r={r} bound={tested_bound} "
            f"mismatches={len(mismatches)}",
            flush=True,
        )
        if not mismatches:
            winner = record
            break

    result = {
        "family": "F04_rankkill",
        "search_scope": {
            "distinct_prime_pairs": True,
            "both_factors_at_most": args.max_factor,
            "ordered_by_product": True,
            "hard_regime_requires_factors_exceed_r": True,
        },
        "pair_count_in_box": len(pairs),
        "skipped_by_necessary_small_factor_bound_before_winner": (
            skipped_small_factor
        ),
        "parameter_candidates_through_winner": parameter_candidates,
        "fully_scanned_through_winner": fully_scanned,
        "first_counterexample_in_enumerated_order": winner,
        "elapsed_seconds": time.monotonic() - started,
    }
    with open(args.output, "w") as handle:
        json.dump(result, handle, indent=2, default=int)
        handle.write("\n")


main()
