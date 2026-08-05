#!/usr/bin/env sage

"""Independent hostile audit of F10/X11 cubic automorphism claims."""

import argparse
import json
from collections import Counter
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path


FAMILY_ID = "F10-aut-audit"


argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("--run-id", required=True)
arguments = argument_parser.parse_args()
RUN_ID = arguments.run_id


def integer_discriminant(coefficients):
    u, v, w = coefficients
    return u * u * v * v - 4 * v**3 - 4 * u**3 * w - 27 * w * w + 18 * u * v * w


def cubic_type(coefficients, prime):
    if integer_discriminant(coefficients) % prime == 0:
        return "non-squarefree"
    u, v, w = coefficients
    roots = sum((r**3 + u * r**2 + v * r + w) % prime == 0 for r in range(prime))
    return {0: "3", 1: "12", 3: "111"}[roots]


def polynomial_automorphisms(modulus, coefficients):
    coefficient_ring = Integers(modulus)
    polynomial_ring = PolynomialRing(coefficient_ring, "x")
    x = polynomial_ring.gen()
    u, v, w = map(coefficient_ring, coefficients)
    defining_polynomial = x**3 + u * x**2 + v * x + w
    records = []

    for a, b, c in product(range(modulus), repeat=3):
        image = coefficient_ring(a) + coefficient_ring(b) * x + coefficient_ring(c) * x**2
        image_squared = (image**2) % defining_polynomial
        relation = (image**3 + u * image_squared + v * image + w) % defining_polynomial
        if relation != 0:
            continue

        basis_matrix = Matrix(
            coefficient_ring,
            [
                [1, image[0], image_squared[0]],
                [0, image[1], image_squared[1]],
                [0, image[2], image_squared[2]],
            ],
        )
        determinant = int(basis_matrix.det())
        if gcd(determinant, modulus) != 1:
            continue

        current = x
        order = None
        for candidate_order in range(1, 7):
            current = current(image) % defining_polynomial
            if current == x:
                order = candidate_order
                break
        assert order is not None
        records.append(
            {
                "image": [a, b, c],
                "order": order,
                "determinant_modulus": determinant,
                "gcds_from_identity": [gcd(a, modulus), gcd((b - 1) % modulus, modulus), gcd(c, modulus)],
            }
        )
    return records


def characteristic_three_scheme_stats(coefficients, exponent):
    field = GF(3)
    parameter_ring = PolynomialRing(field, names=("a", "b", "c", "z"), order="degrevlex")
    a, b, c, z = parameter_ring.gens()
    polynomial_ring = PolynomialRing(parameter_ring, "x")
    x = polynomial_ring.gen()
    u, v, w = map(field, coefficients)
    defining_polynomial = x**3 + u * x**2 + v * x + w
    image = a + b * x + c * x**2
    image_squared = (image**2) % defining_polynomial
    relation = (image**3 + u * image_squared + v * image + w) % defining_polynomial
    basis_matrix = Matrix(
        parameter_ring,
        [
            [1, image[0], image_squared[0]],
            [0, image[1], image_squared[1]],
            [0, image[2], image_squared[2]],
        ],
    )
    determinant = basis_matrix.det()

    iterate = x
    for _ in range(exponent):
        iterate = iterate(image) % defining_polynomial
    order_relation = iterate - x
    equations = [relation[i] for i in range(3)]
    equations.extend(order_relation[i] for i in range(3))
    equations.append(z * determinant - 1)
    ideal = parameter_ring.ideal(equations)
    local_records = polynomial_automorphisms(3, coefficients)
    rational_count = sum(exponent % record["order"] == 0 for record in local_records)
    return {
        "krull_dimension": int(ideal.dimension()),
        "geometric_rank": int(ideal.vector_space_dimension()),
        "is_radical": ideal.radical() == ideal,
        "rational_point_count": rational_count,
    }


def conjugation_orbit_lengths(group, frobenius, subset):
    unseen = set(subset)
    lengths = []
    while unseen:
        start = unseen.pop()
        orbit = {start}
        current = frobenius * start * frobenius**-1
        while current not in orbit:
            orbit.add(current)
            unseen.discard(current)
            current = frobenius * current * frobenius**-1
        lengths.append(len(orbit))
    return sorted(lengths)


