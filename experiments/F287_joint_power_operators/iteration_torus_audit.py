"""Exact quadratic-algebra audit of h2 collision and first-pole claims.
No factor-dependent operations are proposed for the public algorithm.
"""
import json
from pathlib import Path

records=json.loads(Path(__file__).with_name('iteration_counts.json').read_text())['records']
checks=0
for rec in records:
    if rec['h']!=2:continue
    ell,r=rec['field'],rec['other']
    def mul(x,y):
        a,b=x;c,d=y
        return ((a*c-b*d)%ell,(a*d+b*c+b*d)%ell)
    def inv(x):
        a,b=x
        n=pow((a*a+a*b+b*b)%ell,-1,ell)
        return ((a+b)*n%ell,-b*n%ell)
    def M(x):
        return mul((x,-1),inv((x-1,1)))
    stages=rec['stages']
    rootsets=[set(s['B_roots']) for s in stages]
    poles=[set(s['first_pole_x']) for s in stages]
    for t in range(2,ell):
        x=pow(t,r,ell)
        if x==t:continue
        if (x*x-x+1)%ell==0 or (t*t-t+1)%ell==0:
            assert all(t not in s for s in rootsets)
            continue
        mx,my=M(x),M(t)
        ratio=mul(mx,inv(my))
        xp,yp,cp=mx,my,ratio
        deadx=deady=False
        for j,s in enumerate(stages):
            xp=mul(xp,xp);yp=mul(yp,yp);cp=mul(cp,cp)
            newpole=not deadx and xp==(1,0)
            assert (t in poles[j])==newpole
            deadx=deadx or xp==(1,0)
            deady=deady or yp==(1,0)
            assert (t in rootsets[j])==(not deadx and not deady and cp==(1,0))
            checks+=1
print(json.dumps(dict(status='all exact quadratic-algebra checks passed',stage_checks=checks),indent=2))
