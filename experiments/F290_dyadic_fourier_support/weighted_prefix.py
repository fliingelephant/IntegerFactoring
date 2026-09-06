"""Exact dyadic Fourier-ray compression and geometry comparison.
Family: route:F31. Pilot <30 seconds,<256 MB. Standard integers only.
No factors are supplied or used in any operation.
"""
import json
import time
from math import isqrt

started=time.monotonic()

def phases(N,a,b,K):
    m=K//2
    roots=[0] if m==0 else [1]
    for j in range(1,m):
        roots=[v for u in roots for v in (u,u+(1<<j)) if (a*v*v-b*N)%(1<<(j+1))==0]
    if m==0:roots=[1]
    elif K%2:roots=[v for u in roots for v in (u,u+(1<<m))]
    mod=1<<K
    return [(a*u+b*N*pow(u,-1,mod))%mod for u in roots]

def progression(L,T,c,mod,weighted):
    first=L+(c-L)%mod
    if first>T:return 0
    n=(T-first)//mod+1
    return n*(T+1-first)-mod*n*(n-1)//2 if weighted else n

def compressed(N,k,a,b,L,T,weighted=False):
    total=(T-L+1)*(T-L+2)//2 if weighted else T-L+1
    phase_count=0
    for K in range(1,k+1):
        cs=phases(N,a,b,K)
        phase_count+=len(cs)
        for c in cs:
            total+=(1<<(K//2))*(progression(L,T,c,1<<K,weighted)-progression(L,T,c+(1<<(K-1)),1<<K,weighted))
    assert total%2==0
    return total//2,phase_count

checks=0
for k in range(2,10):
    M=1<<k
    for N in (1,3,5,7,9,13,12*M+1):
        for a,b in ((1,1),(1,3),(3,5)):
            hist=[0]*M
            for x in range(1,M,2):hist[(a*x+b*N*pow(x,-1,M))%M]+=1
            for L,T in [(0,M-1),(M//3,2*M//3),(3,min(M-1,13))]:
                if L>T:continue
                for weighted in (False,True):
                    exact=sum(hist[s]*(T+1-s if weighted else 1) for s in range(L,T+1))
                    got,_=compressed(N,k,a,b,L,T,weighted)
                    assert got==exact,(k,N,a,b,L,T,weighted,got,exact)
                    checks+=1

rows=[]
for k in (10,12,14,16,18,20):
    M=1<<k
    for delta in (1,3,17):
        N=12*M+delta
        # Public exact floor of 1.01*2sqrt(N).
        T=isqrt(40804*N)//100
        L=isqrt(4*N)
        if L*L<4*N:L+=1
        assert T*T<4*(N+M)
        modular_count,operations=compressed(N,k,1,1,L,T)
        modular_weight,_=compressed(N,k,1,1,L,T,True)
        cap=[]
        for x in range(1,T,2):
            y=N*pow(x,-1,M)%M
            if y>0 and L<=x+y<=T and x*y>=N:cap.append((x,y))
        assert all(x*y==N for x,y in cap)
        rows.append(dict(k=k,M=M,N=N,L=L,T=T,modular_count=modular_count,modular_weight=modular_weight,cap_points=cap,cap_weight=sum(T+1-x-y for x,y in cap),stationary_phase_terms=operations))

# A single transverse shift8 breaks the common stationary-root list.
transverse=[]
for m in range(5,13):
    L=1<<m
    N=12*(1<<(2*m))+1
    ratios={N*r*pow(r+8,-1,L)%L for r in range(1,L,2)}
    roots=[u for u in range(1,L,2) if u*u%L in ratios]
    assert len(ratios)==1<<(m-4)
    assert len(roots)==1<<(m-2)
    transverse.append(dict(m=m,M=1<<(2*m),distinct_ratios=len(ratios),distinct_stationary_roots=len(roots)))
assert time.monotonic()-started<25
print(json.dumps(dict(scope='Exact compressed modular-objective counts; positive cap is independently enumerated only for finite comparison',prefix_checks=checks,geometry=rows,transverse=transverse,elapsed_seconds=time.monotonic()-started),indent=2))
