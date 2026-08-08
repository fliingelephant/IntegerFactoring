#!/usr/bin/env python3
"""Independent arithmetic verifier for the frozen F98 witness.

This audit deliberately uses Sage factorization to reconstruct square-class
vectors.  It does not import any candidate function.
"""

from __future__ import annotations

import argparse
import bisect
import json
import math
from pathlib import Path

from sage.all import factor, is_prime


N = 202_537_109
PREFIX = 5_616


def stable_json(value):
    if isinstance(value, dict):
        return {key: stable_json(item) for key, item in value.items() if key != "elapsed_seconds"}
    if isinstance(value, list):
        return [stable_json(item) for item in value]
    return value


def factor_parity(value: int) -> frozenset[int]:
    return frozenset(int(prime) for prime, exponent in factor(value) if int(exponent) & 1)


def root_data(indices: tuple[int, ...], products: list[int]) -> tuple[bool, int, int, int]:
    product = math.prod(products[index] for index in indices)
    root = math.isqrt(product)
    if root * root != product:
        raise AssertionError("Square-class zero did not give an integer square.")
    minus = math.gcd(root - 1, N)
    plus = math.gcd(root + 1, N)
    useful = 1 < minus < N or 1 < plus < N
    return useful, root % N, minus, plus


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate-output", type=Path, required=True)
    parser.add_argument("--audit-output", type=Path, required=True)
    parser.add_argument("--small-support-output", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    candidate = json.loads(args.candidate_output.read_text())
    replay = json.loads(args.audit_output.read_text())
    small = json.loads(args.small_support_output.read_text())
    if stable_json(candidate) != stable_json(replay):
        raise AssertionError("The N-only audit replay differs from the pinned replay.")

    n = N.bit_length()
    bound = n * n
    if (n, bound) != (28, 784):
        raise AssertionError("Bit-length or trial bound changed.")
    factorization = [(int(prime), int(exponent)) for prime, exponent in factor(N)]
    if factorization != [(10_267, 1), (19_727, 1)]:
        raise AssertionError("Independent factorization changed.")
    if not all(is_prime(prime) for prime, _ in factorization):
        raise AssertionError("A displayed factor is not prime.")
    p, q = factorization[0][0], factorization[1][0]
    g = math.gcd(p - 1, q - 1)
    a = (p - 1) // g
    b = (q - 1) // g
    if (g, a, b, math.gcd(a * b, N - 1)) != (2, 5_133, 9_863, 1):
        raise AssertionError("The P98 stability certificate failed.")
    if p <= bound or any(1 < math.gcd(trial, N) < N for trial in range(2, bound + 1)):
        raise AssertionError("The trial-hard certificate failed.")

    certificate = candidate["decoder"]["first_useful_certificate"]
    records = certificate["witness_records"]
    if len(records) != 166 or len({int(record["P"]) for record in records}) != 166:
        raise AssertionError("The public certificate is not 166 distinct values.")
    for record in records:
        c, w, product = int(record["c"]), int(record["w"]), int(record["P"])
        if not (1 <= c < N and 1 <= w < N):
            raise AssertionError("A canonical endpoint is out of range.")
        if pow(c, -1, N) != w or c * w != product or product % N != 1:
            raise AssertionError("A public witness record is invalid.")
    public_product = math.prod(int(record["P"]) for record in records)
    public_root = math.isqrt(public_product)
    if public_root * public_root != public_product:
        raise AssertionError("The public certificate product is not a square.")
    public_tuple = (
        public_root % N,
        math.gcd(public_root - 1, N),
        math.gcd(public_root + 1, N),
    )
    if public_tuple != (132_013_085, 19_727, 10_267):
        raise AssertionError("The public root or gcd certificate failed.")

    active_pairs = [tuple(pair) for pair in candidate["active_pairs"]]
    seen: set[int] = set()
    relation_records: list[tuple[int, int, int]] = []

    def retain(c: int) -> None:
        if c in seen:
            return
        seen.add(c)
        w = pow(c, -1, N)
        relation_records.append((c, w, c * w))

    for seed in range(2, n + 1):
        retain(seed)
    for u, v in active_pairs:
        for exponent in range(bound + 1):
            retain(pow(u, exponent, N) * v % N)
            if len(relation_records) >= PREFIX:
                break
            retain(u * pow(v, exponent, N) % N)
            if len(relation_records) >= PREFIX:
                break
        if len(relation_records) >= PREFIX:
            break
    if len(relation_records) != PREFIX:
        raise AssertionError("The public prefix did not regenerate.")

    prime_sets: list[frozenset[int]] = []
    products: list[int] = []
    all_primes: set[int] = set()
    for c, w, product in relation_records:
        parity = factor_parity(c) ^ factor_parity(w)
        prime_sets.append(parity)
        all_primes.update(parity)
        products.append(product)
    prime_order = {prime: index for index, prime in enumerate(sorted(all_primes))}
    parities = [sum(1 << prime_order[p] for p in parity) for parity in prime_sets]

    support_one = [index for index, parity in enumerate(parities) if parity == 0]
    if support_one != [1_600] or root_data((1_600,), products)[0]:
        raise AssertionError("Independent support-one result differs.")

    classes: dict[int, list[int]] = {}
    for index, parity in enumerate(parities):
        classes.setdefault(parity, []).append(index)
    support_two_count = 0
    for indices in classes.values():
        for position, left in enumerate(indices):
            for right in indices[position + 1:]:
                support_two_count += 1
                if products[left] != products[right]:
                    raise AssertionError("A same-class pair has distinct values.")
                if root_data((left, right), products)[0]:
                    raise AssertionError("A useful support-two circuit exists.")
    if support_two_count != 1_847:
        raise AssertionError("Independent support-two count differs.")

    triple_count = 0
    for left in range(PREFIX):
        for middle in range(left + 1, PREFIX):
            candidates = classes.get(parities[left] ^ parities[middle], ())
            position = bisect.bisect_right(candidates, middle)
            if position == len(candidates):
                continue
            right = candidates[position]
            triple_count += 1
            if root_data((left, middle, right), products)[0]:
                raise AssertionError("A useful support-three circuit exists.")
    if triple_count != 1_530:
        raise AssertionError("Independent support-three count differs.")

    pivots: dict[int, tuple[int, int]] = {}
    independent_first_general = None
    for index, parity in enumerate(parities):
        reduced = parity
        combination = 1 << index
        while reduced:
            pivot = reduced.bit_length() - 1
            known = pivots.get(pivot)
            if known is None:
                pivots[pivot] = (reduced, combination)
                break
            reduced ^= known[0]
            combination ^= known[1]
        else:
            indices = tuple(
                relation_index
                for relation_index in range(index + 1)
                if (combination >> relation_index) & 1
            )
            data = root_data(indices, products)
            if data[0]:
                independent_first_general = (index, indices, data)
                break
    if independent_first_general is None:
        raise AssertionError("Independent elimination found no useful circuit.")
    if independent_first_general[0] != 5_615:
        raise AssertionError("Independent first-useful ordinal differs.")

    general = small["first_general_dependency_factor"]
    diagnostic = general["reduced_witness"]
    diagnostic_indices = tuple(int(index) for index in diagnostic["indices_zero_based"])
    if len(diagnostic_indices) != 166 or len({products[index] for index in diagnostic_indices}) != 166:
        raise AssertionError("The diagnostic certificate is not 166 distinct values.")
    diagnostic_tuple = root_data(diagnostic_indices, products)[1:]
    if diagnostic_tuple != (70_524_024, 10_267, 19_727):
        raise AssertionError("The diagnostic root or gcd certificate failed.")
    if [products[index] for index in diagnostic_indices] != [
        int(value) for value in diagnostic["relation_products"]
    ]:
        raise AssertionError("The diagnostic relation-value list is not its stated prefix subset.")

    if candidate["direct_screen"] != {
        "new_relations_examined": 12_522,
        "status": "complete_round_one_null",
    }:
        raise AssertionError("The full direct-screen summary differs.")
    full_seen: set[int] = set()
    full_records: list[tuple[int, int, int]] = []

    def full_retain(c: int) -> None:
        if c in full_seen:
            return
        full_seen.add(c)
        w = pow(c, -1, N)
        if 1 < math.gcd(c - w, N) < N or 1 < math.gcd(c + w, N) < N:
            raise AssertionError("The claimed complete direct screen has a hit.")
        full_records.append((c, w, c * w))

    for seed in range(2, n + 1):
        full_retain(seed)
    full_new = 0
    for u, v in active_pairs:
        for exponent in range(bound + 1):
            for c in (pow(u, exponent, N) * v % N, u * pow(v, exponent, N) % N):
                if c in full_seen:
                    continue
                full_retain(c)
                full_new += 1
                w = pow(c, -1, N)
                if 1 < math.gcd(c - w, N) < N or 1 < math.gcd(c + w, N) < N:
                    raise AssertionError("The claimed direct-null screen has a hit.")
    if full_new != 12_522 or len(full_seen) != 12_549:
        raise AssertionError("The independent full direct-screen count differs.")
    unique_records: list[tuple[int, int, int]] = []
    unique_raw_indices: list[int] = []
    seen_products: set[int] = set()
    for raw_index, record in enumerate(full_records):
        if record[2] == 1 or record[2] in seen_products:
            continue
        seen_products.add(record[2])
        unique_records.append(record)
        unique_raw_indices.append(raw_index)
    if len(unique_records) != 9_414:
        raise AssertionError("The independent unique-relation count differs.")
    selected_columns = [int(index) for index in certificate["selected_columns_zero_based"]]
    selected_raw = [int(index) for index in certificate["selected_raw_indices_zero_based"]]
    if [unique_raw_indices[index] for index in selected_columns] != selected_raw:
        raise AssertionError("The selected public columns do not map to the stated raw indices.")
    if [unique_records[index] for index in selected_columns] != [
        (int(record["c"]), int(record["w"]), int(record["P"])) for record in records
    ]:
        raise AssertionError("The selected public records are not their stated stream columns.")

    result = {
        "status": "PASS",
        "N": N,
        "factorization": factorization,
        "stable_certificate": {"g": g, "A": a, "B": b, "gcd_AB_N_minus_1": 1},
        "trial_bound": bound,
        "least_factor": p,
        "audit_replay_equal_ignoring_elapsed_seconds": True,
        "full_direct_new_residues": full_new,
        "full_direct_residues_including_seeds": len(full_seen),
        "full_direct_hit_count": 0,
        "public_certificate": {
            "support": 166,
            "distinct_relation_values": 166,
            "root_mod_N": public_tuple[0],
            "gcd_minus": public_tuple[1],
            "gcd_plus": public_tuple[2],
        },
        "independent_prefix_factorization_rows": len(all_primes),
        "support_one_matches": len(support_one),
        "support_two_matches": support_two_count,
        "support_three_first_right_matches": triple_count,
        "independent_first_useful_ordinal_one_based": independent_first_general[0] + 1,
        "independent_first_useful_support": len(independent_first_general[1]),
        "diagnostic_certificate": {
            "support": len(diagnostic_indices),
            "distinct_relation_values": len({products[index] for index in diagnostic_indices}),
            "root_mod_N": diagnostic_tuple[0],
            "gcd_minus": diagnostic_tuple[1],
            "gcd_plus": diagnostic_tuple[2],
        },
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("audit_verifier_status=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
