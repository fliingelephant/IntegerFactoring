"""F299 bounded exact check of the root-derived P235 equivalence.

20-second alarm, estimated peak below64MiB; integer arithmetic only.
"""
import json
import resource
import signal
import time
from pathlib import Path

signal.alarm(20)
started=time.monotonic()
packet=Path(__file__).parent
abstract=[]
abstract_point_checks=0
for row in json.loads((packet/'global_covariance.json').read_text())['rows'][:3]:
    m=row['m']
    r=row['linearization_r']
    L=row['linearization_L']
    T=m*L
    classes=[]
    for c in row['classes']:
        count=0
        for x in range(L):
            for v in range(m//2):
                t=x+L*v
                old=(c['A']*x+c['E']-L*row['d']*v)%T
                new=(c['A']*t+c['E'])%T
                assert old==new
                abstract_point_checks+=1
                count+=new<T//2
        assert count==c['count']
        classes.append(dict(i0=c['i0'],affine_count=count))
    abstract.append(dict(m=m,u=row['u'],gamma=row['gamma'],D=row['D'],T=T,classes=classes))
faithful=[]
point_checks=0
for N,m in ((147053,8),(147053,16),(8464705853,8),(8464705853,16)):
    k=m.bit_length()-1
    r=1<<(k//2)
    L=m//r
    M=m**3
    S=m*r
    T=m*L
    assert S*T==M and S==1<<((3*k)//2)
    origins=[u0+m*i0 for u0 in range(1,m,2) for i0 in range(r)]
    assert sorted(origins)==list(range(1,S,2))
    for u0 in (1,3):
        v0=N*pow(u0,-1,M)%M
        d=N*pow(u0,-2,m*m)%(m*m)
        beta=N*pow(u0,-3,m)%m
        D=v0//m
        kappa=beta*r%L
        for i0 in sorted({0,1,r-1}):
            f0=m*beta*i0*i0-d*i0+D
            E=f0//r
            A=m*(2*beta*i0+kappa)-d
            U0=u0+m*i0
            V0=v0%m+m*(f0%r)
            base=V0+S*(E%T)
            slope=S*A%M
            assert base==N*pow(U0,-1,M)%M
            assert slope==(N*pow(U0+S,-1,M)-N*pow(U0,-1,M))%M
            points=[]
            for t in sorted({0,1,T//2-1,T//2,T-1}):
                X=U0+S*t
                Y=V0+S*((E+A*t)%T)
                actual=N*pow(X,-1,M)%M
                assert Y==actual and X*Y%M==N%M
                assert (X<M//2)==(t<T//2)
                assert (Y<M//2)==((E+A*t)%T<T//2)
                point_checks+=1
                points.append(dict(t=t,X=X,Y=Y))
            faithful.append(dict(N=N,m=m,M=M,u0=u0,i0=i0,S=S,T=T,U0=U0,V0=V0,
                                 E=E,A=A,p235_base=base,p235_slope=slope,points=points))
out=dict(packet='F299',route='F31',status='exact_finite_affine_cover_equivalence',
         runtime_seconds=time.monotonic()-started,
         max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
         abstract_point_checks=abstract_point_checks,faithful_point_checks=point_checks,
         abstract_controls=abstract,faithful_controls=faithful)
(packet/'affine_equivalence.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
