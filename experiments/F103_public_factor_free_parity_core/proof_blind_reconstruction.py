#!/usr/bin/env python3
"""Proof-blind reconstruction of the public F103 fixed-input claims.

The executable receives only N. It uses gcd refinement and binary linear
algebra. It does not call an integer factorization routine, primality test,
or target selector.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from collections import Counter, deque
from pathlib import Path


def exact_nth_root(value: int, exponent: int) -> int | None:
    low = 1
    high = 1 << ((value.bit_length() + exponent - 1) // exponent + 1)
    while low + 1 < high:
        middle = (low + high) // 2
        power = middle**exponent
        if power < value:
            low = middle
        elif power > value:
            high = middle
        else:
            return middle
    return low if low**exponent == value else None


def primitive_root(value: int) -> tuple[int, int]:
    for exponent in range(value.bit_length(), 1, -1):
        root = exact_nth_root(value, exponent)
        if root is not None:
            return root, exponent
    return value, 1


def add_signatures(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    result = dict(left)
    for endpoint, exponent in right.items():
        result[endpoint] = result.get(endpoint, 0) + exponent
    return result


def scale_signature(signature: dict[int, int], scale: int) -> dict[int, int]:
    return signature if scale == 1 else {
        endpoint: scale * exponent for endpoint, exponent in signature.items()
    }


def gcd_free_basis(endpoint_values: list[int]):
    """Reconstruct the public source's initial active-pair presentation."""
    pending = [
        (value, {endpoint: 1})
        for endpoint, value in enumerate(endpoint_values)
        if value > 1
    ]
    basis: list[tuple[int, dict[int, int]]] = []
    stats = Counter()
    while pending:
        value, signature = pending.pop()
        if value == 1:
            continue
        root, power = primitive_root(value)
        if power > 1:
            value = root
            signature = scale_signature(signature, power)
            stats["perfect_power_splits"] += 1
        for position, (old_value, old_signature) in enumerate(basis):
            stats["gcd_calls"] += 1
            common = math.gcd(value, old_value)
            if common == 1:
                continue
            basis.pop(position)
            if value == old_value:
                pending.append((value, add_signatures(signature, old_signature)))
                stats["identical_merges"] += 1
            else:
                pending.extend(
                    (
                        (common, signature),
                        (value // common, signature),
                        (common, old_signature),
                        (old_value // common, old_signature),
                    )
                )
                stats["overlap_splits"] += 1
            break
        else:
            basis.append((value, signature))

    basis.sort(key=lambda item: item[0])
    reconstructed = [1] * len(endpoint_values)
    for block, signature in basis:
        assert primitive_root(block)[1] == 1
        for endpoint, exponent in signature.items():
            reconstructed[endpoint] *= block**exponent
    assert reconstructed == endpoint_values
    return basis, {
        name: stats[name]
        for name in (
            "gcd_calls",
            "overlap_splits",
            "perfect_power_splits",
            "identical_merges",
        )
    }


def relation_columns(basis, relation_count: int):
    endpoint_incidence: list[list[tuple[int, int]]] = [
        [] for _ in range(2 * relation_count)
    ]
    for block_index, (_, signature) in enumerate(basis):
        for endpoint, exponent in signature.items():
            endpoint_incidence[endpoint].append((block_index, exponent))
    columns = []
    for relation_index in range(relation_count):
        column: dict[int, int] = {}
        for endpoint in (2 * relation_index, 2 * relation_index + 1):
            for block_index, exponent in endpoint_incidence[endpoint]:
                column[block_index] = column.get(block_index, 0) + exponent
        columns.append(column)
    return columns


def parity_coprime_basis(initial_entries: list[tuple[int, int]]):
    """Apply the stated P66 refinement without factoring any integer."""
    stable: list[tuple[int, int]] = []
    work = [(value, mask) for value, mask in initial_entries if value > 1 and mask]
    refinements = 0
    gcd_tests = 0
    while work:
        value, mask = work.pop()
        for index, (old_value, old_mask) in enumerate(stable):
            gcd_tests += 1
            common = math.gcd(value, old_value)
            if common == 1:
                continue
            stable.pop(index)
            refinements += 1
            for new_value, new_mask in (
                (common, mask ^ old_mask),
                (value // common, mask),
                (old_value // common, old_mask),
            ):
                if new_value > 1 and new_mask:
                    work.append((new_value, new_mask))
            break
        else:
            stable.append((value, mask))
    accumulated_product = 1
    for value, _ in stable:
        assert math.gcd(value, accumulated_product) == 1
        accumulated_product *= value
    return stable, {
        "refinements": refinements,
        "gcd_tests": gcd_tests,
        "pairwise_coprime_verified": True,
    }


def public_rows(records: list[dict[str, object]]):
    entries: list[tuple[int, int]] = []
    for column, record in enumerate(records):
        mask = 1 << column
        entries.extend(((int(record["c"]), mask), (int(record["w"]), mask)))
    blocks, stats = parity_coprime_basis(entries)
    rows = []
    square_blocks = 0
    for value, mask in blocks:
        root = math.isqrt(value)
        if root * root == value:
            square_blocks += 1
        else:
            rows.append(mask)
    stats.update(
        {
            "coprime_blocks": len(blocks),
            "square_blocks": square_blocks,
            "public_rows": len(rows),
            "distinct_public_rows": len(set(rows)),
        }
    )
    return rows, stats


def row_echelon(row_masks: list[int]):
    pivots: dict[int, int] = {}
    for original in row_masks:
        row = original
        while row:
            pivot = row.bit_length() - 1
            known = pivots.get(pivot)
            if known is None:
                pivots[pivot] = row
                break
            row ^= known
    return pivots


def kernel_basis(row_masks: list[int], column_count: int):
    pivots = row_echelon(row_masks)
    pivot_columns = set(pivots)
    ordered_pivots = sorted(pivots)
    kernel = []
    for free_column in range(column_count):
        if free_column in pivot_columns:
            continue
        vector = 1 << free_column
        for pivot in ordered_pivots:
            if (pivots[pivot] & vector).bit_count() & 1:
                vector ^= 1 << pivot
        assert all((row & vector).bit_count() % 2 == 0 for row in pivots.values())
        kernel.append(vector)
    return len(pivots), kernel


def supports_and_incidence(rows: list[int], column_count: int):
    supports: list[list[int]] = []
    incidence: list[list[int]] = [[] for _ in range(column_count)]
    for row_index, row in enumerate(rows):
        support = []
        remaining = row
        while remaining:
            low_bit = remaining & -remaining
            column = low_bit.bit_length() - 1
            support.append(column)
            incidence[column].append(row_index)
            remaining ^= low_bit
        supports.append(support)
    return supports, incidence


def peel(rows: list[int], column_count: int, schedule: str):
    supports, incidence = supports_and_incidence(rows, column_count)
    degree = [len(support) for support in supports]
    active = [True] * column_count
    order: list[int] = []
    initial_degree_one = sum(value == 1 for value in degree)

    if schedule in ("fifo", "lifo"):
        pending = deque(index for index, value in enumerate(degree) if value == 1)
        while pending:
            row_index = pending.popleft() if schedule == "fifo" else pending.pop()
            if degree[row_index] != 1:
                continue
            column = next(column for column in supports[row_index] if active[column])
            active[column] = False
            order.append(column)
            for affected_row in incidence[column]:
                degree[affected_row] -= 1
                if degree[affected_row] == 1:
                    pending.append(affected_row)
    elif schedule == "batch_descending":
        while True:
            columns = {
                next(column for column in supports[row_index] if active[column])
                for row_index, value in enumerate(degree)
                if value == 1
            }
            if not columns:
                break
            for column in sorted(columns, reverse=True):
                if not active[column]:
                    continue
                active[column] = False
                order.append(column)
                for affected_row in incidence[column]:
                    degree[affected_row] -= 1
    else:
        raise ValueError(schedule)

    final_columns = [column for column, present in enumerate(active) if present]
    assert all(value == 0 or value >= 2 for value in degree)
    return {
        "initial_degree_one_rows": initial_degree_one,
        "peeled_columns": len(order),
        "core_columns": final_columns,
        "deletion_order_sha256": digest_json(order),
    }


def remap_rows(rows: list[int], columns: list[int]):
    positions = {column: position for position, column in enumerate(columns)}
    core_mask = sum(1 << column for column in columns)
    remapped = []
    for row in rows:
        remaining = row & core_mask
        if not remaining:
            continue
        new_row = 0
        while remaining:
            low_bit = remaining & -remaining
            new_row |= 1 << positions[low_bit.bit_length() - 1]
            remaining ^= low_bit
        remapped.append(new_row)
    return remapped


def component_sizes(rows: list[int], column_count: int):
    parent = list(range(column_count))
    size = [1] * column_count

    def find(item: int):
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    for row in rows:
        support = []
        remaining = row
        while remaining:
            low_bit = remaining & -remaining
            support.append(low_bit.bit_length() - 1)
            remaining ^= low_bit
        first = find(support[0])
        for column in support[1:]:
            other = find(column)
            first = find(first)
            if first != other:
                if size[first] < size[other]:
                    first, other = other, first
                parent[other] = first
                size[first] += size[other]
    return sorted(size[index] for index in range(column_count) if find(index) == index)


def digest_json(value: object):
    encoded = json.dumps(value, separators=(",", ":"), sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()


def ordered_column_digest(columns: list[int]):
    """Hash comma-joined zero-based matrix columns with no final newline."""
    return hashlib.sha256(",".join(map(str, columns)).encode()).hexdigest()


def decode_distinct_records(records: list[dict[str, object]]):
    unique: list[tuple[int, dict[str, object]]] = []
    seen_values: set[int] = set()
    value_one = 0
    repeated = 0
    for raw_index, record in enumerate(records):
        value = int(record["P"])
        if value == 1:
            value_one += 1
        elif value in seen_values:
            repeated += 1
        else:
            seen_values.add(value)
            unique.append((raw_index, record))
    return unique, value_one, repeated


def scan_useful_dependency(
    modulus: int,
    core_rows: list[int],
    core_columns: list[int],
    unique_records: list[tuple[int, dict[str, object]]],
):
    rank, basis = kernel_basis(core_rows, len(core_columns))
    global_plus = 0
    global_minus = 0
    for scan_index, vector in enumerate(basis):
        positions = []
        remaining = vector
        product = 1
        while remaining:
            low_bit = remaining & -remaining
            position = low_bit.bit_length() - 1
            positions.append(position)
            product *= int(unique_records[core_columns[position]][1]["P"])
            remaining ^= low_bit
        root = math.isqrt(product)
        assert root * root == product
        residue = root % modulus
        if residue == 1:
            global_plus += 1
            continue
        if residue == modulus - 1:
            global_minus += 1
            continue
        minus = math.gcd(root - 1, modulus)
        plus = math.gcd(root + 1, modulus)
        assert 1 < minus < modulus or 1 < plus < modulus
        selected_columns = [core_columns[position] for position in positions]
        return {
            "scan": "ascending free columns after highest-pivot row elimination",
            "kernel_rank": rank,
            "kernel_dimension": len(basis),
            "basis_vectors_scanned": scan_index + 1,
            "global_plus_before_useful": global_plus,
            "global_minus_before_useful": global_minus,
            "support": len(positions),
            "selected_unique_columns_zero_based": selected_columns,
            "selected_raw_indices_zero_based": [
                unique_records[column][0] for column in selected_columns
            ],
            "selected_columns_sha256": digest_json(selected_columns),
            "exact_product_is_square": True,
            "root_mod_N": residue,
            "gcd_root_minus_one_N": minus,
            "gcd_root_plus_one_N": plus,
        }
    return {
        "scan": "ascending free columns after highest-pivot row elimination",
        "kernel_rank": rank,
        "kernel_dimension": len(basis),
        "basis_vectors_scanned": len(basis),
        "global_plus_before_useful": global_plus,
        "global_minus_before_useful": global_minus,
        "status": "no useful dependency",
    }


def reconstruct_stream(modulus: int):
    n = modulus.bit_length()
    bound = n * n
    trial_gcds = []
    for trial in range(2, bound + 1):
        divisor = math.gcd(trial, modulus)
        trial_gcds.append(divisor)
        assert not 1 < divisor < modulus

    records: list[dict[str, object]] = []
    initial_endpoints: list[int] = []
    seen_candidates: set[int] = set()
    candidate_attempts = 0
    repeated_candidates = 0
    sign_screens = 0

    def retain(candidate: int, provenance: dict[str, object]):
        nonlocal candidate_attempts, repeated_candidates, sign_screens
        candidate_attempts += 1
        if candidate in seen_candidates:
            repeated_candidates += 1
            return
        seen_candidates.add(candidate)
        inverse = pow(candidate, -1, modulus)
        for difference in (candidate - inverse, candidate + inverse):
            divisor = math.gcd(difference, modulus)
            sign_screens += 1
            assert not 1 < divisor < modulus
        records.append(
            {
                "c": candidate,
                "w": inverse,
                "P": candidate * inverse,
                "provenance": provenance,
            }
        )

    for seed in range(2, n + 1):
        retain(seed, {"kind": "initial_seed", "seed": seed})
        initial_endpoints.extend((records[-1]["c"], records[-1]["w"]))

    initial_basis, initial_basis_stats = gcd_free_basis(initial_endpoints)
    initial_columns = relation_columns(initial_basis, len(records))
    initial_rows, initial_p66_stats = public_rows(records)
    initial_rank, initial_kernel = kernel_basis(initial_rows, len(records))
    initial_global_plus = 0
    initial_global_minus = 0
    for vector in initial_kernel:
        product = 1
        remaining = vector
        while remaining:
            low_bit = remaining & -remaining
            product *= int(records[low_bit.bit_length() - 1]["P"])
            remaining ^= low_bit
        root = math.isqrt(product)
        assert root * root == product
        residue = root % modulus
        if residue == 1:
            initial_global_plus += 1
        elif residue == modulus - 1:
            initial_global_minus += 1
        else:
            raise AssertionError("The public source would stop before feedback generation.")

    active = []
    for relation_index, column in enumerate(initial_columns):
        if not any(exponent & 1 for exponent in column.values()):
            continue
        support = sorted(initial_basis[index][0] for index in column)
        pair = (support[0], 1) if len(support) == 1 else tuple(support[:2])
        active.append((relation_index, pair))
        if len(active) == n:
            break

    for relation_index, (u, v) in active:
        for exponent in range(bound + 1):
            for orientation, candidate in (
                ("u_power_times_v", pow(u, exponent, modulus) * v % modulus),
                ("u_times_v_power", u * pow(v, exponent, modulus) % modulus),
            ):
                retain(
                    candidate,
                    {
                        "kind": "feedback_trajectory",
                        "round": 1,
                        "active_relation_index_zero_based": relation_index,
                        "u": u,
                        "v": v,
                        "exponent": exponent,
                        "orientation": orientation,
                    },
                )

    stream_digest = digest_json(records)
    return records, {
        "N": modulus,
        "bit_length": n,
        "bound": bound,
        "trial_screen": {
            "checks": len(trial_gcds),
            "all_failed": True,
            "result_gcd_counts": dict(sorted(Counter(trial_gcds).items())),
        },
        "direct_sign_screen": {
            "checks": sign_screens,
            "all_failed": True,
        },
        "candidate_attempts": candidate_attempts,
        "repeated_candidates": repeated_candidates,
        "retained_raw_relations": len(records),
        "initial_seed_count": n - 1,
        "initial_basis_size": len(initial_basis),
        "initial_basis_stats": initial_basis_stats,
        "initial_public_decoder": {
            **initial_p66_stats,
            "rank": initial_rank,
            "nullity": len(initial_kernel),
            "global_plus_basis_roots": initial_global_plus,
            "global_minus_basis_roots": initial_global_minus,
            "useful_dependency": False,
        },
        "active_pairs": [list(pair) for _, pair in active],
        "stream_sha256": stream_digest,
    }


def analyze_batch(
    records_with_raw_indices: list[tuple[int, dict[str, object]]],
    label: str,
):
    records = [record for _, record in records_with_raw_indices]
    rows, p66_stats = public_rows(records)
    column_count = len(records)
    rank = len(row_echelon(rows))
    fifo = peel(rows, column_count, "fifo")
    lifo = peel(rows, column_count, "lifo")
    batch = peel(rows, column_count, "batch_descending")
    core_columns = fifo["core_columns"]
    assert core_columns == lifo["core_columns"] == batch["core_columns"]
    assert len({fifo["deletion_order_sha256"], lifo["deletion_order_sha256"], batch["deletion_order_sha256"]}) == 3
    core_rows = remap_rows(rows, core_columns)
    core_rank = len(row_echelon(core_rows))
    return {
        "label": label,
        "distinct_values": column_count,
        **p66_stats,
        "rank": rank,
        "nullity": column_count - rank,
        "initial_degree_one_rows": fifo["initial_degree_one_rows"],
        "peeled_columns": fifo["peeled_columns"],
        "core_columns": len(core_columns),
        "core_rows": len(core_rows),
        "core_rank": core_rank,
        "core_nullity": len(core_columns) - core_rank,
        "core_components": component_sizes(core_rows, len(core_columns)),
        "ordered_core_sha256": ordered_column_digest(core_columns),
        "ordered_core_hash_encoding": (
            "ASCII decimal zero-based distinct-value column indices, joined by commas, "
            "with no trailing newline"
        ),
        "peeling_schedules": {
            "fifo": {
                "peeled_columns": fifo["peeled_columns"],
                "deletion_order_sha256": fifo["deletion_order_sha256"],
            },
            "lifo": {
                "peeled_columns": lifo["peeled_columns"],
                "deletion_order_sha256": lifo["deletion_order_sha256"],
            },
            "batch_descending": {
                "peeled_columns": batch["peeled_columns"],
                "deletion_order_sha256": batch["deletion_order_sha256"],
            },
        },
        "_rows": rows,
        "_core_rows": core_rows,
        "_core_column_indices": core_columns,
    }


def provenance_summary(
    core_columns: list[int], unique_records: list[tuple[int, dict[str, object]]]
):
    selected = [unique_records[column][1] for column in core_columns]
    seeds = [
        int(record["c"])
        for record in selected
        if record["provenance"]["kind"] == "initial_seed"
    ]
    feedback = [
        record for record in selected if record["provenance"]["kind"] == "feedback_trajectory"
    ]
    orientations = Counter(record["provenance"]["orientation"] for record in feedback)
    families = Counter(
        (
            record["provenance"]["active_relation_index_zero_based"],
            record["provenance"]["u"],
            record["provenance"]["v"],
        )
        for record in feedback
    )
    return {
        "seed_count": len(seeds),
        "seed_values": seeds,
        "feedback_count": len(feedback),
        "orientation_counts": dict(sorted(orientations.items())),
        "active_pair_family_count": len(families),
        "active_pair_families": [
            {
                "active_relation_index_zero_based": family[0],
                "u": family[1],
                "v": family[2],
                "core_records": count,
            }
            for family, count in sorted(families.items())
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--modulus", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()

    print("stage=stream", flush=True)
    raw_records, replay = reconstruct_stream(args.modulus)
    unique_records, value_one, repeated_values = decode_distinct_records(raw_records)

    print("stage=full_p66", flush=True)
    full = analyze_batch(unique_records, "full")
    full_rows = full.pop("_rows")
    full_core_rows = full.pop("_core_rows")
    full_core_columns = full.pop("_core_column_indices")
    full["provenance"] = provenance_summary(full_core_columns, unique_records)

    print("stage=prefix_p66", flush=True)
    prefix_records = [item for item in unique_records if item[0] < 5_616]
    prefix = analyze_batch(prefix_records, "first occurrence raw index < 5616")
    prefix_rows = prefix.pop("_rows")
    prefix.pop("_core_rows")
    prefix.pop("_core_column_indices")
    prefix_mask = (1 << len(prefix_records)) - 1
    restricted_full_row_set = {row & prefix_mask for row in full_rows if row & prefix_mask}
    prefix["distinct_row_set_equals_full_restriction"] = (
        set(prefix_rows) == restricted_full_row_set
    )
    assert prefix["distinct_row_set_equals_full_restriction"]

    print("stage=kernel_scan", flush=True)
    certificate = scan_useful_dependency(
        args.modulus,
        full_core_rows,
        full_core_columns,
        unique_records,
    )

    full_expected = {
        "distinct_values": 9_414,
        "public_rows": 11_015,
        "rank": 8_926,
        "nullity": 488,
        "initial_degree_one_rows": 7_866,
        "peeled_columns": 7_633,
        "core_columns": 1_781,
        "core_rows": 1_298,
        "core_rank": 1_293,
        "core_nullity": 488,
        "core_components": [1_781],
        "ordered_core_sha256": "5e18521931048141bdc4c09f23af1b8b9e7d0b5b95bb70b42b420443c6f2cbc8",
    }
    prefix_expected = {
        "distinct_values": 4_293,
        "public_rows": 5_607,
        "rank": 4_291,
        "nullity": 2,
        "initial_degree_one_rows": 4_012,
        "peeled_columns": 3_920,
        "core_columns": 373,
        "core_rows": 387,
        "core_rank": 371,
        "core_nullity": 2,
        "core_components": [373],
        "ordered_core_sha256": "9b75bad6177686931cc714931b37bdf4e42823db4d0121b7e8859dff3c1260df",
    }
    claim_checks = {
        "trial_and_direct_sign_screens_all_fail": (
            replay["trial_screen"]["all_failed"]
            and replay["direct_sign_screen"]["all_failed"]
        ),
        "retained_raw_relations": len(raw_records) == 12_549,
        "distinct_nontrivial_values": len(unique_records) == 9_414,
        "full_metrics_and_hash": all(full[name] == expected for name, expected in full_expected.items()),
        "three_materially_different_full_peels_same_core": (
            len(
                {
                    schedule["deletion_order_sha256"]
                    for schedule in full["peeling_schedules"].values()
                }
            )
            == 3
        ),
        "full_core_provenance": full["provenance"]["seed_count"] == 3
        and full["provenance"]["seed_values"] == [2, 11, 27]
        and full["provenance"]["feedback_count"] == 1_778
        and full["provenance"]["active_pair_family_count"] == 8
        and full["provenance"]["orientation_counts"]
        == {"u_power_times_v": 1_138, "u_times_v_power": 640},
        "prefix_metrics_and_hash": all(
            prefix[name] == expected for name, expected in prefix_expected.items()
        ),
        "three_materially_different_prefix_peels_same_core": (
            len(
                {
                    schedule["deletion_order_sha256"]
                    for schedule in prefix["peeling_schedules"].values()
                }
            )
            == 3
        ),
        "prefix_public_row_set_is_full_row_set_restriction": prefix[
            "distinct_row_set_equals_full_restriction"
        ],
        "untargeted_core_scan_finds_support_166_exact_square": (
            certificate.get("support") == 166
            and certificate.get("exact_product_is_square") is True
        ),
    }

    result = {
        "experiment": "F103 proof-blind reconstruction",
        "input_policy": "executable receives only N",
        "forbidden_operations_used": [],
        "replay": replay,
        "deduplication": {
            "retained_raw_relations": len(raw_records),
            "value_one_relations_removed": value_one,
            "repeated_exact_values_removed": repeated_values,
            "distinct_nontrivial_values": len(unique_records),
        },
        "full": full,
        "prefix": prefix,
        "useful_certificate": certificate,
        "claim_checks": claim_checks,
        "status": "PASS" if all(claim_checks.values()) else "FAIL",
        "elapsed_seconds": time.monotonic() - started,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"status={result['status']} elapsed_seconds={result['elapsed_seconds']:.6f}", flush=True)
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