def main():
    checks = {}

    symbolic_ring = PolynomialRing(ZZ, names=("u", "v", "w", "a", "b", "c"))
    u, v, w, a, b, c = symbolic_ring.gens()
    polynomial_ring = PolynomialRing(symbolic_ring, "X")
    X = polynomial_ring.gen()
    defining_polynomial = X**3 + u * X**2 + v * X + w
    image = a + b * X + c * X**2
    image_squared = (image**2) % defining_polynomial
    image_cubed = (image**3) % defining_polynomial

    expected_squared = (
        a**2 - 2 * w * b * c + u * w * c**2,
        2 * a * b - 2 * v * b * c + (u * v - w) * c**2,
        b**2 + 2 * a * c - 2 * u * b * c + (u**2 - v) * c**2,
    )
    assert all(image_squared[i] == expected_squared[i] for i in range(3))

    D0, D1, D2 = expected_squared
    expected_cubed = (
        a * D0 - w * (b * D2 + c * D1) + u * w * c * D2,
        a * D1 + b * D0 - v * (b * D2 + c * D1) + (u * v - w) * c * D2,
        a * D2 + b * D1 + c * D0 - u * (b * D2 + c * D1) + (u**2 - v) * c * D2,
    )
    assert all(image_cubed[i] == expected_cubed[i] for i in range(3))

    endomorphism_equations = tuple(
        image_cubed[i] + u * image_squared[i] + v * image[i] + (w if i == 0 else 0)
        for i in range(3)
    )
    expected_endomorphism_equations = (
        expected_cubed[0] + u * D0 + v * a + w,
        expected_cubed[1] + u * D1 + v * b,
        expected_cubed[2] + u * D2 + v * c,
    )
    assert all(endomorphism_equations[i] == expected_endomorphism_equations[i] for i in range(3))

    determinant = Matrix(
        symbolic_ring,
        [
            [1, image[0], image_squared[0]],
            [0, image[1], image_squared[1]],
            [0, image[2], image_squared[2]],
        ],
    ).det()
    expected_determinant = b**3 - 2 * u * b**2 * c + (u**2 + v) * b * c**2 - (u * v - w) * c**3
    assert determinant == b * D2 - c * D1 == expected_determinant

    sigma_squared = (a + b * image + c * image_squared) % defining_polynomial
    Q0, Q1, Q2 = a + a * b + c * D0, b**2 + c * D1, b * c + c * D2
    assert all(sigma_squared[i] == (Q0, Q1, Q2)[i] for i in range(3))
    sigma_cubed = (Q0 + Q1 * image + Q2 * image_squared) % defining_polynomial
    expected_sigma_cubed = (
        Q0 + a * Q1 + D0 * Q2,
        b * Q1 + D1 * Q2,
        c * Q1 + D2 * Q2,
    )
    assert all(sigma_cubed[i] == expected_sigma_cubed[i] for i in range(3))

    canonical_output_path = Path("experiments/F10_autkill/output/R06.json")
    canonical_output = json.loads(canonical_output_path.read_text())
    artifact_equations = canonical_output["symbolic_equations"]
    assert all(symbolic_ring(artifact_equations["y_squared"][i]) == image_squared[i] for i in range(3))
    assert all(
        symbolic_ring(artifact_equations["f_of_y_coefficients"][i]) == endomorphism_equations[i]
        for i in range(3)
    )
    assert all(
        symbolic_ring(artifact_equations["sigma2_minus_x"][i]) == sigma_squared[i] - (1 if i == 1 else 0)
        for i in range(3)
    )
    assert all(
        symbolic_ring(artifact_equations["sigma3_minus_x"][i]) == sigma_cubed[i] - (1 if i == 1 else 0)
        for i in range(3)
    )
    assert symbolic_ring(artifact_equations["determinant"]) == determinant
    checks["all_compact_and_expanded_coefficient_equations"] = True
    checks["canonical_R06_sha256"] = sha256(canonical_output_path.read_bytes()).hexdigest()

    type_count_records = {}
    for prime in (3, 5, 7, 11):
        counts = Counter(cubic_type(coefficients, prime) for coefficients in product(range(prime), repeat=3))
        expected_counts = {
            "111": prime * (prime - 1) * (prime - 2) // 6,
            "12": prime**2 * (prime - 1) // 2,
            "3": (prime**3 - prime) // 3,
            "non-squarefree": prime**2,
        }
        assert dict(counts) == expected_counts
        for coefficients in product(range(prime), repeat=3):
            factor_type = cubic_type(coefficients, prime)
            if factor_type == "non-squarefree":
                continue
            discriminant = integer_discriminant(coefficients) % prime
            character = 1 if power_mod(discriminant, (prime - 1) // 2, prime) == 1 else -1
            assert (character == -1) == (factor_type == "12")
        type_count_records[str(prime)] = {
            "raw_counts": dict(sorted(counts.items())),
            "conditional_probabilities": {
                "111": str(QQ(expected_counts["111"]) / (prime**2 * (prime - 1))),
                "12": str(QQ(expected_counts["12"]) / (prime**2 * (prime - 1))),
                "3": str(QQ(expected_counts["3"]) / (prime**2 * (prime - 1))),
            },
        }
    checks["type_counts_and_discriminant_character"] = type_count_records

    p, q = 3, 5
    squarefree_p, squarefree_q = p**2 * (p - 1), q**2 * (q - 1)
    type3_p, type3_q = (p**3 - p) // 3, (q**3 - q) // 3
    order2_p, order2_q = squarefree_p - type3_p, squarefree_q - type3_q
    conditional_order2 = QQ(order2_p * type3_q + type3_p * order2_q) / (squarefree_p * squarefree_q)
    raw_order2 = QQ(order2_p * type3_q + type3_p * order2_q) / (p**3 * q**3)
    formula_conditional_order2 = QQ(4 * p * q + p + q - 2) / (9 * p * q)
    formula_raw_order2 = QQ((p - 1) * (q - 1) * (4 * p * q + p + q - 2)) / (9 * p**2 * q**2)
    assert conditional_order2 == formula_conditional_order2
    assert raw_order2 == formula_raw_order2

    order3_positive_p = squarefree_p // 2
    order3_positive_q = squarefree_q // 2
    order3_negative_p = squarefree_p // 2
    order3_negative_q = squarefree_q // 2
    conditional_order3 = QQ(
        order3_positive_p * order3_negative_q + order3_negative_p * order3_positive_q
    ) / (squarefree_p * squarefree_q)
    raw_order3 = QQ(
        order3_positive_p * order3_negative_q + order3_negative_p * order3_positive_q
    ) / (p**3 * q**3)
    assert conditional_order3 == QQ(1) / 2
    assert raw_order3 == QQ((p - 1) * (q - 1)) / (2 * p * q)
    checks["mismatch_probabilities_p3_q5"] = {
        "order2_conditional": str(conditional_order2),
        "order2_raw": str(raw_order2),
        "order3_conditional": str(conditional_order3),
        "order3_raw": str(raw_order3),
        "order3_expected_raw_trials": str(1 / raw_order3),
    }

    group = SymmetricGroup(3)
    identity = group.one()
    transposition = next(element for element in group if element.order() == 2)
    three_cycle = next(element for element in group if element.order() == 3)
    order_loci = {
        2: [element for element in group if 2 % element.order() == 0],
        3: [element for element in group if 3 % element.order() == 0],
    }
    geometric_records = {}
    for factor_type, frobenius in (("111", identity), ("12", transposition), ("3", three_cycle)):
        geometric_records[factor_type] = {}
        for exponent in (2, 3):
            subset = order_loci[exponent]
            fixed_count = sum(frobenius * element * frobenius**-1 == element for element in subset)
            orbit_lengths = conjugation_orbit_lengths(group, frobenius, subset)
            geometric_records[factor_type][str(exponent)] = {
                "geometric_rank": len(subset),
                "rational_points": fixed_count,
                "descent_orbit_degrees": orbit_lengths,
            }
    assert [geometric_records[t]["3"]["geometric_rank"] for t in ("111", "12", "3")] == [3, 3, 3]
    assert [geometric_records[t]["3"]["rational_points"] for t in ("111", "12", "3")] == [3, 1, 3]
    assert [geometric_records[t]["2"]["geometric_rank"] for t in ("111", "12", "3")] == [4, 4, 4]
    assert [geometric_records[t]["2"]["rational_points"] for t in ("111", "12", "3")] == [4, 2, 1]
    checks["geometric_conjugation_orbits"] = geometric_records

    characteristic_three_representatives = {
        "111": (0, 2, 0),
        "12": (0, 1, 0),
        "3": (0, 2, 1),
    }
    characteristic_three_records = {}
    for factor_type, coefficients in characteristic_three_representatives.items():
        assert cubic_type(coefficients, 3) == factor_type
        characteristic_three_records[factor_type] = {
            "coefficients": list(coefficients),
            "order2_scheme": characteristic_three_scheme_stats(coefficients, 2),
            "order3_scheme": characteristic_three_scheme_stats(coefficients, 3),
        }
        assert characteristic_three_records[factor_type]["order2_scheme"]["geometric_rank"] == 4
        assert characteristic_three_records[factor_type]["order3_scheme"]["geometric_rank"] == 3
        assert characteristic_three_records[factor_type]["order2_scheme"]["is_radical"]
        assert characteristic_three_records[factor_type]["order3_scheme"]["is_radical"]
    checks["characteristic_three_coefficient_schemes"] = characteristic_three_records

    field_three = GF(3)
    polynomial_ring_three = PolynomialRing(field_three, "t")
    t = polynomial_ring_three.gen()
    split_polynomial = t**3 - t
    roots = [field_three(r) for r in range(3)]
    interpolated_cycle = polynomial_ring_three.zero()
    for index, root in enumerate(roots):
        basis = polynomial_ring_three.one()
        denominator = field_three.one()
        for other_index, other_root in enumerate(roots):
            if other_index == index:
                continue
            basis *= t - other_root
            denominator *= root - other_root
        interpolated_cycle += roots[(index + 1) % 3] * basis / denominator
    interpolated_cycle %= split_polynomial
    cycle_coefficients = [int(interpolated_cycle[i]) for i in range(3)]
    split_records = polynomial_automorphisms(3, (0, 2, 0))
    assert any(record["image"] == cycle_coefficients and record["order"] == 3 for record in split_records)

    interpolated_transposition = polynomial_ring_three.zero()
    transposition_targets = [roots[1], roots[0], roots[2]]
    for index, root in enumerate(roots):
        basis = polynomial_ring_three.one()
        denominator = field_three.one()
        for other_index, other_root in enumerate(roots):
            if other_index == index:
                continue
            basis *= t - other_root
            denominator *= root - other_root
        interpolated_transposition += transposition_targets[index] * basis / denominator
    interpolated_transposition %= split_polynomial
    transposition_coefficients = [int(interpolated_transposition[i]) for i in range(3)]
    assert any(record["image"] == transposition_coefficients and record["order"] == 2 for record in split_records)

    irreducible_polynomial = t**3 + 2 * t + 1
    frobenius_image = (t**3) % irreducible_polynomial
    frobenius_coefficients = [int(frobenius_image[i]) for i in range(3)]
    irreducible_records = polynomial_automorphisms(3, (0, 2, 1))
    assert any(record["image"] == frobenius_coefficients and record["order"] == 3 for record in irreducible_records)

    mixed_polynomial = t**3 + t
    mixed_frobenius_image = (t**3) % mixed_polynomial
    mixed_frobenius_coefficients = [int(mixed_frobenius_image[i]) for i in range(3)]
    mixed_records = polynomial_automorphisms(3, (0, 1, 0))
    assert any(record["image"] == mixed_frobenius_coefficients and record["order"] == 2 for record in mixed_records)
    checks["characteristic_three_reverse_constructions"] = {
        "split_111_interpolated_cycle": cycle_coefficients,
        "split_111_interpolated_transposition": transposition_coefficients,
        "irreducible_3_frobenius_image": frobenius_coefficients,
        "mixed_12_frobenius_image": mixed_frobenius_coefficients,
    }

    assert all(is_prime(prime) for prime in (3, 5, 7))
    first_n15 = next(
        coefficients
        for coefficients in product(range(15), repeat=3)
        if gcd(integer_discriminant(coefficients), 15) == 1
        and cubic_type(coefficients, 3) == "12"
        and cubic_type(coefficients, 5) == "3"
    )
    assert first_n15 == (0, 1, 1)
    n15_records = polynomial_automorphisms(15, (0, 1, 1))
    assert len(n15_records) == 6
    assert Counter(record["order"] for record in n15_records) == Counter({1: 1, 2: 1, 3: 2, 6: 2})
    n15_order_two = [record for record in n15_records if record["order"] == 2]
    n15_order_three = [record for record in n15_records if record["order"] == 3]
    assert [record["image"] for record in n15_order_two] == [[5, 11, 0]]
    assert [record["image"] for record in n15_order_three] == [[6, 1, 9], [9, 13, 6]]
    assert any(1 < value < 15 for value in n15_order_two[0]["gcds_from_identity"])
    assert all(any(1 < value < 15 for value in record["gcds_from_identity"]) for record in n15_order_three)
    checks["fresh_N15_gcd_audit"] = {
        "polynomial": "x^3 + x + 1",
        "local_types": [cubic_type((0, 1, 1), 3), cubic_type((0, 1, 1), 5)],
        "lexicographically_first_coefficients": list(first_n15),
        "global_automorphism_count": len(n15_records),
        "automorphisms": n15_records,
    }

    first_n35 = next(
        coefficients
        for coefficients in product(range(35), repeat=3)
        if gcd(integer_discriminant(coefficients), 35) == 1
        and cubic_type(coefficients, 5) == "12"
        and cubic_type(coefficients, 7) == "3"
    )
    assert first_n35 == (0, 0, 2)
    n35_records = polynomial_automorphisms(35, (0, 0, 2))
    assert len(n35_records) == 6
    assert Counter(record["order"] for record in n35_records) == Counter({1: 1, 2: 1, 3: 2, 6: 2})
    local_five_records = polynomial_automorphisms(5, (0, 0, 2))
    local_seven_records = polynomial_automorphisms(7, (0, 0, 2))
    assert len(local_five_records) == 2
    assert len(local_seven_records) == 3
    order_three_records = [record for record in n35_records if record["order"] == 3]
    assert [record["image"] for record in order_three_records] == [[0, 11, 0], [0, 16, 0]]
    assert all(5 in record["gcds_from_identity"] for record in order_three_records)
    scalar_cube_roots = [b for b in range(35) if (b**3 - 1) % 35 == 0]
    assert scalar_cube_roots == [1, 11, 16]
    checks["fresh_N35_certificate"] = {
        "polynomial": "x^3 + 2",
        "integer_discriminant": integer_discriminant((0, 0, 2)),
        "local_types": [cubic_type((0, 0, 2), 5), cubic_type((0, 0, 2), 7)],
        "lexicographically_first_coefficients": list(first_n35),
        "local_automorphism_counts": [len(local_five_records), len(local_seven_records)],
        "global_automorphism_count": len(n35_records),
        "order_histogram": dict(sorted(Counter(record["order"] for record in n35_records).items())),
        "automorphisms": n35_records,
        "scalar_cube_roots": scalar_cube_roots,
    }

    output = {
        "family_id": FAMILY_ID,
        "run_id": RUN_ID,
        "checks": checks,
    }
    output_path = Path(f"experiments/F10_aut_audit/output/{RUN_ID}.json")
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True, default=int) + "\n")
    print(
        json.dumps(
            {
                "family_id": FAMILY_ID,
                "run_id": RUN_ID,
                "status": "passed",
                "output": str(output_path),
                "fresh_N35_automorphisms": len(n35_records),
                "characteristic_three_scheme_checks": len(characteristic_three_records) * 2,
            },
            sort_keys=True,
            default=int,
        )
    )


if __name__ == "__main__":
    main()
