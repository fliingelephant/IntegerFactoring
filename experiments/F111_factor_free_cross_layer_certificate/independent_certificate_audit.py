#!/usr/bin/env python3
"""Independent hostile audit of the F111 public index certificate."""

from __future__ import annotations

import argparse
import ast
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import re
import time
import traceback


class AuditFailure(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AuditFailure(message)


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


def independent_gcd_basis(
    endpoints: list[int],
) -> tuple[list[tuple[int, dict[int, int]]], dict[str, int]]:
    """Reimplement the pinned LIFO gcd/perfect-power basis algorithm."""
    work = [
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

    while work:
        value, signature = work.pop()
        if value == 1:
            continue
        root, exponent = primitive_power(value)
        if exponent > 1:
            value = root
            signature = {
                endpoint: multiplicity * exponent
                for endpoint, multiplicity in signature.items()
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
                for endpoint, multiplicity in old_signature.items():
                    merged[endpoint] = merged.get(endpoint, 0) + multiplicity
                work.append((value, merged))
                stats["identical_merges"] += 1
                break
            work.extend(
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

    basis.sort(key=lambda entry: entry[0])
    reconstructed = [1] * len(endpoints)
    for position, (value, signature) in enumerate(basis):
        require(primitive_power(value)[1] == 1, "basis block remains a perfect power")
        for old_value, _ in basis[:position]:
            require(math.gcd(value, old_value) == 1, "basis blocks are not coprime")
        for endpoint, multiplicity in signature.items():
            reconstructed[endpoint] *= value**multiplicity
    require(reconstructed == endpoints, "basis signatures do not reconstruct endpoints")
    return basis, stats


def independent_relation_columns(
    basis: list[tuple[int, dict[int, int]]], relation_count: int
) -> list[dict[int, int]]:
    incidence: list[list[tuple[int, int]]] = [
        [] for _ in range(2 * relation_count)
    ]
    for block_index, (_, signature) in enumerate(basis):
        for endpoint, multiplicity in signature.items():
            incidence[endpoint].append((block_index, multiplicity))

    columns: list[dict[int, int]] = []
    for relation_index in range(relation_count):
        column: dict[int, int] = {}
        for endpoint in (2 * relation_index, 2 * relation_index + 1):
            for block_index, multiplicity in incidence[endpoint]:
                column[block_index] = column.get(block_index, 0) + multiplicity
        columns.append(column)
    return columns


def regenerate_public_source(
    modulus: int, n: int, bound: int, stop: int
) -> dict[str, object]:
    """Regenerate the ordered source from public scalar inputs only."""
    trial_digest = hashlib.sha256()
    trial_distribution: Counter[int] = Counter()
    for trial in range(2, bound + 1):
        divisor = math.gcd(trial, modulus)
        trial_distribution[divisor] += 1
        feed_digest(trial_digest, [trial, divisor])
    require(trial_distribution == Counter({1: bound - 1}), "trial screen found a divisor")

    records: list[dict[str, object]] = []
    endpoints: list[int] = []
    seen: set[int] = set()
    attempted = 0
    repeated = 0
    proper_direct_gcds = 0
    direct_distribution: Counter[int] = Counter()
    nonunit_direct_screens = []
    attempt_digest = hashlib.sha256()
    record_digest = hashlib.sha256()
    direct_digest = hashlib.sha256()

    def retain(residue: int, provenance: dict[str, object]) -> None:
        nonlocal attempted, repeated, proper_direct_gcds
        attempted += 1
        duplicate = residue in seen
        feed_digest(
            attempt_digest,
            {
                "attempt_one_based": attempted,
                "c": residue,
                "duplicate": duplicate,
                "provenance": provenance,
            },
        )
        if duplicate:
            repeated += 1
            return
        require(0 < residue < modulus, "retained residue is not canonical and invertible")
        seen.add(residue)
        inverse = pow(residue, -1, modulus)
        require(0 < inverse < modulus, "inverse is not canonical")
        product = residue * inverse
        require(product % modulus == 1, "retained relation is not congruent to one")
        record_index = len(records)
        for sign, difference in (("minus", residue - inverse), ("plus", residue + inverse)):
            divisor = math.gcd(difference, modulus)
            direct_distribution[divisor] += 1
            proper_direct_gcds += int(1 < divisor < modulus)
            if divisor != 1:
                nonunit_direct_screens.append(
                    {
                        "record_index_zero_based": record_index,
                        "c": residue,
                        "w": inverse,
                        "sign": sign,
                        "difference": difference,
                        "gcd": divisor,
                        "provenance": provenance,
                    }
                )
            feed_digest(
                direct_digest,
                [record_index, residue, inverse, sign, difference, divisor],
            )
        record = {
            "c": residue,
            "w": inverse,
            "P": product,
            "provenance": provenance,
        }
        records.append(record)
        endpoints.extend((residue, inverse))
        feed_digest(record_digest, [record_index, record])

    for seed in range(2, n + 1):
        retain(seed, {"kind": "initial_seed", "seed": seed})

    initial_endpoint_count = len(endpoints)
    basis, basis_stats = independent_gcd_basis(endpoints)
    columns = independent_relation_columns(basis, len(records))
    frozen_pairs: list[tuple[int, int]] = []
    for column in columns:
        support = sorted(basis[block_index][0] for block_index in column)
        require(bool(support), "seed relation has empty basis support")
        frozen_pairs.append(
            (support[0], 1) if len(support) == 1 else (support[0], support[1])
        )

    for pair_index, (left, right) in enumerate(frozen_pairs):
        for exponent in range(bound + 1):
            retain(
                pow(left, exponent, modulus) * right % modulus,
                {
                    "kind": "frozen_seed_basis_pair",
                    "pair_index_zero_based": pair_index,
                    "u": left,
                    "v": right,
                    "exponent": exponent,
                    "orientation": "u_power_times_v",
                },
            )
            retain(
                left * pow(right, exponent, modulus) % modulus,
                {
                    "kind": "frozen_seed_basis_pair",
                    "pair_index_zero_based": pair_index,
                    "u": left,
                    "v": right,
                    "exponent": exponent,
                    "orientation": "u_times_v_power",
                },
            )
    frozen_relation_count = len(records)

    appended_pair_stats = []
    for pair_index, (left, right) in enumerate(((2, 3), (2, 4))):
        attempts_before = attempted
        records_before = len(records)
        stopped = False
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
                    stopped = True
                    break
            if stopped:
                break
        appended_pair_stats.append(
            {
                "pair": [left, right],
                "attempts": attempted - attempts_before,
                "new_relations": len(records) - records_before,
                "reached_stop": stopped,
            }
        )
        if stopped:
            break

    require(len(records) == stop, "public source did not reach the certificate stop")
    require(proper_direct_gcds == 0, "a direct screen exposed an undeclared proper gcd")
    require(attempted - repeated == len(records), "dedup accounting failed")
    require(sum(direct_distribution.values()) == 2 * len(records), "direct screen count failed")

    basis_payload = [
        {
            "value": value,
            "signature": sorted([endpoint, multiplicity] for endpoint, multiplicity in signature.items()),
        }
        for value, signature in basis
    ]
    basis_digest = hashlib.sha256(
        json.dumps(basis_payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return {
        "records": records,
        "n": n,
        "bound": bound,
        "trial_screen_count": bound - 1,
        "trial_screen_distribution": dict(sorted(trial_distribution.items())),
        "trial_screen_sha256": trial_digest.hexdigest(),
        "initial_endpoint_count": initial_endpoint_count,
        "initial_basis": basis_payload,
        "initial_basis_sha256": basis_digest,
        "initial_basis_stats": basis_stats,
        "frozen_pairs": frozen_pairs,
        "frozen_relation_count": frozen_relation_count,
        "source_stop_relation_count": len(records),
        "candidate_residues_attempted": attempted,
        "duplicate_residues": repeated,
        "attempt_stream_sha256": attempt_digest.hexdigest(),
        "retained_record_stream_sha256": record_digest.hexdigest(),
        "direct_gcd_screens": sum(direct_distribution.values()),
        "direct_screen_distribution": dict(sorted(direct_distribution.items())),
        "nonunit_direct_screens": nonunit_direct_screens,
        "direct_screen_stream_sha256": direct_digest.hexdigest(),
        "proper_direct_gcds": proper_direct_gcds,
        "appended_pair_stats": appended_pair_stats,
    }


def source_static_audit(candidate_source: Path, public_source: Path) -> dict[str, object]:
    blocked_imports = {
        "cypari2",
        "ecm",
        "factor",
        "gmpy2",
        "httpx",
        "pari",
        "requests",
        "sage",
        "socket",
        "subprocess",
        "sympy",
        "urllib",
    }
    blocked_calls = {
        "ecm",
        "factor",
        "factor_integer",
        "factorint",
        "is_prime",
        "isprime",
        "next_prime",
        "nextprime",
        "prime_divisors",
        "prime_factors",
        "prime_range",
        "qsieve",
    }
    selector_calls = {"binary_kernel_basis", "decode_relations", "parity_coprime_basis"}
    results: dict[str, object] = {}
    for label, path in (("candidate_replay", candidate_source), ("pinned_public_basis", public_source)):
        text = path.read_text()
        tree = ast.parse(text, filename=str(path))
        imports = set()
        calls = set()
        read_sites = []
        dynamic_import_sites = []
        dynamic_import_targets = []
        sha256_file_arguments = []
        public_module_calls = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module.split(".")[0])
            elif isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    calls.add(node.func.id)
                    if node.func.id == "sha256_file":
                        sha256_file_arguments.extend(ast.unparse(argument) for argument in node.args)
                elif isinstance(node.func, ast.Attribute):
                    calls.add(node.func.attr)
                    if isinstance(node.func.value, ast.Name) and node.func.value.id == "PUBLIC":
                        public_module_calls.append(node.func.attr)
                    if node.func.attr in {"open", "read_bytes", "read_text"}:
                        read_sites.append(
                            {"method": node.func.attr, "receiver": ast.unparse(node.func.value)}
                        )
                    if node.func.attr in {"exec_module", "spec_from_file_location"}:
                        dynamic_import_sites.append(node.func.attr)
                    if node.func.attr == "spec_from_file_location" and len(node.args) >= 2:
                        dynamic_import_targets.append(ast.unparse(node.args[1]))
        forbidden_imports = sorted(imports & blocked_imports)
        forbidden_calls = sorted(calls & blocked_calls)
        require(not forbidden_imports, f"{label} imports forbidden factor/network machinery")
        require(not forbidden_calls, f"{label} calls forbidden factor/primality machinery")
        require("/F109" not in text and "/F110" not in text, f"{label} contains a hidden experiment path")
        results[label] = {
            "sha256": sha256_file(path),
            "imports": sorted(imports),
            "forbidden_imports": forbidden_imports,
            "forbidden_factor_or_primality_calls": forbidden_calls,
            "file_read_sites": read_sites,
            "dynamic_import_sites": sorted(dynamic_import_sites),
            "dynamic_import_targets": sorted(dynamic_import_targets),
            "sha256_file_arguments": sorted(sha256_file_arguments),
            "public_module_calls": sorted(public_module_calls),
            "single_letter_hidden_factor_names": sorted(
                {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)} & {"p", "q"}
            ),
            "selector_calls": sorted(calls & selector_calls),
        }

    candidate_result = results["candidate_replay"]
    require(
        candidate_result["selector_calls"] == [],
        "candidate replay invokes a dependency selector",
    )
    require(
        sorted(
            candidate_result["file_read_sites"],
            key=lambda site: (site["method"], site["receiver"]),
        )
        == [
            {"method": "read_bytes", "receiver": "path"},
            {"method": "read_text", "receiver": "CERTIFICATE"},
        ],
        "candidate replay has an unexpected file-read site",
    )
    require(
        candidate_result["dynamic_import_sites"] == ["exec_module", "spec_from_file_location"],
        "candidate replay dynamic import surface changed",
    )
    require(
        candidate_result["dynamic_import_targets"] == ["PUBLIC_BASIS_SOURCE"],
        "candidate replay imports an unpinned target",
    )
    require(
        Counter(candidate_result["sha256_file_arguments"])
        == Counter({"PUBLIC_BASIS_SOURCE": 2, "CERTIFICATE": 1}),
        "candidate replay hashes an unauthorized file",
    )
    require(
        candidate_result["public_module_calls"] == ["gcd_free_basis", "relation_columns"],
        "candidate replay calls an undeclared public-module routine",
    )
    require(
        results["pinned_public_basis"]["file_read_sites"] == [],
        "pinned public basis source reads a file",
    )
    return results


def audit(candidate_dir: Path, public_source: Path) -> dict[str, object]:
    started = time.monotonic()
    candidate_names = [
        "DESIGN.md",
        "FAILED_RUNS.md",
        "run_with_timeout.py",
        "replay_public_certificate.py",
        "RUN_MANIFEST.md",
        "CERTIFICATE.json",
        "OUTPUT.json",
        "RUN.log",
        "RESULT.md",
    ]
    candidate_paths = {name: candidate_dir / name for name in candidate_names}
    require(all(path.is_file() for path in candidate_paths.values()), "candidate artifact is missing")
    require(public_source.is_file(), "pinned public basis source is missing")

    candidate_hashes = {name: sha256_file(path) for name, path in candidate_paths.items()}
    public_hash = sha256_file(public_source)
    require(
        public_hash == "5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b",
        "pinned public basis source hash changed",
    )

    manifest_text = candidate_paths["RUN_MANIFEST.md"].read_text()
    manifest_pins = dict(re.findall(r"^([0-9a-f]{64})  (.+)$", manifest_text, re.MULTILINE))
    expected_manifest_pins = {
        candidate_hashes["DESIGN.md"]: "DESIGN.md",
        candidate_hashes["CERTIFICATE.json"]: "CERTIFICATE.json",
        candidate_hashes["replay_public_certificate.py"]: "replay_public_certificate.py",
        candidate_hashes["run_with_timeout.py"]: "run_with_timeout.py",
        candidate_hashes["OUTPUT.json"]: "OUTPUT.json",
        candidate_hashes["RUN.log"]: "RUN.log",
        candidate_hashes["FAILED_RUNS.md"]: "FAILED_RUNS.md",
        public_hash: "../F98_multiseed_presentation_closure_kill/public_factorization_free_replay.py",
    }
    require(manifest_pins == expected_manifest_pins, "candidate run-manifest pins do not match files")
    require(
        not list(candidate_dir.glob("RUN_FAILED_*")),
        "candidate failed-run file exists but is not declared",
    )

    certificate = json.loads(candidate_paths["CERTIFICATE.json"].read_text())
    expected_certificate_keys = {
        "N",
        "bound",
        "dependency_relation_indices_zero_based",
        "dependency_support",
        "expected_gcd_root_minus_one_N",
        "expected_gcd_root_plus_one_N",
        "expected_root_mod_N",
        "first_successful_appended_pair",
        "n",
        "provenance_kind_counts",
        "source_stop_relation_count",
    }
    require(set(certificate) == expected_certificate_keys, "certificate schema changed")
    modulus = int(certificate["N"])
    n = int(certificate["n"])
    bound = int(certificate["bound"])
    stop = int(certificate["source_stop_relation_count"])
    require(n == modulus.bit_length(), "certificate bit length is wrong")
    require(bound == n * n, "certificate bound is wrong")

    regenerated = regenerate_public_source(modulus, n, bound, stop)
    records = regenerated.pop("records")

    indices = certificate["dependency_relation_indices_zero_based"]
    require(all(type(index) is int for index in indices), "certificate index is not an integer")
    require(indices == sorted(indices), "certificate indices are not in canonical order")
    require(len(indices) == 363, "certificate does not contain 363 indices")
    require(len(indices) == certificate["dependency_support"], "support field is wrong")
    require(len(indices) == len(set(indices)), "certificate repeats an index")
    require(indices[0] >= 0 and indices[-1] < len(records), "certificate index is out of range")
    require(indices[-1] == stop - 1, "certificate does not anchor the public stop record")

    selected = [records[index] for index in indices]
    selected_product = math.prod(int(record["P"]) for record in selected)
    exact_square_root = math.isqrt(selected_product)
    require(exact_square_root * exact_square_root == selected_product, "selected product is not square")
    root_modulus = exact_square_root % modulus
    root_minus = math.gcd(exact_square_root - 1, modulus)
    root_plus = math.gcd(exact_square_root + 1, modulus)
    require(selected_product % modulus == 1, "selected product is not one modulo N")
    require(pow(root_modulus, 2, modulus) == 1, "reported root is not a square root of one")
    require(root_modulus not in (1, modulus - 1), "root is global rather than mixed-sign")
    require(root_modulus == certificate["expected_root_mod_N"], "certificate root residue is wrong")
    require(
        root_minus == certificate["expected_gcd_root_minus_one_N"],
        "certificate minus gcd is wrong",
    )
    require(
        root_plus == certificate["expected_gcd_root_plus_one_N"],
        "certificate plus gcd is wrong",
    )
    require(1 < root_minus < modulus and 1 < root_plus < modulus, "gcd is not proper")
    require(root_minus * root_plus == modulus, "two extraction gcds do not split N")

    provenance_counts = Counter(record["provenance"]["kind"] for record in selected)
    require(
        dict(sorted(provenance_counts.items())) == certificate["provenance_kind_counts"],
        "certificate layer split is wrong",
    )
    appended_pairs = Counter(
        (record["provenance"]["u"], record["provenance"]["v"])
        for record in selected
        if record["provenance"]["kind"] == "nonadaptive_seed_pair"
    )
    declared_success_pair = tuple(certificate["first_successful_appended_pair"])
    require(
        appended_pairs == Counter({declared_success_pair: 36}),
        "selected appended relations do not all come from the declared pair",
    )

    selected_index_digest = hashlib.sha256()
    selected_record_digest = hashlib.sha256()
    for index, record in zip(indices, selected, strict=True):
        feed_digest(selected_index_digest, index)
        feed_digest(selected_record_digest, [index, record])

    candidate_output = json.loads(candidate_paths["OUTPUT.json"].read_text())
    expected_output_fields = {
        "N": modulus,
        "n": n,
        "bound": bound,
        "trial_screen_null": True,
        "initial_endpoint_count": regenerated["initial_endpoint_count"],
        "initial_basis_blocks": len(regenerated["initial_basis"]),
        "initial_basis_stats": regenerated["initial_basis_stats"],
        "frozen_pair_count": len(regenerated["frozen_pairs"]),
        "frozen_pairs": [list(pair) for pair in regenerated["frozen_pairs"]],
        "frozen_relation_count": regenerated["frozen_relation_count"],
        "source_stop_relation_count": regenerated["source_stop_relation_count"],
        "candidate_residues_attempted": regenerated["candidate_residues_attempted"],
        "duplicate_residues": regenerated["duplicate_residues"],
        "direct_gcd_screens": regenerated["direct_gcd_screens"],
        "proper_direct_gcds": regenerated["proper_direct_gcds"],
        "dependency_support": len(indices),
        "dependency_provenance_kind_counts": dict(sorted(provenance_counts.items())),
        "selected_exact_product_bit_length": selected_product.bit_length(),
        "selected_exact_product_is_square": True,
        "root_mod_N": root_modulus,
        "gcd_root_minus_one_N": root_minus,
        "gcd_root_plus_one_N": root_plus,
        "status": "PASS",
        "forbidden_operations_used": [],
    }
    for field, expected in expected_output_fields.items():
        require(candidate_output.get(field) == expected, f"candidate OUTPUT field {field} is wrong")
    require(candidate_output.get("input_hashes") == {
        "CERTIFICATE.json": candidate_hashes["CERTIFICATE.json"],
        "experiments/F98_multiseed_presentation_closure_kill/public_factorization_free_replay.py": public_hash,
    }, "candidate OUTPUT input hashes are wrong")
    require(candidate_output.get("elapsed_seconds", 0) > 0, "candidate elapsed time is invalid")

    run_log = candidate_paths["RUN.log"].read_text()
    require("returncode=0" in run_log, "candidate run log did not exit zero")
    require("timeout_seconds=120" in run_log, "candidate run timeout changed")
    logged_stdout = run_log.split("stdout:\n", 1)[1].split("\nstderr:\n", 1)[0]
    require(json.loads(logged_stdout) == candidate_output, "candidate log stdout differs from OUTPUT")

    design_normalized = " ".join(candidate_paths["DESIGN.md"].read_text().lower().split())
    result_normalized = " ".join(candidate_paths["RESULT.md"].read_text().lower().split())
    require(
        "index list is a certificate, not a selector" in design_normalized,
        "DESIGN does not state the certificate-selector boundary",
    )
    require("indices are advice" in result_normalized, "RESULT does not disclose index advice")
    require(
        "do not provide an all-input selector" in result_normalized,
        "RESULT overstates the certificate as a selector",
    )
    require(
        all(
            token in result_normalized
            for token in ("15,383", "30,766", "363", "327", "36", "21,620-bit")
        ),
        "RESULT omits a regenerated count",
    )

    static_audit = source_static_audit(
        candidate_paths["replay_public_certificate.py"], public_source
    )
    require(
        static_audit["candidate_replay"]["sha256"]
        == candidate_hashes["replay_public_certificate.py"],
        "static audit source hash mismatch",
    )

    product_bytes = selected_product.to_bytes((selected_product.bit_length() + 7) // 8, "big")
    root_bytes = exact_square_root.to_bytes((exact_square_root.bit_length() + 7) // 8, "big")
    output = {
        "status": "PASS",
        "audit_verdict": "PASS",
        "role": "independent hostile replay of the F111 public index certificate",
        "regeneration_input_policy": "N and CERTIFICATE.json only; candidate outputs are comparison claims",
        "forbidden_experiments_read": [],
        "general_factorization_or_primality_operations_used": [],
        "allowed_arithmetic_operations_observed": [
            "gcd trial and direct screens",
            "gcd-based endpoint splitting",
            "exact perfect-power extraction",
            "modular inversion",
            "exact integer square root and square testing",
            "terminal gcd extraction",
        ],
        "candidate_artifact_hashes": candidate_hashes,
        "pinned_public_basis_source": {
            "path": "experiments/F98_multiseed_presentation_closure_kill/public_factorization_free_replay.py",
            "sha256": public_hash,
        },
        "candidate_manifest_pins_verified": True,
        "candidate_failed_runs_declared": 0,
        "N": modulus,
        "n": n,
        "bound": bound,
        "public_source": regenerated,
        "certificate": {
            "dependency_support": len(indices),
            "indices_strictly_increasing": all(
                left < right for left, right in zip(indices, indices[1:])
            ),
            "minimum_index": indices[0],
            "maximum_index": indices[-1],
            "index_stream_sha256": selected_index_digest.hexdigest(),
            "selected_record_stream_sha256": selected_record_digest.hexdigest(),
            "provenance_kind_counts": dict(sorted(provenance_counts.items())),
            "selected_nonadaptive_pairs": {
                f"{left},{right}": count for (left, right), count in sorted(appended_pairs.items())
            },
            "selected_exact_product_bit_length": selected_product.bit_length(),
            "selected_exact_product_unsigned_big_endian_sha256": hashlib.sha256(
                product_bytes
            ).hexdigest(),
            "selected_exact_product_is_square": True,
            "positive_exact_root_bit_length": exact_square_root.bit_length(),
            "positive_exact_root_unsigned_big_endian_sha256": hashlib.sha256(
                root_bytes
            ).hexdigest(),
            "root_mod_N": root_modulus,
            "root_squared_mod_N": pow(root_modulus, 2, modulus),
            "gcd_root_minus_one_N": root_minus,
            "gcd_root_plus_one_N": root_plus,
            "gcd_product": root_minus * root_plus,
        },
        "candidate_output_exact_fields_verified": sorted(expected_output_fields),
        "candidate_log_stdout_matches_output": True,
        "result_claims_match_regeneration": True,
        "static_source_audit": static_audit,
        "advice_boundary": {
            "verified": "The fixed 363-index advice identifies one useful dependency in this regenerated batch for this N.",
            "not_verified": [
                "a public algorithm that selects these indices",
                "a selector for another modulus or another batch",
                "a success probability or all-input factoring theorem",
            ],
            "candidate_invokes_dependency_selector": False,
        },
        "certificate_claim_usage": {
            "generation_inputs": [
                "N",
                "n",
                "bound",
                "source_stop_relation_count",
            ],
            "selection_advice": "dependency_relation_indices_zero_based",
            "post_computation_comparisons_only": [
                "expected_root_mod_N",
                "expected_gcd_root_minus_one_N",
                "expected_gcd_root_plus_one_N",
                "provenance_kind_counts",
                "first_successful_appended_pair",
            ],
        },
        "source_semantic_boundary": {
            "no_general_integer_factorization_call": True,
            "no_primality_test_call": True,
            "no_hidden_factor_file_read": True,
            "endpoint_decomposition_by_gcd_and_exact_roots": True,
            "certificate_contains_expected_terminal_gcd_values": True,
            "expected_terminal_gcd_values_used_only_after_independent_gcd_computation": True,
        },
        "elapsed_seconds": time.monotonic() - started,
    }
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate-dir", type=Path, required=True)
    parser.add_argument("--public-basis-source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        output = audit(args.candidate_dir.resolve(), args.public_basis_source.resolve())
        exit_code = 0
    except Exception as error:
        output = {
            "status": "FAIL",
            "audit_verdict": "FAIL",
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
                "audit_verdict": output["audit_verdict"],
                "error": output.get("error"),
            },
            sort_keys=True,
        )
    )
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
