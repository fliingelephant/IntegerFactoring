"""F292 / route:F31: exact balanced binary-frontier rank pilot.

Budget: 30 seconds, 64 MiB. No hidden factor labels. Gram ranks modulo
1000003 certify lower bounds for characteristic-zero row ranks.
"""
import json
import math
import signal
import time
from pathlib import Path

signal.alarm(30)
started = time.monotonic()
prime = 1000003
results = []
for t in range(3, 9):
    L = 1 << t
    for N in (1, 3, 11, L * L // 3 | 1, L * L - 1):
        lines = []
        for u in range(1, L, 2):
            v = N * pow(u, -1, L) % L
            c = (N - u * v) // L % L
            inverse = pow(u, -1, L)
            lines.append((v * inverse % L, c * inverse % L))
        gram = []
        for s, d in lines:
            row = []
            for ss, dd in lines:
                g = math.gcd(s - ss, L)
                row.append(g if (d - dd) % g == 0 else 0)
            gram.append(row)
        rank = 0
        for j in range(len(lines)):
            pivot = next((i for i in range(rank, len(lines))
                          if gram[i][j] % prime), None)
            if pivot is None:
                continue
            gram[rank], gram[pivot] = gram[pivot], gram[rank]
            row = gram[rank]
            inv = pow(row[j], -1, prime)
            for i in range(rank + 1, len(lines)):
                q = gram[i][j] * inv % prime
                if q:
                    gram[i][j:] = [(a - q * b) % prime
                                   for a, b in zip(gram[i][j:], row[j:])]
            rank += 1
        distinct_slopes = len({s for s, d in lines})
        assert distinct_slopes == L // 8
        assert rank >= distinct_slopes
        results.append(dict(t=t, L=L, M=L*L, N=N, rows=L//2,
                            distinct_lines=len(set(lines)),
                            primitive_directions=distinct_slopes,
                            gram_rank_mod_prime=rank))
output = dict(packet="F292", route="F31", prime=prime,
              runtime_seconds=time.monotonic()-started, results=results)
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps(output, indent=2))
