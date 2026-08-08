#!/usr/bin/env python3
"""Stress the frozen first layer plus the nonadaptive (2,v) menu."""

from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib
import importlib.util
import json
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parents[2]
F110_SOURCE = ROOT / "experiments/F110_frozen_batch_seed_pair_rescue/test_frozen_batch_rescue.py"
EXPECTED_F110_SHA256 = "2fa5068fbd8eb724d8f169fbf03be7e019db072c8b4fab2537c2c2e725204131"
F104_DIR = ROOT / "experiments/F104_all_input_peeling_counterexample"
EXCLUDED_FILES = {"PRIME_SCAN_320K_640K_WIDE_OUTPUT.json"}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha256_file(F110_SOURCE) == EXPECTED_F110_SHA256
SPEC = importlib.util.spec_from_file_location("f112_pinned_f110", F110_SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot import pinned F110 source")
F110 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(F110)


def global_only_cases() -> tuple[list[dict[str, object]], dict[str, str]]:
    selected: dict[int, dict[str, object]] = {}
    input_hashes = {}
    for path in sorted(F104_DIR.glob("*OUTPUT.json")):
        if path.name in EXCLUDED_FILES:
            continue
        data = json.loads(path.read_text())
        if data.get("status") == "running":
            continue
        used = False
        for row in data.get("trace", []):
            result = row.get("result", {})
            roots = result.get("matrix", {}).get("public_kernel_basis_roots", {})
            if (
                result.get("status") == "round_complete"
                and roots.get("basis_size", 0) > 0
                and roots.get("non_global_count") == 0
                and roots.get("global_minus") == 0
                and roots.get("global_plus") == roots.get("basis_size")
            ):
                used = True
                selected[row["N"]] = {
                    "p": row["p"],
                    "q": row["q"],
                    "N": row["N"],
                    "source_file": path.name,
                    "first_round_kernel_basis_size": roots["basis_size"],
                }
        if used:
            input_hashes[str(path.relative_to(ROOT))] = sha256_file(path)
    return [selected[N] for N in sorted(selected)], input_hashes


def run_narrow_case(case: dict[str, object]) -> dict[str, object]:
    p = int(case["p"])
    q = int(case["q"])
    modulus = p * q
    assert modulus == case["N"]
    n = modulus.bit_length()
    bound = n * n
    started = time.monotonic()

    batch = F110.FrozenBatch(modulus)
    for seed in range(2, n + 1):
        assert not batch.retain(seed, {"kind": "initial_seed", "seed": seed})
    initial_records = len(batch.records)
    _, supports = F110.F98.public_basis(batch.records)
    frozen_pairs = []
    for support in supports:
        pair = (support[0], 1) if len(support) == 1 else (support[0], support[1])
        frozen_pairs.append(pair)
    for pair_index, (u, v) in enumerate(frozen_pairs):
        assert not batch.run_pair(u, v, bound, "frozen_seed_basis_pair", pair_index)

    first_layer_relations = len(batch.records)
    first_layer_dependencies = batch.decoder.dependencies
    first_layer_global_dependencies = batch.decoder.global_dependencies
    assert first_layer_dependencies == first_layer_global_dependencies

    successful_pair = None
    appended_pairs_attempted = 0
    for v in range(3, n + 1):
        pair_index = appended_pairs_attempted
        appended_pairs_attempted += 1
        if batch.run_pair(2, v, bound, "nonadaptive_two_v_pair", pair_index):
            successful_pair = [2, v]
            break

    provenance = batch.dependency_provenance()
    compact_provenance = None
    if provenance is not None:
        compact_provenance = {
            "kind_counts": provenance["kind_counts"],
            "distinct_nonseed_trajectory_keys": provenance["distinct_nonseed_trajectory_keys"],
            "root_mod_N": provenance["root_mod_N"],
            "gcd_root_minus_one_N": provenance["gcd_root_minus_one_N"],
            "gcd_root_plus_one_N": provenance["gcd_root_plus_one_N"],
        }
    return {
        **case,
        "n": n,
        "bound": bound,
        "status": "factor" if batch.decoder.factor is not None else "null",
        "factor": batch.decoder.factor,
        "factor_method": batch.decoder.factor_method,
        "factor_dependency_size": batch.decoder.factor_dependency_size,
        "successful_pair": successful_pair,
        "appended_pairs_attempted": appended_pairs_attempted,
        "appended_pair_cap": n - 2,
        "initial_records": initial_records,
        "frozen_pair_count": len(frozen_pairs),
        "first_layer_relations": first_layer_relations,
        "first_layer_dependencies": first_layer_dependencies,
        "first_layer_global_dependencies": first_layer_global_dependencies,
        "relations_at_stop": len(batch.records),
        "dependencies_at_stop": batch.decoder.dependencies,
        "global_dependencies_at_stop": batch.decoder.global_dependencies,
        "candidate_residues_attempted": batch.attempted,
        "duplicate_residues": batch.repeated,
        "dependency_provenance": compact_provenance,
        "elapsed_seconds": time.monotonic() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--checkpoint", type=Path, required=True)
    args = parser.parse_args()
    assert 1 <= args.workers <= 8
    cases, input_hashes = global_only_cases()
    started = time.monotonic()
    completed = []

    def write_checkpoint(status: str) -> None:
        data = {
            "status": status,
            "role": "factor-assisted finite stress test; N-only replay required",
            "corpus_size": len(cases),
            "completed_cases": len(completed),
            "pinned_source": {
                str(F110_SOURCE.relative_to(ROOT)): sha256_file(F110_SOURCE),
            },
            "input_hashes": input_hashes,
            "cases": sorted(completed, key=lambda row: row["N"]),
            "elapsed_seconds": time.monotonic() - started,
        }
        temporary = args.checkpoint.with_suffix(args.checkpoint.suffix + ".tmp")
        temporary.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
        temporary.replace(args.checkpoint)

    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(run_narrow_case, case): case for case in cases}
        for future in as_completed(futures):
            completed.append(future.result())
            write_checkpoint("running")

    completed.sort(key=lambda row: row["N"])
    parity_cases = [row for row in completed if row["factor_method"] == "retained_parity_dependency"]
    all_cross_layer = all(
        row["dependency_provenance"]["kind_counts"].get("frozen_seed_basis_pair", 0) > 0
        and row["dependency_provenance"]["kind_counts"].get("nonadaptive_two_v_pair", 0) > 0
        for row in parity_cases
    )
    result = {
        "status": "PASS" if all(row["status"] == "factor" for row in completed) else "FAIL",
        "role": "factor-assisted finite stress test; N-only replay required",
        "corpus_size": len(cases),
        "completed_cases": len(completed),
        "pinned_source": {
            str(F110_SOURCE.relative_to(ROOT)): sha256_file(F110_SOURCE),
        },
        "input_hashes": input_hashes,
        "all_frozen_two_v_batches_factor": all(row["status"] == "factor" for row in completed),
        "parity_factor_cases": len(parity_cases),
        "direct_factor_cases": len(completed) - len(parity_cases),
        "all_parity_witnesses_cross_the_layer_boundary": all_cross_layer,
        "null_cases": [row["N"] for row in completed if row["status"] != "factor"],
        "cases": completed,
        "elapsed_seconds": time.monotonic() - started,
    }
    args.checkpoint.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": result["status"],
        "corpus_size": result["corpus_size"],
        "parity_factor_cases": result["parity_factor_cases"],
        "direct_factor_cases": result["direct_factor_cases"],
        "all_parity_witnesses_cross_the_layer_boundary": all_cross_layer,
        "null_cases": result["null_cases"],
        "elapsed_seconds": result["elapsed_seconds"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
