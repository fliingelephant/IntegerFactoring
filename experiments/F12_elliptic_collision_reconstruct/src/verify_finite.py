#!/usr/bin/env python3
"""Exact finite certificate for F12 elliptic collision reconstruction."""

import argparse
import json
import math
from pathlib import Path


def add(left, right, a, p):
    if left is None:
        return right
    if right is None:
        return left
    x1, y1 = left
    x2, y2 = right
    if x1 == x2 and (y1 + y2) % p == 0:
        return None
    if left == right:
        slope = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    else:
        slope = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x3 = (slope * slope - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p
    return x3, y3


def curve_order(a, b, p):
    total = 1
    for x in range(p):
        rhs = (x**3 + a * x + b) % p
        if rhs == 0:
            total += 1
        elif pow(rhs, (p - 1) // 2, p) == 1:
            total += 2
    return total


def point_data(point, a, b, p, m):
    multiples = [None]
    current = None
    order = None
    for k in range(1, 4 * p + 1):
        current = add(current, point, a, p)
        if k <= m:
            multiples.append(current)
        if current is None:
            order = k
            break
    if order is None:
        raise RuntimeError("order search did not terminate")
    if any(value is None for value in multiples[1:]):
        raise RuntimeError("a denominator vanishes before m")
    collisions = []
    for i in range(1, m + 1):
        for j in range(i + 1, m + 1):
            if multiples[i][0] == multiples[j][0]:
                collisions.append((i, j))
    first_i, first_j = collisions[0]
    return {
        "point": list(point),
        "curve_order": curve_order(a, b, p),
        "point_order": order,
        "multiples_1_through_m_affine": True,
        "collision_count": len(collisions),
        "first_collision": [first_i, first_j],
        "first_collision_left_point": list(multiples[first_i]),
        "first_collision_right_point": list(multiples[first_j]),
        "first_collision_sum": first_i + first_j,
        "first_collision_difference": first_j - first_i,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--parameters", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    params = json.loads(Path(args.parameters).read_text())
    n, p, q, m = (params[key] for key in ("N", "p", "q", "m"))
    a, b = params["curve"]["A"], params["curve"]["B"]
    x, y = params["point"]["x"], params["point"]["y"]
    discriminant = -16 * (4 * a**3 + 27 * b**2)
    if p * q != n or (y * y - x**3 - a * x - b) % n:
        raise SystemExit("global parameter check failed")
    if math.gcd(discriminant, n) != 1:
        raise SystemExit("curve is not good at both primes")
    local = {}
    for prime in (p, q):
        point = (x % prime, y % prime)
        if (point[1] ** 2 - point[0] ** 3 - a * point[0] - b) % prime:
            raise SystemExit("bad local point")
        local[str(prime)] = point_data(point, a, b, prime, m)
    result = {
        "status": "pass",
        "N_factorization_checked": p * q == n,
        "global_point_on_curve": True,
        "discriminant": discriminant,
        "discriminant_gcd_N": math.gcd(discriminant, n),
        "m": m,
        "hasse_integer_upper_bounds": {
            str(p): math.floor(p + 1 + 2 * math.sqrt(p)),
            str(q): math.floor(q + 1 + 2 * math.sqrt(q)),
        },
        "local": local,
    }
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
