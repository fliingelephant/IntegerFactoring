"""Exact Sage F292 Gauss/Cauchy reduction and finite-part pilot.

Budget: 30 seconds; estimated Sage peak below256MiB. Complete sums in this
finite verification are directly enumerated; this is not a Hiary implementation.
"""
from sage.all import CyclotomicField, QQ, gcd, inverse_mod
import json
import random
import resource
import signal
import time
from pathlib import Path

signal.alarm(30)
started=time.monotonic()
rng=random.Random(2922611)
cases=[]
gauss_checks=0
removable=[]
inputs=[(8,1,0,4),(8,0,0,1),(8,1,0,0)]
for m in (4,6,8,9,12,15,16,20,24,25,32,36):
    inputs.extend((m,rng.randrange(m),0,rng.randrange(m)) for _ in range(3))
inputs.extend([(8,1,1,3),(12,4,2,2),(16,6,3,4),(15,3,6,2)])
for m,a,c,b in inputs:
    field=CyclotomicField(m)
    zeta=field.gen()
    ell=m//int(gcd(b,m))
    d=int(gcd(a,m))
    q=m//d
    common=int(gcd(d,b))
    h=d//common
    compatible=c%common==0
    n0=0 if h==1 or not compatible else (-c//common*int(inverse_mod(b//common,h)))%h
    aprime=a//d
    values=[]
    for n in range(ell):
        actual=sum(zeta**(a*z*z+(c+b*n)*z) for z in range(m))
        if not compatible or (n-n0)%h:
            reduced=field(0)
        elif q==1:
            reduced=field(m)
        else:
            linear=(c+b*n)//d
            root=zeta**d
            if q%2:
                complete=sum(root**(aprime*z*z) for z in range(q))
                reduced=d*complete*root**(-int(inverse_mod(4*aprime,q))*linear*linear)
            elif q%4==2:
                if linear%2==0:
                    reduced=field(0)
                else:
                    Q=q//2
                    root2=root**2
                    complete=sum(root2**(2*aprime*z*z) for z in range(Q))
                    phase=0 if Q==1 else -int(inverse_mod(8*aprime,Q))*linear*linear
                    reduced=2*d*complete*root2**phase
            elif linear%2:
                reduced=field(0)
            else:
                complete=sum(root**(aprime*z*z) for z in range(q))
                reduced=d*complete*root**(-int(inverse_mod(aprime,q))*(linear//2)**2)
        assert actual==reduced
        gauss_checks+=1
        values.append(actual)
    t=QQ(1)/3
    direct=sum(zeta**(a*z*z+c*z)/(1-t*zeta**(b*z)) for z in range(m))
    numerator=sum(t**n*values[n] for n in range(ell))
    assert direct==numerator/(1-t**ell)
    reciprocal=sum(zeta**(a*z*z-c*z)/(1-zeta**(b*z)/t) for z in range(m))
    assert direct+reciprocal==values[0]
    for s in sorted({0,1%ell,ell//2}):
        t0=zeta**(s*(m//ell))
        P0=sum(t0**n*values[n] for n in range(ell))
        P1=sum(n*t0**n*values[n] for n in range(ell))
        residue=sum(zeta**(a*z*z+c*z) for z in range(m) if t0*zeta**(b*z)==1)
        finite=sum(zeta**(a*z*z+c*z)/(1-t0*zeta**(b*z)) for z in range(m) if t0*zeta**(b*z)!=1)
        assert P0/ell==residue
        assert (QQ(ell-1)/2*P0-P1)/ell==finite
        if t0*t0==1:
            if c==0:
                assert finite==(values[0]-residue)/2
            opposite=sum(zeta**(a*z*z-c*z)/(1-t0*zeta**(b*z)) for z in range(m) if t0*zeta**(b*z)!=1)
            assert finite+opposite==values[0]-residue
        g=m//ell
        z0=0 if ell==1 else (-s*int(inverse_mod(b//g,ell)))%ell
        residue_gauss=zeta**(a*z0*z0+c*z0)*sum((zeta**ell)**(a*ell*j*j+(2*a*z0+c)*j) for j in range(g))
        assert residue==residue_gauss
        case=dict(m=m,a=a,c=c,b=b,ell=ell,root_index=s,residue=str(residue),finite_part=str(finite))
        cases.append(case)
        if residue==0 and finite!=0:
            removable.append(case)
out=dict(packet='F292',route='F31',seed=2922611,
         runtime_seconds=time.monotonic()-started,
         max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
         gauss_reduction_checks=gauss_checks,
         interior_kernel_checks=len(inputs),finite_part_checks=len(cases),
         nonzero_removable_examples=removable,cases=cases)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
