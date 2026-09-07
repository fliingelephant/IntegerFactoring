"""Exact half-box counts modulo eight; 30 seconds and <256 MiB pilot.

P238 supplies the finite odd-product expansion. P242 supplies transport_bit.
Only small independent controls enumerate graph points. The constructor
uses degree-two Euclidean floor moments and polynomial-size product data.
"""
import ast
from functools import lru_cache
import json
import math
from pathlib import Path
import random
import resource
import signal
import time

signal.alarm(28)
started = time.monotonic()
packet = Path(__file__).resolve().parent
source = packet.parent / "F313_group_log_cocycle"
for filename, names in (("pilot.py", {"group_log"}),
                        ("transport_bit.py", {"floor_sum", "transport_bit"})):
    tree = ast.parse((source / filename).read_text())
    selected = [node for node in tree.body
                if isinstance(node, ast.FunctionDef) and node.name in names]
    exec(compile(ast.Module(body=selected, type_ignores=[]), str(source / filename), "exec"))


def floor_moments(n, m, a, b):
    """Return sum f, sum j*f, sum f^2 for f=floor((a*j+b)/m)."""
    if n == 0:
        return 0, 0, 0
    A, a0 = divmod(a, m)
    B, b0 = divmod(b, m)
    sx = n * (n - 1) // 2
    sxx = n * (n - 1) * (2 * n - 1) // 6
    if A or B:
        y0, y1, y2 = floor_moments(n, m, a0, b0)
        return (A*sx + B*n + y0,
                A*sxx + B*sx + y1,
                A*A*sxx + 2*A*B*sx + B*B*n + 2*A*y1 + 2*B*y0 + y2)
    if a == 0:
        return 0, 0, 0
    height = (a*(n-1) + b) // m
    t0, t1, t2 = floor_moments(height, a, m, m+a-b-1)
    assert (t2-t0) % 2 == 0
    return n*height-t0, height*sx-(t2-t0)//2, n*height*height-2*t1-t0


@lru_cache(None)
def odd_product_guard(R):
    """P238 odd product modulo 8R, never constructing the full product."""
    modulus = 8*R
    length = R//4
    degree = min((modulus.bit_length()-2)//2, length)
    powers = [length]
    for j in range(1, degree+1):
        numerator = length**(j+1) - sum(math.comb(j+1, h)*powers[h] for h in range(j))
        assert numerator % (j+1) == 0
        powers.append(numerator//(j+1))
    elementary = [1]
    for j in range(1, degree+1):
        numerator = sum((-1)**(h-1)*elementary[j-h]*powers[h] for h in range(1, j+1))
        assert numerator % j == 0
        elementary.append(numerator//j)
    product = 1
    for a in (1, 3):
        ratio = 4*pow(a, -1, modulus)
        expansion = sum(elementary[j]*pow(ratio, j, modulus) for j in range(degree+1))
        product = product * pow(a, length, modulus) * expansion % modulus
    return product, degree, max(x.bit_length() for x in powers+elementary)


def half_box(N, R):
    ell, nu = divmod(N, R)
    phi = R//2
    product, degree, product_bits = odd_product_guard(R)
    numerator = (product*product - pow(N, phi, 8*R)) % (8*R)
    assert numerator % R == 0
    H = numerator//R * pow(N, 1-phi, 8) % 8
    J = 0
    for a in (1, 3, 5, 7):
        sf, _, sf2 = floor_moments(R//8, R, 8*nu, a*nu)
        J += sf2+a*sf
    J %= 8
    assert J % 2 == 0
    tbit, _ = transport_bit(nu, R)
    transport = 2*tbit
    b_nu = (2 + nu*(nu-1) + J//2 - nu*transport) % 4
    B = (b_nu-ell*H) % 4
    cubic_parity = int(N % 8 == 1)
    count = (phi-H+2*B-4*cubic_parity) % 8
    return count, dict(H_mod8=H, B_mod4=B, J_mod8=J,
                       T_mod4=transport, cubic_parity=cubic_parity,
                       product_degree=degree, product_integer_bits=product_bits)


rng = random.Random(3182609)
floor_checks = 0
for _ in range(300):
    n = rng.randrange(0, 40)
    m = rng.randrange(1, 50)
    a = rng.randrange(0, 300)
    b = rng.randrange(-100, 300)
    values = [(a*j+b)//m for j in range(n)]
    expected = (sum(values), sum(j*y for j, y in enumerate(values)), sum(y*y for y in values))
    assert floor_moments(n, m, a, b) == expected
    floor_checks += 1

rows = []
count_checks = 0
product_checks = 0
for k in range(3, 13):
    R = 1 << k
    M = 2*R
    product = 1
    for u in range(1, R, 2):
        product = product*u % (8*R)
    assert odd_product_guard(R)[0] == product
    product_checks += 1
    if k <= 7:
        residues = list(range(1, M, 2))
    else:
        residues = sorted({1, 3, 5, 7, M-1} | {rng.randrange(1, M, 2) for _ in range(24)})
    tested = 0
    for r in residues:
        for N in (r, 8*M+r, (1 << (3*k))+r):
            predicted, details = half_box(N, R)
            carry = [(u*(N*pow(u, -1, R) % R)-N)//R for u in range(1, R, 2)]
            actual = sum(N*pow(u, -1, M) % M < R for u in range(1, R, 2))
            assert predicted == actual % 8, (k, N, predicted, actual, details)
            assert details['H_mod8'] == sum(carry) % 8
            assert details['B_mod4'] == sum(q*(q-1)//2 for q in carry) % 4
            assert details['cubic_parity'] == sum(q*(q-1)*(q-2)//6 for q in carry) % 2
            count_checks += 1
            tested += 1
    base = [(u*pow(u, -1, R)-1)//R for u in range(1, R, 2)]
    assert sum(base) % 4 == 2
    assert sum(q*(q-1)//2 for q in base) % 4 == 2
    rows.append(dict(k=k, R=R, graph_modulus=M, residues=residues,
                     full_input_forms=['r', '8*M+r', '2^(3*k)+r'], checked=tested))

large = []
for k in (32, 64, 128, 256):
    R = 1 << k
    M = 2*R
    N = 8*M+((M//3)|1)
    tick = time.monotonic()
    residue, details = half_box(N, R)
    large.append(dict(k=k, graph_modulus=M, N=N, count_mod8=residue,
                      seconds=time.monotonic()-tick, **details))

result = dict(floor_checks=floor_checks, product_checks=product_checks,
              count_checks=count_checks, rows=rows, large=large,
              seconds=time.monotonic()-started,
              peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
(packet/'pilot.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({key:value for key, value in result.items() if key != 'rows'}, indent=2))
