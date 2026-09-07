"""Exact ring phases, field trace fitting, Walsh tests, and log coordinates."""
import json, math, random, resource, signal, time
from pathlib import Path
signal.alarm(30); start=time.monotonic(); rng=random.Random(31120260907)

def mul(a,b,poly,m):
    z=0
    while b:
        if b&1:z^=a
        b>>=1; a<<=1
        if a>>m:a^=poly
    return z

def gcdpoly(a,b):
    while b:
        while a.bit_length()>=b.bit_length():a^=b<<(a.bit_length()-b.bit_length())
        a,b=b,a
    return a

def fieldpoly(m):
    for p in range((1<<m)|1,1<<(m+1),2):
        z=2; good=True
        for j in range(1,m+1):
            z=mul(z,z,p,m)
            if j<=m//2 and gcdpoly(z^2,p)!=1:good=False;break
        if good and z==2:return p
    raise AssertionError('irreducible polynomial missing')

def basis(columns):
    out={}
    for j,col in enumerate(columns):
        mask=1<<j
        while col:
            p=col.bit_length()-1
            if p not in out:out[p]=(col,mask);break
            old,w=out[p];col^=old;mask^=w
    return out

def solve(target,b):
    mask=0
    while target:
        p=target.bit_length()-1
        if p not in b:return None
        old,w=b[p];target^=old;mask^=w
    return mask

