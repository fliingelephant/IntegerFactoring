#!/usr/bin/env python3
"""Independent hostile audit for F13 Teichmuller-lift claims.

Approach-family ID: F13_teichmuller_lift_audit.
Python standard library only.  This source does not import the author's code
or read the author's JSON certificate when recomputing mathematics.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


FAMILY = "F13_teichmuller_lift_audit"
INSTANCES = [
    (3, 5),
    (3, 7),
    (5, 7),
    (7, 11),
    (11, 13),
    (13, 17),
    (101, 103),
    (1009, 1013),
    (10007, 10009),
]
EXPECTED_ADDITIVE = [
    "7/8",
    "11/12",
    "1/2",
    "1/2",
    "3/10",
    "9/32",
    "33/850",
    "673/170016",
    "3335/8345004",
]
EXPECTED_ITERATED = [
    "1/2",
    "0",
    "1/2",
    "2/5",
    "3/10",
    "5/12",
    "33/850",
    "503/63756",
    "3335/8345004",
]
EXPECTED_HIGH_UNION = [
    "1/2",
    "1/4",
    "1/4",
    "31/60",
    "37/120",
    "9/32",
    "571/10200",
]
AUTHOR_HASHES = {
    "teichmuller_kill.py": "200cfb7d28fea4c643dde0b6602f348e41ac5f71ad9fe4b09ca2864d849823f1",
    "run.sh": "e91c52d055ee9e7f8ed9becb747d3e14fef2c1b6bae25a268d59c4238cafbf70",
    "output/R01.json": "7a2c6c678acd99f38b6ff274c21f7512a3aca156ecfc760b8a41f5eb14ea399d",
    "logs/R01.log": "7273da35708dc28077f25727c9ae2ab2c2aeb86f7141ca7f835c79bcff46b0ca",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def primes_below(limit: int) -> list[int]:
    values = []
    for candidate in range(2, limit):
        if all(candidate % divisor for divisor in range(2, math.isqrt(candidate) + 1)):
            values.append(candidate)
    return values


def crt_pair(left: int, right: int, left_modulus: int, right_modulus: int) -> int:
    return (
        left
        + left_modulus
        * ((right - left) * pow(left_modulus, -1, right_modulus) % right_modulus)
    ) % (left_modulus * right_modulus)


def teich(residue: int, prime: int) -> int:
    return pow(residue % prime, prime, prime * prime)


def global_teich(residue: int, p: int, q: int) -> int:
    return crt_pair(teich(residue, p), teich(residue, q), p * p, q * q)


def valuation_category(value: int, prime: int) -> int:
    residue = value % (prime * prime)
    if residue % prime:
        return 0
    return 2 if residue == 0 else 1


def local_additive_counts(prime: int, other_prime: int) -> list[int]:
    counts = [0, 0, 0]
    modulus = prime * prime
    for ratio in range(1, prime):
        ratio_lift = teich(ratio, prime)
        successor_lift = teich(ratio + 1, prime)
        defect = (
            pow(successor_lift, other_prime, modulus)
            - pow(ratio_lift, other_prime, modulus)
            - 1
        ) % modulus
        counts[valuation_category(defect, prime)] += 1
    return counts


def additive_probability(p: int, q: int) -> tuple[Fraction, list[int], list[int]]:
    counts_p = local_additive_counts(p, q)
    counts_q = local_additive_counts(q, p)
    probabilities_p = [Fraction(count, p - 1) for count in counts_p]
    probabilities_q = [Fraction(count, q - 1) for count in counts_q]
    success = 1 - sum(
        probabilities_p[category] * probabilities_q[category]
        for category in range(3)
    )
    return success, counts_p, counts_q


def direct_additive_probability(p: int, q: int) -> Fraction:
    n = p * q
    modulus = n * n
    units = [value for value in range(1, n) if math.gcd(value, n) == 1]
    success = 0
    for left in units:
        left_lift = pow(left, n, modulus)
        for right in units:
            defect = (
                pow((left + right) % modulus, n, modulus)
                - left_lift
                - pow(right, n, modulus)
            ) % modulus
            first = math.gcd(defect, n)
            if 1 < first < n:
                success += 1
            elif first == n and 1 < math.gcd(defect // n, n) < n:
                success += 1
    return Fraction(success, len(units) ** 2)


def iterated_probabilities(p: int, q: int) -> list[Fraction]:
    values = []
    for iteration in range(1, 4):
        roots_p = sum(
            pow(x, pow(q, iteration + 1), p) == pow(x, pow(q, iteration), p)
            for x in range(1, p)
        )
        roots_q = sum(
            pow(x, pow(p, iteration + 1), q) == pow(x, pow(p, iteration), q)
            for x in range(1, q)
        )
        probability_p = Fraction(roots_p, p - 1)
        probability_q = Fraction(roots_q, q - 1)
        formula_p = Fraction(math.gcd(q - 1, p - 1), p - 1)
        formula_q = Fraction(math.gcd(pow(p, iteration) * (p - 1), q - 1), q - 1)
        assert probability_p == formula_p
        assert probability_q == formula_q
        values.append(
            probability_p * (1 - probability_q)
            + (1 - probability_p) * probability_q
        )
    return values


def exact_high_digits(p: int, q: int) -> tuple[list[Fraction], Fraction]:
    n = p * q
    modulus = n * n
    units = [value for value in range(1, n) if math.gcd(value, n) == 1]
    marginal_successes = [0, 0, 0]
    union_successes = 0
    for base in units:
        any_success = False
        value = base
        for index in range(3):
            value = pow(value, n, modulus)
            high_digit = (value - value % n) // n
            divisor = math.gcd(high_digit, n)
            if 1 < divisor < n:
                marginal_successes[index] += 1
                any_success = True
        union_successes += any_success
    return (
        [Fraction(count, len(units)) for count in marginal_successes],
        Fraction(union_successes, len(units)),
    )


def high_digit_census(p: int, q: int) -> dict[str, int]:
    count_p = 0
    count_q = 0
    count_proper = 0
    maximum_p_fibre = 0
    maximum_q_fibre = 0
    for x in range(1, p):
        fibre = 0
        for y in range(1, q):
            representative = crt_pair(x, y, p, q)
            p_zero = (representative - teich(x, p)) % (p * p) == 0
            q_zero = (representative - teich(y, q)) % (q * q) == 0
            count_p += p_zero
            count_q += q_zero
            count_proper += p_zero != q_zero
            fibre += p_zero
        maximum_p_fibre = max(maximum_p_fibre, fibre)
    for y in range(1, q):
        fibre = 0
        for x in range(1, p):
            representative = crt_pair(x, y, p, q)
            fibre += (representative - teich(y, q)) % (q * q) == 0
        maximum_q_fibre = max(maximum_q_fibre, fibre)
    total = (p - 1) * (q - 1)
    assert count_p <= 2 * (p - 1)
    assert count_q <= q - 1
    assert maximum_p_fibre <= 2
    assert maximum_q_fibre <= 1
    return {
        "p_divisible": count_p,
        "q_divisible": count_q,
        "proper": count_proper,
        "total": total,
        "maximum_p_fibre": maximum_p_fibre,
        "maximum_q_fibre": maximum_q_fibre,
    }


def structural_record(p: int, q: int) -> dict[str, object]:
    n = p * q
    modulus = n * n
    exhaustive = n <= 10_403
    bases = range(n) if exhaustive else list(range(256)) + [n - 2, n - 1]
    principal_coefficients = range(n) if exhaustive else list(range(256)) + [n - 1]

    local_checks = 0
    identity_checks = 0
    factor_through_checks = 0
    for base in bases:
        lifted = pow(base, n, modulus)
        assert lifted % (p * p) == pow(teich(base, p), q, p * p)
        assert lifted % (q * q) == pow(teich(base, q), p, q * q)
        local_checks += 1
        assert pow(lifted, n + 1, modulus) == pow(lifted, p + q, modulus)
        identity_checks += 1
        for coefficient in (0, 1, n - 1):
            assert pow(base + coefficient * n, n, modulus) == lifted
            factor_through_checks += 1

    coordinate_pairs = set()
    for coefficient in principal_coefficients:
        principal = (1 + coefficient * n) % modulus
        assert pow(principal, n, modulus) == 1
        coordinate_pairs.add(((q * coefficient) % p, (p * coefficient) % q))
    if exhaustive:
        assert len(coordinate_pairs) == n

    lam = math.lcm(p - 1, q - 1)
    exponent_gcd = math.gcd(n, lam)
    unit_bases = [base for base in bases if math.gcd(base, n) == 1]
    if exponent_gcd == 1:
        inverse = pow(n, -1, lam)
        for base in unit_bases:
            assert pow(pow(base, n, modulus), inverse, modulus) == global_teich(base, p, q)
        collision = None
    else:
        inverse = None
        teich_values = [global_teich(base, p, q) for base in range(1, n) if math.gcd(base, n) == 1]
        images: dict[int, int] = {}
        collision = None
        for value in teich_values:
            image = pow(value, n, modulus)
            if image in images and images[image] != value:
                collision = [images[image], value, image]
                break
            images[image] = value
        assert collision is not None

    additive, counts_p, counts_q = additive_probability(p, q)
    iteration = iterated_probabilities(p, q)
    return {
        "p": p,
        "q": q,
        "N": n,
        "exhaustive_structural": exhaustive,
        "local_decomposition_checks": local_checks,
        "hidden_sum_identity_checks_including_nonunits": identity_checks,
        "factor_through_reduction_checks": factor_through_checks,
        "principal_coefficients_checked": len(principal_coefficients),
        "principal_coordinate_pairs": len(coordinate_pairs),
        "lambda": lam,
        "gcd_N_lambda": exponent_gcd,
        "inverse": inverse,
        "noninjective_collision_when_no_inverse": collision,
        "additive_counts_p": counts_p,
        "additive_counts_q": counts_q,
        "additive_probability": str(additive),
        "iterated_probabilities": [str(value) for value in iteration],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()

    records = [structural_record(p, q) for p, q in INSTANCES]
    assert [record["additive_probability"] for record in records] == EXPECTED_ADDITIVE
    assert [record["iterated_probabilities"][0] for record in records] == EXPECTED_ITERATED

    for p, q in INSTANCES:
        if p * q <= 221:
            assert direct_additive_probability(p, q) == additive_probability(p, q)[0]

    exact_high_records = []
    for index, (p, q) in enumerate(INSTANCES[:7]):
        marginals, union = exact_high_digits(p, q)
        assert str(union) == EXPECTED_HIGH_UNION[index]
        assert all(value <= Fraction(2, q - 1) + Fraction(1, p - 1) for value in marginals)
        exact_high_records.append(
            {
                "p": p,
                "q": q,
                "marginal_proper_probabilities": [str(value) for value in marginals],
                "three_iterate_union_probability": str(union),
            }
        )

    balanced_census = []
    odd_primes = [prime for prime in primes_below(80) if prime % 2]
    for p in odd_primes:
        for q in odd_primes:
            if p < q < 2 * p:
                assert (q - 1) % p != 0
                balanced_census.append({"p": p, "q": q, **high_digit_census(p, q)})

    twin_records = []
    for p in primes_below(200):
        q = p + 2
        if q not in primes_below(202):
            continue
        probability, counts_p, counts_q = additive_probability(p, q)
        if p > 3:
            assert counts_p == [p - 2, 0, 1]
            assert counts_q == [q - 4, 0, 3]
            assert probability == Fraction(4 * (p - 2), (p - 1) * (p + 1))
            formula_applies = True
        else:
            assert (p, q) == (3, 5)
            assert counts_p == [0, 1, 1]
            assert counts_q == [3, 0, 1]
            assert probability == Fraction(7, 8)
            formula_applies = False
        twin_records.append(
            {
                "p": p,
                "q": q,
                "counts_p": counts_p,
                "counts_q": counts_q,
                "probability": str(probability),
                "p_greater_than_3_formula_applies": formula_applies,
            }
        )

    repository = Path(__file__).resolve().parents[2]
    author_directory = repository / "experiments" / "F13_teichmuller_lift_kill"
    provenance = {}
    for relative_path, expected_hash in AUTHOR_HASHES.items():
        actual_hash = sha256(author_directory / relative_path)
        assert actual_hash == expected_hash
        provenance[relative_path] = actual_hash

    source = Path(__file__).resolve()
    result = {
        "approach_family": FAMILY,
        "status": "PASS_WITH_CORRECTION",
        "correction": "The twin-prime category theorem requires p > 3; (3,5) is exceptional.",
        "records": records,
        "direct_global_additive_cross_checks_through_N": 221,
        "exact_high_digit_records": exact_high_records,
        "balanced_high_digit_census_prime_limit": 80,
        "balanced_high_digit_pairs_checked": len(balanced_census),
        "balanced_high_digit_census": balanced_census,
        "twin_prime_records_below_202": twin_records,
        "author_artifact_hashes": provenance,
        "source": str(source),
        "source_sha256": sha256(source),
    }
    Path(arguments.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
