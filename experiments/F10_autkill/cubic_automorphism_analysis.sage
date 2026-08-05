#!/usr/bin/env sage

import argparse
import json
from math import gcd
from pathlib import Path


FAMILY_ID = "F10-autkill"


argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("--run-id", required=True)
argument_parser.add_argument("--modulus", required=True, type=int)
argument_parser.add_argument("--p", required=True, type=int)
argument_parser.add_argument("--q", required=True, type=int)
arguments = argument_parser.parse_args()
RUN_ID = arguments.run_id
N = arguments.modulus
P = arguments.p
Q = arguments.q


def mul(r, s, modulus, coeffs):
    """Multiply coefficient triples modulo x^3 + u*x^2 + v*x + w."""
    u, v, w = coeffs
    r0, r1, r2 = r
    s0, s1, s2 = s
    cross = r1 * s2 + r2 * s1
    return (
        (r0 * s0 - w * cross + u * w * r2 * s2) % modulus,
        (r0 * s1 + r1 * s0 - v * cross + (u * v - w) * r2 * s2) % modulus,
        (r0 * s2 + r1 * s1 + r2 * s0 - u * cross + (u * u - v) * r2 * s2) % modulus,
    )


def add(*terms, modulus):
    return tuple(sum(term[i] for term in terms) % modulus for i in range(3))


def scale(k, r, modulus):
    return tuple((k * value) % modulus for value in r)


def apply_image(r, image, modulus, coeffs):
    image_squared = mul(image, image, modulus, coeffs)
    return add(
        (r[0], 0, 0),
        scale(r[1], image, modulus),
        scale(r[2], image_squared, modulus),
        modulus=modulus,
    )


def f_at_image(image, modulus, coeffs):
    u, v, w = coeffs
    image_squared = mul(image, image, modulus, coeffs)
    image_cubed = mul(image, image_squared, modulus, coeffs)
    return add(
        image_cubed,
        scale(u, image_squared, modulus),
        scale(v, image, modulus),
        (w, 0, 0),
        modulus=modulus,
    )


def determinant(image, modulus, coeffs):
    _, b, c = image
    u, v, w = coeffs
    return (b**3 - 2 * u * b**2 * c + (u**2 + v) * b * c**2 - (u * v - w) * c**3) % modulus


def is_automorphism(image, modulus, coeffs):
    return f_at_image(image, modulus, coeffs) == (0, 0, 0) and gcd(determinant(image, modulus, coeffs), modulus) == 1


def automorphism_order(image, modulus, coeffs):
    current = (0, 1, 0)
    for order in range(1, 7):
        current = apply_image(current, image, modulus, coeffs)
        if current == (0, 1, 0):
            return order
    raise AssertionError("A cubic etale automorphism must have order at most 6")


def discriminant(coeffs):
    u, v, w = coeffs
    return u * u * v * v - 4 * v**3 - 4 * u**3 * w - 27 * w * w + 18 * u * v * w


def local_type(coeffs, prime):
    roots = sum(
        1
        for x in range(prime)
        if (x**3 + coeffs[0] * x**2 + coeffs[1] * x + coeffs[2]) % prime == 0
    )
    if discriminant(coeffs) % prime == 0:
        return "non-squarefree"
    return {0: "3", 1: "12", 3: "111"}[roots]


def all_automorphisms(modulus, coeffs):
    return [
        (a, b, c)
        for a in range(modulus)
        for b in range(modulus)
        for c in range(modulus)
        if is_automorphism((a, b, c), modulus, coeffs)
    ]


