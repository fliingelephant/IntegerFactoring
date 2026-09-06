#!/usr/bin/env python3
"""Check affine inverse patches and higher differences with exact arithmetic."""
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError("30-second certificate limit")))
signal.alarm(30)
started = time.monotonic()
affine_checks = 0
for k in range(1, 13):
    modulus = 1 << k
    h = max(1, k // 2)
    step = 1 << h
    for n in range(1, 32, 2):
        for origin in range(1, step, 2):
            v0 = n * pow(origin, -1, modulus) % modulus
            delta = n * (pow(origin + step, -1, modulus) - pow(origin, -1, modulus)) % modulus
            for x in range(origin, modulus, step):
                assert n * pow(x, -1, modulus) % modulus == (v0 + ((x-origin)//step)*delta) % modulus
                affine_checks += 1

higher_checks = 0
degrees = []
for k in (4, 8, 16, 32, 64, 128, 256, 512):
    modulus = 1 << k
    n = (1 << 521) + 12345
    for r in (1, 2, 4, 8, 16):
        step = 1 << r
        d = 1
        while r*d + d-d.bit_count() < k:
            d += 1
        origin = step - 1
        denominator = origin
        numerator = n
        coefficients = []
        for i in range(d):
            if i:
                numerator *= -i*step
                denominator *= origin+i*step
            coefficients.append(numerator * pow(denominator, -1, modulus) % modulus)
        for j in (-257, -11, -1, 0, 1, 2, 17, 257, (1 << 137)+7):
            value = 0
            choose = 1
            for i, coefficient in enumerate(coefficients):
                if i:
                    choose = choose*(j-i+1)//i
                value = (value + choose*coefficient) % modulus
            assert value == n*pow(origin+step*j, -1, modulus) % modulus
            higher_checks += 1
        degrees.append({"k": k, "r": r, "degree_bound": d-1})

# sqrt(2)<99/70 gives the rational upper bound 577/560.
assert 99**2 > 2*70**2
assert 10201*577*16 < 17*10000*560
elapsed = time.monotonic()-started
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if sys.platform != "darwin":
    rss *= 1024
result = {
    "status": "exact_finite_certificate",
    "family": "route:F31",
    "experiment": "experiment:F289_modular_support_union",
    "resource_plan": {"timeout_seconds": 30, "estimated_seconds": 3, "estimated_peak_mb": 64, "processes": 1},
    "affine_checks": affine_checks,
    "higher_difference_checks": higher_checks,
    "higher_degree_bounds": degrees,
    "one_percent_margin_rational_check": "passed",
    "elapsed_seconds": elapsed,
    "max_rss_bytes": rss,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k != 'higher_degree_bounds'}))
