"""F292 exact twisted-window recurrence and seeded short-cap projection.

Budget: 30 seconds / 64 MiB. Integer cyclotomic arithmetic, no float claims.
"""
import collections
import json
import math
import random
import signal
import time
from pathlib import Path

signal.alarm(30)
started = time.monotonic()
rng = random.Random(2922608)
cases = []
recurrence_checks = 0
linear_multiplier_checks = 0
for R in (10, 12, 14, 16, 18):
    M = 1 << R
    inputs = ([12827,12851] if R == 10 else []) + [rng.randrange(8*M,16*M)|1 for _ in range(12)]
    for N in inputs:
        a, b = 64+N%8, 65
        T = math.isqrt(4*a*b*N*10201//10000)
        disc = T*T-4*a*b*N
        largest = max((T+math.isqrt(disc))//(2*a), (T+math.isqrt(disc))//(2*b))
        q = 1 << largest.bit_length()
        H = M//q
        assert q*q >= M and H >= 2 and T*T < 4*a*b*(N+M)
        carry = collections.Counter()
        for x in range(1,q,2):
            y = N*pow(x,-1,q)%q
            if x*y >= N and a*x+b*y <= T:
                carry[(x*y-N)//q] += 1
        assert all(0 <= c < H for c in carry)
        vectors = []
        inverse = pow(N,-1,H)
        for e in range(H):
            vector = [0]*(H//2)
            for c,count in carry.items():
                d = e*c*inverse%H
                vector[d%(H//2)] += count if d<H//2 else -count
            vectors.append(tuple(vector))
        total = [sum(v[j] for v in vectors) for j in range(H//2)]
        assert total == [H*carry[0]] + [0]*(H//2-1)
        direct = sum(1 for x in range(1,largest+1,2)
                     if N%x == 0 and a*x+b*(N//x) <= T)
        assert direct == carry[0]
        cases.append(dict(R=R,M=M,N=N,a=a,b=b,T=T,q=q,H=H,
                          base_cap_mass=sum(carry.values()),
                          nonzero_carries=len(carry),exact_count=carry[0],
                          distinct_twisted_values=len(set(vectors)),
                          carry_histogram=dict(sorted(carry.items()))))
    if R > 12:
        continue
    P = M//4
    logs = {}
    unit = 1
    for j in range(P):
        logs[unit] = logs[-unit%M] = j
        unit = unit*5%M
    for N in inputs[:4]:
        a,b=64+N%8,65
        T=math.isqrt(4*a*b*N*10201//10000)
        for m in range(R//2+1,R+1):
            modulus,L=1<<m,1<<(m-1)
            K=M//L
            beta=logs[1+L]//(P//K)
            for e in (0,1,3):
                direct=[0]*(P//2)
                rhs=[0]*(P//2)
                for u in range(1,modulus,2):
                    v=N*pow(u,-1,modulus)%modulus
                    if u*v>=N and a*u+b*v<=T:
                        d=e*(logs[u]+logs[v]-logs[N%M])%P
                        direct[d%(P//2)]+=1 if d<P//2 else -1
                for u in range(1,L,2):
                    v=N*pow(u,-1,L)%L
                    base=logs[u]+logs[v]-logs[N%M]
                    for eps in (0,1):
                        for eta in (0,1):
                            x,y=u+eps*L,v+eta*L
                            increment=(logs[x]-logs[u]+logs[y]-logs[v])%P
                            predicted=(P//K)*beta*(eps*v+eta*u)*pow(N,-1,K)%P
                            assert increment == predicted
                            linear_multiplier_checks+=1
                            if x*y<N or a*x+b*y>T:
                                continue
                            for extra,sgn in ((0,1),(1<<(R-m),(-1)**(eps+eta))):
                                d=((e+extra)*base+e*increment)%P
                                rhs[d%(P//2)]+=sgn*(1 if d<P//2 else -1)
                assert rhs == [2*z for z in direct]
                recurrence_checks+=1
output=dict(packet="F292",route="F31",seed=2922608,
            runtime_seconds=time.monotonic()-started,
            recurrence_checks=recurrence_checks,
            linear_multiplier_checks=linear_multiplier_checks,cases=cases)
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
