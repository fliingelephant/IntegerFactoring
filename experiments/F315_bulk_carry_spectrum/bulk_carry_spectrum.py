#!/usr/bin/env python3
"""Exact bulk discovery for the unshifted transport T(N) modulo 16.

The four cyclic convolutions are integer polynomial products in Sage/FLINT.
They are discovery computations. They are not an asymptotic evaluator.
"""

from sage.all import ZZ, PolynomialRing

import argparse
import base64
import gc
import hashlib
import json
import os
from pathlib import Path
import random
import resource
import signal
import sys
import threading
import time
import traceback


SEED = 31520260907
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 1 << 30
SPARSE_MONOMIAL_LIMIT = 256
POLYNOMIAL_RING = PolynomialRing(ZZ, "X")


def peak_rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def write_json(path, value):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(target)


def source_sha256():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def packed_bits(bits):
    data = bytearray((len(bits) + 7) // 8)
    for index, bit in enumerate(bits):
        if bit:
            data[index >> 3] |= 1 << (index & 7)
    raw = bytes(data)
    return {
        "bit_count": len(bits),
        "byte_count": len(raw),
        "bit_order": "index i is bit (i mod 8) of byte floor(i/8), least-significant bit first",
        "base64": base64.b64encode(raw).decode("ascii"),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }


def anf_coefficients(truth, variable_count):
    coefficients = list(truth)
    for variable in range(variable_count):
        step = 1 << variable
        for mask in range(len(coefficients)):
            if mask & step:
                coefficients[mask] ^= coefficients[mask ^ step]
    return coefficients


def analyze_boolean_table(truth, variable_count):
    coefficients = anf_coefficients(truth, variable_count)
    masks = [mask for mask, coefficient in enumerate(coefficients) if coefficient]
    counts = {}
    for mask in masks:
        degree = mask.bit_count()
        counts[str(degree)] = counts.get(str(degree), 0) + 1
    packed_coefficients = packed_bits(coefficients)
    result = {
        "truth": packed_bits(truth),
        "anf_degree": max((mask.bit_count() for mask in masks), default=-1),
        "anf_monomial_count": len(masks),
        "anf_monomial_counts_by_degree": counts,
        "anf_coefficient_sha256": packed_coefficients["sha256"],
    }
    if len(masks) <= SPARSE_MONOMIAL_LIMIT:
        result["anf_representation"] = "exact_sparse_masks"
        result["anf_monomial_masks"] = [hex(mask) for mask in masks]
    else:
        result["anf_representation"] = "packed_coefficients"
        result["anf_coefficients"] = packed_coefficients
    return result


def analyze_three_bits(values, variable_count):
    return {
        f"bit_{bit}": analyze_boolean_table(
            [((value >> bit) & 1) for value in values], variable_count
        )
        for bit in range(3)
    }


def cyclic_integer_convolution(left, right):
    """Return the exact convolution folded modulo X^R-1."""
    length = len(left)
    assert length == len(right) and length > 0
    product = POLYNOMIAL_RING(left) * POLYNOMIAL_RING(right)
    output = [0] * length
    for degree, coefficient in enumerate(product.list()):
        output[degree if degree < length else degree - length] += int(coefficient)
    del product
    gc.collect()
    if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
        raise MemoryError("peak RSS exceeded the one-GiB experiment limit")
    return output


def group_arrays(modulus):
    length = modulus // 4
    inverse_five = pow(5, -1, modulus)
    plus = []
    minus = []
    a_plus = []
    a_minus = []
    mu_plus_mod16 = []
    mu_minus_mod16 = []
    current = 1
    inverse_current = 1
    a_mu = 0
    for _ in range(length):
        negative = modulus - current
        inverse_negative = modulus - inverse_current
        q_plus = (current * inverse_current - 1) // modulus
        q_minus = (negative * inverse_negative - 1) // modulus
        mu_plus = (inverse_current * q_plus) % 16
        mu_minus = (inverse_negative * q_minus) % 16
        plus.append(current)
        minus.append(negative)
        a_plus.append((current * q_plus) % 16)
        a_minus.append((negative * q_minus) % 16)
        mu_plus_mod16.append(mu_plus)
        mu_minus_mod16.append(mu_minus)
        a_mu += mu_plus * current + mu_minus * negative
        current = (current * 5) % modulus
        inverse_current = (inverse_current * inverse_five) % modulus
    assert len(set(plus + minus)) == modulus // 2
    return {
        "plus": plus,
        "minus": minus,
        "a_plus": a_plus,
        "a_minus": a_minus,
        "mu_plus_mod16": mu_plus_mod16,
        "mu_minus_mod16": mu_minus_mod16,
        "a_mu": a_mu,
    }


def direct_transport_mod16(modulus, argument, arrays):
    total = 0
    for w, mu in zip(arrays["plus"], arrays["mu_plus_mod16"]):
        total += mu * ((argument * w) // modulus)
    for w, mu in zip(arrays["minus"], arrays["mu_minus_mod16"]):
        total += mu * ((argument * w) // modulus)
    return total % 16


def validation_residues(k, modulus):
    if modulus <= 128:
        return list(range(1, modulus, 2)), "all_canonical_odd_residues"
    fixed = [1, 3, 5, 7]
    generator = random.Random(SEED ^ (k << 16) ^ modulus)
    seeded = []
    while len(seeded) < 4:
        candidate = generator.randrange(1, modulus, 2)
        if candidate not in fixed and candidate not in seeded:
            seeded.append(candidate)
    return fixed + seeded, "four_fixed_and_four_seeded_residues"


def compute_modulus(k, include_spectrum):
    started = time.perf_counter()
    modulus = 1 << k
    length = modulus // 4
    arrays = group_arrays(modulus)

    print(json.dumps({"event": "convolutions_start", "k": k, "R": length}), flush=True)
    convolution_plus_plus = cyclic_integer_convolution(arrays["a_plus"], arrays["plus"])
    convolution_minus_minus = cyclic_integer_convolution(arrays["a_minus"], arrays["minus"])
    convolution_plus_minus = cyclic_integer_convolution(arrays["a_plus"], arrays["minus"])
    convolution_minus_plus = cyclic_integer_convolution(arrays["a_minus"], arrays["plus"])
    c_plus = [x + y for x, y in zip(convolution_plus_plus, convolution_minus_minus)]
    c_minus = [x + y for x, y in zip(convolution_plus_minus, convolution_minus_plus)]
    del convolution_plus_plus, convolution_minus_minus
    del convolution_plus_minus, convolution_minus_plus
    gc.collect()

    a_mu = arrays["a_mu"]
    transport_by_residue = {}
    canonical_by_residue = {}
    division_failures = 0
    raw_canonical_failures = 0
    for index in range(length):
        for residue, c_value in (
            (arrays["plus"][index], c_plus[index]),
            (arrays["minus"][index], c_minus[index]),
        ):
            raw_argument = 8 * modulus + residue
            canonical_numerator = residue * a_mu - c_value
            raw_numerator = raw_argument * a_mu - c_value
            if canonical_numerator % modulus or raw_numerator % modulus:
                division_failures += 1
                continue
            canonical_value = (canonical_numerator // modulus) % 16
            raw_value = (raw_numerator // modulus) % 16
            canonical_by_residue[residue] = canonical_value
            transport_by_residue[residue] = raw_value
            if raw_value != (canonical_value + 8 * a_mu) % 16:
                raw_canonical_failures += 1
    if division_failures or raw_canonical_failures:
        raise AssertionError(
            f"division={division_failures}, raw/canonical={raw_canonical_failures}"
        )
    if any(value & 1 for value in transport_by_residue.values()):
        raise AssertionError("T(N) was not even for some residue")

    residues, validation_scope = validation_residues(k, modulus)
    validation_rows = []
    for residue in residues:
        raw_argument = 8 * modulus + residue
        direct_canonical = direct_transport_mod16(modulus, residue, arrays)
        direct_raw = direct_transport_mod16(modulus, raw_argument, arrays)
        row = {
            "residue": residue,
            "raw_argument": raw_argument,
            "formula_canonical_mod16": canonical_by_residue[residue],
            "direct_canonical_mod16": direct_canonical,
            "formula_raw_mod16": transport_by_residue[residue],
            "direct_raw_mod16": direct_raw,
            "raw_minus_canonical_mod16": (
                transport_by_residue[residue] - canonical_by_residue[residue]
            )
            % 16,
            "expected_raw_correction_mod16": (8 * a_mu) % 16,
        }
        row["passed"] = (
            row["formula_canonical_mod16"] == row["direct_canonical_mod16"]
            and row["formula_raw_mod16"] == row["direct_raw_mod16"]
            and row["raw_minus_canonical_mod16"]
            == row["expected_raw_correction_mod16"]
        )
        validation_rows.append(row)
    if not all(row["passed"] for row in validation_rows):
        raise AssertionError("direct validation failed")

    t0 = {residue: (value >> 1) & 1 for residue, value in transport_by_residue.items()}
    t0_minus_one = t0[modulus - 1]
    sign_mismatches = [
        residue
        for residue in range(1, modulus, 2)
        if t0[(-residue) % modulus] != (t0_minus_one ^ t0[residue])
    ]
    if sign_mismatches:
        raise AssertionError("first-bit sign relation failed")

    result = {
        "k": k,
        "M": modulus,
        "R": length,
        "group": "C2 x C_(M/4), with residues (-1)^epsilon*5^j",
        "convolution_count": 4,
        "convolution_ring": "ZZ[X]/(X^R-1), products computed in Sage/FLINT and folded exactly",
        "a_mu_exact": a_mu,
        "exact_division_failures_all_residues": division_failures,
        "raw_canonical_congruence_failures_all_residues": raw_canonical_failures,
        "validation_scope": validation_scope,
        "validation_case_count": len(validation_rows),
        "validation_rows": validation_rows,
        "first_bit_sign_relation": {
            "identity": "t0(-r)=t0(-1)+t0(r) in F2",
            "t0_minus_one": t0_minus_one,
            "tested_residue_count": modulus // 2,
            "mismatch_count": 0,
        },
        "walltime_seconds": time.perf_counter() - started,
        "peak_rss_bytes_after_modulus": peak_rss_bytes(),
    }

    if include_spectrum:
        ordinary_values = [0] * (modulus // 2)
        log_values = [0] * (modulus // 2)
        plus_values = [0] * length
        for index in range(length):
            plus_residue = arrays["plus"][index]
            minus_residue = arrays["minus"][index]
            plus_value = transport_by_residue[plus_residue] // 2
            minus_value = transport_by_residue[minus_residue] // 2
            ordinary_values[(plus_residue - 1) // 2] = plus_value
            ordinary_values[(minus_residue - 1) // 2] = minus_value
            log_values[2 * index] = plus_value
            log_values[2 * index + 1] = minus_value
            plus_values[index] = plus_value
        result["spectrum"] = {
            "value": "T(8M+r)/2 modulo 8",
            "bit_0_role": "F313 modulo-four control",
            "bit_1_role": "new T modulo-eight information",
            "bit_2_role": "new T modulo-sixteen information",
            "ordinary_coordinate": {
                "index": "x=(r-1)/2, with index bits in little-endian order",
                "variable_count": k - 1,
                "bits": analyze_three_bits(ordinary_values, k - 1),
            },
            "sign_log_coordinate": {
                "index": "epsilon+2*j for r=(-1)^epsilon*5^j; epsilon is variable bit 0",
                "variable_count": k - 1,
                "bits": analyze_three_bits(log_values, k - 1),
            },
            "positive_sign_restrictions": {
                "j_even_square_exponents": {
                    "index": "t with epsilon=0 and j=2*t",
                    "variable_count": k - 3,
                    "bits": analyze_three_bits(plus_values[0::2], k - 3),
                },
                "j_odd_nonsquare_exponents": {
                    "index": "t with epsilon=0 and j=2*t+1",
                    "variable_count": k - 3,
                    "bits": analyze_three_bits(plus_values[1::2], k - 3),
                },
            },
        }

    del arrays, c_plus, c_minus, transport_by_residue, canonical_by_residue
    gc.collect()
    result["peak_rss_bytes_after_cleanup"] = peak_rss_bytes()
    print(
        json.dumps(
            {
                "event": "modulus_complete",
                "k": k,
                "walltime_seconds": result["walltime_seconds"],
                "peak_rss_bytes": result["peak_rss_bytes_after_cleanup"],
            }
        ),
        flush=True,
    )
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scales", required=True, help="comma-separated k values")
    parser.add_argument("--output", required=True)
    parser.add_argument("--status", required=True)
    parser.add_argument("--label", required=True)
    arguments = parser.parse_args()
    scales = [int(item) for item in arguments.scales.split(",") if item]
    if not scales or any(k < 8 for k in scales):
        raise ValueError("analysis scales must all be at least 8")

    started = time.perf_counter()
    stop_watchdog = threading.Event()

    def alarm_handler(_signal_number, _frame):
        raise TimeoutError("internal 28-second alarm fired")

    def memory_watchdog():
        while not stop_watchdog.wait(0.05):
            current = peak_rss_bytes()
            if current > MEMORY_LIMIT_BYTES:
                write_json(
                    arguments.status,
                    {
                        "status": "memory_limit_exceeded",
                        "label": arguments.label,
                        "scales": scales,
                        "peak_rss_bytes": current,
                        "memory_limit_bytes": MEMORY_LIMIT_BYTES,
                        "source_sha256": source_sha256(),
                    },
                )
                os._exit(70)

    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(INTERNAL_TIMEOUT_SECONDS)
    thread = threading.Thread(target=memory_watchdog, daemon=True)
    thread.start()
    write_json(
        arguments.status,
        {
            "status": "running",
            "label": arguments.label,
            "scales": scales,
            "seed": SEED,
            "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
            "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
            "memory_limit_bytes": MEMORY_LIMIT_BYTES,
            "source_sha256": source_sha256(),
        },
    )

    try:
        print(
            json.dumps(
                {
                    "event": "start",
                    "label": arguments.label,
                    "scales": scales,
                    "seed": SEED,
                    "source_sha256": source_sha256(),
                }
            ),
            flush=True,
        )
        small_controls = [compute_modulus(k, False) for k in range(3, 8)]
        scale_results = [compute_modulus(k, True) for k in scales]
        payload = {
            "status": "passed",
            "label": arguments.label,
            "seed": SEED,
            "method_scope": "exact enumerative discovery; no polynomial-bit claim",
            "source_sha256": source_sha256(),
            "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
            "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
            "memory_limit_bytes": MEMORY_LIMIT_BYTES,
            "small_full_validation": small_controls,
            "scales": scale_results,
            "total_walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, payload)
        write_json(
            arguments.status,
            {
                "status": "passed",
                "label": arguments.label,
                "scales": scales,
                "seed": SEED,
                "output": arguments.output,
                "source_sha256": source_sha256(),
                "total_walltime_seconds": payload["total_walltime_seconds"],
                "peak_rss_bytes": payload["peak_rss_bytes"],
                "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
                "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
                "memory_limit_bytes": MEMORY_LIMIT_BYTES,
            },
        )
        print(json.dumps({"event": "passed", "status": payload["status"]}), flush=True)
    except BaseException as exception:
        failure = {
            "status": "failed",
            "label": arguments.label,
            "scales": scales,
            "seed": SEED,
            "source_sha256": source_sha256(),
            "exception_type": type(exception).__name__,
            "exception": str(exception),
            "traceback": traceback.format_exc(),
            "total_walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
            "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
            "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
            "memory_limit_bytes": MEMORY_LIMIT_BYTES,
        }
        write_json(arguments.output, failure)
        write_json(arguments.status, failure)
        print(json.dumps({"event": "failed", "failure": failure}), flush=True)
        raise
    finally:
        signal.alarm(0)
        stop_watchdog.set()
        thread.join(timeout=0.2)


if __name__ == "__main__":
    main()
