"""F319 / route:F31: exact fan probabilities and randomized support pilot.

Estimated <=30 s, <=512 MiB. Hull enumeration is ONLY a bounded oracle audit
and simulation accelerator. support.py provides the separate scalable query.
The factors below are offline labels. Proposal routines receive n alone.
"""
from bisect import bisect_left
from fractions import Fraction
from math import isqrt, atan, pi, log, gcd
from pathlib import Path
from random import Random
import json, signal, resource, time
from support import nextpt, seek, support

signal.alarm(30)
started = time.monotonic()
rng = Random(319)


def hull(n):
    points = set()
    for x in range(1,isqrt(n)+2):
        y = (n+x-1)//x
        points.add((x,y))
        points.add((y,x))
    vertices = []
    for p in sorted(points):
        while len(vertices)>=2:
            a,b = vertices[-2:]
            cross = (b[0]-a[0])*(p[1]-b[1])-(b[1]-a[1])*(p[0]-b[0])
            if cross>0:
                break
            vertices.pop()
        vertices.append(p)
    return vertices


def oracle(vertices,a,b):
    lo,hi = 0,len(vertices)-1
    while lo<hi:
        m = (lo+hi)//2
        v,w = vertices[m:m+2]
        change = a*(w[0]-v[0])+b*(w[1]-v[1])
        if change==0:
            return min((m,m+1),key=lambda i:(vertices[i][0]*vertices[i][1],i))
        if change<0:
            lo=m+1
        else:
            hi=m
    return lo


def global_direction(n,rng):
    bits=n.bit_length()
    grid=1<<(4*bits)
    exponent=rng.randrange(-bits,bits)
    a,b=grid+rng.randrange(grid),grid
    if exponent>=0:
        a<<=exponent
    else:
        b<<=-exponent
    return a,b


def cdf(boundary,bits,inclusive):
    grid=1<<(4*bits)
    numerator,denominator=boundary.numerator,boundary.denominator
    total=0
    for exponent in range(-bits,bits):
        a,b=(1<<exponent,1) if exponent>=0 else (1,1<<-exponent)
        num=numerator*b*grid-denominator*a*grid
        den=denominator*a
        count=num//den+1 if inclusive else -((-num)//den)
        total+=max(0,min(grid,count))
    return total


def prime_after(x):
    while any(x%d==0 for d in range(2,isqrt(x)+1)):
        x+=1
    return x


cases=[]
labels=[(83,127),(331,479),(1009,1429),(10007,prime_after(14142)),
        (100003,prime_after(141425)),(101,1000003),(1009,1000003)]
