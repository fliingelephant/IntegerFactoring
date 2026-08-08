#!/usr/bin/env python3
"""Independent factor-free audit of the F116 sparse-DAG first-case certificate."""

from __future__ import annotations

import argparse
import ast
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import time
import traceback


EXPECTED_INPUT_SHA256 = "5194ee596916810edb78fa802c3179341746423c6fb65f2548a600c598b05015"
EXPECTED_STATEMENT_SHA256 = "f402a39c9d751a72c93a46b28ab593c5a1e8a03ed4c9bdc97655b310c01e8983"
EXPECTED_CANDIDATE_SOURCE_SHA256 = "7a65e664d9cdca422da47a5d26bd22432ce2eee5c61f8b3db5541bd348e81b84"
EXPECTED_CANDIDATE_OUTPUT_SHA256 = "17f909113a0777695adec24c9e5619eaef1fec2327987e7e26c3212d04397671"
EXPECTED_CANDIDATE_LOG_SHA256 = "6f5542bc618f921ff81129939509a1e47d694dc1c0492a7da050b4cc0885f542"


class VerificationFailure(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationFailure(message)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_root(value: int, exponent: int) -> int | None:
    low = 1
    high = 2
    while high**exponent < value:
        high *= 2
    while low <= high:
        middle = (low + high) // 2
        power = middle**exponent
        if power == value:
            return middle
        if power < value:
            low = middle + 1
        else:
            high = middle - 1
    return None


def primitive_power(value: int) -> tuple[int, int]:
    for exponent in range(value.bit_length(), 1, -1):
        root = exact_root(value, exponent)
        if root is not None:
            return root, exponent
    return value, 1


def initial_gcd_basis(
    endpoints: list[int],
) -> tuple[list[tuple[int, dict[int, int]]], dict[str, int]]:
    pending = [
        (value, {endpoint_index: 1})
        for endpoint_index, value in enumerate(endpoints)
        if value > 1
    ]
    basis: list[tuple[int, dict[int, int]]] = []
    stats = {
        "gcd_calls": 0,
        "overlap_splits": 0,
        "perfect_power_splits": 0,
        "identical_merges": 0,
    }
    while pending:
        value, signature = pending.pop()
        if value == 1:
            continue
        root, power = primitive_power(value)
        if power > 1:
            value = root
            signature = {
                endpoint: power * exponent for endpoint, exponent in signature.items()
            }
            stats["perfect_power_splits"] += 1
        for position, (old_value, old_signature) in enumerate(basis):
            stats["gcd_calls"] += 1
            divisor = math.gcd(value, old_value)
            if divisor == 1:
                continue
            basis.pop(position)
            if value == old_value:
                merged = dict(signature)
                for endpoint, exponent in old_signature.items():
                    merged[endpoint] = merged.get(endpoint, 0) + exponent
                pending.append((value, merged))
                stats["identical_merges"] += 1
                break
            pending.extend(
                (
                    (divisor, signature),
                    (value // divisor, signature),
                    (divisor, old_signature),
                    (old_value // divisor, old_signature),
                )
            )
            stats["overlap_splits"] += 1
            break
        else:
            basis.append((value, signature))

    basis.sort(key=lambda item: item[0])
    reconstructed = [1] * len(endpoints)
    for position, (block, signature) in enumerate(basis):
        require(primitive_power(block)[1] == 1, "public basis retains a perfect power")
        require(
            all(math.gcd(block, old_block) == 1 for old_block, _ in basis[:position]),
            "public basis is not pairwise coprime",
        )
        for endpoint, exponent in signature.items():
            reconstructed[endpoint] *= block**exponent
    require(reconstructed == endpoints, "public basis does not reconstruct seed endpoints")
    return basis, stats


def unsigned_bytes(value: int) -> bytes:
    return value.to_bytes(max(1, (value.bit_length() + 7) // 8), "big")


def feed_uint(digest: object, value: int) -> None:
    encoded = unsigned_bytes(value)
    digest.update(len(encoded).to_bytes(2, "big"))
    digest.update(encoded)


def sparse_dag_mechanics_audit() -> dict[str, object]:
    modulus = 35
    rows = [
        {2: 1, 53: 1},
        {2: 2, 3: 1, 41: 1, 53: 1},
        {2: 4, 3: 3, 41: 1, 53: 1},
    ]
    values = [math.prod(base**exponent for base, exponent in row.items()) for row in rows]
    require(values == [106, 26076, 938736], "symbolic fixture changed")
    require(all(value % modulus == 1 for value in values), "fixture relation is not one modulo M")

    pivots: dict[int, tuple[set[int], int, int, set[int]]] = {}
    left: list[int] = []
    right: list[int] = []
    dense_nodes: list[set[int]] = []
    invariant_checks = 0
    dependency: dict[str, object] | None = None

    def check_state(parity: set[int], half_root: int, support: set[int]) -> None:
        nonlocal invariant_checks
        exponents: Counter[int] = Counter()
        for relation in support:
            exponents.update(rows[relation])
        expected_parity = {base for base, exponent in exponents.items() if exponent & 1}
        expected_half = 1
        for base, exponent in exponents.items():
            expected_half = expected_half * pow(base, exponent // 2, modulus) % modulus
        require(parity == expected_parity, "sparse parity differs from dense XOR expression")
        require(half_root == expected_half, "online modular half-root invariant failed")
        invariant_checks += 1

    for relation_index, factors in enumerate(rows):
        parity = {base for base, exponent in factors.items() if exponent & 1}
        half_root = 1
        for base, exponent in factors.items():
            half_root = half_root * pow(base, exponent // 2, modulus) % modulus
        expression = -relation_index - 1
        support = {relation_index}
        check_state(parity, half_root, support)
        while parity:
            pivot = max(parity)
            known = pivots.get(pivot)
            if known is None:
                pivots[pivot] = (set(parity), expression, half_root, set(support))
                break
            known_parity, known_expression, known_half_root, known_support = known
            common = parity.intersection(known_parity)
            half_root = half_root * known_half_root % modulus
            for base in common:
                half_root = half_root * base % modulus
            parity.symmetric_difference_update(known_parity)
            left.append(expression)
            right.append(known_expression)
            support.symmetric_difference_update(known_support)
            dense_nodes.append(set(support))
            expression = len(left) - 1
            check_state(parity, half_root, support)
        else:
            active_nodes = bytearray(len(left))
            recovered: set[int] = set()

            def toggle(reference: int) -> None:
                if reference < 0:
                    column = -reference - 1
                    if column in recovered:
                        recovered.remove(column)
                    else:
                        recovered.add(column)
                else:
                    active_nodes[reference] ^= 1

            toggle(expression)
            for node in range(len(left) - 1, -1, -1):
                if active_nodes[node]:
                    require(left[node] < node and right[node] < node, "DAG is not topological")
                    toggle(left[node])
                    toggle(right[node])
            require(recovered == support == dense_nodes[expression], "DAG support recovery failed")
            product = math.prod(values[index] for index in recovered)
            root = math.isqrt(product)
            require(root * root == product, "synthetic dependency product is not square")
            require(root % modulus == half_root, "dependency root differs from online half root")
            dependency = {
                "support_indices_zero_based": sorted(recovered),
                "exact_root_modulus": root % modulus,
                "online_half_root_modulus": half_root,
                "non_global": half_root not in (1, modulus - 1),
            }

    require(dependency is not None, "symbolic sparse audit found no dependency")
    require(dependency["support_indices_zero_based"] == [1, 2], "shared leaf did not cancel")
    require(dependency["non_global"], "symbolic dependency is global")
    return {
        "status": "PASS",
        "method": "independent sparse implementation checked against dense XOR exponent sums",
        "modulus": modulus,
        "relation_values": values,
        "pivot_count": len(pivots),
        "dag_node_count": len(left),
        "invariant_checks": invariant_checks,
        "dependency": dependency,
        "shared_leaf_cancellation_checked": True,
    }


def audit(
    input_path: Path,
    statement_path: Path,
    candidate_source_path: Path,
    candidate_output_path: Path,
    candidate_log_path: Path,
) -> dict[str, object]:
    started = time.monotonic()
    require(sha256_file(input_path) == EXPECTED_INPUT_SHA256, "reconstruction input hash changed")
    require(sha256_file(statement_path) == EXPECTED_STATEMENT_SHA256, "statement hash changed")
    input_data = json.loads(input_path.read_text())
    require(
        set(input_data)
        == {"N", "n", "bound", "source_stop_relation_count", "dependency_relation_indices_zero_based"},
        "unexpected reconstruction input field",
    )
    modulus = int(input_data["N"])
    n = int(input_data["n"])
    bound = int(input_data["bound"])
    stop = int(input_data["source_stop_relation_count"])
    advised_support = [int(index) for index in input_data["dependency_relation_indices_zero_based"]]
    require(n == modulus.bit_length(), "input bit length is wrong")
    require(bound == n * n, "input bound is wrong")
    require(
        advised_support == sorted(set(advised_support)),
        "advised support is not strictly increasing and distinct",
    )
    require(advised_support and advised_support[-1] == stop - 1, "support does not end at stop")
    require(advised_support[0] >= 0 and advised_support[-1] < stop, "support is out of range")
    support_set = set(advised_support)

    phase = time.monotonic()
    trial_distribution: Counter[int] = Counter(
        math.gcd(trial, modulus) for trial in range(2, bound + 1)
    )
    require(
        sum(count for divisor, count in trial_distribution.items() if 1 < divisor < modulus) == 0,
        "trial screen found a proper divisor",
    )

    seen_residues: set[int] = set()
    exact_first_coordinate: dict[int, int] = {}
    coordinate_shift = stop.bit_length()
    coordinate_mask = (1 << coordinate_shift) - 1
    selected_value_parity: set[int] = set()
    selected_value_source_indices: dict[int, list[int]] = {}
    attempted = 0
    duplicates = 0
    retained = 0
    exact_units = 0
    exact_duplicates = 0
    selected_units = 0
    residue_gcd_distribution: Counter[int] = Counter()
    endpoint_gcd_distribution: Counter[int] = Counter()
    proper_direct: list[dict[str, object]] = []
    source_digest = hashlib.sha256()
    support_record_digest = hashlib.sha256()
    raw_support_product = 1
    support_kind_counts: Counter[str] = Counter()
    support_appended_pairs: set[tuple[int, int]] = set()
    seed_endpoints: list[int] = []
    seed_records = 0

    def retain(
        residue: int,
        kind: str,
        pair_index: int,
        left_value: int,
        right_value: int,
        exponent: int,
        orientation: int,
        seed: int,
    ) -> bool:
        nonlocal attempted, duplicates, retained, exact_units, exact_duplicates
        nonlocal selected_units, raw_support_product, seed_records
        attempted += 1
        if residue in seen_residues:
            duplicates += 1
            return False
        require(0 < residue < modulus, "source residue is not canonical")
        seen_residues.add(residue)
        residue_gcd = math.gcd(residue, modulus)
        residue_gcd_distribution[residue_gcd] += 1
        if 1 < residue_gcd < modulus:
            proper_direct.append(
                {"channel": "noninvertible_residue", "gcd": residue_gcd, "index": retained}
            )
            return True
        require(residue_gcd == 1, "source residue is zero modulo N")
        inverse = pow(residue, -1, modulus)
        for sign, difference in (("minus", residue - inverse), ("plus", residue + inverse)):
            divisor = math.gcd(difference, modulus)
            endpoint_gcd_distribution[divisor] += 1
            if 1 < divisor < modulus:
                proper_direct.append(
                    {"channel": f"endpoint_{sign}", "gcd": divisor, "index": retained}
                )
                return True

        value = residue * inverse
        require(value % modulus == 1, "relation value is not one modulo N")
        source_index = retained
        kind_code = {"initial_seed": 0, "frozen_seed_basis_pair": 1, "nonadaptive_seed_pair": 2}[kind]
        for field in (
            source_index,
            residue,
            inverse,
            value,
            kind_code,
            pair_index + 1,
            left_value,
            right_value,
            exponent,
            orientation,
            seed,
        ):
            feed_uint(source_digest, field)
        if kind == "initial_seed":
            seed_endpoints.extend((residue, inverse))
            seed_records += 1

        if value == 1:
            exact_units += 1
        elif value in exact_first_coordinate:
            exact_duplicates += 1
        else:
            exact_first_coordinate[value] = (
                len(exact_first_coordinate) << coordinate_shift
            ) | source_index

        if source_index in support_set:
            raw_support_product *= value
            support_kind_counts[kind] += 1
            if kind == "nonadaptive_seed_pair":
                support_appended_pairs.add((left_value, right_value))
            for field in (
                source_index,
                residue,
                inverse,
                value,
                kind_code,
                pair_index + 1,
                left_value,
                right_value,
                exponent,
                orientation,
                seed,
            ):
                feed_uint(support_record_digest, field)
            if value == 1:
                selected_units += 1
            else:
                selected_value_source_indices.setdefault(value, []).append(source_index)
                if value in selected_value_parity:
                    selected_value_parity.remove(value)
                else:
                    selected_value_parity.add(value)

        retained += 1
        return retained == stop

    for seed in range(2, n + 1):
        reached = retain(seed, "initial_seed", -1, 0, 0, 0, 0, seed)
        require(not reached, "source stop occurred in seed layer")
    require(seed_records == n - 1, "seed record count is wrong")
    basis, basis_stats = initial_gcd_basis(seed_endpoints)
    frozen_pairs: list[tuple[int, int]] = []
    for relation in range(seed_records):
        support = sorted(
            block
            for block, signature in basis
            if 2 * relation in signature or 2 * relation + 1 in signature
        )
        require(support, "seed relation has empty public support")
        frozen_pairs.append((support[0], 1) if len(support) == 1 else (support[0], support[1]))

    reached = False
    for pair_index, (left_value, right_value) in enumerate(frozen_pairs):
        for exponent in range(bound + 1):
            reached = retain(
                pow(left_value, exponent, modulus) * right_value % modulus,
                "frozen_seed_basis_pair",
                pair_index,
                left_value,
                right_value,
                exponent,
                0,
                0,
            )
            if not reached:
                reached = retain(
                    left_value * pow(right_value, exponent, modulus) % modulus,
                    "frozen_seed_basis_pair",
                    pair_index,
                    left_value,
                    right_value,
                    exponent,
                    1,
                    0,
                )
            require(not reached, "source stop occurred in frozen layer")
    frozen_attempted = attempted
    frozen_duplicates = duplicates
    frozen_retained = retained

    menu_attempted = 0
    stop_pair: tuple[int, int] | None = None
    for left_value in range(2, n + 1):
        if reached:
            break
        for right_value in range(left_value + 1, n + 1):
            menu_index = menu_attempted
            menu_attempted += 1
            for exponent in range(bound + 1):
                reached = retain(
                    pow(left_value, exponent, modulus) * right_value % modulus,
                    "nonadaptive_seed_pair",
                    menu_index,
                    left_value,
                    right_value,
                    exponent,
                    0,
                    0,
                )
                if not reached:
                    reached = retain(
                        left_value * pow(right_value, exponent, modulus) % modulus,
                        "nonadaptive_seed_pair",
                        menu_index,
                        left_value,
                        right_value,
                        exponent,
                        1,
                        0,
                    )
                if reached:
                    stop_pair = (left_value, right_value)
                    break
            if reached:
                break
    require(reached and retained == stop, "source did not reach the exact advised stop")
    require(attempted - duplicates == retained, "residue dedup accounting failed")
    require(not proper_direct, "a proper direct gcd precedes the advised dependency")
    require(len(support_set) == len(advised_support), "support set collapsed an index")

    source_seconds = time.monotonic() - phase
    phase = time.monotonic()
    raw_root = math.isqrt(raw_support_product)
    require(raw_root * raw_root == raw_support_product, "advised raw product is not a square")
    raw_root_modulus = raw_root % modulus
    require(pow(raw_root_modulus, 2, modulus) == 1, "raw root does not square to one")
    require(raw_root_modulus not in (1, modulus - 1), "advised raw root is global")

    projected_entries = sorted(
        (
            exact_first_coordinate[value] >> coordinate_shift,
            exact_first_coordinate[value] & coordinate_mask,
            selected_value_source_indices[value],
        )
        for value in selected_value_parity
    )
    projected_columns = [column for column, _, _ in projected_entries]
    projected_first_source_indices = [source for _, source, _ in projected_entries]
    require(
        selected_units == 0
        and len(selected_value_source_indices) == len(advised_support)
        and all(len(indices) == 1 for indices in selected_value_source_indices.values()),
        "advised support values are not distinct nonunits",
    )
    projected_selected_source_indices = [indices[0] for _, _, indices in projected_entries]
    coordinate_identity_count = sum(
        first == selected
        for first, selected in zip(
            projected_first_source_indices, projected_selected_source_indices, strict=True
        )
    )
    projected_product = math.prod(selected_value_parity)
    projected_root = math.isqrt(projected_product)
    require(
        projected_root * projected_root == projected_product,
        "exact-value projected product is not a square",
    )
    projected_root_modulus = projected_root % modulus
    require(projected_root_modulus == raw_root_modulus, "exact-value projection changed root class")
    require(projected_columns, "useful raw dependency projected to zero")

    minus = math.gcd(raw_root_modulus - 1, modulus)
    plus = math.gcd(raw_root_modulus + 1, modulus)
    require(1 < minus < modulus and 1 < plus < modulus, "terminal gcd is not a proper split")
    require(minus * plus == modulus, "terminal gcds do not multiply to N")
    support_seconds = time.monotonic() - phase

    phase = time.monotonic()
    mechanics = sparse_dag_mechanics_audit()
    mechanics_seconds = time.monotonic() - phase

    # Discovery artifacts are read only after the terminal gcds above exist.
    require(
        sha256_file(candidate_source_path) == EXPECTED_CANDIDATE_SOURCE_SHA256,
        "candidate source hash changed",
    )
    require(
        sha256_file(candidate_output_path) == EXPECTED_CANDIDATE_OUTPUT_SHA256,
        "candidate output hash changed",
    )
    require(sha256_file(candidate_log_path) == EXPECTED_CANDIDATE_LOG_SHA256, "candidate log hash changed")
    candidate = json.loads(candidate_output_path.read_text())
    require(candidate["status"] == "PASS", "candidate discovery did not report PASS")
    require(int(candidate["case"]["N"]) == modulus, "candidate modulus differs")
    discovered_factors = sorted((int(candidate["case"]["p"]), int(candidate["case"]["q"])))
    require(discovered_factors == sorted((minus, plus)), "terminal gcds differ from known factors")
    candidate_support = [
        int(index)
        for index in candidate["factor_free_support_replay"]["source_indices_zero_based"]
    ]
    require(candidate_support == advised_support, "candidate and advised supports differ")
    require(candidate["frozen"]["pairs"] == [list(pair) for pair in frozen_pairs], "frozen pairs differ")
    require(int(candidate["frozen"]["retained_relations"]) == frozen_retained, "frozen retained count differs")
    require(int(candidate["frozen"]["attempted_residues"]) == frozen_attempted, "frozen attempt count differs")
    require(int(candidate["frozen"]["duplicate_residues"]) == frozen_duplicates, "frozen duplicate count differs")
    require(int(candidate["source_at_stop"]["retained_relations"]) == retained, "stop count differs")
    require(int(candidate["source_at_stop"]["attempted_residues"]) == attempted, "attempt count differs")
    require(int(candidate["source_at_stop"]["duplicate_residues"]) == duplicates, "duplicate count differs")
    require(candidate["menu"]["successful_pair"] == list(stop_pair or ()), "stop pair differs")
    require(int(candidate["menu"]["attempted_pairs"]) == menu_attempted, "menu pair count differs")
    candidate_replay = candidate["factor_free_support_replay"]
    require(int(candidate_replay["root_mod_N"]) == raw_root_modulus, "candidate root differs")
    require(int(candidate_replay["gcd_root_minus_one_N"]) == minus, "candidate minus gcd differs")
    require(int(candidate_replay["gcd_root_plus_one_N"]) == plus, "candidate plus gcd differs")
    require(
        candidate_replay["source_indices_sha256"]
        == hashlib.sha256(json.dumps(advised_support, separators=(",", ":")).encode()).hexdigest(),
        "candidate support hash differs",
    )
    raw_product_bytes = unsigned_bytes(raw_support_product)
    raw_root_bytes = unsigned_bytes(raw_root)
    require(
        candidate_replay["exact_product_unsigned_big_endian_sha256"]
        == hashlib.sha256(raw_product_bytes).hexdigest(),
        "candidate exact product hash differs",
    )
    require(
        candidate_replay["positive_root_unsigned_big_endian_sha256"]
        == hashlib.sha256(raw_root_bytes).hexdigest(),
        "candidate positive root hash differs",
    )
    decoder = candidate["decoder"]
    require(
        int(decoder["pivot_count"]) + int(decoder["dependencies"]) == retained,
        "candidate sparse rank/dependency accounting fails",
    )
    require(int(decoder["dag_node_count"]) == int(decoder["eliminations"]), "candidate DAG accounting fails")
    require(
        int(decoder["global_dependencies"]) + 1 == int(decoder["dependencies"]),
        "candidate dependency class accounting fails",
    )

    verifier_source = Path(__file__).read_text()
    tree = ast.parse(verifier_source)
    calls = {
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    } | {
        node.func.attr
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
    }
    prohibited = calls & {
        "factor",
        "factorint",
        "is_prime",
        "isprime",
        "prime_factors",
        "prime_range",
    }
    require(not prohibited, "decisive verifier calls factorization or primality machinery")

    projected_product_bytes = unsigned_bytes(projected_product)
    projected_root_bytes = unsigned_bytes(projected_root)
    raw_kernel_dimension = exact_units + exact_duplicates
    require(
        raw_kernel_dimension == retained - len(exact_first_coordinate),
        "raw-to-exact projection dimension is wrong",
    )
    return {
        "status": "PASS",
        "verdict": "PASS_WITH_CLAIM_BOUNDARIES",
        "role": "independent factor-free verification of an advised F116 fixed-input support",
        "input_hashes": {
            "RECONSTRUCT_INPUT.json": sha256_file(input_path),
            "RECONSTRUCT_STATEMENT.md": sha256_file(statement_path),
            "stress_sparse_dag_first_case.py": sha256_file(candidate_source_path),
            "SPARSE_DAG_OUTPUT.json": sha256_file(candidate_output_path),
            "SPARSE_DAG_RUN.log": sha256_file(candidate_log_path),
        },
        "input_policy": {
            "decisive_fields": [
                "N",
                "n",
                "bound",
                "source_stop_relation_count",
                "dependency_relation_indices_zero_based",
            ],
            "factorization_calls": False,
            "primality_calls": False,
            "known_factors_read_before_terminal_gcds": False,
            "candidate_discovery_imported_or_executed": False,
            "known_factors_used_only_for_post_extraction_comparison": True,
            "support_is_external_advice": True,
            "stop_is_external_advice": True,
        },
        "N": modulus,
        "n": n,
        "bound": bound,
        "trial_screen": {
            "count": sum(trial_distribution.values()),
            "gcd_distribution": dict(sorted(trial_distribution.items())),
        },
        "public_seed_basis": {
            "endpoint_count": len(seed_endpoints),
            "block_count": len(basis),
            "blocks": [block for block, _ in basis],
            "stats": basis_stats,
            "pair_count": len(frozen_pairs),
            "pairs": [list(pair) for pair in frozen_pairs],
        },
        "source_at_stop": {
            "retained_relations": retained,
            "attempted_residues": attempted,
            "duplicate_residues": duplicates,
            "residue_gcd_distribution": dict(sorted(residue_gcd_distribution.items())),
            "endpoint_gcd_distribution": dict(sorted(endpoint_gcd_distribution.items())),
            "proper_direct_gcd_count": len(proper_direct),
            "frozen_retained_relations": frozen_retained,
            "frozen_attempted_residues": frozen_attempted,
            "frozen_duplicate_residues": frozen_duplicates,
            "menu_attempted_pairs": menu_attempted,
            "stop_pair": list(stop_pair or ()),
            "retained_record_stream_sha256": source_digest.hexdigest(),
            "record_digest_encoding": "11 length-prefixed unsigned integers per retained record",
        },
        "exact_value_dedup": {
            "candidate_sparse_decoder_performs_this_dedup": False,
            "raw_columns": retained,
            "unit_columns_removed": exact_units,
            "duplicate_exact_value_columns_removed": exact_duplicates,
            "unique_nonunit_columns": len(exact_first_coordinate),
            "raw_to_exact_projection_kernel_dimension": raw_kernel_dimension,
            "projection_kernel_generators": {
                "unit_generators": exact_units,
                "same_value_pair_generators": exact_duplicates,
                "all_generator_roots_mod_N": 1,
                "all_kernel_directions_globally_trivial": True,
            },
            "first_occurrence_coordinates_are_append_monotone": True,
        },
        "raw_advised_support_replay": {
            "support_size": len(advised_support),
            "first_index_zero_based": advised_support[0],
            "last_index_zero_based": advised_support[-1],
            "source_indices_sha256": hashlib.sha256(
                json.dumps(advised_support, separators=(",", ":")).encode()
            ).hexdigest(),
            "support_record_stream_sha256": support_record_digest.hexdigest(),
            "provenance_kind_counts": dict(sorted(support_kind_counts.items())),
            "distinct_appended_pairs": len(support_appended_pairs),
            "selected_unit_columns": selected_units,
            "exact_product_bit_length": raw_support_product.bit_length(),
            "exact_product_unsigned_big_endian_sha256": hashlib.sha256(raw_product_bytes).hexdigest(),
            "positive_root_bit_length": raw_root.bit_length(),
            "positive_root_unsigned_big_endian_sha256": hashlib.sha256(raw_root_bytes).hexdigest(),
            "root_mod_N": raw_root_modulus,
            "root_class": "non_global",
        },
        "projected_unique_exact_value_support": {
            "support_size": len(projected_columns),
            "raw_support_values_are_distinct_nonunits": True,
            "projection_is_one_to_one_by_exact_value": True,
            "each_value_first_occurs_at_its_selected_raw_record": (
                coordinate_identity_count == len(projected_columns)
            ),
            "dedup_column_numbers_equal_selected_raw_indices": (
                projected_columns == projected_selected_source_indices
            ),
            "selected_values_first_occurring_at_same_raw_index": coordinate_identity_count,
            "selected_values_first_occurring_outside_raw_support": (
                len(projected_columns) - coordinate_identity_count
            ),
            "dedup_columns_zero_based": projected_columns,
            "dedup_columns_sha256": hashlib.sha256(
                json.dumps(projected_columns, separators=(",", ":")).encode()
            ).hexdigest(),
            "first_occurrence_raw_source_indices_sha256": hashlib.sha256(
                json.dumps(projected_first_source_indices, separators=(",", ":")).encode()
            ).hexdigest(),
            "exact_product_bit_length": projected_product.bit_length(),
            "exact_product_unsigned_big_endian_sha256": hashlib.sha256(
                projected_product_bytes
            ).hexdigest(),
            "positive_root_bit_length": projected_root.bit_length(),
            "positive_root_unsigned_big_endian_sha256": hashlib.sha256(
                projected_root_bytes
            ).hexdigest(),
            "root_mod_N": projected_root_modulus,
            "root_class": "non_global",
            "same_root_class_as_raw_support": True,
        },
        "terminal_extraction": {
            "root_mod_N": raw_root_modulus,
            "root_squared_mod_N": pow(raw_root_modulus, 2, modulus),
            "gcd_root_minus_one_N": minus,
            "gcd_root_plus_one_N": plus,
            "gcd_product": minus * plus,
            "known_factor_comparison_after_extraction": discovered_factors,
        },
        "sparse_dag_mechanics": mechanics,
        "candidate_discovery_accounting": {
            "factor_assisted_and_not_decisive": True,
            "pivot_count": int(decoder["pivot_count"]),
            "dependencies": int(decoder["dependencies"]),
            "global_dependencies": int(decoder["global_dependencies"]),
            "eliminations": int(decoder["eliminations"]),
            "dag_node_count": int(decoder["dag_node_count"]),
            "maximum_reduced_parity_support": int(decoder["maximum_reduced_parity_support"]),
            "rank_plus_dependency_events_equals_raw_columns": True,
        },
        "monotone_extension_boundary": {
            "raw_residue_stream_dependency_existence_append_monotone": True,
            "exact_value_projected_dependency_existence_append_monotone": True,
            "advised_replay_needs_stop_and_support": True,
            "candidate_sparse_discovery_needs_endpoint_factorization": True,
            "no_stop_no_support_corollary_level": "P66 useful-dependency existence only",
            "full_1378_pair_source_executed": False,
            "full_complete_factor_free_decoder_executed": False,
            "specified_separate_complete_decoder_would_use_stop": False,
            "specified_separate_complete_decoder_would_use_support": False,
            "full_source_order": (
                "seeds; frozen pairs in seed order; all unordered seed pairs lexicographically; "
                "within each pair exponents 0..n^2 and orientations u^e*v then u*v^e"
            ),
            "complete_decoder": (
                "residue first occurrence; exact-value first occurrence; factor-free gcd basis; "
                "complete GF(2) kernel; test every basis root"
            ),
            "success_proved_for_this_N_only": True,
            "all_input_success_theorem": False,
        },
        "complexity_boundary": {
            "full_source_positions": "O(n^4)",
            "relation_value_bits": "at most 2n",
            "dependency_product_bits": "O(n^5) for O(n^4) columns",
            "separate_complete_factor_free_decoder_polynomial_bit_time_and_space": True,
            "candidate_endpoint_factorization_polynomial_time_claim": False,
            "candidate_dag_replaces_dense_combination_masks": True,
            "candidate_total_memory_is_constant_or_linear": False,
            "candidate_fixed_signed_64_bit_DAG_references_are_all_input_unbounded": False,
        },
        "timings_seconds": {
            "source_generation_and_dedup": source_seconds,
            "support_exact_arithmetic": support_seconds,
            "sparse_dag_mechanics": mechanics_seconds,
            "total": time.monotonic() - started,
        },
        "static_source_audit": {
            "prohibited_factorization_or_primality_calls_found": sorted(prohibited),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--statement", type=Path, required=True)
    parser.add_argument("--candidate-source", type=Path, required=True)
    parser.add_argument("--candidate-output", type=Path, required=True)
    parser.add_argument("--candidate-log", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        output = audit(
            args.input.resolve(),
            args.statement.resolve(),
            args.candidate_source.resolve(),
            args.candidate_output.resolve(),
            args.candidate_log.resolve(),
        )
        exit_code = 0
    except Exception as error:
        output = {
            "status": "FAIL",
            "verdict": "FAIL",
            "error_type": type(error).__name__,
            "error": str(error),
            "traceback": traceback.format_exc(),
        }
        exit_code = 1
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "status": output["status"],
                "verdict": output["verdict"],
                "error": output.get("error"),
            },
            sort_keys=True,
        )
    )
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
