"""F323: exact finite certificates for Jerabek Theorem 3.5 and two samplers."""
import collections
import itertools
import json
import math
import signal
import time
from pathlib import Path

signal.alarm(30)
start = time.monotonic()
out = {"seed": None, "randomness": "exhaustive deterministic enumeration",
       "timeout_seconds": 30, "memory_estimate_bytes": 16000000,
       "censored": [], "instances": []}
for n in [21, 33, 77, 161, 209, 341, 437, 589, 65, 85, 221]:
    units = [x for x in range(1, n) if math.gcd(x, n) == 1]
    half = [x for x in units if 2*x < n]
    factors = [p for p in range(2, n) if n % p == 0 and
               all(p % d for d in range(2, math.isqrt(p)+1))]
    # Factors below label outcomes only. Public construction uses Jacobi's algorithm.
    jac = {}
    for x in range(1, n):
        a, m, s = x, n, 1
        while a:
            while a % 2 == 0:
                a //= 2
                if m % 8 in (3, 5):
                    s = -s
            a, m = m, a
            if a % 4 == m % 4 == 3:
                s = -s
            a %= m
        jac[x] = s if m == 1 else 0
    b = next(x for x in range(1, n) if jac[x] == -1)
    coeff = [1, n-1, b]
    fibers = collections.defaultdict(list)
    for i, c in enumerate(coeff):
        for x in range(1, (n-1)//2+1):
            fibers[c*x*x % n if math.gcd(x, n) == 1 else x].append((i, x))
    counts = collections.Counter()
    for fiber in fibers.values():
        for (i, x), (j, y) in itertools.combinations(fiber, 2):
            if math.gcd(x, n) != 1 or math.gcd(y, n) != 1:
                counts['nonunit_factor'] += 1
                continue
            counts['unit_collisions'] += 1
            counts['same_jacobi' if jac[x] == jac[y] else 'opposite_jacobi'] += 1
            if i == j:
                assert 1 < math.gcd(x-y, n) < n
                counts['same_branch_factor'] += 1
            else:
                r = x*pow(y, -1, n) % n
                target = coeff[j]*pow(coeff[i], -1, n) % n
                assert r*r % n == target
                if i == 1 and j == 2:
                    r = coeff[1]*r % n
                    target = coeff[1]*coeff[2] % n
                    assert r*r % n == target
                counts['cross_branch_root'] += 1
    depth = []
    previous = None
    for t in range(1, 9):
        fs = collections.defaultdict(list)
        for x in half:
            fs[pow(x, 1 << t, n)].append(x)
        partition = sorted(sorted(v) for v in fs.values())
        depth.append({'t': t, 'collision_pairs': sum(len(v)*(len(v)-1)//2 for v in fs.values()),
                      'fiber_sizes': dict(collections.Counter(map(len, fs.values()))),
                      'same_partition_as_previous': previous == partition if previous else None,
                      'modular_squarings': t*len(half)})
        previous = partition
    common_seed_checks = 0
    for c in units:
        expected = math.gcd(c*c-1, n)
        for x in units:
            y = c*x % n
            assert math.gcd(x*x-y*y, n) == expected
            common_seed_checks += 1
    blum = len(factors) == 2 and all(p % 4 == 3 for p in factors)
    if blum:
        assert counts['same_jacobi'] == counts['cross_branch_root'] == 0
        assert counts['unit_collisions'] == 3*len(units)//4
        assert all(d['fiber_sizes'] == {2: len(units)//4} for d in depth)
        assert all(d['same_partition_as_previous'] for d in depth[1:])
    out['instances'].append({'N': n, 'offline_prime_labels': factors, 'blum': blum,
       'a': n-1, 'b': b, 'domain_size': 3*(n-1)//2,
       'map_evaluations': 3*(n-1)//2, 'counts': dict(counts),
       'power_depth': depth, 'common_seed_identity_checks': common_seed_checks})
out['elapsed_seconds'] = time.monotonic()-start
out['status'] = 'complete'
Path(__file__).with_name('output.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'status': out['status'], 'instances': len(out['instances']),
                  'elapsed_seconds': out['elapsed_seconds'], 'censored': out['censored']}))
