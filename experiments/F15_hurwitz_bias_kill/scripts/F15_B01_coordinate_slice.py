#!/usr/bin/env python3
"""Exact small checks for a nonuniform Hurwitz coordinate-slice sampler.

The unbounded claims in RESULT.md are proved there.  This script only checks the
small certificates: integer-shell orientation fibres, the adaptive Q8
canonicalization, and the 24-unit right-orbit postprocessing.
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
Line = tuple[int, int]
Matrix = tuple[tuple[int, int], tuple[int, int]]


def qmul(x: Quat, y: Quat) -> Quat:
    a, b, c, d = x
    e, f, g, h = y
    return (
        a * e - b * f - c * g - d * h,
        a * f + b * e + c * h - d * g,
        a * g - b * h + c * e + d * f,
        a * h + b * g - c * f + d * e,
    )


def qconj(x: Quat) -> Quat:
    a, b, c, d = x
    return (a, -b, -c, -d)


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


def q8_canonical(x: Quat) -> Quat:
    candidates: list[Quat] = []
    for left in Q8:
        for right in Q8:
            candidates.append(qmul(qmul(left, x), right))
            candidates.append(qmul(qmul(left, qconj(x)), right))
    return min(candidates)


def matmul(a: Matrix, b: Matrix, modulus: int) -> Matrix:
    return (
        (
            (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % modulus,
            (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % modulus,
        ),
        (
            (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % modulus,
            (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % modulus,
        ),
    )


def find_split(modulus: int) -> tuple[int, int]:
    squares: dict[int, int] = {}
    for y in range(modulus):
        squares.setdefault(y * y % modulus, y)
    for x in range(modulus):
        target = (-1 - x * x) % modulus
        if target in squares:
            return x, squares[target]
    raise AssertionError(f"no split parameters modulo {modulus}")


def split_basis(modulus: int) -> tuple[Matrix, Matrix, Matrix, Matrix]:
    x, y = find_split(modulus)
    one = ((1, 0), (0, 1))
    i_mat = ((0, 1), (-1 % modulus, 0))
    j_mat = ((x, y), (y, -x % modulus))
    k_mat = matmul(i_mat, j_mat, modulus)
    return one, i_mat, j_mat, k_mat


def qmatrix_from_doubled(q2: Quat, modulus: int, basis: tuple[Matrix, ...]) -> Matrix:
    inv2 = pow(2, -1, modulus)
    coeffs = [(entry * inv2) % modulus for entry in q2]
    return tuple(
        tuple(
            sum(coeffs[t] * basis[t][row][col] for t in range(4)) % modulus
            for col in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def qmatrix_integral(q: Quat, modulus: int, basis: tuple[Matrix, ...]) -> Matrix:
    return qmatrix_from_doubled(tuple(2 * x for x in q), modulus, basis)


def row_line(matrix: Matrix, modulus: int) -> Line:
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % modulus
    if det != 0 or matrix == ((0, 0), (0, 0)):
        raise AssertionError(f"matrix is not nonzero rank one modulo {modulus}: {matrix}")
    row = matrix[0] if matrix[0] != (0, 0) else matrix[1]
    if row[0] != 0:
        inv = pow(row[0], -1, modulus)
        return (1, row[1] * inv % modulus)
    return (0, 1)


def right_action(line: Line, matrix: Matrix, modulus: int) -> Line:
    row = (
        (line[0] * matrix[0][0] + line[1] * matrix[1][0]) % modulus,
        (line[0] * matrix[0][1] + line[1] * matrix[1][1]) % modulus,
    )
    if row[0] != 0:
        inv = pow(row[0], -1, modulus)
        return (1, row[1] * inv % modulus)
    return (0, 1)


def integral_representations(n: int) -> list[Quat]:
    bound = isqrt(n)
    result: list[Quat] = []
    for a in range(-bound, bound + 1):
        rem_a = n - a * a
        if rem_a < 0:
            continue
        for b in range(-bound, bound + 1):
            rem_b = rem_a - b * b
            if rem_b < 0:
                continue
            for c in range(-bound, bound + 1):
                rem_c = rem_b - c * c
                if rem_c < 0:
                    continue
                d = isqrt(rem_c)
                if d * d != rem_c:
                    continue
                result.append((a, b, c, d))
                if d:
                    result.append((a, b, c, -d))
    return result


def orientation_counter(
    weighted_quaternions: Counter[Quat], p: int, q: int
) -> Counter[tuple[Line, Line]]:
    basis_p = split_basis(p)
    basis_q = split_basis(q)
    counter: Counter[tuple[Line, Line]] = Counter()
    for quat, weight in weighted_quaternions.items():
        lp = row_line(qmatrix_integral(quat, p, basis_p), p)
        lq = row_line(qmatrix_integral(quat, q, basis_q), q)
        counter[(lp, lq)] += weight
    return counter


def collision_table(counter: Counter[tuple[Line, Line]]) -> dict[str, object]:
    total = sum(counter.values())
    marginal_p: Counter[Line] = Counter()
    marginal_q: Counter[Line] = Counter()
    for (lp, lq), weight in counter.items():
        marginal_p[lp] += weight
        marginal_q[lq] += weight
    both = sum(weight * weight for weight in counter.values())
    at_p = sum(weight * weight for weight in marginal_p.values())
    at_q = sum(weight * weight for weight in marginal_q.values())
    denominator = total * total
    categories = {
        "1": denominator - at_p - at_q + both,
        "p": at_p - both,
        "q": at_q - both,
        "N": both,
    }
    return {
        "sample_mass": total,
        "support": len(counter),
        "p_marginal_support": len(marginal_p),
        "q_marginal_support": len(marginal_q),
        "ordered_pair_counts": categories,
        "ordered_pair_denominator": denominator,
        "proper_probability": str(Fraction(categories["p"] + categories["q"], denominator)),
        "max_p_atom": str(Fraction(max(marginal_p.values()), total)),
        "max_q_atom": str(Fraction(max(marginal_q.values()), total)),
    }


def projective_hurwitz_units(modulus: int, basis: tuple[Matrix, ...]) -> list[Matrix]:
    doubled_units: list[Quat] = [
        (2, 0, 0, 0),
        (0, 2, 0, 0),
        (0, 0, 2, 0),
        (0, 0, 0, 2),
    ]
    for si in (-1, 1):
        for sj in (-1, 1):
            for sk in (-1, 1):
                doubled_units.append((1, si, sj, sk))
    matrices = [qmatrix_from_doubled(unit, modulus, basis) for unit in doubled_units]
    if len(matrices) != 12:
        raise AssertionError("wrong projective unit count")
    return matrices


def unit_orbit_certificate(quat: Quat, p: int, q: int) -> dict[str, object]:
    basis_p = split_basis(p)
    basis_q = split_basis(q)
    lp = row_line(qmatrix_integral(quat, p, basis_p), p)
    lq = row_line(qmatrix_integral(quat, q, basis_q), q)
    units_p = projective_hurwitz_units(p, basis_p)
    units_q = projective_hurwitz_units(q, basis_q)
    stabilizer_p = [idx for idx, unit in enumerate(units_p) if right_action(lp, unit, p) == lp]
    stabilizer_q = [idx for idx, unit in enumerate(units_q) if right_action(lq, unit, q) == lq]
    categories = Counter()
    for up, uq in zip(units_p, units_q):
        for vp, vq in zip(units_p, units_q):
            equal_p = right_action(lp, up, p) == right_action(lp, vp, p)
            equal_q = right_action(lq, uq, q) == right_action(lq, vq, q)
            categories[(equal_p, equal_q)] += 1
    proper = categories[(True, False)] + categories[(False, True)]
    expected = len(stabilizer_p) + len(stabilizer_q) - 2 * len(set(stabilizer_p) & set(stabilizer_q))
    if proper != 12 * expected:
        raise AssertionError("unit-orbit stabilizer formula mismatch")
    return {
        "quaternion": list(quat),
        "row_line_p": list(lp),
        "row_line_q": list(lq),
        "stabilizer_p": stabilizer_p,
        "stabilizer_q": stabilizer_q,
        "ordered_unit_pair_counts": {
            "neither": categories[(False, False)],
            "p_only": categories[(True, False)],
            "q_only": categories[(False, True)],
            "both": categories[(True, True)],
        },
        "proper_probability": str(Fraction(proper, 144)),
    }


def analyze_pair(p: int, q: int) -> dict[str, object]:
    n = p * q
    reps = integral_representations(n)
    expected_count = 8 * (p + 1) * (q + 1)
    if len(reps) != expected_count:
        raise AssertionError((n, len(reps), expected_count))
    uniform_counter = orientation_counter(Counter(reps), p, q)
    if len(uniform_counter) != (p + 1) * (q + 1) or set(uniform_counter.values()) != {8}:
        raise AssertionError(f"integer-shell fibres failed at {n}")
    uniform_table = collision_table(uniform_counter)
    expected_categories = {
        "1": 64 * p * q * (p + 1) * (q + 1),
        "p": 64 * q * (p + 1) * (q + 1),
        "q": 64 * p * (p + 1) * (q + 1),
        "N": 64 * (p + 1) * (q + 1),
    }
    if uniform_table["ordered_pair_counts"] != expected_categories:
        raise AssertionError(f"uniform collision law failed at {n}")

    canonical_weights = Counter(q8_canonical(rep) for rep in reps)
    canonical_counter = orientation_counter(canonical_weights, p, q)
    canonical_table = collision_table(canonical_counter)
    bound_p = Fraction(128, p + 1)
    bound_q = Fraction(128, q + 1)
    if Fraction(canonical_table["max_p_atom"]) > bound_p:
        raise AssertionError("p atom exceeds finite-menu bound")
    if Fraction(canonical_table["max_q_atom"]) > bound_q:
        raise AssertionError("q atom exceeds finite-menu bound")

    partition_quat = min(tuple(sorted(abs(x) for x in rep)) for rep in reps)
    orbit = unit_orbit_certificate(partition_quat, p, q)
    return {
        "p": p,
        "q": q,
        "N": n,
        "integer_representation_count": len(reps),
        "orientation_fibre_count": 8,
        "uniform_integer_shell": uniform_table,
        "q8_canonicalized": {
            "output_support": len(canonical_weights),
            "largest_output_fibre": max(canonical_weights.values()),
            "collision": canonical_table,
            "proved_atom_bound_used": {"p": str(bound_p), "q": str(bound_q)},
        },
        "sorted_nonnegative_lex_first": orbit,
    }


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    source_path = Path(__file__)
    cases = [(3, 5), (3, 7), (5, 7), (5, 11), (7, 11), (7, 13), (11, 13)]
    analyses = [analyze_pair(p, q) for p, q in cases]

    scan: list[dict[str, object]] = []
    primes = [p for p in range(3, 32, 2) if is_prime(p)]
    for i, p in enumerate(primes):
        for q in primes[i + 1 :]:
            if p * q > 300:
                continue
            reps = integral_representations(p * q)
            partition_quat = min(tuple(sorted(abs(x) for x in rep)) for rep in reps)
            orbit = unit_orbit_certificate(partition_quat, p, q)
            scan.append(
                {
                    "N": p * q,
                    "p": p,
                    "q": q,
                    "quaternion": orbit["quaternion"],
                    "proper_probability": orbit["proper_probability"],
                }
            )
    scan.sort(key=lambda row: int(row["N"]))

    certificate = {
        "run": "F15-B01",
        "family": "F15_hurwitz_bias_kill",
        "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
        "status": "PASS",
        "cases": analyses,
        "lex_first_unit_orbit_scan_through_N_300": scan,
        "first_zero_orbit_case": next(row for row in scan if row["proper_probability"] == "0"),
        "first_positive_orbit_case": next(
            (row for row in scan if row["proper_probability"] != "0"), None
        ),
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": "PASS",
        "cases": len(analyses),
        "scan_cases": len(scan),
        "first_zero": certificate["first_zero_orbit_case"],
        "first_positive": certificate["first_positive_orbit_case"],
        "output": str(output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
