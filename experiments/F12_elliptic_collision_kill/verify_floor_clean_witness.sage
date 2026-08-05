#!/usr/bin/env sage
"""Recheck the clean elliptic witness at m=floor(sqrt(N)).

Approach-family ID: F12_elliptic_collision_kill.
"""

import argparse
import hashlib
import json
import math
import time
from pathlib import Path


FAMILY = "F12_elliptic_collision_kill"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--witness", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    started = time.monotonic()
    witness_path = Path(args.witness).resolve()
    with witness_path.open() as handle:
        certificate = json.load(handle)
    N = certificate["inputs"]["N"]
    length = math.isqrt(N)
    threshold = 2 * length - 1
    curve_a = certificate["witness"]["curve"]["a"]
    curve_b = certificate["witness"]["curve"]["b"]
    local_outputs = []

    for local in certificate["witness"]["local"]:
        characteristic = local["characteristic"]
        curve = EllipticCurve(GF(characteristic), [curve_a, curve_b])
        point = curve(local["point"])
        order = int(point.order())
        assert length < order <= threshold
        multiples = [index * point for index in range(1, length + 1)]
        assert all(not multiple.is_zero() for multiple in multiples)
        collisions = [
            [left, right]
            for left in range(1, length + 1)
            for right in range(left + 1, length + 1)
            if multiples[left - 1][0] == multiples[right - 1][0]
        ]
        assert collisions
        assert all(
            (right - left) % order == 0 or (right + left) % order == 0
            for left, right in collisions
        )
        local_outputs.append(
            {
                "characteristic": characteristic,
                "point_order": order,
                "m": length,
                "two_m_minus_1": threshold,
                "all_multiples_affine": True,
                "first_x_collision": collisions[0],
                "collision_count": len(collisions),
            }
        )

    source_path = Path(__file__).resolve().with_suffix("")
    output = {
        "approach_family": FAMILY,
        "N": N,
        "m_floor_sqrt_N": length,
        "collision_threshold": threshold,
        "local": local_outputs,
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
