#!/usr/bin/env python3

import argparse
import json
import math
import time
from collections import Counter, defaultdict
from fractions import Fraction


R_BANK = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)


def primes_upto(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for x in range(2, math.isqrt(limit) + 1):
        if sieve[x]:
            sieve[x * x : limit + 1 : x] = b"\x00" * (((limit - x * x) // x) + 1)
    return [x for x in range(2, limit + 1) if sieve[x]]


def add_term(vector, exponent, value, modulus):
    vector[exponent % len(vector)] = (vector[exponent % len(vector)] + value) % modulus


def h_vector(m, a, ell, r):
    vector = [0] * r
    for j in range(1, m):
        add_term(vector, j, math.comb(m, j) * pow(a, m - j, ell), ell)
    return vector


def e_vector_local(other_prime, a, ell, r):
    source = h_vector(other_prime, a, ell, r)
    target = [0] * r
    for j, value in enumerate(source):
        target[(ell * j) % r] = value
    return target


def fast_p_vector(p, q, a, r):
    d = q - p
    source = [0] * r
    for j in range(d):
        coefficient = math.comb(d, j) * pow(a, d - j, p)
        add_term(source, p + j, coefficient, p)
    for j in range(1, d + 1):
        coefficient = math.comb(d, j) * pow(a, d - j + 1, p)
        add_term(source, j, coefficient, p)
    target = [0] * r
    for j, value in enumerate(source):
        target[(p * j) % r] = value
    return target


def masks_for_all_shifts(m, ell, valid_rs):
    binomials = [math.comb(m, j) % ell for j in range(m + 1)]
    masks = {r: [0] * ell for r in valid_rs}
    supports = {r: [] for r in valid_rs}
    for a in range(1, ell):
        vectors = {r: [0] * r for r in valid_rs}
        power = pow(a, m - 1, ell)
        inverse = pow(a, -1, ell)
        for j in range(1, m):
            coefficient = binomials[j] * power % ell
            for r in valid_rs:
                vectors[r][j % r] = (vectors[r][j % r] + coefficient) % ell
            power = power * inverse % ell
        for r in valid_rs:
            permuted = [0] * r
            for j, value in enumerate(vectors[r]):
                permuted[(ell * j) % r] = value
            mask = sum(1 << j for j, value in enumerate(permuted) if value == 0)
            masks[r][a] = mask
            supports[r].append(r - mask.bit_count())
    return masks, supports


def fast_p_masks_for_all_shifts(p, q, valid_rs):
    d = q - p
    binomials = [math.comb(d, j) % p for j in range(d + 1)]
    masks = {r: [0] * p for r in valid_rs}
    supports = {r: [] for r in valid_rs}
    for a in range(1, p):
        vectors = {r: [0] * r for r in valid_rs}
        powers = [1] * (d + 2)
        for exponent in range(1, d + 2):
            powers[exponent] = powers[exponent - 1] * a % p
        for j in range(d):
            coefficient = binomials[j] * powers[d - j] % p
            for r in valid_rs:
                index = (p + j) % r
                vectors[r][index] = (vectors[r][index] + coefficient) % p
        for j in range(1, d + 1):
            coefficient = binomials[j] * powers[d - j + 1] % p
            for r in valid_rs:
                vectors[r][j % r] = (vectors[r][j % r] + coefficient) % p
        for r in valid_rs:
            permuted = [0] * r
            for j, value in enumerate(vectors[r]):
                permuted[(p * j) % r] = value
            mask = sum(1 << j for j, value in enumerate(permuted) if value == 0)
            masks[r][a] = mask
            supports[r].append(r - mask.bit_count())
    return masks, supports


def validate():
    for p, q in ((5, 7), (7, 11), (11, 13), (13, 19)):
        for r in (3, 5, 7):
            if math.gcd(r, p * q) != 1:
                continue
            for a in range(1, p * q):
                if math.gcd(a, p * q) != 1:
                    continue
                assert fast_p_vector(p, q, a % p, r) == e_vector_local(q, a % p, p, r)
                direct_p = [0] * r
                direct_q = [0] * r
                n = p * q
                for j in range(1, n):
                    coefficient = math.comb(n, j)
                    add_term(direct_p, j, coefficient * pow(a, n - j, p), p)
                    add_term(direct_q, j, coefficient * pow(a, n - j, q), q)
                assert direct_p == fast_p_vector(p, q, a % p, r)
                assert direct_q == e_vector_local(p, a % q, q, r)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--p-limit", type=int, default=500)
    args = parser.parse_args()

    started = time.time()
    validate()
    primes = primes_upto(2 * args.p_limit + 100)
    rows = []
    aggregates = defaultdict(list)

    for index, p in enumerate(primes[:-1]):
        if p < 5 or p > args.p_limit:
            continue
        q = primes[index + 1]
        if q >= 2 * p:
            continue
        n = p * q
        d = q - p
        valid_rs = [r for r in R_BANK if math.gcd(r, n) == 1]
        p_masks, p_supports = fast_p_masks_for_all_shifts(p, q, valid_rs)
        q_masks, q_supports = masks_for_all_shifts(p, q, valid_rs)
        for r in valid_rs:
            denominator = (p - 1) * (q - 1)
            p_counts = Counter(p_masks[r][1:])
            q_counts = Counter(q_masks[r][1:])
            synchronized = sum(count * q_counts.get(mask, 0) for mask, count in p_counts.items())
            successes = denominator - synchronized
            first_success = None
            if successes:
                for a in range(1, n):
                    if a % p and a % q and p_masks[r][a % p] != q_masks[r][a % q]:
                        first_success = a
                        break
            probability = Fraction(successes, denominator)
            row = {
                "p": p,
                "q": q,
                "N": n,
                "gap": d,
                "r": r,
                "successes": successes,
                "unit_shifts": denominator,
                "probability_numerator": probability.numerator,
                "probability_denominator": probability.denominator,
                "probability_float": float(probability),
                "first_success_shift": first_success,
                "all_synchronized": successes == 0,
                "p_support_min": min(p_supports[r]),
                "p_support_max": max(p_supports[r]),
                "p_support_mean": sum(p_supports[r]) / (p - 1),
                "q_support_min": min(q_supports[r]),
                "q_support_max": max(q_supports[r]),
                "q_support_mean": sum(q_supports[r]) / (q - 1),
            }
            rows.append(row)
            aggregates[(d, r)].append(row)

    summaries = []
    for (gap, r), group in sorted(aggregates.items()):
        minimum = min(group, key=lambda row: (row["probability_float"], row["p"]))
        maximum = max(group, key=lambda row: (row["probability_float"], -row["p"]))
        zeros = [row for row in group if row["successes"] == 0]
        summaries.append({
            "gap": gap,
            "r": r,
            "rows": len(group),
            "minimum": {"p": minimum["p"], "q": minimum["q"], "numerator": minimum["probability_numerator"], "denominator": minimum["probability_denominator"]},
            "maximum": {"p": maximum["p"], "q": maximum["q"], "numerator": maximum["probability_numerator"], "denominator": maximum["probability_denominator"]},
            "zero_rows": len(zeros),
            "largest_zero_p": max((row["p"] for row in zeros), default=None),
        })

    by_r = []
    for r in R_BANK:
        group = [row for row in rows if row["r"] == r]
        if not group:
            continue
        minimum = min(group, key=lambda row: (row["probability_float"], row["p"]))
        by_r.append({
            "r": r,
            "rows": len(group),
            "minimum_probability": {"p": minimum["p"], "q": minimum["q"], "numerator": minimum["probability_numerator"], "denominator": minimum["probability_denominator"]},
            "zero_rows": sum(row["successes"] == 0 for row in group),
        })

    positive_rs = [entry["r"] for entry in by_r if entry["zero_rows"] == 0]
    if positive_rs:
        verdict = "finite_positive_lower_envelope_lead"
    else:
        verdict = "each_fixed_r_has_finite_null"

    output = {
        "run_id": "F222-D01",
        "status": "complete",
        "verdict": verdict,
        "elapsed_seconds": time.time() - started,
        "p_limit": args.p_limit,
        "r_bank": list(R_BANK),
        "validation": "passed",
        "row_count": len(rows),
        "by_r": by_r,
        "positive_lower_envelope_r_values": positive_rs,
        "by_gap_and_r": summaries,
        "rows": rows,
    }
    with open(args.output, "w", encoding="utf-8") as stream:
        json.dump(output, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({key: output[key] for key in ("run_id", "status", "verdict", "elapsed_seconds", "row_count")}, sort_keys=True))


if __name__ == "__main__":
    main()
