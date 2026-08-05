#!/usr/bin/env sage
"""Check Sage subresultant residues against the fixed determinant, including signs."""

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
    return matrix(
        ring.base_ring(),
        [
            [polynomial[degree] for polynomial in columns]
            for degree in range(index, m + n - index)
        ],
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
residue_count = 0
gap_cases = 0
positive_gcd_cases = 0

for characteristic, maximum_m in ((2, 5), (3, 4)):
    field = GF(characteristic)
    ring = PolynomialRing(field, "x")
    for m in range(1, maximum_m + 1):
        for n in range(m):
            for monic_first in monic_polynomials(ring, m):
                for monic_second in monic_polynomials(ring, n):
                    for first_scale in field:
                        if not first_scale:
                            continue
                        for second_scale in field:
                            if not second_scale:
                                continue
                            first = first_scale * monic_first
                            second = second_scale * monic_second
                            direct = [
                                canonical_determinant(first, second, index)
                                for index in range(n + 1)
                            ]
                            gcd_degree = int(first.gcd(second).degree())
                            dividend = first
                            divisor = second
                            degrees = [m, n]
                            while divisor:
                                remainder = dividend % divisor
                                if remainder:
                                    degrees.append(int(remainder.degree()))
                                dividend, divisor = divisor, remainder
                            gap_cases += int(any(
                                degrees[position] - degrees[position + 1] > 1
                                for position in range(1, len(degrees) - 1)
                            ))
                            positive_gcd_cases += int(gcd_degree > 0)
                            if gcd_degree > 0:
                                continue
                            subresultants = first.subresultants(second)
                            reconstructed = [
                                subresultants[index][index] for index in range(n)
                            ]
                            reconstructed.append(second[n] ** (m - n))
                            assert direct == reconstructed
                            case_count += 1
                            residue_count += n + 1

source_path = Path(__file__).resolve().with_suffix("")
result = {
    "fixed_convention": "increasing output degrees; increasing F shifts followed by increasing G shifts",
    "coprime_case_count": int(case_count),
    "exact_residue_comparisons": int(residue_count),
    "internal_gap_cases": int(gap_cases),
    "positive_gcd_cases_excluded_from_sparse_sage_indexing": int(positive_gcd_cases),
    "all_coprime_direct_determinants_equal_sage_reconstruction": True,
    "top_formula_checked": "D_n=lc(G)^(m-n)",
    "elapsed_seconds": time.monotonic() - started,
    "source": str(source_path),
    "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
}
Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, sort_keys=True))
