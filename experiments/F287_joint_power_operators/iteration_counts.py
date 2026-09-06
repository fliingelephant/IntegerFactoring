"""Exact bounded rational-iteration experiment.
30 seconds /128 MB budget; poles stop each local path permanently.
Factors label offline fields only. Public operations use N,t,h,j.
"""
import json
import time
from math import gcd

started=time.monotonic()
pairs=[(11,17),(43,47),(101,149),(193,257),(383,643),(613,887),(887,1259),(1259,1783),(1783,2521),(4001,6007)]
records=[]
for p,q in pairs:
    assert all(n%d for n in (p,q) for d in range(2,int(n**.5)+1))
    for ell,r in [(p,q),(q,p)]:
        for h in (2,3):
            jmax=ell.bit_length()
            roots_a=[[] for _ in range(jmax)]
            roots_b=[[] for _ in range(jmax)]
            pole_x=[[] for _ in range(jmax)]
            pole_y=[[] for _ in range(jmax)]
            alive_a=[0]*jmax
            alive_b=[0]*jmax
            eligible=[]
            for t in range(2,ell):
                x=pow(t,r,ell)
                if x==t:continue
                eligible.append(t)
                y=t
                for j in range(jmax):
                    if x is not None:
                        d=(h*x-1)%ell
                        if not d:
                            pole_x[j].append(t)
                            x=None
                        else:x=x*(h-x)*pow(d,-1,ell)%ell
                    if y is not None:
                        d=(h*y-1)%ell
                        if not d:
                            pole_y[j].append(t)
                            y=None
                        else:y=y*(h-y)*pow(d,-1,ell)%ell
                    if x is not None:
                        alive_a[j]+=1
                        if x==t:roots_a[j].append(t)
                    if x is not None and y is not None:
                        alive_b[j]+=1
                        if x==y:roots_b[j].append(t)
            assert time.monotonic()-started<25
            disc=pow((-3)%ell,(ell-1)//2,ell)
            torus=ell-(1 if disc==1 else -1)
            two=1
            while torus%(two*2)==0:two*=2
            records.append(dict(p=p,q=q,field=ell,other=r,h=h,eligible=len(eligible),shared_gcd=gcd(p-1,q-1),torus_order=torus,torus_two_part=two,stages=[dict(j=j+1,A_count=len(roots_a[j]),B_count=len(roots_b[j]),A_roots=roots_a[j],B_roots=roots_b[j],first_pole_x=pole_x[j],first_pole_y=pole_y[j],alive_A=alive_a[j],alive_B=alive_b[j]) for j in range(jmax)]))
print(json.dumps(dict(scope='Exact finite local counts, restricted to t!=0,1 and t^N!=t locally; no success theorem',records=records,elapsed_seconds=time.monotonic()-started),indent=2))
