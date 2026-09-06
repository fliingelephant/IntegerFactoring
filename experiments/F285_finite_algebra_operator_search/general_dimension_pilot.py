"""F285 general-d companion matrices; factors used only as offline labels."""
import json
import random
import resource
import signal
import time
from pathlib import Path

signal.alarm(10)
start = time.monotonic()
rng = random.Random(28502)


def product(a, b, modulus):
    d = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(d)) % modulus
             for j in range(d)] for i in range(d)]


def plus(a, b, modulus):
    return [[(x+y) % modulus for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def derivative(a, exponent, modulus):
    d = len(a)
    columns = []
    for pos in range(d*d):
        h = [[int(i*d+j == pos) for j in range(d)] for i in range(d)]
        v = [[int(i == j) for j in range(d)] for i in range(d)]
        z = [[0]*d for _ in range(d)]
        for bit in bin(exponent)[2:]:
            z = plus(product(v, z, modulus), product(z, v, modulus), modulus)
            v = product(v, v, modulus)
            if bit == '1':
                z = plus(product(z, a, modulus), product(v, h, modulus), modulus)
                v = product(v, a, modulus)
        columns.append([x for row in z for x in row])
    return [list(row) for row in zip(*columns)], v


def rank(a, prime):
    a = [[v % prime for v in row] for row in a]
    pivot = 0
    for col in range(len(a[0])):
        row = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if row is None:
            continue
        a[pivot], a[row] = a[row], a[pivot]
        inv = pow(a[pivot][col], -1, prime)
        a[pivot] = [v*inv % prime for v in a[pivot]]
        for i in range(pivot+1, len(a)):
            scale = a[i][col]
            a[i] = [(x-scale*y) % prime for x, y in zip(a[i], a[pivot])]
        pivot += 1
    return pivot


def remainder(a, b, prime):
    a = [x % prime for x in a]
    while a and a[-1] == 0:
        a.pop()
    inv = pow(b[-1], -1, prime)
    while len(a) >= len(b):
        shift, scale = len(a)-len(b), a[-1]*inv % prime
        for i in range(len(b)):
            a[i+shift] = (a[i+shift]-scale*b[i]) % prime
        while a and a[-1] == 0:
            a.pop()
    return a


def order(base, prime):
    residue = base % prime
    k = 1
    while residue != 1:
        residue = residue*base % prime
        k += 1
    return k


rows = []
for p, q in [(5, 7), (5, 11), (5, 13), (7, 11), (7, 13), (11, 17)]:
    modulus = p*q
    for d in (2, 3, 4):
        hist = {}
        accepted = 0
        for trial in range(8):
            coeff = [rng.randrange(modulus) for _ in range(d)]+[1]
            separable = True
            for r in (p, q):
                a = [x % r for x in coeff]
                b = [(i*coeff[i]) % r for i in range(1, d+1)]
                while b:
                    a, b = b, remainder(a, b, r)
                separable &= len(a) == 1
            if not separable:
                continue
            a = [[0]*d for _ in range(d)]
            for i in range(d):
                a[i][d-1] = -coeff[i] % modulus
                if i:
                    a[i][i-1] = 1
            operator, powered = derivative(a, modulus, modulus)
            commutator_columns = []
            for pos in range(d*d):
                h = [[int(i*d+j == pos) for j in range(d)] for i in range(d)]
                left, right = product(powered, h, modulus), product(h, powered, modulus)
                commutator_columns.append([(left[i][j]-right[i][j]) % modulus
                                           for i in range(d) for j in range(d)])
            commutator = [list(row) for row in zip(*commutator_columns)]
            ranks = (rank(operator, p), rank(operator, q))
            assert ranks == (rank(commutator, p), rank(commutator, q))
            for r, s, observed in ((p, q, ranks[0]), (q, p, ranks[1])):
                if order(r, s) > d:
                    assert observed == d*d-d, (p, q, d, coeff, ranks)
            key = ','.join(map(str, ranks))
            hist[key] = hist.get(key, 0)+1
            accepted += 1
        rows.append({'p': p, 'q': q, 'dimension': d,
                     'ord_q_p': order(p, q), 'ord_p_q': order(q, p),
                     'separable_samples': accepted, 'rank_histogram': hist})

report = {'seed': 28502, 'rows': rows, 'elapsed_seconds': time.monotonic()-start,
          'peak_rss_platform_units': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          'status': 'All general-d rank-law assertions passed; finite checks only.'}
Path(__file__).with_name('general_dimension_results.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
