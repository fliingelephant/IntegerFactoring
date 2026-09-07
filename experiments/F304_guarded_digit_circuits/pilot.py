"""Guarded Newton digit circuits and exact local Taylor controls."""
import json, random, resource, signal, time
from fractions import Fraction as F
from pathlib import Path

signal.alarm(30)
start=time.monotonic()
rng=random.Random(30420260907)

def digits(x,k,p):
    bits=[]; squarings=0
    for j in range(k):
        P=p+k-j; modulus=1<<P
        e=x%modulus
        for _ in range((P-1).bit_length()):
            e=e*e*(3-2*e)%modulus
            squarings+=1
        bits.append(e%(1<<p))
        x=((x-e)%modulus)//2
    return bits,squarings

def selector(bits,A,s,modulus):
    value=1
    for j in range(s,len(bits)):
        value=value*(bits[j] if A>>j&1 else 1-bits[j])%modulus
    return value

rows=[]; checked=0
for k in range(3,11):
    M=1<<k; p=k
    for case in range(4):
        N=rng.randrange(8*M,16*M)|1
        s=rng.randrange(k); t=rng.randrange(k)
        A=rng.randrange(M>>s)<<s; B=rng.randrange(M>>t)<<t
        got=direct=0; gates=0
        for u in range(1,M,2):
            v=N*pow(u,-1,M)%M
            # Use a higher-precision inverse, not the canonical graph v.
            V=N*pow(u,-1,1<<(p+k))%(1<<(p+k))
            ub,g=digits(u,k,p); vb,h=digits(V,k,p)
            assert all(bit==((u>>j)&1) for j,bit in enumerate(ub))
            assert all(bit==((v>>j)&1) for j,bit in enumerate(vb))
            got=(got+selector(ub,A,s,M)*selector(vb,B,t,M))%M
            direct+=A<=u<A+(1<<s) and B<=v<B+(1<<t)
            checked+=2*k; gates+=g+h
        assert got==direct
        rows.append(dict(k=k,N=N,A=A,s=s,B=B,t=t,count=got,point_count=M//2,
                         newton_updates=gates,working_precision_bits=2*k))

def product(a,b,D):
    c=[F(0)]*(D+1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:D+1-i]):
                if y:c[i+j]+=x*y
    return c

jets=[]
for k in range(4,9):
    p=k; D=1<<p.bit_length()
    x=[F(1),F(4)]+[F(0)]*(D-1)
    for j in range(k):
        P=p+k-j; e=x[:]
        for _ in range((P-1).bit_length()):
            square=product(e,e,D); cube=product(square,e,D)
            e=[3*a-2*b for a,b in zip(square,cube)]
        if j<k-1:x=[(a-b)/2 for a,b in zip(x,e)]
    assert not any(e[:D]) and e[D]
    denominator=e[D].denominator
    assert denominator==1<<((k-3)*D)
    jets.append(dict(k=k,first_nonzero_degree=D,coefficient=str(e[D]),
                     denominator_guard_bits=(k-3)*D,
                     available_F303_precision=2*k,
                     truncation_at_first_term_is_nonintegral=True,
                     minimum_mod2_polynomial_degree_on_class=1<<(k-3)))

result=dict(seed=30420260907,rectangles=rows,exact_digit_checks=checked,taylor_jets=jets,
            runtime_seconds=time.monotonic()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            scope='Pointwise polynomial-size circuit and enumerated aggregate controls. No fast whole-graph circuit trace.')
Path(__file__).with_name('output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['exact_digit_checks','taylor_jets','runtime_seconds','peak_rss_bytes']},indent=2))
