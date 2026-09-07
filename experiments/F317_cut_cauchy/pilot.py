"""F317 / route:F31: precision-local progression products and Cauchy entries.

Pilot budget: 30 seconds, estimated below 256 MiB. No scalar-sum speed claim.
"""
from fractions import Fraction
from math import comb, factorial, prod
from pathlib import Path
import json, resource, signal, time

signal.alarm(30)
started = time.monotonic()


def odd_product(c, step, m, p):
    """Product of an odd arithmetic progression, modulo 2**p."""
    modulus = 1 << p
    if not m:
        return 1
    degree = min(m, p - 1)
    # Exact power sums and Newton identities. Their bit sizes are O(p log m).
    powers = [m]
    for k in range(1, degree + 1):
        powers.append((m ** (k + 1) - sum(comb(k + 1, j) * powers[j]
                                        for j in range(k))) // (k + 1))
    elementary = [1]
    for k in range(1, degree + 1):
        numerator = sum((-1) ** (j - 1) * elementary[k-j] * powers[j]
                        for j in range(1, k + 1))
        assert numerator % k == 0
        elementary.append(numerator // k)
    ratio = step * pow(c, -1, modulus) % modulus
    return pow(c, m, modulus) * sum(e * pow(ratio, k, modulus)
                                   for k, e in enumerate(elementary)) % modulus


def progression(a, b, length, p):
    """Return the exact valuation and modular odd part; None means zero."""
    if a % b == 0 and 0 <= -a // b < length:
        return None
    valuation, unit = 0, 1
    modulus = 1 << p
    while length:
        parity = a & 1
        even_count = (length + 1 - parity) // 2
        odd_start = 1 - parity
        odd_count = (length + 1 - odd_start) // 2
        unit = unit * odd_product(a + b * odd_start, 2 * b, odd_count, p) % modulus
        valuation += even_count
        a = (a + b * parity) // 2
        length = even_count
    return valuation, unit


def entry(g, s, i, j, p):
    alpha, beta, gamma, delta = g
    length = 1 << s
    d = length - 1
    determinant = alpha * delta - beta * gamma
    bij = alpha*i + beta - (gamma*i + delta)*j
    if bij == 0:
        return 1
    row = progression(alpha*i + beta, -(gamma*i + delta), length, p)
    column = progression(beta - delta*j, alpha - gamma*j, length, p)
    if row is None or column is None:
        return 0
    denominator = 1
    for n in (i, d-i, j, d-j):
        denominator *= progression(1, 1, n, p)[1]
    vbij = (abs(bij) & -abs(bij)).bit_length() - 1
    valuation = row[0] + column[0] - 2*(d-s) - 2*vbij
    assert valuation >= 0
    if valuation >= p:
        return 0
    modulus = 1 << p
    denominator *= (-1) ** (i+j) * (bij >> vbij) ** 2
    denominator *= pow(-determinant, d, modulus)
    return ((row[1] * column[1] * pow(denominator, -1, modulus)) << valuation) % modulus


checks = 0
for p in (1, 2, 5, 12):
    for a in (-19, -4, 0, 1, 18):
        for b in (-7, -1, 1, 5):
            for length in (0, 1, 2, 9, 32):
                actual = prod(a + b*k for k in range(length))
                obtained = progression(a, b, length, p)
                if actual == 0:
                    assert obtained is None
                else:
                    v = (abs(actual) & -abs(actual)).bit_length()-1
                    assert obtained == (v, (actual >> v) % (1 << p))
                checks += 1

cases = []
for s in (1, 2, 3, 4):
    length = 1 << s
    d = length-1
    for g in ((1, 0, 0, 1), (1, 1, 2, 1), (-3, 7, 2, 5)):
        alpha, beta, gamma, delta = g
        determinant = alpha*delta-beta*gamma
        zeros = 0
        for i in range(length):
            for j in range(length):
                row = prod(alpha*i+beta-(gamma*i+delta)*r for r in range(length) if r != j)
                column = prod(alpha*r+beta-(gamma*r+delta)*j for r in range(length) if r != i)
                denominator = ((-determinant)**d * (-1)**(i+j)
                               * factorial(i)*factorial(d-i)*factorial(j)*factorial(d-j))
                z = Fraction(row*column, denominator)
                assert z.denominator & 1
                zeros += alpha*i+beta-(gamma*i+delta)*j == 0
                for p in (2, 5, 12):
                    assert entry(g,s,i,j,p) == z.numerator*pow(z.denominator,-1,1<<p) % (1<<p)
                    checks += 1
                if z and (alpha*i+beta-(gamma*i+delta)*j) % length:
                    v = (abs(z.numerator) & -abs(z.numerator)).bit_length()-1
                    bij = alpha*i+beta-(gamma*i+delta)*j
                    vb = (abs(bij) & -abs(bij)).bit_length()-1
                    assert v >= 2*(s-vb)
                    checks += 1
        cases.append(dict(s=s,g=g,exact_zero_pairs=zeros))

large = []
for s, p in ((40, 12), (80, 20)):
    g = (-3, 7, 2, 5)
    i = (1 << (s-1)) + 11
    j = (g[0]*i+g[1])*pow(g[2]*i+g[3], -1, 1<<s) % (1<<s)
    before = time.monotonic()
    z = entry(g,s,i,j,p)
    assert z % 4 == 1
    large.append(dict(s=s,p=p,i=i,j=j,z=z,seconds=time.monotonic()-before))

block_checks = 0
for g in ((1,1,2,1),(-3,7,2,5)):
    alpha,beta,gamma,delta = g
    for h in range(1,6):
        base = 1 << h
        for t in range(1,h+1):
            modulus = base << t
            for i0 in range(base):
                d0 = gamma*i0+delta
                y0 = (alpha*i0+beta)*pow(d0,-1,base)%base
                e0 = alpha-gamma*y0
                q0 = (alpha*i0+beta-d0*y0)//base
                for u in range(1<<t):
                    actual = (alpha*(i0+base*u)+beta)*pow(gamma*(i0+base*u)+delta,-1,modulus)%modulus
                    v = (q0+e0*u)*pow(d0,-1,1<<t)%(1<<t)
                    assert actual == y0+base*v
                    block_checks += 1
# Same one-bit normalized state, different next zero-input branch state.
carry_collision = []
for i0 in (3,5):
    base,alpha,beta,gamma,delta = 8,-3,7,2,5
    d0 = gamma*i0+delta
    y0 = (alpha*i0+beta)*pow(d0,-1,base)%base
    e0 = alpha-gamma*y0
    q0 = (alpha*i0+beta-d0*y0)//base
    v = q0%2
    carry_collision.append(dict(i0=i0,y0=y0,D=d0,E=e0,q=q0,
                                state=[d0%2,e0%2,q0%2],next_q_bit=((q0-d0*v)//2)%2))
assert carry_collision[0]['state'] == carry_collision[1]['state']
assert carry_collision[0]['next_q_bit'] != carry_collision[1]['next_q_bit']

result = dict(experiment='F317_cut_cauchy',route='route:F31',checks=checks,
              block_checks=block_checks,carry_collision=carry_collision,
              cases=cases,large_entry_pilots=large,seconds=time.monotonic()-started,
              peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_name('pilot.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
