#!/usr/bin/env python3
"""Factorization-free public replay of C2T round one on one input.

The executable receives only N. It does not call integer factorization,
primality testing, order finding, or a target selector.
"""

from __future__ import annotations

import argparse
import json
import math
import time
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


def add_signatures(
    left: dict[int, int], right: dict[int, int]
) -> dict[int, int]:
    result = dict(left)
    for endpoint, exponent in right.items():
        result[endpoint] = result.get(endpoint, 0) + exponent
    return result


def scale_signature(signature: dict[int, int], scale: int) -> dict[int, int]:
    if scale == 1:
        return signature
    return {endpoint: scale * exponent for endpoint, exponent in signature.items()}


def gcd_free_basis(
    endpoint_values: list[int],
) -> tuple[list[tuple[int, dict[int, int]]], dict[str, int]]:
    """Split endpoints into a pairwise-coprime perfect-power-free basis."""
    pending = [
        (value, {endpoint: 1})
        for endpoint, value in enumerate(endpoint_values)
        if value > 1
    ]
    basis: list[tuple[int, dict[int, int]]] = []
    gcd_calls = 0
    overlap_splits = 0
    perfect_power_splits = 0
    identical_merges = 0

    while pending:
        value, signature = pending.pop()
        if value == 1:
            continue
        root, power = primitive_root(value)
        if power > 1:
            value = root
            signature = scale_signature(signature, power)
            perfect_power_splits += 1

        for position, (old_value, old_signature) in enumerate(basis):
            gcd_calls += 1
            common = math.gcd(value, old_value)
            if common == 1:
                continue
            basis.pop(position)
            if value == old_value:
                pending.append((value, add_signatures(signature, old_signature)))
                identical_merges += 1
                break
            pending.append((common, signature))
            pending.append((value // common, signature))
            pending.append((common, old_signature))
            pending.append((old_value // common, old_signature))
            overlap_splits += 1
            break
        else:
            basis.append((value, signature))

    basis.sort(key=lambda item: item[0])
    for index, (value, _) in enumerate(basis):
        if primitive_root(value)[1] != 1:
            raise AssertionError("A final basis block is still a perfect power.")
        for old_value, _ in basis[:index]:
            if math.gcd(value, old_value) != 1:
                raise AssertionError("The final basis is not pairwise coprime.")

    reconstructed = [1] * len(endpoint_values)
    for block, signature in basis:
        for endpoint, exponent in signature.items():
            reconstructed[endpoint] *= block**exponent
    if reconstructed != endpoint_values:
        raise AssertionError("The factorization-free endpoint basis did not reconstruct.")
    return basis, {
        "gcd_calls": gcd_calls,
        "overlap_splits": overlap_splits,
        "perfect_power_splits": perfect_power_splits,
        "identical_merges": identical_merges,
    }


def relation_columns(
    basis: list[tuple[int, dict[int, int]]], relation_count: int
) -> list[dict[int, int]]:
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
    """Audited P66 factor-free parity refinement, copied self-contained."""
    stable = []
    work = [(value, mask) for value, mask in initial_entries if value > 1 and mask]
    refinements = 0
    gcd_tests = 0

    while work:
        value, mask = work.pop()
        for index, (basis_value, basis_mask) in enumerate(stable):
            gcd_tests += 1
            divisor = math.gcd(value, basis_value)
            if divisor == 1:
                continue

            stable.pop(index)
            refinements += 1
            for new_value, new_mask in (
                (divisor, mask ^ basis_mask),
                (value // divisor, mask),
                (basis_value // divisor, basis_mask),
            ):
                if new_value > 1 and new_mask:
                    work.append((new_value, new_mask))
            break
        else:
            stable.append((value, mask))

    return stable, refinements, gcd_tests


def binary_kernel_basis(row_masks: list[int], column_count: int):
    """Audited P66 binary kernel routine, copied self-contained."""
    pivots = {}
    for original in row_masks:
        row = original
        while row:
            pivot = row.bit_length() - 1
            known = pivots.get(pivot)
            if known is None:
                pivots[pivot] = row
                break
            row ^= known

    kernel = []
    pivot_columns = set(pivots)
    ordered_pivots = sorted(pivots)
    for free_column in range(column_count):
        if free_column in pivot_columns:
            continue
        vector = 1 << free_column
        for pivot in ordered_pivots:
            if (pivots[pivot] & vector).bit_count() & 1:
                vector ^= 1 << pivot
        if not all(not ((row & vector).bit_count() & 1) for row in pivots.values()):
            raise AssertionError("The public binary kernel reconstruction failed.")
        kernel.append(vector)

    return len(pivots), kernel


def decode_relations(
    modulus: int, records: list[dict[str, object]]
) -> dict[str, object]:
    """P66 batch decoder with first-occurrence provenance retained."""
    unique_records = []
    seen_products = set()
    duplicate_count = 0
    zero_count = 0
    for raw_index, record in enumerate(records):
        product = int(record["P"])
        if product == 1:
            zero_count += 1
            continue
        if product in seen_products:
            duplicate_count += 1
            continue
        seen_products.add(product)
        unique_records.append((raw_index, record))

    initial_entries = []
    relation_values = []
    for column, (_, record) in enumerate(unique_records):
        mask = 1 << column
        c = int(record["c"])
        w = int(record["w"])
        product = int(record["P"])
        if c * w != product or product % modulus != 1:
            raise AssertionError("A retained canonical relation is invalid.")
        initial_entries.append((c, mask))
        initial_entries.append((w, mask))
        relation_values.append(product)

    blocks, refinements, gcd_tests = parity_coprime_basis(initial_entries)
    row_masks = []
    square_block_count = 0
    for value, mask in blocks:
        root = math.isqrt(value)
        if root * root == value:
            square_block_count += 1
        else:
            row_masks.append(mask)

    rank, kernel = binary_kernel_basis(row_masks, len(unique_records))
    if rank + len(kernel) != len(unique_records):
        raise AssertionError("Rank-nullity failed in the public decoder.")

    global_plus = 0
    global_minus = 0
    first_certificate = None
    for vector in kernel:
        selected_columns = []
        product = 1
        remaining = vector
        while remaining:
            low_bit = remaining & -remaining
            column = low_bit.bit_length() - 1
            selected_columns.append(column)
            product *= relation_values[column]
            remaining ^= low_bit
        root = math.isqrt(product)
        if root * root != product:
            raise AssertionError("A public kernel vector did not give an exact square.")
        residue = root % modulus
        if residue == 1:
            global_plus += 1
            continue
        if residue == modulus - 1:
            global_minus += 1
            continue
        minus = math.gcd(root - 1, modulus)
        plus = math.gcd(root + 1, modulus)
        if not (1 < minus < modulus or 1 < plus < modulus):
            raise AssertionError("A non-global root did not expose a proper divisor.")
        raw_indices = [unique_records[column][0] for column in selected_columns]
        first_certificate = {
            "selected_columns_zero_based": selected_columns,
            "selected_raw_indices_zero_based": raw_indices,
            "support": len(selected_columns),
            "distinct_relation_values": len(
                {relation_values[column] for column in selected_columns}
            ),
            "root_mod_N": residue,
            "gcd_root_minus_one_N": minus,
            "gcd_root_plus_one_N": plus,
            "witness_records": [unique_records[column][1] for column in selected_columns],
        }
        break

    return {
        "status": "factor" if first_certificate is not None else "null",
        "raw_relation_count": len(records),
        "zero_relation_count": zero_count,
        "duplicate_relation_value_count": duplicate_count,
        "unique_relation_count": len(unique_records),
        "coprime_block_count": len(blocks),
        "square_block_count": square_block_count,
        "nonsquare_row_count": len(row_masks),
        "squareclass_rank": rank,
        "kernel_dimension": len(kernel),
        "global_plus_basis_roots_before_factor": global_plus,
        "global_minus_basis_roots_before_factor": global_minus,
        "gcd_refinements": refinements,
        "gcd_pair_tests": gcd_tests,
        "first_useful_certificate": first_certificate,
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
            args.output.write_text(
                json.dumps(
                    {"status": "trial_factor", "factor": divisor},
                    indent=2,
                    sort_keys=True,
                )
                + "\n"
            )
            return 0

    records: list[dict[str, object]] = []
    endpoint_values: list[int] = []
    seen: set[int] = set()

    def retain(c: int, provenance: dict[str, object]) -> dict[str, object] | None:
        if c in seen:
            return None
        seen.add(c)
        w = pow(c, -1, modulus)
        for sign, difference in (("minus", c - w), ("plus", c + w)):
            divisor = math.gcd(difference, modulus)
            if 1 < divisor < modulus:
                return {
                    "status": "direct_factor",
                    "factor": divisor,
                    "sign": sign,
                    "c": c,
                    "w": w,
                    "provenance": provenance,
                }
        records.append({"c": c, "w": w, "P": c * w, "provenance": provenance})
        endpoint_values.extend((c, w))
        return None

    for seed in range(2, n + 1):
        direct = retain(seed, {"kind": "initial_seed", "seed": seed})
        if direct is not None:
            args.output.write_text(json.dumps(direct, indent=2, sort_keys=True) + "\n")
            return 0

    initial_basis, initial_basis_stats = gcd_free_basis(endpoint_values)
    initial_columns = relation_columns(initial_basis, len(records))
    initial_decoder = decode_relations(modulus, records)
    if initial_decoder["status"] == "factor":
        output = {
            "experiment": "F98_multiseed_presentation_closure_kill",
            "role": "factorization-free public replay of C2T initial state",
            "input_policy": "executable receives only N",
            "forbidden_operations_used": [],
            "N": modulus,
            "n": n,
            "B": bound,
            "trial_screen_null": True,
            "initial_decoder": initial_decoder,
        }
        args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
        return 0
    active = []
    for relation_index, column in enumerate(initial_columns):
        if not any(exponent & 1 for exponent in column.values()):
            continue
        support = sorted(initial_basis[index][0] for index in column)
        pair = (support[0], 1) if len(support) == 1 else tuple(support[:2])
        active.append((relation_index, pair))
        if len(active) == n:
            break

    direct_relations_examined = 0
    for relation_index, (u, v) in active:
        for exponent in range(bound + 1):
            candidates = (
                ("u_power_times_v", pow(u, exponent, modulus) * v % modulus),
                ("u_times_v_power", u * pow(v, exponent, modulus) % modulus),
            )
            for orientation, c in candidates:
                before = len(records)
                direct = retain(
                    c,
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
                if len(records) > before:
                    direct_relations_examined += 1
                if direct is not None:
                    output = {
                        "experiment": "F98_multiseed_presentation_closure_kill",
                        "input_policy": "executable receives only N",
                        "N": modulus,
                        "n": n,
                        "B": bound,
                        "direct_screen": direct,
                    }
                    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
                    return 0

    decoder = decode_relations(modulus, records)
    output = {
        "experiment": "F98_multiseed_presentation_closure_kill",
        "role": "factorization-free public replay of C2T round one",
        "input_policy": "executable receives only N",
        "forbidden_operations_used": [],
        "N": modulus,
        "n": n,
        "B": bound,
        "trial_screen_null": True,
        "initial_seed_count": n - 1,
        "initial_basis_size": len(initial_basis),
        "initial_basis_stats": initial_basis_stats,
        "initial_decoder": initial_decoder,
        "active_pairs": [list(pair) for _, pair in active],
        "direct_screen": {
            "status": "complete_round_one_null",
            "new_relations_examined": direct_relations_examined,
        },
        "retained_relation_count": len(records),
        "retained_endpoint_count": len(endpoint_values),
        "decoder": decoder,
        "elapsed_seconds": time.monotonic() - started,
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(f"relations={len(records)}")
    print(f"decoder_status={decoder['status']}")
    if decoder["status"] == "factor":
        certificate = decoder["first_useful_certificate"]
        print(
            "factors="
            f"{certificate['gcd_root_minus_one_N']},"
            f"{certificate['gcd_root_plus_one_N']}"
        )
    print(f"elapsed_seconds={output['elapsed_seconds']:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
