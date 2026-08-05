#!/usr/bin/env python3
"""Independent exact finite checks for the F15 Hurwitz-gcd audit.

Every quaternion is stored as the four integer numerators of
    (a + b*i + c*j + d*k) / 2.
The four numerators therefore have one common parity.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path


Quaternion = tuple[int, int, int, int]
Matrix = tuple[tuple[int, int], tuple[int, int]]


def elements_norm(n: int) -> list[Quaternion]:
    radius = math.isqrt(4 * n)
    answer = []
    for value in product(range(-radius, radius + 1), repeat=4):
        if sum(x * x for x in value) != 4 * n:
            continue
        if len({x & 1 for x in value}) != 1:
            continue
        answer.append(value)
    return answer


def conjugate(x: Quaternion) -> Quaternion:
    return x[0], -x[1], -x[2], -x[3]


def multiply(x: Quaternion, y: Quaternion) -> Quaternion:
    a, b, c, d = x
    e, f, g, h = y
    raw = (
        a * e - b * f - c * g - d * h,
        a * f + b * e + c * h - d * g,
        a * g - b * h + c * e + d * f,
        a * h + b * g - c * f + d * e,
    )
    assert all(z % 2 == 0 for z in raw)
    result = tuple(z // 2 for z in raw)
    assert len({z & 1 for z in result}) == 1
    return result  # type: ignore[return-value]


def norm(x: Quaternion) -> int:
    total = sum(z * z for z in x)
    assert total % 4 == 0
    return total // 4


def mat_add(a: Matrix, b: Matrix, r: int) -> Matrix:
    return tuple(
        tuple((a[i][j] + b[i][j]) % r for j in range(2)) for i in range(2)
    )  # type: ignore[return-value]


def mat_scale(c: int, a: Matrix, r: int) -> Matrix:
    return tuple(
        tuple(c * a[i][j] % r for j in range(2)) for i in range(2)
    )  # type: ignore[return-value]


def mat_mul(a: Matrix, b: Matrix, r: int) -> Matrix:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) % r for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def mat_adj(a: Matrix, r: int) -> Matrix:
    return ((a[1][1] % r, -a[0][1] % r), (-a[1][0] % r, a[0][0] % r))


def mat_det(a: Matrix, r: int) -> int:
    return (a[0][0] * a[1][1] - a[0][1] * a[1][0]) % r


def mat_trace(a: Matrix, r: int) -> int:
    return (a[0][0] + a[1][1]) % r


def zero_matrix(a: Matrix) -> bool:
    return all(value == 0 for row in a for value in row)


def splitting_generators(r: int) -> tuple[Matrix, Matrix, Matrix, Matrix]:
    identity: Matrix = ((1, 0), (0, 1))
    i_matrix: Matrix = ((0, -1 % r), (1, 0))
    uv = next(
        (u, v)
        for u in range(r)
        for v in range(r)
        if (u * u + v * v + 1) % r == 0
    )
    u, v = uv
    j_matrix: Matrix = ((u, v), (v, -u % r))
    k_matrix = mat_mul(i_matrix, j_matrix, r)
    minus_identity = mat_scale(-1, identity, r)
    assert mat_mul(i_matrix, i_matrix, r) == minus_identity
    assert mat_mul(j_matrix, j_matrix, r) == minus_identity
    assert mat_mul(j_matrix, i_matrix, r) == mat_scale(-1, k_matrix, r)
    return identity, i_matrix, j_matrix, k_matrix


def quaternion_matrix(x: Quaternion, r: int) -> Matrix:
    basis = splitting_generators(r)
    answer: Matrix = ((0, 0), (0, 0))
    inv2 = pow(2, -1, r)
    for coefficient, generator in zip(x, basis, strict=True):
        answer = mat_add(answer, mat_scale(coefficient * inv2, generator, r), r)
    return answer


def canonical_line(vector: tuple[int, int], r: int) -> tuple[int, int]:
    assert vector != (0, 0)
    pivot = 0 if vector[0] % r else 1
    inverse = pow(vector[pivot] % r, -1, r)
    return vector[0] * inverse % r, vector[1] * inverse % r


def row_line(a: Matrix, r: int) -> tuple[int, int]:
    row = a[0] if a[0] != (0, 0) else a[1]
    return canonical_line(row, r)


def image_line(a: Matrix, r: int) -> tuple[int, int]:
    first = (a[0][0], a[1][0])
    column = first if first != (0, 0) else (a[0][1], a[1][1])
    return canonical_line(column, r)


def kernel_line(a: Matrix, r: int) -> tuple[int, int]:
    row = row_line(a, r)
    return canonical_line((-row[1] % r, row[0]), r)


def is_scalar(a: Matrix, r: int) -> bool:
    return a[0][1] % r == 0 and a[1][0] % r == 0 and (a[0][0] - a[1][1]) % r == 0


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def category_counts(
    values: list[Quaternion],
    local_keys: dict[int, list[tuple[int, int]]],
    primes: tuple[int, int],
) -> Counter[int]:
    counts: Counter[int] = Counter()
    p, q = primes
    for i in range(len(values)):
        for j in range(len(values)):
            category = 1
            if local_keys[p][i] == local_keys[p][j]:
                category *= p
            if local_keys[q][i] == local_keys[q][j]:
                category *= q
            counts[category] += 1
    return counts


def divisor_signatures(
    values: list[Quaternion], divisors: list[Quaternion], r: int, handedness: str
) -> list[frozenset[Quaternion]]:
    signatures = []
    for alpha in values:
        current = set()
        for divisor in divisors:
            if handedness == "right":
                numerator = multiply(alpha, conjugate(divisor))
            else:
                numerator = multiply(conjugate(divisor), alpha)
            if all(coordinate % r == 0 for coordinate in numerator):
                quotient = tuple(coordinate // r for coordinate in numerator)
                assert len({coordinate & 1 for coordinate in quotient}) == 1
                current.add(divisor)
        signatures.append(frozenset(current))
    return signatures


def assert_signature_matches_line(
    signatures: list[frozenset[Quaternion]], lines: list[tuple[int, int]]
) -> dict[str, int]:
    line_to_signature: dict[tuple[int, int], frozenset[Quaternion]] = {}
    signature_to_line: dict[frozenset[Quaternion], tuple[int, int]] = {}
    for signature, line in zip(signatures, lines, strict=True):
        assert signature
        if line in line_to_signature:
            assert line_to_signature[line] == signature
        else:
            line_to_signature[line] = signature
        if signature in signature_to_line:
            assert signature_to_line[signature] == line
        else:
            signature_to_line[signature] = line
    return {
        "distinct_signatures": len(signature_to_line),
        "divisors_per_signature": len(next(iter(signature_to_line))),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    p, q, n = 3, 5, 15
    primes = (p, q)
    values = elements_norm(n)
    units = elements_norm(1)
    assert len(units) == 24
    assert len(values) == 24 * (p + 1) * (q + 1) == 576

    matrices = {r: [quaternion_matrix(alpha, r) for alpha in values] for r in primes}
    rows = {r: [row_line(a, r) for a in matrices[r]] for r in primes}
    images = {r: [image_line(a, r) for a in matrices[r]] for r in primes}
    kernels = {r: [kernel_line(a, r) for a in matrices[r]] for r in primes}

    for r in primes:
        for alpha, matrix in zip(values, matrices[r], strict=True):
            assert mat_det(matrix, r) == norm(alpha) % r == 0
            assert not zero_matrix(matrix)
            assert quaternion_matrix(conjugate(alpha), r) == mat_adj(matrix, r)

    row_fibres = Counter(zip(rows[p], rows[q], strict=True))
    image_fibres = Counter(zip(images[p], images[q], strict=True))
    assert len(row_fibres) == (p + 1) * (q + 1)
    assert len(image_fibres) == (p + 1) * (q + 1)
    assert set(row_fibres.values()) == {24}
    assert set(image_fibres.values()) == {24}

    value_set = set(values)
    for index, alpha in enumerate(values):
        left_orbit = {multiply(unit, alpha) for unit in units}
        right_orbit = {multiply(alpha, unit) for unit in units}
        assert len(left_orbit) == len(right_orbit) == 24
        assert left_orbit <= value_set and right_orbit <= value_set
        assert left_orbit == {
            beta
            for beta, rp, rq in zip(values, rows[p], rows[q], strict=True)
            if (rp, rq) == (rows[p][index], rows[q][index])
        }
        assert right_orbit == {
            beta
            for beta, ip, iq in zip(values, images[p], images[q], strict=True)
            if (ip, iq) == (images[p][index], images[q][index])
        }

    expected_probabilities = {
        1: Fraction(p * q, (p + 1) * (q + 1)),
        p: Fraction(q, (p + 1) * (q + 1)),
        q: Fraction(p, (p + 1) * (q + 1)),
        n: Fraction(1, (p + 1) * (q + 1)),
    }
    right_counts = category_counts(values, rows, primes)
    left_counts = category_counts(values, images, primes)
    total_pairs = len(values) ** 2
    assert right_counts == left_counts
    assert all(Fraction(right_counts[key], total_pairs) == value for key, value in expected_probabilities.items())

    divisor_audit: dict[str, dict[str, dict[str, int]]] = {"right": {}, "left": {}}
    for r in primes:
        divisors = elements_norm(r)
        for handedness, lines in (("right", rows[r]), ("left", images[r])):
            signatures = divisor_signatures(values, divisors, r, handedness)
            divisor_audit[handedness][str(r)] = assert_signature_matches_line(signatures, lines)

    product_counts: Counter[int] = Counter()
    for a_index in range(len(values)):
        for b_index in range(len(values)):
            category = 1
            for r in primes:
                product_matrix = mat_mul(matrices[r][a_index], matrices[r][b_index], r)
                zero = zero_matrix(product_matrix)
                assert zero == (images[r][b_index] == kernels[r][a_index])
                if zero:
                    category *= r
            product_counts[category] += 1
    assert product_counts == right_counts

    self_conjugation_counts: Counter[int] = Counter()
    for index, alpha in enumerate(values):
        trace = alpha[0]
        category = 1
        for r in primes:
            matrix = matrices[r][index]
            right_equal = row_line(matrix, r) == row_line(mat_adj(matrix, r), r)
            left_equal = image_line(matrix, r) == image_line(mat_adj(matrix, r), r)
            assert right_equal == left_equal == (trace % r == 0)
            if right_equal:
                category *= r
        assert math.gcd(abs(trace), n) == category
        self_conjugation_counts[category] += 1

    one: Quaternion = (2, 0, 0, 0)
    fixed_right_multipliers: dict[str, Quaternion] = {
        "nonscalar_both_1_plus_i": (2, 2, 0, 0),
        "scalar_mod_3_only_2_plus_3i": (4, 6, 0, 0),
        "scalar_mod_15_1_plus_15i": (2, 30, 0, 0),
    }
    fixed_transform_audit = {}
    for name, multiplier in fixed_right_multipliers.items():
        assert math.gcd(norm(multiplier), n) == 1
        local = {}
        for r in primes:
            b_matrix = quaternion_matrix(multiplier, r)
            fixed_lines = {
                rows[r][index]
                for index, matrix in enumerate(matrices[r])
                if row_line(mat_mul(matrix, b_matrix, r), r) == rows[r][index]
            }
            scalar = is_scalar(b_matrix, r)
            assert len(fixed_lines) == (r + 1 if scalar else len(fixed_lines))
            if not scalar:
                assert len(fixed_lines) <= 2
            local[str(r)] = {"scalar": scalar, "fixed_projective_lines": len(fixed_lines)}
        tracefree_gcd = math.gcd(n, multiplier[1], multiplier[2], multiplier[3])
        fixed_transform_audit[name] = {
            "norm": norm(multiplier),
            "tracefree_numerator_gcd": tracefree_gcd,
            "local": local,
        }
    assert fixed_transform_audit["scalar_mod_3_only_2_plus_3i"]["tracefree_numerator_gcd"] == 3
    assert fixed_transform_audit["scalar_mod_15_1_plus_15i"]["tracefree_numerator_gcd"] == 15

    mixed_multipliers = (elements_norm(1)[:4] + elements_norm(2)[:4])
    mixed_checks = 0
    mixed_asymmetric_checks = 0
    for b in mixed_multipliers:
        for c in mixed_multipliers:
            assert math.gcd(norm(b) * norm(c), n) == 1
            global_scalars = []
            for alpha in values:
                scalar = multiply(multiply(b, conjugate(c)), alpha)[0]
                global_scalars.append(scalar)
            for index, alpha in enumerate(values):
                collision_primes = []
                for r in primes:
                    a_matrix = matrices[r][index]
                    b_matrix = quaternion_matrix(b, r)
                    c_matrix = quaternion_matrix(c, r)
                    x_matrix = mat_mul(a_matrix, b_matrix, r)
                    y_matrix = mat_mul(mat_adj(a_matrix, r), c_matrix, r)
                    equality = row_line(x_matrix, r) == row_line(y_matrix, r)
                    t_matrix = mat_mul(b_matrix, mat_adj(c_matrix, r), r)
                    linear_zero = mat_trace(mat_mul(t_matrix, a_matrix, r), r) == 0
                    assert equality == linear_zero == (global_scalars[index] % r == 0)
                    if equality:
                        collision_primes.append(r)
                    mixed_checks += 1
                if len(collision_primes) == 1:
                    assert math.gcd(abs(global_scalars[index]), n) == collision_primes[0]
                    mixed_asymmetric_checks += 1

    extension_counts = {str(m): len(elements_norm(m)) for m in (2, 6, 9)}
    assert extension_counts == {"2": 24, "6": 96, "9": 312}
    assert extension_counts["6"] != 24 * (2 + 1) * (3 + 1)
    assert extension_counts["9"] != 24 * (3 + 1) ** 2

    mod_two_residues = []
    for coefficients in product(range(2), repeat=4):
        x0, x1, x2, x3 = coefficients
        representative = (2 * x0 + x3, 2 * x1 + x3, 2 * x2 + x3, x3)
        mod_two_residues.append((coefficients, norm(representative) % 2))
    hurwitz_mod_two_units = sum(norm_parity for _, norm_parity in mod_two_residues)
    gl2_f2_units = 6
    assert hurwitz_mod_two_units == 12
    assert hurwitz_mod_two_units != gl2_f2_units

    result = {
        "run": "F15-A01",
        "status": "PASS",
        "source_sha256": source_hash,
        "hurwitz_normalization": "(a+b*i+c*j+d*k)/2 with a,b,c,d of one parity",
        "p3_edge": {
            "N": n,
            "primes": list(primes),
            "S_N_size": len(values),
            "left_units": len(units),
            "row_orientation_pairs": len(row_fibres),
            "image_orientation_pairs": len(image_fibres),
            "orientation_fibre_size": sorted(set(row_fibres.values())),
            "ordered_pair_counts": {str(key): right_counts[key] for key in sorted(right_counts)},
            "probabilities": {
                str(key): fraction_text(expected_probabilities[key]) for key in sorted(expected_probabilities)
            },
            "proper_probability": fraction_text(expected_probabilities[p] + expected_probabilities[q]),
            "direct_product_counts": {str(key): product_counts[key] for key in sorted(product_counts)},
            "self_conjugation_gcd_counts": {
                str(key): self_conjugation_counts[key] for key in sorted(self_conjugation_counts)
            },
        },
        "direct_divisor_handedness": divisor_audit,
        "fixed_transform_checks": fixed_transform_audit,
        "mixed_barred_unbarred": {
            "multipliers": len(mixed_multipliers),
            "local_equivalences_checked": mixed_checks,
            "asymmetric_scalar_gcds_checked": mixed_asymmetric_checks,
        },
        "non_extension_certificates": {
            "norm_set_sizes": extension_counts,
            "naive_S_6_product_formula": 24 * (2 + 1) * (3 + 1),
            "naive_S_9_product_formula": 24 * (3 + 1) ** 2,
            "units_in_H_mod_2": hurwitz_mod_two_units,
            "units_in_M2_F2": gl2_f2_units,
        },
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"F15-A01 PASS: wrote {output}")


if __name__ == "__main__":
    main()
