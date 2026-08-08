#!/usr/bin/env python3
"""Isolate the first F116 Sage case and export its exact dependency support."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import time

from sage.all import ZZ


ROOT = Path(__file__).resolve().parents[2]
F115_SOURCE = ROOT / "experiments/F115_all_pairs_global_corpus_audit/audit_independent_verifier.py"
EXPECTED_F115_SHA256 = "bfca59151b428d41631ee445892a42b77d35bd41e468cea111cbd97a97e9626a"
P = 80_000_059
Q = 159_999_943
N = 12_800_004_879_996_637


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()

    source_hash = hashlib.sha256(F115_SOURCE.read_bytes()).hexdigest()
    assert source_hash == EXPECTED_F115_SHA256
    spec = importlib.util.spec_from_file_location("f116_single_pinned_f115", F115_SOURCE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    assert P * Q == N
    assert bool(ZZ(P).is_prime()) and bool(ZZ(Q).is_prime())
    n = N.bit_length()
    bound = n * n
    assert n == 54 and P > bound and Q > bound

    batch = module.Batch(N)
    seed_records = []
    for seed in range(2, n + 1):
        provenance = ("initial_seed", -1, 0, 0, 0, "", seed)
        assert not batch.retain(seed, provenance)
        inverse = pow(seed, -1, N)
        seed_records.append((batch.cache(seed), batch.cache(inverse)))

    supports = module.public_supports(seed_records)
    frozen_pairs = [
        (support[0], 1) if len(support) == 1 else (support[0], support[1])
        for support in supports
    ]
    for pair_index, (u, v) in enumerate(frozen_pairs):
        assert not batch.run_pair(u, v, bound, "frozen_seed_basis_pair", pair_index)
    frozen_summary = {
        "relations": len(batch.residues),
        "dependencies": batch.decoder.dependencies,
        "global_dependencies": batch.decoder.global_dependencies,
        "all_dependencies_global": batch.decoder.dependencies
        == batch.decoder.global_dependencies,
        "pair_count": len(frozen_pairs),
        "pairs": [list(pair) for pair in frozen_pairs],
    }
    assert frozen_summary["all_dependencies_global"]

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

    assert batch.decoder.factor_method == "retained_parity_dependency"
    assert batch.decoder.factor_support is not None
    assert batch.decoder.factor_root is not None
    assert batch.decoder.factor_gcds is not None
    support = batch.decoder.factor_support
    support_records = []
    exact_product = 1
    for source_index in support:
        c = batch.residues[source_index]
        w = pow(c, -1, N)
        value = c * w
        exact_product *= value
        support_records.append(
            {
                "source_index_zero_based": source_index,
                "c": c,
                "w": w,
                "P": value,
                "provenance": list(batch.decoder.provenance[source_index]),
            }
        )
    root = math.isqrt(exact_product)
    assert root * root == exact_product
    root_residue = root % N
    assert root_residue == batch.decoder.factor_root
    assert pow(root_residue, 2, N) == 1
    gcds = [math.gcd(root_residue - 1, N), math.gcd(root_residue + 1, N)]
    assert tuple(gcds) == batch.decoder.factor_gcds
    product_bytes = exact_product.to_bytes((exact_product.bit_length() + 7) // 8, "big")
    root_bytes = root.to_bytes((root.bit_length() + 7) // 8, "big")

    output = {
        "status": "PASS",
        "role": "factor-assisted isolated candidate export; independent factor-free replay required",
        "case": {"ordinal": 3, "p": P, "q": Q, "N": N, "n": n, "bound": bound},
        "pinned_source": {
            str(F115_SOURCE.relative_to(ROOT)): source_hash,
        },
        "frozen": frozen_summary,
        "menu": {
            "total_pairs": (n - 1) * (n - 2) // 2,
            "attempted_pairs": menu_attempted,
            "successful_pair": list(successful_pair) if successful_pair else None,
        },
        "source": {
            "retained_relations": len(batch.residues),
            "attempted_residues": batch.attempted,
            "duplicate_residues": batch.repeated,
            "direct_witness": batch.direct_witness,
        },
        "dependency": {
            "support_size": len(support),
            "source_indices_zero_based": support,
            "source_indices_sha256": hashlib.sha256(
                json.dumps(support, separators=(",", ":")).encode()
            ).hexdigest(),
            "support_records": support_records,
            "exact_product_bit_length": exact_product.bit_length(),
            "exact_product_unsigned_big_endian_sha256": hashlib.sha256(product_bytes).hexdigest(),
            "positive_root_bit_length": root.bit_length(),
            "positive_root_unsigned_big_endian_sha256": hashlib.sha256(root_bytes).hexdigest(),
            "root_mod_N": root_residue,
            "gcd_root_minus_one_N": gcds[0],
            "gcd_root_plus_one_N": gcds[1],
            "provenance_summary": batch.compact_provenance(),
            "support_audit": batch.support_audit(successful_pair),
        },
        "elapsed_seconds": time.monotonic() - started,
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "elapsed_seconds": output["elapsed_seconds"]}))


if __name__ == "__main__":
    main()
