#!/usr/bin/env python3
"""Target-free canonical-residue square-class selector."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--block-a", type=int, required=True)
    parser.add_argument("--block-b", type=int, required=True)
    parser.add_argument("--bound", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    started = time.monotonic()
    modulus = args.n
    block_a = args.block_a
    block_b = args.block_b
    bound = args.bound

    first_inverse = pow(block_a, -1, modulus)
    first_product = block_a * first_inverse
    if first_product != block_a * block_b * block_b:
        raise AssertionError("The supplied public square normalization is inconsistent.")

    seen: set[int] = set()
    same_class: list[dict[str, object]] = []
    pair_ordinal = 0
    for total in range(2 * bound + 1):
        for exponent_a in range(bound + 1):
            exponent_b = total - exponent_a
            if not 0 <= exponent_b <= bound:
                continue
            pair_ordinal += 1
            residue = (
                pow(block_a, exponent_a, modulus)
                * pow(block_b, exponent_b, modulus)
                % modulus
            )
            if residue in seen:
                continue
            seen.add(residue)
            inverse = pow(residue, -1, modulus)
            product = residue * inverse
            root = math.isqrt(first_product * product)
            if root * root != first_product * product:
                continue
            divisor_minus = math.gcd(root - 1, modulus)
            divisor_plus = math.gcd(root + 1, modulus)
            same_class.append(
                {
                    "exponents": [exponent_a, exponent_b],
                    "exponent_pair_ordinal_1_based": pair_ordinal,
                    "unique_residue_ordinal_1_based": len(seen),
                    "residue": residue,
                    "inverse": inverse,
                    "relation_value": product,
                    "same_relation_value_as_first": product == first_product,
                    "induced_root": root,
                    "gcd_root_minus_one_n": divisor_minus,
                    "gcd_root_plus_one_n": divisor_plus,
                    "useful": 1 < divisor_minus < modulus,
                }
            )

    distinct = [
        record
        for record in same_class
        if not bool(record["same_relation_value_as_first"])
    ]
    useful = [record for record in same_class if bool(record["useful"])]
    output = {
        "experiment_id": "F96_target_free_canonical_residue_selector",
        "status": "useful_hit" if useful else "finite_null",
        "inputs": {
            "N": modulus,
            "block_a": block_a,
            "block_b": block_b,
            "exponent_bound_each": bound,
            "first_relation_value": first_product,
        },
        "data_policy": {
            "target_endpoint_received": False,
            "target_relation_value_received": False,
            "factor_received": False,
            "candidate_operations": [
                "bounded exponent-pair enumeration",
                "modular exponentiation and multiplication",
                "canonical modular inversion",
                "exact integer square root",
                "gcd of induced root plus or minus one with N",
            ],
        },
        "ordering": "increasing a+b, then increasing a; duplicate residues skipped",
        "counts": {
            "exponent_pairs": (bound + 1) * (bound + 1),
            "unique_residues": len(seen),
            "all_same_square_class": len(same_class),
            "same_old_relation_value": sum(
                bool(record["same_relation_value_as_first"])
                for record in same_class
            ),
            "distinct_relation_value": len(distinct),
            "useful": len(useful),
        },
        "first_distinct_relation_value": distinct[0] if distinct else None,
        "first_useful": useful[0] if useful else None,
        "all_same_square_class_records": same_class,
        "elapsed_seconds": time.monotonic() - started,
    }
    encoded = json.dumps(output, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded, encoding="utf-8")
    print(f"status={output['status']}")
    print(
        f"pairs={output['counts']['exponent_pairs']} "
        f"residues={output['counts']['unique_residues']} "
        f"same_class={output['counts']['all_same_square_class']} "
        f"distinct={output['counts']['distinct_relation_value']} "
        f"useful={output['counts']['useful']}"
    )
    if useful:
        hit = useful[0]
        print(
            f"first_useful=exponents={hit['exponents']} "
            f"residue={hit['residue']} inverse={hit['inverse']} "
            f"factors=({hit['gcd_root_minus_one_n']},{hit['gcd_root_plus_one_n']})"
        )
    print(f"output_sha256={hashlib.sha256(encoded.encode()).hexdigest()}")
    print(f"elapsed_seconds={output['elapsed_seconds']:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
