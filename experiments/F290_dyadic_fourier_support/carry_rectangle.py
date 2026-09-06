"""Exact joint-half carry recurrence and histogram-only counterexamples.
Family route:F31; tiny finite certificates, no hidden factors supplied.
"""
import json
from math import isqrt, gcd

checks=0
for k in range(3,10):
    M=1<<k;L=M//2
    for N in range(1,32,2):
        direct=sum(N*pow(u,-1,M)%M<L for u in range(1,L,2))
        signed=0
        for u in range(1,L,2):
            v=N*pow(u,-1,L)%L
            c=((N-u*v)//L)%2
            signed+=1-2*c
            for e in (0,1):
                lifted_v=N*pow(u+e*L,-1,M)%M
                assert lifted_v==v+((e+c)%2)*L
        assert direct==(L//2+signed)//2
        checks+=1

small=[]
for N in (3,11):
    M=16
    points=[(u,N*pow(u,-1,M)%M) for u in range(1,M,2)]
    hist=[sum((u+v)%M==s for u,v in points) for s in range(M)]
    small.append(dict(N=N,M=M,histogram=hist,lower_square=[(u,v) for u,v in points if u<M//2 and v<M//2]))
assert small[0]['histogram']==small[1]['histogram']
assert len(small[0]['lower_square'])==4 and not small[1]['lower_square']

groups={}
cap_witness=None
M=1024
for N in range(12*M+3,13*M,8):
    if gcd(N,200560490130)!=1:continue
    L=isqrt(4*N)
    if L*L<4*N:L+=1
    T=isqrt(40804*N)//100
    cap=[]
    for u in range(1,T,2):
        v=N*pow(u,-1,M)%M
        if v and L<=u+v<=T and u*v>=N:cap.append((u,v))
    row=dict(N=N,M=M,L=L,T=T,cap=cap)
    key=(L,T)
    for previous in groups.get(key,[]):
        if bool(previous['cap'])!=bool(cap):
            cap_witness=[previous,row]
            break
    groups.setdefault(key,[]).append(row)
    if cap_witness:break
assert cap_witness
for row in cap_witness:
    hist=[0]*M
    for u in range(1,M,2):hist[(u+row['N']*pow(u,-1,M))%M]+=1
    assert hist==[4 if s%8==4 else 0 for s in range(M)]
    row['modular_interval_count']=sum(hist[row['L']:row['T']+1])
    assert row['T']**2<4*(row['N']+M)
    assert all(u*v==row['N'] for u,v in row['cap'])
print(json.dumps(dict(scope='Counterexamples only to objective-histogram-only localization, not to algorithms using N and additional joint geometry',carry_checks=checks,small=small,cap_witness=cap_witness),indent=2))
