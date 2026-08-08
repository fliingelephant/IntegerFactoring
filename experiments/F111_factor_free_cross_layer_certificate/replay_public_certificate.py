#!/usr/bin/env python3
"""Factor-free public verification of one explicit F110 dependency."""

from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
PUBLIC_BASIS_SOURCE = ROOT / "experiments/F98_multiseed_presentation_closure_kill/public_factorization_free_replay.py"
EXPECTED_PUBLIC_BASIS_SHA256 = "5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b"
CERTIFICATE = HERE / "CERTIFICATE.json"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha256_file(PUBLIC_BASIS_SOURCE) == EXPECTED_PUBLIC_BASIS_SHA256
SPEC = importlib.util.spec_from_file_location("f111_public_basis", PUBLIC_BASIS_SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot import pinned public basis source")
PUBLIC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PUBLIC)


def main() -> None:
    started = time.monotonic()
    certificate = json.loads(CERTIFICATE.read_text())
    modulus = certificate["N"]
    n = modulus.bit_length()
    bound = n * n
    assert n == certificate["n"] and bound == certificate["bound"]
    assert all(math.gcd(trial, modulus) == 1 for trial in range(2, bound + 1))

    records: list[dict[str, object]] = []
    endpoints: list[int] = []
    seen: set[int] = set()
    attempted = 0
    repeated = 0
    direct_screens = 0

    def retain(c: int, provenance: dict[str, object]) -> None:
        nonlocal attempted, repeated, direct_screens
        attempted += 1
        if c in seen:
            repeated += 1
            return
        seen.add(c)
        w = pow(c, -1, modulus)
        for difference in (c - w, c + w):
            direct_screens += 1
            divisor = math.gcd(difference, modulus)
            assert divisor in (1, modulus)
        records.append({"c": c, "w": w, "P": c * w, "provenance": provenance})
        endpoints.extend((c, w))

    for seed in range(2, n + 1):
        retain(seed, {"kind": "initial_seed", "seed": seed})

    initial_endpoint_count = len(endpoints)
    initial_basis, basis_stats = PUBLIC.gcd_free_basis(endpoints)
    initial_columns = PUBLIC.relation_columns(initial_basis, len(records))
    frozen_pairs = []
    for column in initial_columns:
        support = sorted(initial_basis[index][0] for index in column)
        frozen_pairs.append((support[0], 1) if len(support) == 1 else tuple(support[:2]))

    for pair_index, (u, v) in enumerate(frozen_pairs):
        for exponent in range(bound + 1):
            for orientation, c in (
                ("u_power_times_v", pow(u, exponent, modulus) * v % modulus),
                ("u_times_v_power", u * pow(v, exponent, modulus) % modulus),
            ):
                retain(
                    c,
                    {
                        "kind": "frozen_seed_basis_pair",
                        "pair_index_zero_based": pair_index,
                        "u": u,
                        "v": v,
                        "exponent": exponent,
                        "orientation": orientation,
                    },
                )
    frozen_relation_count = len(records)

    stop = certificate["source_stop_relation_count"]
    for pair_index, (u, v) in enumerate(((2, 3), (2, 4))):
        for exponent in range(bound + 1):
            for orientation, c in (
                ("u_power_times_v", pow(u, exponent, modulus) * v % modulus),
                ("u_times_v_power", u * pow(v, exponent, modulus) % modulus),
            ):
                retain(
                    c,
                    {
                        "kind": "nonadaptive_seed_pair",
                        "pair_index_zero_based": pair_index,
                        "u": u,
                        "v": v,
                        "exponent": exponent,
                        "orientation": orientation,
                    },
                )
                if len(records) == stop:
                    break
            if len(records) == stop:
                break
        if len(records) == stop:
            break
    assert len(records) == stop

    indices = certificate["dependency_relation_indices_zero_based"]
    assert len(indices) == certificate["dependency_support"] == len(set(indices))
    assert min(indices) >= 0 and max(indices) < len(records)
    selected = [records[index] for index in indices]
    selected_product = math.prod(record["P"] for record in selected)
    exact_root = math.isqrt(selected_product)
    assert exact_root * exact_root == selected_product
    root_mod_n = exact_root % modulus
    minus = math.gcd(exact_root - 1, modulus)
    plus = math.gcd(exact_root + 1, modulus)
    assert root_mod_n == certificate["expected_root_mod_N"]
    assert minus == certificate["expected_gcd_root_minus_one_N"]
    assert plus == certificate["expected_gcd_root_plus_one_N"]
    assert minus * plus == modulus
    kind_counts = Counter(record["provenance"]["kind"] for record in selected)
    assert dict(sorted(kind_counts.items())) == certificate["provenance_kind_counts"]

    output = {
        "status": "PASS",
        "role": "factor-free verification of one explicit public dependency certificate",
        "forbidden_operations_used": [],
        "input_hashes": {
            "CERTIFICATE.json": sha256_file(CERTIFICATE),
            str(PUBLIC_BASIS_SOURCE.relative_to(ROOT)): sha256_file(PUBLIC_BASIS_SOURCE),
        },
        "N": modulus,
        "n": n,
        "bound": bound,
        "trial_screen_null": True,
        "initial_endpoint_count": initial_endpoint_count,
        "initial_basis_blocks": len(initial_basis),
        "initial_basis_stats": basis_stats,
        "frozen_pair_count": len(frozen_pairs),
        "frozen_pairs": [list(pair) for pair in frozen_pairs],
        "frozen_relation_count": frozen_relation_count,
        "source_stop_relation_count": len(records),
        "candidate_residues_attempted": attempted,
        "duplicate_residues": repeated,
        "direct_gcd_screens": direct_screens,
        "proper_direct_gcds": 0,
        "dependency_support": len(indices),
        "dependency_provenance_kind_counts": dict(sorted(kind_counts.items())),
        "selected_exact_product_bit_length": selected_product.bit_length(),
        "selected_exact_product_is_square": True,
        "root_mod_N": root_mod_n,
        "gcd_root_minus_one_N": minus,
        "gcd_root_plus_one_N": plus,
        "elapsed_seconds": time.monotonic() - started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