checks=0
for p,q in labels:
    n=p*q
    before=time.monotonic()
    vertices=hull(n)
    bits=n.bit_length()
    total=(2*bits)*(1<<(4*bits))
    edges=[Fraction(v[1]-w[1],w[0]-v[0]) for v,w in zip(vertices,vertices[1:])]
    less=[cdf(edge,bits,False) for edge in edges]
    inclusive=[cdf(edge,bits,True) for edge in edges]
    masses=[]
    for i,v in enumerate(vertices):
        upper=total if i==0 else less[i-1]
        lower=0 if i==len(vertices)-1 else inclusive[i]
        masses.append(upper-lower)
    for i,edge in enumerate(edges):
        chosen=min((i,i+1),key=lambda j:(vertices[j][0]*vertices[j][1],j))
        masses[chosen]+=inclusive[i]-less[i]
    assert sum(masses)==total
    factor_indices=[i for i,(x,y) in enumerate(vertices) if x*y==n and 1<x<n]
    direct=sum(masses[i] for i in factor_indices)/total
    success_indices=[i for i,(x,y) in enumerate(vertices)
                     if 1<gcd(x,n)<n or 1<gcd(y,n)<n]
    gcd_success=sum(masses[i] for i in success_indices)/total
    normalizer=sum(mass/total/(x*y-n+1) for mass,(x,y) in zip(masses,vertices) if 1<x<n)
    cube_low,cube_high=0,1<<((bits+2)//3)
    while cube_low+1<cube_high:
        middle=(cube_low+cube_high)//2
        if middle**3<n:
            cube_low=middle
        else:
            cube_high=middle
    cube=cube_high
    scaled_normalizer=sum(mass/total*min(x,y,cube)/(x*y-n+1)
                          for mass,(x,y) in zip(masses,vertices) if 1<x<n)
    scaled_factor=sum(masses[i]/total*min(*vertices[i],cube) for i in factor_indices)
    factor_fans=[]
    for i in factor_indices:
        x,y=vertices[i]
        low,high=edges[i],edges[i-1]
        factor_fans.append(dict(point=[x,y],left=vertices[i-1],right=vertices[i+1],
                                low=str(low),high=str(high),grid_mass=str(Fraction(masses[i],total)),
                                angle_mass=(atan(float(high))-atan(float(low)))/(pi/2)))
        # Exact floor/ceiling extremal characterization, scanned only in pilot.
        # All right-side hull candidates suffice by convexity.
        lows=[Fraction(y-v[1],v[0]-x) for v in vertices if v[0]>x]
        highs=[Fraction(v[1]-y,x-v[0]) for v in vertices if v[0]<x]
        assert low==max(lows) and high==min(highs)
        assert n*(high-low)**3>=4*low**3
        checks+=3
    # Audit NEXTPT, SEEK, and the nonenumerating SUPPORT against exact hull.
    xs=[v[0] for v in vertices]
    for _ in range(4):
        k=rng.randrange(len(vertices)-1)
        assert nextpt(n,vertices[k])==vertices[k+1]
        start=rng.randrange(1,n+1)
        assert seek(n,start)==vertices[bisect_left(xs,start)]
        a,b=global_direction(n,rng)
        actual=support(n,a,b)
        expected=vertices[oracle(vertices,a,b)]
        assert a*actual[0]+b*actual[1]==a*expected[0]+b*expected[1]
        checks+=3
    trials=24
    cap=3000
    walks={}
    for mode in ('independent','local_residual','multiscale_residual','scaled_local'):
        hits=[]
        censored=0
        for trial in range(trials):
            current=None
            for step in range(1,cap+1):
                if mode=='independent' or current is None or rng.randrange(4)==0:
                    a,b=global_direction(n,rng)
                else:
                    x,y=vertices[current]
                    defect=x*y-n
                    root=isqrt(n*(defect+1))+1
                    grid=1<<(4*bits)
                    displacement=4*root*(2*rng.randrange(grid)-grid)
                    if mode=='multiscale_residual':
                        exponent=rng.randrange(-3,bits//2+1)
                        if exponent>=0:
                            displacement<<=exponent
                        else:
                            displacement//=1<<-exponent
                    a,b=y*x*grid+displacement,x*x*grid
                    if a<=0:
                        a,b=global_direction(n,rng)
                candidate=oracle(vertices,a,b)
                x,y=vertices[candidate]
                if 1<gcd(x,n)<n or 1<gcd(y,n)<n:
                    hits.append(step)
                    break
                if x==1 or x==n:
                    continue
                if current is None or mode=='independent':
                    current=candidate
                else:
                    old=vertices[current][0]*vertices[current][1]-n
                    new=x*y-n
                    if mode=='scaled_local':
                        numerator=min(x,y,cube)*(old+1)
                        denominator=min(*vertices[current],cube)*(new+1)
                        accepted=rng.randrange(denominator)<numerator
                    else:
                        accepted=rng.randrange(new+1)<=old
                    if accepted:
                        current=candidate
            else:
                censored+=1
                hits.append(cap)
        walks[mode]=dict(trials=trials,cap=cap,censored=censored,
                         mean_capped_calls=sum(hits)/trials,steps=hits)
    cases.append(dict(n=n,offline_factors=[p,q],vertices=len(vertices),
                      factor_point_success=direct,direct_success=gcd_success,
                      gcd_success_vertices=len(success_indices),independent_mean_calls=1/gcd_success,
                      residual_weight_normalizer=normalizer,
                      ideal_residual_target_factor_mass=direct/normalizer,
                      ideal_scale_normalized_factor_mass=scaled_factor/scaled_normalizer,
                      factor_fans=factor_fans,walks=walks,seconds=time.monotonic()-before))

large=[]
for n in (10**24+39,10**48+151):
    before=time.monotonic()
    a,b=17,11
    p=support(n,a,b)
    assert p[0]*p[1]>=n
    neighbor=nextpt(n,p)
    previous=nextpt(n,(p[1],p[0]))
    previous=previous[1],previous[0]
    assert a*neighbor[0]+b*neighbor[1]>=a*p[0]+b*p[1]
    assert a*previous[0]+b*previous[1]>=a*p[0]+b*p[1]
    large.append(dict(n=n,a=a,b=b,point=p,defect=p[0]*p[1]-n,
                      left=previous,right=neighbor,
                      seconds=time.monotonic()-before))

result=dict(experiment='F319_random_support_hull',route='route:F31',seed=319,
            checks=checks,cases=cases,large_queries=large,
            seconds=time.monotonic()-started,
            peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_name('pilot.json').write_text(json.dumps(result,indent=2)+'\n')
Path(__file__).with_name('pilot.status.json').write_text(json.dumps(dict(completed=True,timeout_seconds=30))+'\n')
print(json.dumps(result,indent=2))
