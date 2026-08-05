"""Proof-blind, end-to-end reconstruction of the finite F04 AKS witness.

This source deliberately computes from the numeric statement only.  It does not
load any project registry, note, certificate, or earlier F04 experiment.
"""

import argparse
import csv
import hashlib
import json
import math
import os
import struct
import sys
import time


APPROACH_FAMILY = "F04_reconstruct"
N = ZZ(20000000499999937)
P = ZZ(100000007)
Q = ZZ(199999991)
R = ZZ(2953)
EXPECTED_A = ZZ(2942)


def trial_factor(n):
    """Return the complete factorization of a positive machine-sized integer."""
    remaining = ZZ(n)
    factors = {}
    divisor = ZZ(2)
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors[int(divisor)] = factors.get(int(divisor), 0) + 1
            remaining //= divisor
        divisor = ZZ(3) if divisor == 2 else divisor + 2
    if remaining > 1:
        factors[int(remaining)] = factors.get(int(remaining), 0) + 1
    return factors


def trial_is_prime(n):
    factors = trial_factor(n)
    return len(factors) == 1 and factors.get(int(n)) == 1


def euler_phi_from_trial_factorization(n):
    result = ZZ(n)
    for prime in trial_factor(n):
        result = result // prime * (prime - 1)
    return result


def exact_order_naive(base, modulus):
    """Compute an exact order by traversing powers, with no order oracle."""
    if math.gcd(int(base), int(modulus)) != 1:
        return None
    residue = ZZ(1)
    reduced_base = ZZ(base % modulus)
    for exponent in range(1, int(euler_phi_from_trial_factorization(modulus)) + 1):
        residue = residue * reduced_base % modulus
        if residue == 1:
            return ZZ(exponent)
    raise AssertionError("Euler bound exhausted without finding the order")


def write_order_table(output_dir, order_threshold):
    """Exhaust every r candidate through 2953 and preserve the exact orders."""
    path = os.path.join(output_dir, "orders_2_through_2953.csv")
    digest = hashlib.sha256()
    passing = []
    maximum_before = ZZ(0)
    maximum_before_at = []
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        header = ["candidate_r", "gcd_N_r", "phi_r", "ord_r_N", "order_exceeds_log2N_squared"]
        writer.writerow(header)
        digest.update((",".join(header) + "\n").encode())
        for candidate in range(2, int(R) + 1):
            common = ZZ(math.gcd(int(N), candidate))
            phi = euler_phi_from_trial_factorization(candidate)
            order = exact_order_naive(N, candidate)
            passes = order is not None and ZZ(order) > order_threshold.upper()
            row = [candidate, int(common), int(phi), "" if order is None else int(order), int(passes)]
            encoded = (",".join(str(value) for value in row) + "\n").encode()
            handle.write(encoded.decode())
            digest.update(encoded)
            if passes:
                passing.append(candidate)
            if candidate < R and order is not None:
                if order > maximum_before:
                    maximum_before = order
                    maximum_before_at = [candidate]
                elif order == maximum_before:
                    maximum_before_at.append(candidate)
    assert passing == [int(R)]
    return {
        "path": path,
        "sha256": digest.hexdigest(),
        "rows": int(R - 1),
        "passing_candidates": passing,
        "max_order_before_r": int(maximum_before),
        "max_order_before_r_locations": maximum_before_at,
    }


def coefficient_vector(element, field, r):
    lifted = element.lift().list()
    if len(lifted) > r:
        raise AssertionError("quotient representative is not reduced")
    values = [int(coefficient) for coefficient in lifted]
    values.extend([0] * (r - len(values)))
    return values


def permute_substitution(values, multiplier, modulus, r):
    """Coefficients of f(X^multiplier) modulo X^r-1."""
    permuted = [0] * r
    for position, value in enumerate(values):
        target = (multiplier * position) % r
        permuted[target] = value % modulus
    return permuted


