"""Full signed-window recombination and reciprocal boundary pairing.

Exact Q(zeta_m) coefficient arithmetic for m=8,16. One process, hard20s,
estimated <128 MB. Pole values come from the full finite polynomial.
"""
from fractions import Fraction as F
import json
import math
import signal
import time

class Field:
    def __init__(self,m):
        self.m=m
        self.h=m//2
        self.zero=(F(0),)*self.h
        self.one=self.root(0)
        self.inverses={}
    def root(self,e):
        e%=self.m
        v=[F(0)]*self.h
        v[e%self.h]=F(1 if e<self.h else -1)
        return tuple(v)
    def add(self,*vectors):
        return tuple(sum(x,F(0)) for x in zip(*vectors)) if vectors else self.zero
    def scale(self,v,c):
        return tuple(c*x for x in v)
    def mul(self,v,w):
        out=[F(0)]*self.h
        for i,x in enumerate(v):
            if not x:continue
            for j,y in enumerate(w):
                if y:out[(i+j)%self.h]+=(1 if i+j<self.h else -1)*x*y
        return tuple(out)
    def invone(self,e):
        e%=self.m
        if e==0:return None
        if e not in self.inverses:
            ell=self.m//math.gcd(e,self.m)
            self.inverses[e]=self.add(*(self.scale(self.root(e*j),F(-j,ell)) for j in range(1,ell)))
        return self.inverses[e]
    def gauss(self,A,c=0):
        return self.add(*(self.root(A*z*z+c*z) for z in range(self.h)))
    def cauchy(self,A,c,e):
        out=self.zero
        pole=self.zero
        for z in range(self.h):
            phase=self.root(A*z*z+c*z)
            inverse=self.invone(e-2*z)
            if inverse is None:pole=self.add(pole,phase)
            else:out=self.add(out,self.mul(phase,inverse))
        return out,pole

def serialize(v):
    return [str(x) for x in v]

if __name__=='__main__':
    signal.alarm(20)
    start=time.monotonic()
    cases=[]
    for m,u,gamma,D in ((8,1,45,13),(8,1,45,0),(16,1,109,230),
                         (16,1,109,0),(8,3,5,7),(16,3,11,17)):
        q=m*m
        field=Field(m)
        d=gamma*pow(u,-1,q)%q
        quotient,a=divmod(d,m)
        bq,b=divmod(m-1-D,m)
        H=(a*(m-1)+b)//m
        child_exponents=[(m*i+m-b+a-1)//a for i in range(H)]
        total=field.zero
        gauss_total=field.zero
        residual_total=field.zero
        pole_total=field.zero
        records=[]
        for bf in range(1,m,2):
            A=-u*u*pow(bf*gamma,-1,m)%m
            e=(-bf*quotient)%m
            h=(-e)%field.h
            K={c:field.zero for c in range(0,m,2)}
            for i,p in enumerate(child_exponents):
                c=(-2*p)%m
                K[c]=field.add(K[c],field.root(-bf*(i+quotient*p)))
            V=field.add(*(field.root(-e-bf*j) for j in range(H)))
            cinv=(-2)%m
            shiftphase=field.root(A*h*h+cinv*h)
            shifted=(cinv+2*A*h)%m
            K[shifted]=field.add(K[shifted],field.mul(V,shiftphase))
            common=field.scale(field.mul(field.root(-bf*bq),field.invone(-bf*d)),F(-1))
            fullgauss=field.scale(field.gauss(bf*gamma),F(2))
            weight=field.mul(fullgauss,common)
            off=field.zero
            paired=field.zero
            residual=field.zero
            seen=set()
            unmatched=[]
            for c in range(0,m,2):
                Fc,Pc=field.cauchy(A,c,e)
                off=field.add(off,field.mul(K[c],Fc))
                if c in seen:continue
                partner=(-c+2*A*h)%m
                seen.update((c,partner))
                R=field.root(A*h*h-c*h)
                Fp,_=field.cauchy(A,partner,e)
                Gminus=field.add(field.gauss(A,c),field.scale(Pc,F(-1)))
                assert field.add(Fc,field.mul(R,Fp))==Gminus
                if partner==c:
                    if R==field.one:
                        paired=field.add(paired,field.scale(field.mul(K[c],Gminus),F(1,2)))
                    else:
                        assert R==field.scale(field.one,F(-1)) and Gminus==field.zero
                        residual=field.add(residual,field.mul(K[c],Fc))
                        if K[c]!=field.zero:unmatched.append(dict(c=c,partner=c,coefficient=serialize(K[c])))
                else:
                    paired=field.add(paired,field.mul(K[c],Gminus))
                    delta=field.add(K[partner],field.scale(field.mul(K[c],R),F(-1)))
                    residual=field.add(residual,field.mul(delta,Fp))
                    if delta!=field.zero:unmatched.append(dict(c=c,partner=partner,coefficient=serialize(delta)))
            assert off==field.add(paired,residual)
            pole_full=field.zero
            pole_z=[]
            # Recombine the full polynomial at a pole; never reduce a
            # deformation-dependent monomial before taking its finite part.
            den=field.mul(field.invone(-bf*d),field.invone(-bf))
            direct_frame=field.zero
            for z in range(field.h):
                polynomial=field.add(*(field.root(-2*z*i-bf*((d*i+m-1-D)//m)) for i in range(m)))
                value=field.mul(field.root(A*z*z),field.mul(polynomial,den))
                direct_frame=field.add(direct_frame,value)
                if (e-2*z)%m==0:
                    pole_z.append(z)
                    pole_full=field.add(pole_full,value)
            assert field.add(field.mul(common,off),pole_full)==direct_frame
            total=field.add(total,field.mul(fullgauss,direct_frame))
            gauss_total=field.add(gauss_total,field.mul(weight,paired))
            residual_total=field.add(residual_total,field.mul(weight,residual))
            pole_total=field.add(pole_total,field.mul(fullgauss,pole_full))
            records.append(dict(b0=bf,quadratic=A,t_exponent=e,shift=h,pole_z=pole_z,
                coefficients={str(c):serialize(v) for c,v in K.items() if v!=field.zero},
                unmatched_orbits=unmatched))
        assert total==field.add(gauss_total,residual_total,pole_total)
        answer=field.add(field.scale(field.one,F(q,4)),field.scale(total,F(4,m*m)))
        kappa=1+q//2
        brute=sum((u*(kappa*w+(m//2)*w*w))%q<q//2 and
                  (D+gamma*(-kappa*w+(m//2)*w*w))%q<q//2 for w in range(q))
        assert answer==field.scale(field.one,F(brute))
        cases.append(dict(q=q,m=m,u=u,gamma=gamma,D=D,d=d,count=brute,
            child_exponents=child_exponents,gauss_correction=serialize(field.scale(gauss_total,F(4,m*m))),
            residual_correction=serialize(field.scale(residual_total,F(4,m*m))),
            pole_correction=serialize(field.scale(pole_total,F(4,m*m))),frames=records))
    print(json.dumps(dict(elapsed_seconds=time.monotonic()-start,cases=cases),indent=2))
