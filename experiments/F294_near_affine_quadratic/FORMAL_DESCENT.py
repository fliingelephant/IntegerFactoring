"""F294 exact formal-group and retained-window descent checks.

One process, 20-second alarm, estimated <128 MB. This does not overlap the
independent ROOT_GAUSS_WINDOW files. All validation arithmetic is exact.
"""
import collections
from fractions import Fraction as F
import json
from pathlib import Path
import random
import signal
import time
from evaluator import affine_half

def geom(X,n):
    return (1-X**n)/(1-X) if X!=1 else F(n)

def weighted_floor(n,m,a,b,X,Y,depth=0):
    if not n:
        return F(0),depth
    pref=Y**(b//m)
    X=X*Y**(a//m)
    a%=m
    b%=m
    h=(a*(n-1)+b)//m
    if not h:
        return pref*geom(X,n),depth
    inner,d=weighted_floor(h,a,m,m-b+a-1,Y,X,depth+1)
    return pref*(geom(X,n)+(Y-1)/(1-X)*(inner-X**n*geom(Y,h))),d

def add_root(v,exponent,coefficient=1):
    q=2*len(v)
    z=exponent%q
    v[z%len(v)]+=coefficient if z<len(v) else -coefficient

if __name__=='__main__':
    signal.alarm(20)
    started=time.monotonic()
    rng=random.Random(202609070345)
    log_checks=0
    group_checks=0
    counts=[]
    for r in range(3,9):
        m=1<<r
        q=m*m
        kappa=1+q//2
        points=range(q) if r<=5 else [rng.randrange(q) for _ in range(256)]
        for w in points:
            z=(kappa*w+(m//2)*w*w)%q
            assert (z-(m//2)*z*z)%q==w
            g=-z*pow(1+m*z,-1,q)%q
            assert (g-(m//2)*g*g)%q==(-w)%q
            log_checks+=1
        for _ in range(32):
            x,y=rng.randrange(q),rng.randrange(q)
            z=(x+y+m*x*y)%q
            assert (z-(m//2)*z*z-x+(m//2)*x*x-y+(m//2)*y*y)%q==0
            group_checks+=1
        for _ in range(4):
            u=rng.randrange(q)|1
            gamma=rng.randrange(q)|1
            D=rng.randrange(q)
            direct=0
            for w in range(q):
                positive=(kappa*w+(m//2)*w*w)%q
                negative=(-kappa*w+(m//2)*w*w)%q
                direct+=(u*positive)%q<q//2 and (D+gamma*negative)%q<q//2
            d=gamma*pow(u,-1,q)%q
            beta=gamma*pow(u,-1,m)**2%m
            phases=[(beta*i*i+(D-d*i)//m)%m for i in range(m)]
            contracted=sum(affine_half(m,-d,phase) for phase in phases)
            assert direct==contracted
            hist=collections.Counter(phases)
            counts.append(dict(r=r,u=u,gamma=gamma,D=D,d=d,beta=beta,count=direct,
                affine_terms=m,distinct_phases=len(hist),
                nonzero_half_phase_differences=sum(hist[i]!=hist[i+m//2] for i in range(m//2))))
    old=json.loads(Path(__file__).with_name('output.json').read_text())['chart_checks']
    old_checks=[]
    for chart in old:
        r=chart['r']
        if r<3:
            continue
        m=1<<r
        q=m*m
        u,gamma,D=chart['u0'],chart['gamma'],chart['D']
        d=gamma*pow(u,-1,q)%q
        beta=gamma*pow(u,-1,m)**2%m
        got=sum(affine_half(m,-d,beta*i*i+(D-d*i)//m) for i in range(m))
        assert got==chart['count']
        old_checks.append(dict(N=chart['N'],r=r,u=u,count=got))
    floor_checks=[]
    for _ in range(100):
        n=rng.randrange(33)
        m=rng.randrange(1,33)
        a=rng.randrange(65)
        b=rng.randrange(-64,65)
        X,Y=F(2,3),F(3,5)
        got,depth=weighted_floor(n,m,a,b,X,Y)
        expected=sum((X**i*Y**((a*i+b)//m) for i in range(n)),F(0))
        assert got==expected
        floor_checks.append(dict(n=n,m=m,a=a,b=b,depth=depth))
    moment_checks=[]
    for r in range(3,7):
        m=1<<r
        for _ in range(8):
            a=rng.randrange(m)|1
            b=rng.randrange(m)
            A=rng.randrange(m)|1
            B=rng.randrange(m)
            nu=rng.randrange(m)|1
            h=(a*(m-1)+b)//m
            left=[0]*(m//2)
            right=[0]*(m//2)
            for i in range(m):
                add_root(left,A*i*i+B*i+nu*((a*i+b)//m))
                add_root(right,A*i*i+B*i+nu*h)
            lengths=[]
            for j in range(1,h+1):
                length=-(-(m*j-b)//a)
                lengths.append(length)
                for i in range(length):
                    add_root(right,A*i*i+B*i+nu*j,-1)
                    add_root(right,A*i*i+B*i+nu*(j-1),1)
            assert left==right
            moment_checks.append(dict(r=r,a=a,b=b,A=A,B=B,nu=nu,
                prefix_count=h,prefix_lengths=lengths))
    print(json.dumps(dict(seed=202609070345,elapsed_seconds=time.monotonic()-started,
        logarithm_inverse_checks=log_checks,group_checks=group_checks,
        retained_count_checks=counts,old_chart_checks=old_checks,
        euclidean_generating_function_checks=floor_checks,
        quadratic_boundary_moment_checks=moment_checks),indent=2))
