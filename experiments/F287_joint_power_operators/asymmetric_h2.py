"""Exact asymmetric triple certificate and small comparison counts.
Budget <10 seconds, <128 MB. Factors are offline labels only.
"""
import json
import time
from pathlib import Path
from math import gcd

started=time.monotonic()
scope={}
exec(Path(__file__).with_name('pilot.py').read_text().split('checked=0')[0],scope)
A=[[0,1,1],[1,0,1],[1,2,0]]
C=[[0,1,1],[1,0,1],[1,0,0]]
witness=None
for p,q in [(11,17),(17,23),(23,31),(31,47)]:
    N=p*q
    la={r:scope['derivative'](A,N,r) for r in (p,q)}
    lc={r:scope['derivative'](C,N,r) for r in (p,q)}
    for t in range(2,N):
        u=pow(t,N-1,N)
        if gcd(t*(t-1)*(t*u-1)*(u-1),N)!=1: continue
        f=(t*u*u+2*(t-1)*u-1)%N
        if gcd(f,N) in (1,N): continue
        B=[[0,0,0],[0,1,0],[0,0,t]]
        local=[]
        for r in (p,q):
            lb=scope['derivative'](B,N,r)
            mul,rank=scope['mul'],scope['rank']
            local.append(dict(prime=r,rank_a=rank(la[r],r),rank_b=rank(lb,r),rank_c=rank(lc[r],r),rank_ab=rank(mul(la[r],lb,r),r),rank_bc=rank(mul(lb,lc[r],r),r),rank_abc=rank(mul(mul(la[r],lb,r),lc[r],r),r)))
        if not all(x['rank_a']==x['rank_b']==x['rank_c']==6 for x in local):continue
        assert sorted(x['rank_abc'] for x in local)==[4,5]
        assert all(x['rank_ab']==x['rank_bc']==5 for x in local)
        witness=dict(N=N,t=t,u=u,F2=f,gcd=gcd(f,N),A=A,C=C,locals=local)
        break
    if witness: break
assert witness

# h=2 is not an ordinary power equation in the original t coordinate.
# R2 commutes with 1-v, but exponentiation generally does not.
p=17
N=187
counterexample=dict(prime=p,N=N,t=3,power_of_complement=pow(1-3,N,p),complement_of_power=(1-pow(3,N,p))%p)
assert counterexample['power_of_complement']!=counterexample['complement_of_power']
print(json.dumps(dict(witness=witness,noncommutation=counterexample,elapsed_seconds=time.monotonic()-started),indent=2))
