"""F303/F31 global moment precision pilot; 60sec/<512MiB budget.

Fast routines never enumerate the unit group. Small direct scans certify
them; large-bit cases exercise only the polynomial-size universal formulas.
"""
import json
import math
import random
import resource
import signal
import time
from pathlib import Path

signal.alarm(60)
started=time.monotonic()
rng=random.Random(3032608)
degree=4
moments=((1,1),(1,2),(2,2),(1,3),(1,5),(2,5),(3,3))

def valuation(x):
    return None if x==0 else (abs(x)&-abs(x)).bit_length()-1

def universal(k):
    M=1<<k
    bits=3*k+max(valuation(j) for j in range(1,degree+1))
    modulus=1<<bits
    J=M//4
    top=max(degree,(bits-1)//2)
    ps=[J]
    for j in range(1,top+1):
        numerator=J**(j+1)-sum(math.comb(j+1,h)*ps[h] for h in range(j))
        assert numerator%(j+1)==0
        ps.append(numerator//(j+1))
    elementary=[1]
    for j in range(1,top+1):
        numerator=sum((-1)**(h-1)*elementary[j-h]*ps[h] for h in range(1,j+1))
        assert numerator%j==0
        elementary.append(numerator//j)
    product=1
    for a in (1,3):
        inv=pow(a,-1,modulus)
        expansion=sum(elementary[j]*pow(4*inv,j,modulus) for j in range(top+1))%modulus
        product=product*pow(a,J,modulus)*expansion%modulus
    positive=[M//2]
    negative=[M//2]
    for j in range(1,degree+1):
        positive.append(sum(math.comb(j,h)*4**h*ps[h]*(1+3**(j-h)) for h in range(j+1)))
        value=0
        for a in (1,3):
            inv=pow(a,-1,modulus)
            value+=sum((-1)**h*math.comb(j+h-1,h)*pow(4,h,modulus)*pow(inv,j+h,modulus)*ps[h]
                       for h in range(top+1))
        negative.append(value%modulus)
    return dict(k=k,M=M,bits=bits,product=product,positive=positive,negative=negative,
                truncation_degree=top,max_exact_bits=max(x.bit_length() for x in ps+elementary))

def accessible(data,N):
    M=data['M']
    mod2,mod3=M*M,M**3
    phi=M//2
    R0=data['product']**2*pow(N,-phi,mod3)%mod3
    w=(R0-1)%mod3
    assert w%M==0
    logR=(w-w*w//2)%mod3
    L=[(N*logR%mod3)//M]
    for j in range(1,degree+1):
        v=valuation(j)
        work=mod3<<v
        numerator=(N*data['positive'][j]-pow(N,j+1,work)*data['negative'][j])%work
        assert numerator%(M<<v)==0
        L.append((numerator//(M<<v))*pow(j>>v,-1,mod2)%mod2)
    K=(N*w%mod3)//M
    return L,K

def direct(M,N):
    pairs=[(u,N*pow(u,-1,M)%M) for u in range(1,M,2)]
    carry=[(u,(u*v-N)//M) for u,v in pairs]
    Q1=[sum(u**j*q for u,q in carry) for j in range(degree+1)]
    Q2=[sum(u**j*q*q for u,q in carry) for j in range(degree+1)]
    S={(a,b):sum(u**a*v**b for u,v in pairs) for a,b in moments}
    return S,Q1,Q2

rows=[]
sequence_rows=[]
congruence_checks=0
third_digit_checks=0
weighted_carry_checks=0
for k in range(3,13):
    data=universal(k)
    M=data['M']
    actual_product=1
    for u in range(1,M,2):
        actual_product=actual_product*u%(1<<data['bits'])
    assert actual_product==data['product']
    for j in range(1,degree+1):
        assert sum(u**j for u in range(1,M,2))==data['positive'][j]
        assert sum(pow(u,-j,1<<data['bits']) for u in range(1,M,2))%(1<<data['bits'])==data['negative'][j]
    length=min(65,M//2)
    inputs=list(range(1,2*length,2))
    inputs+=sorted({rng.randrange(1,M,2) for _ in range(4)}-set(inputs))
    seqE=[]
    seqQ=[]
    seqResidual=[]
    for N in inputs:
        L,K=accessible(data,N)
        S,Q1,Q2=direct(M,N)
        E2=(Q1[0]**2-Q2[0])//2
        assert (Q1[0]**2-Q2[0])%2==0
        for j in range(degree+1):
            assert L[j]%M==Q1[j]%M
            assert (L[j]+(M//2)*(j+1)*pow(N,-1,M*M)*Q2[j])%(M*M)==Q1[j]%(M*M)
            weighted_carry_checks+=1
        for a0,b0 in moments:
            a,b=max(a0,b0),min(a0,b0)
            j=a-b
            known=(pow(N,b,M**3)*data['positive'][j]+b*M*pow(N,b-1,M**3)*L[j])%(M**3)
            assert known%(M*M)==S[(a0,b0)]%(M*M)
            congruence_checks+=1
            corrected=(known+a*b*(M*M//2)*pow(N,b-2,M**3)*Q2[j])%(M**3)
            assert corrected==S[(a0,b0)]%(M**3)
            third_digit_checks+=1
        assert S[(1,2)]==M*S[(1,1)]-M*M*(M*M+2)//24
        noE2=(M//2*N+M*K)%(M**3)
        assert (noE2-M*M*pow(N,-1,M**3)*E2)%(M**3)==S[(1,1)]
        residual=(S[(1,1)]-noE2)//(M*M)%M
        assert residual==(-pow(N,-1,M)*E2)%M
        if N<2*length:
            seqE.append(E2%M)
            seqQ.append(Q2[0]%(2*M))
            seqResidual.append(residual)
    coefficients={}
    for label,seq,mod in (('E2_mod_M',seqE,M),('Q02_mod_2M',seqQ,2*M),('normalized_residual_mod_M',seqResidual,M)):
        diff=seq[:]
        vals=[]
        while diff:
            vals.append(diff[0]%mod)
            diff=[(y-x)%mod for x,y in zip(diff,diff[1:])]
        coefficients[label]=dict(modulus=mod,coefficients=vals,valuations=[valuation(v) for v in vals])
    sequence_rows.append(dict(k=k,M=M,input_N='1+2t',length=length,mahler=coefficients))
    sampleN=1
    sampleS,_,_=direct(M,sampleN)
    rows.append(dict(k=k,M=M,cases=len(inputs),working_bits=data['bits'],
                     product_mod_work=data['product'],max_exact_bits=data['max_exact_bits'],
                     sample_S11=sampleS[(1,1)],sample_S11_mod_M2=sampleS[(1,1)]%(M*M)))
large=[]
for k in (32,64,128):
    tick=time.monotonic()
    data=universal(k)
    M=data['M']
    values=[]
    for N in (1,3,(M//3)|1):
        L,K=accessible(data,N)
        values.append(dict(N=N,S11_mod_M2=(N*(M//2)+M*L[0])%(M*M),
                           accessible_third_precision_part=(N*(M//2)+M*K)%(M**3)))
    large.append(dict(k=k,working_bits=data['bits'],truncation_degree=data['truncation_degree'],
                      max_exact_bits=data['max_exact_bits'],runtime_seconds=time.monotonic()-tick,
                      enumerated_units=0,values=values))
block_checks=[]
for M in (8,16):
    for R in (2,4):
        for N in (1,3):
            base=direct(M,N)[0][(1,1)]
            total=sum(direct(M*R,N+M*t)[0][(1,1)] for t in range(R))
            correction=M**3*R**2*(R**2-1)//8
            assert total==R**2*base+correction
            assert ((total-correction)%(M*R)**2)//R**2==base%(M*M)
            block_checks.append(dict(M=M,R=R,N=N,total=total,base_S11=base))
out=dict(packet='F303',route='F31',seed=3032608,
         status='exact_small_certificates_and_polynomial_size_large_bit_evaluations',
         runtime_seconds=time.monotonic()-started,
         max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
         mixed_M2_checks=congruence_checks,mixed_M3_correction_checks=third_digit_checks,
         weighted_carry_checks=weighted_carry_checks,small_cases=rows,
         large_bit_evaluations=large,mahler_sequences=sequence_rows,
         exact_high_input_block_checks=block_checks)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
