#!/usr/bin/env python3
"""Factor-free complete-kernel analysis of the F111 layer interaction."""

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


EXPECTED_CERTIFICATE_SHA256 = "735a8535eb8cd4e8bc5e1c0fbc71d78b3acd79b3e6efa1f865d9084dea67cf6b"
EXPECTED_PUBLIC_BASIS_SHA256 = "5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b"


class VerificationFailure(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationFailure(message)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def feed_digest(digest: object, value: object) -> None:
    digest.update(json.dumps(value, sort_keys=True, separators=(",", ":")).encode())
    digest.update(b"\n")


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
        require(primitive_power(block)[1] == 1, "initial basis retains a perfect power")
        require(
            all(math.gcd(block, old_block) == 1 for old_block, _ in basis[:position]),
            "initial basis is not pairwise coprime",
        )
        for endpoint, exponent in signature.items():
            reconstructed[endpoint] *= block**exponent
    require(reconstructed == endpoints, "initial basis does not reconstruct endpoints")
    return basis, stats


def regenerate_source(certificate: dict[str, object]) -> dict[str, object]:
    modulus = int(certificate["N"])
    n = int(certificate["n"])
    bound = int(certificate["bound"])
    stop = int(certificate["source_stop_relation_count"])
    require(n == modulus.bit_length(), "certificate n is wrong")
    require(bound == n * n, "certificate bound is wrong")

    trial_distribution: Counter[int] = Counter(
        math.gcd(trial, modulus) for trial in range(2, bound + 1)
    )
    require(trial_distribution == Counter({1: bound - 1}), "trial screen is not null")

    records: list[dict[str, object]] = []
    endpoints: list[int] = []
    seen_residues: set[int] = set()
    attempted = 0
    duplicate_residues = 0
    direct_distribution: Counter[int] = Counter()
    record_digest = hashlib.sha256()

    def retain(residue: int, provenance: dict[str, object]) -> None:
        nonlocal attempted, duplicate_residues
        attempted += 1
        if residue in seen_residues:
            duplicate_residues += 1
            return
        require(0 < residue < modulus, "noncanonical retained residue")
        seen_residues.add(residue)
        inverse = pow(residue, -1, modulus)
        require(0 < inverse < modulus, "noncanonical modular inverse")
        for difference in (residue - inverse, residue + inverse):
            divisor = math.gcd(difference, modulus)
            direct_distribution[divisor] += 1
            require(divisor in (1, modulus), "proper direct gcd appears before public stop")
        record = {
            "source_index_zero_based": len(records),
            "c": residue,
            "w": inverse,
            "P": residue * inverse,
            "provenance": provenance,
        }
        require(record["P"] % modulus == 1, "relation is not one modulo N")
        records.append(record)
        endpoints.extend((residue, inverse))
        feed_digest(record_digest, record)

    for seed in range(2, n + 1):
        retain(seed, {"kind": "initial_seed", "seed": seed})

    basis, basis_stats = initial_gcd_basis(endpoints)
    incidence: list[list[int]] = [[] for _ in endpoints]
    for block_index, (_, signature) in enumerate(basis):
        for endpoint_index in signature:
            incidence[endpoint_index].append(block_index)
    frozen_pairs: list[tuple[int, int]] = []
    for relation_index in range(len(records)):
        support = sorted(
            basis[block_index][0]
            for block_index in set(
                incidence[2 * relation_index] + incidence[2 * relation_index + 1]
            )
        )
        require(bool(support), "initial relation has no public support")
        frozen_pairs.append(
            (support[0], 1) if len(support) == 1 else (support[0], support[1])
        )

    for pair_index, (left, right) in enumerate(frozen_pairs):
        for exponent in range(bound + 1):
            for orientation, residue in (
                ("u_power_times_v", pow(left, exponent, modulus) * right % modulus),
                ("u_times_v_power", left * pow(right, exponent, modulus) % modulus),
            ):
                retain(
                    residue,
                    {
                        "kind": "frozen_seed_basis_pair",
                        "pair_index_zero_based": pair_index,
                        "u": left,
                        "v": right,
                        "exponent": exponent,
                        "orientation": orientation,
                    },
                )
    frozen_stop = len(records)

    appended_stats = []
    for pair_index, (left, right) in enumerate(((2, 3), (2, 4))):
        attempts_before = attempted
        records_before = len(records)
        reached_stop = False
        for exponent in range(bound + 1):
            for orientation, residue in (
                ("u_power_times_v", pow(left, exponent, modulus) * right % modulus),
                ("u_times_v_power", left * pow(right, exponent, modulus) % modulus),
            ):
                retain(
                    residue,
                    {
                        "kind": "nonadaptive_seed_pair",
                        "pair_index_zero_based": pair_index,
                        "u": left,
                        "v": right,
                        "exponent": exponent,
                        "orientation": orientation,
                    },
                )
                if len(records) == stop:
                    reached_stop = True
                    break
            if reached_stop:
                break
        appended_stats.append(
            {
                "pair": [left, right],
                "attempts": attempted - attempts_before,
                "new_retained_records": len(records) - records_before,
                "reached_stop": reached_stop,
            }
        )
        if reached_stop:
            break
    require(len(records) == stop, "source does not reach exact public stop")
    require(attempted - duplicate_residues == len(records), "residue dedup accounting fails")
    return {
        "N": modulus,
        "n": n,
        "bound": bound,
        "records": records,
        "frozen_stop": frozen_stop,
        "initial_basis_blocks": [block for block, _ in basis],
        "initial_basis_stats": basis_stats,
        "frozen_pairs": [list(pair) for pair in frozen_pairs],
        "appended_stats": appended_stats,
        "attempted_residues": attempted,
        "duplicate_residues": duplicate_residues,
        "direct_screen_count": sum(direct_distribution.values()),
        "direct_screen_distribution": dict(sorted(direct_distribution.items())),
        "retained_record_stream_sha256": record_digest.hexdigest(),
    }


def exact_value_dedup(records: list[dict[str, object]]) -> dict[str, object]:
    seen_values: set[int] = set()
    unique = []
    units = 0
    duplicates = 0
    for record in records:
        value = int(record["P"])
        if value == 1:
            units += 1
            continue
        if value in seen_values:
            duplicates += 1
            continue
        seen_values.add(value)
        unique.append(record)
    return {
        "records": unique,
        "raw_records": len(records),
        "unit_values_skipped": units,
        "duplicate_exact_values_skipped": duplicates,
        "unique_nonunit_exact_values": len(unique),
    }


def factor_free_union_rows(
    records: list[dict[str, object]],
) -> tuple[list[int], dict[str, int]]:
    pending = []
    for column, record in enumerate(records):
        mask = 1 << column
        pending.append((int(record["c"]), mask))
        pending.append((int(record["w"]), mask))
    stable: list[tuple[int, int]] = []
    refinements = 0
    gcd_tests = 0
    while pending:
        value, mask = pending.pop()
        if value <= 1 or mask == 0:
            continue
        for position, (old_value, old_mask) in enumerate(stable):
            gcd_tests += 1
            divisor = math.gcd(value, old_value)
            if divisor == 1:
                continue
            stable.pop(position)
            refinements += 1
            pending.extend(
                (
                    (divisor, mask ^ old_mask),
                    (value // divisor, mask),
                    (old_value // divisor, old_mask),
                )
            )
            break
        else:
            stable.append((value, mask))

    stable.sort()
    for position, (value, mask) in enumerate(stable):
        require(mask != 0, "stable parity fragment has zero mask")
        require(
            all(math.gcd(value, old_value) == 1 for old_value, _ in stable[:position]),
            "stable parity fragments are not pairwise coprime",
        )
    square_fragments = 0
    row_masks = []
    for value, mask in stable:
        root = math.isqrt(value)
        if root * root == value:
            square_fragments += 1
        else:
            row_masks.append(mask)
    unique_rows = sorted(set(row_masks))
    return unique_rows, {
        "endpoint_entries": 2 * len(records),
        "gcd_tests": gcd_tests,
        "refinements": refinements,
        "stable_coprime_fragments": len(stable),
        "square_fragments_removed": square_fragments,
        "nonsquare_fragment_rows": len(row_masks),
        "duplicate_row_masks_removed": len(row_masks) - len(unique_rows),
        "unique_parity_rows": len(unique_rows),
    }


def kernel_basis(row_masks: list[int], column_count: int) -> tuple[int, list[int]]:
    rows = sorted({row for row in row_masks if row})
    require(all(row.bit_length() <= column_count for row in rows), "row exceeds columns")
    pivots: dict[int, int] = {}
    for original in rows:
        row = original
        while row:
            pivot = (row & -row).bit_length() - 1
            known = pivots.get(pivot)
            if known is None:
                pivots[pivot] = row
                break
            row ^= known

    basis = []
    pivot_columns = set(pivots)
    for free_column in range(column_count):
        if free_column in pivot_columns:
            continue
        vector = 1 << free_column
        for pivot in sorted(pivots, reverse=True):
            if (pivots[pivot] & vector).bit_count() & 1:
                vector ^= 1 << pivot
        require(
            all((row & vector).bit_count() % 2 == 0 for row in rows),
            "constructed vector is not in kernel",
        )
        basis.append(vector)
    require(len(pivots) + len(basis) == column_count, "rank-nullity fails")
    return len(pivots), basis


def root_image_closure(roots: list[int], modulus: int, normalize_sign: bool) -> dict[str, object]:
    normalize = (lambda residue: min(residue, modulus - residue)) if normalize_sign else (lambda residue: residue)
    image = {1}
    generators = []
    for root in roots:
        normalized_root = normalize(root)
        if normalized_root in image:
            continue
        previous = tuple(image)
        image.update(normalize(value * root % modulus) for value in previous)
        generators.append(root)
    require(len(image) & (len(image) - 1) == 0, "root image size is not a power of two")
    rank = len(image).bit_length() - 1
    return {
        "rank": rank,
        "size": len(image),
        "residues": sorted(image),
        "generator_roots": generators,
    }


def summarize_vectors(
    records: list[dict[str, object]], vectors: list[int], modulus: int
) -> dict[str, object]:
    entries = []
    roots = []
    classes: Counter[str] = Counter()
    for basis_index, vector in enumerate(vectors):
        remaining = vector
        product = 1
        support_columns = []
        source_indices = []
        provenance_counts: Counter[str] = Counter()
        while remaining:
            bit = remaining & -remaining
            column = bit.bit_length() - 1
            record = records[column]
            support_columns.append(column)
            source_indices.append(int(record["source_index_zero_based"]))
            provenance_counts[str(record["provenance"]["kind"])] += 1
            product *= int(record["P"])
            remaining ^= bit
        root = math.isqrt(product)
        require(root * root == product, "kernel vector product is not an exact square")
        residue = root % modulus
        require(pow(residue, 2, modulus) == 1, "kernel root does not square to one")
        root_class = "+1" if residue == 1 else "-1" if residue == modulus - 1 else "non_global"
        classes[root_class] += 1
        roots.append(residue)
        product_bytes = product.to_bytes((product.bit_length() + 7) // 8, "big")
        root_bytes = root.to_bytes((root.bit_length() + 7) // 8, "big")
        entries.append(
            {
                "basis_index_zero_based": basis_index,
                "vector_hex": hex(vector),
                "support": len(support_columns),
                "support_columns_sha256": hashlib.sha256(
                    json.dumps(support_columns, separators=(",", ":")).encode()
                ).hexdigest(),
                "source_indices_sha256": hashlib.sha256(
                    json.dumps(source_indices, separators=(",", ":")).encode()
                ).hexdigest(),
                "provenance_kind_counts": dict(sorted(provenance_counts.items())),
                "exact_product_bit_length": product.bit_length(),
                "exact_product_unsigned_big_endian_sha256": hashlib.sha256(
                    product_bytes
                ).hexdigest(),
                "positive_root_bit_length": root.bit_length(),
                "positive_root_unsigned_big_endian_sha256": hashlib.sha256(
                    root_bytes
                ).hexdigest(),
                "root_mod_N": residue,
                "root_class": root_class,
            }
        )
    full_image = root_image_closure(roots, modulus, False)
    normalized_image = root_image_closure(roots, modulus, True)
    return {
        "basis_size": len(vectors),
        "basis": entries,
        "basis_root_class_counts": dict(sorted(classes.items())),
        "full_root_map_image": full_image,
        "normalized_root_map_image_mod_global_sign": normalized_image,
        "contains_non_global_root": normalized_image["rank"] > 0,
        "all_dependencies_global": normalized_image["rank"] == 0,
    }


def analyze_system(
    name: str,
    records: list[dict[str, object]],
    row_masks: list[int],
    modulus: int,
) -> dict[str, object]:
    rank, basis = kernel_basis(row_masks, len(records))
    summary = summarize_vectors(records, basis, modulus)
    require(summary["basis_size"] == len(records) - rank, f"{name} nullity mismatch")
    return {
        "name": name,
        "columns": len(records),
        "parity_rank": rank,
        "nullity": len(basis),
        "kernel": summary,
        "kernel_vectors": basis,
    }


def remap_rows(row_masks: list[int], union_columns: list[int]) -> list[int]:
    remapped = []
    for row in row_masks:
        mapped = 0
        for target, source in enumerate(union_columns):
            if row & (1 << source):
                mapped |= 1 << target
        if mapped:
            remapped.append(mapped)
    return sorted(set(remapped))


def add_to_span(pivots: dict[int, int], vector: int) -> bool:
    reduced = vector
    while reduced:
        pivot = reduced.bit_length() - 1
        known = pivots.get(pivot)
        if known is None:
            pivots[pivot] = reduced
            return True
        reduced ^= known
    return False


def main_audit(certificate_path: Path, public_basis_path: Path) -> dict[str, object]:
    started = time.monotonic()
    require(sha256_file(certificate_path) == EXPECTED_CERTIFICATE_SHA256, "certificate hash changed")
    require(sha256_file(public_basis_path) == EXPECTED_PUBLIC_BASIS_SHA256, "public basis hash changed")
    certificate = json.loads(certificate_path.read_text())
    source = regenerate_source(certificate)
    records = source.pop("records")
    modulus = int(source["N"])
    frozen_stop = int(source["frozen_stop"])
    frozen_raw = records[:frozen_stop]
    appended_raw = records[frozen_stop:]
    trajectory_raw = [
        record
        for record in frozen_raw
        if record["provenance"]["kind"] == "frozen_seed_basis_pair"
    ]

    frozen_dedup = exact_value_dedup(frozen_raw)
    appended_dedup = exact_value_dedup(appended_raw)
    union_dedup = exact_value_dedup(records)
    trajectory_dedup = exact_value_dedup(trajectory_raw)
    frozen_unique = frozen_dedup.pop("records")
    appended_unique = appended_dedup.pop("records")
    union_unique = union_dedup.pop("records")
    trajectory_unique = trajectory_dedup.pop("records")

    require(
        [int(record["P"]) for record in union_unique[: len(frozen_unique)]]
        == [int(record["P"]) for record in frozen_unique],
        "union no longer begins with frozen exact values",
    )
    frozen_values = {int(record["P"]) for record in frozen_unique}
    appended_values = {int(record["P"]) for record in appended_unique}
    overlap_values = frozen_values & appended_values
    union_value_to_column = {
        int(record["P"]): column for column, record in enumerate(union_unique)
    }
    frozen_columns = len(frozen_unique)
    union_appended_records = union_unique[frozen_columns:]
    union_appended_columns = len(union_appended_records)
    require(
        union_appended_columns == len(appended_values - frozen_values),
        "union appended coordinate count is wrong",
    )

    union_rows, refinement_stats = factor_free_union_rows(union_unique)
    frozen_mask = (1 << frozen_columns) - 1
    frozen_rows = sorted({row & frozen_mask for row in union_rows if row & frozen_mask})
    union_appended_rows = sorted(
        {
            row >> frozen_columns
            for row in union_rows
            if row >> frozen_columns
        }
    )
    appended_mapping = [
        union_value_to_column[int(record["P"])] for record in appended_unique
    ]
    trajectory_mapping = [
        union_value_to_column[int(record["P"])] for record in trajectory_unique
    ]
    appended_rows = remap_rows(union_rows, appended_mapping)
    trajectory_rows = remap_rows(union_rows, trajectory_mapping)

    frozen = analyze_system("A_frozen_preappend", frozen_unique, frozen_rows, modulus)
    appended = analyze_system("B_appended_only", appended_unique, appended_rows, modulus)
    union = analyze_system("C_union", union_unique, union_rows, modulus)
    union_appended = analyze_system(
        "union_appended_coordinate_subspace",
        union_appended_records,
        union_appended_rows,
        modulus,
    )
    trajectory = analyze_system(
        "frozen_trajectory_only_without_initial_seeds",
        trajectory_unique,
        trajectory_rows,
        modulus,
    )

    frozen_kernel = frozen.pop("kernel_vectors")
    appended_kernel = appended.pop("kernel_vectors")
    union_kernel = union.pop("kernel_vectors")
    union_appended_kernel = union_appended.pop("kernel_vectors")
    trajectory.pop("kernel_vectors")

    for vector in frozen_kernel:
        require(
            all((row & vector).bit_count() % 2 == 0 for row in union_rows),
            "embedded frozen kernel vector is not in union kernel",
        )
    embedded_appended_kernel = [vector << frozen_columns for vector in union_appended_kernel]
    for vector in embedded_appended_kernel:
        require(
            all((row & vector).bit_count() % 2 == 0 for row in union_rows),
            "embedded appended kernel vector is not in union kernel",
        )

    pure_span: dict[int, int] = {}
    for vector in frozen_kernel + embedded_appended_kernel:
        require(add_to_span(pure_span, vector), "pure layer kernel bases are dependent")
    quotient_representatives = []
    for vector in union_kernel:
        if add_to_span(pure_span, vector):
            require(vector & frozen_mask != 0, "quotient representative lacks frozen support")
            require(vector >> frozen_columns != 0, "quotient representative lacks appended support")
            quotient_representatives.append(vector)

    quotient_dimension = (
        union["nullity"] - frozen["nullity"] - union_appended["nullity"]
    )
    image_intersection_dimension = (
        frozen["parity_rank"]
        + union_appended["parity_rank"]
        - union["parity_rank"]
    )
    require(quotient_dimension == image_intersection_dimension, "projection/kernel dimension identity fails")
    require(len(quotient_representatives) == quotient_dimension, "quotient basis is incomplete")
    quotient_root_map = summarize_vectors(union_unique, quotient_representatives, modulus)

    frozen_useful = bool(frozen["kernel"]["contains_non_global_root"])
    appended_useful = bool(appended["kernel"]["contains_non_global_root"])
    union_appended_useful = bool(
        union_appended["kernel"]["contains_non_global_root"]
    )
    union_useful = bool(union["kernel"]["contains_non_global_root"])
    every_useful_crosses = (
        union_useful
        and not frozen_useful
        and not union_appended_useful
        and quotient_root_map["normalized_root_map_image_mod_global_sign"]["rank"] > 0
    )
    require(not frozen_useful, "frozen layer has a non-global root")
    require(not appended_useful, "appended-only layer has a non-global root")
    require(not union_appended_useful, "union's pure appended subspace has a non-global root")
    require(union_useful, "union lacks a non-global root")
    require(every_useful_crosses, "algebraic criterion does not force useful dependencies to cross")

    verifier_source = Path(__file__).read_text()
    tree = ast.parse(verifier_source)
    called_names = {
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    } | {
        node.func.attr
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
    }
    forbidden_call_names = {
        "factor",
        "factorint",
        "is_prime",
        "isprime",
        "prime_range",
        "prime_factors",
    }
    require(not (called_names & forbidden_call_names), "verifier contains factorization/primality call")
    certificate_subscript_keys = {
        node.slice.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
        and node.value.id == "certificate"
        and isinstance(node.slice, ast.Constant)
        and isinstance(node.slice.value, str)
    }
    require(
        certificate_subscript_keys == {"N", "n", "bound", "source_stop_relation_count"},
        "verifier reads an undeclared certificate field",
    )

    return {
        "status": "PASS",
        "verdict": "PASS",
        "analysis": "factor-free exact-value-deduplicated complete kernel/root-map bases",
        "input_hashes": {
            "CERTIFICATE.json": sha256_file(certificate_path),
            "experiments/F98_multiseed_presentation_closure_kill/public_factorization_free_replay.py": sha256_file(
                public_basis_path
            ),
        },
        "input_policy": {
            "main_replay_uses_known_factors": False,
            "main_replay_calls_factorization": False,
            "main_replay_calls_primality_test": False,
            "selected_363_index_certificate_read": False,
            "diagnostic_factor_assisted_stage_run": False,
            "certificate_fields_used": ["N", "n", "bound", "source_stop_relation_count"],
        },
        "source_regeneration": source,
        "exact_value_dedup": {
            "frozen_preappend": frozen_dedup,
            "appended_only": appended_dedup,
            "union": union_dedup,
            "frozen_trajectory_only": trajectory_dedup,
            "cross_layer_exact_value_overlap": len(overlap_values),
            "union_appended_new_exact_values": union_appended_columns,
            "overlap_value_sha256": hashlib.sha256(
                json.dumps(sorted(overlap_values), separators=(",", ":")).encode()
            ).hexdigest(),
        },
        "factor_free_parity_refinement": refinement_stats,
        "systems": {
            "A_frozen_preappend": frozen,
            "B_appended_only": appended,
            "C_union": union,
            "union_appended_coordinate_subspace": union_appended,
            "frozen_trajectory_only_without_initial_seeds": trajectory,
        },
        "projection_kernel_criterion": {
            "identity": "K_U/(K_F direct_sum K_A) is isomorphic to image(M_F) intersect image(M_A)",
            "pure_kernel_dimension": frozen["nullity"] + union_appended["nullity"],
            "union_kernel_dimension": union["nullity"],
            "cross_layer_quotient_dimension": quotient_dimension,
            "parity_image_intersection_dimension": image_intersection_dimension,
            "quotient_complete_root_map_basis": quotient_root_map,
            "frozen_normalized_root_map_rank": frozen["kernel"][
                "normalized_root_map_image_mod_global_sign"
            ]["rank"],
            "appended_union_coordinate_normalized_root_map_rank": union_appended[
                "kernel"
            ]["normalized_root_map_image_mod_global_sign"]["rank"],
            "union_normalized_root_map_rank": union["kernel"][
                "normalized_root_map_image_mod_global_sign"
            ]["rank"],
            "induced_quotient_normalized_root_map_rank": quotient_root_map[
                "normalized_root_map_image_mod_global_sign"
            ]["rank"],
            "every_useful_union_dependency_crosses_layers": every_useful_crosses,
        },
        "answers": {
            "A_frozen_layer_contains_non_global_square_root": frozen_useful,
            "B_appended_only_contains_non_global_square_root": appended_useful,
            "C_union_contains_non_global_square_root": union_useful,
            "every_useful_exact_deduplicated_union_dependency_crosses_layers": every_useful_crosses,
        },
        "theorem_boundary": {
            "proved": (
                "For this N, exact source order, public stop, and global first-occurrence exact-value dedup, "
                "the frozen and appended pure kernels map only to global roots, while the union kernel has a "
                "nontrivial normalized-root image induced through the cross-layer quotient."
            ),
            "not_proved": [
                "that the supplied 363 indices can be selected without advice",
                "that another source order or stop has the same layer interaction",
                "that another modulus has the same quotient or root map",
                "an all-input, density, probability, or runtime theorem",
            ],
        },
        "elapsed_seconds": time.monotonic() - started,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--public-basis-source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        output = main_audit(args.certificate.resolve(), args.public_basis_source.resolve())
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
