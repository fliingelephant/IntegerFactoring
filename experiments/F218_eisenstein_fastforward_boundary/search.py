#!/usr/bin/env python3
"""F218-D01 deterministic affine-Cartier and theta isolation search."""

from argparse import ArgumentParser
from array import array
from hashlib import sha256
from itertools import product
import json
from math import isqrt
import platform
import sys
import time


def build_spf(limit):
    spf = array("I", [0]) * (limit + 1)
    for prime in range(2, isqrt(limit) + 1):
        if spf[prime]:
            continue
        for multiple in range(prime * prime, limit + 1, prime):
            if not spf[multiple]:
                spf[multiple] = prime
    return spf


def factor_from_spf(value, spf):
    factors = []
    while value > 1:
        prime = spf[value] or value
        exponent = 0
        while value % prime == 0:
            value //= prime
            exponent += 1
        factors.append((int(prime), exponent))
    return factors


def sigma_from_factors(factors):
    total = 1
    for prime, exponent in factors:
        total *= (prime ** (exponent + 1) - 1) // (prime - 1)
    return total


def r_two_from_factors(factors):
    total = 4
    for prime, exponent in factors:
        if prime % 4 == 3 and exponent % 2:
            return 0
        if prime % 4 == 1:
            total *= exponent + 1
    return total


def fermat_quotient(base, prime):
    residue = pow(base, prime - 1, prime * prime)
    return ((residue - 1) // prime) % prime


def determinant_mod(matrix, prime):
    work = [[entry % prime for entry in row] for row in matrix]
    determinant = 1
    size = len(work)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column]), None
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = -determinant
        pivot_value = work[column][column]
        determinant = determinant * pivot_value % prime
        inverse = pow(pivot_value, -1, prime)
        for row in range(column + 1, size):
            multiplier = work[row][column] * inverse % prime
            if not multiplier:
                continue
            for index in range(column, size):
                work[row][index] = (
                    work[row][index] - multiplier * work[column][index]
                ) % prime
    return determinant % prime


def canonical_digest(rows):
    payload = "\n".join(
        json.dumps(row, sort_keys=True, separators=(",", ":")) for row in rows
    )
    return sha256(payload.encode()).hexdigest()


