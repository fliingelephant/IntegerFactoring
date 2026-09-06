#!/usr/bin/env sage-python
"""Exact signed group convolution and finite compression diagnostics."""
import json
import signal
import sys
import time
import resource
from pathlib import Path
from collections import Counter

signal.alarm(30)
started = time.monotonic()
from sage.all import ZZ, PolynomialRing

ring = PolynomialRing(ZZ, 'z')
z = ring.gen()
rows = []
first_continuity_failure = None
brute_checks = 0
for k in range(2, 19):
    row_started = time.monotonic()
    modulus = 1 << k
    period = 1 << (k-2)
    residues = []
    word = []
    u = 1
    for j in range(period):
        residues.append(u)
        word.append(1 if u < modulus//2 else -1)
        u = (5*u) % modulus
    assert u == 1 and len(set(residues)) == period
    if k >= 3:
        assert word[period//2:] == [-a for a in word[:period//2]]
    poly = ring(word)
    squared = poly*poly
    convolution = [int(squared[t]+squared[t+period]) for t in range(period)]
    half_counts = [0]*modulus
    for t,u in enumerate(residues):
        for sign,n in ((1,u),(-1,(-u)%modulus)):
            numerator = modulus+4*sign*convolution[t]
            assert numerator % 8 == 0
            half_counts[n] = numerator//8
    assert min(half_counts) >= 0
    assert sum(half_counts) == (modulus//4)**2
    if k <= 9:
        direct = [0]*modulus
        for x in range(1,modulus//2,2):
            for y in range(1,modulus//2,2):
                direct[x*y % modulus] += 1
        assert direct == half_counts
        brute_checks += modulus//2
    continuity = []
    for r in range(1,k):
        step = 1 << r
        minimum = k+2
        witness = None
        for n in range(1,modulus,2):
            difference = 2*(half_counts[(n+step)%modulus]-half_counts[n])
            valuation = k+2 if difference == 0 else (abs(difference)&-abs(difference)).bit_length()-1
            if valuation < minimum:
                minimum = valuation
                witness = [n,(n+step)%modulus,half_counts[n],half_counts[(n+step)%modulus]]
        continuity.append({'input_valuation':r,'minimum_output_valuation':minimum,'witness':witness})
        if minimum < r and first_continuity_failure is None:
            first_continuity_failure = {'k':k,'r':r,'output_valuation':minimum,'witness':witness}
    record = {
        'k':k,'M':modulus,'period':period,
        'maximum_absolute_convolution':max(map(abs,convolution)),
        'distinct_convolution_values':len(set(convolution)),
        'zero_coefficients':convolution.count(0),
        'count_histogram':dict(sorted(Counter(half_counts[1::2]).items())),
        'continuity':continuity,
        'word_prefix':word[:64],
        'convolution_prefix':convolution[:32],
        'elapsed_seconds':time.monotonic()-row_started,
    }
    if k <= 8:
        record['polynomial_factorization'] = str(poly.factor())
    rows.append(record)
    print('completed',k,'period',period,'distinct',record['distinct_convolution_values'],'seconds',record['elapsed_seconds'],file=sys.stderr,flush=True)
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if sys.platform != 'darwin':
    rss *= 1024
result = {
    'family':'route:F31','experiment':'experiment:F293_carry_convolution',
    'status':'exact_finite_pilot','brute_histogram_checks':brute_checks,
    'first_continuity_failure':first_continuity_failure,
    'elapsed_seconds':time.monotonic()-started,'max_rss_bytes':rss,
    'rows':rows,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k != 'rows'}))
