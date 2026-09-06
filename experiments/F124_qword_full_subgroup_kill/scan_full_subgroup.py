#!/usr/bin/env python3
"""Exact F124-D01 full-supergroup scan."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from array import array
from collections import Counter, deque
from pathlib import Path


R = 1 << 15
PRIME_MIN = 257
PRIME_MAX = 4096


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def integer_sha256(value: int) -> str:
    length = max(1, (value.bit_length() + 7) // 8)
    return hashlib.sha256(value.to_bytes(length, "big")).hexdigest()


def factor_integer(value: int, smallest_prime_factor: array) -> dict[int, int]:
    factors: dict[int, int] = {}
    remaining = value
    while remaining > 1:
        prime = int(smallest_prime_factor[remaining]) or remaining
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        factors[prime] = exponent
    return factors


def multiply_factorization(factors: dict[int, int]) -> int:
    value = 1
    for prime, exponent in sorted(factors.items()):
        value *= prime**exponent
    return value


def proper_gcd(value: int, modulus: int) -> int | None:
    divisor = math.gcd(value, modulus)
    return divisor if 1 < divisor < modulus else None


def make_log_table(prime: int, smallest_prime_factor: array) -> tuple[int, list[int]]:
    order_factors = factor_integer(prime - 1, smallest_prime_factor)
    generator = 2
    while any(pow(generator, (prime - 1) // divisor, prime) == 1 for divisor in order_factors):
        generator += 1
    table = [-1] * prime
    value = 1
    for exponent in range(prime - 1):
        if table[value] != -1:
            raise AssertionError("primitive-root table repeated early")
        table[value] = exponent
        value = value * generator % prime
    if value != 1 or any(table[residue] < 0 for residue in range(1, prime)):
        raise AssertionError("incomplete discrete-log table")
    return generator, table


def enumerate_subgroup(modulus: int, generators: list[int]) -> list[int]:
    subgroup = {1}
    queue = deque([1])
    reduced_generators = [generator % modulus for generator in generators]
    while queue:
        residue = queue.popleft()
        for generator in reduced_generators:
            candidate = residue * generator % modulus
            if candidate not in subgroup:
                subgroup.add(candidate)
                queue.append(candidate)
    return sorted(subgroup)


def selected_indices(combination: int) -> list[int]:
    indices: list[int] = []
    remaining = combination
    while remaining:
        bit = remaining & -remaining
        indices.append(bit.bit_length() - 1)
        remaining ^= bit
    return indices


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)

    started = time.monotonic()

    primality = bytearray(b"\x01") * (PRIME_MAX + 1)
    primality[0:2] = b"\x00\x00"
    for candidate in range(2, math.isqrt(PRIME_MAX) + 1):
        if primality[candidate]:
            primality[candidate * candidate : PRIME_MAX + 1 : candidate] = b"\x00" * (
                (PRIME_MAX - candidate * candidate) // candidate + 1
            )
    primes = [value for value in range(2, PRIME_MAX + 1) if primality[value]]
    corpus_primes = [value for value in primes if value >= PRIME_MIN]

    pair_count_before_trial_gate = 0
    corpus: list[tuple[int, int, int, int]] = []
    for p_index, p in enumerate(corpus_primes):
        for q in corpus_primes[p_index + 1 :]:
            if q > 2 * p:
                break
            pair_count_before_trial_gate += 1
            modulus = p * q
            n = modulus.bit_length()
            if p > n * n and q > n * n:
                corpus.append((modulus, p, q, n))
    corpus.sort()

    maximum_modulus = max(modulus for modulus, _, _, _ in corpus)
    smallest_prime_factor = array("I", [0]) * (maximum_modulus + 1)
    for prime in primes:
        for multiple in range(prime * prime, maximum_modulus + 1, prime):
            if smallest_prime_factor[multiple] == 0:
                smallest_prime_factor[multiple] = prime

    log_tables: dict[int, tuple[int, list[int]]] = {}
    records: list[dict[str, object]] = []
    feasible_count = 0
    size_skipped_count = 0
    direct_positive_count = 0
    relation_positive_count = 0
    decisive_null: dict[str, object] | None = None

    for corpus_index, (modulus, p, q, n) in enumerate(corpus):
        generators: set[int] = set()
        initial_direct_hit_count = 0
        first_initial_direct_hit: dict[str, int | str] | None = None
        for seed in range(2, n + 1):
            inverse = pow(seed, -1, modulus)
            for sign, tested in (("minus", seed - inverse), ("plus", seed + inverse)):
                divisor = proper_gcd(tested, modulus)
                if divisor is not None:
                    initial_direct_hit_count += 1
                    if first_initial_direct_hit is None:
                        first_initial_direct_hit = {
                            "seed": seed,
                            "inverse": inverse,
                            "screen": sign,
                            "gcd": divisor,
                        }
            generators.update(factor_integer(seed, smallest_prime_factor))
            generators.update(factor_integer(inverse, smallest_prime_factor))

        sorted_generators = sorted(generators)
        if any(math.gcd(generator, modulus) != 1 for generator in sorted_generators):
            raise AssertionError("nonunit rational-prime generator")
        generator_hash = sha256_text(",".join(map(str, sorted_generators)))

        if p not in log_tables:
            log_tables[p] = make_log_table(p, smallest_prime_factor)
        if q not in log_tables:
            log_tables[q] = make_log_table(q, smallest_prime_factor)
        primitive_p, logs_p = log_tables[p]
        primitive_q, logs_q = log_tables[q]

        vectors: list[tuple[int, int]] = [(p - 1, 0), (0, q - 1)]
        lattice_index = (p - 1) * (q - 1)
        for generator in sorted_generators:
            vector = (logs_p[generator % p], logs_q[generator % q])
            if vector[0] < 0 or vector[1] < 0:
                raise AssertionError("missing local discrete logarithm")
            for prior in vectors:
                lattice_index = math.gcd(
                    lattice_index,
                    abs(prior[0] * vector[1] - prior[1] * vector[0]),
                )
            vectors.append(vector)
            if lattice_index == 1:
                break
        if lattice_index <= 0 or (p - 1) * (q - 1) % lattice_index:
            raise AssertionError("invalid lattice index")
        subgroup_size = (p - 1) * (q - 1) // lattice_index

        record: dict[str, object] = {
            "corpus_index_zero_based": corpus_index,
            "N": modulus,
            "p": p,
            "q": q,
            "n": n,
            "trial_hard_p_gt_n2": p > n * n,
            "trial_hard_q_gt_n2": q > n * n,
            "initial_direct_hit_count": initial_direct_hit_count,
            "first_initial_direct_hit": first_initial_direct_hit,
            "generator_count": len(sorted_generators),
            "generators_sha256": generator_hash,
            "primitive_root_p": primitive_p,
            "primitive_root_q": primitive_q,
            "lattice_index": lattice_index,
            "subgroup_size": subgroup_size,
            "feasible": subgroup_size <= R,
        }

        if subgroup_size > R:
            size_skipped_count += 1
            records.append(record)
        else:
            feasible_count += 1
            subgroup = enumerate_subgroup(modulus, sorted_generators)
            if len(subgroup) != subgroup_size:
                raise AssertionError(
                    f"lattice/enumeration mismatch for N={modulus}: "
                    f"{subgroup_size} != {len(subgroup)}"
                )
            if any(math.gcd(residue, modulus) != 1 for residue in subgroup):
                raise AssertionError("enumerated subgroup contains a nonunit")

            direct_hit_count = 0
            first_direct_hit: dict[str, int | str] | None = None
            exact_values: dict[int, tuple[int, int]] = {}
            for residue in subgroup:
                inverse = pow(residue, -1, modulus)
                for sign, tested in (("minus", residue - inverse), ("plus", residue + inverse)):
                    divisor = proper_gcd(tested, modulus)
                    if divisor is not None:
                        direct_hit_count += 1
                        if first_direct_hit is None:
                            first_direct_hit = {
                                "c": residue,
                                "w": inverse,
                                "screen": sign,
                                "gcd": divisor,
                            }
                exact_values.setdefault(residue * inverse, (residue, inverse))

            relations: list[dict[str, object]] = []
            for value, (residue, inverse) in sorted(exact_values.items()):
                factors = Counter(factor_integer(residue, smallest_prime_factor))
                factors.update(factor_integer(inverse, smallest_prime_factor))
                factorization = sorted((int(prime), int(exponent)) for prime, exponent in factors.items())
                if multiply_factorization(dict(factorization)) != value:
                    raise AssertionError("incorrect exact P factorization")
                if value % modulus != 1 % modulus:
                    raise AssertionError("relation is not 1 modulo N")
                relations.append(
                    {
                        "P": value,
                        "c": residue,
                        "w": inverse,
                        "factorization": factorization,
                    }
                )

            row_index: dict[int, int] = {}
            signatures: list[int] = []
            for relation in relations:
                signature = 0
                for prime, exponent in relation["factorization"]:  # type: ignore[index]
                    if exponent % 2:
                        if prime not in row_index:
                            row_index[prime] = len(row_index)
                        signature ^= 1 << row_index[prime]
                signatures.append(signature)

            pivots: dict[int, tuple[int, int]] = {}
            dependency_records: list[dict[str, object]] = []
            dependency_digest = hashlib.sha256()
            first_relation_witness: dict[str, object] | None = None
            root_classes: Counter[str] = Counter()

            for column, original_signature in enumerate(signatures):
                signature = original_signature
                combination = 1 << column
                while signature:
                    pivot = signature.bit_length() - 1
                    prior = pivots.get(pivot)
                    if prior is None:
                        pivots[pivot] = (signature, combination)
                        break
                    signature ^= prior[0]
                    combination ^= prior[1]
                if signature:
                    continue

                indices = selected_indices(combination)
                exponent_totals: Counter[int] = Counter()
                exact_product = 1
                for selected in indices:
                    relation = relations[selected]
                    exact_product *= int(relation["P"])
                    exponent_totals.update(
                        {int(prime): int(exponent) for prime, exponent in relation["factorization"]}  # type: ignore[index]
                    )
                if any(exponent % 2 for exponent in exponent_totals.values()):
                    raise AssertionError("dependent parity column has odd exact exponent")
                root_factorization = [
                    (int(prime), int(exponent // 2))
                    for prime, exponent in sorted(exponent_totals.items())
                    if exponent
                ]
                positive_root = multiply_factorization(dict(root_factorization))
                if positive_root * positive_root != exact_product:
                    raise AssertionError("incorrect exact positive square root")
                root_modulus = positive_root % modulus
                if root_modulus * root_modulus % modulus != 1:
                    raise AssertionError("decoded root is not square-one modulo N")
                local_p = root_modulus % p
                local_q = root_modulus % q
                if local_p == 1 and local_q == 1:
                    classification = "global_plus"
                elif local_p == p - 1 and local_q == q - 1:
                    classification = "global_minus"
                elif local_p in (1, p - 1) and local_q in (1, q - 1):
                    classification = "non_global"
                else:
                    raise AssertionError("square-one root has invalid local signs")
                gcd_minus = math.gcd(root_modulus - 1, modulus)
                gcd_plus = math.gcd(root_modulus + 1, modulus)
                if classification == "non_global" and not (
                    1 < gcd_minus < modulus or 1 < gcd_plus < modulus
                ):
                    raise AssertionError("non-global root did not expose a factor")

                dependency = {
                    "combination_hex": format(combination, "x"),
                    "selected_count": len(indices),
                    "selected_indices_sha256": sha256_text(",".join(map(str, indices))),
                    "root_factorization": root_factorization,
                    "positive_root_bit_length": positive_root.bit_length(),
                    "positive_root_sha256": integer_sha256(positive_root),
                    "root_mod_N": root_modulus,
                    "root_mod_p": local_p,
                    "root_mod_q": local_q,
                    "classification": classification,
                    "gcd_root_minus_1_N": gcd_minus,
                    "gcd_root_plus_1_N": gcd_plus,
                }
                dependency_digest.update(
                    (json.dumps(dependency, sort_keys=True, separators=(",", ":")) + "\n").encode()
                )
                dependency_records.append(dependency)
                root_classes[classification] += 1
                if classification == "non_global" and first_relation_witness is None:
                    first_relation_witness = dict(dependency)
                    first_relation_witness["selected_columns_zero_based"] = indices
                    first_relation_witness["positive_root"] = str(positive_root)

            rank = len(pivots)
            nullity = len(relations) - rank
            if nullity != len(dependency_records):
                raise AssertionError("online dependencies do not form a kernel basis")

            relation_digest = hashlib.sha256()
            for relation in relations:
                relation_digest.update(
                    (json.dumps(relation, sort_keys=True, separators=(",", ":")) + "\n").encode()
                )
            record.update(
                {
                    "enumerated_subgroup_size": len(subgroup),
                    "subgroup_residues_sha256": sha256_text(",".join(map(str, subgroup))),
                    "full_direct_hit_count": direct_hit_count,
                    "first_full_direct_hit": first_direct_hit,
                    "distinct_exact_P_count": len(relations),
                    "exact_P_collision_count": len(subgroup) - len(relations),
                    "relations_sha256": relation_digest.hexdigest(),
                    "parity_row_count": len(row_index),
                    "matrix_rank": rank,
                    "matrix_nullity": nullity,
                    "root_class_counts": dict(sorted(root_classes.items())),
                    "all_basis_roots_global": root_classes["non_global"] == 0,
                    "normalized_root_image_rank": int(root_classes["non_global"] > 0),
                    "dependencies_sha256": dependency_digest.hexdigest(),
                    "first_relation_witness": first_relation_witness,
                }
            )

            if direct_hit_count:
                direct_positive_count += 1
            if first_relation_witness is not None:
                relation_positive_count += 1

            if direct_hit_count == 0 and first_relation_witness is None:
                record["decisive_full_supergroup_null"] = True
                record["complete_certificate"] = {
                    "generators": sorted_generators,
                    "subgroup_residues": subgroup,
                    "relations_in_ascending_P_order": relations,
                    "kernel_basis_dependencies": dependency_records,
                }
                decisive_null = record
                records.append(record)
                print(
                    f"decisive_null N={modulus} p={p} q={q} "
                    f"H={subgroup_size} columns={len(relations)} nullity={nullity}",
                    flush=True,
                )
                break

            record["decisive_full_supergroup_null"] = False
            records.append(record)

        if (corpus_index + 1) % 1000 == 0:
            print(
                f"processed={corpus_index + 1}/{len(corpus)} feasible={feasible_count} "
                f"skipped={size_skipped_count}",
                flush=True,
            )

    result = {
        "run_id": "F124-D01",
        "status": "DECISIVE_NULL" if decisive_null is not None else "COMPLETE_NO_NULL",
        "exact_arithmetic": True,
        "prime_interval": [PRIME_MIN, PRIME_MAX],
        "subgroup_cap_R": R,
        "prime_count_in_interval": len(corpus_primes),
        "pair_count_before_trial_hard_gate": pair_count_before_trial_gate,
        "retained_corpus_count": len(corpus),
        "processed_corpus_count": len(records),
        "stopped_early": decisive_null is not None,
        "unprocessed_corpus_count": len(corpus) - len(records),
        "feasible_subgroup_count": feasible_count,
        "size_skipped_count": size_skipped_count,
        "direct_positive_feasible_count": direct_positive_count,
        "relation_positive_feasible_count": relation_positive_count,
        "decisive_null_N": None if decisive_null is None else decisive_null["N"],
        "records": records,
        "elapsed_seconds": time.monotonic() - started,
    }
    with args.output.open("x", encoding="utf-8") as output:
        json.dump(result, output, indent=2, sort_keys=True)
        output.write("\n")
    print(
        f"status={result['status']} processed={len(records)}/{len(corpus)} "
        f"feasible={feasible_count} elapsed={result['elapsed_seconds']:.6f}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
