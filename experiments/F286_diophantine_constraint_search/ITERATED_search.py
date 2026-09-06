"""F286 exact outward-enclosure pilot for iterated local tangent cuts.

One process, 25 second alarm, estimated <128 MB. Factors label inputs and
audit preservation only. Public decisions use N, box, residue, and menu.
"""
import json
import math
import signal
import time
from fractions import Fraction as F

signal.alarm(25)
started = time.monotonic()
scale = 1 << 32

def prime_after(x):
    while any(x % d == 0 for d in range(2, math.isqrt(x)+1)):
        x += 1
    return x

rows = []
for exponent in (12,16,20):
    B = 1 << exponent
    p = prime_after(5*B//4)
    q = prime_after(math.isqrt(2*p*p))
    N = p*q
    for A in (4,8):
        menu = [(a,b) for a in range(1,A+1) for b in range(1,A+1) if math.gcd(a,b)==1]
        for M in (8,32,128):
            states=[]
            for u in range(1,M,2):
                v=N*pow(u,-1,M)%M
                xl=B+(u-B)%M
                xh=2*B-(2*B-u)%M
                yl=B+(v-B)%M
                yh=2*B-(2*B-v)%M
                l,r=max(F(xl),F(N,yh)),min(F(xh),F(N,yl))
                arcs=[(l,r)] if l<=r else []
                visits=updates=peak=0
                first_factor_sweep=None
                sweeps=[]
                fixed=False
                for sweep in range(1,25):
                    before=arcs
                    for a,b in menu:
                        new=[]
                        for l,r in arcs:
                            visits+=1
                            if a*l*l <= b*N <= a*r*r:
                                minimum=math.isqrt(4*a*b*N)
                                minimum += minimum*minimum < 4*a*b*N
                            else:
                                value=min(a*l+b*N/l,a*r+b*N/r)
                                minimum=-(-value.numerator//value.denominator)
                            t=minimum+((a*u+b*v)-minimum)%M
                            maxvalue=max(a*l+b*N/l,a*r+b*N/r)
                            if t>maxvalue:
                                updates+=1
                                continue
                            D=t*t-4*a*b*N
                            if D<=0:
                                new.append((l,r))
                                continue
                            sd=math.isqrt(D)
                            if sd*sd==D:
                                lo,hi=F(t-sd,2*a),F(t+sd,2*a)
                                if first_factor_sweep is None and any(1<math.gcd(t+sgn*sd,N)<N for sgn in (-1,1)):
                                    first_factor_sweep=sweep
                            else:
                                sd_scaled=math.isqrt(D*scale*scale)
                                lo,hi=F(t*scale-sd_scaled,2*a*scale),F(t*scale+sd_scaled,2*a*scale)
                            pieces=[]
                            if l<=lo:
                                pieces.append((l,min(r,lo)))
                            if hi<=r:
                                pieces.append((max(l,hi),r))
                            if pieces != [(l,r)]:
                                updates+=1
                            new.extend(pieces)
                        merged=[]
                        for l,r in sorted(new):
                            if merged and l<=merged[-1][1]:
                                merged[-1]=(merged[-1][0],max(merged[-1][1],r))
                            else:
                                merged.append((l,r))
                        arcs=merged
                        peak=max(peak,len(arcs))
                        # Labels audit only, after the public update.
                        for actual in (p,q):
                            if actual%M==u:
                                assert any(l<=actual<=r for l,r in arcs),(N,A,M,u,sweep,a,b,actual)
                    sweeps.append(len(arcs))
                    if arcs==before:
                        fixed=True
                        break
                states.append(dict(u=u,sweeps=len(sweeps),arc_counts=sweeps,fixed=fixed,
                    final_arcs=len(arcs),peak_arcs=peak,visits=visits,updates=updates,
                    first_factor_sweep=first_factor_sweep,
                    endpoints=[[[l.numerator,l.denominator],[r.numerator,r.denominator]] for l,r in arcs]))
            rows.append(dict(B=B,N=N,p_label=p,q_label=q,A=A,M=M,states=states,
                survivors=sum(s['final_arcs']>0 for s in states),
                fixed=sum(s['fixed'] for s in states),
                factor_states=sum(s['first_factor_sweep'] is not None for s in states),
                max_sweeps=max(s['sweeps'] for s in states),
                visits=sum(s['visits'] for s in states)))
print(json.dumps(dict(elapsed_seconds=time.monotonic()-started,root_enclosure_scale=scale,
    max_sweeps=24,rows=rows),indent=2))