rows=[]; field_rows=[]; summary=[]
for m in range(3,13):
    q=1<<m; M=4*q; L=2*q; s=m+1
    residues=list(range(1,2*q,2)) if m<=8 else sorted(set([1,3,5,7,2*q-1]+[rng.randrange(q)*2+1 for _ in range(27)]))
    invring=[pow(1+2*x,-1,L) for x in range(q)]
    logperm=[(((-1 if z&1 else 1)*pow(5,z>>1,L))%L-1)//2 for z in range(q)]
    assert len(set(logperm))==q
    local=[]
    for residue in residues:
        N=8*M+residue; n=(N-1)//2
        natural=[((n-x)*invring[x]%L)>>m for x in range(q)]
        assert all((((n+q-x)*invring[x]%L)>>m)==1-natural[x] for x in range(q))
        for encoding,values in [('ordinary',natural),('sign_log',[natural[x] for x in logperm])]:
            S=q-2*sum(values); walsh=[1-2*v for v in values]; anf=values[:]
            h=1
            while h<q:
                for a in range(0,q,2*h):
                    for j in range(h):
                        u,v=walsh[a+j],walsh[a+j+h]
                        walsh[a+j],walsh[a+j+h]=u+v,u-v
                        anf[a+j+h]^=anf[a+j]
                h*=2
            degree=max((j.bit_count() for j,v in enumerate(anf) if v),default=0)
            wmax=max(abs(x) for x in walsh)
            lower=next(g for g in range(q) if max(0,wmax-1)**2<=4*g*g*q)
            row=dict(m=m,N=N,M=M,encoding=encoding,S=S,truth_hex=hex(sum(v<<j for j,v in enumerate(values))),
                     anf_degree=degree,walsh_max=wmax,
                     elliptic_total_bound_failure=degree>1 and max(0,abs(S)-1)**2>4*q,
                     elliptic_walsh_bound_failure=degree>1 and max(0,wmax-1)**2>4*q,
                     two_pole_genus_lower_bound=lower if degree>1 else 0,
                     quadratic_boolean=degree<=2)
            rows.append(row);local.append(row)
    if m<=8:
        p=fieldpoly(m)
        # Exact inverse and trace tables in the verified polynomial basis.
        inv=[0]*q
        for x in range(1,q):
            a=x; b=q-2; z=1
            while b:
                if b&1:z=mul(z,a,p,m)
                b>>=1;a=mul(a,a,p,m)
            inv[x]=z;assert mul(x,z,p,m)==1
        tr=[]
        for x in range(q):
            t=x; z=0
            for _ in range(m):z^=t;t=mul(t,t,p,m)
            assert z in [0,1];tr.append(z)
        tracebits=[sum(tr[mul(x,1<<j,p,m)]<<j for j in range(m)) for x in range(q)]
        columns={}; positive=list(range(q)); negative=inv[:]
        cap=min(31,q-1)
        for d in range(1,cap+1,2):
            for label,vals in [('positive',positive),('inverse',negative)]:
                cc=[0]*m
                for x,v in enumerate(vals):
                    bits=tracebits[v]
                    for j in range(m):
                        if bits>>j&1:cc[j]|=1<<x
                columns[label,d]=cc
            positive=[mul(v,mul(x,x,p,m),p,m) for x,v in enumerate(positive)]
            negative=[mul(v,mul(inv[x],inv[x],p,m),p,m) for x,v in enumerate(negative)]
        base=[(1<<q)-1,1]
        models={
            'two_simple_poles_genus1':base+columns['positive',1]+columns['inverse',1],
            'orders_3_1_genus2':base+columns['positive',1]+columns['positive',3]+columns['inverse',1],
            'orders_1_3_genus2':base+columns['positive',1]+columns['inverse',1]+columns['inverse',3]}
        shifted=[0]*m
        for x in range(q):
            bits=tracebits[inv[x^1]]
            for j in range(m):
                if bits>>j&1:shifted[j]|=1<<x
        models['three_simple_poles_genus2']=base+[2]+columns['positive',1]+columns['inverse',1]+shifted
        for name,cols in models.items():
            bb=basis(cols)
            for row in local:row[name]=solve(int(row['truth_hex'],16),bb) is not None
        growing=base[:];labels=['constant','exception_at_zero'];left=list(local)
        for d in range(1,cap+1,2):
            for label in ['positive','inverse']:
                growing+=columns[label,d];labels += [f'{label}_{d}_bit{j}' for j in range(m)]
            bb=basis(growing); remaining=[]
            for row in left:
                solution=solve(int(row['truth_hex'],16),bb)
                if solution is None:remaining.append(row)
                else:
                    row['first_symmetric_odd_pole_order']=d
                    row['trace_witness']=[labels[j] for j in range(len(labels)) if solution>>j&1]
                    check=0
                    for j,col in enumerate(growing):
                        if solution>>j&1:check^=col
                    assert check==int(row['truth_hex'],16)
            left=remaining
        for row in left:row['first_symmetric_odd_pole_order']=None
        field_rows.append(dict(m=m,polynomial=hex(p),symmetric_pole_order_cap=cap,final_space_rank=len(bb),unfitted=len(left)))
    summary.append(dict(m=m,per_encoding=len(residues),exhaustive_mod_complement=m<=8,
                        encodings={enc:dict(max_abs_S=max(abs(x['S']) for x in local if x['encoding']==enc),
                                            max_walsh=max(x['walsh_max'] for x in local if x['encoding']==enc),
                                            max_genus_lower=max(x['two_pole_genus_lower_bound'] for x in local if x['encoding']==enc),
                                            total_bound_failures=sum(x['elliptic_total_bound_failure'] for x in local if x['encoding']==enc),
                                            walsh_bound_failures=sum(x['elliptic_walsh_bound_failure'] for x in local if x['encoding']==enc),
                                            quadratic_count=sum(x['quadratic_boolean'] for x in local if x['encoding']==enc))
                                   for enc in ['ordinary','sign_log']}))
result=dict(seed=31120260907,summary=summary,fields=field_rows,rows=rows,
            runtime_seconds=time.monotonic()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            scope='Original N and full period phase. Field fits use explicit coordinate identifications; no selected-window evaluator.')
Path(__file__).with_name('output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(summary=summary,fields=field_rows,runtime_seconds=result['runtime_seconds'],peak_rss_bytes=result['peak_rss_bytes']),indent=2))
