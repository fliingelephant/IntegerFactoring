"""Exact geometry-first frontier certificates; F292 / route:F31.

Budget: 30 seconds / 64 MiB. Scans all low-residue rows; no speed claim.
Public inputs include the retained F290 separating pair.
"""
import json
import math
import signal
import time
from pathlib import Path

signal.alarm(30)
started = time.monotonic()
cases = []
for N in (12827, 12851):
    M, L = 1024, 32
    for a, b in ((1, 1), (67, 65)):
        T = 228 if a == 1 else math.isqrt(4*a*b*N*10201//10000)
        assert T*T < 4*a*b*(N+M)
        points = []
        rows = []
        occupied = set()
        for u in range(1, L, 2):
            v = N * pow(u, -1, L) % L
            row = []
            for X in range(T//(a*L)+1):
                x = u + L*X
                for Y in range(T//(b*L)+1):
                    y = v + L*Y
                    if x*y % M == N % M and x*y >= N and a*x+b*y <= T:
                        points.append([x, y])
                        occupied.add((X, Y))
                        row.append([X, Y])
            if row:
                rows.append(dict(u=u, v=v, high_blocks=row))
        assert all(x*y == N for x,y in points)
        cases.append(dict(N=N,M=M,L=L,a=a,b=b,T=T,
                          scanned_low_rows=L//2,
                          nonzero_low_rows=len(rows),
                          occupied_high_blocks=len(occupied),
                          points=points,rows=rows))
output = dict(packet="F292",route="F31",
              runtime_seconds=time.monotonic()-started,cases=cases)
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
