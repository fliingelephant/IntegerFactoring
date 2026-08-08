#!/usr/bin/env python3
"""Stress the fixed all-seed-pair batch on a registered fresh 54-bit corpus."""

from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib
import importlib.util
import json
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parents[2]
F104_SOURCE = ROOT / "experiments/F104_all_input_peeling_counterexample/scan_prime_core_candidates.py"
F110_SOURCE = ROOT / "experiments/F110_frozen_batch_seed_pair_rescue/test_frozen_batch_rescue.py"
EXPECTED_F104_SHA256 = "2b38a3920524a434988ab4fa105d5770a2ef755e5d519c4248b0d2d6bebda79f"
EXPECTED_F110_SHA256 = "2fa5068fbd8eb724d8f169fbf03be7e019db072c8b4fab2537c2c2e725204131"
PAIR_CAP = 24
SELECTED_CAP = 6
P_START = 80_000_000
Q_START = 159_999_999


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha256_file(F104_SOURCE) == EXPECTED_F104_SHA256
assert sha256_file(F110_SOURCE) == EXPECTED_F110_SHA256

F104_SPEC = importlib.util.spec_from_file_location("f116_pinned_f104", F104_SOURCE)
if F104_SPEC is None or F104_SPEC.loader is None:
    raise RuntimeError("cannot import pinned F104 source")
F104 = importlib.util.module_from_spec(F104_SPEC)
F104_SPEC.loader.exec_module(F104)

F110_SPEC = importlib.util.spec_from_file_location("f116_pinned_f110", F110_SOURCE)
if F110_SPEC is None or F110_SPEC.loader is None:
    raise RuntimeError("cannot import pinned F110 source")
F110 = importlib.util.module_from_spec(F110_SPEC)
F110_SPEC.loader.exec_module(F110)


def next_prime(value: int) -> int:
    candidate = value if value & 1 else value + 1
    while not F104.is_prime_u64(candidate):
        candidate += 2
    return candidate


def previous_prime(value: int) -> int:
    candidate = value if value & 1 else value - 1
    while not F104.is_prime_u64(candidate):
        candidate -= 2
    return candidate


def compact_batch(pair: tuple[int, int]) -> dict[str, object]:
    result = F110.run_case(*pair)
    provenance = result.get("dependency_provenance")
    if provenance is not None:
        result["dependency_provenance"] = {
            key: value
            for key, value in provenance.items()
            if key != "relation_indices_zero_based"
        }
    return result


