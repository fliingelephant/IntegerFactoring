"""F312 exact orbit/quotient pilot, 30 seconds and <256 MiB."""
from pathlib import Path
import json, random, resource, signal, time

signal.alarm(30)
start=time.monotonic()
rng=random.Random(312)
checks=dict(lift=0,cut_lift=0,parity_reduction=0,orbit=0,square_classes=0,precision_compression=0)
separators=[]
cut_failures=[]
rows=[]
for k in range(4,10):
    M=1<<k
    L=M//2
    units=list(range(1,M,2))
    inv={w:pow(w,-1,M) for w in units}
    for A in sorted({1,3,5,M-1,*[rng.randrange(1,M,2) for _ in range(4)]}):
        f={w:A*w//M for w in units}
        K=sum(f[w]*f[inv[w]] for w in units)
        U=sum(x*x for x in f.values())
        selected=sum(x%2 for x in f.values())
        overlap=sum((f[w]%2)*(f[inv[w]]%2) for w in units)
        assert (K-U+selected-overlap)%8==0
        checks['parity_reduction']+=1
        h=(A-1)//2
        for epsilon in (1,3,5,7):
            image={w:epsilon*inv[w]%M for w in units}
            twisted=sum(f[w]*f[image[w]] for w in units)
            overlap_eps=sum((f[w]%2)*(f[image[w]]%2) for w in units)
            root_term=sum((f[w]-h)%2 for w in units if w<M//2 and (w*w+epsilon)%M==0)
            assert (twisted-U+selected-overlap_eps+4*root_term)%8==0
            checks['square_classes']+=1
            for p in range(3,min(k,7)+1):
                q=1<<(p-2)
                g={w:(f[w]-h)%q if w<M//2 else -((f[M-w]-h)%q) for w in units}
                predicted=U+sum(g[w]*g[image[w]]-g[w]**2 for w in units)
                assert (twisted-predicted)%(1<<p)==0
                checks['precision_compression']+=1
        shifted={w:(A*w-2)//M for w in units}
        shifted_K=sum(shifted[w]*shifted[inv[w]] for w in units)
        naive=sum(shifted[w]**2-(shifted[w]%2)+(shifted[w]%2)*(shifted[inv[w]]%2) for w in units)
        if (shifted_K-naive)%8 and len(cut_failures)<6:
            cut_failures.append(dict(M=M,A=A,d=2,K_mod8=shifted_K%8,naive_mod8=naive%8))
        remaining=set(units)
        while remaining:
            w=min(remaining)
            orbit={w,(-w)%M,(w+L)%M,(-w+L)%M,
                   inv[w],(-inv[w])%M,(inv[w]+L)%M,(-inv[w]+L)%M}
            remaining-=orbit
            norm=sum(f[x]*f[inv[x]]-f[x]**2 for x in orbit)
            assert norm%2==0
            if len(orbit)==8:
                delta=f[w]-f[inv[w]]
                dw=f[(w+L)%M]-f[w]
                du=f[(inv[w]+L)%M]-f[inv[w]]
                predicted=-2*((delta%2)+((delta+dw-du)%2))
                assert (norm-predicted)%8==0
                if norm%8 and len(separators)<12:
                    separators.append(dict(M=M,A=A,orbit=sorted(orbit),
                        floor_values=[f[x] for x in sorted(orbit)],
                        norm_mod8=norm%8,delta_parity=delta%2,
                        translation_parity_change=(dw-du)%2))
            checks['orbit']+=1
        B=rng.randrange(1,M,2)
        d=rng.choice((-M//3,0,M//3))
        e=rng.choice((-2,0,M//4))
        direct=sum(((A*w-d)//M)*((B*inv[w]-e)//M) for w in units)
        lifted=0
        directcut=sum(((A*w-d)//M)*((B*inv[w]-e)//M)*int(w<M//3)*int(inv[w]<3*M//4) for w in units)
        liftedcut=0
        for a in range(1,L,2):
            b=pow(a,-1,L)
            carry=((a*b-1)//L)%2
            x=[(A*(a+L*t)-d)//M for t in (0,1)]
            y=[(B*(b+L*t)-e)//M for t in (0,1)]
            PA=(A*a-d)//L+(A-1)//2
            QA=-(A-1)//2-int((A*a-d)%M>=L)
            PB=(B*b-e)//L+(B-1)//2
            QB=-(B-1)//2-int((B*b-e)%M>=L)
            assert PA==sum(x) and QA==x[0]-x[1]
            assert PB==sum(y) and QB==y[0]-y[1]
            numerator=PA*PB+(-1)**carry*QA*QB
            assert numerator%2==0
            lifted+=numerator//2
            xc=[x[t]*int(a+L*t<M//3) for t in (0,1)]
            yc=[y[t]*int(b+L*t<3*M//4) for t in (0,1)]
            cutnum=sum(xc)*sum(yc)+(-1)**carry*(xc[0]-xc[1])*(yc[0]-yc[1])
            assert cutnum%2==0
            liftedcut+=cutnum//2
        assert direct==lifted
        assert directcut==liftedcut
        checks['lift']+=1
        checks['cut_lift']+=1
        rows.append(dict(M=M,A=A,B=B,d=d,e=e,K_mod8=K%8,
            ordinary_square_mod8=U%8,odd_floor_count_mod8=selected%8,
            parity_overlap_mod8=overlap%8))

# A translation orbit of size 8 is affine for inversion when M>=64.
# These full carry truth tables test the proposed carry-independent norm.
tables=[]
for A,p,q in ((1,0,0),(3,0,0),(3,2,5),(5,1,7),(17,3,2)):
    values=[sum(((p+A*t)//8)*((q+A*((c-t)%8))//8) for t in range(8))%8 for c in range(8)]
    tables.append(dict(A=A,p=p,q=q,carry_values=values))

result=dict(checks=checks,rows=rows,separators=separators,cut_failures=cut_failures,translation_tables=tables,
            seconds=time.monotonic()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({key:value for key,value in result.items() if key!='rows'},indent=2))
