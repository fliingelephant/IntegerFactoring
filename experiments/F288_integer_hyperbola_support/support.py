"""F288 exact integer-hyperbola hull and public support-normal descent.

One process; 20-second timeout, estimated <64 MB and <5 seconds.
Factors only label constructed inputs. Normals/descent use hull points only.
"""
import json
import math
import signal
import time
from fractions import Fraction as F

signal.alarm(20)
started=time.monotonic()

def prime_after(x):
    while any(x%d==0 for d in range(2,math.isqrt(x)+1)):
        x+=1
    return x

outputs=[]
for exponent in (6,8,10,12,14,16):
    B=1<<exponent
    p=prime_after(5*B//4)
    q=prime_after(math.isqrt(2*p*p))
    N=p*q
    hull=[]
    for x in range(B,2*B+1):
        y=max(B,(N+x-1)//x)
        if y>2*B:
            continue
        if hull and y==hull[-1][1]:
            continue
        while len(hull)>=2:
            l,m=hull[-2],hull[-1]
            cross=(m[0]-l[0])*(y-l[1])-(m[1]-l[1])*(x-l[0])
            if cross>0:
                break
            hull.pop()
        hull.append((x,y))
    records=[]
    next_indices=[]
    for i,(x,y) in enumerate(hull):
        # Exact support for normal (y,x), tie resolved by least product.
        a,b=y,x
        lo,hi=0,len(hull)-1
        while lo<hi:
            mid=(lo+hi)//2
            dx=hull[mid+1][0]-hull[mid][0]
            dy=hull[mid+1][1]-hull[mid][1]
            if a*dx+b*dy<0:
                lo=mid+1
            else:
                hi=mid
        candidates=[lo]
        if lo+1<len(hull) and a*hull[lo][0]+b*hull[lo][1]==a*hull[lo+1][0]+b*hull[lo+1][1]:
            candidates.append(lo+1)
        nxt=min(candidates,key=lambda j:(hull[j][0]*hull[j][1],hull[j][0]))
        assert hull[nxt][0]*hull[nxt][1]<=x*y
        assert nxt==i or hull[nxt][0]*hull[nxt][1]<x*y
        lower=F(y-hull[i+1][1],hull[i+1][0]-x) if i+1<len(hull) else F(0)
        upper=F(hull[i-1][1]-y,x-hull[i-1][0]) if i else None
        low=max(lower,F(1,2))
        high=min(upper,F(2)) if upper is not None else F(2)
        width=max(F(0),high-low)
        records.append(dict(x=x,y=y,defect=x*y-N,
            lower_normal=[lower.numerator,lower.denominator],
            upper_normal=[upper.numerator,upper.denominator] if upper is not None else None,
            clipped_width=[width.numerator,width.denominator],next=nxt,
            strict_fixed=nxt==i and lower<F(y,x) and (upper is None or F(y,x)<upper)))
        next_indices.append(nxt)
    basin={}
    for i,r in enumerate(records):
        j=i
        steps=0
        while next_indices[j]!=j:
            j=next_indices[j]
            steps+=1
            assert steps<=len(records)
        r['trap']=j
        r['steps']=steps
        width=F(*r['clipped_width'])
        basin[j]=basin.get(j,F(0))+width
    factor_mass=sum((width for j,width in basin.items() if records[j]['defect']==0),F(0))/F(3,2)
    direct_factor_mass=sum((F(*r['clipped_width']) for r in records if r['defect']==0),F(0))/F(3,2)
    outputs.append(dict(B=B,N=N,p_label=p,q_label=q,hull_vertices=len(hull),
        strict_nonfactor_traps=sum(r['strict_fixed'] and r['defect']>0 for r in records),
        fixed_points=len(basin),max_steps=max(r['steps'] for r in records),
        direct_factor_mass=[direct_factor_mass.numerator,direct_factor_mass.denominator],
        descent_factor_mass=[factor_mass.numerator,factor_mass.denominator],
        traps=[dict(index=j,basin_mass=[(w/F(3,2)).numerator,(w/F(3,2)).denominator]) for j,w in basin.items()],
        vertices=records))
print(json.dumps(dict(elapsed_seconds=time.monotonic()-started,
    normal_distribution='continuous uniform a/b in [1/2,2], used only for exact fan measure',
    outputs=outputs),indent=2))
