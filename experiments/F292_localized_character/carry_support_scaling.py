"""F292 sparse moment recurrence discovery; 30 sec / 64 MiB budget."""
import collections
import json
import math
import random
import signal
import time
from pathlib import Path

signal.alarm(30)
rng=random.Random(2922609)
started=time.monotonic()
cases=[]
for R in (18,22,26,30):
    M=1<<R
    for _ in range(4):
        N=rng.randrange(8*M,16*M)|1
        a,b=64+N%8,65
        T=math.isqrt(4*a*b*N*10201//10000)
        disc=T*T-4*a*b*N
        lo=max(1,(T-math.isqrt(disc))//(2*a)-1)
        hi=(T+math.isqrt(disc))//(2*a)
        largest=max(hi,(T+math.isqrt(disc))//(2*b))
        q=1<<largest.bit_length()
        H=M//q
        carry=collections.Counter()
        scanned=0
        for x in range(lo|1,hi+1,2):
            scanned+=1
            y=N*pow(x,-1,q)%q
            if x*y>=N and a*x+b*y<=T:
                carry[(x*y-N)//q]+=1
        assert all(0<=c<H for c in carry)
        # Integer carry moments avoid finite-field/root-of-unity assumptions.
        # P(z)=product(z-c) annihilates mu_j=sum multiplicity*c**j.
        polynomial=[1]
        for c in carry:
            next_poly=[0]*(len(polynomial)+1)
            for j,coef in enumerate(polynomial):
                next_poly[j]-=c*coef
                next_poly[j+1]+=coef
            polynomial=next_poly
        moments=[sum(weight*c**j for c,weight in carry.items())
                 for j in range(len(polynomial)+3)]
        for shift in range(4):
            assert sum(coef*moments[j+shift] for j,coef in enumerate(polynomial))==0
        cases.append(dict(R=R,M=M,N=N,a=a,b=b,T=T,q=q,H=H,
                          scanned_low_rows=scanned,base_mass=sum(carry.values()),
                          occupied_carries=len(carry),exact_count=carry[0],
                          carry_histogram=dict(sorted(carry.items())),
                          recurrence_degree=len(polynomial)-1,
                          maximum_coefficient_bits=max(abs(x).bit_length() for x in polynomial)))
output=dict(packet="F292",route="F31",seed=2922609,
            runtime_seconds=time.monotonic()-started,cases=cases)
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
