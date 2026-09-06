"""F292 exact inverse reciprocity with half-square/cap boundary terms.

30-second / 64-MiB pilot. Public seeded inputs; no factor-dependent queries.
"""
import json
import math
import random
import signal
import time
from pathlib import Path

signal.alarm(30)
started=time.monotonic()
rng=random.Random(2922610)
root=Path(__file__).parent
half_cases=[]
point_checks=0
cochrane_checks=0
for k in range(4,13):
    M=1<<k
    inputs=range(1,M,2) if k<=6 else sorted({1,3,5,M-1,*[rng.randrange(1,M,2) for _ in range(20)]})
    for r in inputs:
        direct=0
        upper=0
        for u in range(1,M//2,2):
            v=r*pow(u,-1,M)%M
            w=r*pow(M,-1,u)%u
            reflected=(r-M*w)//u+(M if w else 0)
            assert reflected==v
            point_checks+=1
            direct+=v<M//2
            upper+=2*w>u
        divisors=sum(1+(d*d!=r) for d in range(1,math.isqrt(r)+1) if r%d==0)
        correction=divisors
        if r>M//2:
            s=r-M//2
            shifted=sum(1+(d*d!=s) for d in range(1,math.isqrt(s)+1) if s%d==0)
            correction-=shifted+1
        assert direct==upper+correction
        if k<=9:
            numerator=[]
            for q in (M,M//2):
                numerator.append(sum((2*u-q)*(2*(r*pow(u,-1,q)%q)-q)
                                     for u in range(1,q,2)))
            assert 4*(numerator[0]-2*numerator[1])==(4*direct-M//2)*M*M
            cochrane_checks+=1
        half_cases.append(dict(k=k,M=M,r=r,half_square_count=direct,
                               reciprocal_upper_count=upper,boundary=correction,
                               smaller_modulus_calls=M//4))
cap_cases=[]
for case in json.loads((root/'conductor_descent.json').read_text())['cases']:
    N,M,a,b,T=(case[z] for z in ('N','M','a','b','T'))
    r,Q=N%M,N//M
    disc=T*T-4*a*b*N
    lo=max(1,(T-math.isqrt(disc))//(2*a)-1)
    hi=(T+math.isqrt(disc))//(2*a)
    found=[]
    calls=0
    for x in range(lo|1,hi+1,2):
        calls+=1
        w=r*pow(M,-1,x)%x
        y=(r-M*w)//x+(M if w else 0)
        level=0 if w==0 else x-w
        assert x*y==r+M*level
        if x*y>=N and a*x+b*y<=T:
            assert level==Q
            found.append([x,y])
    assert len(found)==case['exact_count']
    cap_cases.append(dict(N=N,M=M,r=r,Q=Q,a=a,b=b,T=T,
                          smaller_modulus_calls=calls,largest_modulus=hi,
                          exact_count=len(found),points=found))
retained=[]
for line in Path('experiments/F293_carry_convolution/reciprocal_trace.jsonl').read_text().splitlines():
    row=json.loads(line)
    if row.get('status')=='complete' and row['k']<=12:
        match=next(c for c in half_cases if c['k']==row['k'] and c['r']==row['N'])
        assert match['half_square_count']==row['half_square_count']
        retained.append([row['k'],row['N']])
out=dict(packet='F292',route='F31',seed=2922610,
         runtime_seconds=time.monotonic()-started,
         pointwise_reciprocity_checks=point_checks,
         cochrane_difference_checks=cochrane_checks,
         retained_F293_cross_checks=retained,half_cases=half_cases,cap_cases=cap_cases)
root.joinpath('reciprocal_boundaries.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
