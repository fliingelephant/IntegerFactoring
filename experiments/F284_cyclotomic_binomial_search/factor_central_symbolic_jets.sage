#!/usr/bin/env sage

import argparse
import json
import platform
import time
from pathlib import Path

from sage.all import (
    PolynomialRing,
    QQ,
    ZZ,
    bernoulli,
    factorial,
    gcd,
    lcm,
    matrix,
    version as sage_version,
)


ORDER = 12
MAX_HANKEL_SIZE = 5


def coefficient_bits(coefficient):
    coefficient = QQ(coefficient)
    return {
        "numerator_bits": int(abs(coefficient.numerator()).nbits()),
        "denominator_bits": int(coefficient.denominator().nbits()),
    }


def power_sum_polynomial(limit, exponent, ring):
    """Return sum_{a=1}^limit a^exponent with exponent+1 power terms."""
    exponent = int(exponent)
    degree = exponent + 1
    point = ring(limit) + 1
    total = ring.zero()
    for index in range(degree):
        total += (
            bernoulli(index)
            * ZZ(factorial(degree) // (factorial(index) * factorial(degree - index)))
            * point ** (degree - index)
        )
    return ring(total / degree)


def log_jet_central(B, ring):
    coefficients = [ring.zero() for _ in range(ORDER + 1)]
    coefficients[1] = B ** 2 / 2
    for degree in range(2, ORDER + 1, 2):
        difference = (
            power_sum_polynomial(2 * B, degree, ring)
            - 2 * power_sum_polynomial(B, degree, ring)
        )
        coefficients[degree] = ring(
            bernoulli(degree) * difference / (degree * factorial(degree))
        )
    return coefficients


def exp_jet(log_coefficients, ring):
    coefficients = [ring.zero() for _ in range(ORDER + 1)]
    coefficients[0] = ring.one()
    for degree in range(1, ORDER + 1):
        coefficients[degree] = ring(
            sum(
                index * log_coefficients[index] * coefficients[degree - index]
                for index in range(1, degree + 1)
            )
            / degree
        )
    return coefficients


def polynomial_record(label, polynomial, ring):
    polynomial = ring(polynomial)
    coefficients = polynomial.list()
    common_denominator = ZZ.one()
    for coefficient in coefficients:
        common_denominator = lcm(common_denominator, coefficient.denominator())
    integer_numerator = ring(common_denominator * polynomial)
    integer_coefficients = [ZZ(value) for value in integer_numerator.list()]
    content = ZZ.zero()
    for value in integer_coefficients:
        content = gcd(content, abs(value))
    if polynomial:
        factorization = polynomial.factor()
        factor_data = {
            "unit": str(factorization.unit()),
            "factors": [
                {"factor": str(factor), "multiplicity": int(multiplicity)}
                for factor, multiplicity in factorization
            ],
            "display": str(factorization),
        }
    else:
        factor_data = {"unit": "0", "factors": [], "display": "0"}
    bit_data = [coefficient_bits(value) for value in coefficients]
    return {
        "label": label,
        "degree": int(polynomial.degree()) if polynomial else int(-1),
        "expanded": str(polynomial),
        "common_denominator": str(common_denominator),
        "common_denominator_bits": int(common_denominator.nbits()),
        "integer_numerator": str(integer_numerator),
        "integer_numerator_content": str(content),
        "max_coefficient_numerator_bits": max(
            (item["numerator_bits"] for item in bit_data), default=int(0)
        ),
        "max_coefficient_denominator_bits": max(
            (item["denominator_bits"] for item in bit_data), default=int(0)
        ),
        "factorization": factor_data,
    }


def write_text(path, coefficient_records, hankel_records, timings):
    lines = [
        "# F284 exact central Gaussian-jet factors",
        "",
        "All expressions are over QQ[B]. This is exact symbolic output, not a factoring claim.",
        "",
        "## Normalized exponential-jet coefficients",
        "",
    ]
    for record in coefficient_records:
        lines.extend([
            f"{record['label']} = {record['factorization']['display']}",
            f"  common denominator: {record['common_denominator']}",
            f"  degree: {record['degree']}",
            f"  maximum coefficient numerator bits: {record['max_coefficient_numerator_bits']}",
            "",
        ])
    lines.extend(["## Moment Hankel determinants", ""])
    for record in hankel_records:
        lines.extend([
            f"{record['label']} = {record['factorization']['display']}",
            f"  common denominator: {record['common_denominator']}",
            f"  degree: {record['degree']}",
            f"  maximum coefficient numerator bits: {record['max_coefficient_numerator_bits']}",
            "",
        ])
    lines.extend([
        "## Timings",
        "",
        *(f"{name}: {value:.9f} seconds" for name, value in timings.items()),
        "",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-output", required=True)
    parser.add_argument("--text-output", required=True)
    arguments = parser.parse_args()

    total_start = time.perf_counter()
    timings = {}
    ring = PolynomialRing(QQ, "B")
    B = ring.gen()

    stage = time.perf_counter()
    log_coefficients = log_jet_central(B, ring)
    coefficients = exp_jet(log_coefficients, ring)
    timings["jet_construction"] = time.perf_counter() - stage

    assert coefficients[1] == B ** 2 / 2
    assert coefficients[2] == B ** 2 * (3 * B ** 2 + 2 * B + 1) / 24
    assert coefficients[3] == B ** 4 * (B + 1) ** 2 / 48

    stage = time.perf_counter()
    coefficient_records = [
        polynomial_record(f"c_{degree}", coefficients[degree], ring)
        for degree in range(1, ORDER + 1)
    ]
    timings["coefficient_factorization"] = time.perf_counter() - stage

    moments = [ring(factorial(degree) * coefficients[degree]) for degree in range(ORDER + 1)]
    stage = time.perf_counter()
    hankel_records = []
    for size in range(1, MAX_HANKEL_SIZE + 1):
        hankel = matrix(ring, size, size, lambda row, column: moments[row + column])
        determinant = ring(hankel.det())
        hankel_records.append(
            polynomial_record(f"H_{size}=det(mu_(i+j))_{{i,j=0}}^{size - 1}", determinant, ring)
        )
    timings["hankel_determinants_and_factorization"] = time.perf_counter() - stage
    timings["total"] = time.perf_counter() - total_start

    result = {
        "all_assertions_passed": True,
        "environment": {
            "python": platform.python_version(),
            "sage": str(sage_version()),
            "platform": platform.platform(),
        },
        "ring": "QQ[B]",
        "jet_order": int(ORDER),
        "power_sum_method": "Bernoulli-polynomial formula with exponent+1 rational power terms",
        "sanity_checks": {
            "c_1": "B^2/2",
            "c_2": "B^2*(3*B^2+2*B+1)/24",
            "c_3": "B^4*(B+1)^2/48",
        },
        "log_coefficients": [
            polynomial_record(f"ell_{degree}", log_coefficients[degree], ring)
            for degree in range(1, ORDER + 1)
        ],
        "coefficients": coefficient_records,
        "moments": [
            polynomial_record(f"mu_{degree}", moments[degree], ring)
            for degree in range(0, 2 * MAX_HANKEL_SIZE - 1)
        ],
        "hankel_determinants": hankel_records,
        "timings_seconds": timings,
    }

    json_path = Path(arguments.json_output)
    text_path = Path(arguments.text_output)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    text_path.parent.mkdir(parents=True, exist_ok=True)
    json_temporary = json_path.with_suffix(json_path.suffix + ".tmp")
    text_temporary = text_path.with_suffix(text_path.suffix + ".tmp")
    json_temporary.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    write_text(text_temporary, coefficient_records, hankel_records, timings)
    json_temporary.replace(json_path)
    text_temporary.replace(text_path)
    print(json.dumps({
        "all_assertions_passed": True,
        "coefficient_count": len(coefficient_records),
        "hankel_count": len(hankel_records),
        "total_seconds": timings["total"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
