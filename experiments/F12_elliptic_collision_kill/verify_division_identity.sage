#!/usr/bin/env sage
"""Verify the division-polynomial collision identity on the clean witness.

Approach-family ID: F12_elliptic_collision_kill.
"""

import argparse
import hashlib
import json
import time
from pathlib import Path


FAMILY = "F12_elliptic_collision_kill"


def sum_multiplicity(index, length):
    if index < 3 or index > 2 * length - 1:
        return 0
    lower = max(1, index - length)
    upper = floor((index - 1) / 2)
    return max(0, upper - lower + 1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--witness", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    started = time.monotonic()
    witness_path = Path(args.witness).resolve()
    with witness_path.open() as handle:
        certificate = json.load(handle)
    assert certificate["approach_family"] == FAMILY
    length = certificate["inputs"]["m"]
    threshold = 2 * length - 1
    curve_a = certificate["witness"]["curve"]["a"]
    curve_b = certificate["witness"]["curve"]["b"]
    local_outputs = []

    for local in certificate["witness"]["local"]:
        characteristic = local["characteristic"]
        field = GF(characteristic)
        curve = EllipticCurve(field, [curve_a, curve_b])
        point = curve(local["point"])
        order = ZZ(point.order())
        assert order == local["point_order"]
        psi = {
            index: curve.division_polynomial(
                index, point, two_torsion_multiplicity=1
            )
            for index in range(1, threshold + 1)
        }
        zero_indices = [index for index, value in psi.items() if value == 0]
        assert zero_indices == [
            index for index in range(1, threshold + 1) if order.divides(index)
        ]
        assert all(psi[index] != 0 for index in range(1, length + 1))

        exponent_by_index = {}
        for index in range(1, threshold + 1):
            difference_exponent = length - index if 1 <= index <= length - 1 else 0
            exponent_by_index[index] = int(
                difference_exponent + sum_multiplicity(index, length)
            )
        assert [
            index
            for index, exponent in exponent_by_index.items()
            if index >= 2 and exponent > 0
        ] == list(range(2, threshold + 1))
        collected_product = field(1)
        for index, exponent in exponent_by_index.items():
            collected_product *= psi[index] ** exponent
        assert collected_product == 0

        local_outputs.append(
            {
                "characteristic": characteristic,
                "point_order": int(order),
                "division_polynomial_zero_indices_through_2m_minus_1": zero_indices,
                "denominator_indices_1_through_m_all_nonzero": True,
                "positive_product_exponent_range": [2, threshold],
                "collected_cleared_product": int(collected_product),
            }
        )

    identity_curve = EllipticCurve(GF(101), [curve_a, curve_b])
    identity_point = identity_curve(certificate["witness"]["local"][0]["point"])
    identity_length = 10
    identity_checks = 0
    identity_psi = {
        index: identity_curve.division_polynomial(
            index, identity_point, two_torsion_multiplicity=1
        )
        for index in range(1, 2 * identity_length)
    }
    for left in range(1, identity_length + 1):
        for right in range(left + 1, identity_length + 1):
            phi_left = (left * identity_point)[0] * identity_psi[left] ** 2
            phi_right = (right * identity_point)[0] * identity_psi[right] ** 2
            cleared_difference = (
                phi_left * identity_psi[right] ** 2
                - phi_right * identity_psi[left] ** 2
            )
            factored_difference = identity_psi[left + right] * identity_psi[
                right - left
            ]
            assert cleared_difference == factored_difference
            identity_checks += 1

    source_path = Path(__file__).resolve().with_suffix("")
    output = {
        "approach_family": FAMILY,
        "identity": "phi_i*psi_j^2-phi_j*psi_i^2=psi_(i+j)*psi_(j-i) for i<j",
        "pairwise_identity_checks": identity_checks,
        "identity_check_field": 101,
        "identity_check_m": identity_length,
        "witness_local_checks": local_outputs,
        "elapsed_seconds": time.monotonic() - started,
        "witness_source": str(witness_path),
        "witness_source_sha256": hashlib.sha256(witness_path.read_bytes()).hexdigest(),
        "source": str(source_path),
        "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
    }
    with open(args.output, "w") as handle:
        json.dump(output, handle, indent=2, default=int)
        handle.write("\n")


main()
