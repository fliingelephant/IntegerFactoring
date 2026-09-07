"""F320: exact energy moments and exhaustive two-bank collision checks."""
import itertools
import json
import math
import signal
import time
from fractions import Fraction
from pathlib import Path

signal.alarm(30)
start = time.monotonic()
rows = []
for n in (9, 15, 25, 27, 45, 49, 77, 121, 143, 303, 10403):
    w = [math.gcd(k, n) for k in range(n)]
    h = [g - 1 if k else 0 for k, g in enumerate(w)]
    s = sum(w)
    mu = Fraction(sum(h), n)
    var = Fraction(sum(x*x for x in h), n) - mu*mu
    divisors = [d for d in range(1, n+1) if n % d == 0]
    phi = lambda a: sum(math.gcd(k, a) == 1 for k in range(a))
    assert s == sum(d*phi(n//d) for d in divisors)
    assert sum(x*x for x in h) == sum((d-1)**2*phi(n//d) for d in divisors if d<n)
    block = []
    for b in (1, 2, 4, 8, 16):
        if b > n:
            continue
        totals = [sum(h[(a+j) % n] for j in range(b)) for a in range(n)]
        bv = Fraction(sum(t*t for t in totals), n*b*b)-mu*mu
        block.append({'B': b, 'relative_variance': str(bv/(mu*mu))})
    rows.append({'N': n, 'S': s, 'proper_mass': str(Fraction(sum(g for g in w if 1<g<n),s)),
                 'control_mean': str(mu), 'control_relative_variance': str(var/(mu*mu)), 'blocks': block})

collision = []
for n in (9, 15):
    alpha = Fraction(sum(1<math.gcd(k,n)<n for k in range(n)), n)
    zsum = z2sum = hits = 0
    for a,b,c,d in itertools.product(range(n), repeat=4):
        z = sum(1<math.gcd(x-y,n)<n for x in (a,b) for y in (c,d))
        zsum += z
        z2sum += z*z
        hits += z>0
    mean = Fraction(zsum, n**4)
    variance = Fraction(z2sum, n**4)-mean*mean
    assert mean == 4*alpha
    assert variance == 4*alpha*(1-alpha)
    assert Fraction(hits,n**4) >= mean/(mean+1-alpha)
    collision.append({'N':n, 'm':2, 'mean':str(mean), 'variance':str(variance),
                      'success':str(Fraction(hits,n**4)), 'second_moment_lower_bound':str(mean/(mean+1-alpha))})
out = {'scope':'Exact finite checks; no unbounded runtime certification', 'energy': rows,
       'collision': collision, 'seconds':time.monotonic()-start}
Path(__file__).with_name('output.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'status':'PASS', 'energy_inputs':len(rows), 'exhaustive_bank_inputs':len(collision), 'seconds':out['seconds']}))
