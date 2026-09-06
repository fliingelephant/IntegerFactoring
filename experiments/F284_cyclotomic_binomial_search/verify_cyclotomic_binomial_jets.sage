#!/usr/bin/env sage

import argparse
import json
import platform
import sys
import time
from pathlib import Path

from sage.all import (
    Integer,
    PolynomialRing,
    PowerSeriesRing,
    QQ,
    ZZ,
    bernoulli,
    binomial,
    cyclotomic_polynomial,
    factorial,
    version as sage_version,
)


ORDER = 12
MAX_M = 30
MAX_D = 12


def integer_bits(value):
    value = ZZ(value)
    return int(abs(value).nbits())


def rational_record(value):
    value = QQ(value)
    numerator = value.numerator()
    denominator = value.denominator()
    return {
        "value": str(value),
        "numerator_bits": integer_bits(numerator),
        "denominator": str(denominator),
        "denominator_bits": integer_bits(denominator),
    }


def power_sum_bernoulli(limit, exponent):
    """Return sum_{a=1}^limit a^exponent using exponent+1 terms."""
    limit = ZZ(limit)
    exponent = int(exponent)
    degree = exponent + 1
    point = limit + 1
    total = QQ.zero()
    # B_degree(point)-B_degree; the final Bernoulli term cancels.
    for index in range(degree):
        total += binomial(degree, index) * bernoulli(index) * point ** (degree - index)
    return QQ(total / degree)


def log_jet(m, k, order=ORDER):
    m = ZZ(m)
    k = ZZ(k)
    coefficients = [QQ.zero() for _ in range(order + 1)]
    coefficients[1] = QQ(k * (m - k)) / 2
    for degree in range(2, order + 1):
        if degree % 2:
            continue
        difference = (
            power_sum_bernoulli(m, degree)
            - power_sum_bernoulli(k, degree)
            - power_sum_bernoulli(m - k, degree)
        )
        coefficients[degree] = QQ(bernoulli(degree) * difference) / (
            degree * factorial(degree)
        )
    return coefficients


def exp_jet(log_coefficients):
    order = len(log_coefficients) - 1
    coefficients = [QQ.zero() for _ in range(order + 1)]
    coefficients[0] = QQ.one()
    for degree in range(1, order + 1):
        coefficients[degree] = QQ(
            sum(
                index * log_coefficients[index] * coefficients[degree - index]
                for index in range(1, degree + 1)
            )
        ) / degree
    return coefficients


def gaussian_table(max_m, polynomial_ring, q):
    rows = [[polynomial_ring.one()]]
    for m in range(1, max_m + 1):
        previous = rows[-1]
        row = [polynomial_ring.one()]
        for k in range(1, m):
            row.append(previous[k] + q ** (m - k) * previous[k - 1])
        row.append(polynomial_ring.one())
        rows.append(row)
    return rows


def verify_power_sums():
    checks = 0
    for limit in range(MAX_M + 1):
        for exponent in range(1, ORDER + 1):
            expected = ZZ(sum(ZZ(value) ** exponent for value in range(1, limit + 1)))
            observed = power_sum_bernoulli(limit, exponent)
            assert observed == expected, (limit, exponent, observed, expected)
            checks += 1
    return int(checks)


def verify_literal_jets(rows, q):
    series_ring = PowerSeriesRing(QQ, "z", default_prec=ORDER + 1)
    z = series_ring.gen()
    exp_z = z.exp()
    checks = 0
    max_degree = 0
    max_numerator_bits = 0
    max_denominator_bits = 0
    for m in range(MAX_M + 1):
        for k in range(m + 1):
            polynomial = rows[m][k]
            max_degree = max(max_degree, int(polynomial.degree()))
            assert polynomial(1) == binomial(m, k)
            literal = (polynomial(exp_z) / QQ(binomial(m, k))).add_bigoh(ORDER + 1)
            formula_log = log_jet(m, k)
            formula_coefficients = exp_jet(formula_log)
            formula = series_ring(
                sum(formula_coefficients[degree] * z ** degree for degree in range(ORDER + 1))
            ).add_bigoh(ORDER + 1)
            assert literal == formula, (m, k, literal, formula)
            literal_log = literal.log()
            for degree in range(1, ORDER + 1):
                assert literal_log[degree] == formula_log[degree], (
                    m,
                    k,
                    degree,
                    literal_log[degree],
                    formula_log[degree],
                )
            for coefficient in formula_coefficients:
                max_numerator_bits = max(
                    max_numerator_bits, integer_bits(coefficient.numerator())
                )
                max_denominator_bits = max(
                    max_denominator_bits, integer_bits(coefficient.denominator())
                )
            checks += 1
    return {
        "cases": int(checks),
        "max_polynomial_degree": int(max_degree),
        "max_coefficient_numerator_bits": int(max_numerator_bits),
        "max_coefficient_denominator_bits": int(max_denominator_bits),
    }


