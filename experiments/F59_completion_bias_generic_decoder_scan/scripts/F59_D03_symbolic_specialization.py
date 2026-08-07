import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

from sage.all import PolynomialRing, QQ


RUN = "F59-D03"
BASE = Path(__file__).resolve().parent.parent
INPUT = BASE / "output" / "F59-D02.json"
OUTPUT = BASE / "output" / f"{RUN}.json"
EXPECTED_INPUT_HASH = "23c1272fdaebfd932fb727b75d73e47f46b34a0d468b761c39956b9075073b6e"
SAGE_RING = PolynomialRing(QQ, "T")
SAGE_T = SAGE_RING.gen()


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def trim(polynomial):
    while len(polynomial) > 1 and polynomial[-1] == 0:
        polynomial.pop()
    return polynomial


def multiply(left, right):
    product = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_degree, left_coefficient in enumerate(left):
        for right_degree, right_coefficient in enumerate(right):
            product[left_degree + right_degree] += (
                left_coefficient * right_coefficient
            )
    return trim(product)


def evaluate(polynomial, value):
    result = Fraction(0)
    for coefficient in reversed(polynomial):
        result = result * value + coefficient
    return result


def sage_polynomial(polynomial):
    return SAGE_RING(
        sum(
            QQ(coefficient.numerator) / coefficient.denominator * SAGE_T**degree
            for degree, coefficient in enumerate(polynomial)
        )
    )


def lift_walk(modulus, start_offset, step_cap):
    state_value = modulus - start_offset
    state_affine = (Fraction(1), Fraction(-start_offset))
    records = []
    for step_index in range(step_cap):
        if state_value == 1 or math.gcd(state_value, modulus) != 1:
            break
        inverse_value = pow(state_value, -1, modulus)
        quotient_value = (state_value * inverse_value - 1) // modulus
        state_slope, state_constant = state_affine
        assert state_constant
        inverse_constant = 1 / state_constant
        inverse_slope = (Fraction(inverse_value) - inverse_constant) / modulus
        inverse_affine = (inverse_slope, inverse_constant)
        quotient_affine = (
            state_slope * inverse_slope,
            state_slope * inverse_constant + state_constant * inverse_slope,
        )
        state_polynomial = [state_constant, state_slope]
        inverse_polynomial = [inverse_constant, inverse_slope]
        relation_polynomial = multiply(state_polynomial, inverse_polynomial)
        assert relation_polynomial == trim(
            [Fraction(1), quotient_affine[1], quotient_affine[0]]
        )
        assert evaluate(state_polynomial, modulus) == state_value
        assert evaluate(inverse_polynomial, modulus) == inverse_value
        assert (
            quotient_affine[0] * modulus + quotient_affine[1]
            == quotient_value
        )
        records.append(
            {
                "start_offset": start_offset,
                "step_index": step_index,
                "u": state_value,
                "v": inverse_value,
                "k": quotient_value,
                "u_affine": state_affine,
                "v_affine": inverse_affine,
                "k_affine": quotient_affine,
                "A_polynomial": relation_polynomial,
            }
        )
        state_value = quotient_value
        state_affine = quotient_affine
    return records


