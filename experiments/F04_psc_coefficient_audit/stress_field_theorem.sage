#!/usr/bin/env sage
"""Directly search for counterexamples to the fixed D_j degree-chain theorem."""

import argparse
import hashlib
import itertools
import json
from pathlib import Path
import time


def canonical_determinant(first, second, index):
    ring = first.parent()
    x = ring.gen()
    m = first.degree()
    n = second.degree()
    columns = [x**shift * first for shift in range(n - index)]
    columns += [x**shift * second for shift in range(m - index)]
    rows = range(index, m + n - index)
    return matrix(
        ring.base_ring(),
        [[polynomial[degree] for polynomial in columns] for degree in rows],
    ).det()


def monic_polynomials(ring, degree):
    field = ring.base_ring()
    x = ring.gen()
    for coefficients in itertools.product(field, repeat=degree):
        yield x**degree + ring(list(coefficients))


parser = argparse.ArgumentParser()
parser.add_argument("--output", required=True)
args = parser.parse_args()
started = time.monotonic()
case_count = 0
determinant_count = 0
abnormal_gap_cases = 0
positive_gcd_cases = 0
constant_second_cases = 0
first_counterexample = None
examples = {}

for characteristic, maximum_m in ((2, 5), (3, 4)):
    field = GF(characteristic)
    ring = PolynomialRing(field, "x")
    for m in range(1, maximum_m + 1):
        for n in range(m):
            for first in monic_polynomials(ring, m):
                for second in monic_polynomials(ring, n):
                    dividend = first
                    divisor = second
                    degrees = [int(first.degree()), int(second.degree())]
                    while divisor:
                        remainder = dividend % divisor
                        if remainder:
                            degrees.append(int(remainder.degree()))
                        dividend, divisor = divisor, remainder
                    determinants = [
                        canonical_determinant(first, second, index)
                        for index in range(n + 1)
                    ]
                    nonzero_indices = [
                        index for index, value in enumerate(determinants) if value
                    ]
                    expected = sorted(degrees[1:])
                    case_count += 1
                    determinant_count += n + 1
                    has_gap = any(
                        degrees[position] - degrees[position + 1] > 1
                        for position in range(1, len(degrees) - 1)
                    )
                    has_positive_gcd = degrees[-1] > 0
                    abnormal_gap_cases += int(has_gap)
                    positive_gcd_cases += int(has_positive_gcd)
                    constant_second_cases += int(n == 0)
                    assert determinants[n] == second[n] ** (m - n)
                    if has_gap and "abnormal_gap" not in examples:
                        examples["abnormal_gap"] = {
                            "field": int(characteristic),
                            "F": str(first),
                            "G": str(second),
                            "degrees": degrees,
                            "D": [int(value) for value in determinants],
                        }
                    if has_positive_gcd and "positive_gcd" not in examples:
                        examples["positive_gcd"] = {
                            "field": int(characteristic),
                            "F": str(first),
                            "G": str(second),
                            "degrees": degrees,
                            "D": [int(value) for value in determinants],
                        }
                    if nonzero_indices != expected:
                        first_counterexample = {
                            "field": int(characteristic),
                            "F": str(first),
                            "G": str(second),
                            "degrees": degrees,
                            "D": [int(value) for value in determinants],
                            "nonzero_indices": nonzero_indices,
                            "expected": expected,
                        }
                        break
                if first_counterexample:
                    break
            if first_counterexample:
                break
        if first_counterexample:
            break
    if first_counterexample:
        break

if first_counterexample:
    raise RuntimeError(json.dumps(first_counterexample, sort_keys=True))
assert abnormal_gap_cases > 0
assert positive_gcd_cases > 0
assert constant_second_cases > 0
source_path = Path(__file__).resolve().with_suffix("")
result = {
    "theorem_under_test": "D_j != 0 iff j is a nonzero Euclidean-remainder degree, including G",
    "normalization": "exhaustive monic inputs; nonzero rescaling preserves both degree chains and determinant vanishing",
    "fields_and_max_first_degree": {"2": int(5), "3": int(4)},
    "case_count": int(case_count),
    "direct_determinant_count": int(determinant_count),
    "abnormal_gap_case_count": int(abnormal_gap_cases),
    "positive_gcd_case_count": int(positive_gcd_cases),
    "constant_second_case_count": int(constant_second_cases),
    "top_formula_checked_every_case": True,
    "first_counterexample": None,
    "examples": examples,
    "elapsed_seconds": time.monotonic() - started,
    "source": str(source_path),
    "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
}
Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, sort_keys=True))
