#!/usr/bin/env sage
"""Independent hostile verifier for the finite F04/X05 AKS certificate.

This source serves family F04.  It does not import or execute the retained
scanner.  It verifies the AKS parameters with elementary exact loops, scans
the two finite-field error families with an independently written binary
power routine, and directly compares localized and global errors at sample
shifts.
"""

import argparse
import hashlib
import json
import math
import time
from pathlib import Path


P = 100000007
Q = 199999991
N = 20000000499999937
EXPECTED_R = 2953
EXPECTED_SHIFT_BOUND = 2942


def exact_multiplicative_order(value, modulus):
    """Find the first positive exponent giving one by direct iteration."""
    assert math.gcd(value, modulus) == 1
    residue = 1
    multiplier = value % modulus
    for exponent in range(1, modulus + 1):
        residue = residue * multiplier % modulus
        if residue == 1:
            return exponent
    raise AssertionError("Euler's theorem bound was exceeded")


def quotient_power(base, exponent, modulus):
    """Binary powering with explicit polynomial reduction after each product."""
    result = base.parent().one()
    while exponent:
        if exponent & 1:
            result = (result * base).mod(modulus)
        exponent >>= 1
        if exponent:
            base = (base * base).mod(modulus)
    return result


def scan_local_family(characteristic, cofactor, r, shift_bound):
    """Scan h_(cofactor,a) before the Frobenius position permutation."""
    polynomial_ring = PolynomialRing(GF(characteristic), "y")
    y = polynomial_ring.gen()
    modulus = y**r - 1
    y_cofactor = y ** (cofactor % r)
    coefficient_digest = hashlib.sha256()
    zero_count = 0
    scanned = 0
    exceptional_shifts = []
    started = time.monotonic()

    for a in range(1, shift_bound + 1):
        error = quotient_power(y + polynomial_ring(a), cofactor, modulus)
        error -= y_cofactor
        error -= polynomial_ring(a)
        shift_zero_count = 0
        for position in range(r):
            coefficient = int(error[position])
            coefficient_digest.update(coefficient.to_bytes(4, "big"))
            shift_zero_count += coefficient == 0
            scanned += 1
        zero_count += shift_zero_count
        if shift_zero_count:
            exceptional_shifts.append(
                {"a": a, "zero_count_before_permutation": shift_zero_count}
            )
        if a % 100 == 0 or a == shift_bound:
            print(
                f"characteristic={characteristic} shift={a}/{shift_bound} "
                f"zeros={zero_count}",
                flush=True,
            )

    return {
        "characteristic": characteristic,
        "cofactor": cofactor,
        "scanned_coefficients": scanned,
        "zero_count_before_permutation": zero_count,
        "coefficient_sha256": coefficient_digest.hexdigest(),
        "digest_encoding": "a increasing, position 0..r-1, uint32 big-endian",
        "exceptional_shifts": exceptional_shifts,
        "elapsed_seconds": time.monotonic() - started,
    }


