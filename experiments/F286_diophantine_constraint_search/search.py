"""Exact survivor certificates for a floating-proposal tangent-cut pilot.

F286; closest scoped priors route:F15/P26 and P10.
No hidden factor determines a cut: factors only construct labelled inputs.
Timeout: 55 seconds. Estimated peak memory <64 MB; runtime <30 seconds.
"""
import json
import math
import signal
import time
from fractions import Fraction

signal.alarm(55)
started = time.monotonic()

def prime_after(x):
    while any(x % d == 0 for d in range(2, math.isqrt(x) + 1)):
        x += 1
    return x

menu = [(a, b) for a in range(1, 9) for b in range(1, 9)
        if math.gcd(a, b) == 1]
rows = []
for exponent in (12, 16, 20, 24, 28):
    B = 1 << exponent
    p = prime_after(5 * B // 4)
    q = prime_after(math.isqrt(2*p*p))
    N = p * q
    minima = [(a, b, math.isqrt(4 * a * b * N)) for a, b in menu]
    minima = [(a, b, c + (c*c < 4*a*b*N)) for a, b, c in minima]
    for k in range(2, min(exponent, 13)):
        M = 1 << k
        baseline = certified = proposal_empty = uncertified = components = 0
        exact_boundary_survivors = 0
        certificates = []
        for u in range(1, M, 2):
            v = N * pow(u, -1, M) % M
            xl = B + (u-B) % M
            xh = 2*B - (2*B-u) % M
            yl = B + (v-B) % M
            yh = 2*B - (2*B-v) % M
            if xl*yl > N or xh*yh < N:
                continue
            baseline += 1
            left, right = max(Fraction(xl), Fraction(N, yh)), min(Fraction(xh), Fraction(N, yl))
            spans = [(float(left), float(right))]
            cuts = []
            exact_roots = set()
            for a, b, minimum in minima:
                residue = (a*u+b*v) % M
                t = minimum + (residue-minimum) % M
                cuts.append((a, b, t))
                D = t*t - 4*a*b*N
                if D <= 0:
                    continue
                sd = math.isqrt(D)
                if sd*sd == D:
                    exact_roots.update((Fraction(t-sd,2*a),Fraction(t+sd,2*a)))
                lo = (t-math.sqrt(D))/(2*a)
                hi = (t+math.sqrt(D))/(2*a)
                updated = []
                for l, r in spans:
                    if hi <= l or lo >= r:
                        updated.append((l, r))
                    else:
                        if l < lo:
                            updated.append((l, lo))
                        if hi < r:
                            updated.append((hi, r))
                spans = updated
            components += len(spans)
            boundary_witness = next((x for x in sorted(exact_roots) if left <= x <= right
                                    and all(a*x+b*Fraction(N,1)/x >= t for a,b,t in cuts)), None)
            if boundary_witness is not None:
                exact_boundary_survivors += 1
                certified += 1
                certificates.append([u,boundary_witness.numerator,boundary_witness.denominator])
                continue
            if not spans:
                proposal_empty += 1
                continue
            passed = False
            for l, r in spans:
                x = Fraction((l+r)/2).limit_denominator(1 << 30)
                if left <= x <= right and all(a*x+b*Fraction(N, 1)/x >= t for a,b,t in cuts):
                    passed = True
                    break
            if passed:
                certified += 1
                certificates.append([u,x.numerator,x.denominator])
            else:
                uncertified += 1
        rows.append(dict(B=B,N=N,p_label=p,q_label=q,M=M,states=M//2,
            product_window=baseline,certified_tangent_survivors=certified,
            exact_boundary_survivors=exact_boundary_survivors,
            float_empty=proposal_empty,uncertified=uncertified,components=components,
            certificates=certificates))
print(json.dumps(dict(menu=menu,rows=rows,elapsed_seconds=time.monotonic()-started,
    scope="Survivors have exact rational certificates; empty proposals are numerical observations only."),indent=2))
