"""F295 full-window auxiliary Gauss and adjacent-ray coordinate checks.

Exact cyclotomic coefficients for m=8,16; symbolic valuation certificates
at larger bit lengths. One process, 30-second alarm, estimated <128 MB.
"""
from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path
import signal
import time

path=Path(__file__).resolve().parents[1]/'F294_near_affine_quadratic'/'RECOMBINATION.py'
spec=importlib.util.spec_from_file_location('exact_field',path)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Field=module.Field

def axis_moment(m,eta,t):
    t%=m
    if eta:
        return F(m,4) if t<m//2 else F(-m,4)
    return F(m//2-1,2)-(t%(m//2))

if __name__=='__main__':
    signal.alarm(30)
    start=time.monotonic()
    cases=[]
    inputs=[(8,1,45,13,(1,5,1,6)),(8,1,45,0,(1,6,1,5)),
        (16,1,109,230,(1,6,1,7)),(16,1,109,0,(1,7,1,6)),
        (8,3,5,7,(1,2,1,3)),(16,3,11,17,(1,5,1,6)),
        (8,1,45,13,(1,1,0,1))]
    for m,u,gamma,D,(P,Q,R,S) in inputs:
        f=Field(m)
        q=m*m
        eps=P*S-Q*R
        assert abs(eps)==1
        eta1,eta2=Q%2,S%2
        d=gamma*pow(u,-1,q)%q
        original=f.zero
        transformed=f.zero
        gauss_checks=0
        coordinate_checks=0
        for b in range(1,m,2):
            denominator=f.mul(f.invone(-d*b),f.invone(-b))
            complete=f.scale(f.gauss(b*gamma),F(2))
            inv=pow(b*gamma,-1,m)
            for z in range(m//2):
                Z=2*z
                auxiliary=f.add(*(f.root(b*gamma*x*x+u*Z*x) for x in range(m)))
                assert auxiliary==f.mul(complete,f.root(-u*u*z*z*inv))
                gauss_checks+=1
                window=f.add(*(f.root(-Z*i-b*((d*i+m-1-D)//m)) for i in range(m)))
                original=f.add(original,f.mul(auxiliary,f.mul(window,denominator)))
        for U in range(eta1,m,2):
            for V in range(eta2,m,2):
                Z=eps*(S*U-Q*V)%m
                b=eps*(-R*U+P*V)%m
                assert Z%2==0 and b%2==1
                auxiliary=f.add(*(f.root(eps*(U*(-gamma*R*x*x+u*S*x)
                    +V*(gamma*P*x*x-u*Q*x))) for x in range(m)))
                window=f.add(*(f.root(-Z*i-b*((d*i+m-1-D)//m)) for i in range(m)))
                denominator=f.mul(f.invone(-d*b),f.invone(-b))
                transformed=f.add(transformed,f.mul(auxiliary,f.mul(window,denominator)))
                coordinate_checks+=1
        assert transformed==original
        answer=f.add(f.scale(f.one,F(q,4)),f.scale(transformed,F(4,m*m)))
        kappa=1+q//2
        direct=sum((u*(kappa*w+(m//2)*w*w))%q<q//2 and
            (D+gamma*(-kappa*w+(m//2)*w*w))%q<q//2 for w in range(q))
        assert answer==f.scale(f.one,F(direct))
        # A pole-excluded three-denominator cone, including arbitrary retained
        # linear numerator phases. The full-window check above uses the full
        # finite polynomial, so no pole convention enters that equality.
        c1,c2=1,D%m
        axis_direct=f.zero
        for U in range(eta1,m,2):
            for V in range(eta2,m,2):
                if U==0 or V==0:continue
                b=eps*(-R*U+P*V)%m
                den=f.mul(f.mul(f.invone(-U),f.invone(-V)),f.invone(-d*b))
                val=f.add(*(f.root(U*(eps*(-gamma*R*x*x+u*S*x)+c1)
                     +V*(eps*(gamma*P*x*x-u*Q*x)+c2)) for x in range(m)))
                axis_direct=f.add(axis_direct,f.mul(val,den))
        moments=F(0)
        for x in range(m):
            for t in range(m//2):
                L1=eps*(-gamma*R*x*x+u*S*x+d*R*t)+c1
                L2=eps*(gamma*P*x*x-u*Q*x-d*P*t)+c2
                moments+=axis_moment(m,eta1,L1)*axis_moment(m,eta2,L2)/2
                assert (P*L1+R*L2-u*x-P*c1-R*c2)%m==0
                assert (Q*L1+S*L2-gamma*x*x+d*t-Q*c1-S*c2)%m==0
        assert axis_direct==f.scale(f.one,moments)
        unrestricted=F(0)
        for x in range(m):
            for t in range(m):
                L1=eps*(-gamma*R*x*x+u*S*x+d*R*t)+c1
                L2=eps*(gamma*P*x*x-u*Q*x-d*P*t)+c2
                unrestricted+=axis_moment(m,eta1,L1)*axis_moment(m,eta2,L2)/2
        assert unrestricted==0
        axis=0 if R%2 else 1
        def phase(t,x):
            U=eta1+2*t if axis==0 else eta1
            V=eta2 if axis==0 else eta2+2*t
            return eps*(U*(-gamma*R*x*x+u*S*x)+V*(gamma*P*x*x-u*Q*x))
        third=(phase(1,2)-2*phase(1,1)+phase(1,0)-phase(0,2)+2*phase(0,1)-phase(0,0))%m
        assert third==4*eps*gamma*(-R if axis==0 else P)%m and third!=0
        rb=m.bit_length()-1
        aa=(rb-1)//2
        split=1<<aa
        replacements=0
        for U in range(eta1,m,2):
            for V in range(eta2,m,2):
                blin=eps*(-R*((U-eta1)//2)+P*((V-eta2)//2))
                for x0 in range(split):
                    for y in range(m//split):
                        x=x0+split*y
                        exact=eps*(U*(-gamma*R*x*x+u*S*x)+V*(gamma*P*x*x-u*Q*x))
                        cubic=(1<<(2*aa+1))*gamma*blin*y*y
                        replacement=(1<<(2*aa+1))*gamma*blin*y if 2*aa+1==rb-1 else 0
                        assert (exact-(exact-cubic+replacement))%m==0
                        replacements+=1
        cases.append(dict(m=m,q=q,u=u,gamma=gamma,D=D,matrix=[P,Q,R,S],
            parity=[eta1,eta2],count=direct,gauss_checks=gauss_checks,
            coordinate_points=coordinate_checks,axis_linear_shifts=[c1,c2],axis_moment_value=str(moments),
            dropped_half_window_value=str(unrestricted),
            third_difference=third,auxiliary_residue_bits=aa,
            auxiliary_classes=split,quadratic_replacement_checks=replacements))
    growth=[]
    for r in (3,4,5,6,8,12,16,24,32):
        a=(r-1)//2
        assert 2*a+2>=r
        if a:assert 2*(a-1)+2<r
        growth.append(dict(modulus_bits=r,min_auxiliary_residue_bits=a,
            classes=1<<a,previous_third_difference=(1<<(2*a))%(1<<r)))
    print(json.dumps(dict(elapsed_seconds=time.monotonic()-start,cases=cases,
        literal_gaussianization_growth=growth),indent=2))
