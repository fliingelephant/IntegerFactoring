"""F308 exact cocycle and square-input precision pilot. 30s / <256MiB."""
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import json, math, random, resource, signal, time

signal.alarm(30)
start=time.monotonic()
rng=random.Random(308)

def floor_square(M,A):
    # Degree-two specialization of F305's exact Euclidean recurrence.
    polys=((Fraction(0),Fraction(1)),
           (Fraction(0),Fraction(-1,2),Fraction(1,2)),
           (Fraction(0),Fraction(1,6),Fraction(-1,2),Fraction(1,3)))
    @lru_cache(None)
    def F(p,q,n,m,a,b):
        if not n:
            return 0
        if not q:
            return sum(c*n**j for j,c in enumerate(polys[p]))
        aa,a0=divmod(a,m)
        bb,b0=divmod(b,m)
        if aa or bb:
            return sum(math.comb(q,h)*math.comb(q-h,j)*aa**j*bb**(q-h-j)*F(p+j,h,n,m,a0,b0)
                       for h in range(q+1) for j in range(q-h+1) if aa**j*bb**(q-h-j))
        if not a:
            return 0
        H=(a*(n-1)+b)//m
        return F(p,0,n,m,a,b)*H**q-sum(math.comb(q,j)*c*F(j,s,H,a,m,m-b+a-1)
                    for j in range(q) for s,c in enumerate(polys[p]) if c)
    value=Fraction(F(0,2,M//2,M,2*A,A))
    assert value.denominator==1
    return value.numerator,F.cache_info().currsize

def base_carry_mod4(M):
    # P238's unit product, only k+2 bits needed here.
    modulus=4*M
    top=(modulus.bit_length()-2)//2
    J=M//4
    ps=[J]
    for j in range(1,top+1):
        ps.append((J**(j+1)-sum(math.comb(j+1,h)*ps[h] for h in range(j)))//(j+1))
    es=[1]
    for j in range(1,top+1):
        es.append(sum((-1)**(h-1)*es[j-h]*ps[h] for h in range(1,j+1))//j)
    product=1
    for a in (1,3):
        product=product*pow(a,J,modulus)*sum(es[j]*pow(4*pow(a,-1,modulus),j,modulus) for j in range(top+1))%modulus
    residue=(product*product-1)%modulus
    assert residue%M==0
    return residue//M

counts=dict(point=0,cocycle=0,shifted=0,square_precision=0)
rows=[]
for k in range(3,10):
    M=1<<k
    units=range(1,M,2)
    inv={w:pow(w,-1,M) for w in units}
    mu={w:inv[w]*((w*inv[w]-1)//M) for w in units}
    Q=sum((w*inv[w]-1)//M for w in units)
    assert base_carry_mod4(M)==Q%4
    values=sorted({1,3,5,M-1,M//2+1,*[rng.randrange(1,M,2) for _ in range(6)]})
    T={A:sum(mu[w]*(A*w//M) for w in units)%M for A in values}
    for A in values:
        assert T[A]%2==0
        sq,states=floor_square(M,A)
        rawsq,rawstates=floor_square(M,A*A)
        assert sq==sum((A*w//M)**2 for w in units)
        numerator=rawsq-(A*A+1)*sq
        assert numerator%(2*A)==0
        R=numerator//(2*A)
        assert R==sum((A*w//M)*(A*(A*w%M)//M) for w in units)
        K=sum((A*w//M)*(A*inv[w]//M) for w in units)
        Kfast=2*(A*(M//2-1)//M)%4
        assert K%4==Kfast
        N=A*A%M
        predicted=(-Kfast+pow(A,-1,4)*R-(A*A//M)*base_carry_mod4(M))%4
        actual=sum(mu[w]*(N*w//M) for w in units)%4
        assert predicted==actual
        counts['square_precision']+=1
        rows.append(dict(M=M,A=A,N=N,T_mod4=actual,K_mod4=Kfast,R_mod4=R%4,states=states+rawstates))
        B=rng.choice(values)
        b=inv[B]
        qB=(B*b-1)//M
        for w in units:
            u=inv[w]
            v=B*w%M
            assert (mu[v]-(b*mu[w]+b*qB*u-b*u//M-b*b*u*u*(B*w//M)))%M==0
            counts['point']+=1
        for d in (0,M//3):
            TA=sum(mu[w]*((A*w-d)//M) for w in units)
            TAB=sum(mu[w]*((A*B*w-d)//M) for w in units)
            K=sum(((A*w-d)//M)*(B*inv[w]//M) for w in units)
            R=sum(inv[w]**2*(B*w//M)*((A*(B*w%M)-d)//M) for w in units)
            assert (TAB-B*TA-A*T[B]+K-b*R)%M==0
            counts['cocycle']+=1
            c=M//3
            TcA=sum((mu[w]+int(inv[w]<c))*((A*w-d)//M) for w in units)
            TcB=sum((mu[w]+int(inv[w]<c))*(B*w//M) for w in units)
            TcAB=sum((mu[w]+int(inv[w]<c))*((A*B*w-d)//M) for w in units)
            cut=sum((int(B*inv[w]%M<c)-B*int(inv[w]<c))*((A*w-d)//M) for w in units)
            assert (TcAB-B*TcA-A*TcB+K-b*R-cut)%M==0
            counts['shifted']+=1

large=[]
for k in (32,64,128):
    tick=time.monotonic()
    M=1<<k
    A=(M//3)|1
    U,s1=floor_square(M,A)
    V,s2=floor_square(M,A*A)
    R=(V-(A*A+1)*U)//(2*A)
    value=(-2*(A*(M//2-1)//M)+pow(A,-1,4)*R-(A*A//M)*base_carry_mod4(M))%4
    large.append(dict(k=k,A=A,N=A*A%M,T_mod4=value,states=s1+s2,seconds=time.monotonic()-tick))
result=dict(counts=counts,rows=rows,large=large,seconds=time.monotonic()-start,
            peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({key:value for key,value in result.items() if key!='rows'},indent=2))
