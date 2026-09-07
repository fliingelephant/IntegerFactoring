"""Exact finite check for the root-designed F303 exponent derivative.

Source estimate: less than 10 seconds and 128 MiB. The 30-second alarm is
an outer guard. All logarithms below are 2-adic; no value approximates a
complex logarithm.
"""

import json
import resource
import signal
import time
from pathlib import Path


signal.alarm(30)
started = time.monotonic()


def valuation(value):
    return (abs(value) & -abs(value)).bit_length() - 1


def log_input_bits(target_bits):
    return target_bits + 1 + (target_bits.bit_length() - 1)


def padic_log(value, target_bits):
    """Return log_2(value) modulo 2^target_bits for an odd integer value."""
    target = 1 << target_bits
    square_minus_one = value * value - 1
    assert square_minus_one % 8 == 0
    total = 0
    for h in range(1, target_bits + 1):
        h_valuation = valuation(h)
        division_bits = 1 + h_valuation
        work = 1 << (target_bits + division_bits)
        numerator = pow(square_minus_one, h, work)
        assert numerator % (1 << division_bits) == 0
        term = numerator >> division_bits
        term = term * pow(h >> h_valuation, -1, target) % target
        total = (total + term if h % 2 else total - term) % target
    return total


def exponent_value(units, M, N, exponent, target_bits):
    """Evaluate L_exponent with every jM division guard bit retained."""
    k = M.bit_length() - 1
    exponent_valuation = valuation(exponent)
    division_bits = k + exponent_valuation
    work_bits = target_bits + division_bits
    work = 1 << work_bits
    positive = sum(pow(unit, exponent, work) for unit in units) % work
    negative = sum(pow(unit, -exponent, work) for unit in units) % work
    numerator = (
        N * positive - pow(N, exponent + 1, work) * negative
    ) % work
    divisor_power = 1 << division_bits
    assert numerator % divisor_power == 0
    target = 1 << target_bits
    odd_divisor = exponent >> exponent_valuation
    result = (
        (numerator >> division_bits) * pow(odd_divisor, -1, target)
    ) % target
    return {
        "exponent": exponent,
        "target_bits": target_bits,
        "division_guard_bits": division_bits,
        "work_bits": work_bits,
        "positive_power_sum_mod_work": positive,
        "inverse_power_sum_mod_work": negative,
        "numerator_mod_work": numerator,
        "value_mod_target": result,
    }


def zero_value(units, M, N, target_bits):
    """Evaluate L_0 with the k-bit division guard required by M."""
    k = M.bit_length() - 1
    phi = M // 2
    logarithm_bits = target_bits + k
    input_bits = log_input_bits(logarithm_bits)
    work = 1 << input_bits
    product = 1
    for unit in units:
        product = product * unit % work
    ratio = product * product * pow(N, -phi, work) % work
    logarithm = padic_log(ratio, logarithm_bits)
    assert logarithm % M == 0
    value = N * (logarithm >> k) % (1 << target_bits)
    return {
        "target_bits": target_bits,
        "division_guard_bits": k,
        "logarithm_bits": logarithm_bits,
        "logarithm_input_bits": input_bits,
        "unit_product_mod_log_work": product,
        "ratio_mod_log_work": ratio,
        "ratio_log_mod_guarded_target": logarithm,
        "value_mod_target": value,
    }


