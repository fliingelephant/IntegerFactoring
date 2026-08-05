#!/usr/bin/env python3
"""Independent finite checks for the cubic-automorphism reconstruction.

This script uses only the Python standard library.  It verifies the local
factorization counts, the mismatch counts, the coefficient formulas, and the
two explicit composite-modulus examples used in RESULT.md.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from itertools import product


def discriminant(A: int, B: int, C: int) -> int:
    return A * A * B * B - 4 * B**3 - 4 * A**3 * C - 27 * C * C + 18 * A * B * C


def mul(v: tuple[int, int, int], w: tuple[int, int, int], A: int, B: int, C: int, n: int) -> tuple[int, int, int]:
    raw = [0] * 5
    for i, vi in enumerate(v):
        for j, wj in enumerate(w):
            raw[i + j] += vi * wj
    for degree in (4, 3):
        coefficient = raw[degree]
        raw[degree - 1] -= coefficient * A
        raw[degree - 2] -= coefficient * B
        raw[degree - 3] -= coefficient * C
    return tuple(value % n for value in raw[:3])


def add(*vectors: tuple[int, int, int], n: int) -> tuple[int, int, int]:
    return tuple(sum(vector[i] for vector in vectors) % n for i in range(3))


def scale(scalar: int, vector: tuple[int, int, int], n: int) -> tuple[int, int, int]:
    return tuple(scalar * value % n for value in vector)


def image_is_root(y: tuple[int, int, int], A: int, B: int, C: int, n: int) -> bool:
    one = (1, 0, 0)
    y2 = mul(y, y, A, B, C, n)
    y3 = mul(y2, y, A, B, C, n)
    value = add(y3, scale(A, y2, n), scale(B, y, n), scale(C, one, n), n=n)
    return value == (0, 0, 0)


def determinant_formula(y: tuple[int, int, int], A: int, B: int, C: int, n: int) -> int:
    _, beta, gamma = y
    return (
        beta**3
        - 2 * A * beta * beta * gamma
        + (A * A + B) * beta * gamma * gamma
        + (C - A * B) * gamma**3
    ) % n


def apply_image(z: tuple[int, int, int], y: tuple[int, int, int], A: int, B: int, C: int, n: int) -> tuple[int, int, int]:
    one = (1, 0, 0)
    y2 = mul(y, y, A, B, C, n)
    return add(scale(z[0], one, n), scale(z[1], y, n), scale(z[2], y2, n), n=n)


def image_power(y: tuple[int, int, int], exponent: int, A: int, B: int, C: int, n: int) -> tuple[int, int, int]:
    current = (0, 1, 0)
    for _ in range(exponent):
        current = apply_image(current, y, A, B, C, n)
    return current


def formula_y2_fixed(y: tuple[int, int, int], A: int, B: int, C: int, n: int) -> tuple[int, int, int]:
    # Kept separate from mul() so that the displayed closed formula is checked.
    alpha, beta, gamma = y
    return tuple(
        value % n
        for value in (
            alpha * alpha - 2 * C * beta * gamma + A * C * gamma * gamma,
            2 * alpha * beta - 2 * B * beta * gamma + (A * B - C) * gamma * gamma,
            beta * beta + 2 * alpha * gamma - 2 * A * beta * gamma + (A * A - B) * gamma * gamma,
        )
    )


def classify_cubic(A: int, B: int, C: int, prime: int) -> str | None:
    delta = discriminant(A, B, C) % prime
    if delta == 0:
        return None
    roots = sum((x**3 + A * x * x + B * x + C) % prime == 0 for x in range(prime))
    return {0: "3", 1: "12", 3: "111"}[roots]


def local_counts(prime: int) -> dict[str, int]:
    counts = {"111": 0, "12": 0, "3": 0, "nonsquarefree": 0}
    for A, B, C in product(range(prime), repeat=3):
        kind = classify_cubic(A, B, C, prime)
        counts[kind if kind is not None else "nonsquarefree"] += 1
    expected = {
        "111": prime * (prime - 1) * (prime - 2) // 6,
        "12": prime * prime * (prime - 1) // 2,
        "3": (prime**3 - prime) // 3,
        "nonsquarefree": prime * prime,
    }
    assert counts == expected, (prime, counts, expected)
    return counts


def mismatch_counts(p: int, q: int, counts_p: dict[str, int], counts_q: dict[str, int]) -> dict[str, object]:
    support2 = {"111", "12"}
    support3 = {"111", "3"}
    squarefree = sum(counts_p[k] for k in support2 | {"3"}) * sum(counts_q[k] for k in support2 | {"3"})
    mismatch2 = sum(
        counts_p[kp] * counts_q[kq]
        for kp in ("111", "12", "3")
        for kq in ("111", "12", "3")
        if (kp in support2) != (kq in support2)
    )
    mismatch3 = sum(
        counts_p[kp] * counts_q[kq]
        for kp in ("111", "12", "3")
        for kq in ("111", "12", "3")
        if (kp in support3) != (kq in support3)
    )
    total = (p * q) ** 3
    expected_squarefree = Fraction((p - 1) * (q - 1), p * q)
    expected_mismatch2 = expected_squarefree * Fraction(4 * p * q + p + q - 2, 9 * p * q)
    expected_mismatch3 = expected_squarefree * Fraction(1, 2)
    assert Fraction(squarefree, total) == expected_squarefree
    assert Fraction(mismatch2, total) == expected_mismatch2
    assert Fraction(mismatch3, total) == expected_mismatch3
    return {
        "squarefree_count": squarefree,
        "squarefree_probability": str(expected_squarefree),
        "order2_mismatch_count": mismatch2,
        "order2_mismatch_probability": str(expected_mismatch2),
        "order3_mismatch_count": mismatch3,
        "order3_mismatch_probability": str(expected_mismatch3),
    }


def enumerate_automorphisms(n: int, A: int, B: int, C: int) -> dict[str, list[list[int]]]:
    identity = (0, 1, 0)
    automorphisms: list[tuple[int, int, int]] = []
    square_torsion: list[tuple[int, int, int]] = []
    cube_torsion: list[tuple[int, int, int]] = []
    for y in product(range(n), repeat=3):
        assert formula_y2_fixed(y, A, B, C, n) == mul(y, y, A, B, C, n)
        if not image_is_root(y, A, B, C, n):
            continue
        determinant = determinant_formula(y, A, B, C, n)
        if math.gcd(determinant, n) != 1:
            continue
        automorphisms.append(y)
        if image_power(y, 2, A, B, C, n) == identity:
            square_torsion.append(y)
        if image_power(y, 3, A, B, C, n) == identity:
            cube_torsion.append(y)
    return {
        "automorphisms": [list(y) for y in automorphisms],
        "square_torsion": [list(y) for y in square_torsion],
        "cube_torsion": [list(y) for y in cube_torsion],
    }


def example_record(n: int, A: int, B: int, C: int, local_primes: tuple[int, int]) -> dict[str, object]:
    data = enumerate_automorphisms(n, A, B, C)
    delta = discriminant(A, B, C)
    record: dict[str, object] = {
        "N": n,
        "f": [1, A, B, C],
        "discriminant": delta,
        "discriminant_mod_N": delta % n,
        "gcd_discriminant_N": math.gcd(delta, n),
        "local_types": {str(prime): classify_cubic(A, B, C, prime) for prime in local_primes},
        **data,
    }
    record["nonidentity_cube_gcds"] = [
        [math.gcd(n, y[0]), math.gcd(n, y[1] - 1), math.gcd(n, y[2])]
        for y in data["cube_torsion"]
        if y != [0, 1, 0]
    ]
    record["nonidentity_square_gcds"] = [
        [math.gcd(n, y[0]), math.gcd(n, y[1] - 1), math.gcd(n, y[2])]
        for y in data["square_torsion"]
        if y != [0, 1, 0]
    ]
    return record


def find_full_coefficient_involution(prime: int, kind: str) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    identity = (0, 1, 0)
    for A, B, C in product(range(prime), repeat=3):
        if classify_cubic(A, B, C, prime) != kind:
            continue
        for y in product(range(prime), repeat=3):
            difference = (y[0], y[1] - 1, y[2])
            if y == identity or any(value % prime == 0 for value in difference):
                continue
            if not image_is_root(y, A, B, C, prime):
                continue
            if determinant_formula(y, A, B, C, prime) == 0:
                continue
            if image_power(y, 2, A, B, C, prime) == identity:
                return (A, B, C), y
    raise AssertionError(f"no full-coefficient involution for prime={prime}, kind={kind}")


def crt_pair(value_p: int, value_q: int, p: int, q: int) -> int:
    return (value_p + p * ((value_q - value_p) * pow(p, -1, q) % q)) % (p * q)


def off_promise_order2_counterexample() -> dict[str, object]:
    p, q = 3, 5
    f_p, y_p = find_full_coefficient_involution(p, "12")
    f_q, y_q = find_full_coefficient_involution(q, "111")
    A, B, C = (crt_pair(f_p[i], f_q[i], p, q) for i in range(3))
    y = tuple(crt_pair(y_p[i], y_q[i], p, q) for i in range(3))
    n = p * q
    identity = (0, 1, 0)
    assert classify_cubic(A, B, C, p) == "12"
    assert classify_cubic(A, B, C, q) == "111"
    assert image_is_root(y, A, B, C, n)
    assert math.gcd(determinant_formula(y, A, B, C, n), n) == 1
    assert image_power(y, 2, A, B, C, n) == identity
    coefficient_gcds = [math.gcd(n, y[0]), math.gcd(n, y[1] - 1), math.gcd(n, y[2])]
    assert coefficient_gcds == [1, 1, 1]
    return {
        "N": n,
        "f": [1, A, B, C],
        "local_f_mod_3": list(f_p),
        "local_f_mod_5": list(f_q),
        "involution": list(y),
        "local_involution_mod_3": list(y_p),
        "local_involution_mod_5": list(y_q),
        "coefficient_gcds": coefficient_gcds,
        "discriminant_mod_N": discriminant(A, B, C) % n,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    counts = {str(prime): local_counts(prime) for prime in (3, 5, 7, 11)}
    results = {
        "local_counts": counts,
        "mismatch_counts": {
            "N=15": mismatch_counts(3, 5, counts["3"], counts["5"]),
            "N=35": mismatch_counts(5, 7, counts["5"], counts["7"]),
        },
        "examples": {
            "N=15,f=X^3+2X+5": example_record(15, 0, 2, 5, (3, 5)),
            "N=35,f=X^3+2": example_record(35, 0, 0, 2, (5, 7)),
            "order2_Jacobi_minus_off_promise": off_promise_order2_counterexample(),
        },
    }

    with open(args.output, "w", encoding="utf-8") as output:
        json.dump(results, output, indent=2, sort_keys=True)
        output.write("\n")


if __name__ == "__main__":
    main()
