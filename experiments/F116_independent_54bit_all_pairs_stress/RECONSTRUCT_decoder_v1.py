#!/usr/bin/env python3
"""Proof-blind, factor-free replay of the fixed F116 certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from pathlib import Path


sys.dont_write_bytecode = True


def unsigned_bytes(value: int) -> bytes:
    if value < 0:
        raise ValueError("negative integer in unsigned encoding")
    size = max(1, (value.bit_length() + 7) // 8)
    return value.to_bytes(size, "big")


class IntegerSequenceHash:
    def __init__(self) -> None:
        self.digest = hashlib.sha256()
        self.count = 0

    def add(self, *values: int) -> None:
        for value in values:
            payload = unsigned_bytes(value)
            self.digest.update(len(payload).to_bytes(8, "big"))
            self.digest.update(payload)
            self.count += 1

    def hexdigest(self) -> str:
        result = self.digest.copy()
        result.update(self.count.to_bytes(8, "big"))
        return result.hexdigest()


def hash_integer_sequence(values: list[int]) -> str:
    digest = IntegerSequenceHash()
    digest.add(*values)
    return digest.hexdigest()


def integer_nth_root(value: int, exponent: int) -> int:
    if exponent == 2:
        return math.isqrt(value)
    bit_length = value.bit_length()
    low = 1 << ((bit_length - 1) // exponent)
    high = 1 << ((bit_length + exponent - 1) // exponent)
    while low + 1 < high:
        middle = (low + high) // 2
        if pow(middle, exponent) <= value:
            low = middle
        else:
            high = middle
    return low


_power_cache: dict[int, tuple[int, int]] = {}


def maximal_perfect_power(value: int) -> tuple[int, int]:
    cached = _power_cache.get(value)
    if cached is not None:
        return cached
    for exponent in range(value.bit_length() - 1, 1, -1):
        base = integer_nth_root(value, exponent)
        if pow(base, exponent) == value:
            result = (base, exponent)
            _power_cache[value] = result
            return result
    result = (value, 1)
    _power_cache[value] = result
    return result


def add_signatures(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    result = left.copy()
    for index, multiplicity in right.items():
        result[index] = result.get(index, 0) + multiplicity
    return result


def deterministic_gcd_basis(
    values: list[int],
) -> tuple[list[tuple[int, dict[int, int]]], dict[str, int]]:
    stack = [(value, {index: 1}) for index, value in enumerate(values) if value > 1]
    basis: list[tuple[int, dict[int, int]]] = []
    operations = {
        "initial_stack_items": len(stack),
        "pops": 0,
        "discarded_ones": 0,
        "perfect_power_reductions": 0,
        "basis_gcd_scans": 0,
        "overlaps": 0,
        "equal_merges": 0,
        "proper_splits": 0,
        "basis_appends": 0,
        "maximum_stack_size": len(stack),
        "maximum_basis_size": 0,
    }
    while stack:
        operations["pops"] += 1
        value, signature = stack.pop()
        if value == 1:
            operations["discarded_ones"] += 1
            continue
        base, exponent = maximal_perfect_power(value)
        if exponent > 1:
            value = base
            signature = {
                index: multiplicity * exponent
                for index, multiplicity in signature.items()
            }
            operations["perfect_power_reductions"] += 1
        overlap_index = None
        divisor = 1
        for index, (other_value, _) in enumerate(basis):
            operations["basis_gcd_scans"] += 1
            common = math.gcd(value, other_value)
            if common > 1:
                overlap_index = index
                divisor = common
                break
        if overlap_index is None:
            basis.append((value, signature))
            operations["basis_appends"] += 1
            operations["maximum_basis_size"] = max(
                operations["maximum_basis_size"], len(basis)
            )
            continue
        operations["overlaps"] += 1
        other_value, other_signature = basis.pop(overlap_index)
        if value == other_value:
            stack.append((value, add_signatures(signature, other_signature)))
            operations["equal_merges"] += 1
        else:
            stack.extend(
                [
                    (divisor, signature),
                    (value // divisor, signature),
                    (divisor, other_signature),
                    (other_value // divisor, other_signature),
                ]
            )
            operations["proper_splits"] += 1
        operations["maximum_stack_size"] = max(
            operations["maximum_stack_size"], len(stack)
        )
    basis.sort(key=lambda item: item[0])
    return basis, operations


def validate_basis(
    originals: list[int], basis: list[tuple[int, dict[int, int]]]
) -> dict[str, object]:
    blocks = [block for block, _ in basis]
    pairwise = all(
        math.gcd(blocks[left], blocks[right]) == 1
        for left in range(len(blocks))
        for right in range(left + 1, len(blocks))
    )
    power_free = all(maximal_perfect_power(block)[1] == 1 for block in blocks)
    reconstructed = [1] * len(originals)
    signature_entries = 0
    for block, signature in basis:
        for index, multiplicity in signature.items():
            reconstructed[index] *= pow(block, multiplicity)
            signature_entries += 1
    mismatches = sum(
        expected != actual for expected, actual in zip(originals, reconstructed)
    )
    result = {
        "block_count": len(blocks),
        "block_sha256": hash_integer_sequence(blocks),
        "signature_entry_count": signature_entries,
        "pairwise_coprime": pairwise,
        "perfect_power_free": power_free,
        "exact_endpoint_reconstruction": mismatches == 0,
        "endpoint_reconstruction_mismatch_count": mismatches,
    }
    if not pairwise or not power_free or mismatches:
        raise AssertionError(f"seed basis validation failed: {result}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    started = time.monotonic()

    if maximal_perfect_power(64) != (2, 6):
        raise AssertionError("perfect-power self-check failed")
    input_bytes = arguments.input.read_bytes()
    public = json.loads(input_bytes)
    modulus = int(public["N"])
    bit_length = int(public["n"])
    bound = int(public["bound"])
    stop_count = int(public["source_stop_relation_count"])
    advice = [int(index) for index in public["dependency_relation_indices_zero_based"]]
    if (
        modulus % 2 != 1
        or modulus.bit_length() != bit_length
        or bound != bit_length * bit_length
    ):
        raise AssertionError("public instance metadata is inconsistent")
    advice_increasing = all(
        left < right for left, right in zip(advice, advice[1:])
    )
    advice_distinct = len(set(advice)) == len(advice)
    advice_in_range = bool(advice) and advice[0] >= 0 and advice[-1] < stop_count
    advice_ends_at_stop = bool(advice) and advice[-1] == stop_count - 1
    if not (
        advice_increasing
        and advice_distinct
        and advice_in_range
        and advice_ends_at_stop
    ):
        raise AssertionError("public advice list validation failed")

    trial_nonunits = [
        (value, math.gcd(value, modulus))
        for value in range(2, bound + 1)
        if math.gcd(value, modulus) != 1
    ]
    if trial_nonunits:
        raise AssertionError(f"trial gcd range contains nonunits: {trial_nonunits}")
    print(
        f"public input: N_bits={bit_length} B={bound} stop={stop_count} "
        f"advice={len(advice)}; all trial gcds are one",
        flush=True,
    )

    seen: set[int] = set()
    attempts = 0
    duplicates = 0
    retained = 0
    endpoint_count = 0
    next_attempt_progress = 1_000_000
    provenance_counts = {"seed": 0, "frozen_seed_basis_pair": 0, "nonadaptive_seed_pair": 0}
    screen_counts = {"unit": 0, "improper_nonunit": 0, "proper_factor": 0}
    residue_gcd_counts = {"unit": 0, "proper_factor": 0, "improper_nonunit": 0}
    nonunit_screens: list[dict[str, int | str]] = []
    proper_residue_gcds: list[dict[str, int]] = []
    record_hash = IntegerSequenceHash()
    screen_hash = IntegerSequenceHash()
    selected_record_hash = IntegerSequenceHash()
    selected_values: list[int] = []
    selected_provenance_counts = {
        "seed": 0,
        "frozen_seed_basis_pair": 0,
        "nonadaptive_seed_pair": 0,
    }
    selected_frozen_pair_indices: set[int] = set()
    selected_appended_pair_indices: set[int] = set()
    advice_cursor = 0
    frozen_retained_by_pair: list[int] = []
    appended_retained_by_pair: dict[int, int] = {}
    appended_pair_values: dict[int, tuple[int, int]] = {}

    kind_code = {
        "seed": 0,
        "frozen_seed_basis_pair": 1,
        "nonadaptive_seed_pair": 2,
    }

    def attempt(
        residue: int,
        provenance_kind: str,
        pair_index: int,
        left: int,
        right: int,
        exponent: int,
        orientation: int,
    ) -> bool:
        nonlocal attempts, duplicates, retained, endpoint_count
        nonlocal advice_cursor, next_attempt_progress
        attempts += 1
        if residue in seen:
            duplicates += 1
            return False
        seen.add(residue)
        common = math.gcd(residue, modulus)
        if common == 1:
            residue_gcd_counts["unit"] += 1
        elif common == modulus:
            residue_gcd_counts["improper_nonunit"] += 1
            raise AssertionError(f"canonical residue {residue} is zero modulo N")
        else:
            residue_gcd_counts["proper_factor"] += 1
            proper_residue_gcds.append(
                {"record_index": retained, "residue": residue, "gcd": common}
            )
            raise AssertionError(f"attempted residue gives proper gcd {common}")
        inverse = pow(residue, -1, modulus)
        relation_value = residue * inverse
        if relation_value % modulus != 1:
            raise AssertionError("retained relation is not congruent to one")
        minus_gcd = math.gcd(residue - inverse, modulus)
        plus_gcd = math.gcd(residue + inverse, modulus)
        for sign_code, divisor in ((0, minus_gcd), (1, plus_gcd)):
            if divisor == 1:
                classification = "unit"
                class_code = 0
            elif divisor == modulus:
                classification = "improper_nonunit"
                class_code = 1
            else:
                classification = "proper_factor"
                class_code = 2
            screen_counts[classification] += 1
            screen_hash.add(retained, sign_code, divisor, class_code)
            if classification != "unit":
                nonunit_screens.append(
                    {
                        "record_index": retained,
                        "provenance": provenance_kind,
                        "pair_index": pair_index,
                        "residue": residue,
                        "inverse": inverse,
                        "sign": "minus" if sign_code == 0 else "plus",
                        "gcd": divisor,
                        "classification": classification,
                    }
                )
        code = kind_code[provenance_kind]
        record_hash.add(
            retained,
            code,
            pair_index,
            left,
            right,
            exponent,
            orientation,
            residue,
            inverse,
            relation_value,
            minus_gcd,
            plus_gcd,
        )
        provenance_counts[provenance_kind] += 1
        if provenance_kind == "frozen_seed_basis_pair":
            frozen_retained_by_pair[pair_index] += 1
        elif provenance_kind == "nonadaptive_seed_pair":
            appended_retained_by_pair[pair_index] = (
                appended_retained_by_pair.get(pair_index, 0) + 1
            )
        if advice_cursor < len(advice) and retained == advice[advice_cursor]:
            selected_values.append(relation_value)
            selected_provenance_counts[provenance_kind] += 1
            if provenance_kind == "frozen_seed_basis_pair":
                selected_frozen_pair_indices.add(pair_index)
            elif provenance_kind == "nonadaptive_seed_pair":
                selected_appended_pair_indices.add(pair_index)
            selected_record_hash.add(
                retained,
                code,
                pair_index,
                left,
                right,
                exponent,
                orientation,
                residue,
                inverse,
                relation_value,
            )
            advice_cursor += 1
        retained += 1
        endpoint_count += 2
        if attempts >= next_attempt_progress:
            print(
                f"progress attempts={attempts} retained={retained} duplicates={duplicates}",
                flush=True,
            )
            next_attempt_progress += 1_000_000
        return True

    for seed in range(2, bit_length + 1):
        attempt(seed, "seed", seed - 2, seed, 1, 0, 0)
    seed_record_count = retained
    seed_endpoints: list[int] = []
    for seed in range(2, bit_length + 1):
        inverse = pow(seed, -1, modulus)
        seed_endpoints.extend((seed, inverse))
    seed_basis, seed_basis_operations = deterministic_gcd_basis(seed_endpoints)
    seed_basis_validation = validate_basis(seed_endpoints, seed_basis)
    frozen_pairs: list[tuple[int, int]] = []
    for seed_index in range(seed_record_count):
        left_endpoint = 2 * seed_index
        right_endpoint = left_endpoint + 1
        support = [
            block
            for block, signature in seed_basis
            if signature.get(left_endpoint, 0)
            + signature.get(right_endpoint, 0)
            > 0
        ]
        if not support:
            raise AssertionError("seed relation has empty basis support")
        frozen_pairs.append(
            (support[0], 1 if len(support) == 1 else support[1])
        )
    frozen_retained_by_pair = [0] * len(frozen_pairs)
    print(
        f"seed basis blocks={len(seed_basis)} frozen_pairs={len(frozen_pairs)}",
        flush=True,
    )

    frozen_attempt_start = attempts
    frozen_duplicate_start = duplicates
    frozen_retained_start = retained
    for pair_index, (left, right) in enumerate(frozen_pairs):
        left_power = 1
        right_power = 1
        for exponent in range(bound + 1):
            attempt(
                (left_power * right) % modulus,
                "frozen_seed_basis_pair",
                pair_index,
                left,
                right,
                exponent,
                0,
            )
            attempt(
                (left * right_power) % modulus,
                "frozen_seed_basis_pair",
                pair_index,
                left,
                right,
                exponent,
                1,
            )
            left_power = (left_power * left) % modulus
            right_power = (right_power * right) % modulus
    frozen_attempt_count = attempts - frozen_attempt_start
    frozen_duplicate_count = duplicates - frozen_duplicate_start
    frozen_trajectory_retained_count = retained - frozen_retained_start
    expected_frozen_attempts = len(frozen_pairs) * 2 * (bound + 1)
    if frozen_attempt_count != expected_frozen_attempts:
        raise AssertionError("frozen attempt count is incomplete")
    retained_before_menu = retained
    print(
        f"frozen attempts={frozen_attempt_count} duplicates={frozen_duplicate_count} "
        f"retained={frozen_trajectory_retained_count} total_records={retained}",
        flush=True,
    )

    menu_attempt_start = attempts
    menu_duplicate_start = duplicates
    menu_pairs_started = 0
    menu_pairs_completed = 0
    final_pair_complete = False
    stop_reached = retained == stop_count
    menu_index = 0
    for left in range(2, bit_length):
        if stop_reached:
            break
        for right in range(left + 1, bit_length + 1):
            if stop_reached:
                break
            current_index = menu_index
            menu_index += 1
            menu_pairs_started += 1
            appended_pair_values[current_index] = (left, right)
            left_power = 1
            right_power = 1
            pair_complete = True
            for exponent in range(bound + 1):
                attempt(
                    (left_power * right) % modulus,
                    "nonadaptive_seed_pair",
                    current_index,
                    left,
                    right,
                    exponent,
                    0,
                )
                if retained == stop_count:
                    stop_reached = True
                    pair_complete = False
                    break
                attempt(
                    (left * right_power) % modulus,
                    "nonadaptive_seed_pair",
                    current_index,
                    left,
                    right,
                    exponent,
                    1,
                )
                if retained == stop_count:
                    stop_reached = True
                    pair_complete = exponent == bound
                    break
                left_power = (left_power * left) % modulus
                right_power = (right_power * right) % modulus
            if pair_complete:
                menu_pairs_completed += 1
            final_pair_complete = pair_complete
    if not stop_reached or retained != stop_count:
        raise AssertionError("declared retained-record stop was not reached exactly")
    menu_attempt_count = attempts - menu_attempt_start
    menu_duplicate_count = duplicates - menu_duplicate_start
    menu_retained_count = retained - retained_before_menu
    if advice_cursor != len(advice) or len(selected_values) != len(advice):
        raise AssertionError("not every advised record was captured")
    print(
        f"menu pairs_started={menu_pairs_started} completed={menu_pairs_completed} "
        f"attempts={menu_attempt_count} duplicates={menu_duplicate_count} "
        f"retained={menu_retained_count}; exact stop reached",
        flush=True,
    )

    selected_product = math.prod(selected_values)
    selected_root = math.isqrt(selected_product)
    selected_product_is_square = selected_root * selected_root == selected_product
    if not selected_product_is_square:
        raise AssertionError("advised exact product is not a positive square")
    root_residue = selected_root % modulus
    root_squares_to_one = pow(root_residue, 2, modulus) == 1
    root_is_global = root_residue in (1, modulus - 1)
    terminal_minus = math.gcd(root_residue - 1, modulus)
    terminal_plus = math.gcd(root_residue + 1, modulus)
    terminal_product = terminal_minus * terminal_plus
    terminal_gcds_proper = all(
        1 < divisor < modulus for divisor in (terminal_minus, terminal_plus)
    )
    if (
        not root_squares_to_one
        or root_is_global
        or not terminal_gcds_proper
        or terminal_product != modulus
    ):
        raise AssertionError("terminal square-root or gcd certificate failed")

    selected_appended_pairs = [
        {
            "menu_index": index,
            "u": appended_pair_values[index][0],
            "v": appended_pair_values[index][1],
        }
        for index in sorted(selected_appended_pair_indices)
    ]
    nonunit_improper_count = sum(
        detail["classification"] == "improper_nonunit"
        for detail in nonunit_screens
    )
    nonunit_proper_count = sum(
        detail["classification"] == "proper_factor"
        for detail in nonunit_screens
    )
    full_menu_pair_count = (bit_length - 1) * (bit_length - 2) // 2
    last_started_index = menu_pairs_started - 1
    last_started_pair = appended_pair_values[last_started_index]

    output = {
        "verdict": "PASS",
        "public_instance": {
            "N": modulus,
            "n": bit_length,
            "bound": bound,
            "source_stop_relation_count": stop_count,
            "input_sha256": hashlib.sha256(input_bytes).hexdigest(),
            "trial_gcd_start": 2,
            "trial_gcd_end": bound,
            "trial_nonunit_count": len(trial_nonunits),
        },
        "advice": {
            "index_count": len(advice),
            "indices_sha256": hash_integer_sequence(advice),
            "strictly_increasing": advice_increasing,
            "distinct": advice_distinct,
            "in_range": advice_in_range,
            "first_index": advice[0],
            "last_index": advice[-1],
            "ends_at_final_retained_record": advice_ends_at_stop,
        },
        "seed_basis": {
            "blocks": [block for block, _ in seed_basis],
            "operations": seed_basis_operations,
            "validation": seed_basis_validation,
            "frozen_pairs": [[left, right] for left, right in frozen_pairs],
            "frozen_pair_count": len(frozen_pairs),
        },
        "source": {
            "seed_record_count": seed_record_count,
            "frozen_trajectory_attempt_count": frozen_attempt_count,
            "frozen_trajectory_duplicate_count": frozen_duplicate_count,
            "frozen_trajectory_retained_count": frozen_trajectory_retained_count,
            "frozen_layer_record_count_including_seeds": retained_before_menu,
            "frozen_retained_by_pair": frozen_retained_by_pair,
            "full_small_pair_menu_count": full_menu_pair_count,
            "menu_pairs_started": menu_pairs_started,
            "menu_pairs_completed": menu_pairs_completed,
            "final_started_pair_complete": final_pair_complete,
            "last_started_menu_index": last_started_index,
            "last_started_pair": [last_started_pair[0], last_started_pair[1]],
            "menu_pairs_with_retained_records": len(appended_retained_by_pair),
            "menu_attempt_count": menu_attempt_count,
            "menu_duplicate_count": menu_duplicate_count,
            "menu_retained_count": menu_retained_count,
            "total_attempt_count": attempts,
            "total_duplicate_count": duplicates,
            "total_retained_record_count": retained,
            "endpoint_count": endpoint_count,
            "exact_stop_reached": retained == stop_count,
            "provenance_counts": provenance_counts,
            "record_sequence_sha256": record_hash.hexdigest(),
        },
        "direct_screens": {
            "retained_residue_gcd_counts": residue_gcd_counts,
            "sign_screen_counts": screen_counts,
            "sign_screen_count": sum(screen_counts.values()),
            "screen_transcript_sha256": screen_hash.hexdigest(),
            "nonunit_improper_count": nonunit_improper_count,
            "proper_factor_count": nonunit_proper_count,
            "nonunit_screen_details": nonunit_screens,
            "proper_residue_gcds": proper_residue_gcds,
        },
        "selected_certificate": {
            "selected_record_count": len(selected_values),
            "selected_provenance_counts": selected_provenance_counts,
            "selected_distinct_frozen_pair_count": len(
                selected_frozen_pair_indices
            ),
            "selected_distinct_appended_pair_count": len(
                selected_appended_pair_indices
            ),
            "selected_appended_pairs": selected_appended_pairs,
            "selected_record_transcript_sha256": selected_record_hash.hexdigest(),
            "selected_values_sha256": hash_integer_sequence(selected_values),
            "product_is_positive_square": selected_product_is_square,
            "product_bit_length": selected_product.bit_length(),
            "product_sha256": hash_integer_sequence([selected_product]),
            "positive_root_bit_length": selected_root.bit_length(),
            "positive_root_sha256": hash_integer_sequence([selected_root]),
            "root_residue_mod_N": root_residue,
            "root_squares_to_one_mod_N": root_squares_to_one,
            "root_is_global_plus_or_minus_one": root_is_global,
            "gcd_root_minus_one_N": terminal_minus,
            "gcd_root_plus_one_N": terminal_plus,
            "terminal_gcds_are_proper": terminal_gcds_proper,
            "terminal_gcd_product": terminal_product,
            "terminal_gcd_product_equals_N": terminal_product == modulus,
        },
        "method_boundary": {
            "factorization_used": False,
            "primality_test_used": False,
            "known_factor_used": False,
            "allowed_operations": [
                "integer gcd",
                "modular inverse",
                "modular multiplication",
                "exact perfect-power extraction",
                "exact integer square root",
            ],
            "advice_statement": (
                "The supplied 6486-index support is external advice. "
                "The replay verifies it and does not discover it."
            ),
            "monotonic_statement": (
                "Appending more ordered records preserves every record in this valid exact-square support, "
                "so dependency existence is monotone for this source prefix. A separate complete factor-free decoder "
                "can inspect the full public pair menu without the stop or advice."
            ),
            "fixed_instance_statement": (
                f"This proves only the advised certificate for N={modulus}, n={bit_length}, "
                f"B={bound}, stop={stop_count}, and the specified source order. "
                "It is not an all-input factoring theorem."
            ),
        },
        "elapsed_seconds_decoder": time.monotonic() - started,
    }
    arguments.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        f"certificate PASS root_mod_N={root_residue} "
        f"gcds=({terminal_minus},{terminal_plus}); wrote {arguments.output}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
