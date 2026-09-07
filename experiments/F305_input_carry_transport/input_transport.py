"""F305/F31 exact input transport and nonenumerative floor marginals.

Initial pilot: 30 seconds, estimated peak below256MiB. Fast marginals use
degree-bounded Euclidean floor moments; inverse graphs appear only in small
independent verification loops.
"""
from fractions import Fraction
from functools import lru_cache
import json
import math
import random
import resource
import signal
import time
from pathlib import Path

signal.alarm(30)
started=time.monotonic()
rng=random.Random(3052608)

def marginal_bank(M,N,d,limit=None,modulus=None):
    if limit is None:
        limit=M
    if modulus is None:
        modulus=2*M
    bits=modulus.bit_length()-1
    top=(bits-1)//2
    degree=top+2
    polynomials=[[Fraction(0),Fraction(1)]]
    for p in range(1,degree+1):
        row=[Fraction(0)]*(p+2)
        row[p+1]=Fraction(1)
        for h in range(p):
            for j,c in enumerate(polynomials[h]):
                row[j]-=math.comb(p+1,h)*c
        polynomials.append([c/(p+1) for c in row])
    largest=0
    @lru_cache(None)
    def F(p,q,n,m,a,b):
        nonlocal largest
        if n==0:
            return 0
        if q==0:
            value=sum(c*n**j for j,c in enumerate(polynomials[p]))
        else:
            A,a0=divmod(a,m)
            B,b0=divmod(b,m)
            if A or B:
                value=0
                for h in range(q+1):
                    for j in range(q-h+1):
                        c=math.comb(q,h)*math.comb(q-h,j)*A**j*B**(q-h-j)
                        if c:
                            value+=c*F(p+j,h,n,m,a0,b0)
            elif a==0:
                value=0
            else:
                H=(a*(n-1)+b)//m
                value=F(p,0,n,m,a,b)*H**q
                for j in range(q):
                    for s,c in enumerate(polynomials[p]):
                        if c:
                            value-=math.comb(q,j)*c*F(j,s,H,a,m,m-b+a-1)
        value=Fraction(value)
        assert value.denominator==1
        answer=value.numerator
        largest=max(largest,abs(answer).bit_length())
        return answer
    bank={}
    for inv_degree in (0,1,2):
        for power in (0,1,2):
            result=0
            for residue in (1,3):
                for h in range(top+1):
                    c=(1 if h==0 else 0) if inv_degree==0 else (-1)**h*math.comb(inv_degree+h-1,h)*pow(4,h,modulus)*pow(residue,-inv_degree-h,modulus)
                    if c:
                        length=max(0,(limit-1-residue)//4+1)
                        result+=c*F(h,power,length,M,4*N,residue*N-d)
            bank[(inv_degree,power)]=result%modulus
    return bank,dict(states=F.cache_info().currsize,degree=degree,largest_integer_bits=largest)

cases=[]
point_checks=0
shifted_checks=0
reflections=[]
for k in range(3,10):
    M=1<<k
    units=list(range(1,M,2))
    base={w:(pow(w,-1,M),(w*pow(w,-1,M)-1)//M) for w in units}
    base_Q=sum(q for u,q in base.values())
    prefix={c:marginal_bank(M,0,0,limit=c,modulus=M)[0][(1,0)] for c in (0,2,M//2+1)}
    for N in sorted({1,3,M-1,rng.randrange(1,M,2)}):
        for d in (0,M//3):
            bank,stats=marginal_bank(M,N,d)
            f={w:(N*w-d)//M for w in units}
            for inv_degree in (0,1,2):
                for power in (0,1,2):
                    direct=sum(pow(w,-inv_degree,2*M)*f[w]**power for w in units)%(2*M)
                    assert bank[(inv_degree,power)]==direct
            for c in (0,2,M//2+1):
                A=Q=T=Jtarget=Q2target=Qtarget=0
                for w,(u,q1) in base.items():
                    alpha=int(u<c)
                    x=u+M*alpha
                    v=N*w%M
                    y=v+M*int(v<d)
                    qc=(x*w-1)//M
                    q=(x*y-N)//M
                    assert q==N*qc-x*f[w]
                    assert (x*qc-u*q1)%M==alpha
                    point_checks+=1
                    A+=qc*qc
                    Q+=qc
                    T+=x*qc*f[w]
                    Jtarget+=q*(q-1)//2
                    Q2target+=q*q
                    Qtarget+=q
                assert Q%M==(base_Q+prefix[c])%M
                assert Qtarget%M==(N*(base_Q+prefix[c])-bank[(1,1)])%M
                bracket=(N*N*A-N*Q+bank[(2,2)]+bank[(1,1)])%(2*M)
                assert bracket%2==0
                predicted=(bracket//2+(M//2-N)*T)%M
                assert predicted==Jtarget%M
                base_binomial=(A-Q)//2
                marginal=(bank[(2,2)]+bank[(1,1)])%(2*M)
                assert marginal%2==0
                assert predicted==(N*N*base_binomial+N*(N-1)//2*Q+marginal//2+(M//2-N)*T)%M
                if c==0 and d==0:
                    E_base=(Q*Q-A)//2
                    E_target=(Qtarget*Qtarget-Q2target)//2
                    correction=(Qtarget*Qtarget-N*N*Q*Q-bank[(2,2)])%(2*M)
                    assert correction%2==0
                    assert E_target%M==(N*N*E_base+N*T+correction//2)%M
                shifted_checks+=1
                cases.append(dict(M=M,N=N,c=c,d=d,binomial_sum_mod_M=predicted,
                                  shifted_Q2_parity=Q2target%2,linear_carry_transform=T%M,
                                  R2=bank[(2,2)],R1_star=bank[(1,1)],floor_algorithm=stats))
        # One exact reflection step for the fixed carry measure, d=0.
        L=M//2
        bank,stats=marginal_bank(M,N,0,limit=L,modulus=M)
        Gamma=((N-1)*(bank[(2,0)]+bank[(0,0)])-bank[(2,1)]-bank[(0,1)])%M
        T=sum(u*q1*(N*w//M) for w,(u,q1) in base.items())%M
        lower=indicator=0
        for w in range(1,L,2):
            u,q1=base[w]
            a=pow(w,-1,L)
            qL=(a*w-1)//L
            eps=qL%2
            assert (2*u*q1-a*qL-(L+1)*eps)%M==0
            weight=N*w//M-(N-1)//2
            lower+=a*qL*weight
            indicator+=(L+1)*eps*weight
            wp=L-w
            up,qp=base[wp]
            assert (u*q1+up*qp-((u*u+1)//2-L//2+int(u>L)))%L==0
        assert T==(Gamma+lower+indicator)%M
        reflections.append(dict(M=M,N=N,T=T,Gamma=Gamma,lower_carry_term=lower%M,
                                new_indicator_term=indicator%M,target_modulus=M,
                                smaller_graph_modulus=L,retained_floor_modulus=M))
large=[]
for k,N,d in ((24,0x5a17d3,12345),(32,0x5a17d3b1,123456789)):
    M=1<<k
    tick=time.monotonic()
    bank,stats=marginal_bank(M,N,d)
    large.append(dict(k=k,N=N,d=d,R2=bank[(2,2)],R1_star=bank[(1,1)],
                      runtime_seconds=time.monotonic()-tick,enumerated_units=0,**stats))
out=dict(packet='F305',route='F31',seed=3052608,
         status='exact_input_transport_and_computable_marginals_not_a_carry_evaluator',
         runtime_seconds=time.monotonic()-started,
         max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
         pointwise_transport_checks=point_checks,shifted_binomial_checks=shifted_checks,
         cases=cases,reflection_checks=reflections,large_marginal_evaluations=large)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
