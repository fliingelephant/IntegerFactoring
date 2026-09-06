"""F300 / route:F31: exact complete and Cauchy-weighted Gauss/Salié sums.

One process, <128 MiB, estimated<5s; 30-second alarm. Fresh preflight:
05:56 local, load2.25/2.11/2.03,73% available memory, no numerical process.
"""

import json
import random
import resource
import signal
import time
from pathlib import Path

signal.alarm(30)
started = time.monotonic()
rng = random.Random(300260907)
rows = []


def add(vector, exponent, coefficient, modulus):
    exponent %= modulus
    vector[exponent % (modulus//2)] += coefficient if exponent < modulus//2 else -coefficient


for k in range(3, 9):
    m = 1 << k
    half = m//2
    for trial in range(12):
        gamma, d = rng.randrange(1, m, 2), rng.randrange(1, m, 2)
        V = rng.randrange(m)
        w = (0, 1, 2, half)[trial] if trial < 4 else rng.randrange(m)
        complete, weighted = [0]*half, [0]*half
        twice_weighted = [0]*half
        for b in range(1, m, 2):
            phase = (-w*w*pow(b*gamma, -1, m)+V*b) % m
            if k % 2:
                amplitude = 1 << ((k+1)//2)
                gauss_phases = [((b*gamma) % 8)*(m//8)]
            else:
                amplitude = 1 << (k//2)
                gauss_phases = [0, ((b*gamma) % 4)*(m//4)]
            for gphase in gauss_phases:
                add(complete, phase+gphase, amplitude, m)
                for j in range(half):
                    add(weighted, phase+gphase-d*b*j, amplitude//2, m)
                    if k <= 5 and trial < 3:
                        for h in range(half):
                            add(twice_weighted, phase+gphase-d*b*j-b*h, amplitude//4, m)
        complete_rhs, weighted_rhs = [0]*half, [0]*half
        double_rhs = [0]*half
        parity_part = [0]*half
        d_inverse = pow(d, -1, m)
        for x in range(m):
            value = (gamma*x*x+V) % m
            add(complete_rhs, 2*w*x, half*((value == 0)-(value == half)), m)
            sign = 1 if (d_inverse*value) % m < half else -1
            add(weighted_rhs, 2*w*x, (m//4)*sign, m)
            if x % 2 == w % 2:
                add(parity_part, 2*w*x, (m//4)*sign, m)
            if k <= 5 and trial < 3:
                window_count = sum((value-d*h) % m < half for h in range(half))
                add(double_rhs, 2*w*x, (m//4)*(window_count-m//4), m)
        assert complete == complete_rhs
        assert weighted == weighted_rhs
        if k >= 4:
            assert weighted == parity_part
        if k <= 5 and trial < 3:
            assert twice_weighted == double_rhs
        rows.append({"m":m,"gamma":gamma,"d":d,"V":V,"w":w,
                     "complete_coefficients":{str(i):v for i,v in enumerate(complete) if v},
                     "weighted_coefficients":{str(i):v for i,v in enumerate(weighted) if v},
                     "two_denominators_checked":k <= 5 and trial < 3,
                     "parity_filter_checked":k >= 4})

result = {"status":"complete","family":"route:F31","seed":300260907,
          "scope":"Exact identities in Z[X]/(X^(m/2)+1); the reference sums enumerate numerical ranges.",
          "cases":rows,"runtime_seconds":time.monotonic()-started,
          "peak_rss_bytes":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({"status":"complete","complete_checks":len(rows),
                  "one_denominator_checks":len(rows),
                  "two_denominator_checks":sum(row["two_denominators_checked"] for row in rows),
                  "parity_checks":sum(row["parity_filter_checked"] for row in rows),
                  "runtime_seconds":result["runtime_seconds"],"peak_rss_bytes":result["peak_rss_bytes"]}))