def direct_frobenius_checks(characteristic, cofactor, r, shifts):
    """Compare h_(cofactor,a)(X^characteristic) with the global H_a."""
    polynomial_ring = PolynomialRing(GF(characteristic), "z")
    z = polynomial_ring.gen()
    modulus = z**r - 1
    mapping = [(characteristic * j) % r for j in range(r)]
    mapping_is_permutation = sorted(mapping) == list(range(r))
    comparisons = []

    for a in shifts:
        local_error = quotient_power(
            z + polynomial_ring(a), cofactor, modulus
        )
        local_error -= z ** (cofactor % r)
        local_error -= polynomial_ring(a)
        permuted_coefficients = [polynomial_ring.base_ring().zero()] * r
        for j in range(r):
            permuted_coefficients[mapping[j]] = local_error[j]
        localized_global_error = polynomial_ring(permuted_coefficients)

        direct_global_error = quotient_power(
            z + polynomial_ring(a), N, modulus
        )
        direct_global_error -= z ** (N % r)
        direct_global_error -= polynomial_ring(a)
        comparisons.append(
            {
                "a": a,
                "localized_equals_direct_global": (
                    localized_global_error == direct_global_error
                ),
                "direct_global_zero_count": sum(
                    direct_global_error[j] == 0 for j in range(r)
                ),
            }
        )

    return {
        "characteristic": characteristic,
        "cofactor": cofactor,
        "position_map_is_permutation": mapping_is_permutation,
        "comparisons": comparisons,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--retained", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    total_started = time.monotonic()
    source_path = Path(
        "experiments/F04_audit/verify_f04_counterexample.sage"
    ).resolve()

    assert P * Q == N
    assert P != Q

    primality_checks = []
    for candidate in (P, Q):
        limit = math.isqrt(candidate)
        first_divisor = None
        for divisor in range(2, limit + 1):
            if candidate % divisor == 0:
                first_divisor = divisor
                break
        primality_checks.append(
            {
                "candidate": candidate,
                "trial_division_through": limit,
                "tested_integer_divisors": limit - 1,
                "first_divisor": first_divisor,
                "prime": first_divisor is None,
            }
        )
    assert all(item["prime"] for item in primality_checks)

    interval_field = RealIntervalField(256)
    log2_n = interval_field(N).log() / interval_field(2).log()
    order_threshold = log2_n**2
    assert order_threshold > interval_field(2932)
    assert order_threshold < interval_field(2933)
    threshold_floor = 2932

    orders = {}
    noncoprime_moduli = []
    order_transcript = []
    for modulus in range(2, EXPECTED_R + 1):
        if math.gcd(N, modulus) != 1:
            noncoprime_moduli.append(modulus)
            order_transcript.append(f"{modulus}:noncoprime")
            continue
        order = exact_multiplicative_order(N, modulus)
        orders[modulus] = order
        order_transcript.append(f"{modulus}:{order}")
    qualifying_moduli = [
        modulus
        for modulus, order in orders.items()
        if order >= threshold_floor + 1
    ]
    selected_r = min(qualifying_moduli)
    prior_max_order = max(orders[modulus] for modulus in range(2, selected_r))
    prior_max_moduli = [
        modulus
        for modulus in range(2, selected_r)
        if orders[modulus] == prior_max_order
    ]
    assert selected_r == EXPECTED_R
    assert orders[selected_r] == 2952

    phi_r = sum(math.gcd(k, selected_r) == 1 for k in range(1, selected_r + 1))
    assert phi_r == 2952
    shift_expression = interval_field(phi_r).sqrt() * log2_n
    assert shift_expression > interval_field(EXPECTED_SHIFT_BOUND)
    assert shift_expression < interval_field(EXPECTED_SHIFT_BOUND + 1)
    assert P > selected_r and Q > selected_r
    preliminary_nonunits = [
        a for a in range(2, selected_r + 1) if math.gcd(a, N) != 1
    ]
    assert not preliminary_nonunits

    print("exact parameter audit complete", flush=True)
    scan_mod_p = scan_local_family(P, Q, selected_r, EXPECTED_SHIFT_BOUND)
    scan_mod_q = scan_local_family(Q, P, selected_r, EXPECTED_SHIFT_BOUND)
    direct_checks = [
        direct_frobenius_checks(P, Q, selected_r, [1, 1471, 2942]),
        direct_frobenius_checks(Q, P, selected_r, [1, 1471, 2942]),
    ]

    retained_path = Path(args.retained)
    retained_bytes = retained_path.read_bytes()
    retained = json.loads(retained_bytes)
    retained_expected = {
        "N": N,
        "p": P,
        "q": Q,
        "r": EXPECTED_R,
        "order": 2952,
        "phi_r": 2952,
        "shift_bound": EXPECTED_SHIFT_BOUND,
        "tested_shift_bound": EXPECTED_SHIFT_BOUND,
        "aks_trial_gcd_would_stop": False,
        "any_pass_fail": False,
        "total_coefficients": EXPECTED_R * EXPECTED_SHIFT_BOUND,
        "total_zero_mod_p": 0,
        "total_zero_mod_q": 0,
        "total_zero_both": 0,
        "total_separator_positions": 0,
    }
    retained_field_matches = {
        key: retained.get(key) == value for key, value in retained_expected.items()
    }

    expected_positions = EXPECTED_R * EXPECTED_SHIFT_BOUND
    audit_passed = all(
        [
            P * Q == N,
            all(item["prime"] for item in primality_checks),
            selected_r == EXPECTED_R,
            orders[selected_r] == 2952,
            phi_r == 2952,
            not preliminary_nonunits,
            scan_mod_p["scanned_coefficients"] == expected_positions,
            scan_mod_q["scanned_coefficients"] == expected_positions,
            scan_mod_p["zero_count_before_permutation"] == 0,
            scan_mod_q["zero_count_before_permutation"] == 0,
            all(
                check["position_map_is_permutation"]
                and all(
                    comparison["localized_equals_direct_global"]
                    for comparison in check["comparisons"]
                )
                for check in direct_checks
            ),
            all(retained_field_matches.values()),
        ]
    )

    output = {
        "family": "F04",
        "audit_scope": "standard minimal-r AKS pass/fail and coefficient scan",
        "source": str(source_path),
        "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
        "N": N,
        "p": P,
        "q": Q,
        "product_verified": P * Q == N,
        "primality_checks": primality_checks,
        "distinct_prime_factors": P != Q and all(
            item["prime"] for item in primality_checks
        ),
        "log2_n_interval": str(log2_n),
        "order_threshold_interval": str(order_threshold),
        "order_threshold_floor": threshold_floor,
        "selected_r": selected_r,
        "selected_order": orders[selected_r],
        "prior_max_order": prior_max_order,
        "prior_max_order_moduli": prior_max_moduli,
        "orders_2934_through_2953": {
            str(modulus): orders[modulus]
            for modulus in range(2934, EXPECTED_R + 1)
        },
        "noncoprime_moduli_through_selected_r": noncoprime_moduli,
        "order_transcript_sha256": hashlib.sha256(
            "\n".join(order_transcript).encode("ascii")
        ).hexdigest(),
        "phi_r": phi_r,
        "shift_expression_interval": str(shift_expression),
        "shift_bound": EXPECTED_SHIFT_BOUND,
        "p_and_q_exceed_r": P > selected_r and Q > selected_r,
        "preliminary_gcd_nonunits": preliminary_nonunits,
        "global_coefficient_positions": expected_positions,
        "scan_mod_p": scan_mod_p,
        "scan_mod_q": scan_mod_q,
        "direct_frobenius_checks": direct_checks,
        "retained_certificate": str(retained_path),
        "retained_certificate_sha256": hashlib.sha256(retained_bytes).hexdigest(),
        "retained_field_matches": retained_field_matches,
        "audit_passed": audit_passed,
        "elapsed_seconds": time.monotonic() - total_started,
    }
    output_path = Path(args.output)
    with output_path.open("w") as handle:
        json.dump(output, handle, indent=2, default=int)
        handle.write("\n")
    print(f"audit_passed={audit_passed}", flush=True)
    print(f"certificate={output_path}", flush=True)
    if not audit_passed:
        raise RuntimeError("F04 hostile audit failed")


main()
