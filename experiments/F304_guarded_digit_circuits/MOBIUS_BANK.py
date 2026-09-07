"""Non-enumerative normalized Möbius moment bank; enumeration only audits."""
import json, math, random, resource, signal, time
from pathlib import Path

def bank(s,A,B,C,n,D):
    L=1<<s; v=(C&-C).bit_length()-1
    J=max(D,2*D-1+(s-1)//v)
    E=J+1
    W=2*s+E-E.bit_count()
    limit=2*E+W+2*D+3
    powers=[]
    for j in range(limit+1):
        powers.append((L**(j+1)-sum(math.comb(j+1,t)*powers[t] for t in range(j)))//(j+1))

    def universal(i,j,P):
        mod=1<<P
        if j==0:return powers[i]%mod
        invB=pow(B,-1,mod); total=0
        for ell in range(j+1):
            outer=math.comb(j,ell)*pow(n,j-ell,mod)*pow(-A,ell,mod)*pow(invB,j,mod)
            for t in range((P-1)//v+1):
                coeff=(-1)**t*math.comb(j+t-1,t)*pow(C*invB,t,mod)
                total+=outer*coeff*powers[i+ell+t]
        return total%mod

    ordinary=[powers[j]%(1<<W) for j in range(E+1)]
    rational=[universal(0,j,W) for j in range(E+1)]
    elements=[]
    for ps in [ordinary,rational]:
        el=[1]
        for j in range(1,E+1):
            vj=(j&-j).bit_length()-1
            precision=2*s+(E-E.bit_count())-(j-j.bit_count())
            modulus=1<<precision
            numerator=sum((-1)**(t-1)*el[j-t]*ps[t] for t in range(1,j+1))%(modulus<<vj)
            assert numerator%(1<<vj)==0
            el.append((numerator>>vj)*pow(j>>vj,-1,modulus)%modulus)
        elements.append(el)
    mod=L*L; ratio=[1]
    for j in range(1,E+1):
        ratio.append((elements[0][j]-sum(elements[1][t]*ratio[j-t] for t in range(1,j+1)))%mod)
        assert ratio[j]%L==0
    Q=[(-1)**j*(ratio[j+1]//L)%L for j in range(J+1)]
    moments={}
    invA=pow(A,-1,L)
    for i in range(D+1):
        for j in range(D+1):
            value=universal(i,j,2*s)
            if j:
                weighted=0
                if i==0:weighted=Q[j-1]
                else:
                    for ell in range(i+1):
                        outer=math.comb(i,ell)*pow(n,i-ell,L)*pow(-B,ell,L)*pow(invA,i,L)
                        for t in range((s-1)//v+1):
                            coeff=(-1)**t*math.comb(i+t-1,t)*pow(C*invA,t,L)
                            weighted+=outer*coeff*Q[j-1+ell+t]
                value=(value+j*L*weighted)%mod
            moments[i,j]=value
    return moments,Q,dict(carry_indices=J+1,series_degree=E,guard_precision_bits=W,
                          universal_power_indices=limit+1,canonical_points_enumerated=0)

if __name__=='__main__':
    signal.alarm(30); start=time.monotonic(); rng=random.Random(304021)
    rows=[]; checks=0
    for k in range(4,10):
        M=1<<k
        for r in sorted(set([1,2,max(1,k//2)])):
            R=1<<r; L=M//R; s=k-r
            for case in range(2):
                N=rng.randrange(8*M,16*M)|1
                u0=rng.randrange(R//2)*2+1; v0=N*pow(u0,-1,R)%R
                A=v0; B=u0; C=R; n=(N-u0*v0)//R
                moments,Q,counts=bank(s,A,B,C,n,3)
                points=[(x,(n-A*x)*pow(B+C*x,-1,L)%L) for x in range(L)]
                for (i,j),value in moments.items():
                    assert value==sum(x**i*y**j for x,y in points)%(L*L)
                    checks+=1
                for j,value in enumerate(Q):
                    expected=0
                    for x,y in points:
                        denominator=B+C*x; T=(n-A*x)*pow(denominator,-1,L)%L
                        q=(denominator*y-(n-A*x))//L
                        expected+=q*pow(denominator,-1,L)*pow(T,j,L)
                    assert value==expected%L
                    checks+=1
                rows.append(dict(k=k,r=r,N=N,u0=u0,v0=v0,L=L,oracle=counts,moments={f'{i},{j}':v for (i,j),v in moments.items()}))
    # Newton error bank identity, verified before any division.
    for a in range(-20,21):
        delta=a*a-a; new=3*a*a-2*a*a*a
        assert new*new-new==delta*delta*(4*delta-3)
    result=dict(rows=rows,exact_checks=checks,seed=304021,runtime_seconds=time.monotonic()-start,
                peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                scope='A non-enumerative moment oracle for one actual low-residue patch, not its full patch family or a rectangle oracle.')
    Path(__file__).with_name('MOBIUS_BANK_output.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['exact_checks','runtime_seconds','peak_rss_bytes']},indent=2))
