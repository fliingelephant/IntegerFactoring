#!/usr/bin/env python3
"""Exact finite checks for the public odd normal menu; labels audit only."""
import json
from pathlib import Path
import resource
import signal
import sys
import time

signal.alarm(30)
started = time.monotonic()
histogram_checks = 0
for k in range(1, 10):
    modulus = 1 << k
    for n in range(1, 16, 2):
        for a,b in ((2,1),(1,2),(6,3),(3,4)):
            histogram = [0]*modulus
            for u in range(1, modulus, 2):
                histogram[(a*u+b*n*pow(u,-1,modulus)) % modulus] += 1
            assert histogram == [s % 2 for s in range(modulus)]
            histogram_checks += 1

factor_pairs = 0
normals_checked = 0
for p in range(3, 256, 2):
    for q in range(p, 256, 2):
        n = p*q
        weights = [(2**(j+3)+(n % 8),65) for j in range(n.bit_length()+5)]
        assert weights[0][0] < 65 and weights[-1][0] > 65*n
        assert all(a % 2 and (a-b*n) % 8 == 0 for a,b in weights)
        assert all(weights[i+1][0] < 2*weights[i][0] for i in range(len(weights)-1))
        # 577/560 is a rational upper bound for (4+3*sqrt(2))/8.
        assert any(560*(a*p+b*q)**2 <= 577*4*a*b*n for a,b in weights)
        factor_pairs += 1
        normals_checked += len(weights)
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if sys.platform != 'darwin':
    rss *= 1024
result = {
    'status': 'exact_finite_certificate',
    'family': 'route:F31',
    'experiment': 'experiment:F290_dyadic_fourier_support',
    'resource_plan': {'seconds': 3, 'timeout_seconds': 30, 'peak_mb': 64, 'processes': 1},
    'mixed_parity_histograms': histogram_checks,
    'offline_factor_pairs': factor_pairs,
    'public_normals_checked': normals_checked,
    'elapsed_seconds': time.monotonic()-started,
    'max_rss_bytes': rss,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result))
