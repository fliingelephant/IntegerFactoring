"""Exact endpoint phases and numerical uniform-remainder checks for F297."""

import json
import resource
import signal
import time
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp


signal.alarm(60)
started = time.monotonic()
mp.mp.dps = 35
phase_checks = 0
max_child_excess = Q(0)
for modulus in (8, 16, 32, 64, 128):
    for numerator in (1, 3, modulus // 2 - 1):
        t = Q(numerator, modulus)
        for alpha_numerator in (0, 1, modulus // 3, modulus - 1):
            alpha = Q(alpha_numerator, modulus)
            for n in range(modulus + 1):
                endpoint = Q(2 * n + 1, 2)
                r = (alpha + t * endpoint).__floor__()
                d = alpha + t * endpoint - r
                assert 0 <= d < 1
                assert 0 <= r <= n // 2 + 1
                original = r + 2 * alpha * endpoint + t * endpoint**2
                left = original - d**2 / t + (alpha - r)**2 / t
                right = original - (1 - d)**2 / t + (alpha - r - 1)**2 / t
                assert left.denominator == 1 and left.numerator % 2 == 0
                assert right.denominator == 1 and right.numerator % 2 == 1
                phase_checks += 2
                max_child_excess = max(max_child_excess, r - n * t)

rows = []
cutoff = mp.mpf(32)
knots = list(range(0, 33, 2))
degree_terms = 9
for numerator, denominator in ((0, 1), (1, 2), (1, 16), (1, 4096)):
    t = mp.mpf(numerator) / denominator
    coefficients = []
    for j in range(degree_terms):
        coefficient = 2 * mp.quad(
            lambda x: x ** (2 * j) * mp.exp(-2 * x + 1j * t * x**2 / mp.pi)
            / mp.cosh(x),
            knots,
        ) / mp.factorial(2 * j)
        coefficient_bound = mp.mpf(4) / mp.power(3, 2 * j + 1)
        assert abs(coefficient) <= coefficient_bound + mp.mpf("1e-28")
        coefficients.append(coefficient)
    for z_numerator, z_denominator in ((-1, 2), (0, 1), (1, 4), (49, 100), (1, 2)):
        z = mp.mpf(z_numerator) / z_denominator
        direct = 2 * mp.quad(
            lambda x: mp.exp(-2 * x + 1j * t * x**2 / mp.pi)
            * mp.cosh(2 * z * x) / mp.cosh(x),
            knots,
        )
        polynomial = sum(coefficient * (2 * z) ** (2 * j)
                         for j, coefficient in enumerate(coefficients))
        observed_error = abs(direct - polynomial)
        series_bound = mp.mpf(3) / 2 * mp.power(9, -degree_terms)
        # Both full integrand and its partial cosh series have tails bounded
        # by 2 exp(-2 cutoff). This does not certify the numerical quadrature.
        integral_tail_bound = 4 * mp.exp(-2 * cutoff)
        assert observed_error <= series_bound + integral_tail_bound + mp.mpf("1e-25")
        rows.append({
            "t": f"{numerator}/{denominator}",
            "z": f"{z_numerator}/{z_denominator}",
            "observed_error": mp.nstr(observed_error, 22),
            "analytic_series_bound": mp.nstr(series_bound, 22),
            "integral_tail_bound": mp.nstr(integral_tail_bound, 22),
        })

result = {
    "status": "complete",
    "family": "route:F31",
    "exact_phase_checks": phase_checks,
    "max_child_excess_over_tn": str(max_child_excess),
    "numerical_precision_decimal_digits": mp.mp.dps,
    "series_terms": degree_terms,
    "numerical_scope": "Finite quadrature observations; no certified quadrature error claim.",
    "numerical_checks": rows,
    "runtime_seconds": time.monotonic() - started,
    "peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({key: value for key, value in result.items() if key != "numerical_checks"}))