def symbolic_equations():
    symbolic_ring = PolynomialRing(ZZ, names=("u", "v", "w", "a", "b", "c"))
    u, v, w, a, b, c = symbolic_ring.gens()

    def symbolic_mul(r, s):
        r0, r1, r2 = r
        s0, s1, s2 = s
        cross = r1 * s2 + r2 * s1
        return (
            r0 * s0 - w * cross + u * w * r2 * s2,
            r0 * s1 + r1 * s0 - v * cross + (u * v - w) * r2 * s2,
            r0 * s2 + r1 * s1 + r2 * s0 - u * cross + (u * u - v) * r2 * s2,
        )

    y = (a, b, c)
    y2 = symbolic_mul(y, y)
    y3 = symbolic_mul(y, y2)
    f_equations = tuple(y3[i] + u * y2[i] + v * y[i] + (w if i == 0 else 0) for i in range(3))

    sigma2 = tuple((a if i == 0 else 0) + b * y[i] + c * y2[i] for i in range(3))
    sigma3 = tuple(sigma2[0] * (1 if i == 0 else 0) + sigma2[1] * y[i] + sigma2[2] * y2[i] for i in range(3))
    targets = (0, 1, 0)
    order2_equations = tuple(sigma2[i] - targets[i] for i in range(3))
    order3_equations = tuple(sigma3[i] - targets[i] for i in range(3))
    det = b * y2[2] - c * y2[1]

    return {
        "y_squared": [str(value) for value in y2],
        "f_of_y_coefficients": [str(value) for value in f_equations],
        "sigma2_minus_x": [str(value) for value in order2_equations],
        "sigma3_minus_x": [str(value) for value in order3_equations],
        "determinant": str(det),
    }


def gcd_certificate(image):
    a, b, c = image
    return {
        "gcd_a": gcd(a, N),
        "gcd_b_minus_1": gcd((b - 1) % N, N),
        "gcd_c": gcd(c, N),
    }


def main():
    chosen = None
    for u in range(N):
        for v in range(N):
            for w in range(N):
                coeffs = (u, v, w)
                if gcd(discriminant(coeffs), N) != 1:
                    continue
                if local_type(coeffs, P) == "12" and local_type(coeffs, Q) == "3":
                    chosen = coeffs
                    break
            if chosen is not None:
                break
        if chosen is not None:
            break
    if chosen is None:
        raise AssertionError("No (12)/(3) example found")

    automorphisms = all_automorphisms(N, chosen)
    records = []
    for image in automorphisms:
        record = {
            "image": list(image),
            "global_order": automorphism_order(image, N, chosen),
            "order_mod_p": automorphism_order(tuple(x % P for x in image), P, tuple(x % P for x in chosen)),
            "order_mod_q": automorphism_order(tuple(x % Q for x in image), Q, tuple(x % Q for x in chosen)),
            "gcd_certificate": gcd_certificate(image),
        }
        records.append(record)

    local_p = all_automorphisms(P, tuple(x % P for x in chosen))
    local_q = all_automorphisms(Q, tuple(x % Q for x in chosen))
    result = {
        "family_id": FAMILY_ID,
        "run_id": RUN_ID,
        "N": N,
        "factorization_used_only_for_audit": [P, Q],
        "coefficients_u_v_w": list(chosen),
        "polynomial": f"x^3 + {chosen[0]}*x^2 + {chosen[1]}*x + {chosen[2]}",
        "integer_discriminant": discriminant(chosen),
        "gcd_discriminant_N": gcd(discriminant(chosen), N),
        "local_type_mod_p": local_type(chosen, P),
        "local_type_mod_q": local_type(chosen, Q),
        "ambient_coefficient_tuples": N**3,
        "local_automorphism_counts": [len(local_p), len(local_q)],
        "global_automorphism_count": len(automorphisms),
        "automorphisms": records,
        "symbolic_equations": symbolic_equations(),
    }
    output_path = Path(f"experiments/F10_autkill/output/{RUN_ID}.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True, default=int) + "\n")
    print(json.dumps({
        "family_id": FAMILY_ID,
        "run_id": RUN_ID,
        "chosen_coefficients": list(chosen),
        "local_types": [result["local_type_mod_p"], result["local_type_mod_q"]],
        "global_automorphism_count": len(automorphisms),
        "output": str(output_path),
    }, sort_keys=True, default=int))


if __name__ == "__main__":
    main()
