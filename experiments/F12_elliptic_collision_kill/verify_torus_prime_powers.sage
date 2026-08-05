#!/usr/bin/env sage
"""Verify the all-input torus reduction on repeated-prime examples.

Approach-family ID: F12_elliptic_collision_kill.
"""

import argparse
import hashlib
import json
import math
import time
from pathlib import Path


FAMILY = "F12_elliptic_collision_kill"
FACTORIZATIONS = [
    {3: 2, 7: 3},
    {2: 2, 3: 1, 11: 2},
]


def torus_superfactorial(base, length, modulus):
    value = 1
    power = base % modulus
    for difference in range(1, length):
        value = value * pow(1 - power, length - difference, modulus) % modulus
        power = power * base % modulus
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    started = time.monotonic()
    records = []

    for factorization in FACTORIZATIONS:
        N = prod(prime**exponent for prime, exponent in factorization.items())
        total_multiplicity = sum(factorization.values())
        length, exact_root = ZZ(N).nth_root(total_multiplicity, truncate_mode=True)
        smallest_prime = min(factorization)
        largest_prime = max(factorization)
        assert not exact_root
        assert smallest_prime <= length < largest_prime
        bitlength = int(ZZ(N).nbits())
        assert 2 <= total_multiplicity <= bitlength

        unit_count = 0
        primitive_largest_count = 0
        successful_at_correct_k = 0
        gcd_values = set()
        for base in range(1, N):
            if gcd(base, N) != 1:
                continue
            unit_count += 1
            primitive_largest = (
                Mod(base, largest_prime).multiplicative_order() == largest_prime - 1
            )
            if not primitive_largest:
                continue
            primitive_largest_count += 1
            collision_value = torus_superfactorial(base, int(length), N)
            divisor = int(gcd(collision_value, N))
            assert 1 < divisor < N
            assert divisor % smallest_prime == 0
            assert divisor % largest_prime != 0
            successful_at_correct_k += 1
            gcd_values.add(divisor)

            scan_divisors = []
            for exponent_guess in range(2, bitlength + 1):
                guessed_length = ZZ(N).nth_root(
                    exponent_guess, truncate_mode=True
                )[0]
                if guessed_length < 2:
                    continue
                guessed_value = torus_superfactorial(base, int(guessed_length), N)
                guessed_divisor = int(gcd(guessed_value, N))
                if 1 < guessed_divisor < N:
                    scan_divisors.append([exponent_guess, guessed_divisor])
            assert any(
                exponent_guess == total_multiplicity
                for exponent_guess, divisor in scan_divisors
            )

        expected_primitive_count = int(
            unit_count * euler_phi(largest_prime - 1) / (largest_prime - 1)
        )
        assert primitive_largest_count == expected_primitive_count
        assert successful_at_correct_k == primitive_largest_count
        records.append(
            {
                "N": int(N),
                "factorization": {
                    str(prime): exponent for prime, exponent in factorization.items()
                },
                "total_prime_multiplicity_s": total_multiplicity,
                "bitlength": bitlength,
                "m_s_floor_N_to_1_over_s": int(length),
                "smallest_prime_le_m_s": smallest_prime <= length,
                "largest_prime_gt_m_s": largest_prime > length,
                "unit_count": unit_count,
                "primitive_largest_residue_unit_count": primitive_largest_count,
                "primitive_probability": (
                    f"{int(euler_phi(largest_prime - 1))}/{largest_prime - 1}"
                ),
                "proper_gcd_values_at_k_equals_s": sorted(gcd_values),
                "scan_2_through_bitlength_contains_k_equals_s": True,
            }
        )

    perfect_power = ZZ(225)
    perfect_root, exact = perfect_power.nth_root(2, truncate_mode=True)
    assert exact and perfect_root == 15 and 1 < perfect_root < perfect_power

    source_path = Path(__file__).resolve().with_suffix("")
    output = {
        "approach_family": FAMILY,
        "purpose": "repeated-prime and exponent-scan verification",
        "records": records,
        "perfect_power_preprocessing": {
            "N": int(perfect_power),
            "exponent": 2,
            "proper_root_divisor": int(perfect_root),
        },
        "elapsed_seconds": time.monotonic() - started,
        "source": str(source_path),
        "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
    }
    with open(args.output, "w") as handle:
        json.dump(output, handle, indent=2, default=int)
        handle.write("\n")


main()
