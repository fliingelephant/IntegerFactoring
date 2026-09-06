"""F298 closed parity recurrence and signed-state growth.

One process, 50-second alarm, estimated <256 MB. All finite verification
uses exact rational arithmetic. No factors guide state selection.
"""
import collections
from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path
import random
import signal
import time

path=Path(__file__).resolve().parents[1]/'F294_near_affine_quadratic'/'evaluator.py'
spec=importlib.util.spec_from_file_location('affine',path)
affine=importlib.util.module_from_spec(spec)
spec.loader.exec_module(affine)

def J(m,eta,z):
    z%=m
    return (F(m,4) if z<m//2 else F(-m,4)) if eta else F(m//2-1,2)-z%(m//2)

def value(m,g,v,c1,c2,u,d,matrix):
    P,Q,R,S=matrix
    eps=P*S-Q*R
    return sum((J(m,Q%2,eps*(-R*g*x*x+(u*S-R*v)*x+d*R*t)+c1)
               *J(m,S%2,eps*(P*g*x*x+(P*v-u*Q)*x-d*P*t)+c2)
                for x in range(m//2) for t in range(m//2)),F(0))

def single(m,A,B,C,D):
    r=m.bit_length()-1
    va=(A&-A).bit_length()-1 if A else r
    vb=(B&-B).bit_length()-1 if B else r
    exponent=min(va,vb,r)
    g=1<<exponent
    atoms=[]
    if g==m:
        atoms=[(0,m)]
    else:
        n=m//g
        a,b=A//g,B//g
        if a%2==0:
            return F(0)
        if b%2:
            if n==2:atoms=[(0,m)]
            else:return F(0)
        else:
            rr=n.bit_length()-1
            if rr==1:return F(0)
            shift=(b//2)*pow(a,-1,n)%n
            c=-g*a*shift*shift%m
            if rr%2==0:
                multiplicity=g*(1<<(rr//2))
                atoms=[(c,multiplicity),((c+a*(m//4))%m,multiplicity)]
            else:
                atoms=[((c+a*(m//8))%m,g*(1<<((rr+1)//2)))]
    return F(m,8)*sum(mult*(2*affine.affine_half(m,C,z+D)-m//2) for z,mult in atoms)

def children(m,state,u,d,matrix):
    g,v,c1,c2=state
    P,Q,R,S=matrix
    eps=P*S-Q*R
    n=m//2
    out=[]
    correction=F(0)
    for e in (0,1):
        for f in (0,1):
            C1=eps*(-R*g*e*e+(u*S-R*v)*e+d*R*f)+c1
            C2=eps*(P*g*e*e+(P*v-u*Q)*e-d*P*f)+c2
            child=(2*g%n,(v+2*g*e)%n,(C1//2)%n,(C2//2)%n)
            out.append(child)
            gg,vv,cc1,cc2=child
            if Q%2==0:
                A=eps*P*gg%n
                B=eps*(P*vv-u*Q)%n
                C=-eps*d*P%n
                assert A%2==B%2==0 and C%2==1
                correction+=(1-2*(C1%2))*single(n,A,B,C,cc2)
            if S%2==0:
                A=-eps*R*gg%n
                B=eps*(u*S-R*vv)%n
                C=eps*d*R%n
                assert A%2==B%2==0 and C%2==1
                correction+=(1-2*(C2%2))*single(n,A,B,C,cc1)
    return out,correction

def canonical(m,state,matrix):
    g,v,c1,c2=state
    c1%=m
    c2%=m
    H=m//2
    sign=-1 if ((matrix[1]%2)*(c1//H)+(matrix[3]%2)*(c2//H))%2 else 1
    return (g%m,v%m,c1%H,c2%H),sign

if __name__=='__main__':
    signal.alarm(50)
    started=time.monotonic()
    rng=random.Random(202609070535)
    checks=[]
    invariance_checks=0
    matrices=[(1,5,1,6),(1,6,1,7),(1,1,0,1),(1,6,1,5)]
    single_checks=0
    for r in (3,4,5):
        m=1<<r
        for _ in range(8):
            matrix=rng.choice(matrices)
            u,d=rng.randrange(m)|1,rng.randrange(m)|1
            state=(rng.randrange(m),2*rng.randrange(m//2),rng.randrange(m),rng.randrange(m))
            P,Q,R,S=matrix
            eps=P*S-Q*R
            g,v,c1,c2=state
            def integrand(x,t):
                return J(m,Q%2,eps*(-R*g*x*x+(u*S-R*v)*x+d*R*t)+c1)*J(m,S%2,eps*(P*g*x*x+(P*v-u*Q)*x-d*P*t)+c2)
            for _ in range(8):
                x,t=rng.randrange(m),rng.randrange(m)
                original=integrand(x,t)
                assert integrand(x+m//2,t)==original
                assert integrand(x,t+m//2)==-original
                invariance_checks+=1
            exact=value(m,*state,u,d,matrix)
            branch,correction=children(m,state,u,d,matrix)
            got=4*sum((value(m//2,*z,u,d,matrix) for z in branch),F(0))+correction
            assert exact==got,(r,matrix,state,exact,got)
            key,sign=canonical(m,state,matrix)
            assert exact==sign*value(m,*key,u,d,matrix)
            checks.append(dict(r=r,matrix=matrix,u=u,d=d,state=state,value=str(exact),
                child_values=[str(value(m//2,*z,u,d,matrix)) for z in branch],correction=str(correction)))
            for _ in range(4):
                A=2*rng.randrange(m//2)
                B=2*rng.randrange(m//2)
                C=rng.randrange(m)|1
                D=rng.randrange(m)
                brute=sum((J(m,1,A*x*x+B*x+C*t+D) for x in range(m//2) for t in range(m//2)),F(0))
                assert single(m,A,B,C,D)==brute
                single_checks+=1
    growth=[]
    for r in (6,8,10,12,14,16):
        m=1<<r
        for family in ('random','fixed_control'):
            matrix=(1,5,1,6)
            if family=='random':
                u,d=rng.randrange(m)|1,rng.randrange(m)|1
                state=(rng.randrange(m)|1,0,rng.randrange(m),rng.randrange(m))
            else:
                u,d=1,45%m
                state=(45%m,0,1,13%m)
            initial_state=state
            key,sign=canonical(m,state,matrix)
            bank={key:sign}
            levels=[]
            n=m
            accumulated=F(0)
            while n>=4 and any(state[0] for state in bank):
                new=collections.defaultdict(int)
                generated=0
                for state,weight in bank.items():
                    branch,corr=children(n,state,u,d,matrix)
                    accumulated+=weight*corr
                    for child in branch:
                        key,sign=canonical(n//2,child,matrix)
                        new[key]+=4*weight*sign
                        generated+=1
                vanished=sum(v==0 for v in new.values())
                bank={k:v for k,v in new.items() if v}
                n//=2
                levels.append(dict(modulus=n,generated=generated,distinct_before_cancellation=len(new),
                    vanished=vanished,live=len(bank),weight_bits=max((abs(w).bit_length() for w in bank.values()),default=0)))
            exact=recursed=None
            if r<=8:
                exact=value(m,*initial_state,u,d,matrix)
                recursed=accumulated+sum((weight*value(n,*state,u,d,matrix) for state,weight in bank.items()),F(0))
                assert exact==recursed
            growth.append(dict(r=r,family=family,u=u,d=d,initial=initial_state,
                levels=levels,linear_states=len(bank),accumulated_correction=str(accumulated),
                direct_value=None if exact is None else str(exact),
                recursive_value=None if recursed is None else str(recursed)))
    print(json.dumps(dict(seed=202609070535,elapsed_seconds=time.monotonic()-started,
        invariance_checks=invariance_checks,recurrence_checks=checks,single_window_checks=single_checks,state_growth=growth),indent=2))
