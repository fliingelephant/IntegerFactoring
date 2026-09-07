"""Whole-family norm gate, exact high-digit identity, and block audit."""
import json, math, random, resource, signal, sys, time
from pathlib import Path

signal.alarm(30); start=time.monotonic(); rng=random.Random(30720260907)
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'F301_factor_rectangles'))
from factor_rectangles import public_boxes

def universal_bank(k):
    H=1<<(k-1); P=3*k; powers=[]; elements=[1]
    for j in range(P):
        powers.append((H**(j+1)-sum(math.comb(j+1,t)*powers[t] for t in range(j)))//(j+1))
    for j in range(1,P):
        numerator=sum((-1)**(t-1)*elements[j-t]*powers[t] for t in range(1,j+1))
        assert numerator%j==0
        elements.append(numerator//j)
    return elements

def shifted_product(k,cut,elements):
    modulus=1<<(3*k); H=1<<(k-1); a=2*(cut//2)+1
    z=2*pow(a,-1,modulus)%modulus
    return pow(a,H,modulus)*sum(e*pow(z,j,modulus) for j,e in enumerate(elements))%modulus

def norm_gate(N,M,c,d,elements):
    k=M.bit_length()-1; modulus=M**3; invN=pow(N,-1,modulus)
    rho=shifted_product(k,c,elements)*shifted_product(k,d,elements)*pow(invN,M//2,modulus)%modulus
    assert (rho-1)%M==0
    qbar=N*((rho-1)//M)%M
    residual=(rho-1-M*invN*qbar-M*M*invN*invN*(qbar*(qbar-1)//2))%modulus
    assert residual%(M*M)==0
    E=N*N*(residual//(M*M))%M
    return rho,qbar,E

rows=[]; rectangle_rows=[]; block_checks=0; dropped_wrong=0
cases=[]
for k in range(3,11):
    M=1<<k
    for _ in range(3):
        N=rng.randrange(8*M,16*M)|1
        cuts=[(0,0),(M//2,M//2),(0,M),(M,M)]
        cuts += [(rng.randrange(M+1),rng.randrange(M+1)) for _ in range(4)]
        cases.append((N,M,cuts))
for N in [289,323,391,667,899,1517,2021]:
    M,boxes,_=public_boxes(N)
    if M:
        cuts=set()
        for b in boxes:
            cuts.update([(b.x_lo,b.y_lo),(b.x_lo,b.y_hi+1),(b.x_hi+1,b.y_lo),(b.x_hi+1,b.y_hi+1)])
        cases.append((N,M,sorted(cuts)))

banks={}
for N,M,cuts in cases:
    k=M.bit_length()-1
    if k not in banks:banks[k]=universal_bank(k)
    graph=[(u,N*pow(u,-1,M)%M) for u in range(1,M,2)]
    gate_values={}
    for c,d in cuts:
        rho,qbar,E=norm_gate(N,M,c,d,banks[k]); terms=[]
        for u,v in graph:
            x=u+M*(u<c); y=v+M*(v<d); q=(x*y-N)//M
            terms.append((u,v,x,y,q))
        Q=sum(p[4] for p in terms); B=sum(p[4]*(p[4]-1)//2 for p in terms)%M
        h=(Q-qbar)//M
        assert (Q-qbar)%M==0
        assert B==((N-M//2)*h-E)%M
        direct_rho=1
        for *_,q in terms:direct_rho=direct_rho*(1+M*pow(N,-1,M**3)*q)%(M**3)
        assert rho==direct_rho
        dropped_wrong += B!=(-E)%M
        for r in sorted(set([1,max(1,k//2),k-1])):
            R=1<<r; L=M//R; groups={}
            for u,v,x,y,q in terms:
                u0=u%R; v0=v%R; X=(x-u0)//R; Y=(y-v0)//R; n=(N-u0*v0)//R
                assert R*X*Y+v0*X+u0*Y-n==L*q
                assert R*L==M and u0*v0+R*n==N
                groups.setdefault(u0,[]).append(q)
            total_Q=0; total_e2=0; block_product=1
            for qs in groups.values():
                qsum=sum(qs); e2=(qsum*qsum-sum(q*q for q in qs))//2
                total_e2 += e2+total_Q*qsum; total_Q+=qsum
                block_product=block_product*math.prod((1+M*pow(N,-1,M**3)*q)%(M**3) for q in qs)%(M**3)
            assert total_e2==Q*(Q-1)//2-sum(q*(q-1)//2 for *_,q in terms)
            assert block_product==rho
            block_checks+=1
        gate_values[c,d]=(B,Q,qbar,E,h)
        rows.append(dict(N=N,M=M,c=c,d=d,B=B,Qbar=qbar,high_linear_digit=h%M,known_norm_residual=E,
                         zero_high_digit_prediction=(-E)%M,original_precision_bits=3*k,universal_states=3*k))
    # Shifted first-moment mixed differences retain the exact rectangle.
    for _ in range(2):
        a,b=sorted((rng.randrange(M+1),rng.randrange(M+1)))
        c,d=sorted((rng.randrange(M+1),rng.randrange(M+1)))
        values=[]
        for xcut,ycut in [(b,d),(a,d),(b,c),(a,c)]:
            Q=sum(((u+M*(u<xcut))*(v+M*(v<ycut))-N)//M for u,v in graph)
            values.append(Q)
        count=sum(a<=u<b and c<=v<d for u,v in graph)
        assert values[0]-values[1]-values[2]+values[3]==M*count
        rectangle_rows.append(dict(N=N,M=M,a=a,b=b,c=c,d=d,count=count))
result=dict(rows=rows,rectangle_controls=rectangle_rows,block_checks=block_checks,dropping_high_digit_failures=dropped_wrong,
            seed=30720260907,runtime_seconds=time.monotonic()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            scope='The norm gate is non-enumerative. Q and B are enumerated controls; the missing high digit is not computed by the gate.')
Path(__file__).with_name('output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(cut_cases=len(rows),rectangle_checks=len(rectangle_rows),block_checks=block_checks,
                     dropping_high_digit_failures=dropped_wrong,runtime_seconds=result['runtime_seconds'],peak_rss_bytes=result['peak_rss_bytes']),indent=2))
