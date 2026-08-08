#!/usr/bin/env python3
"""Proof-blind, factor-free reconstruction for the public F108 statement.

The only data inputs are RECONSTRUCT_STATEMENT.md and the pinned public F98
JSON. This program never factors an endpoint or relation value.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path


PINNED_PUBLIC_SHA256 = "ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_square(value: int) -> bool:
    root = math.isqrt(value)
    return root * root == value


def gf2_rank(masks: set[int]) -> int:
    """Set-valued, lowest-pivot elimination over GF(2)."""
    basis: dict[int, set[int]] = {}
    for mask in sorted(masks):
        row = {bit for bit in range(mask.bit_length()) if mask >> bit & 1}
        while row:
            pivot = min(row)
            prior = basis.get(pivot)
            if prior is None:
                basis[pivot] = row
                break
            row.symmetric_difference_update(prior)
    return len(basis)


def mask_record(mask: int) -> dict[str, object]:
    return {
        "hex": hex(mask),
        "support_columns_zero_based": [
            bit for bit in range(mask.bit_length()) if mask >> bit & 1
        ],
        "weight": mask.bit_count(),
    }


def coprime_refinement(
    endpoint_blocks: list[tuple[int, int]],
) -> tuple[list[tuple[int, int]], dict[str, int]]:
    """Refine with gcd and exact division until surviving values are coprime."""
    pending = list(reversed(endpoint_blocks))
    basis: list[tuple[int, int]] = []
    gcd_tests = 0
    refinements = 0
    discarded_zero_masks = 0
    discarded_ones = 0
    maximum_live_blocks = len(pending)
    while pending:
        value, mask = pending.pop()
        if value == 1:
            discarded_ones += 1
            continue
        if mask == 0:
            discarded_zero_masks += 1
            continue
        for index, (other, other_mask) in enumerate(basis):
            gcd_tests += 1
            divisor = math.gcd(value, other)
            if divisor == 1:
                continue
            basis.pop(index)
            refinements += 1
            pieces = (
                (divisor, mask ^ other_mask),
                (value // divisor, mask),
                (other // divisor, other_mask),
            )
            for piece_value, piece_mask in reversed(pieces):
                if piece_value == 1:
                    discarded_ones += 1
                elif piece_mask == 0:
                    discarded_zero_masks += 1
                else:
                    pending.append((piece_value, piece_mask))
            maximum_live_blocks = max(maximum_live_blocks, len(pending) + len(basis))
            break
        else:
            basis.append((value, mask))
            maximum_live_blocks = max(maximum_live_blocks, len(pending) + len(basis))

    basis.sort()
    for (left, _), (right, _) in combinations(basis, 2):
        if math.gcd(left, right) != 1:
            raise AssertionError("refinement did not produce pairwise-coprime values")
    return basis, {
        "gcd_tests": gcd_tests,
        "refinements": refinements,
        "discarded_zero_masks": discarded_zero_masks,
        "discarded_ones": discarded_ones,
        "maximum_live_blocks": maximum_live_blocks,
    }


def supported_part(value: int, exposure_product: int) -> tuple[int, int, int]:
    """Return S_E(value), the coprime remainder, and the gcd iteration count."""
    supported = math.gcd(value, exposure_product)
    remainder = value // supported
    iterations = 1
    while supported > 1:
        divisor = math.gcd(remainder, supported)
        iterations += 1
        if divisor == 1:
            break
        supported *= divisor
        remainder //= divisor
    if supported * remainder != value or math.gcd(supported, remainder) != 1:
        raise AssertionError("gcd saturation failed")
    return supported, remainder, iterations


def exposure_classification(
    basis: list[tuple[int, int]], exposure_values: list[int]
) -> dict[str, object]:
    exposure_product = math.prod(exposure_values)
    masks = set()
    records = []
    gcd_iterations = 0
    for value, mask in basis:
        supported, remainder, iterations = supported_part(value, exposure_product)
        gcd_iterations += iterations
        nonsquare = not is_square(supported)
        if nonsquare:
            masks.add(mask)
        records.append({
            "basis_value": value,
            "mask_hex": hex(mask),
            "supported_part": supported,
            "unsupported_remainder": remainder,
            "supported_part_is_nonsquare": nonsquare,
        })
    return {
        "insertion_count": len(exposure_values),
        "exposure_product_bit_length": exposure_product.bit_length(),
        "gcd_saturation_iterations": gcd_iterations,
        "distinct_nonsquare_masks": len(masks),
        "rank": gf2_rank(masks),
        "masks": [mask_record(mask) for mask in sorted(masks)],
        "basis_classification": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--statement", type=Path, required=True)
    parser.add_argument("--public", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    statement_path = args.statement.resolve()
    public_path = args.public.resolve()
    output_path = args.output.resolve()
    checks = 0
    verifier_failures: list[str] = []

    def require(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            verifier_failures.append(label)

    public_hash = sha256(public_path)
    statement_hash = sha256(statement_path)
    require(public_hash == PINNED_PUBLIC_SHA256, "public input hash differs from the pin")
    statement_text = statement_path.read_text()
    require("Proof-blind reconstruction statement for F108" in statement_text, "unexpected statement file")
    require("F99 private-row construction" in statement_text, "statement omits its F99 boundary request")

    public = json.loads(public_path.read_text())
    modulus = public["N"]
    bound = public["B"]
    active_pairs = public["active_pairs"]
    records = public["decoder"]["first_useful_certificate"]["witness_records"]
    width = len(records)
    require(width == 166, "public certificate width changed")
    require(modulus == 202537109, "public modulus changed")
    require(bound == 784, "public exponent bound changed")
    require(len(active_pairs) == 27, "public active-pair count changed")

    endpoint_blocks = []
    selected_values = set()
    represented_keys = set()
    for column, record in enumerate(records):
        c_value = record["c"]
        w_value = record["w"]
        require(record["P"] == c_value * w_value, f"column {column}: P differs from c*w")
        require(c_value * w_value % modulus == 1, f"column {column}: endpoints are not inverses")
        require(0 < c_value < modulus, f"column {column}: c outside canonical range")
        require(0 < w_value < modulus, f"column {column}: w outside canonical range")
        require(math.gcd(c_value, modulus) == 1, f"column {column}: c is not a unit")
        require(math.gcd(w_value, modulus) == 1, f"column {column}: w is not a unit")
        column_mask = 1 << column
        endpoint_blocks.append((c_value, column_mask))
        endpoint_blocks.append((w_value, column_mask))
        selected_values.add(record["P"])

        provenance = record["provenance"]
        if provenance["kind"] == "initial_seed":
            require(c_value == provenance["seed"], f"column {column}: seed mismatch")
        else:
            active_index = provenance["active_relation_index_zero_based"]
            orientation = provenance["orientation"]
            u_value = provenance["u"]
            v_value = provenance["v"]
            exponent = provenance["exponent"]
            require(active_pairs[active_index] == [u_value, v_value], f"column {column}: active pair mismatch")
            require(provenance["round"] == 1, f"column {column}: unexpected round")
            if orientation == "u_power_times_v":
                expected_c = pow(u_value, exponent, modulus) * v_value % modulus
            else:
                require(orientation == "u_times_v_power", f"column {column}: unknown orientation")
                expected_c = u_value * pow(v_value, exponent, modulus) % modulus
            require(c_value == expected_c, f"column {column}: trajectory residue mismatch")
            represented_keys.add((active_index, orientation))

    require(len(selected_values) == width, "selected exact relation values are not distinct")
    require(len(represented_keys) == 8, "represented oriented-trajectory count changed")

    basis, refinement_stats = coprime_refinement(endpoint_blocks)
    full_masks = {mask for value, mask in basis if not is_square(value)}
    full_rank = gf2_rank(full_masks)
    full_nullity = width - full_rank
    require(all(mask != 0 for _, mask in basis), "zero mask survived refinement")
    require(all(value > 1 for value, _ in basis), "unit value survived refinement")
    require(all(mask.bit_count() % 2 == 0 for mask in full_masks), "all-column mask is not a dependency")

    trajectory_data = {}
    all_keys = []
    for active_index, (u_value, v_value) in enumerate(active_pairs):
        for orientation in ("u_power_times_v", "u_times_v_power"):
            key = (active_index, orientation)
            all_keys.append(key)
            multiplier = u_value if orientation == "u_power_times_v" else v_value
            c_states = []
            w_states = []
            for exponent in range(bound + 1):
                if orientation == "u_power_times_v":
                    c_value = pow(u_value, exponent, modulus) * v_value % modulus
                else:
                    c_value = u_value * pow(v_value, exponent, modulus) % modulus
                require(math.gcd(c_value, modulus) == 1, f"trajectory {key}, exponent {exponent}: nonunit")
                c_states.append(c_value)
                w_states.append(pow(c_value, -1, modulus))
            transitions = []
            for exponent in range(bound):
                c_numerator = multiplier * c_states[exponent] - c_states[exponent + 1]
                w_numerator = multiplier * w_states[exponent + 1] - w_states[exponent]
                require(c_numerator % modulus == 0, f"trajectory {key}, exponent {exponent}: nonintegral c carry")
                require(w_numerator % modulus == 0, f"trajectory {key}, exponent {exponent}: nonintegral w carry")
                c_carry = c_numerator // modulus
                w_carry = w_numerator // modulus
                require(0 <= c_carry < multiplier, f"trajectory {key}, exponent {exponent}: c carry range")
                require(0 <= w_carry < multiplier, f"trajectory {key}, exponent {exponent}: w carry range")
                if c_carry == 0 and w_carry == 0:
                    require(
                        c_states[exponent] * w_states[exponent]
                        == c_states[exponent + 1] * w_states[exponent + 1],
                        f"trajectory {key}, exponent {exponent}: two-zero values differ",
                    )
                transitions.append((c_carry, w_carry))
            trajectory_data[key] = {
                "multiplier": multiplier,
                "c": c_states,
                "w": w_states,
                "transitions": transitions,
            }
    require(len(all_keys) == 54, "round-one oriented-trajectory count changed")

    def collect_exposures(keys: list[tuple[int, str]], circuit_local: bool) -> tuple[list[int], int]:
        exposures = []
        excluded_two_zero = 0
        for key in keys:
            data = trajectory_data[key]
            for exponent, (c_carry, w_carry) in enumerate(data["transitions"]):
                if c_carry == 0 and w_carry == 0:
                    excluded_two_zero += 1
                    continue
                if circuit_local:
                    left_value = data["c"][exponent] * data["w"][exponent]
                    right_value = data["c"][exponent + 1] * data["w"][exponent + 1]
                    if left_value not in selected_values or right_value not in selected_values:
                        continue
                if c_carry == 0:
                    exposures.append(data["c"][exponent])
                if w_carry == 0:
                    exposures.append(data["w"][exponent + 1])
        return exposures, excluded_two_zero

    represented_order = sorted(represented_keys)
    represented_raw_values, represented_two_zero = collect_exposures(represented_order, False)
    all_raw_values, all_two_zero = collect_exposures(all_keys, False)
    represented_local_values, represented_local_two_zero = collect_exposures(represented_order, True)
    all_local_values, all_local_two_zero = collect_exposures(all_keys, True)
    require(represented_local_two_zero == represented_two_zero, "represented local scan changed two-zero count")
    require(all_local_two_zero == all_two_zero, "all local scan changed two-zero count")

    represented_raw = exposure_classification(basis, represented_raw_values)
    all_raw = exposure_classification(basis, all_raw_values)
    represented_local = exposure_classification(basis, represented_local_values)
    all_local = exposure_classification(basis, all_local_values)

    relation_product = math.prod(record["P"] for record in records)
    exact_root = math.isqrt(relation_product)
    relation_product_is_square = exact_root * exact_root == relation_product
    root_mod_n = exact_root % modulus
    root_minus_gcd = math.gcd(root_mod_n - 1, modulus)
    root_plus_gcd = math.gcd(root_mod_n + 1, modulus)

    fixed_claims = {
        "complete_public_circuit": (
            len(full_masks) == 227 and full_rank == 165 and full_nullity == 1
        ),
        "represented_raw": (
            len(represented_raw_values) == 1840
            and represented_two_zero == 541
            and represented_raw["distinct_nonsquare_masks"] == 191
            and represented_raw["rank"] == 165
        ),
        "all_round_one_raw": (
            len(all_raw_values) == 15935
            and all_two_zero == 6008
            and all_raw["distinct_nonsquare_masks"] == 200
            and all_raw["rank"] == 165
        ),
        "circuit_local": (
            len(represented_local_values) == 34
            and len(all_local_values) == 82
            and all_local["rank"] == 54
        ),
        "all_column_root": (
            relation_product_is_square
            and root_mod_n == 132013085
            and root_minus_gcd == 19727
            and root_plus_gcd == 10267
        ),
    }

    # From canonical inverses alone, 2*w_{e+1}-w_e is either 0 or N. The
    # supplied statement does not include the cited F99 inverse formula (or
    # any F99 parameters), so its choice of N cannot be checked proof-blind.
    f99_counterexample_n = 15
    f99_counterexample_e = 2
    f99_c = 2**f99_counterexample_e
    f99_next_c = 2 * f99_c
    f99_w = pow(f99_c, -1, f99_counterexample_n)
    f99_next_w = pow(f99_next_c, -1, f99_counterexample_n)
    f99_boundary = {
        "authorized_inverse_formula_present": False,
        "general_carry_dichotomy": "2*w[e+1]-w[e] is 0 when w[e] is even and N when w[e] is odd",
        "condition_for_claimed_identity": "the omitted F99 formula must prove every relevant w[e] is odd",
        "counterexample_to_inference_from_c_e_alone": {
            "N": f99_counterexample_n,
            "e": f99_counterexample_e,
            "c_e": f99_c,
            "c_e_plus_1": f99_next_c,
            "w_e": f99_w,
            "w_e_plus_1": f99_next_w,
            "2w_e_plus_1_minus_w_e": 2 * f99_next_w - f99_w,
        },
        "status": "UNDER_SPECIFIED_BY_AUTHORIZED_STATEMENT",
    }

    statement_verdict = (
        "PASS" if all(fixed_claims.values()) and f99_boundary["status"] == "VERIFIED" else "FAIL"
    )
    canonical_mask_sets = {
        "full_public_circuit": [hex(mask) for mask in sorted(full_masks)],
        "represented_eight_trajectory_raw": [
            record["hex"] for record in represented_raw["masks"]
        ],
        "all_54_trajectory_raw": [record["hex"] for record in all_raw["masks"]],
        "represented_eight_trajectory_circuit_local": [
            record["hex"] for record in represented_local["masks"]
        ],
        "all_54_trajectory_circuit_local": [
            record["hex"] for record in all_local["masks"]
        ],
    }
    canonical_mask_sets_sha256 = hashlib.sha256(
        json.dumps(canonical_mask_sets, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    output = {
        "status": "complete",
        "verifier_status": "PASS" if not verifier_failures else "FAIL",
        "statement_verdict": statement_verdict,
        "fixed_reconstruction_verdict": "PASS" if all(fixed_claims.values()) else "FAIL",
        "checks": checks,
        "verifier_failures": verifier_failures,
        "authorized_inputs": {
            "RECONSTRUCT_STATEMENT.md": statement_hash,
            "experiments/F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json": public_hash,
        },
        "forbidden_operations_used": [],
        "general_theorem": {
            "verdict": "PROVED",
            "proof_location": "RECONSTRUCT.md",
            "algorithm": "pairwise gcd refinement followed by gcd saturation of each coprime block",
            "bit_complexity": "O(L^3 G(L) + L^2 M(L) log L), hence polynomial in the total explicit input bit length L",
        },
        "fixed_claims": fixed_claims,
        "canonical_mask_sets_sha256": canonical_mask_sets_sha256,
        "full_public_circuit": {
            "columns": width,
            "coprime_basis_values": len(basis),
            "distinct_nonsquare_masks": len(full_masks),
            "rank": full_rank,
            "nullity": full_nullity,
            "all_column_dependency": all(mask.bit_count() % 2 == 0 for mask in full_masks),
            "refinement": refinement_stats,
            "masks": [mask_record(mask) for mask in sorted(full_masks)],
            "basis": [
                {
                    "value": value,
                    "value_is_square": is_square(value),
                    "mask": mask_record(mask),
                }
                for value, mask in basis
            ],
        },
        "represented_eight_trajectory_raw": {
            "trajectory_count": len(represented_order),
            "two_zero_transitions_excluded": represented_two_zero,
            **represented_raw,
        },
        "all_54_trajectory_raw": {
            "trajectory_count": len(all_keys),
            "two_zero_transitions_excluded": all_two_zero,
            **all_raw,
        },
        "represented_eight_trajectory_circuit_local": {
            "trajectory_count": len(represented_order),
            "selection_rule": "both adjacent exact relation values occur in the selected 166-value circuit",
            **represented_local,
        },
        "all_54_trajectory_circuit_local": {
            "trajectory_count": len(all_keys),
            "selection_rule": "both adjacent exact relation values occur in the selected 166-value circuit",
            **all_local,
        },
        "all_column_root": {
            "relation_product_is_square": relation_product_is_square,
            "root_mod_N": root_mod_n,
            "gcd_root_minus_one_N": root_minus_gcd,
            "gcd_root_plus_one_N": root_plus_gcd,
        },
        "f99_boundary": f99_boundary,
    }
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "checks": checks,
        "fixed_claims": fixed_claims,
        "statement_verdict": statement_verdict,
        "verifier_failures": verifier_failures,
        "verifier_status": output["verifier_status"],
    }, indent=2, sort_keys=True))
    return 0 if not verifier_failures else 1


if __name__ == "__main__":
    sys.exit(main())