def filter_bank(rows, bounds, augmented):
    candidates = list(product(range(-bounds, bounds + 1), repeat=4 if augmented else 2))
    audit_rows = []
    counts = [len(candidates)]
    for row in rows:
        prime = row["r"]
        if augmented:
            candidates = [
                candidate
                for candidate in candidates
                if (
                    candidate[0] * row["u"]
                    + candidate[1]
                    + candidate[2] * row["q2"]
                    + candidate[3] * row["q3"]
                    - row["t"]
                )
                % prime
                == 0
            ]
        else:
            candidates = [
                candidate
                for candidate in candidates
                if (candidate[0] * row["u"] + candidate[1] - row["t"])
                % prime
                == 0
            ]
        audit_rows.append(row)
        counts.append(len(candidates))
        if not candidates:
            break
    return {
        "audit_rows": audit_rows,
        "candidate_counts": counts,
        "survivors": [list(candidate) for candidate in candidates],
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--r-max", type=int, default=2_000_000)
    parser.add_argument("--bm-r-max", type=int, default=200_000)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    started = time.time()
    sieve_limit = max(2 * args.r_max + 1, 17 * args.bm_r_max + 1)
    spf = build_spf(sieve_limit)

    rows = []
    theta_zero_count = 0
    theta_first_nonzero = None
    for prime in range(5, args.r_max + 1):
        if spf[prime]:
            continue
        target = 2 * prime + 1
        target_factor = spf[target]
        if not target_factor:
            continue
        other_factor = target // target_factor
        if (
            target_factor == other_factor
            or spf[other_factor]
            or not target_factor < other_factor < 2 * target_factor
        ):
            continue

        target_factors = [(int(target_factor), 1), (int(other_factor), 1)]
        child_factors = factor_from_spf(prime + 1, spf)
        target_sigma = sigma_from_factors(target_factors) % prime
        child_sigma = sigma_from_factors(child_factors) % prime
        q2 = fermat_quotient(2, prime)
        q3 = fermat_quotient(3, prime)

        r2_target = r_two_from_factors(target_factors)
        r2_child = r_two_from_factors(child_factors)
        theta_total = (r2_target + 4 * r2_child + 16) % prime
        k = (prime + 1) // 2
        eisenstein_sign = 1 if k % 2 else -1
        eisenstein = eisenstein_sign * 8 * target_sigma % prime
        cusp = (theta_total - eisenstein) % prime
        if cusp:
            if theta_first_nonzero is None:
                theta_first_nonzero = {
                    "r": prime,
                    "N": target,
                    "factorization": [target_factor, other_factor],
                    "k": k,
                    "r2_N": r2_target,
                    "r2_r_plus_1": r2_child,
                    "theta_total_mod_r": theta_total,
                    "sigma_1_N_mod_r": target_sigma,
                    "eisenstein_sign": eisenstein_sign,
                    "eisenstein_mod_r": eisenstein,
                    "cusp_mod_r": cusp,
                }
        else:
            theta_zero_count += 1

        rows.append(
            {
                "r": prime,
                "class_mod_24": prime % 24,
                "N": target,
                "p": int(target_factor),
                "q": int(other_factor),
                "t": target_sigma,
                "u": child_sigma,
                "q2": q2,
                "q3": q3,
                "theta_cusp": cusp,
            }
        )

    by_class = {}
    for row in rows:
        by_class.setdefault(row["class_mod_24"], []).append(row)

    affine = {}
    augmented = {}
    for residue_class, class_rows in sorted(by_class.items()):
        affine[str(residue_class)] = filter_bank(class_rows, 64, False)
        augmented[str(residue_class)] = filter_bank(class_rows, 8, True)

    bm_certificate = None
    for row in rows:
        prime = row["r"]
        if prime > args.bm_r_max:
            break
        values = [
            sigma_from_factors(factor_from_spf(index * prime + 1, spf)) % prime
            for index in range(18)
        ]
        differences = [
            (values[index + 1] - values[index]) % prime for index in range(17)
        ]
        hankel = [
            [differences[row_index + column] for column in range(9)]
            for row_index in range(9)
        ]
        determinant = determinant_mod(hankel, prime)
        if determinant:
            bm_certificate = {
                "r": prime,
                "N": row["N"],
                "factorization": [row["p"], row["q"]],
                "b_0_through_17": values,
                "differences_0_through_16": differences,
                "hankel_9_by_9": hankel,
                "determinant_mod_r": determinant,
            }
            break

    result = {
        "family_id": "F218-D01",
        "status": "finite_exact_search_only",
        "parameters": {
            "r_max": args.r_max,
            "bm_r_max": args.bm_r_max,
            "sieve_limit": sieve_limit,
            "affine_bound": 64,
            "augmented_bound": 8,
            "cartier_affine_order_bound": 8,
        },
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
        },
        "row_count": len(rows),
        "row_digest_sha256": canonical_digest(rows),
        "class_counts": {
            str(residue_class): len(class_rows)
            for residue_class, class_rows in sorted(by_class.items())
        },
        "test_A1": affine,
        "test_A2": augmented,
        "test_B_first_nonzero_hankel": bm_certificate,
        "test_C": {
            "isolation_claim": "theta_cusp == 0",
            "first_nonzero": theta_first_nonzero,
            "zero_count": theta_zero_count,
            "nonzero_count": len(rows) - theta_zero_count,
        },
        "elapsed_seconds": time.time() - started,
    }

    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")

    print(json.dumps({
        "row_count": result["row_count"],
        "class_counts": result["class_counts"],
        "A1_survivors": {
            key: len(value["survivors"]) for key, value in affine.items()
        },
        "A2_survivors": {
            key: len(value["survivors"]) for key, value in augmented.items()
        },
        "B_r": None if bm_certificate is None else bm_certificate["r"],
        "C_first_r": None if theta_first_nonzero is None else theta_first_nonzero["r"],
        "elapsed_seconds": result["elapsed_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
