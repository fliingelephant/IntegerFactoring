"""Bounded exact sweep; prime factors are offline field labels only.

Budget: 30 seconds, <128 MB. Deadline 25 seconds. No external packages.
"""
import json
import time
from collections import Counter
from math import gcd

started=time.monotonic()
primes=[p for p in range(5,1501) if all(p%d for d in range(2,int(p**0.5)+1))]
pairs=[(p,q) for p in primes for q in primes if p<q<2*p]
pairs.sort(key=lambda pq:(gcd(pq[0]-1,pq[1]-1)!=2,pq[0],pq[1]))
hist=Counter()
top=[]
first_over4=None
completed=0
field_count=0

def order(t,p):
    x=t%p
    k=1
    while x!=1:
        x=x*t%p
        k+=1
    return k

for p,q in pairs:
    if time.monotonic()-started>25: break
    for ell,r in [(p,q),(q,p)]:
        e=r%(ell-1)
        roots=[]
        for t in range(2,ell):
            v=pow(t,e,ell)
            if v!=1 and (v*v+3*(t-1)*v-t)%ell==0:
                roots.append(t)
        assert all(pow(t,-1,ell) in roots for t in roots)
        assert all(pow(t,e,ell)!=t for t in roots)
        z=len(roots)
        hist[z]+=1
        field_count+=1
        row=dict(p=p,q=q,field=ell,other=r,reduced_exponent=e,shared_gcd=gcd(p-1,q-1),count=z,roots=roots)
        if z>4 and first_over4 is None: first_over4=row
        if len(top)<20 or z>top[-1]['count']:
            top.append(row)
            top.sort(key=lambda x:-x['count'])
            top=top[:20]
    completed+=1
for row in top:
    row['orders']=[order(t,row['field']) for t in row['roots']]
    row['reciprocal_pairs']=[(t,pow(t,-1,row['field'])) for t in row['roots'] if t<pow(t,-1,row['field'])]
if first_over4:
    first_over4['orders']=[order(t,first_over4['field']) for t in first_over4['roots']]
print(json.dumps(dict(scope='Finite sweep only; timeout gives a deterministic prefix',prime_limit=1500,pair_count=completed,total_pairs=len(pairs),field_count=field_count,histogram=dict(sorted(hist.items())),first_over4=first_over4,largest=top,elapsed_seconds=time.monotonic()-started),indent=2))
