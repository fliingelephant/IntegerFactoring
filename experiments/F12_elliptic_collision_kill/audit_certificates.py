#!/usr/bin/env python3
"""Audit the retained F12 certificates without recomputing the searches."""

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


FAMILY = "F12_elliptic_collision_kill"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--elliptic", required=True)
    parser.add_argument("--torus", required=True)
    parser.add_argument("--division", required=True)
    parser.add_argument("--prime-powers", required=True)
    parser.add_argument("--floor-witness", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    paths = {
        name: Path(value).resolve()
        for name, value in {
            "elliptic": args.elliptic,
            "torus": args.torus,
            "division": args.division,
            "prime_powers": args.prime_powers,
            "floor_witness": args.floor_witness,
        }.items()
    }
    records = {name: json.loads(path.read_text()) for name, path in paths.items()}
    assert all(record["approach_family"] == FAMILY for record in records.values())
    for record in records.values():
        source = Path(record["source"])
        assert sha256(source) == record["source_sha256"]

    elliptic = records["elliptic"]
    assert elliptic["inputs"] == {
        "N": 10403,
        "p": 101,
        "q": 103,
        "m": 102,
        "collision_threshold": 203,
        "coefficient_limit": 40,
    }
    assert elliptic["hasse_upper_bounds_floor"] == [122, 124]
    assert elliptic["witness"]["curve"] == {"a": 1, "b": 5}
    assert elliptic["witness"]["global_point"] == [5461, 5889]
    x, y = elliptic["witness"]["global_point"]
    assert (y * y - x**3 - x - 5) % 10403 == 0
    assert [entry["group_order"] for entry in elliptic["witness"]["local"]] == [112, 106]
    assert [entry["point_order"] for entry in elliptic["witness"]["local"]] == [112, 106]
    assert [entry["first_x_collision"] for entry in elliptic["witness"]["local"]] == [
        [10, 102],
        [4, 102],
    ]

    division = records["division"]
    assert division["pairwise_identity_checks"] == 45
    assert [entry["division_polynomial_zero_indices_through_2m_minus_1"] for entry in division["witness_local_checks"]] == [[112], [106]]
    assert all(entry["denominator_indices_1_through_m_all_nonzero"] for entry in division["witness_local_checks"])
    assert all(entry["collected_cleared_product"] == 0 for entry in division["witness_local_checks"])
    assert division["witness_source_sha256"] == sha256(paths["elliptic"])

    floor_witness = records["floor_witness"]
    assert floor_witness["m_floor_sqrt_N"] == 101
    assert floor_witness["collision_threshold"] == 201
    assert [entry["point_order"] for entry in floor_witness["local"]] == [112, 106]
    assert [entry["first_x_collision"] for entry in floor_witness["local"]] == [
        [11, 101],
        [5, 101],
    ]
    for entry in floor_witness["local"]:
        left, right = entry["first_x_collision"]
        assert left + right == entry["point_order"]
        assert entry["m"] < entry["point_order"] <= entry["two_m_minus_1"]
        assert entry["all_multiples_affine"]
    assert floor_witness["witness_source_sha256"] == sha256(paths["elliptic"])

    torus = records["torus"]
    assert [entry["m"] for entry in torus["symbolic_checks"]] == list(range(2, 11))
    first, second = torus["instances"]
    assert (first["N"], first["m_floor_sqrt_N"], first["successful_units"]) == (10403, 101, 3200)
    assert Fraction(first["exact_conditional_success_probability"]) == Fraction(16, 51)
    assert Fraction(first["primitive_root_probability"]) == Fraction(16, 51)
    assert (second["N"], second["m_floor_sqrt_N"], second["successful_units"]) == (1111, 33, 600)
    assert Fraction(second["exact_conditional_success_probability"]) == Fraction(3, 5)
    assert Fraction(second["primitive_root_probability"]) == Fraction(2, 5)

    prime_powers = records["prime_powers"]
    assert [(entry["N"], entry["total_prime_multiplicity_s"], entry["m_s_floor_N_to_1_over_s"]) for entry in prime_powers["records"]] == [(3087, 5, 4), (1452, 5, 4)]
    assert [entry["proper_gcd_values_at_k_equals_s"] for entry in prime_powers["records"]] == [[9], [12]]
    assert all(entry["scan_2_through_bitlength_contains_k_equals_s"] for entry in prime_powers["records"])
    assert prime_powers["perfect_power_preprocessing"] == {
        "N": 225,
        "exponent": 2,
        "proper_root_divisor": 15,
    }

    source = Path(__file__).resolve()
    output = {
        "approach_family": FAMILY,
        "audit_passed": True,
        "input_sha256": {name: sha256(path) for name, path in paths.items()},
        "source": str(source),
        "source_sha256": sha256(source),
    }
    Path(args.output).write_text(json.dumps(output, indent=2) + "\n")


if __name__ == "__main__":
    main()
