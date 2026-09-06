#!/usr/bin/env python3
"""Statement-only reconstruction of the F165-R02 V2 finite replay.

This program deliberately uses only Python's standard library.  It constructs
the public corpus, analyzes each N without receiving its factors, and emits a
canonical JSON transcript with deterministic sequence hashes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from functools import lru_cache
from pathlib import Path
from typing import Any


EXPECTED_CORPUS_SHA256 = (
    "bd1d2987d2eaa6d3cfda3fceea72fbd471592a659137df26ae05a3d86cec7fb3"
)


def unsigned_bytes(value: int) -> bytes:
    return value.to_bytes((value.bit_length() + 7) // 8, "big")


def corpus_hash(pairs: list[tuple[int, int]]) -> str:
    digest = hashlib.sha256()
    values = [value for pair in pairs for value in pair]
    for value in values:
        encoded = unsigned_bytes(value)
        digest.update(len(encoded).to_bytes(8, "big"))
        digest.update(encoded)
    digest.update(len(values).to_bytes(8, "big"))
    return digest.hexdigest()


def canonical_bytes(value: Any) -> bytes:
    """Typed, recursively framed encoding used for every sequence hash."""
    if value is None:
        return b"N"
    if value is True:
        return b"T"
    if value is False:
        return b"F"
    if isinstance(value, int):
        encoded = unsigned_bytes(value)
        return b"I" + len(encoded).to_bytes(8, "big") + encoded
    if isinstance(value, str):
        encoded = value.encode("utf-8")
        return b"S" + len(encoded).to_bytes(8, "big") + encoded
    if isinstance(value, (list, tuple)):
        return (
            b"L"
            + len(value).to_bytes(8, "big")
            + b"".join(canonical_bytes(item) for item in value)
        )
    if isinstance(value, dict):
        keys = sorted(value)
        return (
            b"D"
            + len(keys).to_bytes(8, "big")
            + b"".join(
                canonical_bytes(key) + canonical_bytes(value[key]) for key in keys
            )
        )
    raise TypeError(type(value).__name__)


def sequence_hash(sequence: list[Any]) -> str:
    return hashlib.sha256(canonical_bytes(sequence)).hexdigest()


def integer_nth_root(value: int, exponent: int) -> int:
    low = 1
    high = 1 << ((value.bit_length() + exponent - 1) // exponent)
    while low + 1 < high:
        middle = (low + high) // 2
        if pow(middle, exponent) <= value:
            low = middle
        else:
            high = middle
    return low


@lru_cache(maxsize=None)
def maximal_perfect_power(value: int) -> tuple[int, int]:
    for exponent in range(value.bit_length(), 1, -1):
        root = integer_nth_root(value, exponent)
        if pow(root, exponent) == value:
            return root, exponent
    return value, 1


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def make_corpus() -> list[tuple[int, int]]:
    primes = [value for value in range(10000, 20001) if is_prime(value)]
    pairs: list[tuple[int, int]] = []
    for p in primes:
        for q in primes:
            if q <= p:
                continue
            if q >= 2 * p:
                break
            pairs.append((p, q))
            if len(pairs) == 64:
                return pairs
    raise AssertionError("the public interval did not supply 64 pairs")


def merge_components(
    components: list[tuple[int, dict[int, int]]],
) -> list[tuple[int, dict[int, int]]]:
    merged: dict[int, dict[int, int]] = {}
    for base, exponents in components:
        if base == 1:
            continue
        target = merged.setdefault(base, {})
        for label, exponent in exponents.items():
            target[label] = target.get(label, 0) + exponent
    return sorted(merged.items())


def factor_free_components(
    labelled_values: list[tuple[int, int]],
) -> list[tuple[int, dict[int, int]]]:
    """Return a multiplicity-aware gcd-free basis without factoring values."""
    components = [(value, {label: 1}) for label, value in labelled_values]
    components = merge_components(components)
    while True:
        changed = False
        for index, (base, exponents) in enumerate(components):
            root, power = maximal_perfect_power(base)
            if power > 1:
                scaled = {
                    label: exponent * power for label, exponent in exponents.items()
                }
                components = merge_components(
                    components[:index] + components[index + 1 :] + [(root, scaled)]
                )
                changed = True
                break
        if changed:
            continue

        for left in range(len(components)):
            for right in range(left + 1, len(components)):
                left_base, left_exponents = components[left]
                right_base, right_exponents = components[right]
                common = math.gcd(left_base, right_base)
                if common == 1:
                    continue
                common_exponents = dict(left_exponents)
                for label, exponent in right_exponents.items():
                    common_exponents[label] = (
                        common_exponents.get(label, 0) + exponent
                    )
                replacements = [(common, common_exponents)]
                if left_base != common:
                    replacements.append((left_base // common, left_exponents))
                if right_base != common:
                    replacements.append((right_base // common, right_exponents))
                components = merge_components(
                    components[:left]
                    + components[left + 1 : right]
                    + components[right + 1 :]
                    + replacements
                )
                changed = True
                break
            if changed:
                break
        if not changed:
            break

    for index, (base, _) in enumerate(components):
        assert maximal_perfect_power(base) == (base, 1)
        for other_base, _ in components[index + 1 :]:
            assert math.gcd(base, other_base) == 1
    return components


def proper(value: int, modulus: int) -> bool:
    return 1 < value < modulus


def offer_record(
    modulus: int,
    ledger: list[dict[str, Any]],
    record_by_value: dict[int, int],
    value: int,
    supplied_root: int,
    layer: str,
) -> tuple[str, dict[str, Any] | None]:
    if value not in record_by_value:
        record_by_value[value] = len(ledger)
        ledger.append(
            {
                "A": value,
                "root": supplied_root,
                "occurrences": 1,
                "first_layer": layer,
                "layer_counts": {layer: 1},
            }
        )
        return "new", None

    record_index = record_by_value[value]
    record = ledger[record_index]
    ratio = supplied_root * pow(record["root"], -1, modulus) % modulus
    gcd_minus = math.gcd(ratio - 1, modulus)
    gcd_plus = math.gcd(ratio + 1, modulus)
    status = (
        "global_plus"
        if ratio == 1
        else "global_minus"
        if ratio == modulus - 1
        else "non_global"
    )
    screen = {
        "kind": "duplicate_root_ratio",
        "N": modulus,
        "record_index": record_index,
        "A": value,
        "old_root": record["root"],
        "new_root": supplied_root,
        "ratio": ratio,
        "gcd_minus": gcd_minus,
        "gcd_plus": gcd_plus,
        "status": status,
        "proper": proper(gcd_minus, modulus) or proper(gcd_plus, modulus),
    }
    record["occurrences"] += 1
    record["layer_counts"][layer] = record["layer_counts"].get(layer, 0) + 1
    return "duplicate", screen


def decode(modulus: int, ledger: list[dict[str, Any]]) -> dict[str, Any]:
    active_records = [
        (label, record) for label, record in enumerate(ledger) if record["A"] > 1
    ]
    components = factor_free_components(
        [(label, record["A"]) for label, record in active_records]
    )
    rows = [
        base
        for base, exponents in components
        if any(exponent % 2 for exponent in exponents.values())
    ]
    row_index = {base: index for index, base in enumerate(rows)}
    columns: list[dict[str, Any]] = []
    for label, record in active_records:
        square_part = 1
        bits = 0
        reconstructed = 1
        for base, exponents in components:
            exponent = exponents.get(label, 0)
            if not exponent:
                continue
            reconstructed *= pow(base, exponent)
            square_part *= pow(base, exponent // 2)
            if exponent % 2:
                bits |= 1 << row_index[base]
        assert reconstructed == record["A"]
        parity_product = 1
        for index, block in enumerate(rows):
            if bits >> index & 1:
                parity_product *= block
        assert square_part * square_part * parity_product == record["A"]
        assert pow(record["root"], 2, modulus) == record["A"] % modulus
        assert math.gcd(square_part, modulus) == 1
        lift = record["root"] * pow(square_part, -1, modulus) % modulus
        assert pow(lift, 2, modulus) == parity_product % modulus
        columns.append(
            {
                "local_index": len(columns),
                "record_index": label,
                "A": record["A"],
                "root": record["root"],
                "square_part": square_part,
                "bits": bits,
                "lift": lift,
            }
        )

    pivots: dict[int, tuple[int, int]] = {}
    selected_local_indices: list[int] = []
    kernel: list[int] = []
    for column in columns:
        vector = column["bits"]
        combination = 1 << column["local_index"]
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = (vector, combination)
                selected_local_indices.append(column["local_index"])
                break
            pivot_vector, pivot_combination = pivots[pivot]
            vector ^= pivot_vector
            combination ^= pivot_combination
        if vector == 0:
            kernel.append(combination)

    dependencies: list[dict[str, Any]] = []
    certificates: list[dict[str, Any]] = []
    status_counts = {"global_plus": 0, "global_minus": 0, "non_global": 0}
    for combination in kernel:
        members = [
            column
            for column in columns
            if combination >> column["local_index"] & 1
        ]
        exact_product = math.prod(column["A"] for column in members)
        exact_root = math.isqrt(exact_product)
        assert exact_root * exact_root == exact_product
        supplied_product = math.prod(column["root"] for column in members) % modulus
        normalized = exact_root * pow(supplied_product, -1, modulus) % modulus
        gcd_minus = math.gcd(normalized - 1, modulus)
        gcd_plus = math.gcd(normalized + 1, modulus)
        status = (
            "global_plus"
            if normalized == 1
            else "global_minus"
            if normalized == modulus - 1
            else "non_global"
        )
        status_counts[status] += 1
        summary = {
            "record_indices": [column["record_index"] for column in members],
            "exact_values": [column["A"] for column in members],
            "supplied_roots": [column["root"] for column in members],
            "exact_root_bit_length": exact_root.bit_length(),
            "exact_root_sha256": hashlib.sha256(
                canonical_bytes(exact_root)
            ).hexdigest(),
            "supplied_product": supplied_product,
            "normalized_residue": normalized,
            "gcd_minus": gcd_minus,
            "gcd_plus": gcd_plus,
            "status": status,
        }
        dependencies.append(summary)
        if proper(gcd_minus, modulus) or proper(gcd_plus, modulus):
            certificates.append(
                {
                    "kind": "kernel_dependency",
                    "N": modulus,
                    "record_indices": summary["record_indices"],
                    "exact_values": summary["exact_values"],
                    "supplied_roots": summary["supplied_roots"],
                    "exact_root": exact_root,
                    "supplied_product": supplied_product,
                    "normalized_residue": normalized,
                    "gcd_minus": gcd_minus,
                    "gcd_plus": gcd_plus,
                }
            )

    selected: list[dict[str, Any]] = []
    for local_index in selected_local_indices:
        column = columns[local_index]
        selected.append(
            {
                **column,
                "parity_blocks": [
                    block
                    for index, block in enumerate(rows)
                    if column["bits"] >> index & 1
                ],
            }
        )
    return {
        "components": components,
        "rows": rows,
        "columns": columns,
        "rank": len(pivots),
        "nullity": len(kernel),
        "kernel": kernel,
        "dependencies": dependencies,
        "normalized_root_status": status_counts,
        "certificates": certificates,
        "selected": selected,
    }


def record_sequence(ledger: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "record_index": index,
            "A": record["A"],
            "root": record["root"],
            "occurrences": record["occurrences"],
            "first_layer": record["first_layer"],
            "layer_counts": dict(record["layer_counts"]),
        }
        for index, record in enumerate(ledger)
    ]


def selected_sequence(decoded: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "basis_index": basis_index,
            "record_index": column["record_index"],
            "A": column["A"],
            "parity_blocks": column["parity_blocks"],
            "square_part": column["square_part"],
            "lift": column["lift"],
        }
        for basis_index, column in enumerate(decoded["selected"])
    ]


def snapshot(
    candidates: list[dict[str, Any]],
    ledger: list[dict[str, Any]],
    decoded: dict[str, Any],
) -> dict[str, Any]:
    exact_values = record_sequence(ledger)
    blocks = decoded["rows"]
    selected_columns = selected_sequence(decoded)
    sequences = {
        "candidate": candidates,
        "exact_value": exact_values,
        "block": blocks,
        "selected_column": selected_columns,
    }
    return {
        "hashes": {name: sequence_hash(value) for name, value in sequences.items()},
        "value_only_hashes": {
            "candidate": sequence_hash([item["A"] for item in candidates]),
            "exact_value": sequence_hash([item["A"] for item in exact_values]),
            "block": sequence_hash(blocks),
            "selected_column": sequence_hash(
                [item["A"] for item in selected_columns]
            ),
        },
        "sequences": sequences,
    }


def block_changes(
    old_blocks: list[int], new_component_bases: list[int]
) -> tuple[list[dict[str, Any]], list[int]]:
    splits: list[dict[str, Any]] = []
    preserved: list[int] = []
    for old_block in old_blocks:
        remainder = old_block
        parts: list[list[int]] = []
        for new_block in new_component_bases:
            exponent = 0
            while remainder % new_block == 0:
                remainder //= new_block
                exponent += 1
            if exponent:
                parts.append([new_block, exponent])
        assert remainder == 1
        if parts == [[old_block, 1]]:
            preserved.append(old_block)
        else:
            splits.append({"old_block": old_block, "parts": parts})
    return splits, preserved


def feedback_scan(
    modulus: int,
    level: int,
    ledger: list[dict[str, Any]],
    record_by_value: dict[int, int],
    frozen_decode: dict[str, Any],
) -> dict[str, Any]:
    basis = list(frozen_decode["selected"])
    rows = frozen_decode["rows"]
    candidates: list[dict[str, Any]] = []
    strict_new = 0
    duplicates = 0
    proper_direct_candidates = 0
    duplicate_root_splits = 0
    certificates: list[dict[str, Any]] = []
    supports = [(index,) for index in range(len(basis))]
    supports.extend(
        (left, right)
        for left in range(len(basis))
        for right in range(left + 1, len(basis))
    )
    layer_name = f"level_{level}"
    for support in supports:
        if len(support) == 1:
            selected = basis[support[0]]
            residue = selected["lift"]
        else:
            left, right = (basis[index] for index in support)
            residue = left["lift"] * right["lift"] % modulus
            intersection = left["bits"] & right["bits"]
            while intersection:
                row = intersection.bit_length() - 1
                residue = residue * pow(rows[row], -1, modulus) % modulus
                intersection ^= 1 << row
        inverse = pow(residue, -1, modulus)
        gcd_minus = math.gcd(residue - inverse, modulus)
        gcd_plus = math.gcd(residue + inverse, modulus)
        direct = proper(gcd_minus, modulus) or proper(gcd_plus, modulus)
        proper_direct_candidates += int(direct)
        value = residue * inverse
        assert value > 0 and value % modulus == 1
        disposition, duplicate_screen = offer_record(
            modulus, ledger, record_by_value, value, 1, layer_name
        )
        strict_new += int(disposition == "new")
        duplicates += int(disposition == "duplicate")
        if direct:
            certificates.append(
                {
                    "kind": "feedback_direct_screen",
                    "N": modulus,
                    "level": level,
                    "basis_support": list(support),
                    "record_indices": [basis[index]["record_index"] for index in support],
                    "z": residue,
                    "w": inverse,
                    "A": value,
                    "gcd_minus": gcd_minus,
                    "gcd_plus": gcd_plus,
                }
            )
        if duplicate_screen is not None and duplicate_screen["proper"]:
            duplicate_root_splits += 1
            certificates.append({**duplicate_screen, "level": level})
        candidates.append(
            {
                "attempt_index": len(candidates),
                "basis_support": list(support),
                "record_indices": [basis[index]["record_index"] for index in support],
                "z": residue,
                "w": inverse,
                "A": value,
                "gcd_minus": gcd_minus,
                "gcd_plus": gcd_plus,
                "disposition": disposition,
                "duplicate_ratio_status": (
                    duplicate_screen["status"]
                    if duplicate_screen is not None
                    else None
                ),
            }
        )
    return {
        "candidates": candidates,
        "attempted_subsets": len(candidates),
        "strict_new_exact_values": strict_new,
        "duplicate_exact_values": duplicates,
        "proper_direct_candidates": proper_direct_candidates,
        "duplicate_root_splits": duplicate_root_splits,
        "certificates": certificates,
    }


def analyze_public(modulus: int) -> dict[str, Any]:
    """Analyze one modulus.  No factorization or hidden factors are arguments."""
    bit_length = modulus.bit_length()
    ledger: list[dict[str, Any]] = []
    record_by_value: dict[int, int] = {}
    base_candidates: list[dict[str, Any]] = []
    certificates: list[dict[str, Any]] = []
    base_duplicate_root_splits = 0
    for c in range(2, bit_length + 2):
        unit_gcd = math.gcd(c, modulus)
        if unit_gcd != 1:
            if proper(unit_gcd, modulus):
                certificates.append(
                    {
                        "kind": "base_unit_screen",
                        "N": modulus,
                        "c": c,
                        "gcd": unit_gcd,
                    }
                )
            continue
        inverse = pow(c, -1, modulus)
        value = c * inverse
        disposition, duplicate_screen = offer_record(
            modulus, ledger, record_by_value, value, 1, "base"
        )
        if duplicate_screen is not None and duplicate_screen["proper"]:
            base_duplicate_root_splits += 1
            certificates.append(duplicate_screen)
        base_candidates.append(
            {
                "candidate_index": len(base_candidates),
                "c": c,
                "w": inverse,
                "A": value,
                "root": 1,
                "disposition": disposition,
                "duplicate_ratio_status": (
                    duplicate_screen["status"]
                    if duplicate_screen is not None
                    else None
                ),
            }
        )

    decoded = decode(modulus, ledger)
    certificates.extend(decoded["certificates"])
    base = {
        "attempted_units": len(base_candidates),
        "strict_new_exact_values": len(ledger),
        "duplicate_exact_values": len(base_candidates) - len(ledger),
        "duplicate_root_splits": base_duplicate_root_splits,
        "rows": len(decoded["rows"]),
        "columns": len(decoded["columns"]),
        "rank": decoded["rank"],
        "nullity": decoded["nullity"],
        "normalized_root_status": decoded["normalized_root_status"],
        "dependency_checks": decoded["dependencies"],
        "snapshot": snapshot(base_candidates, ledger, decoded),
    }
    result = {
        "N": modulus,
        "n": bit_length,
        "base": base,
        "levels": [],
        "certificates": list(certificates),
        "success_stage": "base" if certificates else None,
    }
    if certificates:
        return result

    for level in (1, 2):
        old_decode = decoded
        scan = feedback_scan(
            modulus, level, ledger, record_by_value, old_decode
        )
        decoded = decode(modulus, ledger)
        splits, preserved = block_changes(
            old_decode["rows"], [base for base, _ in decoded["components"]]
        )
        level_certificates = scan["certificates"] + decoded["certificates"]
        level_result = {
            "level": level,
            "attempted_subsets": scan["attempted_subsets"],
            "strict_new_exact_values": scan["strict_new_exact_values"],
            "duplicate_exact_values": scan["duplicate_exact_values"],
            "proper_direct_candidates": scan["proper_direct_candidates"],
            "duplicate_root_splits": scan["duplicate_root_splits"],
            "rows": len(decoded["rows"]),
            "columns": len(decoded["columns"]),
            "rank": decoded["rank"],
            "nullity": decoded["nullity"],
            "rank_gain": decoded["rank"] - old_decode["rank"],
            "normalized_root_status": decoded["normalized_root_status"],
            "preserved_old_blocks": preserved,
            "strict_old_block_splits": splits,
            "dependency_checks": decoded["dependencies"],
            "snapshot": snapshot(scan["candidates"], ledger, decoded),
            "certificates": level_certificates,
        }
        result["levels"].append(level_result)
        result["certificates"].extend(level_certificates)
        if level_certificates:
            result["success_stage"] = f"level_{level}"
            return result
    return result


def aggregate_level(results: list[dict[str, Any]], level: int) -> dict[str, int]:
    entries = [result["levels"][level - 1] for result in results]
    return {
        "attempted_subsets": sum(entry["attempted_subsets"] for entry in entries),
        "strict_new_exact_values": sum(
            entry["strict_new_exact_values"] for entry in entries
        ),
        "duplicate_exact_values": sum(
            entry["duplicate_exact_values"] for entry in entries
        ),
        "inputs_with_positive_rank_gain": sum(
            entry["rank_gain"] > 0 for entry in entries
        ),
        "total_rank_gain": sum(entry["rank_gain"] for entry in entries),
        "inputs_with_strict_old_block_splits": sum(
            bool(entry["strict_old_block_splits"]) for entry in entries
        ),
        "total_strictly_split_old_blocks": sum(
            len(entry["strict_old_block_splits"]) for entry in entries
        ),
        "proper_direct_candidates": sum(
            entry["proper_direct_candidates"] for entry in entries
        ),
        "duplicate_root_splits": sum(
            entry["duplicate_root_splits"] for entry in entries
        ),
    }


def first_refinement(
    results: list[dict[str, Any]], level: int
) -> dict[str, Any] | None:
    for result in results:
        entry = result["levels"][level - 1]
        if entry["strict_old_block_splits"]:
            return {
                "N": result["N"],
                "splits": entry["strict_old_block_splits"],
            }
    return None


def add_mismatch(
    mismatches: list[dict[str, Any]], check: str, expected: Any, actual: Any
) -> None:
    if expected != actual:
        mismatches.append({"check": check, "expected": expected, "actual": actual})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    pairs = make_corpus()
    observed_corpus_hash = corpus_hash(pairs)
    mismatches: list[dict[str, Any]] = []
    add_mismatch(
        mismatches,
        "corpus_sha256",
        EXPECTED_CORPUS_SHA256,
        observed_corpus_hash,
    )
    if mismatches:
        payload = {
            "replay_status": "FAIL",
            "first_mismatch": mismatches[0],
            "corpus_sha256": observed_corpus_hash,
            "pairs": pairs,
        }
        with args.output.open("x", encoding="utf-8") as handle:
            json.dump(payload, handle, sort_keys=True, separators=(",", ":"))
            handle.write("\n")
        print(json.dumps(payload["first_mismatch"], sort_keys=True))
        return 1

    public_results = []
    for index, (p, q) in enumerate(pairs):
        modulus = p * q
        result = analyze_public(modulus)
        # The factors enter only after the N-only public result is complete.
        proper_outputs = sorted(
            {
                value
                for certificate in result["certificates"]
                for key, value in certificate.items()
                if key in {"gcd", "gcd_minus", "gcd_plus"}
                and isinstance(value, int)
                and proper(value, modulus)
            }
        )
        result["post_public_classification"] = {
            "p": p,
            "q": q,
            "proper_outputs": proper_outputs,
            "all_outputs_are_true_factors": all(
                value in {p, q} for value in proper_outputs
            ),
        }
        public_results.append(result)
        print(
            json.dumps(
                {
                    "event": "input_complete",
                    "index": index,
                    "N": modulus,
                    "success_stage": result["success_stage"],
                },
                sort_keys=True,
            ),
            flush=True,
        )

    base_positive = [
        result for result in public_results if result["success_stage"] == "base"
    ]
    base_null = [
        result for result in public_results if result["success_stage"] != "base"
    ]
    add_mismatch(mismatches, "base_null_inputs", 63, len(base_null))
    add_mismatch(mismatches, "base_positive_inputs", 1, len(base_positive))
    if base_positive:
        add_mismatch(
            mismatches, "only_base_positive_N", 100160063, base_positive[0]["N"]
        )
        useful = [
            certificate
            for certificate in base_positive[0]["certificates"]
            if certificate["kind"] == "kernel_dependency"
            and (
                proper(certificate["gcd_minus"], base_positive[0]["N"])
                or proper(certificate["gcd_plus"], base_positive[0]["N"])
            )
        ]
        add_mismatch(mismatches, "useful_base_root_count", 1, len(useful))
        if useful:
            add_mismatch(mismatches, "useful_base_exact_root", 10008, useful[0]["exact_root"])
            add_mismatch(mismatches, "useful_base_gcd_minus", 10007, useful[0]["gcd_minus"])
            add_mismatch(mismatches, "useful_base_gcd_plus", 10009, useful[0]["gcd_plus"])

    fully_null = [result for result in base_null if result["success_stage"] is None]
    add_mismatch(mismatches, "null_after_two_levels", 63, len(fully_null))
    add_mismatch(
        mismatches,
        "level_two_only_certificates",
        0,
        sum(result["success_stage"] == "level_2" for result in base_null),
    )

    expected_aggregates = {
        1: {
            "attempted_subsets": 5020,
            "strict_new_exact_values": 315,
            "duplicate_exact_values": 4705,
            "inputs_with_positive_rank_gain": 63,
            "total_rank_gain": 251,
            "inputs_with_strict_old_block_splits": 42,
            "total_strictly_split_old_blocks": 67,
            "proper_direct_candidates": 0,
            "duplicate_root_splits": 0,
        },
        2: {
            "attempted_subsets": 8896,
            "strict_new_exact_values": 310,
            "duplicate_exact_values": 8586,
            "inputs_with_positive_rank_gain": 57,
            "total_rank_gain": 310,
            "inputs_with_strict_old_block_splits": 38,
            "total_strictly_split_old_blocks": 69,
            "proper_direct_candidates": 0,
            "duplicate_root_splits": 0,
        },
    }
    aggregates: dict[int, dict[str, int]] = {}
    if all(len(result["levels"]) == 2 for result in base_null):
        for level in (1, 2):
            aggregates[level] = aggregate_level(base_null, level)
            for key, expected in expected_aggregates[level].items():
                add_mismatch(
                    mismatches,
                    f"level_{level}.{key}",
                    expected,
                    aggregates[level][key],
                )
    else:
        add_mismatch(
            mismatches,
            "two_feedback_levels_for_each_base_null_input",
            63,
            sum(len(result["levels"]) == 2 for result in base_null),
        )

    refinements: dict[int, dict[str, Any] | None] = {}
    if all(len(result["levels"]) == 2 for result in base_null):
        refinements = {
            1: first_refinement(base_null, 1),
            2: first_refinement(base_null, 2),
        }
        add_mismatch(
            mismatches,
            "first_level_1_refinement_N",
            100440259,
            refinements[1]["N"] if refinements[1] else None,
        )
        add_mismatch(
            mismatches,
            "first_level_2_refinement_N",
            100740469,
            refinements[2]["N"] if refinements[2] else None,
        )
        if refinements[1]:
            claimed = {
                (1291243, ((23, 1), (56141, 1))),
                (32284369, ((13, 1), (2483413, 1))),
            }
            actual = {
                (
                    split["old_block"],
                    tuple(tuple(part) for part in split["parts"]),
                )
                for split in refinements[1]["splits"]
            }
            add_mismatch(
                mismatches,
                "claimed_first_level_1_refinements_present",
                True,
                claimed.issubset(actual),
            )
        if refinements[2]:
            claimed = {(11992913, ((23, 1), (521431, 1)))}
            actual = {
                (
                    split["old_block"],
                    tuple(tuple(part) for part in split["parts"]),
                )
                for split in refinements[2]["splits"]
            }
            add_mismatch(
                mismatches,
                "claimed_first_level_2_refinement_present",
                True,
                claimed.issubset(actual),
            )

    stages = []
    for result in public_results:
        stages.append((result["N"], "base", result["base"]["snapshot"]))
        stages.extend(
            (result["N"], f"level_{entry['level']}", entry["snapshot"])
            for entry in result["levels"]
        )
    aggregate_sequence_hashes = {}
    aggregate_value_only_hashes = {}
    for name in ("candidate", "exact_value", "block", "selected_column"):
        aggregate_sequence_hashes[name] = sequence_hash(
            [
                [modulus, stage, snap["sequences"][name]]
                for modulus, stage, snap in stages
            ]
        )
        aggregate_value_only_hashes[name] = sequence_hash(
            [
                [modulus, stage, snap["value_only_hashes"][name]]
                for modulus, stage, snap in stages
            ]
        )

    payload = {
        "schema": "F165-R02-V2-blind-reconstruction-1",
        "replay_status": "FAIL" if mismatches else "STATED_FINITE_CLAIMS_MATCH",
        "final_verdict": (
            "FAIL"
            if mismatches
            else "PENDING_REGISTERED_SEQUENCE_HASH_COMPARISON_AND_PROOF_AUDIT"
        ),
        "first_mismatch": mismatches[0] if mismatches else None,
        "all_mismatches": mismatches,
        "sequence_hash_comparison": {
            "status": "PENDING_EXTERNAL_REGISTERED_REFERENCE",
            "reason": (
                "The blind statement requires sequence-hash reproduction but "
                "does not publish reference sequence digests or their encoding."
            ),
            "encoding": (
                "typed recursive framing: N/T/F; I,S,L,D tags; every length is "
                "unsigned eight-byte big-endian; dictionary keys sort lexically"
            ),
        },
        "corpus_sha256": observed_corpus_hash,
        "pairs": pairs,
        "aggregates": aggregates,
        "first_refinements": refinements,
        "aggregate_sequence_hashes": aggregate_sequence_hashes,
        "aggregate_value_only_hashes": aggregate_value_only_hashes,
        "results": public_results,
    }
    with args.output.open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, sort_keys=True, separators=(",", ":"))
        handle.write("\n")
    print(
        json.dumps(
            {
                "event": "replay_complete",
                "replay_status": payload["replay_status"],
                "final_verdict": payload["final_verdict"],
                "first_mismatch": payload["first_mismatch"],
                "aggregate_sequence_hashes": aggregate_sequence_hashes,
            },
            sort_keys=True,
        ),
        flush=True,
    )
    return int(bool(mismatches))


if __name__ == "__main__":
    raise SystemExit(main())
