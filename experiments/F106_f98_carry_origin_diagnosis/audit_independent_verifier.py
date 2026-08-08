#!/usr/bin/env python3
"""Independent hostile verifier for the fixed F106 diagnosis.

This verifier does not import or execute the candidate implementation.  It
uses set-valued GF(2) rows, breadth-first graph traversal, and explicit
step-by-step canonical trajectories.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_prime_64(value: int) -> bool:
    if value < 2:
        return False
    for small in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % small == 0:
            return value == small
    odd_part = value - 1
    twos = 0
    while odd_part % 2 == 0:
        twos += 1
        odd_part //= 2
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


def gf2_rank(rows: list[set[int]]) -> int:
    """Set/symmetric-difference elimination with lowest pivots."""
    basis: dict[int, set[int]] = {}
    for source in rows:
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
    """Build a hyperedge incidence graph and traverse it with BFS."""
    neighbors = [set() for _ in range(width)]
    for support in supports:
        ordered = sorted(support)
        if not ordered:
            continue
        anchor = ordered[0]
        for column in ordered[1:]:
            neighbors[anchor].add(column)
            neighbors[column].add(anchor)
    unseen = set(range(width))
    sizes = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        frontier = [start]
        size = 0
        while frontier:
            column = frontier.pop()
            size += 1
            for other in neighbors[column]:
                if other in unseen:
                    unseen.remove(other)
                    frontier.append(other)
        sizes.append(size)
    return sorted(sizes, reverse=True)


def support_stats(supports: list[set[int]], width: int) -> dict[str, object]:
    row_rank = gf2_rank(supports)
    return {
        "rows": len(supports),
        "rank": row_rank,
        "nullity": width - row_rank,
        "components": component_sizes(supports, width),
    }


def provenance_bucket(record: dict[str, object]) -> tuple[object, ...]:
    provenance = record["provenance"]
    if provenance["kind"] == "initial_seed":
        return ("seed", provenance["seed"])
    return (
        "feedback",
        provenance["round"],
        provenance["active_relation_index_zero_based"],
        provenance["orientation"],
    )


def feedback_bucket(record: dict[str, object]) -> tuple[object, ...] | None:
    provenance = record["provenance"]
    if provenance["kind"] != "feedback_trajectory":
        return None
    return (
        provenance["round"],
        provenance["active_relation_index_zero_based"],
        provenance["orientation"],
    )


def connected_by_edges(occurrences: set[int], edges: set[tuple[int, int]]) -> bool:
    if not edges:
        return False
    neighbors = {column: set() for column in occurrences}
    for left, right in edges:
        neighbors[left].add(right)
        neighbors[right].add(left)
    reached = {min(occurrences)}
    frontier = list(reached)
    while frontier:
        column = frontier.pop()
        for other in neighbors[column]:
            if other not in reached:
                reached.add(other)
                frontier.append(other)
    return reached == occurrences


def build_row_data(
    prime_supports: dict[int, set[int]],
    records: list[dict[str, object]],
    carry_edges: dict[int, set[tuple[int, int]]],
) -> dict[int, dict[str, object]]:
    result = {}
    for prime, support in prime_supports.items():
        buckets = {provenance_bucket(records[column]) for column in support}
        edges = carry_edges.get(prime, set())
        result[prime] = {
            "support": set(support),
            "degree": len(support),
            "trajectory_count": len(buckets),
            "carry_edges": set(edges),
            "carry_connected": connected_by_edges(support, edges),
        }
    return result


def category_statistics(
    row_data: dict[int, dict[str, object]], width: int, bound: int
) -> dict[str, dict[str, object]]:
    predicates = {
        "all": lambda p, data: True,
        "small_at_most_n_squared": lambda p, data: p <= bound,
        "large_above_n_squared": lambda p, data: p > bound,
        "has_carry_edge": lambda p, data: bool(data["carry_edges"]),
        "carry_connected": lambda p, data: bool(data["carry_connected"]),
        "no_carry_edge": lambda p, data: not data["carry_edges"],
        "one_trajectory": lambda p, data: data["trajectory_count"] == 1,
        "cross_trajectory": lambda p, data: data["trajectory_count"] > 1,
        "large_cross_trajectory": lambda p, data: p > bound and data["trajectory_count"] > 1,
    }
    return {
        name: support_stats(
            [data["support"] for prime, data in sorted(row_data.items()) if predicate(prime, data)],
            width,
        )
        for name, predicate in predicates.items()
    }


def row_class_counts(row_data: dict[int, dict[str, object]], bound: int) -> dict[str, int]:
    counts = Counter()
    for prime, data in row_data.items():
        key = "|".join(
            (
                "small" if prime <= bound else "large",
                "carry" if data["carry_edges"] else "noncarry",
                "cross" if data["trajectory_count"] > 1 else "local",
            )
        )
        counts[key] += 1
    return dict(sorted(counts.items()))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate-dir", type=Path, required=True)
    parser.add_argument("--f98", type=Path, required=True)
    parser.add_argument("--f100", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()

    candidate_dir = arguments.candidate_dir.resolve()
    f98_path = arguments.f98.resolve()
    f100_path = arguments.f100.resolve()
    output_path = arguments.output.resolve()
    public = json.loads(f98_path.read_text(encoding="utf-8"))
    factor_assisted = json.loads(f100_path.read_text(encoding="utf-8"))
    candidate = json.loads((candidate_dir / "OUTPUT.json").read_text(encoding="utf-8"))
    candidate_r01 = json.loads(
        (candidate_dir / "OUTPUT_R01_ADJACENT_ONLY.json").read_text(encoding="utf-8")
    )

    checks = 0
    failures: list[str] = []

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(label)

    certificate = public["decoder"]["first_useful_certificate"]
    records = certificate["witness_records"]
    factorizations = factor_assisted["relation_factorizations"]
    width = len(records)
    modulus = public["N"]
    bit_length = modulus.bit_length()
    public_bound = bit_length * bit_length
    check(width == 166, "public certificate does not have 166 records")
    check(len(factorizations) == width, "factorization list length differs from certificate")
    check(certificate["support"] == width, "public support field differs from record count")
    check(factor_assisted["certificate_size"] == width, "F100 certificate size differs")
    check(public["B"] == public_bound == 784, "public bound is not n squared = 784")
    check(factor_assisted["N"] == modulus, "F98 and F100 moduli differ")

    prime_supports: dict[int, set[int]] = defaultdict(set)
    odd_support_by_column: list[set[int]] = []
    for column, (record, factorization) in enumerate(zip(records, factorizations)):
        check(record["P"] == record["c"] * record["w"], f"column {column}: P != c*w")
        check(record["P"] == factorization["P"], f"column {column}: F98/F100 P mismatch")
        check(1 <= record["c"] < modulus, f"column {column}: c is not canonical")
        check(1 <= record["w"] < modulus, f"column {column}: w is not canonical")
        check(math.gcd(record["c"], modulus) == 1, f"column {column}: c is not a unit")
        check(record["c"] * record["w"] % modulus == 1, f"column {column}: w is not c inverse")
        product = 1
        derived_odd_support = set()
        previous_prime = 1
        for prime, exponent in factorization["factors"]:
            check(prime > previous_prime, f"column {column}: factors are not strictly sorted")
            check(is_prime_64(prime), f"column {column}: composite factor {prime}")
            check(exponent > 0, f"column {column}: nonpositive exponent for {prime}")
            previous_prime = prime
            product *= prime**exponent
            c_copy = record["c"]
            c_valuation = 0
            while c_copy % prime == 0:
                c_copy //= prime
                c_valuation += 1
            w_copy = record["w"]
            w_valuation = 0
            while w_copy % prime == 0:
                w_copy //= prime
                w_valuation += 1
            check(
                c_valuation + w_valuation == exponent,
                f"column {column}: endpoint valuation mismatch for {prime}",
            )
            if exponent & 1:
                derived_odd_support.add(prime)
                prime_supports[prime].add(column)
        check(product == record["P"], f"column {column}: incomplete factorization")
        check(
            sorted(derived_odd_support) == factorization["odd_valuation_support"],
            f"column {column}: odd valuation support mismatch",
        )
        odd_support_by_column.append(derived_odd_support)

    check(all(len(support) % 2 == 0 for support in prime_supports.values()), "all-column vector fails")
    check(2 in prime_supports, "factor 2 parity row is absent")

    trajectory_columns: dict[tuple[object, ...], dict[int, int]] = defaultdict(dict)
    trajectory_parameters: dict[tuple[object, ...], tuple[int, int, str]] = {}
    for column, record in enumerate(records):
        provenance = record["provenance"]
        if provenance["kind"] == "initial_seed":
            seed = provenance["seed"]
            check(record["c"] == seed, f"column {column}: initial seed c mismatch")
            continue
        check(provenance["kind"] == "feedback_trajectory", f"column {column}: unknown provenance")
        active_index = provenance["active_relation_index_zero_based"]
        check(0 <= active_index < len(public["active_pairs"]), f"column {column}: active index out of range")
        check(
            public["active_pairs"][active_index] == [provenance["u"], provenance["v"]],
            f"column {column}: active pair provenance mismatch",
        )
        check(provenance["round"] == 1, f"column {column}: unexpected feedback round")
        orientation = provenance["orientation"]
        exponent = provenance["exponent"]
        if orientation == "u_power_times_v":
            expected_c = pow(provenance["u"], exponent, modulus) * provenance["v"] % modulus
            multiplier = provenance["u"]
            fixed = provenance["v"]
        elif orientation == "u_times_v_power":
            expected_c = provenance["u"] * pow(provenance["v"], exponent, modulus) % modulus
            multiplier = provenance["v"]
            fixed = provenance["u"]
        else:
            expected_c = -1
            multiplier = -1
            fixed = -1
            check(False, f"column {column}: unknown orientation")
        check(record["c"] == expected_c, f"column {column}: c disagrees with provenance")
        key = feedback_bucket(record)
        assert key is not None
        check(exponent not in trajectory_columns[key], f"trajectory {key}: repeated selected exponent {exponent}")
        trajectory_columns[key][exponent] = column
        parameters = (multiplier, fixed, orientation)
        check(
            key not in trajectory_parameters or trajectory_parameters[key] == parameters,
            f"trajectory {key}: inconsistent parameters",
        )
        trajectory_parameters[key] = parameters

    trajectory_states: dict[tuple[object, ...], dict[int, tuple[int, int]]] = {}
    trajectory_carries: dict[tuple[object, ...], dict[int, tuple[int, int]]] = {}
    for key, exponent_columns in sorted(trajectory_columns.items(), key=str):
        multiplier, fixed, orientation = trajectory_parameters[key]
        states = {}
        for exponent in range(public["B"] + 1):
            if orientation == "u_power_times_v":
                c_value = pow(multiplier, exponent, modulus) * fixed % modulus
            else:
                c_value = fixed * pow(multiplier, exponent, modulus) % modulus
            states[exponent] = (c_value, pow(c_value, -1, modulus))
        carries = {}
        for exponent in range(public["B"]):
            c_value, w_value = states[exponent]
            next_c, next_w = states[exponent + 1]
            c_numerator = multiplier * c_value - next_c
            w_numerator = multiplier * next_w - w_value
            check(c_numerator % modulus == 0, f"trajectory {key}, e={exponent}: nonintegral c carry")
            check(w_numerator % modulus == 0, f"trajectory {key}, e={exponent}: nonintegral w carry")
            c_carry = c_numerator // modulus
            w_carry = w_numerator // modulus
            check(0 <= c_carry < multiplier, f"trajectory {key}, e={exponent}: c carry out of range")
            check(0 <= w_carry < multiplier, f"trajectory {key}, e={exponent}: w carry out of range")
            carries[exponent] = (c_carry, w_carry)
        for exponent, column in exponent_columns.items():
            check(
                states[exponent] == (records[column]["c"], records[column]["w"]),
                f"trajectory {key}, e={exponent}: selected state mismatch",
            )
        trajectory_states[key] = states
        trajectory_carries[key] = carries

    all_round_one_parameters = {}
    for active_index, (u_value, v_value) in enumerate(public["active_pairs"]):
        all_round_one_parameters[(1, active_index, "u_power_times_v")] = (
            u_value,
            v_value,
            "u_power_times_v",
        )
        all_round_one_parameters[(1, active_index, "u_times_v_power")] = (
            v_value,
            u_value,
            "u_times_v_power",
        )
    all_round_one_states = {}
    all_round_one_carries = {}
    all_round_one_two_zero_pairs = 0
    for key, (multiplier, fixed, orientation) in all_round_one_parameters.items():
        states = {}
        for exponent in range(public["B"] + 1):
            if orientation == "u_power_times_v":
                c_value = pow(multiplier, exponent, modulus) * fixed % modulus
            else:
                c_value = fixed * pow(multiplier, exponent, modulus) % modulus
            states[exponent] = (c_value, pow(c_value, -1, modulus))
        carries = {}
        for exponent in range(public["B"]):
            c_value, w_value = states[exponent]
            next_c, next_w = states[exponent + 1]
            c_carry = (multiplier * c_value - next_c) // modulus
            w_carry = (multiplier * next_w - w_value) // modulus
            carries[exponent] = (c_carry, w_carry)
            all_round_one_two_zero_pairs += c_carry == 0 and w_carry == 0
        all_round_one_states[key] = states
        all_round_one_carries[key] = carries

    adjacent_edges: dict[int, set[tuple[int, int]]] = defaultdict(set)
    chain_edges: dict[int, set[tuple[int, int]]] = defaultdict(set)
    adjacent_pair_count = 0
    two_zero_adjacent = 0
    adjacent_state_counts = Counter()
    chain_pair_count = 0
    chain_state_counts = Counter()
    endpoint_equivalence_mismatches = []
    chain_pair_records = []
    for key, exponent_columns in trajectory_columns.items():
        selected = sorted(exponent_columns.items())
        multiplier = trajectory_parameters[key][0]
        states = trajectory_states[key]
        carries = trajectory_carries[key]
        for exponent, left_column in selected:
            if exponent + 1 not in exponent_columns:
                continue
            right_column = exponent_columns[exponent + 1]
            adjacent_pair_count += 1
            c_zero = carries[exponent][0] == 0
            w_zero = carries[exponent][1] == 0
            adjacent_state_counts[f"c_zero={int(c_zero)},w_zero={int(w_zero)}"] += 1
            if c_zero and w_zero:
                two_zero_adjacent += 1
                check(
                    records[left_column]["P"] == records[right_column]["P"],
                    f"trajectory {key}, e={exponent}: two zero carries but unequal P",
                )
            shared = []
            if c_zero:
                shared.append(states[exponent][0])
            if w_zero:
                shared.append(states[exponent + 1][1])
            for prime in odd_support_by_column[left_column] & odd_support_by_column[right_column]:
                if any(value % prime == 0 for value in shared):
                    adjacent_edges[prime].add((left_column, right_column))
        for left_position, (left_exponent, left_column) in enumerate(selected):
            for right_exponent, right_column in selected[left_position + 1 :]:
                c_chain = all(carries[e][0] == 0 for e in range(left_exponent, right_exponent))
                w_chain = all(carries[e][1] == 0 for e in range(left_exponent, right_exponent))
                endpoint_c = states[right_exponent][0] == multiplier ** (
                    right_exponent - left_exponent
                ) * states[left_exponent][0]
                endpoint_w = states[left_exponent][1] == multiplier ** (
                    right_exponent - left_exponent
                ) * states[right_exponent][1]
                if (c_chain, w_chain) != (endpoint_c, endpoint_w):
                    endpoint_equivalence_mismatches.append(
                        [str(key), left_exponent, right_exponent, c_chain, w_chain, endpoint_c, endpoint_w]
                    )
                if not (c_chain or w_chain):
                    continue
                chain_pair_count += 1
                chain_state_counts[f"c_chain={int(c_chain)},w_chain={int(w_chain)}"] += 1
                chain_pair_records.append(
                    {
                        "trajectory": str(key),
                        "left_exponent": left_exponent,
                        "right_exponent": right_exponent,
                        "c_chain": c_chain,
                        "w_chain": w_chain,
                    }
                )
                shared = []
                if c_chain:
                    shared.append(states[left_exponent][0])
                if w_chain:
                    shared.append(states[right_exponent][1])
                for prime in odd_support_by_column[left_column] & odd_support_by_column[right_column]:
                    if any(value % prime == 0 for value in shared):
                        chain_edges[prime].add((left_column, right_column))

    check(not endpoint_equivalence_mismatches, "stepwise and endpoint chain definitions disagree")

    # Broader prime-specific transitive closure.  Every intermediate adjacent
    # relation must share this same prime through a zero carry, but the shared
    # endpoint is allowed to switch between c and w.
    local_path_edges: dict[int, set[tuple[int, int]]] = defaultdict(set)
    mixed_path_examples = []
    for prime, support in sorted(prime_supports.items()):
        for key, exponent_columns in trajectory_columns.items():
            selected_occurrences = sorted(
                (exponent, column)
                for exponent, column in exponent_columns.items()
                if column in support
            )
            states = trajectory_states[key]
            carries = trajectory_carries[key]
            for left_position, (left_exponent, left_column) in enumerate(selected_occurrences):
                for right_exponent, right_column in selected_occurrences[left_position + 1 :]:
                    mechanisms = []
                    step_details = []
                    path_exists = True
                    for exponent in range(left_exponent, right_exponent):
                        c_link = carries[exponent][0] == 0 and states[exponent][0] % prime == 0
                        w_link = carries[exponent][1] == 0 and states[exponent + 1][1] % prime == 0
                        if not (c_link or w_link):
                            path_exists = False
                            break
                        mechanisms.append("cw" if c_link and w_link else "c" if c_link else "w")
                        step_details.append(
                            {
                                "exponent": exponent,
                                "c_link": c_link,
                                "w_link": w_link,
                                "shared_c": states[exponent][0] if c_link else None,
                                "shared_w": states[exponent + 1][1] if w_link else None,
                            }
                        )
                    if path_exists:
                        edge = (left_column, right_column)
                        local_path_edges[prime].add(edge)
                        if edge not in chain_edges.get(prime, set()) and len(mixed_path_examples) < 20:
                            mixed_path_examples.append(
                                {
                                    "prime": prime,
                                    "trajectory": str(key),
                                    "left_exponent": left_exponent,
                                    "right_exponent": right_exponent,
                                    "left_column": left_column,
                                    "right_column": right_column,
                                    "mechanisms": mechanisms,
                                    "steps": step_details,
                                    "intermediate_endpoint_divisibility": {
                                        str(exponent): {
                                            "c_divisible": states[exponent][0] % prime == 0,
                                            "w_divisible": states[exponent][1] % prime == 0,
                                        }
                                        for exponent in range(left_exponent + 1, right_exponent)
                                    },
                                }
                            )

    # Full round-one carry exposure asks a different provenance question: can
    # a prime used by the circuit be exposed at any raw adjacent trajectory
    # pair, even when one or both endpoints are outside the certificate?
    represented_raw_exposed_primes = set()
    represented_raw_exposure_witnesses = {}
    represented_raw_two_zero_pairs = sum(
        carries[exponent] == (0, 0)
        for carries in trajectory_carries.values()
        for exponent in range(public["B"])
    )
    for prime in sorted(prime_supports):
        for key in trajectory_columns:
            states = trajectory_states[key]
            carries = trajectory_carries[key]
            for exponent in range(public["B"]):
                if carries[exponent] == (0, 0):
                    continue
                c_link = carries[exponent][0] == 0 and states[exponent][0] % prime == 0
                w_link = carries[exponent][1] == 0 and states[exponent + 1][1] % prime == 0
                if c_link or w_link:
                    represented_raw_exposed_primes.add(prime)
                    represented_raw_exposure_witnesses[str(prime)] = {
                        "trajectory": str(key),
                        "exponent": exponent,
                        "mechanism": "cw" if c_link and w_link else "c" if c_link else "w",
                    }
                    break
            if prime in represented_raw_exposed_primes:
                break

    raw_exposed_primes = set()
    raw_exposure_witnesses = {}
    for prime in sorted(prime_supports):
        for key in all_round_one_parameters:
            states = all_round_one_states[key]
            carries = all_round_one_carries[key]
            for exponent in range(public["B"]):
                if carries[exponent] == (0, 0):
                    continue
                c_link = carries[exponent][0] == 0 and states[exponent][0] % prime == 0
                w_link = carries[exponent][1] == 0 and states[exponent + 1][1] % prime == 0
                if c_link or w_link:
                    raw_exposed_primes.add(prime)
                    raw_exposure_witnesses[str(prime)] = {
                        "trajectory": str(key),
                        "exponent": exponent,
                        "mechanism": "cw" if c_link and w_link else "c" if c_link else "w",
                    }
                    break
            if prime in raw_exposed_primes:
                break

    row_data = build_row_data(prime_supports, records, chain_edges)
    adjacent_row_data = build_row_data(prime_supports, records, adjacent_edges)
    path_row_data = build_row_data(prime_supports, records, local_path_edges)
    category_stats = category_statistics(row_data, width, public_bound)
    adjacent_category_stats = category_statistics(adjacent_row_data, width, public_bound)
    path_category_stats = category_statistics(path_row_data, width, public_bound)
    classes = row_class_counts(row_data, public_bound)
    adjacent_classes = row_class_counts(adjacent_row_data, public_bound)

    computed = {
        "N": modulus,
        "n": bit_length,
        "public_bound": public_bound,
        "columns": width,
        "prime_rows": len(prime_supports),
        "full_rank": gf2_rank(list(prime_supports.values())),
        "full_nullity": width - gf2_rank(list(prime_supports.values())),
        "consecutive_selected_pairs": adjacent_pair_count,
        "carry_state_counts": dict(sorted(adjacent_state_counts.items())),
        "two_zero_carry_selected_pairs": two_zero_adjacent,
        "carry_chain_selected_pairs": chain_pair_count,
        "carry_chain_state_counts": dict(sorted(chain_state_counts.items())),
        "row_class_counts": classes,
        "category_stats": category_stats,
        "largest_prime": max(prime_supports),
        "largest_no_carry_prime": max(
            prime for prime, data in row_data.items() if not data["carry_edges"]
        ),
        "degree_two_rows": sum(data["degree"] == 2 for data in row_data.values()),
        "degree_two_with_carry_edge": sum(
            data["degree"] == 2 and bool(data["carry_edges"]) for data in row_data.values()
        ),
    }
    candidate_fields = [
        "N",
        "n",
        "public_bound",
        "columns",
        "prime_rows",
        "full_rank",
        "full_nullity",
        "consecutive_selected_pairs",
        "carry_state_counts",
        "two_zero_carry_selected_pairs",
        "carry_chain_selected_pairs",
        "carry_chain_state_counts",
        "row_class_counts",
        "category_stats",
        "largest_prime",
        "largest_no_carry_prime",
        "degree_two_rows",
        "degree_two_with_carry_edge",
    ]
    candidate_field_matches = {}
    for field in candidate_fields:
        candidate_field_matches[field] = candidate.get(field) == computed[field]
        check(candidate_field_matches[field], f"candidate OUTPUT field mismatch: {field}")

    input_hashes = {
        "experiments/F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json": digest(f98_path),
        "experiments/F100_f98_dependency_structure/OUTPUT.json": digest(f100_path),
    }
    check(candidate["input_hashes"] == input_hashes, "candidate input hash map mismatch")
    check(candidate["role"] == "factor-assisted finite diagnosis", "candidate role changed")
    check(candidate["status"] == "complete", "candidate status is not complete")

    adjacent_computed = {
        "N": modulus,
        "n": bit_length,
        "public_bound": public_bound,
        "columns": width,
        "prime_rows": len(prime_supports),
        "full_rank": computed["full_rank"],
        "full_nullity": computed["full_nullity"],
        "consecutive_selected_pairs": adjacent_pair_count,
        "carry_state_counts": computed["carry_state_counts"],
        "two_zero_carry_selected_pairs": two_zero_adjacent,
        "row_class_counts": adjacent_classes,
        "category_stats": adjacent_category_stats,
        "largest_prime": max(prime_supports),
        "largest_no_carry_prime": max(
            prime for prime, data in adjacent_row_data.items() if not data["carry_edges"]
        ),
        "degree_two_rows": computed["degree_two_rows"],
        "degree_two_with_carry_edge": sum(
            data["degree"] == 2 and bool(data["carry_edges"])
            for data in adjacent_row_data.values()
        ),
    }
    r01_field_matches = {}
    for field, value in adjacent_computed.items():
        r01_field_matches[field] = candidate_r01.get(field) == value
        check(r01_field_matches[field], f"R01 field mismatch: {field}")
    check(candidate_r01["input_hashes"] == input_hashes, "R01 input hash map mismatch")
    check(candidate_r01["role"] == candidate["role"], "R01 role mismatch")
    check(candidate_r01["status"] == "complete", "R01 status is not complete")

    for output_name, log_name in (
        ("OUTPUT.json", "RUN.log"),
        ("OUTPUT_R01_ADJACENT_ONLY.json", "RUN_R01_ADJACENT_ONLY.log"),
    ):
        logged = (candidate_dir / log_name).read_text(encoding="utf-8")
        match = re.search(r"stdout:\n(.*)\nstderr:\n", logged, re.DOTALL)
        check(match is not None, f"{log_name}: stdout/stderr framing is absent")
        if match is not None:
            check(
                json.loads(match.group(1))
                == json.loads((candidate_dir / output_name).read_text(encoding="utf-8")),
                f"{log_name}: stdout JSON differs from {output_name}",
            )
        check("exit_code=0" in logged, f"{log_name}: exit code is not zero")

    manifest_text = (candidate_dir / "RUN_MANIFEST.md").read_text(encoding="utf-8")
    manifest_hashes = {}
    for claimed_hash, relative_name in re.findall(r"^([0-9a-f]{64})  (.+)$", manifest_text, re.MULTILINE):
        target = (candidate_dir / relative_name).resolve()
        actual_hash = digest(target)
        manifest_hashes[relative_name] = {
            "claimed": claimed_hash,
            "actual": actual_hash,
            "match": claimed_hash == actual_hash,
        }
        check(claimed_hash == actual_hash, f"manifest hash mismatch: {relative_name}")
    check(len(manifest_hashes) == 10, "candidate manifest does not contain ten hashes")

    check(
        factor_assisted["parity_prime_row_count"] == len(prime_supports),
        "F100 prime row count mismatch",
    )
    check(factor_assisted["rank"] == computed["full_rank"], "F100 rank mismatch")
    check(factor_assisted["nullity"] == computed["full_nullity"], "F100 nullity mismatch")
    check(
        factor_assisted["relation_support_graph_component_sizes"]
        == category_stats["all"]["components"],
        "F100 component mismatch",
    )

    all_chain_pairs = set().union(*chain_edges.values()) if chain_edges else set()
    all_adjacent_pairs = set().union(*adjacent_edges.values()) if adjacent_edges else set()
    all_path_pairs = set().union(*local_path_edges.values()) if local_path_edges else set()
    carry_touched_primes = {prime for prime, edges in chain_edges.items() if edges}
    path_touched_primes = {prime for prime, edges in local_path_edges.items() if edges}
    new_path_primes = sorted(path_touched_primes - carry_touched_primes)
    new_path_edge_labels = sum(
        len(local_path_edges[prime] - chain_edges.get(prime, set()))
        for prime in path_touched_primes
    )

    candidate_carry_supports = [
        data["support"] for data in row_data.values() if data["carry_edges"]
    ]
    candidate_noncarry_supports = [
        data["support"] for data in row_data.values() if not data["carry_edges"]
    ]
    carry_rank = gf2_rank(candidate_carry_supports)
    noncarry_rank = gf2_rank(candidate_noncarry_supports)
    full_rank = computed["full_rank"]
    rank_marginals = {
        "carry_touched_subspace_rank": carry_rank,
        "no_carry_subspace_rank": noncarry_rank,
        "subspace_intersection_dimension": carry_rank + noncarry_rank - full_rank,
        "carry_touched_marginal_over_no_carry": full_rank - noncarry_rank,
        "no_carry_marginal_over_carry_touched": full_rank - carry_rank,
    }

    odd_prime_supports = [support for prime, support in prime_supports.items() if prime != 2]
    odd_prime_row_data = {prime: data for prime, data in row_data.items() if prime != 2}
    strict_feedback_keys = {
        prime: {
            key
            for column in support
            if (key := feedback_bucket(records[column])) is not None
        }
        for prime, support in prime_supports.items()
    }
    strict_cross_primes = {
        prime for prime, keys in strict_feedback_keys.items() if len(keys) > 1
    }
    candidate_cross_primes = {
        prime for prime, data in row_data.items() if data["trajectory_count"] > 1
    }
    seed_primes = sorted(odd_support_by_column[0])
    seed_provenance = {
        str(prime): {
            "support_columns_zero_based": sorted(prime_supports[prime]),
            "feedback_oriented_trajectory_count": len(strict_feedback_keys[prime]),
            "feedback_oriented_trajectories": sorted(map(str, strict_feedback_keys[prime])),
            "candidate_bucket_count": row_data[prime]["trajectory_count"],
        }
        for prime in seed_primes
    }

    candidate_row_pair_slots = sum(
        len(data["support"]) * (len(data["support"]) - 1) // 2
        for data in row_data.values()
        if data["carry_edges"]
    )
    carry_labeled_edges = sum(len(edges) for edges in chain_edges.values())
    carry_incident_occurrences = sum(
        len({column for edge in data["carry_edges"] for column in edge})
        for data in row_data.values()
        if data["carry_edges"]
    )
    carry_touched_occurrences = sum(
        len(data["support"]) for data in row_data.values() if data["carry_edges"]
    )

    raw_exposed_supports = [prime_supports[prime] for prime in sorted(raw_exposed_primes)]
    raw_unexposed_supports = [
        support for prime, support in sorted(prime_supports.items()) if prime not in raw_exposed_primes
    ]
    row_classification = {}
    for prime, data in sorted(row_data.items()):
        row_classification[str(prime)] = {
            "support_columns_zero_based": sorted(data["support"]),
            "degree": data["degree"],
            "odd_prime": prime != 2,
            "size_class": "small" if prime <= public_bound else "large",
            "candidate_provenance_bucket_count": data["trajectory_count"],
            "feedback_oriented_trajectory_count": len(strict_feedback_keys[prime]),
            "uniform_chain_edges": [list(edge) for edge in sorted(data["carry_edges"])],
            "uniform_chain_connected": data["carry_connected"],
            "mixed_endpoint_path_edges": [
                list(edge) for edge in sorted(local_path_edges.get(prime, set()))
            ],
            "raw_round_one_carry_exposed": prime in raw_exposed_primes,
        }
    row_classification_sha256 = hashlib.sha256(
        json.dumps(row_classification, separators=(",", ":"), sort_keys=True).encode()
    ).hexdigest()

    independent = {
        "candidate_definition": computed,
        "adjacent_selected_only": adjacent_computed,
        "odd_prime_only": {
            "rows": len(odd_prime_supports),
            "rank": gf2_rank(odd_prime_supports),
            "nullity": width - gf2_rank(odd_prime_supports),
            "components": component_sizes(odd_prime_supports, width),
            "category_stats": category_statistics(odd_prime_row_data, width, public_bound),
            "prime_2_degree": len(prime_supports[2]),
            "prime_2_class": {
                "has_carry_edge": bool(row_data[2]["carry_edges"]),
                "trajectory_count": row_data[2]["trajectory_count"],
            },
        },
        "pure_carry_edge_graph": {
            "distinct_selected_pairs": len(all_chain_pairs),
            "labeled_prime_edges": carry_labeled_edges,
            "rank_of_two_column_edge_vectors": gf2_rank([set(edge) for edge in all_chain_pairs]),
            "components": component_sizes([set(edge) for edge in all_chain_pairs], width),
        },
        "pure_adjacent_selected_edge_graph": {
            "distinct_selected_pairs": len(all_adjacent_pairs),
            "rank_of_two_column_edge_vectors": gf2_rank([set(edge) for edge in all_adjacent_pairs]),
            "components": component_sizes([set(edge) for edge in all_adjacent_pairs], width),
        },
        "carry_touched_row_contamination": {
            "row_support_pair_slots": candidate_row_pair_slots,
            "carry_labeled_edges": carry_labeled_edges,
            "row_occurrences": carry_touched_occurrences,
            "occurrences_incident_to_a_carry_edge": carry_incident_occurrences,
            "carry_touched_but_not_carry_connected_rows": sum(
                bool(data["carry_edges"]) and not data["carry_connected"]
                for data in row_data.values()
            ),
            "carry_touched_cross_trajectory_rows": sum(
                bool(data["carry_edges"]) and data["trajectory_count"] > 1
                for data in row_data.values()
            ),
        },
        "prime_specific_mixed_endpoint_closure": {
            "touched_rows": len(path_touched_primes),
            "new_rows_beyond_candidate": new_path_primes,
            "new_labeled_edges_beyond_candidate": new_path_edge_labels,
            "distinct_selected_pairs": len(all_path_pairs),
            "category_stats": path_category_stats,
            "examples": mixed_path_examples,
        },
        "full_round_one_raw_carry_exposure": {
            "oriented_trajectories_scanned": len(all_round_one_parameters),
            "exponent_range_inclusive": [0, public["B"]],
            "two_zero_pairs_excluded": all_round_one_two_zero_pairs,
            "exposed_rows": len(raw_exposed_primes),
            "unexposed_rows": len(prime_supports) - len(raw_exposed_primes),
            "exposed_row_stats": support_stats(raw_exposed_supports, width),
            "unexposed_row_stats": support_stats(raw_unexposed_supports, width),
            "witnesses": raw_exposure_witnesses,
        },
        "certificate_trajectory_raw_carry_exposure": {
            "oriented_trajectories_scanned": len(trajectory_columns),
            "two_zero_pairs_excluded": represented_raw_two_zero_pairs,
            "exposed_rows": len(represented_raw_exposed_primes),
            "exposed_row_stats": support_stats(
                [prime_supports[prime] for prime in sorted(represented_raw_exposed_primes)], width
            ),
            "witnesses": represented_raw_exposure_witnesses,
        },
        "rank_marginals": rank_marginals,
        "provenance_variants": {
            "candidate_cross_bucket_rows": len(candidate_cross_primes),
            "strict_multiple_feedback_oriented_trajectory_rows": len(strict_cross_primes),
            "candidate_only_cross_primes": sorted(candidate_cross_primes - strict_cross_primes),
            "strict_cross_row_stats": support_stats(
                [prime_supports[prime] for prime in sorted(strict_cross_primes)], width
            ),
            "strict_odd_cross_row_stats": support_stats(
                [
                    prime_supports[prime]
                    for prime in sorted(strict_cross_primes)
                    if prime != 2
                ],
                width,
            ),
            "strict_large_cross_row_stats": support_stats(
                [
                    prime_supports[prime]
                    for prime in sorted(strict_cross_primes)
                    if prime > public_bound
                ],
                width,
            ),
            "seed_prime_details": seed_provenance,
        },
        "chain_pair_records": chain_pair_records,
        "endpoint_equivalence_mismatches": endpoint_equivalence_mismatches,
        "row_classification_sha256": row_classification_sha256,
        "row_classification": row_classification,
    }

    output = {
        "status": "complete" if not failures else "failed",
        "verifier_status": "PASS" if not failures else "FAIL",
        "candidate_verdict": "FAIL",
        "candidate_verdict_basis": [
            "The stated 230 odd-prime rows include the p=2 row; there are 229 odd-prime rows.",
            "The stated 175 rows spanning oriented trajectories count the initial seed as a trajectory; the strict count is 174.",
            "A prime-specific chain can switch from a c overlap to a w overlap at an even-parity intermediate relation; p=17 is missed by the candidate definition.",
            "The reported carry-row components use every support edge of a carry-touched row, not only exact carry edges.",
            "The phrase 'supply 71 rank units' is not an additive attribution; the carry-touched marginal over no-carry rows is smaller.",
        ],
        "checks": checks,
        "failures": failures,
        "input_hashes": input_hashes,
        "candidate_manifest_hashes": manifest_hashes,
        "candidate_field_matches": candidate_field_matches,
        "r01_field_matches": r01_field_matches,
        "independent": independent,
    }
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
