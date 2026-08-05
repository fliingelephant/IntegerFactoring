#!/usr/bin/env python3
"""Independent finite audit for F15 Hurwitz coordinate bias.

Family: F15_hurwitz_bias_audit.  This source imports no candidate code.  It
checks only finite certificates; the unbounded statements require proofs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from math import isqrt
from pathlib import Path


Quat = tuple[int, int, int, int]
Matrix = tuple[int, int, int, int]
Line = tuple[int, int]


def quat_mul(x: Quat, y: Quat) -> Quat:
    a, b, c, d = x
    e, f, g, h = y
    return (
        a * e - b * f - c * g - d * h,
        a * f + b * e + c * h - d * g,
        a * g - b * h + c * e + d * f,
        a * h + b * g - c * f + d * e,
    )


def quat_conj(x: Quat) -> Quat:
    return (x[0], -x[1], -x[2], -x[3])


def doubled_mul(x2: Quat, y2: Quat) -> Quat:
    raw = quat_mul(x2, y2)
    assert all(value % 2 == 0 for value in raw)
    return tuple(value // 2 for value in raw)  # type: ignore[return-value]


def hurwitz_shell_doubled(n: int) -> list[Quat]:
    bound = isqrt(4 * n)
    shell: list[Quat] = []
    for a in range(-bound, bound + 1):
        for b in range(-bound, bound + 1):
            for c in range(-bound, bound + 1):
                rem = 4 * n - a * a - b * b - c * c
                if rem < 0:
                    continue
                d = isqrt(rem)
                if d * d != rem:
                    continue
                for signed_d in ({0} if d == 0 else {d, -d}):
                    q2 = (a, b, c, signed_d)
                    if all(value % 2 == 0 for value in q2) or all(
                        value % 2 != 0 for value in q2
                    ):
                        shell.append(q2)
    return shell


def lipschitz_shell(n: int) -> list[Quat]:
    return [
        tuple(value // 2 for value in q2)  # type: ignore[misc]
        for q2 in hurwitz_shell_doubled(n)
        if all(value % 2 == 0 for value in q2)
    ]


def matrix_mul(a: Matrix, b: Matrix, modulus: int) -> Matrix:
    return (
        (a[0] * b[0] + a[1] * b[2]) % modulus,
        (a[0] * b[1] + a[1] * b[3]) % modulus,
        (a[2] * b[0] + a[3] * b[2]) % modulus,
        (a[2] * b[1] + a[3] * b[3]) % modulus,
    )


def split_basis(modulus: int) -> tuple[Matrix, Matrix, Matrix, Matrix]:
    uv = next(
        (u, v)
        for u in range(modulus)
        for v in range(modulus)
        if (u * u + v * v + 1) % modulus == 0
    )
    u, v = uv
    one = (1, 0, 0, 1)
    i_mat = (0, -1 % modulus, 1, 0)
    j_mat = (u, v, v, -u % modulus)
    k_mat = matrix_mul(i_mat, j_mat, modulus)
    assert matrix_mul(i_mat, i_mat, modulus) == (-1 % modulus, 0, 0, -1 % modulus)
    assert matrix_mul(j_mat, j_mat, modulus) == (-1 % modulus, 0, 0, -1 % modulus)
    return one, i_mat, j_mat, k_mat


def quaternion_matrix(q2: Quat, modulus: int, basis: tuple[Matrix, ...]) -> Matrix:
    inv2 = pow(2, -1, modulus)
    return tuple(
        sum(q2[t] * inv2 * basis[t][entry] for t in range(4)) % modulus
        for entry in range(4)
    )  # type: ignore[return-value]


def normalize_vector(vector: tuple[int, int], modulus: int) -> Line:
    if vector[0] % modulus:
        scale = pow(vector[0], -1, modulus)
        return (1, vector[1] * scale % modulus)
    assert vector[1] % modulus
    return (0, 1)


def row_line(matrix: Matrix, modulus: int) -> Line:
    det = (matrix[0] * matrix[3] - matrix[1] * matrix[2]) % modulus
    assert det == 0 and any(matrix)
    row = (matrix[0], matrix[1]) if (matrix[0], matrix[1]) != (0, 0) else (matrix[2], matrix[3])
    return normalize_vector(row, modulus)


def image_line(matrix: Matrix, modulus: int) -> Line:
    column = (matrix[0], matrix[2]) if (matrix[0], matrix[2]) != (0, 0) else (matrix[1], matrix[3])
    return normalize_vector(column, modulus)


def line_right_action(line: Line, matrix: Matrix, modulus: int) -> Line:
    return normalize_vector(
        (
            (line[0] * matrix[0] + line[1] * matrix[2]) % modulus,
            (line[0] * matrix[1] + line[1] * matrix[3]) % modulus,
        ),
        modulus,
    )


def projective_matrix(matrix: Matrix, modulus: int) -> Matrix:
    first = next(value for value in matrix if value % modulus)
    scale = pow(first, -1, modulus)
    return tuple(value * scale % modulus for value in matrix)  # type: ignore[return-value]


Q8: tuple[Quat, ...] = (
    (1, 0, 0, 0),
    (-1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, -1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, -1, 0),
    (0, 0, 0, 1),
    (0, 0, 0, -1),
)

UNITS2: tuple[Quat, ...] = tuple(
    [(2 * a, 2 * b, 2 * c, 2 * d) for a, b, c, d in Q8]
    + [
        (s0, s1, s2, s3)
        for s0 in (-1, 1)
        for s1 in (-1, 1)
        for s2 in (-1, 1)
        for s3 in (-1, 1)
    ]
)

PROJECTIVE_UNITS2: tuple[Quat, ...] = (
    (2, 0, 0, 0),
    (0, 2, 0, 0),
    (0, 0, 2, 0),
    (0, 0, 0, 2),
) + tuple(
    (1, s1, s2, s3)
    for s1 in (-1, 1)
    for s2 in (-1, 1)
    for s3 in (-1, 1)
)


def is_prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def semiprimes_through(limit: int) -> list[tuple[int, int]]:
    primes = [p for p in range(3, limit + 1, 2) if is_prime(p)]
    return sorted(
        ((p, q) for index, p in enumerate(primes) for q in primes[index + 1 :] if p * q <= limit),
        key=lambda pair: (pair[0] * pair[1], pair[0], pair[1]),
    )


def canonical_four_square(n: int) -> Quat:
    return min(tuple(sorted(abs(value) for value in q)) for q in lipschitz_shell(n))


def unit_orbit_certificate(alpha: Quat, p: int, q: int) -> dict[str, object]:
    bases = {r: split_basis(r) for r in (p, q)}
    lines = {
        r: row_line(quaternion_matrix(tuple(2 * value for value in alpha), r, bases[r]), r)
        for r in (p, q)
    }
    unit_matrices = {
        r: [quaternion_matrix(unit, r, bases[r]) for unit in PROJECTIVE_UNITS2]
        for r in (p, q)
    }
    stabilizers = {
        r: {
            index
            for index, matrix in enumerate(unit_matrices[r])
            if line_right_action(lines[r], matrix, r) == lines[r]
        }
        for r in (p, q)
    }
    direct = Counter()
    for u in range(12):
        for v in range(12):
            equal_p = line_right_action(lines[p], unit_matrices[p][u], p) == line_right_action(
                lines[p], unit_matrices[p][v], p
            )
            equal_q = line_right_action(lines[q], unit_matrices[q][u], q) == line_right_action(
                lines[q], unit_matrices[q][v], q
            )
            direct[(equal_p, equal_q)] += 1
    proper = direct[(True, False)] + direct[(False, True)]
    symmetric_difference = stabilizers[p] ^ stabilizers[q]
    assert proper == 12 * len(symmetric_difference)

    actual_orbit = [doubled_mul(tuple(2 * value for value in alpha), unit) for unit in UNITS2]
    divisor_checks: dict[int, bool] = {}
    for r in (p, q):
        divisors = hurwitz_shell_doubled(r)
        right_divisor_sets = []
        for x2 in actual_orbit:
            divisible = set()
            for index, divisor in enumerate(divisors):
                numerator2 = doubled_mul(x2, quat_conj(divisor))
                if all(value % r == 0 for value in numerator2):
                    quotient2 = tuple(value // r for value in numerator2)
                    if all(value % 2 == 0 for value in quotient2) or all(
                        value % 2 != 0 for value in quotient2
                    ):
                        divisible.add(index)
            right_divisor_sets.append(divisible)
        divisor_checks[r] = all(
            bool(right_divisor_sets[u] & right_divisor_sets[v])
            == (
                line_right_action(lines[r], unit_matrices[r][u // 2], r)
                == line_right_action(lines[r], unit_matrices[r][v // 2], r)
            )
            for u in range(24)
            for v in range(24)
        )
        # UNITS2 is ordered in +/- pairs for Q8 but not for half-units, so use
        # the abstract projective action directly for the definitive check below.
        divisor_checks[r] = all(
            bool(right_divisor_sets[u] & right_divisor_sets[v])
            == (
                row_line(quaternion_matrix(actual_orbit[u], r, bases[r]), r)
                == row_line(quaternion_matrix(actual_orbit[v], r, bases[r]), r)
            )
            for u in range(24)
            for v in range(24)
        )
        assert divisor_checks[r]

    return {
        "N": p * q,
        "p": p,
        "q": q,
        "alpha": list(alpha),
        "row_lines": {str(r): list(lines[r]) for r in (p, q)},
        "stabilizers": {str(r): sorted(stabilizers[r]) for r in (p, q)},
        "stabilizer_sizes": {str(r): len(stabilizers[r]) for r in (p, q)},
        "symmetric_difference_size": len(symmetric_difference),
        "proper_probability": str(Fraction(proper, 144)),
        "ordered_projective_pair_counts": {
            "neither": direct[(False, False)],
            "p_only": direct[(True, False)],
            "q_only": direct[(False, True)],
            "both": direct[(True, True)],
        },
        "right_divisor_direction_checked": {str(r): divisor_checks[r] for r in (p, q)},
    }


def q8_canonical(q: Quat) -> Quat:
    return min(
        quat_mul(quat_mul(left, source), right)
        for source in (q, quat_conj(q))
        for left in Q8
        for right in Q8
    )


def orientation_fibres(n: int, p: int, q: int) -> dict[str, object]:
    reps = lipschitz_shell(n)
    bases = {r: split_basis(r) for r in (p, q)}
    rows: Counter[tuple[Line, Line]] = Counter()
    images: Counter[tuple[Line, Line]] = Counter()
    for quat in reps:
        matrices = {
            r: quaternion_matrix(tuple(2 * value for value in quat), r, bases[r])
            for r in (p, q)
        }
        rows[(row_line(matrices[p], p), row_line(matrices[q], q))] += 1
        images[(image_line(matrices[p], p), image_line(matrices[q], q))] += 1
    assert set(rows.values()) == {8} and len(rows) == (p + 1) * (q + 1)
    assert set(images.values()) == {8} and len(images) == (p + 1) * (q + 1)

    integral_orbit_counts = []
    for quat in reps:
        q2 = tuple(2 * value for value in quat)
        left_orbit = {doubled_mul(unit, q2) for unit in UNITS2}
        right_orbit = {doubled_mul(q2, unit) for unit in UNITS2}
        assert len(left_orbit) == len(right_orbit) == 24
        integral_orbit_counts.append(
            (
                sum(all(value % 2 == 0 for value in item) for item in left_orbit),
                sum(all(value % 2 == 0 for value in item) for item in right_orbit),
            )
        )
    assert set(integral_orbit_counts) == {(8, 8)}
    return {
        "N": n,
        "representation_count": len(reps),
        "row_fibres": len(rows),
        "row_fibre_sizes": sorted(set(rows.values())),
        "image_fibres": len(images),
        "image_fibre_sizes": sorted(set(images.values())),
        "left_right_integral_orbit_counts": [8, 8],
    }


def sampler_certificate(n: int) -> dict[str, object]:
    bound = isqrt(n)
    emitted: Counter[Quat] = Counter()
    zero_cases = 0
    for a in range(-bound, bound + 1):
        for b in range(-bound, bound + 1):
            for c in range(-bound, bound + 1):
                remainder = n - a * a - b * b - c * c
                if remainder < 0:
                    continue
                d = isqrt(remainder)
                if d * d != remainder:
                    continue
                if d == 0:
                    zero_cases += 1
                    emitted[(a, b, c, 0)] += 1
                else:
                    emitted[(a, b, c, d)] += 1
                    emitted[(a, b, c, -d)] += 1
    reps = lipschitz_shell(n)
    assert emitted == Counter(reps) and set(emitted.values()) == {1}
    return {
        "N": n,
        "M": 2 * bound + 1,
        "d_zero_representations": zero_cases,
        "emitted_support": len(emitted),
        "per_representation_probability": str(Fraction(1, 2 * (2 * bound + 1) ** 3)),
        "acceptance_probability": str(Fraction(len(reps), 2 * (2 * bound + 1) ** 3)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate-output", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    candidate_output = Path(args.candidate_output)
    retained = json.loads(candidate_output.read_text())
    retained_pairs = {
        (int(row["p"]), int(row["q"]))
        for row in retained["lex_first_unit_orbit_scan_through_N_300"]
    }
    all_pairs = semiprimes_through(300)
    scan = [unit_orbit_certificate(canonical_four_square(p * q), p, q) for p, q in all_pairs]
    first_zero = next(row for row in scan if row["proper_probability"] == "0")

    faithfulness = {}
    for prime in sorted({prime for pair in all_pairs for prime in pair}):
        basis = split_basis(prime)
        projective_images = {
            projective_matrix(quaternion_matrix(unit, prime, basis), prime)
            for unit in PROJECTIVE_UNITS2
        }
        faithfulness[str(prime)] = len(projective_images)
        assert len(projective_images) == 12

    reps_15 = lipschitz_shell(15)
    canonical_weights = Counter(q8_canonical(quat) for quat in reps_15)
    assert sorted(canonical_weights.values()) == [64, 64, 64]
    basis_3, basis_5 = split_basis(3), split_basis(5)
    canonical_orientations = Counter(
        (
            row_line(quaternion_matrix(tuple(2 * value for value in quat), 3, basis_3), 3),
            row_line(quaternion_matrix(tuple(2 * value for value in quat), 5, basis_5), 5),
        )
        for quat in canonical_weights.elements()
    )
    marginal_3: Counter[Line] = Counter()
    marginal_5: Counter[Line] = Counter()
    for (line_3, line_5), weight in canonical_orientations.items():
        marginal_3[line_3] += weight
        marginal_5[line_5] += weight
    both = sum(weight * weight for weight in canonical_orientations.values())
    at_3 = sum(weight * weight for weight in marginal_3.values())
    at_5 = sum(weight * weight for weight in marginal_5.values())
    proper = at_3 + at_5 - 2 * both
    assert proper == 0

    result = {
        "run": "F15-BA01",
        "family": "F15_hurwitz_bias_audit",
        "status": "PASS",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "candidate_output_sha256": hashlib.sha256(candidate_output.read_bytes()).hexdigest(),
        "orientation_and_orbit_checks": [
            orientation_fibres(15, 3, 5),
            orientation_fibres(39, 3, 13),
        ],
        "rejection_sampler_checks": [sampler_certificate(15), sampler_certificate(21)],
        "unit_orbit_cases": [
            unit_orbit_certificate((1, 1, 2, 3), 3, 5),
            unit_orbit_certificate((1, 1, 1, 6), 3, 13),
        ],
        "q8_canonical_N15": {
            "weights": sorted(canonical_weights.values()),
            "proper_probability": str(Fraction(proper, len(reps_15) ** 2)),
        },
        "complete_semiprime_scan_through_300": {
            "case_count": len(all_pairs),
            "first_zero": first_zero,
            "zero_cases": [
                {key: row[key] for key in ("N", "p", "q", "alpha", "proper_probability")}
                for row in scan
                if row["proper_probability"] == "0"
            ],
        },
        "candidate_scan_coverage": {
            "retained_case_count": len(retained_pairs),
            "complete_case_count": len(all_pairs),
            "missing_pairs": [list(pair) for pair in all_pairs if pair not in retained_pairs],
            "extra_pairs": [list(pair) for pair in sorted(retained_pairs) if pair not in set(all_pairs)],
        },
        "projective_A4_image_sizes": faithfulness,
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "status": "PASS",
                "complete_scan_cases": len(all_pairs),
                "candidate_scan_cases": len(retained_pairs),
                "first_zero": {
                    key: first_zero[key]
                    for key in ("N", "p", "q", "alpha", "proper_probability")
                },
                "output": str(output),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