def verify_q_lucas(rows, polynomial_ring):
    checks = 0
    for d in range(1, MAX_D + 1):
        cyclotomic = polynomial_ring(cyclotomic_polynomial(d))
        for m in range(MAX_M + 1):
            upper_quotient, upper_remainder = divmod(m, d)
            for k in range(m + 1):
                lower_quotient, lower_remainder = divmod(k, d)
                left = rows[m][k] % cyclotomic
                if lower_remainder > upper_remainder:
                    right = polynomial_ring.zero()
                else:
                    right = (
                        ZZ(binomial(upper_quotient, lower_quotient))
                        * rows[upper_remainder][lower_remainder]
                    ) % cyclotomic
                assert left == right, (d, m, k, left, right)
                checks += 1
    return int(checks)


def remote_jet():
    b_value = ZZ(2) ** 512 + 12345
    log_coefficients = log_jet(2 * b_value, b_value)
    coefficients = exp_jet(log_coefficients)
    return {
        "B": str(b_value),
        "B_bits": integer_bits(b_value),
        "m": str(2 * b_value),
        "k": str(b_value),
        "order": int(ORDER),
        "materialized_literal_polynomial": False,
        "log_coefficients": [
            {"degree": int(degree), **rational_record(log_coefficients[degree])}
            for degree in range(1, ORDER + 1)
        ],
        "coefficients": [
            {"degree": int(degree), **rational_record(coefficients[degree])}
            for degree in range(ORDER + 1)
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()
    output_path = Path(arguments.output)

    total_start = time.perf_counter()
    timings = {}

    stage = time.perf_counter()
    power_sum_checks = verify_power_sums()
    timings["power_sum_checks_seconds"] = time.perf_counter() - stage

    stage = time.perf_counter()
    polynomial_ring = PolynomialRing(ZZ, "q")
    q = polynomial_ring.gen()
    rows = gaussian_table(MAX_M, polynomial_ring, q)
    timings["gaussian_table_seconds"] = time.perf_counter() - stage

    stage = time.perf_counter()
    literal_summary = verify_literal_jets(rows, q)
    timings["literal_jet_verification_seconds"] = time.perf_counter() - stage

    stage = time.perf_counter()
    q_lucas_checks = verify_q_lucas(rows, polynomial_ring)
    timings["q_lucas_verification_seconds"] = time.perf_counter() - stage

    stage = time.perf_counter()
    remote = remote_jet()
    timings["remote_jet_seconds"] = time.perf_counter() - stage
    timings["total_seconds"] = time.perf_counter() - total_start

    result = {
        "all_assertions_passed": True,
        "environment": {
            "python": platform.python_version(),
            "sage": str(sage_version()),
            "platform": platform.platform(),
        },
        "parameters": {
            "jet_order": int(ORDER),
            "literal_max_m": int(MAX_M),
            "q_lucas_max_d": int(MAX_D),
        },
        "power_sum_checks": power_sum_checks,
        "literal_jet_verification": literal_summary,
        "q_lucas_checks": q_lucas_checks,
        "remote_jet": remote,
        "timings_seconds": timings,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = output_path.with_suffix(output_path.suffix + ".tmp")
    temporary.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(output_path)
    print(json.dumps({
        "all_assertions_passed": True,
        "literal_cases": literal_summary["cases"],
        "q_lucas_checks": q_lucas_checks,
        "remote_B_bits": remote["B_bits"],
        "total_seconds": timings["total_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