def exhaust_local_family(modulus, factor, other_factor, shift_bound, output_dir):
    """Exhaust h_{other_factor,a} over F_modulus[Y]/(Y^r-1)."""
    modulus_int = int(modulus)
    factor_int = int(factor)
    other_int = int(other_factor)
    r_int = int(R)
    field = GF(modulus)
    polynomial_ring = PolynomialRing(field, "x")
    x = polynomial_ring.gen()
    quotient = polynomial_ring.quotient(x**R - 1, "y")
    y = quotient.gen()
    y_to_other = y**other_factor

    label = "mod_p" if modulus == P else "mod_q"
    rows_path = os.path.join(output_dir, f"local_coefficients_{label}.jsonl")
    zeros_path = os.path.join(output_dir, f"local_zeros_{label}.jsonl")
    stream_digest = hashlib.sha256()
    rows_digest = hashlib.sha256()
    family_product = 1
    family_sum = 0
    family_weighted_sum = 0
    total_zeros = 0
    least_value = modulus_int
    least_location = None
    start = time.monotonic()

    sample_shifts = sorted(set([1, 2, int(shift_bound) // 2, int(shift_bound)]))
    direct_reduction_checks = []

    with open(rows_path, "w", encoding="utf-8") as rows_handle, open(
        zeros_path, "w", encoding="utf-8"
    ) as zeros_handle:
        for a in range(1, int(shift_bound) + 1):
            local_element = (y + field(a)) ** other_factor - y_to_other - field(a)
            values = coefficient_vector(local_element, field, r_int)
            encoded_values = struct.pack(f"<{r_int}I", *values)
            stream_digest.update(struct.pack("<I", a))
            stream_digest.update(encoded_values)

            zero_positions = [position for position, value in enumerate(values) if value == 0]
            total_zeros += len(zero_positions)
            for position in zero_positions:
                zero_row = {"a": a, "position": position}
                zeros_handle.write(json.dumps(zero_row, sort_keys=True, default=int) + "\n")

            row_product = 1
            for value in values:
                row_product = row_product * value % modulus_int
            row_sum = sum(values) % modulus_int
            row_weighted_sum = sum((position + 1) * value for position, value in enumerate(values)) % modulus_int
            row_minimum = min(values)
            row_minimum_position = values.index(row_minimum)
            if row_minimum < least_value:
                least_value = row_minimum
                least_location = [a, row_minimum_position]

            family_product = family_product * row_product % modulus_int
            family_sum = (family_sum + row_sum) % modulus_int
            family_weighted_sum = (family_weighted_sum + a * row_weighted_sum) % modulus_int

            row = {
                "a": a,
                "coefficient_count": r_int,
                "sha256_le_u32": hashlib.sha256(encoded_values).hexdigest(),
                "zero_count": len(zero_positions),
                "product_mod_prime": row_product,
                "sum_mod_prime": row_sum,
                "weighted_sum_mod_prime": row_weighted_sum,
                "minimum_least_residue": row_minimum,
                "minimum_position": row_minimum_position,
            }
            encoded_row = (json.dumps(row, sort_keys=True, default=int) + "\n").encode()
            rows_handle.write(encoded_row.decode())
            rows_digest.update(encoded_row)

            if a in sample_shifts:
                direct_element = (y + field(a)) ** N - y**N - field(a)
                direct_values = coefficient_vector(direct_element, field, r_int)
                predicted_values = permute_substitution(values, factor_int, modulus_int, r_int)
                agrees = direct_values == predicted_values
                assert agrees
                direct_reduction_checks.append({"a": a, "agrees": agrees})

            if a % 100 == 0 or a == int(shift_bound):
                print(
                    f"{label}: exhausted a=1..{a}; zeros={total_zeros}; "
                    f"elapsed={time.monotonic() - start:.3f}s",
                    file=sys.stderr,
                    flush=True,
                )

    assert total_zeros == 0
    assert family_product != 0
    return {
        "label": label,
        "modulus": modulus_int,
        "frobenius_factor": factor_int,
        "reduced_exponent": other_int,
        "a_first": 1,
        "a_last": int(shift_bound),
        "shifts_exhausted": int(shift_bound),
        "positions_per_shift": r_int,
        "coefficients_exhausted": int(shift_bound) * r_int,
        "zero_count": total_zeros,
        "all_coefficients_nonzero": total_zeros == 0,
        "product_of_all_coefficients_mod_prime": family_product,
        "sum_of_row_sums_mod_prime": family_sum,
        "a_weighted_sum_of_row_weighted_sums_mod_prime": family_weighted_sum,
        "minimum_least_residue": least_value,
        "minimum_location_a_position": least_location,
        "coefficient_stream_sha256": stream_digest.hexdigest(),
        "row_file": rows_path,
        "row_file_sha256": rows_digest.hexdigest(),
        "zero_file": zeros_path,
        "direct_original_H_reduction_checks": direct_reduction_checks,
        "elapsed_seconds": time.monotonic() - start,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    output_dir = os.path.abspath(args.output_dir)
    os.makedirs(output_dir, exist_ok=True)
    run_start = time.monotonic()

    primality = {}
    for name, value in [("p", P), ("q", Q), ("r", R)]:
        is_prime = trial_is_prime(value)
        assert is_prime
        primality[name] = {
            "value": int(value),
            "trial_division_prime": is_prime,
            "trial_divisors_checked_through": int(math.isqrt(int(value))),
        }

    assert P * Q == N
    assert P != Q
    assert P > R and Q > R
    assert math.gcd(int(P), int(R)) == 1
    assert math.gcd(int(Q), int(R)) == 1

    precision = 256
    intervals = RealIntervalField(precision)
    log2_n = intervals(N).log() / intervals(2).log()
    order_threshold = log2_n**2
    assert order_threshold.lower() > 2932
    assert order_threshold.upper() < 2933

    phi_r = euler_phi_from_trial_factorization(R)
    assert phi_r == 2952
    shift_expression = intervals(phi_r).sqrt() * log2_n
    shift_lower_floor = int(floor(shift_expression.lower()))
    shift_upper_floor = int(floor(shift_expression.upper()))
    assert shift_lower_floor == shift_upper_floor == EXPECTED_A

    order_table = write_order_table(output_dir, order_threshold)
    order_r = exact_order_naive(N, R)
    assert order_r == phi_r
    order_prime_divisors = sorted(trial_factor(phi_r))
    order_certificate = {
        "base_N_mod_r": int(N % R),
        "claimed_order": int(order_r),
        "power_at_claimed_order": int(power_mod(N % R, order_r, R)),
        "proper_prime_quotient_powers": {
            str(prime): int(power_mod(N % R, order_r // prime, R))
            for prime in order_prime_divisors
        },
    }
    assert order_certificate["power_at_claimed_order"] == 1
    assert all(value != 1 for value in order_certificate["proper_prime_quotient_powers"].values())

    local_mod_p = exhaust_local_family(P, P, Q, EXPECTED_A, output_dir)
    local_mod_q = exhaust_local_family(Q, Q, P, EXPECTED_A, output_dir)

    summary = {
        "approach_family": APPROACH_FAMILY,
        "status_label": "self-audited",
        "finite_claim_result": "confirmed"
        if local_mod_p["zero_count"] == local_mod_q["zero_count"] == 0
        else "refuted",
        "N": int(N),
        "factorization": {str(int(P)): 1, str(int(Q)): 1},
        "factorization_product_check": int(P * Q),
        "prime_checks": primality,
        "both_factors_exceed_r": bool(P > R and Q > R),
        "bit_length_ceil_log2_N_plus_1": int(N.nbits()),
        "log2_N_interval_256_bits": str(log2_n),
        "log2_N_squared_interval_256_bits": str(order_threshold),
        "integer_order_threshold_consequence": "2932 < (log2 N)^2 < 2933",
        "r": int(R),
        "phi_r": int(phi_r),
        "phi_r_factorization": {str(prime): exponent for prime, exponent in trial_factor(phi_r).items()},
        "order_r_N": int(order_r),
        "order_certificate": order_certificate,
        "minimal_r_exhaustion": order_table,
        "shift_expression_interval_256_bits": str(shift_expression),
        "shift_bound_A": int(EXPECTED_A),
        "local_mod_p": local_mod_p,
        "local_mod_q": local_mod_q,
        "total_local_coefficients_exhausted": local_mod_p["coefficients_exhausted"]
        + local_mod_q["coefficients_exhausted"],
        "total_local_zero_count": local_mod_p["zero_count"] + local_mod_q["zero_count"],
        "elapsed_seconds": time.monotonic() - run_start,
    }
    summary_path = os.path.join(output_dir, "summary.json")
    with open(summary_path, "w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2, sort_keys=True, default=int)
        handle.write("\n")
    print(
        json.dumps(
            {"summary_path": summary_path, "finite_claim_result": summary["finite_claim_result"]},
            sort_keys=True,
            default=int,
        )
    )


main()
