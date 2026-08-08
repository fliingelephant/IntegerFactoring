#!/usr/bin/env python3
"""Repeat F116 with the pinned independent Sage/Pari batch implementation."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import time

from sage.all import ZZ
from sage.env import SAGE_VERSION


ROOT = Path(__file__).resolve().parents[2]
F104_SOURCE = ROOT / "experiments/F104_all_input_peeling_counterexample/scan_prime_core_candidates.py"
F115_SOURCE = ROOT / "experiments/F115_all_pairs_global_corpus_audit/audit_independent_verifier.py"
EXPECTED_F104_SHA256 = "2b38a3920524a434988ab4fa105d5770a2ef755e5d519c4248b0d2d6bebda79f"
EXPECTED_F115_SHA256 = "bfca59151b428d41631ee445892a42b77d35bd41e468cea111cbd97a97e9626a"
PAIR_CAP = 24
SELECTED_CAP = 6
P_START = 80_000_000
Q_START = 159_999_999


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


assert sha256_file(F104_SOURCE) == EXPECTED_F104_SHA256
assert sha256_file(F115_SOURCE) == EXPECTED_F115_SHA256
F104 = load_module("f116_sage_pinned_f104", F104_SOURCE)
F115 = load_module("f116_sage_pinned_f115", F115_SOURCE)


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


def write_checkpoint(path: Path, payload: dict[str, object]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def select_cases() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    selected: list[dict[str, object]] = []
    trace: list[dict[str, object]] = []
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
            "sage_primes": bool(ZZ(p).is_prime() and ZZ(q).is_prime()),
        }
        assert row["sage_primes"]
        if row["trial_hard"] and row["stable"]:
            replay = F104.normalize_result(F104.BASE.run_one_round(modulus))
            row["first_round_status"] = replay["status"]
            if replay["status"] == "round_complete":
                roots = replay["matrix"]["public_kernel_basis_roots"]
                row.update(
                    kernel_basis_size=roots["basis_size"],
                    global_plus=roots["global_plus"],
                    global_minus=roots["global_minus"],
                    non_global_count=roots["non_global_count"],
                )
                row["selected"] = bool(
                    roots["basis_size"] > 0
                    and roots["global_plus"] == roots["basis_size"]
                    and roots["global_minus"] == 0
                    and roots["non_global_count"] == 0
                )
            else:
                row["selected"] = False
        else:
            row["selected"] = False
        trace.append(row)
        if row["selected"]:
            selected.append(
                {
                    "ordinal": ordinal,
                    "p": p,
                    "q": q,
                    "N": modulus,
                    "n": n,
                    "first_round_kernel_basis_size": row["kernel_basis_size"],
                }
            )
        if len(selected) == SELECTED_CAP:
            break
        p = next_prime(p + 2)
        q = previous_prime(q - 2)
    if len(selected) != SELECTED_CAP:
        raise RuntimeError("registered pair cap did not supply six qualifying cases")
    return selected, trace


def run_case(case: dict[str, object]) -> dict[str, object]:
    p = int(case["p"])
    q = int(case["q"])
    modulus = p * q
    n = modulus.bit_length()
    bound = n * n
    started = time.monotonic()
    batch = F115.Batch(modulus)
    seed_records = []
    for seed in range(2, n + 1):
        provenance = ("initial_seed", -1, 0, 0, 0, "", seed)
        assert not batch.retain(seed, provenance)
        inverse = pow(seed, -1, modulus)
        seed_records.append((batch.cache(seed), batch.cache(inverse)))

    supports = F115.public_supports(seed_records)
    frozen_pairs = [
        (support[0], 1) if len(support) == 1 else (support[0], support[1])
        for support in supports
    ]
    for pair_index, (u, v) in enumerate(frozen_pairs):
        assert not batch.run_pair(u, v, bound, "frozen_seed_basis_pair", pair_index)
    first_layer = {
        "relations": len(batch.residues),
        "dependencies": batch.decoder.dependencies,
        "global_dependencies": batch.decoder.global_dependencies,
        "all_dependencies_global": (
            batch.decoder.dependencies == batch.decoder.global_dependencies
        ),
        "pair_count": len(frozen_pairs),
        "pairs": [list(pair) for pair in frozen_pairs],
    }
    assert first_layer["all_dependencies_global"]

    successful_pair = None
    menu_attempted = 0
    for u in range(2, n + 1):
        for v in range(u + 1, n + 1):
            pair_index = menu_attempted
            menu_attempted += 1
            if batch.run_pair(u, v, bound, "nonadaptive_seed_pair", pair_index):
                successful_pair = (u, v)
                break
        if successful_pair is not None:
            break

    status = "factor" if batch.decoder.factor is not None else "null"
    provenance = batch.compact_provenance()
    support_audit = None
    if batch.decoder.factor_method == "retained_parity_dependency":
        assert successful_pair is not None
        support_audit = batch.support_audit(successful_pair)
    return {
        **case,
        "status": status,
        "factor": batch.decoder.factor,
        "factor_method": batch.decoder.factor_method,
        "factor_dependency_size": len(batch.decoder.factor_support or []),
        "first_layer": first_layer,
        "seed_pair_menu_total": (n - 1) * (n - 2) // 2,
        "seed_pair_menu_attempted": menu_attempted,
        "successful_pair": list(successful_pair) if successful_pair else None,
        "relations_at_stop": len(batch.residues),
        "dependencies_at_stop": batch.decoder.dependencies,
        "global_dependencies_at_stop": batch.decoder.global_dependencies,
        "candidate_residues_attempted": batch.attempted,
        "duplicate_residues": batch.repeated,
        "dependency_provenance": provenance,
        "support_audit": support_audit,
        "direct_witness": batch.direct_witness,
        "elapsed_seconds": time.monotonic() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    selected, scan_trace = select_cases()
    write_checkpoint(
        args.checkpoint,
        {
            "status": "running_batches",
            "selected": selected,
            "scan_trace": scan_trace,
            "completed_cases": 0,
            "cases": [],
            "elapsed_seconds": time.monotonic() - started,
        },
    )
    cases = []
    for case in selected:
        cases.append(run_case(case))
        write_checkpoint(
            args.checkpoint,
            {
                "status": "running_batches",
                "selected": selected,
                "scan_trace": scan_trace,
                "completed_cases": len(cases),
                "cases": cases,
                "elapsed_seconds": time.monotonic() - started,
            },
        )

    parity_cases = [
        row for row in cases if row["factor_method"] == "retained_parity_dependency"
    ]
    direct_methods = Counter(
        row["factor_method"] for row in cases if row["factor_method"] != "retained_parity_dependency"
    )
    output = {
        "status": "PASS" if all(row["status"] == "factor" for row in cases) else "FAIL",
        "role": "factor-assisted fresh finite stress; N-only replay required",
        "backend": f"SageMath {SAGE_VERSION} / Pari via pinned F115 verifier",
        "registered_bounds": {
            "p_start": P_START,
            "q_start": Q_START,
            "pair_cap": PAIR_CAP,
            "selected_cap": SELECTED_CAP,
            "enumeration": "consecutive p upward and consecutive q downward, paired by ordinal",
        },
        "pinned_sources": {
            str(F104_SOURCE.relative_to(ROOT)): sha256_file(F104_SOURCE),
            str(F115_SOURCE.relative_to(ROOT)): sha256_file(F115_SOURCE),
        },
        "selected": selected,
        "scan_trace": scan_trace,
        "completed_cases": len(cases),
        "factor_cases": sum(row["status"] == "factor" for row in cases),
        "parity_factor_cases": len(parity_cases),
        "direct_factor_methods": dict(sorted(direct_methods.items())),
        "all_parity_witnesses_cross_the_layer_boundary": all(
            row["support_audit"]["crosses_frozen_and_appended_layers"]
            for row in parity_cases
        ),
        "null_cases": [row["N"] for row in cases if row["status"] != "factor"],
        "cases": cases,
        "elapsed_seconds": time.monotonic() - started,
    }
    write_checkpoint(args.checkpoint, output)
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
