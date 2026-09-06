"""F285: exact public differentiated-power operator and offline local labels."""
import itertools
import json
import math
import random
import resource
import signal
import time
from pathlib import Path

signal.alarm(5)
started = time.monotonic()
PAIRS = [(3, 5), (3, 7), (5, 7), (5, 11), (7, 13), (7, 17), (11, 19), (11, 23), (13, 29)]


def multiply(a, b, modulus):
    return tuple(sum(a[2*i+k] * b[2*k+j] for k in range(2)) % modulus
                 for i in range(2) for j in range(2))


def add(a, b, modulus):
    return tuple((x+y) % modulus for x, y in zip(a, b))


def power_jet(a, h, exponent, modulus):
    value, tangent = (1, 0, 0, 1), (0, 0, 0, 0)
    for bit in bin(exponent)[2:]:
        tangent = add(multiply(value, tangent, modulus), multiply(tangent, value, modulus), modulus)
        value = multiply(value, value, modulus)
        if bit == '1':
            tangent = add(multiply(tangent, a, modulus), multiply(value, h, modulus), modulus)
            value = multiply(value, a, modulus)
    return value, tangent


def lucas(exponent, trace, determinant, modulus):
    # (u,v) represents u*A+v*I, with A^2=trace*A-determinant*I.
    u, v = 0, 1
    for bit in bin(exponent)[2:]:
        u, v = (u*u*trace+2*u*v) % modulus, (v*v-u*u*determinant) % modulus
        if bit == '1':
            u, v = (u*trace+v) % modulus, (-u*determinant) % modulus
    return u


rows = []
for p, q in PAIRS:
    local = []
    for r, other in ((p, q), (q, p)):
        zeros = total = 0
        for trace, determinant in itertools.product(range(r), repeat=2):
            if (trace*trace-4*determinant) % r == 0:
                continue
            total += 1
            zeros += lucas(p*q, trace, determinant, r) == 0
        predicted = (r-1)*(other-1)//2 if (r*r-1) % other == 0 else 0
        assert zeros == predicted, (p, q, r, zeros, predicted)
        local.append({'prime': r, 'separable_polynomials': total, 'zero_operators': zeros,
                      'predicted_zero_operators': predicted})
    rows.append({'p': p, 'q': q, 'local': local})

rng = random.Random(285)
checked = 0
for p, q in PAIRS:
    modulus = p*q
    for trial in range(32):
        a = tuple(rng.randrange(modulus) for _ in range(4))
        trace = (a[0]+a[3]) % modulus
        determinant = (a[0]*a[3]-a[1]*a[2]) % modulus
        discriminant = (trace*trace-4*determinant) % modulus
        if math.gcd(discriminant, modulus) != 1:
            continue
        b = ((2*a[0]-trace) % modulus, 2*a[1] % modulus,
             2*a[2] % modulus, (2*a[3]-trace) % modulus)
        u = lucas(modulus, trace, determinant, modulus)
        coefficients = []
        for j in range(4):
            h = tuple(int(i == j) for i in range(4))
            _, tangent = power_jet(a, h, modulus, modulus)
            bhb = multiply(multiply(b, h, modulus), b, modulus)
            predicted = tuple(u*(x-y*pow(discriminant, -1, modulus))*pow(2, -1, modulus) % modulus
                              for x, y in zip(h, bhb))
            assert tangent == predicted, (modulus, a, j, tangent, predicted)
            coefficients.extend(tangent)
        assert math.gcd(modulus, *coefficients) == math.gcd(modulus, u)
        checked += 1

nilpotent_checked = 0
for p, q in PAIRS:
    if p <= 3:
        continue
    modulus = p*q
    for trial in range(16):
        scalar = rng.randrange(modulus)
        a = (scalar, 1, 0, scalar)
        for j in range(4):
            h = tuple(int(i == j) for i in range(4))
            _, tangent = power_jet(a, h, modulus, modulus)
            assert tangent == (0, 0, 0, 0)
        nilpotent_checked += 1

report = {'experiment': 'F285_finite_algebra_operator_search',
          'seed': 285, 'local_exhaustive_counts': rows,
          'matrix_operator_identities_checked': checked,
          'repeated_root_operator_checks': nilpotent_checked,
          'elapsed_seconds': time.monotonic()-started,
          'peak_rss_platform_units': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          'status': 'All exact finite checks passed; no asymptotic theorem inferred from computation.'}
Path(__file__).with_name('results.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
