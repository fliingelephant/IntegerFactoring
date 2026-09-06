"""Exact local enumeration; factors label the fields only.
Budget <30 seconds, <128 MB. No external libraries.
"""
import json
import time
from math import gcd
from pathlib import Path

start=time.monotonic()

def prime(n):
    return n>=2 and all(n%d for d in range(2,int(n**0.5)+1))

def order(a,p):
    x=a%p
    k=1
    while x!=1:
        x=x*a%p
        k+=1
    return k

def local(p,r):
    roots=[]
    eligible=[]
    nonfermat=[]
    for t in range(2,p):
        v=pow(t,r,p)
        if v==1: continue
        eligible.append(t)
        if v!=t: nonfermat.append(t)
        if (v*v+3*(t-1)*v-t)%p==0: roots.append(t)
    assert all(pow(t,-1,p) in roots for t in roots)
    return dict(prime=p,other_prime=r,mutual_order=order(r,p),eligible=len(eligible),nonfermat=len(nonfermat),roots=roots,root_orders=[order(t,p) for t in roots])

rows=[]
for p,q in [(7,11),(11,17),(17,23),(23,31),(31,47),(47,67),(67,101),(101,149),(149,211),(211,307),(307,431),(431,613),(613,887),(887,1259),(1259,1783),(1783,2521)]:
    assert prime(p) and prime(q) and p<q<2*p
    assert time.monotonic()-start<25
    a,b=local(p,q),local(q,p)
    ra,rb=len(a['roots']),len(b['roots'])
    ea,eb=a['eligible'],b['eligible']
    na,nb=a['nonfermat'],b['nonfermat']
    fa,fb=ea-na,eb-nb
    rows.append(dict(p=p,q=q,local_p=a,local_q=b,both_orders_above3=min(a['mutual_order'],b['mutual_order'])>3,q_not_2p_minus1=q!=2*p-1,split_on_eligible=[ra*(eb-rb)+rb*(ea-ra),ea*eb],fermat_split_on_eligible=[fa*nb+fb*na,ea*eb],fermat_gcd1_count=na*nb,F_split_given_fermat_gcd1=[ra*(nb-rb)+rb*(na-ra),na*nb]))

# A separate bounded matrix certificate uses the same public t family.
# Read only function definitions from the retained direct block-power pilot.
source=Path(__file__).with_name('pilot.py').read_text().split('checked=0')[0]
scope={}
exec(source,scope)
witness=None
for row in rows:
    if not row['both_orders_above3'] or not row['q_not_2p_minus1']: continue
    p,q=row['p'],row['q']
    n=p*q
    if gcd(n,13)>1: continue
    a=scope['A']
    la={r:scope['derivative'](a,n,r) for r in (p,q)}
    if any(scope['rank'](la[r],r)!=6 for r in (p,q)): continue
    for t in range(2,min(n,10000)):
        if time.monotonic()-start>25: raise RuntimeError('budget')
        u=pow(t,n-1,n)
        if gcd(t*(t-1)*(t*u-1)*(u-1),n)!=1: continue
        f=(t*u*u+3*(t-1)*u-1)%n
        if gcd(f,n) in (1,n): continue
        b=[[0,0,0],[0,1,0],[0,0,t]]
        records=[]
        for r in (p,q):
            lb=scope['derivative'](b,n,r)
            mul,rank=scope['mul'],scope['rank']
            records.append(dict(prime=r,rank_a=rank(la[r],r),rank_b=rank(lb,r),rank_ab=rank(mul(la[r],lb,r),r),rank_ba=rank(mul(lb,la[r],r),r),rank_aba=rank(mul(mul(la[r],lb,r),la[r],r),r)))
        witness=dict(N=n,p=p,q=q,t=t,u=u,F=f,gcd=gcd(f,n),mutual_orders=[row['local_p']['mutual_order'],row['local_q']['mutual_order']],fermat_gcd=gcd(u-1,n),locals=records)
        assert sorted(x['rank_aba'] for x in records)==[4,5]
        break
    if witness: break
assert witness
twins=[]
for p in [5,11,17,29,41,59,71,101,107,137,149,179,191,197,227,239]:
    q=p+2
    assert prime(p) and prime(q)
    a,b=local(p,q),local(q,p)
    xs=[x for x in range(p) if (x*x+x+2)%p==0]
    predicted=sum(1+(0 if (x*x-4)%p==0 else (1 if pow((x*x-4)%p,(p-1)//2,p)==1 else -1)) for x in xs)
    assert predicted==len(a['roots']) and not b['roots']
    twins.append(dict(p=p,q=q,x_roots=xs,p_root_count=predicted,q_root_count=0,conditional_split=[predicted,p-3]))
print(json.dumps(dict(scope='Exact finite local counts and certificate, no asymptotic inference',rows=rows,twins=twins,witness=witness,elapsed_seconds=time.monotonic()-start),indent=2))