def direct_statistics(units, M, N):
    q_values = []
    S11 = 0
    for unit in units:
        inverse_image = N * pow(unit, -1, M) % M
        q_values.append((unit * inverse_image - N) // M)
        S11 += unit * inverse_image
    Q1 = sum(q_values)
    Q2 = sum(value * value for value in q_values)
    assert Q2 % 2 == 0
    assert (Q1 * Q1 - Q2) % 2 == 0
    e2 = (Q1 * Q1 - Q2) // 2
    return {
        "Q1": Q1,
        "Q2": Q2,
        "Q2_over_2_mod_M": (Q2 // 2) % M,
        "e2": e2,
        "e2_mod_M": e2 % M,
        "S11": S11,
        "S11_mod_M3": S11 % (M**3),
    }


def run_case(M, N):
    k = M.bit_length() - 1
    B = k + 8
    delta = 1 << B
    precision = 6 * k + 64
    units = tuple(range(1, M, 2))
    positive = exponent_value(units, M, N, delta, precision)
    negative = exponent_value(units, M, N, -delta, precision)
    zero = zero_value(units, M, N, precision)

    precision_modulus = 1 << precision
    symmetry_expected = (
        pow(N, -delta, precision_modulus)
        * positive["value_mod_target"]
    ) % precision_modulus
    symmetry_residual = (
        negative["value_mod_target"] - symmetry_expected
    ) % precision_modulus
    assert symmetry_residual == 0

    central_division_bits = B + 1
    central_work_bits = B + central_division_bits
    assert precision >= central_work_bits
    central_work = 1 << central_work_bits
    central_numerator = (
        positive["value_mod_target"] - negative["value_mod_target"]
    ) % central_work
    assert central_numerator % (1 << central_division_bits) == 0
    central = (central_numerator >> central_division_bits) % (1 << B)

    logarithm_N = padic_log(N, precision)
    logarithm_half_source = logarithm_N % (1 << (B + 1))
    assert logarithm_half_source % 2 == 0
    logarithm_half = logarithm_half_source >> 1
    expected_derivative = (
        logarithm_half * (zero["value_mod_target"] % (1 << B))
    ) % (1 << B)
    derivative_residual = (central - expected_derivative) % (1 << B)
    assert derivative_residual == 0

    direct = direct_statistics(units, M, N)
    modulus3 = M**3
    without_quadratic = (
        N * (M // 2) + M * zero["value_mod_target"]
    ) % modulus3
    quadratic_correction = (
        M * M
        * pow(N, -1, modulus3)
        * (direct["Q2"] // 2)
    ) % modulus3
    with_quadratic = (without_quadratic + quadratic_correction) % modulus3
    assert with_quadratic == direct["S11_mod_M3"]

    return {
        "M": M,
        "N": N,
        "k": k,
        "B": B,
        "delta": delta,
        "formal_working_precision_bits": precision,
        "formal_remainder_valuation_lower_bound": 2 * B + 2 - k,
        "positive_exponent": positive,
        "negative_exponent": negative,
        "L0": zero,
        "log2_N_mod_2P": logarithm_N,
        "symmetry_expected_mod_2P": symmetry_expected,
        "symmetry_residual_mod_2P": symmetry_residual,
        "central_difference_work_bits": central_work_bits,
        "central_difference_numerator_mod_work": central_numerator,
        "central_difference_mod_2B": central,
        "log2_N_over_2_mod_2B": logarithm_half,
        "expected_derivative_mod_2B": expected_derivative,
        "derivative_residual_mod_2B": derivative_residual,
        "quadratic_statistics": direct,
        "third_digit_reconstruction": {
            "modulus": modulus3,
            "without_Q2_over_2": without_quadratic,
            "Q2_over_2_correction": quadratic_correction,
            "with_Q2_over_2": with_quadratic,
            "actual_S11_mod_M3": direct["S11_mod_M3"],
        },
    }


rows = []
for M in (8, 16, 32, 64):
    for N in (8 * M + 1, 8 * M + 3, 9 * M + 1, 9 * M + 5):
        rows.append(run_case(M, N))

assert len(rows) == 16
witness_row = next(row for row in rows if row["M"] == 32 and row["N"] == 289)
witness_stats = witness_row["quadratic_statistics"]
assert witness_stats["Q1"] == 2
assert witness_stats["Q2"] == 1090
assert witness_stats["S11"] == 4688
assert witness_stats["e2_mod_M"] == 1

summary = {
    "input_count": len(rows),
    "symmetry_checks": sum(
        row["symmetry_residual_mod_2P"] == 0 for row in rows
    ),
    "zero_derivative_residuals": sum(
        row["derivative_residual_mod_2B"] == 0 for row in rows
    ),
    "nonzero_Q2_over_2_mod_M": sum(
        row["quadratic_statistics"]["Q2_over_2_mod_M"] != 0
        for row in rows
    ),
    "nonzero_e2_mod_M": sum(
        row["quadratic_statistics"]["e2_mod_M"] != 0 for row in rows
    ),
    "third_digit_reconstructions": sum(
        row["third_digit_reconstruction"]["with_Q2_over_2"]
        == row["third_digit_reconstruction"]["actual_S11_mod_M3"]
        for row in rows
    ),
}
assert summary["symmetry_checks"] == 16
assert summary["zero_derivative_residuals"] == 16
assert summary["third_digit_reconstructions"] == 16

output = {
    "packet": "F303",
    "status": "exact_finite_exponent_derivative_checks",
    "semantics": (
        "All logarithms and exponent limits are 2-adic congruences; "
        "they do not approximate complex values."
    ),
    "timeout_seconds": 30,
    "source_runtime_estimate_seconds": "<10",
    "source_peak_memory_estimate_mib": "<128",
    "runtime_seconds": time.monotonic() - started,
    "max_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    "summary": summary,
    "witness_M32_N289": {
        "M": 32,
        "N": 289,
        **witness_stats,
        "derivative_residual_mod_2B": witness_row[
            "derivative_residual_mod_2B"
        ],
        "third_digit_reconstruction": witness_row[
            "third_digit_reconstruction"
        ],
    },
    "rows": rows,
}

encoded = json.dumps(output, indent=2) + "\n"
base = Path(__file__).with_suffix("")
base.with_suffix(".json").write_text(encoded)
base.with_suffix(".log").write_text(encoded)
status = {
    "state": "complete",
    "exit_code": 0,
    "timeout_seconds": 30,
    "input_count": len(rows),
    "runtime_seconds": output["runtime_seconds"],
    "max_rss_bytes": output["max_rss_bytes"],
}
base.with_suffix(".status").write_text(json.dumps(status, indent=2) + "\n")
print(encoded, end="")
