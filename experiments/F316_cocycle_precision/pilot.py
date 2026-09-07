"""F316 full precision section controls; 30s, estimated <32MiB."""
from pathlib import Path
import json, random, resource, signal, time

signal.alarm(30)
start=time.monotonic()
rng=random.Random(316)
checks=dict(carry4=0,product4=0,fold4=0,high_digit_replacement=0,guarded_recursion=0,transport4=0)
failures=[]
projection_failures=[]
mixed_examples=[]
rows=[]
for k in range(4,10):
    M=1<<k
    T=M//4
    H=T//2
    units=list(range(1,M,4))
    e=[pow(5,j,4*M)//M for j in range(T)]
    eta=[x%2 for x in e]
    section_square=[sum(e[j]*e[(r-j)%T] for j in range(T))%4 for r in range(T)]
    binary_square=[sum(eta[j]*eta[(r-j)%T] for j in range(T))%4 for r in range(T)]
    assert section_square==binary_square
    checks['high_digit_replacement']+=T
    for _ in range(24):
        a=rng.randrange(T)
        b=rng.randrange(T)
        A=pow(5,a,M)
        B=pow(5,b,M)
        cA=[(A*pow(5,j,M)//M)%4 for j in range(T)]
        for j in range(T):
            assert cA[j]==(3*((a+j)//T)-e[a]-e[j]+e[(a+j)%T])%4
            checks['carry4']+=1
        cB=[(B*pow(5,j,M)//M)%4 for j in range(T)]
        actual=sum(cA[j]*cB[-j%T] for j in range(T))%4
        linear=sum(e[(b-j)%T]-e[-j%T] for j in range(T-a,T))
        quadratic=section_square[0]-section_square[a]-section_square[b]+section_square[(a+b)%T]
        predicted=(max(0,a+b-T+1)+2*linear+quadratic-3*(b*e[a]+a*e[b]))%4
        assert actual==predicted
        checks['product4']+=1
        L_a=sum(e[r]+e[T-r] for r in range(1,a+1))
        R0=sum(x*x for x in e)
        Ra=sum(e[j]*e[(j+a)%T] for j in range(T))
        t_formula=(2*a+L_a+section_square[0]-section_square[a]+R0-Ra-(A-1)//2)%4
        t_raw=sum(pow(w,-1,M)*((w*pow(w,-1,M)-1)//M)*(A*w//M) for w in range(1,M,2))
        assert t_raw%2==0 and (t_raw//2)%4==t_formula
        checks['transport4']+=1
        naive=(max(0,a+b-T+1)+quadratic-3*(b*e[a]+a*e[b]))%4
        if actual!=naive and len(failures)<6:
            failures.append(dict(M=M,a=a,b=b,actual=actual,drop_linear=naive,linear_mod2=linear%2))
        rows.append(dict(M=M,a=a,b=b,carry_product_mod4=actual,linear_mod2=linear%2,
                         quadratic_mod4=quadratic%4))
    if k>=5:
        lower=[pow(5,j,M)//(M//2) for j in range(H)]
        for j in range(H):
            assert (e[j]-e[j+H]-(1-lower[j]+2*(j%2)))%4==0
        # Anti-periodic projection is a genuine smaller-section square,
        # in the negacyclic ring; preserve its wrap signs.
        d=[1-x for x in lower]
        negacyclic=[(sum(d[j]*d[r-j] for j in range(r+1))
                    -sum(d[j]*d[r+H-j] for j in range(r+1,H)))%4 for r in range(H)]
        for r in range(H):
            assert (section_square[r]-section_square[r+H])%4==negacyclic[r]
            cyclic=sum(d[j]*d[(r-j)%H] for j in range(H))%4
            assert (section_square[r]+section_square[r+H])%4==cyclic
            naive=((cyclic+negacyclic[r])%8)//2
            if naive!=section_square[r] and len(projection_failures)<8:
                projection_failures.append(dict(M=M,r=r,plus_mod4=cyclic,minus_mod4=negacyclic[r],
                    actual_mod4=section_square[r],unguarded_half=naive))
            prefix=sum(d[j]*d[r-j] for j in range(r+1))%4
            point=sum(eta[j]*eta[(r-j)%H] for j in range(H))%2
            mixed=sum(eta[j]*d[(r-j)%H] for j in range(H))%2
            reconstructed=(prefix+2*(point-mixed))%4
            assert reconstructed==section_square[r]
            checks['guarded_recursion']+=1
            if mixed and len(mixed_examples)<6:
                mixed_examples.append(dict(M=M,r=r,prefix_mod4=prefix,point_bit=point,
                    mixed_bit=mixed,result_mod4=reconstructed))
            checks['fold4']+=1
result=dict(checks=checks,rows=rows,failures=failures,projection_failures=projection_failures,
            mixed_examples=mixed_examples,seconds=time.monotonic()-start,
            peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