def write_checkpoint(path: Path, payload: dict[str, object]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--checkpoint", type=Path, required=True)
    args = parser.parse_args()
    assert 1 <= args.workers <= SELECTED_CAP

    started = time.monotonic()
    selected: list[dict[str, object]] = []
    scan_trace: list[dict[str, object]] = []
    p = next_prime(P_START)
    q = previous_prime(Q_START)

    for ordinal in range(1, PAIR_CAP + 1):
        modulus = p * q
        n = modulus.bit_length()
        bound = n * n
        certificate = F104.BASE.stable_certificate(p, q)
        row: dict[str, object] = {
            "ordinal": ordinal,
            "p": p,
            "q": q,
            "N": modulus,
            "n": n,
            "bound": bound,
            "trial_hard": p > bound and q > bound,
            "stable": certificate["stable"],
        }
        if row["trial_hard"] and row["stable"]:
            replay = F104.normalize_result(F104.BASE.run_one_round(modulus))
            row["first_round_status"] = replay["status"]
            if replay["status"] == "round_complete":
                roots = replay["matrix"]["public_kernel_basis_roots"]
                row["kernel_basis_size"] = roots["basis_size"]
                row["global_plus"] = roots["global_plus"]
                row["global_minus"] = roots["global_minus"]
                row["non_global_count"] = roots["non_global_count"]
                if (
                    roots["basis_size"] > 0
                    and roots["global_plus"] == roots["basis_size"]
                    and roots["global_minus"] == 0
                    and roots["non_global_count"] == 0
                ):
                    row["selected"] = True
                    selected.append({
                        "ordinal": ordinal,
                        "p": p,
                        "q": q,
                        "N": modulus,
                        "n": n,
                        "first_round_kernel_basis_size": roots["basis_size"],
                    })
                else:
                    row["selected"] = False
            else:
                row["selected"] = False
        else:
            row["selected"] = False
        scan_trace.append(row)
        write_checkpoint(args.checkpoint, {
            "status": "selecting",
            "selected_count": len(selected),
            "selected": selected,
            "scan_trace": scan_trace,
            "elapsed_seconds": time.monotonic() - started,
        })
        if len(selected) == SELECTED_CAP:
            break
        p = next_prime(p + 2)
        q = previous_prime(q - 2)

    if len(selected) != SELECTED_CAP:
        write_checkpoint(args.checkpoint, {
            "status": "selection_shortfall",
            "selected_count": len(selected),
            "selected": selected,
            "scan_trace": scan_trace,
            "elapsed_seconds": time.monotonic() - started,
        })
        raise RuntimeError("registered pair cap did not supply six qualifying cases")

    completed: list[dict[str, object]] = []
    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(compact_batch, (int(row["p"]), int(row["q"]))): row
            for row in selected
        }
        for future in as_completed(futures):
            result = future.result()
            completed.append(result)
            write_checkpoint(args.checkpoint, {
                "status": "running_batches",
                "selected": selected,
                "scan_trace": scan_trace,
                "completed_cases": len(completed),
                "cases": sorted(completed, key=lambda item: item["N"]),
                "elapsed_seconds": time.monotonic() - started,
            })

    completed.sort(key=lambda row: row["N"])
    parity_cases = [
        row for row in completed
        if row["factor_method"] == "retained_parity_dependency"
    ]
    all_cross_layer = all(
        row["dependency_provenance"]["kind_counts"].get("frozen_seed_basis_pair", 0) > 0
        and row["dependency_provenance"]["kind_counts"].get("nonadaptive_seed_pair", 0) > 0
        for row in parity_cases
    )
    output = {
        "status": "PASS" if all(row["status"] == "factor" for row in completed) else "FAIL",
        "role": "factor-assisted fresh finite stress; N-only replay required",
        "registered_bounds": {
            "p_start": P_START,
            "q_start": Q_START,
            "pair_cap": PAIR_CAP,
            "selected_cap": SELECTED_CAP,
            "enumeration": "consecutive p upward and consecutive q downward, paired by ordinal",
        },
        "pinned_sources": {
            str(F104_SOURCE.relative_to(ROOT)): sha256_file(F104_SOURCE),
            str(F110_SOURCE.relative_to(ROOT)): sha256_file(F110_SOURCE),
        },
        "selected": selected,
        "scan_trace": scan_trace,
        "completed_cases": len(completed),
        "factor_cases": sum(row["status"] == "factor" for row in completed),
        "parity_factor_cases": len(parity_cases),
        "direct_factor_cases": len(completed) - len(parity_cases),
        "all_parity_witnesses_cross_the_layer_boundary": all_cross_layer,
        "null_cases": [row["N"] for row in completed if row["status"] != "factor"],
        "cases": completed,
        "elapsed_seconds": time.monotonic() - started,
    }
    write_checkpoint(args.checkpoint, output)
    print(json.dumps({
        "status": output["status"],
        "selected_count": len(selected),
        "completed_cases": output["completed_cases"],
        "factor_cases": output["factor_cases"],
        "parity_factor_cases": output["parity_factor_cases"],
        "direct_factor_cases": output["direct_factor_cases"],
        "all_parity_witnesses_cross_the_layer_boundary": all_cross_layer,
        "null_cases": output["null_cases"],
        "elapsed_seconds": output["elapsed_seconds"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
