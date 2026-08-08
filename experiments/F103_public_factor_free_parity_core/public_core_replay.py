#!/usr/bin/env python3
"""N-only replay of F98 with lossless peeling of the public P66 matrix."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import time
from collections import Counter, deque
from pathlib import Path


BASE = Path(__file__).resolve().parent
F98_SOURCE = (
    BASE.parent
    / "F98_multiseed_presentation_closure_kill"
    / "public_factorization_free_replay.py"
)
SPEC = importlib.util.spec_from_file_location("pinned_f98_public", F98_SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load pinned F98 public source")
F98 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(F98)


def matrix_for(unique_records: list[tuple[int, dict[str, object]]]):
    initial_entries = []
    relation_values = []
    for column, (_, record) in enumerate(unique_records):
        mask = 1 << column
        c = int(record["c"])
        w = int(record["w"])
        value = int(record["P"])
        if c * w != value:
            raise AssertionError("invalid exact relation")
        initial_entries.extend(((c, mask), (w, mask)))
        relation_values.append(value)

    blocks, refinements, gcd_tests = F98.parity_coprime_basis(initial_entries)
    row_masks = []
    square_blocks = 0
    for value, mask in blocks:
        root = math.isqrt(value)
        if root * root == value:
            square_blocks += 1
        else:
            row_masks.append(mask)
    rank, kernel = F98.binary_kernel_basis(row_masks, len(unique_records))
    return {
        "row_masks": row_masks,
        "relation_values": relation_values,
        "rank": rank,
        "kernel": kernel,
        "coprime_blocks": len(blocks),
        "square_blocks": square_blocks,
        "refinements": refinements,
        "gcd_tests": gcd_tests,
    }


def row_rank(row_masks: list[int]) -> int:
    pivots: dict[int, int] = {}
    for original in row_masks:
        value = original
        while value:
            pivot = value.bit_length() - 1
            prior = pivots.get(pivot)
            if prior is None:
                pivots[pivot] = value
                break
            value ^= prior
    return len(pivots)


def peel(row_masks: list[int], column_count: int, reverse: bool = False):
    active = (1 << column_count) - 1
    degrees = [mask.bit_count() for mask in row_masks]
    column_rows = [[] for _ in range(column_count)]
    for row, mask in enumerate(row_masks):
        value = mask
        while value:
            bit = value & -value
            column_rows[bit.bit_length() - 1].append(row)
            value ^= bit

    singles = [row for row, degree in enumerate(degrees) if degree == 1]
    queue = deque(sorted(singles, reverse=reverse))
    removed = []
    while queue:
        row = queue.pop() if reverse else queue.popleft()
        if degrees[row] != 1:
            continue
        lone = row_masks[row] & active
        if lone.bit_count() != 1:
            raise AssertionError("degree-one row does not have one active column")
        column = lone.bit_length() - 1
        active ^= lone
        removed.append(column)
        for incident_row in column_rows[column]:
            degrees[incident_row] -= 1
            if degrees[incident_row] == 1:
                queue.append(incident_row)

    columns = []
    value = active
    while value:
        bit = value & -value
        columns.append(bit.bit_length() - 1)
        value ^= bit
    restricted_rows = [mask & active for mask in row_masks if mask & active]
    return columns, restricted_rows, removed, degrees


def component_sizes(row_masks: list[int], columns: list[int]) -> list[int]:
    active = set(columns)
    column_rows = {column: [] for column in columns}
    active_mask = sum(1 << column for column in columns)
    supports = []
    for row, mask in enumerate(row_masks):
        support = mask & active_mask
        if not support:
            continue
        supports.append(support)
        value = support
        while value:
            bit = value & -value
            column_rows[bit.bit_length() - 1].append(len(supports) - 1)
            value ^= bit

    unseen = set(active)
    sizes = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        queue = deque([start])
        seen_rows = set()
        size = 0
        while queue:
            column = queue.popleft()
            size += 1
            for row in column_rows[column]:
                if row in seen_rows:
                    continue
                seen_rows.add(row)
                value = supports[row]
                while value:
                    bit = value & -value
                    neighbor = bit.bit_length() - 1
                    if neighbor in unseen:
                        unseen.remove(neighbor)
                        queue.append(neighbor)
                    value ^= bit
        sizes.append(size)
    return sorted(sizes, reverse=True)


def summarize(matrix: dict[str, object], column_count: int):
    rows = list(matrix["row_masks"])
    core, core_rows, removed, _ = peel(rows, column_count)
    reverse_core, _, _, _ = peel(rows, column_count, reverse=True)
    if core != reverse_core:
        raise AssertionError("peeling order changed the core")
    full_rank = int(matrix["rank"])
    core_rank = row_rank(core_rows)
    return {
        "columns": column_count,
        "rows": len(rows),
        "rank": full_rank,
        "nullity": column_count - full_rank,
        "initial_degree_one_rows": sum(mask.bit_count() == 1 for mask in rows),
        "peeled_columns": len(removed),
        "core_columns": len(core),
        "core_rows": len(core_rows),
        "core_rank": core_rank,
        "core_nullity": len(core) - core_rank,
        "kernel_preserved": column_count - full_rank == len(core) - core_rank,
        "core_order_independent_two_orders": True,
        "core_component_sizes": component_sizes(rows, core),
        "core_columns_zero_based": core,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--modulus", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    modulus = args.modulus
    n = modulus.bit_length()
    bound = n * n

    for trial in range(2, bound + 1):
        divisor = math.gcd(trial, modulus)
        if 1 < divisor < modulus:
            args.output.write_text(json.dumps({"status": "trial_factor", "factor": divisor}) + "\n")
            return 0

    records: list[dict[str, object]] = []
    endpoints: list[int] = []
    seen_residues: set[int] = set()

    def retain(c: int, provenance: dict[str, object]):
        if c in seen_residues:
            return None
        seen_residues.add(c)
        w = pow(c, -1, modulus)
        for sign, difference in (("minus", c - w), ("plus", c + w)):
            divisor = math.gcd(difference, modulus)
            if 1 < divisor < modulus:
                return {"status": "direct_factor", "factor": divisor, "sign": sign}
        records.append({"c": c, "w": w, "P": c * w, "provenance": provenance})
        endpoints.extend((c, w))
        return None

    for seed in range(2, n + 1):
        direct = retain(seed, {"kind": "initial_seed", "seed": seed})
        if direct is not None:
            args.output.write_text(json.dumps(direct) + "\n")
            return 0

    initial_basis, _ = F98.gcd_free_basis(endpoints)
    initial_columns = F98.relation_columns(initial_basis, len(records))
    initial_decoder = F98.decode_relations(modulus, records)
    if initial_decoder["status"] != "null":
        raise AssertionError("initial decoder unexpectedly factored the fixed input")
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
            for orientation, c in (
                ("u_power_times_v", pow(u, exponent, modulus) * v % modulus),
                ("u_times_v_power", u * pow(v, exponent, modulus) % modulus),
            ):
                direct = retain(
                    c,
                    {
                        "kind": "feedback_trajectory",
                        "active_relation_index_zero_based": relation_index,
                        "u": u,
                        "v": v,
                        "exponent": exponent,
                        "orientation": orientation,
                    },
                )
                if direct is not None:
                    args.output.write_text(json.dumps(direct) + "\n")
                    return 0

    unique_records = []
    seen_values = set()
    for raw_index, record in enumerate(records):
        value = int(record["P"])
        if value == 1 or value in seen_values:
            continue
        seen_values.add(value)
        unique_records.append((raw_index, record))

    full_matrix = matrix_for(unique_records)
    full = summarize(full_matrix, len(unique_records))
    if not full["kernel_preserved"]:
        raise AssertionError("full peeling changed nullity")

    useful = None
    for vector in full_matrix["kernel"]:
        selected = []
        product = 1
        remaining = vector
        while remaining:
            bit = remaining & -remaining
            column = bit.bit_length() - 1
            selected.append(column)
            product *= full_matrix["relation_values"][column]
            remaining ^= bit
        root = math.isqrt(product)
        if root * root != product:
            raise AssertionError("kernel vector is not an exact square")
        residue = root % modulus
        if residue in (1, modulus - 1):
            continue
        useful = {
            "support": len(selected),
            "selected_columns_zero_based": selected,
            "root_mod_N": residue,
            "gcd_root_minus_one_N": math.gcd(root - 1, modulus),
            "gcd_root_plus_one_N": math.gcd(root + 1, modulus),
        }
        break
    if useful is None:
        raise AssertionError("public matrix has no useful basis vector")
    if not set(useful["selected_columns_zero_based"]).issubset(
        set(full["core_columns_zero_based"])
    ):
        raise AssertionError("useful vector is not inside the public core")

    prefix_records = [item for item in unique_records if item[0] < 5_616]
    prefix_matrix = matrix_for(prefix_records)
    prefix = summarize(prefix_matrix, len(prefix_records))
    if not prefix["kernel_preserved"]:
        raise AssertionError("prefix peeling changed nullity")

    core_set = set(full["core_columns_zero_based"])
    kinds = Counter()
    families = Counter()
    orientations = Counter()
    for column in core_set:
        provenance = unique_records[column][1]["provenance"]
        kind = str(provenance["kind"])
        kinds[kind] += 1
        if kind == "initial_seed":
            families[f"seed:{provenance['seed']}"] += 1
            orientations["seed"] += 1
        else:
            families[
                f"{provenance['active_relation_index_zero_based']}:"
                f"{provenance['u']}:{provenance['v']}"
            ] += 1
            orientations[str(provenance["orientation"])] += 1

    for summary in (full, prefix):
        columns = summary.pop("core_columns_zero_based")
        summary["core_columns_sha256"] = hashlib.sha256(
            ",".join(map(str, columns)).encode()
        ).hexdigest()

    output = {
        "status": "PASS",
        "role": "N-only factor-free parity-core replay",
        "forbidden_operations_used": [],
        "N": modulus,
        "n": n,
        "B": bound,
        "f98_source_sha256": hashlib.sha256(F98_SOURCE.read_bytes()).hexdigest(),
        "retained_relation_count": len(records),
        "unique_relation_count": len(unique_records),
        "active_pairs": [list(pair) for _, pair in active],
        "full": full,
        "raw_prefix_5616": prefix,
        "first_useful_basis_vector": useful,
        "useful_vector_entirely_in_full_core": True,
        "full_matrix_stats": {
            key: full_matrix[key]
            for key in ("coprime_blocks", "square_blocks", "refinements", "gcd_tests")
        },
        "prefix_matrix_stats": {
            key: prefix_matrix[key]
            for key in ("coprime_blocks", "square_blocks", "refinements", "gcd_tests")
        },
        "full_core_provenance_counts": dict(sorted(kinds.items())),
        "full_core_family_counts": dict(sorted(families.items())),
        "full_core_orientation_counts": dict(sorted(orientations.items())),
        "elapsed_seconds": time.monotonic() - started,
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print("status=PASS")
    print(
        f"full rows={full['rows']} columns={full['columns']} "
        f"rank={full['rank']} nullity={full['nullity']}"
    )
    print(
        f"full core rows={full['core_rows']} columns={full['core_columns']} "
        f"rank={full['core_rank']} nullity={full['core_nullity']}"
    )
    print(
        f"prefix core rows={prefix['core_rows']} columns={prefix['core_columns']} "
        f"rank={prefix['core_rank']} nullity={prefix['core_nullity']}"
    )
    print(f"elapsed_seconds={output['elapsed_seconds']:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
