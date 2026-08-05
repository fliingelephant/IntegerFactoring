#!/usr/bin/env python3
"""Exact finite discovery for mixed-handed residual-fibre Hurwitz outputs.

Family: F14 (Hurwitz one-sided gcds).

This script does not implement the Pollack--Trevino finder.  It enumerates the
finite local object isolated by its proof: norm-N Hurwitz generators, the
row/image sections obtained by a deterministic lexicographic normalization,
and every local residual-fibre involution J_[A:B] at selected semiprimes.
Finite output is discovery/counterexample evidence only.

Hurwitz quaternions are stored by doubled coordinates.  All four coordinates
therefore have one common parity.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from itertools import product
from math import isqrt, log
from pathlib import Path


Quat = tuple[int, int, int, int]
Matrix = tuple[int, int, int, int]
Line = tuple[int, int]


def is_prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def factor_pair(n: int) -> tuple[int, int]:
    factors = [d for d in range(3, isqrt(n) + 1, 2) if n % d == 0]
    assert len(factors) == 1
    p = factors[0]
    q = n // p
    assert p != q and is_prime(p) and is_prime(q)
    return p, q


def shell_doubled(n: int) -> list[Quat]:
    bound = isqrt(4 * n)
    answer: list[Quat] = []
    for a in range(-bound, bound + 1):
        for b in range(-bound, bound + 1):
            for c in range(-bound, bound + 1):
                rem = 4 * n - a * a - b * b - c * c
                if rem < 0:
                    continue
                d = isqrt(rem)
                if d * d != rem:
                    continue
                for signed_d in ((0,) if d == 0 else (-d, d)):
                    value = (a, b, c, signed_d)
                    if len({coordinate & 1 for coordinate in value}) == 1:
                        answer.append(value)
    return sorted(set(answer))


def mat_mul(a: Matrix, b: Matrix, r: int) -> Matrix:
    return (
        (a[0] * b[0] + a[1] * b[2]) % r,
        (a[0] * b[1] + a[1] * b[3]) % r,
        (a[2] * b[0] + a[3] * b[2]) % r,
        (a[2] * b[1] + a[3] * b[3]) % r,
    )


def quat_mul(x: Quat, y: Quat) -> Quat:
    a, b, c, d = x
    e, f, g, h = y
    raw = (
        a * e - b * f - c * g - d * h,
        a * f + b * e + c * h - d * g,
        a * g - b * h + c * e + d * f,
        a * h + b * g - c * f + d * e,
    )
    assert all(coordinate % 2 == 0 for coordinate in raw)
    return tuple(coordinate // 2 for coordinate in raw)  # type: ignore[return-value]


def integer_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)


def crt_pair(a: int, p: int, b: int, q: int) -> int:
    return (a + p * (((b - a) * pow(p, -1, q)) % q)) % (p * q)


def split_basis(r: int) -> tuple[Matrix, Matrix, Matrix, Matrix]:
    s, t = next(
        (s, t)
        for s in range(r)
        for t in range(r)
        if (s * s + t * t + 1) % r == 0
    )
    one = (1, 0, 0, 1)
    i_mat = (0, 1, -1 % r, 0)
    j_mat = (s, t, t, -s % r)
    k_mat = mat_mul(i_mat, j_mat, r)
    minus_one = (-1 % r, 0, 0, -1 % r)
    assert mat_mul(i_mat, i_mat, r) == minus_one
    assert mat_mul(j_mat, j_mat, r) == minus_one
    return one, i_mat, j_mat, k_mat


def quat_matrix(value: Quat, r: int, basis: tuple[Matrix, ...]) -> Matrix:
    inv2 = pow(2, -1, r)
    return tuple(
        sum(value[index] * inv2 * basis[index][entry] for index in range(4)) % r
        for entry in range(4)
    )  # type: ignore[return-value]


def line(vector: tuple[int, int], r: int) -> Line:
    if vector[0] % r:
        scale = pow(vector[0] % r, -1, r)
        return (1, vector[1] * scale % r)
    assert vector[1] % r
    return (0, 1)


def normalize_projective_pair(a: int, b: int, r: int) -> Line:
    return line((a % r, b % r), r)


def row_line(matrix: Matrix, r: int) -> Line:
    first = (matrix[0], matrix[1])
    return line(first if first != (0, 0) else (matrix[2], matrix[3]), r)


def image_line(matrix: Matrix, r: int) -> Line:
    first = (matrix[0], matrix[2])
    return line(first if first != (0, 0) else (matrix[1], matrix[3]), r)


def right_action(value: Line, matrix: Matrix, r: int) -> Line:
    return line(
        (
            value[0] * matrix[0] + value[1] * matrix[2],
            value[0] * matrix[1] + value[1] * matrix[3],
        ),
        r,
    )


def left_action(matrix: Matrix, value: Line, r: int) -> Line:
    return line(
        (
            matrix[0] * value[0] + matrix[1] * value[1],
            matrix[2] * value[0] + matrix[3] * value[1],
        ),
        r,
    )


def kernel_line(matrix: Matrix, r: int) -> Line:
    row = row_line(matrix, r)
    return line((-row[1], row[0]), r)


PROJECTIVE_UNITS: tuple[Quat, ...] = (
    (2, 0, 0, 0),
    (0, 2, 0, 0),
    (0, 0, 2, 0),
    (0, 0, 0, 2),
) + tuple(
    (1, b, c, d)
    for b in (-1, 1)
    for c in (-1, 1)
    for d in (-1, 1)
)


def allowed_lines(r: int) -> list[Line]:
    values = [(0, 1)] + [(1, slope) for slope in range(r)]
    return [value for value in values if (value[0] ** 2 + value[1] ** 2) % r]


def fibre_involution(parameter: Line, r: int) -> Matrix:
    a, b = parameter
    matrix = (a, b, b, -a % r)
    scalar = (a * a + b * b) % r
    assert mat_mul(matrix, matrix, r) == (scalar, 0, 0, scalar)
    return matrix


def summarize(n: int) -> dict[str, object]:
    p, q = factor_pair(n)
    primes = (p, q)
    bases = {r: split_basis(r) for r in primes}
    units = {
        r: [quat_matrix(unit, r, bases[r]) for unit in PROJECTIVE_UNITS]
        for r in primes
    }
    shell = shell_doubled(n)
    assert len(shell) == 24 * (p + 1) * (q + 1)
    matrices = {
        value: {r: quat_matrix(value, r, bases[r]) for r in primes}
        for value in shell
    }
    rows = {
        value: tuple(row_line(matrices[value][r], r) for r in primes)
        for value in shell
    }
    images = {
        value: tuple(image_line(matrices[value][r], r) for r in primes)
        for value in shell
    }
    row_fibres: dict[tuple[Line, Line], list[Quat]] = {}
    image_fibres: dict[tuple[Line, Line], list[Quat]] = {}
    for value in shell:
        row_fibres.setdefault(rows[value], []).append(value)
        image_fibres.setdefault(images[value], []).append(value)
    assert set(map(len, row_fibres.values())) == {24}
    assert set(map(len, image_fibres.values())) == {24}

    # Lexicographically least doubled coordinates are an explicit, factor-free
    # canonical representative of each unit orbit once the gcd has produced it.
    right_sections = {key: min(values) for key, values in row_fibres.items()}
    left_sections = {key: min(values) for key, values in image_fibres.items()}
    supports = {r: allowed_lines(r) for r in primes}
    completion_parameters = {
        r: [(value, fibre_involution(value, r)) for value in supports[r]] for r in primes
    }

    completion_summaries: list[dict[str, object]] = []
    completion_by_parameters: dict[tuple[Line, Line], dict[str, object]] = {}
    first_unit_menu_failure: dict[str, object] | None = None
    for (parameter_p, jp), (parameter_q, jq) in product(
        completion_parameters[p], completion_parameters[q]
    ):
        transforms = {p: jp, q: jq}
        parameters = {p: parameter_p, q: parameter_q}
        local_zw: dict[int, tuple[int, int]] = {}
        for r in primes:
            s = bases[r][2][0]
            t = bases[r][2][1]
            a, b = parameters[r]
            local_zw[r] = ((-s * a - t * b) % r, (-t * a + s * b) % r)
        z = crt_pair(local_zw[p][0], p, local_zw[q][0], q)
        w = crt_pair(local_zw[p][1], p, local_zw[q][1], q)
        conjugate_c = (0, 0, -2 * z, -2 * w)
        counts: Counter[str] = Counter()
        first_failure_row_pair: tuple[Line, Line] | None = None
        for row_pair in product(supports[p], supports[q]):
            image_pair = tuple(
                left_action(transforms[r], row_pair[index], r)
                for index, r in enumerate(primes)
            )
            d_right = right_sections[row_pair]
            d_left = left_sections[image_pair]
            d_right_mats = matrices[d_right]
            d_left_mats = matrices[d_left]

            direct_rows = [
                row_line(d_right_mats[r], r) == row_line(d_left_mats[r], r)
                for r in primes
            ]
            direct_images = [
                image_line(d_right_mats[r], r) == image_line(d_left_mats[r], r)
                for r in primes
            ]
            counts["direct_gcrd_proper"] += direct_rows[0] != direct_rows[1]
            counts["direct_gcld_proper"] += direct_images[0] != direct_images[1]

            right_unit_patterns = set()
            left_unit_patterns = set()
            coefficient_gcds = []
            for unit_index in range(12):
                right_pattern = tuple(
                        row_line(d_right_mats[r], r)
                        == right_action(row_line(d_left_mats[r], r), units[r][unit_index], r)
                        for r in primes
                    )
                right_unit_patterns.add(right_pattern)
                left_unit_patterns.add(
                    tuple(
                        left_action(units[r][unit_index], image_line(d_right_mats[r], r), r)
                        == image_line(d_left_mats[r], r)
                        for r in primes
                    )
                )
                normalized_left = quat_mul(d_left, PROJECTIVE_UNITS[unit_index])
                coefficient = quat_mul(conjugate_c, normalized_left)[1]
                coefficient_gcds.append(integer_gcd(n, coefficient))
                assert tuple(coefficient % r == 0 for r in primes) == right_pattern
            counts["some_right_unit_proper"] += (True, False) in right_unit_patterns or (
                False,
                True,
            ) in right_unit_patterns
            counts["some_left_unit_proper"] += (True, False) in left_unit_patterns or (
                False,
                True,
            ) in left_unit_patterns
            if (
                first_unit_menu_failure is None
                and (True, False) not in right_unit_patterns
                and (False, True) not in right_unit_patterns
            ):
                first_unit_menu_failure = {
                    "N": n,
                    "p": p,
                    "q": q,
                    "J_parameters": {str(r): list(parameters[r]) for r in primes},
                    "completion_z_w_mod_N": [z, w],
                    "row_pair": [list(value) for value in row_pair],
                    "image_pair": [list(value) for value in image_pair],
                    "canonical_gcrd": list(d_right),
                    "canonical_gcld": list(d_left),
                    "i_coordinate_gcds_for_12_right_units": coefficient_gcds,
                }
            if (
                first_failure_row_pair is None
                and (True, False) not in right_unit_patterns
                and (False, True) not in right_unit_patterns
            ):
                first_failure_row_pair = row_pair

            product_patterns = []
            for left, right in ((d_left_mats, d_right_mats), (d_right_mats, d_left_mats)):
                product_patterns.append(
                    tuple(
                        image_line(right[r], r) == kernel_line(left[r], r)
                        for r in primes
                    )
                )
            counts["some_product_zero_proper"] += any(
                pattern[0] != pattern[1] for pattern in product_patterns
            )

        total = len(supports[p]) * len(supports[q])
        completion_summary = {
                "J_p": list(jp),
                "J_q": list(jq),
                "total_row_pairs": total,
                "first_right_unit_failure_row_pair": (
                    None
                    if first_failure_row_pair is None
                    else [list(value) for value in first_failure_row_pair]
                ),
                **dict(counts),
            }
        completion_summaries.append(completion_summary)
        completion_by_parameters[(parameter_p, parameter_q)] = completion_summary

    small_three_mod_four_primes = [
        ell
        for ell in range(3, int(log(n)) + 1)
        if ell % 4 == 3 and is_prime(ell)
    ]
    public_product = 1
    for ell in small_three_mod_four_primes:
        public_product *= ell
    auxiliary_modulus = n * public_product // integer_gcd(n, public_product)
    actual_completions: list[tuple[int, int, int, tuple[Line, Line]]] = []
    for z_actual in range(isqrt(auxiliary_modulus - 1) + 1):
        for w_actual in range(isqrt(auxiliary_modulus - 1 - z_actual * z_actual) + 1):
            residual = z_actual * z_actual + w_actual * w_actual
            if not (0 < residual < auxiliary_modulus):
                continue
            if residual % 4 != 1 or integer_gcd(residual, auxiliary_modulus) != 1:
                continue
            parameter_pair = []
            for r in primes:
                s = bases[r][2][0]
                t = bases[r][2][1]
                parameter_pair.append(
                    normalize_projective_pair(
                        z_actual * s + w_actual * t,
                        z_actual * t - w_actual * s,
                        r,
                    )
                )
            actual_completions.append(
                (residual, z_actual, w_actual, tuple(parameter_pair))  # type: ignore[arg-type]
            )

    first_actual_completion_failure: dict[str, object] | None = None
    actual_completion_profiles: list[dict[str, object]] = []
    for residual, z_actual, w_actual, parameter_pair in actual_completions:
        completion_summary = completion_by_parameters[parameter_pair]
        failure_row_data = completion_summary["first_right_unit_failure_row_pair"]
        if residual == 1:
            actual_completion_profiles.append({
                "R": residual,
                "z": z_actual,
                "w": w_actual,
                "J_parameters": [list(value) for value in parameter_pair],
                "some_right_unit_proper": completion_summary.get("some_right_unit_proper", 0),
                "total_row_pairs": completion_summary["total_row_pairs"],
                "has_failure": failure_row_data is not None,
            })
        if failure_row_data is None:
            continue
        if first_actual_completion_failure is not None:
            continue
        row_pair = tuple(tuple(value) for value in failure_row_data)  # type: ignore[assignment]
        image_pair = tuple(
            left_action(
                fibre_involution(parameter_pair[index], r),
                row_pair[index],
                r,
            )
            for index, r in enumerate(primes)
        )
        d_right = right_sections[row_pair]
        d_left = left_sections[image_pair]
        conjugate_c = (0, 0, -2 * z_actual, -2 * w_actual)
        coefficient_gcds = [
            integer_gcd(
                n,
                quat_mul(
                    conjugate_c,
                    quat_mul(d_left, unit),
                )[1],
            )
            for unit in PROJECTIVE_UNITS
        ]
        assert all(value in (1, n) for value in coefficient_gcds)

        local_xy = []
        for index, r in enumerate(primes):
            s = bases[r][2][0]
            t = bases[r][2][1]
            a = (z_actual * s + w_actual * t) % r
            b = (z_actual * t - w_actual * s) % r
            u, v = row_pair[index]
            scale = 2 * (a * u + b * v) * pow((u * u + v * v) % r, -1, r) % r
            local_xy.append(((scale * u - a) % r, (scale * v - b) % r))
        x = crt_pair(local_xy[0][0], p, local_xy[1][0], q)
        y = crt_pair(local_xy[0][1], p, local_xy[1][1], q)
        assert (x * x + y * y + residual) % n == 0
        first_actual_completion_failure = {
            "N": n,
            "p": p,
            "q": q,
            "auxiliary_modulus_M": auxiliary_modulus,
            "residual_R": residual,
            "beta_coordinates_mod_N": [x, y, z_actual, w_actual],
            "J_parameters": {str(r): list(parameter_pair[index]) for index, r in enumerate(primes)},
            "row_pair": [list(value) for value in row_pair],
            "image_pair": [list(value) for value in image_pair],
            "canonical_gcrd": list(d_right),
            "canonical_gcld": list(d_left),
            "i_coordinate_gcds_for_12_right_units": coefficient_gcds,
        }

    fields = (
        "direct_gcrd_proper",
        "direct_gcld_proper",
        "some_right_unit_proper",
        "some_left_unit_proper",
        "some_product_zero_proper",
    )
    extrema = {
        field: {
            "minimum": min(int(entry.get(field, 0)) for entry in completion_summaries),
            "maximum": max(int(entry.get(field, 0)) for entry in completion_summaries),
        }
        for field in fields
    }
    return {
        "N": n,
        "p": p,
        "q": q,
        "shell_size": len(shell),
        "support_sizes": {str(r): len(supports[r]) for r in primes},
        "number_of_completion_pairs": len(completion_summaries),
        "auxiliary_modulus_M": auxiliary_modulus,
        "number_of_residual_compatible_nonnegative_completions": len(actual_completions),
        "residual_one_completion_profiles": actual_completion_profiles,
        "extrema_over_completion_pairs": extrema,
        "first_unit_menu_failure": first_unit_menu_failure,
        "first_residual_compatible_unit_menu_failure": first_actual_completion_failure,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--inputs",
        nargs="+",
        type=int,
        default=[15, 21, 33, 35, 39, 55, 77, 91, 143, 187, 221, 323, 391, 437],
    )
    args = parser.parse_args()
    payload = {
        "family": "F14",
        "run": "F14-M01",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "normalization": "lexicographically least doubled coordinate tuple",
        "results": [summarize(value) for value in args.inputs],
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
