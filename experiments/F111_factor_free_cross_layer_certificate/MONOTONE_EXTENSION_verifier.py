#!/usr/bin/env python3
"""Named factor-free verifier for the full F111 monotone extension."""

from __future__ import annotations

import argparse
import ast
from collections import Counter
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import time
import traceback


EXPECTED_CERTIFICATE_SHA256 = "735a8535eb8cd4e8bc5e1c0fbc71d78b3acd79b3e6efa1f865d9084dea67cf6b"
EXPECTED_PUBLIC_BASIS_SHA256 = "5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b"
EXPECTED_LAYER_VERIFIER_SHA256 = "7c1a12c6489f229e9ea146374b198bd683fbebe6228dcec0c427d2310b394d4c"
EXPECTED_LAYER_OUTPUT_SHA256 = "6b9c66ca97c47d1307212db9ba5fa299df3c66c3312af6ee8f110c9d3e8e52a8"


class VerificationFailure(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationFailure(message)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_layer_module(path: Path):
    specification = importlib.util.spec_from_file_location("monotone_pinned_layer", path)
    require(
        specification is not None and specification.loader is not None,
        "cannot load pinned factor-free layer module",
    )
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def audit(
    certificate_path: Path,
    public_basis_path: Path,
    layer_verifier_path: Path,
    layer_output_path: Path,
) -> dict[str, object]:
    started = time.monotonic()
    require(sha256_file(certificate_path) == EXPECTED_CERTIFICATE_SHA256, "certificate hash changed")
    require(sha256_file(public_basis_path) == EXPECTED_PUBLIC_BASIS_SHA256, "public basis hash changed")
    require(
        sha256_file(layer_verifier_path) == EXPECTED_LAYER_VERIFIER_SHA256,
        "factor-free layer verifier hash changed",
    )
    require(
        sha256_file(layer_output_path) == EXPECTED_LAYER_OUTPUT_SHA256,
        "prefix layer output hash changed",
    )
    layer = load_layer_module(layer_verifier_path)
    certificate = json.loads(certificate_path.read_text())
    modulus = int(certificate["N"])
    n = int(certificate["n"])
    bound = int(certificate["bound"])
    prefix_stop_for_audit_only = int(certificate["source_stop_relation_count"])
    require(n == modulus.bit_length(), "certificate bit length is wrong")
    require(bound == n * n, "certificate bound is wrong")

    phase = time.monotonic()
    trial_distribution = Counter(math.gcd(trial, modulus) for trial in range(2, bound + 1))
    require(trial_distribution == Counter({1: bound - 1}), "trial screen found a divisor")

    records: list[dict[str, object]] = []
    endpoints: list[int] = []
    seen_residues: set[int] = set()
    attempted = 0
    duplicate_residues = 0
    direct_distribution: Counter[int] = Counter()
    proper_direct_gcds = []

    def retain(residue: int, provenance: dict[str, object]) -> None:
        nonlocal attempted, duplicate_residues
        attempted += 1
        if residue in seen_residues:
            duplicate_residues += 1
            return
        require(0 < residue < modulus, "retained residue is not canonical")
        residue_gcd = math.gcd(residue, modulus)
        if 1 < residue_gcd < modulus:
            proper_direct_gcds.append(
                {"channel": "noninvertible_residue", "gcd": residue_gcd, "provenance": provenance}
            )
            return
        require(residue_gcd == 1, "retained residue equals zero modulo N")
        seen_residues.add(residue)
        inverse = pow(residue, -1, modulus)
        for sign, difference in (("minus", residue - inverse), ("plus", residue + inverse)):
            divisor = math.gcd(difference, modulus)
            direct_distribution[divisor] += 1
            if 1 < divisor < modulus:
                proper_direct_gcds.append(
                    {
                        "channel": f"endpoint_{sign}",
                        "gcd": divisor,
                        "c": residue,
                        "w": inverse,
                        "provenance": provenance,
                    }
                )
        record = {
            "source_index_zero_based": len(records),
            "c": residue,
            "w": inverse,
            "P": residue * inverse,
            "provenance": provenance,
        }
        require(record["P"] % modulus == 1, "relation value is not one modulo N")
        records.append(record)
        endpoints.extend((residue, inverse))

    for seed in range(2, n + 1):
        retain(seed, {"kind": "initial_seed", "seed": seed})
    require(not proper_direct_gcds, "initial seed phase found a direct factor")
    initial_record_count = len(records)
    basis, basis_stats = layer.initial_gcd_basis(endpoints)
    incidence: list[list[int]] = [[] for _ in endpoints]
    for block_index, (_, signature) in enumerate(basis):
        for endpoint_index in signature:
            incidence[endpoint_index].append(block_index)
    frozen_pairs = []
    for relation_index in range(initial_record_count):
        support = sorted(
            basis[block_index][0]
            for block_index in set(
                incidence[2 * relation_index] + incidence[2 * relation_index + 1]
            )
        )
        require(bool(support), "initial relation has empty public support")
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
    frozen_record_count = len(records)

    appended_pair_stats = []
    for pair_index, (left, right) in enumerate(((2, 3), (2, 4))):
        attempts_before = attempted
        records_before = len(records)
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
        appended_pair_stats.append(
            {
                "pair": [left, right],
                "attempts": attempted - attempts_before,
                "new_retained_records": len(records) - records_before,
            }
        )
    source_seconds = time.monotonic() - phase
    require(not proper_direct_gcds, "full source found an earlier proper direct gcd")
    require(attempted - duplicate_residues == len(records), "residue dedup accounting failed")
    expected_positions = (n - 1) + 2 * (n - 1) * (bound + 1) + 4 * (bound + 1)
    require(attempted == expected_positions, "full source position count is wrong")

    full_record_digest = hashlib.sha256()
    for record in records:
        layer.feed_digest(full_record_digest, record)

    prefix_output = json.loads(layer_output_path.read_text())
    require(prefix_stop_for_audit_only < len(records), "declared prefix is not proper")
    prefix_records = records[:prefix_stop_for_audit_only]
    prefix_digest = hashlib.sha256()
    for record in prefix_records:
        layer.feed_digest(prefix_digest, record)
    require(
        prefix_digest.hexdigest()
        == prefix_output["source_regeneration"]["retained_record_stream_sha256"],
        "full source does not retain the exact declared prefix",
    )
    prefix_dedup = layer.exact_value_dedup(prefix_records)
    prefix_unique_records = prefix_dedup.pop("records")
    require(
        prefix_dedup == prefix_output["exact_value_dedup"]["union"],
        "full source prefix exact-value dedup differs",
    )

    full_dedup = layer.exact_value_dedup(records)
    unique_records = full_dedup.pop("records")
    require(
        unique_records[: len(prefix_unique_records)] == prefix_unique_records,
        "first-occurrence exact-value dedup did not preserve prefix coordinates",
    )
    unique_column_digest = hashlib.sha256()
    for record in unique_records:
        layer.feed_digest(unique_column_digest, record)
    full_dedup["unique_column_stream_sha256"] = unique_column_digest.hexdigest()
    phase = time.monotonic()
    row_masks, refinement_stats = layer.factor_free_union_rows(unique_records)
    refinement_seconds = time.monotonic() - phase
    phase = time.monotonic()
    system = layer.analyze_system(
        "full_fixed_monotone_extension", unique_records, row_masks, modulus
    )
    kernel_and_root_seconds = time.monotonic() - phase
    system.pop("kernel_vectors")
    non_global_basis = [
        entry for entry in system["kernel"]["basis"] if entry["root_class"] == "non_global"
    ]
    require(non_global_basis, "complete full-source kernel basis has no useful root")
    selected_root = int(non_global_basis[0]["root_mod_N"])
    minus = math.gcd(selected_root - 1, modulus)
    plus = math.gcd(selected_root + 1, modulus)
    require(1 < minus < modulus and 1 < plus < modulus, "non-global root gcd is not proper")
    require(minus * plus == modulus, "terminal gcds do not split N")

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
    require(
        not calls
        & {"factor", "factorint", "is_prime", "isprime", "prime_factors", "prime_range"},
        "named verifier calls factorization or primality machinery",
    )
    certificate_keys = {
        node.slice.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
        and node.value.id == "certificate"
        and isinstance(node.slice, ast.Constant)
        and isinstance(node.slice.value, str)
    }
    require(
        certificate_keys == {"N", "n", "bound", "source_stop_relation_count"},
        "named verifier accesses an undeclared certificate field",
    )

    max_relation_bits = max(int(record["P"]).bit_length() for record in unique_records)
    max_basis_product_bits = max(
        entry["exact_product_bit_length"] for entry in system["kernel"]["basis"]
    )
    return {
        "status": "PASS",
        "verdict": "PASS",
        "role": "named factor-free complete-kernel verification of the full fixed monotone extension",
        "input_hashes": {
            "CERTIFICATE.json": sha256_file(certificate_path),
            "public_factorization_free_replay.py": sha256_file(public_basis_path),
            "LAYER_INTERACTION_independent_verifier.py": sha256_file(layer_verifier_path),
            "LAYER_INTERACTION_OUTPUT.json": sha256_file(layer_output_path),
        },
        "input_policy": {
            "known_factors_used": False,
            "factorization_calls": False,
            "primality_calls": False,
            "dependency_indices_read": False,
            "generation_fields": ["N", "n", "bound"],
            "prefix_stop_used_only_for_post_generation_audit": True,
            "prefix_stop_used_for_generation": False,
        },
        "static_source_audit": {
            "certificate_keys_read": sorted(certificate_keys),
            "prohibited_factorization_or_primality_calls_found": sorted(
                calls
                & {"factor", "factorint", "is_prime", "isprime", "prime_factors", "prime_range"}
            ),
        },
        "N": modulus,
        "n": n,
        "bound": bound,
        "trial_screen": {
            "count": sum(trial_distribution.values()),
            "gcd_distribution": dict(sorted(trial_distribution.items())),
            "proper_gcd_count": sum(
                count for divisor, count in trial_distribution.items() if 1 < divisor < modulus
            ),
        },
        "source": {
            "expected_position_formula": "(n-1)+2(n-1)(n^2+1)+4(n^2+1)",
            "scheduled_positions": attempted,
            "retained_records": len(records),
            "duplicate_residues": duplicate_residues,
            "initial_records": initial_record_count,
            "initial_basis_blocks": len(basis),
            "initial_basis_stats": basis_stats,
            "frozen_pair_count": len(frozen_pairs),
            "frozen_pairs": [list(pair) for pair in frozen_pairs],
            "frozen_record_count": frozen_record_count,
            "appended_pair_stats": appended_pair_stats,
            "direct_screen_count": sum(direct_distribution.values()),
            "direct_screen_distribution": dict(sorted(direct_distribution.items())),
            "proper_direct_gcd_count": len(proper_direct_gcds),
            "retained_record_stream_sha256": full_record_digest.hexdigest(),
            "seconds": source_seconds,
        },
        "prefix_audit": {
            "declared_stop": prefix_stop_for_audit_only,
            "exact_relation_stream_prefix": True,
            "retained_record_stream_sha256": prefix_digest.hexdigest(),
            "exact_value_dedup": prefix_dedup,
            "prefix_column_count": len(prefix_unique_records),
            "full_column_count": len(unique_records),
            "new_columns_after_prefix": len(unique_records) - len(prefix_unique_records),
            "prefix_columns_preserved_as_initial_coordinate_block": True,
            "useful_dependency_existence_monotone": True,
            "kernel_basis_vectors_themselves_monotone": False,
        },
        "full_exact_value_dedup": full_dedup,
        "factor_free_refinement": refinement_stats,
        "complete_system": system,
        "terminal_extraction": {
            "tested_basis_root_count": system["kernel"]["basis_size"],
            "non_global_basis_root_count": len(non_global_basis),
            "selected_computed_root_mod_N": selected_root,
            "root_squared_mod_N": pow(selected_root, 2, modulus),
            "gcd_root_minus_one_N": minus,
            "gcd_root_plus_one_N": plus,
            "gcd_product": minus * plus,
        },
        "bit_size_audit": {
            "maximum_relation_value_bit_length": max_relation_bits,
            "maximum_tested_basis_product_bit_length": max_basis_product_bits,
            "general_relation_value_bound": "at most 2n bits",
            "general_dependency_product_bound": "O(n^4) bits because m=O(n^3)",
            "complete_basis_count_bound": "at most m=O(n^3)",
        },
        "timings": {
            "source_seconds": source_seconds,
            "factor_free_refinement_seconds": refinement_seconds,
            "kernel_and_all_basis_root_tests_seconds": kernel_and_root_seconds,
            "total_seconds": time.monotonic() - started,
        },
        "complexity_boundary": {
            "uniform_N_input_algorithm": True,
            "source_positions_polynomial": True,
            "integer_sizes_polynomial": True,
            "gcd_free_decoder_polynomial_bit_time": True,
            "all_basis_root_tests_polynomial_bit_time": True,
            "success_proved_for_this_N_only": True,
            "all_input_success_theorem": False,
            "fixed_pair_schedule_historically_post_selected": True,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--public-basis-source", type=Path, required=True)
    parser.add_argument("--layer-verifier", type=Path, required=True)
    parser.add_argument("--layer-output", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        output = audit(
            args.certificate.resolve(),
            args.public_basis_source.resolve(),
            args.layer_verifier.resolve(),
            args.layer_output.resolve(),
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