def normalize_affine(affine):
    slope, constant = affine
    if slope == 0:
        return constant, None
    denominator = math.lcm(slope.denominator, constant.denominator)
    integer_slope = slope.numerator * (denominator // slope.denominator)
    integer_constant = constant.numerator * (denominator // constant.denominator)
    common = math.gcd(abs(integer_slope), abs(integer_constant))
    integer_slope //= common
    integer_constant //= common
    scalar = Fraction(common, denominator)
    if integer_slope < 0:
        integer_slope = -integer_slope
        integer_constant = -integer_constant
        scalar = -scalar
    return scalar, (integer_slope, integer_constant)


def is_fraction_square(value):
    if value < 0:
        return False
    numerator_root = math.isqrt(value.numerator)
    denominator_root = math.isqrt(value.denominator)
    return (
        numerator_root * numerator_root == value.numerator
        and denominator_root * denominator_root == value.denominator
    )


def fraction_square_root(value):
    assert is_fraction_square(value)
    return Fraction(math.isqrt(value.numerator), math.isqrt(value.denominator))


def polynomial_text(polynomial):
    return str(sage_polynomial(polynomial))


assert sha256(INPUT) == EXPECTED_INPUT_HASH
with INPUT.open("r", encoding="utf-8") as handle:
    payload = json.load(handle)
assert payload["run"] == "F59-D02"

per_input = []
certificate_results = []
discovery_triggers = []
for stored_input in payload["records"]:
    modulus = stored_input["N"]
    input_bits = stored_input["input_bits"]
    stored_batch = stored_input["full_offset_batch"]
    assert len(stored_batch["certificates"]) == stored_batch["kernel_dimension"]
    lifted_relations = {}
    symbolic_basis_count = 0
    symbolic_global_basis_count = 0
    for certificate_index, certificate in enumerate(stored_batch["certificates"]):
        polynomial_factor_counts = {}
        rational_unit = Fraction(1)
        exact_product = 1
        product_polynomial = [Fraction(1)]
        selected_provenance = []
        for stored_relation in certificate["selected_relations"]:
            provenance = (
                stored_relation["start_offset"],
                stored_relation["step_index"],
            )
            relation = lifted_relations.get(provenance)
            if relation is None:
                lifted = lift_walk(
                    modulus, provenance[0], provenance[1] + 1
                )
                assert len(lifted) == provenance[1] + 1
                relation = lifted[-1]
                relation["A"] = modulus * relation["k"] + 1
                lifted_relations[provenance] = relation
            for key in (
                "start_offset",
                "step_index",
                "u",
                "v",
                "k",
                "A",
            ):
                assert relation[key] == stored_relation[key]
            for affine in (relation["u_affine"], relation["v_affine"]):
                scalar, factor = normalize_affine(affine)
                rational_unit *= scalar
                if factor is not None:
                    polynomial_factor_counts[factor] = (
                        polynomial_factor_counts.get(factor, 0) + 1
                    )
            exact_product *= relation["A"]
            product_polynomial = multiply(
                product_polynomial, relation["A_polynomial"]
            )
            selected_provenance.append(
                [relation["start_offset"], relation["step_index"]]
            )

        symbolic_square = is_fraction_square(rational_unit) and all(
            exponent % 2 == 0 for exponent in polynomial_factor_counts.values()
        )
        if not symbolic_square:
            discovery_triggers.append(
                {
                    "N": modulus,
                    "type": "specialization_only_basis_relation",
                    "certificate_index": certificate_index,
                }
            )
            continue

        symbolic_basis_count += 1
        root_polynomial = [fraction_square_root(rational_unit)]
        root_factors = []
        for (slope, constant), exponent in sorted(polynomial_factor_counts.items()):
            half_exponent = exponent // 2
            for _ in range(half_exponent):
                root_polynomial = multiply(
                    root_polynomial,
                    [Fraction(constant), Fraction(slope)],
                )
            root_factors.append([f"{slope}*T+({constant})", half_exponent])
        root_at_modulus = evaluate(root_polynomial, modulus)
        assert root_at_modulus.denominator == 1
        if root_at_modulus < 0:
            root_polynomial = [-coefficient for coefficient in root_polynomial]
            root_at_modulus = -root_at_modulus
        integer_root = math.isqrt(exact_product)
        assert integer_root * integer_root == exact_product
        assert root_at_modulus == integer_root
        assert multiply(root_polynomial, root_polynomial) == product_polynomial
        assert sage_polynomial(root_polynomial) ** 2 == sage_polynomial(
            product_polynomial
        )
        assert integer_root % modulus == certificate["root_mod_N"]
        root_constant = root_polynomial[0]
        assert root_constant in (-1, 1)
        denominator_lcm = math.lcm(
            *(coefficient.denominator for coefficient in root_polynomial)
        )
        denominator_gcd = math.gcd(denominator_lcm, modulus)
        if denominator_gcd != 1:
            discovery_triggers.append(
                {
                    "N": modulus,
                    "type": "symbolic_root_denominator_nonunit",
                    "certificate_index": certificate_index,
                    "gcd": denominator_gcd,
                }
            )
        else:
            assert integer_root % modulus == int(root_constant) % modulus
        if certificate["root_type"] in ("global_plus", "global_minus"):
            symbolic_global_basis_count += 1
        certificate_results.append(
            {
                "N": modulus,
                "certificate_index": certificate_index,
                "arithmetic_only_under_numeric_endpoint_labels": not certificate[
                    "formal_endpoint_even"
                ],
                "selected_provenance": selected_provenance,
                "support_size": certificate["support_size"],
                "root_type": certificate["root_type"],
                "symbolic_square_over_Q_of_T": True,
                "symbolic_root": polynomial_text(root_polynomial),
                "symbolic_root_constant": str(root_constant),
                "symbolic_root_denominator_lcm": denominator_lcm,
                "symbolic_root_denominator_gcd_N": denominator_gcd,
                "symbolic_root_factors": root_factors,
            }
        )

    numeric_kernel_dimension = stored_batch["kernel_dimension"]
    kernels_equal = symbolic_basis_count == numeric_kernel_dimension
    all_numeric_relations_global = (
        symbolic_global_basis_count == numeric_kernel_dimension
    )
    per_input.append(
        {
            "N": modulus,
            "input_bits": input_bits,
            "unique_relation_count": stored_batch["unique_relation_count"],
            "generic_squareclass_rank": (
                stored_batch["unique_relation_count"] - numeric_kernel_dimension
                if kernels_equal
                else None
            ),
            "generic_kernel_dimension": (
                numeric_kernel_dimension if kernels_equal else None
            ),
            "numeric_kernel_dimension": numeric_kernel_dimension,
            "all_numeric_basis_relations_symbolic": (
                symbolic_basis_count == numeric_kernel_dimension
            ),
            "generic_and_numeric_kernels_equal": kernels_equal,
            "all_numeric_kernel_relations_global": all_numeric_relations_global,
            "lifted_relation_count": len(lifted_relations),
        }
    )

arithmetic_results = [
    result
    for result in certificate_results
    if result["arithmetic_only_under_numeric_endpoint_labels"]
]
output = {
    "run": RUN,
    "family": "F26",
    "input_run": "F59-D02",
    "input_sha256": EXPECTED_INPUT_HASH,
    "method": (
        "lift only the relations used by the complete numeric kernel basis "
        "to exact affine rational pairs; equality follows because every "
        "numeric basis vector is generic and every generic square identity "
        "specializes to a numeric square; verify every selected polynomial "
        "identity independently in Sage"
    ),
    "disposition": "finite symbolic certificate; no all-input source theorem",
    "per_input": per_input,
    "basis_certificate_count": len(certificate_results),
    "arithmetic_only_certificate_count": len(arithmetic_results),
    "all_basis_certificates_symbolic_global_decoys": not discovery_triggers,
    "arithmetic_only_certificates": arithmetic_results,
    "discovery_triggers": discovery_triggers,
}
with OUTPUT.open("w", encoding="utf-8") as handle:
    json.dump(output, handle, indent=2, sort_keys=True)
    handle.write("\n")

print(
    json.dumps(
        {
            "output": str(OUTPUT),
            "inputs": len(per_input),
            "basis_certificates": len(certificate_results),
            "arithmetic_only_certificates": len(arithmetic_results),
            "discovery_triggers": len(discovery_triggers),
        },
        sort_keys=True,
    )
)
