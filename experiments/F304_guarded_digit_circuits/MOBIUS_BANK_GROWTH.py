"""Distinguish literal degree-two banks, separately from map distinctness."""
import json, random, resource, signal, time
from pathlib import Path
from MOBIUS_BANK import bank
signal.alarm(30); start=time.monotonic(); rng=random.Random(304023); rows=[]
for k in [7,10,13,16,19]:
    M=1<<k; N=rng.randrange(8*M,16*M)|1; r=(k-1)//3; R=1<<r; L=M//R
    moments=set(); carries=set()
    for u0 in range(1,R,2):
        v0=N*pow(u0,-1,R)%R; n=(N-u0*v0)//R
        S,Q,stats=bank(k-r,v0,u0,R,n,2)
        moments.add(tuple(S.values())); carries.add(tuple(Q))
    rows.append(dict(k=k,N=N,r=r,patches=R//2,distinct_moment_banks=len(moments),distinct_carry_banks=len(carries)))
result=dict(rows=rows,runtime_seconds=time.monotonic()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_name('MOBIUS_BANK_GROWTH_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
