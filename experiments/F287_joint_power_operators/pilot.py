"""Exact tiny finite certificate; factors are offline labels only.

Budget: 60 seconds, <512 MB; actual matrices have dimension at most 9.
Public family A is fixed, B=diag(0,1,t), N alone selects the exponent.
"""
import json
import time
from math import gcd

started = time.monotonic()
A = [[0,1,1],[1,0,1],[1,2,0]]

def mul(a,b,p):
    return [[sum(x*y for x,y in zip(row,col))%p for col in zip(*b)] for row in a]

def power(a,n,p):
    r=[[int(i==j) for j in range(len(a))] for i in range(len(a))]
    while n:
        if n&1: r=mul(r,a,p)
        a=mul(a,a,p)
        n//=2
    return r

def derivative(a,n,p):
    cols=[]
    for k in range(9):
        h=[[int(3*i+j==k) for j in range(3)] for i in range(3)]
        block=[a[i]+h[i] for i in range(3)]+[[0]*3+a[i] for i in range(3)]
        out=power(block,n,p)
        cols.append([out[i][j+3] for i in range(3) for j in range(3)])
    return [list(x) for x in zip(*cols)]

def rank(a,p):
    a=[row[:] for row in a]
    r=0
    for c in range(len(a[0])):
        k=next((k for k in range(r,len(a)) if a[k][c]%p),None)
        if k is None: continue
        a[r],a[k]=a[k],a[r]
        v=pow(a[r][c],-1,p)
        a[r]=[x*v%p for x in a[r]]
        for k in range(len(a)):
            if k!=r:
                v=a[k][c]
                a[k]=[(x-v*y)%p for x,y in zip(a[k],a[r])]
        r+=1
    return r

checked=0
witness=None
for p,q in [(5,7),(5,11),(7,11),(7,17),(11,17),(17,19),(19,23),(23,29),(29,31)]:
    n=p*q
    if gcd(13,n)!=1: continue
    la={r:derivative(A,n,r) for r in (p,q)}
    if any(rank(la[r],r)!=6 for r in (p,q)): continue
    for t in range(2,n):
        if time.monotonic()-started>50: raise RuntimeError('pilot budget')
        u=pow(t,n-1,n)
        if gcd(t*(t-1)*u*(t*u-1),n)!=1: continue
        f=(t*u*u+3*(t-1)*u-1)%n
        g=gcd(f,n)
        checked+=1
        if g in (1,n): continue
        b=[[0,0,0],[0,1,0],[0,0,t]]
        local=[]
        for r in (p,q):
            lb=derivative(b,n,r)
            local.append(dict(prime=r,u=u%r,f=f%r,rank_a=rank(la[r],r),rank_b=rank(lb,r),rank_ab=rank(mul(la[r],lb,r),r),rank_ba=rank(mul(lb,la[r],r),r),rank_aba=rank(mul(mul(la[r],lb,r),la[r],r),r)))
        witness=dict(N=n,t=t,A=A,B=b,u=u,F=f,gcd=g,locals=local)
        break
    if witness: break
result=dict(scope='Exact finite certificate only; not a probability theorem',checked=checked,witness=witness,elapsed_seconds=time.monotonic()-started)
print(json.dumps(result,indent=2))
assert witness and sorted(x['rank_aba'] for x in witness['locals'])==[4,5]
assert all(x['rank_a']==x['rank_b']==6 and x['rank_ab']==x['rank_ba']==5 for x in witness['locals'])
