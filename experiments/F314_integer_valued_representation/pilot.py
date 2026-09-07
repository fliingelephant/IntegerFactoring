"""F314 / route:F31: exact bounded representation and precision checks."""
from fractions import Fraction as F
from math import comb, factorial
import json, resource, signal, time
from pathlib import Path

signal.alarm(30)
started = time.monotonic()
cases = []
first_mod8_failure = None
checks = 0
for L in (2, 4, 8, 16):
    d = L - 1
    for A, B, C, n in ((1, 1, 2, 1), (1, 1, 2, 4), (3, 5, 2, 7)):
        # R is weighted substitution in the exact Lagrange node basis.
        mats = []
        K = A * B + C * n
        for a, b, c, e, scale in ((-A, n, C, B, 1), (B, -n, -C, -A, F(1, (-K) ** d))):
            rows = []
            for i in range(L):
                row = []
                for j in range(L):
                    val = F((-1) ** (d-j), factorial(j) * factorial(d-j)) * scale
                    for k in range(L):
                        if k != j:
                            val *= a * i + b - k * (c * i + e)
                    row.append(val)
                rows.append(row)
            mats.append(rows)
        R, S = mats
        for i in range(L):
            for j in range(L):
                assert sum(R[i][k] * S[k][j] for k in range(L)) == int(i == j)
                assert R[i][j].denominator % 2 == 1
                checks += 1
        y = [(n-A*i) * pow(B+C*i, -1, L) % L for i in range(L)]
        weights = [[R[i][j] * S[j][i] for j in range(L)] for i in range(L)]
        for h in range(L+1):
            for k in range(L+1):
                trace = sum((weights[i][j] for i in range(h) for j in range(k)), F(0))
                count = sum(y[i] < k for i in range(h))
                assert (trace.numerator * pow(trace.denominator, -1, 4) - count) % 4 == 0
                checks += 1
                if first_mod8_failure is None and (trace.numerator * pow(trace.denominator, -1, 8)-count) % 8:
                    first_mod8_failure = dict(L=L,A=A,B=B,C=C,n=n,h=h,k=k,trace=str(trace),count=count,
                                             R=[[str(v) for v in row] for row in R],
                                             inverse=[[str(v) for v in row] for row in S])
        # Polynomial idempotent lift, verified at precision up to twelve.
        for p in range(1,13):
            modulus = 1 << p
            m = (p+1)//2
            for i in range(L):
                for j in range(L):
                    z = weights[i][j]
                    z = z.numerator * pow(z.denominator, -1, modulus) % modulus
                    lifted = sum(comb(2*m-1,t)*pow(z,t,modulus)*pow(1-z,2*m-1-t,modulus)
                                 for t in range(m,2*m)) % modulus
                    assert lifted == int(y[i] == j)
                    checks += 1
        # Pascal conjugate of a prefix projector: exact Cauchy formula.
        for h in range(1,L):
            for i in range(L):
                for j in range(i+1):
                    actual = sum((-1)**(i-t)*comb(i,t)*comb(t,j) for t in range(j,min(i,h-1)+1))
                    if i < h:
                        expected = int(i == j)
                    elif j >= h:
                        expected = 0
                    else:
                        expected = (-1)**(i+h-1)*comb(i,j)*comb(i-j-1,h-1-j)
                    assert actual == expected
                    checks += 1
        cases.append(dict(L=L,A=A,B=B,C=C,n=n))
result = dict(route='route:F31',experiment='F314_integer_valued_representation',
              cases=cases,checks=checks,first_mod8_failure=first_mod8_failure,
              seconds=time.monotonic()-started,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_name('pilot.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
