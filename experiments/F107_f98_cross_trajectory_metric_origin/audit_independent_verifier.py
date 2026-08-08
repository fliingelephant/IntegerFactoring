#!/usr/bin/env python3
"""Independent hostile verifier for the fixed F107 diagnosis.

This file does not import or execute the candidate implementation. It uses
set-valued rows, lowest-pivot symmetric-difference elimination, explicit graph
traversal, and stepwise canonical trajectories.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path


PINNED_F98_SHA256 = "ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab"
PINNED_F100_SHA256 = "9bcf6217f412f837fab8e3d0b832e01c80fbd5afa1d173156ec93df95bd94076"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_prime_64(value: int) -> bool:
    """Deterministic Miller-Rabin for the 64-bit range."""
    if value < 2:
        return False
    for small in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % small == 0:
            return value == small
    odd_part = value - 1
    twos = 0
    while odd_part % 2 == 0:
        odd_part //= 2
        twos += 1
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % value == 0:
            continue
        residue = pow(base, odd_part, value)
        if residue in (1, value - 1):
            continue
        for _ in range(twos - 1):
            residue = residue * residue % value
            if residue == value - 1:
                break
        else:
            return False
    return True


def gf2_rank(supports: list[set[int]]) -> int:
    """Use set symmetric difference and the lowest available pivot."""
    basis: dict[int, set[int]] = {}
    for source in supports:
        row = set(source)
        while row:
            pivot = min(row)
            prior = basis.get(pivot)
            if prior is None:
                basis[pivot] = row
                break
            row.symmetric_difference_update(prior)
    return len(basis)


def component_sizes(supports: list[set[int]], width: int) -> list[int]:
    """Expand each row as a star, then use explicit graph traversal."""
    adjacency = [set() for _ in range(width)]
    for support in supports:
        if not support:
            continue
        anchor = min(support)
        for column in support - {anchor}:
            adjacency[anchor].add(column)
            adjacency[column].add(anchor)
    unseen = set(range(width))
    sizes = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        stack = [start]
        size = 0
        while stack:
            column = stack.pop()
            size += 1
            for other in adjacency[column] & unseen:
                unseen.remove(other)
                stack.append(other)
        sizes.append(size)
    return sorted(sizes, reverse=True)


def edge_component_sizes(edges: set[tuple[int, int]], width: int) -> list[int]:
    adjacency = [set() for _ in range(width)]
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    unseen = set(range(width))
    sizes = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        stack = [start]
        size = 0
        while stack:
            column = stack.pop()
            size += 1
            for other in adjacency[column] & unseen:
                unseen.remove(other)
                stack.append(other)
        sizes.append(size)
    return sorted(sizes, reverse=True)


def support_stats(primes: set[int], rows: dict[int, set[int]], width: int) -> dict[str, object]:
    supports = [rows[prime] for prime in sorted(primes)]
    row_rank = gf2_rank(supports)
    return {
        "rows": len(supports),
        "rank": row_rank,
        "nullity": width - row_rank,
        "components": component_sizes(supports, width),
    }


def trajectory_key(record: dict[str, object]) -> tuple[object, ...] | None:
    provenance = record["provenance"]
    if provenance["kind"] != "feedback_trajectory":
        return None
    return (
        "trajectory",
        provenance["round"],
        provenance["active_relation_index_zero_based"],
        provenance["u"],
        provenance["v"],
        provenance["orientation"],
    )


def source_bucket(record: dict[str, object]) -> tuple[object, ...]:
    provenance = record["provenance"]
    if provenance["kind"] == "initial_seed":
        return ("seed", provenance["seed"])
    return trajectory_key(record)


def key_label(key: tuple[object, ...]) -> str:
    if key[0] == "seed":
        return f"seed:{key[1]}"
    return f"round:{key[1]}:active:{key[2]}:{key[3]}:{key[4]}:{key[5]}"


def key_bases(key: tuple[object, ...]) -> set[int]:
    if key[0] == "seed":
        return {key[1]}
    return {key[3], key[4]}


def classify_rows(
    rows: dict[int, set[int]],
    records: list[dict[str, object]],
    include_seed_bucket: bool,
) -> tuple[dict[int, dict[str, object]], Counter[str]]:
    result = {}
    totals: Counter[str] = Counter()
    for prime, support in sorted(rows.items()):
        keys = set()
        for column in support:
            key = source_bucket(records[column]) if include_seed_bucket else trajectory_key(records[column])
            if key is not None:
                keys.add(key)
        base_pairs = []
        residual_pairs = []
        for left, right in combinations(sorted(keys, key=key_label), 2):
            pair = [key_label(left), key_label(right)]
            shared = key_bases(left) & key_bases(right)
            if any(value % prime == 0 for value in shared):
                base_pairs.append(pair)
                totals["base_inherited"] += 1
            else:
                residual_pairs.append(pair)
                totals["non_base_inherited"] += 1
        result[prime] = {
            "keys": sorted(key_label(key) for key in keys),
            "base_pairs": base_pairs,
            "non_base_pairs": residual_pairs,
        }
    return result, totals


def extract_logged_json(path: Path) -> dict[str, object]:
    text = path.read_text()
    stdout = text.split("stdout:\n", 1)[1].rsplit("\nstderr:\n", 1)[0]
    return json.loads(stdout)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate-dir", type=Path, required=True)
    parser.add_argument("--f98", type=Path, required=True)
    parser.add_argument("--f100", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    candidate_dir = args.candidate_dir.resolve()
    f98_path = args.f98.resolve()
    f100_path = args.f100.resolve()
    output_path = args.output.resolve()
    checks = 0
    verifier_failures: list[str] = []

    def require(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            verifier_failures.append(label)

    candidate_names = (
        "DESIGN.md",
        "RESULT.md",
        "RUN_MANIFEST.md",
        "FAILED_RUNS.md",
        "analyze_metric_origin.py",
        "run_with_timeout.py",
        "OUTPUT.json",
        "RUN.log",
        "OUTPUT_R01.json",
        "RUN_R01.log",
    )
    candidate_paths = {name: candidate_dir / name for name in candidate_names}
    for name, path in candidate_paths.items():
        require(path.is_file(), f"missing candidate artifact: {name}")

    f98_hash = sha256(f98_path)
    f100_hash = sha256(f100_path)
    require(f98_hash == PINNED_F98_SHA256, "F98 input hash changed")
    require(f100_hash == PINNED_F100_SHA256, "F100 input hash changed")

    public = json.loads(f98_path.read_text())
    assisted = json.loads(f100_path.read_text())
    candidate_output = json.loads(candidate_paths["OUTPUT.json"].read_text())
    preliminary_output = json.loads(candidate_paths["OUTPUT_R01.json"].read_text())
    records = public["decoder"]["first_useful_certificate"]["witness_records"]
    factorizations = assisted["relation_factorizations"]
    width = len(records)
    modulus = public["N"]
    bound = public["B"]
    require(width == 166, "certificate does not have 166 columns")
    require(len(factorizations) == width, "factorization count differs from column count")
    require(modulus == 202537109, "fixed modulus changed")
    require(bound == 784, "public bound changed")

    rows: dict[int, set[int]] = defaultdict(set)
    column_primes: list[set[int]] = []
    exact_values = set()
    provenance_counts: Counter[str] = Counter()
    for column, (record, factorization) in enumerate(zip(records, factorizations)):
        require(record["P"] == factorization["P"], f"P mismatch at column {column}")
        require(record["P"] == record["c"] * record["w"], f"endpoint product mismatch at column {column}")
        require(record["c"] * record["w"] % modulus == 1, f"inverse product mismatch at column {column}")
        require(0 < record["c"] < modulus, f"c outside canonical range at column {column}")
        require(0 < record["w"] < modulus, f"w outside canonical range at column {column}")
        require(math.gcd(record["c"], modulus) == 1, f"c is not a unit at column {column}")
        require(math.gcd(record["w"], modulus) == 1, f"w is not a unit at column {column}")
        product = 1
        odd_support = set()
        prior_prime = 1
        for prime, exponent in factorization["factors"]:
            require(prime > prior_prime, f"factor list not strictly increasing at column {column}")
            require(exponent > 0, f"nonpositive exponent at column {column}, prime {prime}")
            require(is_prime_64(prime), f"composite factor at column {column}: {prime}")
            require(modulus % prime != 0, f"row prime divides N at column {column}: {prime}")
            prior_prime = prime
            product *= prime**exponent
            if exponent & 1:
                odd_support.add(prime)
                rows[prime].add(column)
        require(product == record["P"], f"factor product mismatch at column {column}")
        require(odd_support == set(factorization["odd_valuation_support"]), f"odd support mismatch at column {column}")
        column_primes.append(odd_support)
        exact_values.add(record["P"])

        provenance = record["provenance"]
        provenance_counts[provenance["kind"]] += 1
        if provenance["kind"] == "initial_seed":
            require(record["c"] == provenance["seed"], f"seed residue mismatch at column {column}")
            require(record["w"] == pow(record["c"], -1, modulus), f"seed inverse mismatch at column {column}")
        else:
            active_index = provenance["active_relation_index_zero_based"]
            require(public["active_pairs"][active_index] == [provenance["u"], provenance["v"]], f"active pair mismatch at column {column}")
            require(provenance["round"] == 1, f"unexpected round at column {column}")
            require(0 <= provenance["exponent"] <= bound, f"exponent outside public range at column {column}")
            if provenance["orientation"] == "u_power_times_v":
                expected_c = pow(provenance["u"], provenance["exponent"], modulus) * provenance["v"] % modulus
            else:
                require(provenance["orientation"] == "u_times_v_power", f"unknown orientation at column {column}")
                expected_c = provenance["u"] * pow(provenance["v"], provenance["exponent"], modulus) % modulus
            require(record["c"] == expected_c, f"trajectory residue mismatch at column {column}")
            require(record["w"] == pow(expected_c, -1, modulus), f"trajectory inverse mismatch at column {column}")

    require(len(exact_values) == width, "selected exact relation values are not distinct")
    require(provenance_counts == Counter({"feedback_trajectory": 165, "initial_seed": 1}), "provenance counts changed")
    require(len(rows) == 230, "prime-row count changed")
    for prime, support in rows.items():
        require(len(support) % 2 == 0, f"prime row {prime} has odd degree")
    all_primes = set(rows)
    full_stats = support_stats(all_primes, rows, width)
    require(full_stats == {"rows": 230, "rank": 165, "nullity": 1, "components": [166]}, "full row invariant changed")
    require(assisted["rank"] == full_stats["rank"], "F100 rank metadata mismatch")
    require(assisted["parity_prime_row_count"] == len(rows), "F100 row-count metadata mismatch")
    require(assisted["relation_support_graph_component_sizes"] == full_stats["components"], "F100 component metadata mismatch")

    candidate_classes, candidate_pair_totals = classify_rows(rows, records, include_seed_bucket=True)
    strict_classes, strict_pair_totals = classify_rows(rows, records, include_seed_bucket=False)

    base_values = sorted(
        {
            value
            for record in records
            for value in key_bases(source_bucket(record))
        }
    )
    distinct_base_gcds = {
        f"{left}:{right}": math.gcd(left, right)
        for left, right in combinations(base_values, 2)
    }
    require(all(value == 1 for value in distinct_base_gcds.values()), "distinct public bases are not pairwise coprime")

    columns_by_trajectory: dict[tuple[object, ...], list[int]] = defaultdict(list)
    for column, record in enumerate(records):
        key = trajectory_key(record)
        if key is not None:
            columns_by_trajectory[key].append(column)
    require(len(columns_by_trajectory) == 8, "represented feedback-oriented trajectory count changed")

    uniform_edges: dict[int, set[tuple[int, int]]] = defaultdict(set)
    mixed_edges: dict[int, set[tuple[int, int]]] = defaultdict(set)
    represented_states: dict[tuple[object, ...], tuple[dict[int, int], dict[int, int], int]] = {}
    for key, columns in columns_by_trajectory.items():
        _, _, _, u, v, orientation = key
        multiplier = u if orientation == "u_power_times_v" else v
        canonical_c = {}
        canonical_w = {}
        for exponent in range(bound + 1):
            if orientation == "u_power_times_v":
                residue = pow(u, exponent, modulus) * v % modulus
            else:
                residue = u * pow(v, exponent, modulus) % modulus
            canonical_c[exponent] = residue
            canonical_w[exponent] = pow(residue, -1, modulus)
        represented_states[key] = (canonical_c, canonical_w, multiplier)
        ordered = sorted(columns, key=lambda column: (records[column]["provenance"]["exponent"], column))
        for column in ordered:
            exponent = records[column]["provenance"]["exponent"]
            require(records[column]["c"] == canonical_c[exponent], f"stepwise c mismatch at column {column}")
            require(records[column]["w"] == canonical_w[exponent], f"stepwise w mismatch at column {column}")
        for left, right in combinations(ordered, 2):
            left_exponent = records[left]["provenance"]["exponent"]
            right_exponent = records[right]["provenance"]["exponent"]
            shared_primes = column_primes[left] & column_primes[right]
            scale = multiplier ** (right_exponent - left_exponent)
            for prime in shared_primes:
                if (
                    canonical_c[right_exponent] == scale * canonical_c[left_exponent]
                    and canonical_c[left_exponent] % prime == 0
                ) or (
                    canonical_w[left_exponent] == scale * canonical_w[right_exponent]
                    and canonical_w[right_exponent] % prime == 0
                ):
                    uniform_edges[prime].add((left, right))
                mixed_path = True
                for exponent in range(left_exponent, right_exponent):
                    shared_values = []
                    if canonical_c[exponent + 1] == multiplier * canonical_c[exponent]:
                        shared_values.append(canonical_c[exponent])
                    if canonical_w[exponent] == multiplier * canonical_w[exponent + 1]:
                        shared_values.append(canonical_w[exponent + 1])
                    if not any(value % prime == 0 for value in shared_values):
                        mixed_path = False
                        break
                if mixed_path:
                    mixed_edges[prime].add((left, right))

    uniform_primes = set(uniform_edges)
    mixed_primes = set(mixed_edges)
    require(
        all(uniform_edges[prime] <= mixed_edges[prime] for prime in uniform_edges),
        "a uniform endpoint path is missing from the mixed-endpoint reconstruction",
    )

    # A broader origin test scans raw adjacent states, not only selected
    # odd-support endpoints. Two-zero steps are excluded because their two
    # endpoint products are identical and first-occurrence deduplication drops
    # the second raw relation.
    represented_raw_exposed = set()
    represented_raw_witnesses = {}
    represented_two_zero_steps = 0
    for prime in sorted(rows):
        for key, (canonical_c, canonical_w, multiplier) in represented_states.items():
            found = False
            for exponent in range(bound):
                c_zero = canonical_c[exponent + 1] == multiplier * canonical_c[exponent]
                w_zero = canonical_w[exponent] == multiplier * canonical_w[exponent + 1]
                if c_zero and w_zero:
                    continue
                c_link = c_zero and canonical_c[exponent] % prime == 0
                w_link = w_zero and canonical_w[exponent + 1] % prime == 0
                if c_link or w_link:
                    represented_raw_exposed.add(prime)
                    represented_raw_witnesses[str(prime)] = {
                        "trajectory": key_label(key),
                        "exponent": exponent,
                        "mechanism": "cw" if c_link and w_link else "c" if c_link else "w",
                    }
                    found = True
                    break
            if found:
                break
    for canonical_c, canonical_w, multiplier in represented_states.values():
        for exponent in range(bound):
            represented_two_zero_steps += (
                canonical_c[exponent + 1] == multiplier * canonical_c[exponent]
                and canonical_w[exponent] == multiplier * canonical_w[exponent + 1]
            )

    raw_exposed = set()
    raw_witnesses = {}
    all_round_one_two_zero_steps = 0
    all_round_one_trajectory_count = 0
    for active_index, (u, v) in enumerate(public["active_pairs"]):
        for orientation in ("u_power_times_v", "u_times_v_power"):
            all_round_one_trajectory_count += 1
            multiplier = u if orientation == "u_power_times_v" else v
            canonical_c = {}
            canonical_w = {}
            for exponent in range(bound + 1):
                if orientation == "u_power_times_v":
                    residue = pow(u, exponent, modulus) * v % modulus
                else:
                    residue = u * pow(v, exponent, modulus) % modulus
                canonical_c[exponent] = residue
                canonical_w[exponent] = pow(residue, -1, modulus)
            for exponent in range(bound):
                all_round_one_two_zero_steps += (
                    canonical_c[exponent + 1] == multiplier * canonical_c[exponent]
                    and canonical_w[exponent] == multiplier * canonical_w[exponent + 1]
                )
            for prime in sorted(all_primes - raw_exposed):
                for exponent in range(bound):
                    c_zero = canonical_c[exponent + 1] == multiplier * canonical_c[exponent]
                    w_zero = canonical_w[exponent] == multiplier * canonical_w[exponent + 1]
                    if c_zero and w_zero:
                        continue
                    c_link = c_zero and canonical_c[exponent] % prime == 0
                    w_link = w_zero and canonical_w[exponent + 1] % prime == 0
                    if c_link or w_link:
                        raw_exposed.add(prime)
                        raw_witnesses[str(prime)] = {
                            "active_relation_index_zero_based": active_index,
                            "u": u,
                            "v": v,
                            "orientation": orientation,
                            "exponent": exponent,
                            "mechanism": "cw" if c_link and w_link else "c" if c_link else "w",
                        }
                        break
    require(all_round_one_trajectory_count == 54, "round-one oriented trajectory count changed")

    candidate_predicates = {
        "all": lambda prime: True,
        "carry": lambda prime: prime in uniform_primes,
        "cross_any": lambda prime: len(candidate_classes[prime]["keys"]) > 1,
        "base_cross_any": lambda prime: bool(candidate_classes[prime]["base_pairs"]),
        "base_cross_only": lambda prime: bool(candidate_classes[prime]["base_pairs"]) and not candidate_classes[prime]["non_base_pairs"],
        "metric_cross_any": lambda prime: bool(candidate_classes[prime]["non_base_pairs"]),
        "metric_cross_only": lambda prime: bool(candidate_classes[prime]["non_base_pairs"]) and not candidate_classes[prime]["base_pairs"],
        "metric_cross_no_carry": lambda prime: bool(candidate_classes[prime]["non_base_pairs"]) and prime not in uniform_primes,
        "metric_cross_only_no_carry": lambda prime: bool(candidate_classes[prime]["non_base_pairs"]) and not candidate_classes[prime]["base_pairs"] and prime not in uniform_primes,
        "carry_or_base_cross": lambda prime: prime in uniform_primes or bool(candidate_classes[prime]["base_pairs"]),
        "neither_carry_nor_base_cross": lambda prime: prime not in uniform_primes and not candidate_classes[prime]["base_pairs"],
    }
    candidate_category_stats = {
        name: support_stats({prime for prime in rows if predicate(prime)}, rows, width)
        for name, predicate in candidate_predicates.items()
    }
    candidate_metric_primes = {prime for prime in rows if candidate_classes[prime]["non_base_pairs"]}
    expected_candidate_output = {
        "status": "complete",
        "role": "factor-assisted fixed-circuit diagnosis",
        "input_hashes": {
            "experiments/F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json": f98_hash,
            "experiments/F100_f98_dependency_structure/OUTPUT.json": f100_hash,
        },
        "columns": width,
        "prime_rows": len(rows),
        "rank": full_stats["rank"],
        "cross_key_pair_counts_with_row_multiplicity": {
            "base_inherited": candidate_pair_totals["base_inherited"],
            "metric": candidate_pair_totals["non_base_inherited"],
        },
        "category_stats": candidate_category_stats,
        "metric_cross_prime_min": min(candidate_metric_primes),
        "metric_cross_prime_max": max(candidate_metric_primes),
        "metric_cross_primes_above_784": sum(prime > bound for prime in candidate_metric_primes),
        "base_cross_primes": sorted(prime for prime in rows if candidate_classes[prime]["base_pairs"]),
    }
    require(candidate_output == expected_candidate_output, "candidate OUTPUT.json differs from independent narrow reconstruction")

    strict_predicates = {
        "cross_any": lambda prime: len(strict_classes[prime]["keys"]) > 1,
        "base_cross_any": lambda prime: bool(strict_classes[prime]["base_pairs"]),
        "base_cross_only": lambda prime: bool(strict_classes[prime]["base_pairs"]) and not strict_classes[prime]["non_base_pairs"],
        "non_base_cross_any": lambda prime: bool(strict_classes[prime]["non_base_pairs"]),
        "non_base_cross_only": lambda prime: bool(strict_classes[prime]["non_base_pairs"]) and not strict_classes[prime]["base_pairs"],
        "non_base_cross_no_uniform_carry": lambda prime: bool(strict_classes[prime]["non_base_pairs"]) and prime not in uniform_primes,
        "non_base_cross_only_no_uniform_carry": lambda prime: bool(strict_classes[prime]["non_base_pairs"]) and not strict_classes[prime]["base_pairs"] and prime not in uniform_primes,
        "non_base_cross_no_mixed_carry": lambda prime: bool(strict_classes[prime]["non_base_pairs"]) and prime not in mixed_primes,
        "non_base_cross_only_no_mixed_carry": lambda prime: bool(strict_classes[prime]["non_base_pairs"]) and not strict_classes[prime]["base_pairs"] and prime not in mixed_primes,
        "neither_mixed_carry_nor_base_cross": lambda prime: prime not in mixed_primes and not strict_classes[prime]["base_pairs"],
    }
    strict_category_stats = {
        name: support_stats({prime for prime in rows if predicate(prime)}, rows, width)
        for name, predicate in strict_predicates.items()
    }
    strict_metric_primes = {prime for prime in rows if strict_classes[prime]["non_base_pairs"]}

    candidate_log_json = extract_logged_json(candidate_paths["RUN.log"])
    preliminary_log_json = extract_logged_json(candidate_paths["RUN_R01.log"])
    require(candidate_log_json == candidate_output, "authoritative run log JSON differs from OUTPUT.json")
    require(preliminary_log_json == preliminary_output, "preliminary run log JSON differs from OUTPUT_R01.json")
    require("exit_code=0" in candidate_paths["RUN.log"].read_text(), "authoritative candidate log is not exit zero")
    require("exit_code=0" in candidate_paths["RUN_R01.log"].read_text(), "preliminary candidate log is not exit zero")

    preliminary_field_matches = {}
    for field, value in preliminary_output.items():
        if field == "category_stats":
            matches = {
                name: statistic == candidate_category_stats.get(name)
                for name, statistic in value.items()
            }
            preliminary_field_matches[field] = matches
            for name, match in matches.items():
                require(match, f"preliminary category {name} does not reproduce")
        else:
            match = value == expected_candidate_output.get(field)
            preliminary_field_matches[field] = match
            require(match, f"preliminary field {field} does not reproduce")

    manifest_text = candidate_paths["RUN_MANIFEST.md"].read_text()
    declared_hashes = re.findall(r"^([0-9a-f]{64})  (.+)$", manifest_text, flags=re.MULTILINE)
    manifest_hash_matches = {}
    for declared, relative in declared_hashes:
        target = (candidate_dir / relative).resolve()
        match = target.is_file() and sha256(target) == declared
        manifest_hash_matches[relative] = match
        require(match, f"candidate manifest hash mismatch: {relative}")
    require(len(declared_hashes) == 10, "candidate manifest does not declare ten expected hashes")

    candidate_artifact_hashes = {
        name: sha256(path) for name, path in candidate_paths.items()
    }

    row_classification = {}
    for prime, support in sorted(rows.items()):
        row_classification[str(prime)] = {
            "support_columns_zero_based": sorted(support),
            "degree": len(support),
            "above_public_bound": prime > bound,
            "incident_to_initial_seed": 0 in support,
            "candidate_source_buckets": candidate_classes[prime]["keys"],
            "candidate_base_pairs": candidate_classes[prime]["base_pairs"],
            "candidate_non_base_pairs": candidate_classes[prime]["non_base_pairs"],
            "strict_feedback_trajectories": strict_classes[prime]["keys"],
            "strict_base_pairs": strict_classes[prime]["base_pairs"],
            "strict_non_base_pairs": strict_classes[prime]["non_base_pairs"],
            "uniform_endpoint_carry_edges": [list(edge) for edge in sorted(uniform_edges[prime])],
            "mixed_endpoint_carry_edges": [list(edge) for edge in sorted(mixed_edges[prime])],
        }
    row_classification_hash = hashlib.sha256(
        json.dumps(row_classification, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    candidate_metric_labelled_edges = []
    strict_metric_labelled_edges = []
    candidate_metric_column_edges = set()
    strict_metric_column_edges = set()
    for prime, support in rows.items():
        for left, right in combinations(sorted(support), 2):
            left_candidate = source_bucket(records[left])
            right_candidate = source_bucket(records[right])
            if left_candidate != right_candidate:
                shared = key_bases(left_candidate) & key_bases(right_candidate)
                if not any(value % prime == 0 for value in shared):
                    candidate_metric_labelled_edges.append((prime, left, right))
                    candidate_metric_column_edges.add((left, right))
            left_strict = trajectory_key(records[left])
            right_strict = trajectory_key(records[right])
            if left_strict is not None and right_strict is not None and left_strict != right_strict:
                shared = key_bases(left_strict) & key_bases(right_strict)
                if not any(value % prime == 0 for value in shared):
                    strict_metric_labelled_edges.append((prime, left, right))
                    strict_metric_column_edges.add((left, right))

    strict_neutral_primes = {
        prime
        for prime in rows
        if strict_classes[prime]["non_base_pairs"]
        and not strict_classes[prime]["base_pairs"]
        and prime not in mixed_primes
    }
    strict_complement = all_primes - strict_neutral_primes
    strict_neutral_rank = gf2_rank([rows[prime] for prime in strict_neutral_primes])
    strict_complement_rank = gf2_rank([rows[prime] for prime in strict_complement])

    raw_scope_sets = {
        "candidate_non_base_cross_no_represented_raw_exposure": {
            prime for prime in candidate_metric_primes if prime not in represented_raw_exposed
        },
        "candidate_non_base_cross_no_full_raw_exposure": {
            prime for prime in candidate_metric_primes if prime not in raw_exposed
        },
        "strict_non_base_cross_no_represented_raw_exposure": {
            prime for prime in strict_metric_primes if prime not in represented_raw_exposed
        },
        "strict_non_base_cross_no_full_raw_exposure": {
            prime for prime in strict_metric_primes if prime not in raw_exposed
        },
        "strict_non_base_cross_only_no_full_raw_exposure": {
            prime
            for prime in strict_metric_primes
            if not strict_classes[prime]["base_pairs"] and prime not in raw_exposed
        },
    }

    result_text = candidate_paths["RESULT.md"].read_text()
    wording_audit = {
        "operational_meaning": "a residual trajectory-key pair for which no exact shared public base integer is divisible by the row prime",
        "randomness_disclaimer_present": "does not mean that the overlap is random" in result_text,
        "fixed_circuit_disclaimer_present": "one 28-bit diagnosis" in result_text,
        "asymptotic_disclaimer_present": "no lower bound on the frequency" in result_text,
        "positive_effect_wording_present": all(
            phrase in result_text
            for phrase in ("mostly a metric integer effect", "metric presentation effect")
        ),
        "not_established": [
            "a metric-space property",
            "randomness, rarity, independence, or a birthday law",
            "a statistical correlation with either nontrivial factor of N",
            "a causal origin for every occurrence in a selected row",
            "frequency on unselected relations or other inputs",
        ],
    }
    require(wording_audit["randomness_disclaimer_present"], "candidate lacks its stated randomness disclaimer")
    require(wording_audit["fixed_circuit_disclaimer_present"], "candidate lacks a fixed-circuit disclaimer")
    require(wording_audit["asymptotic_disclaimer_present"], "candidate lacks an asymptotic disclaimer")

    semantic_findings = {
        "seed_is_not_a_feedback_trajectory": len(candidate_metric_primes) != len(strict_metric_primes),
        "uniform_endpoint_rule_misses_exact_mixed_paths": any(
            mixed_edges[prime] != uniform_edges[prime] for prime in mixed_edges
        ),
        "selected_pair_carry_scope_is_not_an_origin_complete_scope": (
            support_stats(raw_exposed, rows, width)["rank"] == full_stats["rank"]
            and raw_exposed != uniform_primes
        ),
        "metric_is_only_a_negative_residual_label": wording_audit["positive_effect_wording_present"],
    }
    candidate_verdict = "FAIL" if any(semantic_findings.values()) else "PASS"

    new_mixed_edges = {
        str(prime): [list(edge) for edge in sorted(mixed_edges[prime] - uniform_edges[prime])]
        for prime in sorted(mixed_edges)
        if mixed_edges[prime] != uniform_edges[prime]
    }
    new_mixed_path_details = []
    for prime in sorted(mixed_edges):
        for left, right in sorted(mixed_edges[prime] - uniform_edges[prime]):
            key = trajectory_key(records[left])
            canonical_c, canonical_w, multiplier = represented_states[key]
            left_exponent = records[left]["provenance"]["exponent"]
            right_exponent = records[right]["provenance"]["exponent"]
            steps = []
            for exponent in range(left_exponent, right_exponent):
                c_link = (
                    canonical_c[exponent + 1] == multiplier * canonical_c[exponent]
                    and canonical_c[exponent] % prime == 0
                )
                w_link = (
                    canonical_w[exponent] == multiplier * canonical_w[exponent + 1]
                    and canonical_w[exponent + 1] % prime == 0
                )
                steps.append({
                    "exponent": exponent,
                    "mechanism": "cw" if c_link and w_link else "c" if c_link else "w",
                    "shared_c": canonical_c[exponent] if c_link else None,
                    "shared_w": canonical_w[exponent + 1] if w_link else None,
                })
            new_mixed_path_details.append({
                "prime": prime,
                "trajectory": key_label(key),
                "left_column": left,
                "right_column": right,
                "left_exponent": left_exponent,
                "right_exponent": right_exponent,
                "steps": steps,
            })
    output = {
        "status": "complete",
        "verifier_status": "PASS" if not verifier_failures else "FAIL",
        "candidate_verdict": candidate_verdict,
        "checks": checks,
        "verifier_failures": verifier_failures,
        "input_hashes": {
            "experiments/F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json": f98_hash,
            "experiments/F100_f98_dependency_structure/OUTPUT.json": f100_hash,
        },
        "candidate_artifact_hashes": candidate_artifact_hashes,
        "candidate_manifest_hash_matches": manifest_hash_matches,
        "candidate_output_exact_match_under_its_rules": candidate_output == expected_candidate_output,
        "preliminary_field_matches": preliminary_field_matches,
        "full_circuit": full_stats,
        "public_base_audit": {
            "distinct_values": base_values,
            "pairwise_gcds": distinct_base_gcds,
            "distinct_values_are_pairwise_coprime": all(value == 1 for value in distinct_base_gcds.values()),
        },
        "candidate_nine_source_bucket_reconstruction": {
            "source_bucket_count": len({source_bucket(record) for record in records}),
            "pair_counts_with_row_multiplicity": dict(sorted(candidate_pair_totals.items())),
            "base_cross_primes": sorted(prime for prime in rows if candidate_classes[prime]["base_pairs"]),
            "metric_prime_min": min(candidate_metric_primes),
            "metric_prime_max": max(candidate_metric_primes),
            "metric_primes_above_public_bound": sum(prime > bound for prime in candidate_metric_primes),
            "category_stats": candidate_category_stats,
        },
        "strict_feedback_trajectory_reconstruction": {
            "feedback_oriented_trajectory_count": len(columns_by_trajectory),
            "pair_counts_with_row_multiplicity": dict(sorted(strict_pair_totals.items())),
            "base_cross_primes": sorted(prime for prime in rows if strict_classes[prime]["base_pairs"]),
            "non_base_prime_min": min(strict_metric_primes),
            "non_base_prime_max": max(strict_metric_primes),
            "non_base_primes_above_public_bound": sum(prime > bound for prime in strict_metric_primes),
            "category_stats": strict_category_stats,
        },
        "carry_reconstruction": {
            "uniform_endpoint": {
                "primes": len(uniform_primes),
                "prime_labelled_edges": sum(len(edges) for edges in uniform_edges.values()),
                "distinct_column_edges": len({edge for edges in uniform_edges.values() for edge in edges}),
                "stats": support_stats(uniform_primes, rows, width),
            },
            "mixed_endpoint": {
                "primes": len(mixed_primes),
                "prime_labelled_edges": sum(len(edges) for edges in mixed_edges.values()),
                "distinct_column_edges": len({edge for edges in mixed_edges.values() for edge in edges}),
                "stats": support_stats(mixed_primes, rows, width),
            },
            "new_mixed_endpoint_edges": new_mixed_edges,
            "new_mixed_endpoint_path_details": new_mixed_path_details,
        },
        "raw_round_one_carry_exposure": {
            "meaning": "a circuit-row prime divides an exact shared endpoint at any distinct adjacent raw relation pair",
            "represented_eight_trajectories": {
                "trajectory_count": len(represented_states),
                "two_zero_duplicate_steps_excluded": represented_two_zero_steps,
                "exposed_primes": len(represented_raw_exposed),
                "exposed_stats": support_stats(represented_raw_exposed, rows, width),
                "unexposed_stats": support_stats(all_primes - represented_raw_exposed, rows, width),
                "witnesses": represented_raw_witnesses,
            },
            "all_round_one_trajectories": {
                "trajectory_count": all_round_one_trajectory_count,
                "two_zero_duplicate_steps_excluded": all_round_one_two_zero_steps,
                "exposed_primes": len(raw_exposed),
                "exposed_stats": support_stats(raw_exposed, rows, width),
                "unexposed_stats": support_stats(all_primes - raw_exposed, rows, width),
                "witnesses": raw_witnesses,
            },
            "non_base_row_sets_after_raw_exposure_exclusion": {
                name: support_stats(primes, rows, width)
                for name, primes in raw_scope_sets.items()
            },
        },
        "pure_non_base_occurrence_graphs": {
            "candidate_source_bucket_graph": {
                "prime_labelled_edges": len(candidate_metric_labelled_edges),
                "distinct_column_edges": len(candidate_metric_column_edges),
                "components": edge_component_sizes(candidate_metric_column_edges, width),
            },
            "strict_feedback_trajectory_graph": {
                "prime_labelled_edges": len(strict_metric_labelled_edges),
                "distinct_column_edges": len(strict_metric_column_edges),
                "components": edge_component_sizes(strict_metric_column_edges, width),
            },
        },
        "strict_neutral_partition_rank": {
            "non_base_cross_only_no_mixed_carry_rows": len(strict_neutral_primes),
            "non_base_cross_only_no_mixed_carry_rank": strict_neutral_rank,
            "complement_rows": len(strict_complement),
            "complement_rank": strict_complement_rank,
            "full_rank": full_stats["rank"],
            "span_intersection_dimension": strict_neutral_rank + strict_complement_rank - full_stats["rank"],
            "neutral_subset_marginal_over_complement": full_stats["rank"] - strict_complement_rank,
            "complement_marginal_over_neutral_subset": full_stats["rank"] - strict_neutral_rank,
        },
        "wording_audit": wording_audit,
        "semantic_findings": semantic_findings,
        "required_corrections": [
            "Either rename the candidate's cross-trajectory objects as nine provenance/source buckets, or use the strict eight feedback-oriented trajectories and the corrected strict statistics.",
            "Replace the uniform-endpoint carry exclusion with the prime-specific stepwise mixed-endpoint exclusion, or call the existing class uniform-endpoint carry-touched rows.",
            "State that the carry exclusion is selected-pair-local. Do not use it as an origin-complete contrast: raw adjacent carry exposure spans the full fixed circuit.",
            "Use non-base-inherited integer overlap as the neutral term. If metric is retained, define it as an audit-local residual label and do not present it as a positive causal effect.",
            "State ranks and components as properties of complete selected row supports. Do not treat subset rank as an additive causal allocation.",
        ],
        "row_classification_sha256": row_classification_hash,
        "row_classification": row_classification,
    }
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "candidate_verdict": candidate_verdict,
        "checks": checks,
        "row_classification_sha256": row_classification_hash,
        "verifier_failures": verifier_failures,
        "verifier_status": output["verifier_status"],
    }, indent=2, sort_keys=True))
    return 0 if not verifier_failures else 1


if __name__ == "__main__":
    sys.exit(main())
