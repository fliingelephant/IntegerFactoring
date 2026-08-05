#!/usr/bin/env sage
"""Find a clean balanced additive-orbit collision synchronized in both fields.

Approach-family ID: F12_elliptic_collision_kill.

The fixed balanced semiprime is 101*103 and m=ceil(sqrt(N)).  We search a
single short Weierstrass equation whose two local groups contain points of
order strictly greater than m.  Hasse already puts every local point order
below 2m-1, so such points have unit/defined denominators through m but an
x-coordinate collision caused by the +/- ambiguity.
"""

import argparse
import hashlib
import json
import math
import time
from pathlib import Path


FAMILY = "F12_elliptic_collision_kill"
P = ZZ(101)
Q = ZZ(103)
N = P * Q
M = ZZ(math.isqrt(int(N)))
if M * M < N:
    M += 1
THRESHOLD = 2 * M - 1


def maximal_order_point(curve):
    points = [point for point in curve.points() if not point.is_zero()]
    return max(points, key=lambda point: point.order())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--coefficient-limit", type=int, default=40)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    started = time.monotonic()
    witness = None

    for curve_a in range(args.coefficient_limit + 1):
        for curve_b in range(args.coefficient_limit + 1):
            discriminant_core = 4 * curve_a**3 + 27 * curve_b**2
            if discriminant_core % P == 0 or discriminant_core % Q == 0:
                continue
            curve_p = EllipticCurve(GF(P), [curve_a, curve_b])
            curve_q = EllipticCurve(GF(Q), [curve_a, curve_b])
            point_p = maximal_order_point(curve_p)
            point_q = maximal_order_point(curve_q)
            order_p = ZZ(point_p.order())
            order_q = ZZ(point_q.order())
            if order_p <= M or order_q <= M:
                continue
            assert order_p <= THRESHOLD and order_q <= THRESHOLD

            local_records = []
            for characteristic, curve, point, order in (
                (P, curve_p, point_p, order_p),
                (Q, curve_q, point_q, order_q),
            ):
                multiples = [index * point for index in range(1, M + 1)]
                assert all(not multiple.is_zero() for multiple in multiples)
                first_collision = None
                for left in range(1, M + 1):
                    for right in range(left + 1, M + 1):
                        if multiples[left - 1][0] == multiples[right - 1][0]:
                            first_collision = [left, right]
                            break
                    if first_collision is not None:
                        break
                assert first_collision is not None
                assert order.divides(first_collision[1] - first_collision[0]) or order.divides(
                    first_collision[0] + first_collision[1]
                )
                difference_product = GF(characteristic)(1)
                for left in range(M):
                    for right in range(left + 1, M):
                        difference_product *= multiples[left][0] - multiples[right][0]
                assert difference_product == 0
                local_records.append(
                    {
                        "characteristic": int(characteristic),
                        "group_order": int(curve.cardinality()),
                        "point": [int(point[0]), int(point[1])],
                        "point_order": int(order),
                        "all_multiples_1_through_m_affine": True,
                        "first_x_collision": first_collision,
                        "collision_is_difference_multiple": order.divides(
                            first_collision[1] - first_collision[0]
                        ),
                        "collision_is_sum_multiple": order.divides(
                            first_collision[0] + first_collision[1]
                        ),
                        "x_difference_product": int(difference_product),
                    }
                )

            point_x = int(crt([local_records[0]["point"][0], local_records[1]["point"][0]], [P, Q]))
            point_y = int(crt([local_records[0]["point"][1], local_records[1]["point"][1]], [P, Q]))
            assert (point_y**2 - point_x**3 - curve_a * point_x - curve_b) % N == 0
            assert gcd(-16 * discriminant_core, N) == 1
            witness = {
                "curve": {"a": curve_a, "b": curve_b},
                "global_point": [point_x, point_y],
                "discriminant_mod_N": int((-16 * discriminant_core) % N),
                "local": local_records,
            }
            break
        if witness is not None:
            break
    assert witness is not None

    source_path = Path(__file__).resolve().with_suffix("")
    output = {
        "approach_family": FAMILY,
        "purpose": "clean synchronized additive-orbit collision",
        "inputs": {
            "N": int(N),
            "p": int(P),
            "q": int(Q),
            "m": int(M),
            "collision_threshold": int(THRESHOLD),
            "coefficient_limit": args.coefficient_limit,
        },
        "hasse_upper_bounds_floor": [
            int(P + 1 + floor(2 * sqrt(P))),
            int(Q + 1 + floor(2 * sqrt(Q))),
        ],
        "witness": witness,
        "elapsed_seconds": time.monotonic() - started,
        "source": str(source_path),
        "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
    }
    with open(args.output, "w") as handle:
        json.dump(output, handle, indent=2, default=int)
        handle.write("\n")


main()
