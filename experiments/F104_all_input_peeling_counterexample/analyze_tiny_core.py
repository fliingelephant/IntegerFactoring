#!/usr/bin/env python3
"""Expose the exact records and dependencies of one tiny hidden-prime core."""

from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import importlib.util
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
FAST_SOURCE = HERE / "scan_prime_core_candidates.py"
EXPECTED_FAST_SHA256 = "2b38a3920524a434988ab4fa105d5770a2ef755e5d519c4248b0d2d6bebda79f"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha256(FAST_SOURCE) == EXPECTED_FAST_SHA256
SPEC = importlib.util.spec_from_file_location("f104_fast", FAST_SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot import fast F104 source")
FAST = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(FAST)
BASE = FAST.BASE


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--modulus", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    capture: dict[str, object] = {}

    def capturing_builder(unique_records: list[tuple[int, dict[str, object]]]):
        data = FAST.hidden_prime_matrix(unique_records)
        capture["unique_records"] = unique_records
        capture["matrix"] = data
        return data

    BASE.p66_matrix = capturing_builder
    result = FAST.normalize_result(BASE.run_one_round(args.modulus))
    assert result["status"] == "round_complete"
    unique_records = capture["unique_records"]
    matrix_data = capture["matrix"]
    core_columns, core_rows, _ = BASE.peel(
        matrix_data["row_masks"], len(unique_records)
    )
    assert len(core_columns) == result["matrix"]["core_columns"]

    core_set = set(core_columns)
    core_records = []
    prime_supports: dict[int, set[int]] = defaultdict(set)
    for column in core_columns:
        raw_index, record = unique_records[column]
        endpoint_parity: set[int] = set()
        endpoint_factors = []
        for endpoint in (int(record["c"]), int(record["w"])):
            factors = FAST.factor_u64(endpoint)
            endpoint_factors.append(factors)
            for prime, exponent in factors.items():
                if exponent & 1:
                    if prime in endpoint_parity:
                        endpoint_parity.remove(prime)
                    else:
                        endpoint_parity.add(prime)
        for prime in endpoint_parity:
            prime_supports[prime].add(column)
        core_records.append(
            {
                "column_zero_based": column,
                "raw_index_zero_based": raw_index,
                "c": record["c"],
                "w": record["w"],
                "P": record["P"],
                "c_factors": endpoint_factors[0],
                "w_factors": endpoint_factors[1],
                "odd_primes": sorted(endpoint_parity),
                "provenance": record["provenance"],
            }
        )

    restricted_masks: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for prime, global_support in prime_supports.items():
        restricted = tuple(sorted(global_support & core_set))
        if restricted:
            restricted_masks[restricted].append(prime)

    dependencies = []
    for vector in matrix_data["kernel"]:
        support = []
        product = 1
        remaining = vector
        while remaining:
            bit = remaining & -remaining
            column = bit.bit_length() - 1
            support.append(column)
            product *= matrix_data["relation_values"][column]
            remaining ^= bit
        assert set(support).issubset(core_set)
        root = math.isqrt(product)
        assert root * root == product
        dependencies.append(
            {
                "support_zero_based": support,
                "support_size": len(support),
                "root_mod_N": root % args.modulus,
                "gcd_minus": math.gcd(root - 1, args.modulus),
                "gcd_plus": math.gcd(root + 1, args.modulus),
            }
        )

    payload = {
        "status": "PASS",
        "source_sha256": sha256(Path(__file__).resolve()),
        "fast_source_sha256": sha256(FAST_SOURCE),
        "N": args.modulus,
        "one_round_summary": result,
        "core_columns_zero_based": core_columns,
        "core_records": core_records,
        "distinct_restricted_prime_masks": [
            {"support_zero_based": list(support), "primes": sorted(primes)}
            for support, primes in sorted(restricted_masks.items())
        ],
        "kernel_basis": dependencies,
        "core_row_rank": BASE.row_rank(core_rows),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("status=PASS")
    print(f"core_columns={len(core_columns)}")
    print(f"nullity={len(dependencies)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
