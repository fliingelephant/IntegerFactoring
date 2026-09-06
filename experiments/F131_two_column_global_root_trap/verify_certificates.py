#!/usr/bin/env python3
"""Exact arithmetic verifier for the finite F131 certificates."""

import json
import math


def check_case(t: int, factors: tuple[int, ...] | None = None) -> dict:
    n_value = t * t - 2
    a = (n_value - t) // 2
    b = (n_value + t) // 2
    endpoints = (
        (t - 2) ** 2,
        (t + 1) ** 2 // 2,
        2 * (t + 2) ** 2 // 3,
        3 * (t - 1) ** 2 // 4,
    )
    c1, w1, c2, w2 = endpoints
    p1 = c1 * w1
    p2 = c2 * w2
    root = 2 * a * b
    screens = (
        math.gcd(c1 - w1, n_value),
        math.gcd(c1 + w1, n_value),
        math.gcd(c2 - w2, n_value),
        math.gcd(c2 + w2, n_value),
    )

    assert t >= 11 and t % 2 == 1 and t % 3 == 1
    assert all(1 <= endpoint < n_value for endpoint in endpoints)
    assert p1 == 2 * a * a and p2 == 2 * b * b
    assert p1 % n_value == 1 and p2 % n_value == 1
    assert pow(c1, -1, n_value) == w1
    assert pow(c2, -1, n_value) == w2
    assert screens == (1, 1, 1, 1)
    assert root * root == p1 * p2
    assert root % n_value == n_value - 1
    if factors is not None:
        product = 1
        for factor in factors:
            product *= factor
        assert product == n_value

    return {
        "t": t,
        "N": n_value,
        "a": a,
        "b": b,
        "endpoints": endpoints,
        "P1": p1,
        "P2": p2,
        "screens": screens,
        "root": root,
        "root_mod_N": root % n_value,
    }


def main() -> None:
    base = check_case(97, (23, 409))
    nonsquarefree = check_case(373, (23, 23, 263))
    constant = 119 * 17 * 4559 * 5233
    modulus = 6 * 529 * constant
    family = []
    for index in range(8):
        case = check_case(373 + index * modulus)
        assert case["N"] % 529 == 0
        assert math.gcd(case["N"], constant) == 1
        family.append(
            {
                "index": index,
                "t": case["t"],
                "N_bits": case["N"].bit_length(),
                "N_mod_529": case["N"] % 529,
                "screens": case["screens"],
                "root_mod_N": case["root_mod_N"],
            }
        )

    print(
        json.dumps(
            {
                "status": "PASS",
                "base_certificate": base,
                "nonsquarefree_certificate": nonsquarefree,
                "family_prefix": family,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

