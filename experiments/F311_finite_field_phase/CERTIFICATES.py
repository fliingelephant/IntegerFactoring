"""An exact corrected genus-two fit and a larger fixed-family dual witness."""
import json, resource, signal, time
from pathlib import Path
signal.alarm(30);start=time.monotonic();folder=Path(__file__).resolve().parent
prior=json.loads((folder/'output.json').read_text());results=[]

def mul(a,b,p,m):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a>>m:a^=p
    return z

for m,N,enc,kind in [(4,527,'sign_log','three_simple_poles'),(8,8193,'ordinary','orders_31_31')]:
    q=1<<m;p=int(next(x['polynomial'] for x in prior['fields'] if x['m']==m),16)
    target=int(next(x['truth_hex'] for x in prior['rows'] if x['m']==m and x['N']==N and x['encoding']==enc),16)
    inv=[0]*q;tr=[]
    for x in range(1,q):
        a=x;b=q-2;z=1
        while b:
            if b&1:z=mul(z,a,p,m)
            b>>=1;a=mul(a,a,p,m)
        inv[x]=z
    for x in range(q):
        z=0;a=x
        for _ in range(m):z^=a;a=mul(a,a,p,m)
        assert z in [0,1];tr.append(z)
    columns=[(1<<q)-1,1];labels=['constant','delta0']
    if kind=='three_simple_poles':
        columns.append(2);labels.append('delta1')
        values=[('X',list(range(q))),('inverse_X',inv),('inverse_Xplus1',[inv[x^1] for x in range(q)])]
    else:
        values=[];pos=list(range(q));neg=inv[:]
        for d in range(1,32,2):
            values.extend([(f'X^{d}',pos),(f'inverse_X^{d}',neg)])
            pos=[mul(a,mul(x,x,p,m),p,m) for x,a in enumerate(pos)]
            neg=[mul(a,mul(inv[x],inv[x],p,m),p,m) for x,a in enumerate(neg)]
    for label,vals in values:
        for j in range(m):
            columns.append(sum(tr[mul(v,1<<j,p,m)]<<x for x,v in enumerate(vals)))
            labels.append(f'{label}_bit{j}')
    basis={}
    for j,v in enumerate(columns):
        mask=1<<j
        while v:
            i=v.bit_length()-1
            if i not in basis:basis[i]=(v,mask);break
            old,w=basis[i];v^=old;mask^=w
    def reduce(v):
        mask=0
        for i in sorted(basis,reverse=True):
            if v>>i&1:
                old,w=basis[i];v^=old;mask^=w
        return v,mask
    residue,witness=reduce(target)
    result=dict(m=m,N=N,encoding=enc,kind=kind,field_polynomial=hex(p),space_rank=len(basis))
    if kind=='three_simple_poles':
        assert residue==0
        chosen=[labels[j] for j in range(len(labels)) if witness>>j&1]
        coefficients={name:sum(1<<j for j in range(m) if f'{name}_bit{j}' in chosen) for name in ['X','inverse_X','inverse_Xplus1']}
        assert all(coefficients.values())
        S=q-2*target.bit_count();pole_signs=[1-2*((target>>x)&1) for x in [0,1]]
        curve_points=q+1+S-sum(pole_signs)
        constant=next(i for i,t in enumerate(tr) if t) if 'constant' in chosen else 0
        direct_points=3
        for x in range(2,q):
            rhs=constant^mul(coefficients['X'],x,p,m)^mul(coefficients['inverse_X'],inv[x],p,m)^mul(coefficients['inverse_Xplus1'],inv[x^1],p,m)
            direct_points+=sum((mul(y,y,p,m)^y)==rhs for y in range(q))
        assert direct_points==curve_points
        result.update(witness=chosen,field_coefficients=coefficients,S=S,pole_signs=pole_signs,genus=2,
                      constant_field_element=constant,curve_points=curve_points,direct_curve_points=direct_points,
                      frobenius_trace=q+1-curve_points)
    else:
        assert residue
        bit=(residue&-residue).bit_length()-1
        dual=sum(((reduce(1<<j)[0]>>bit)&1)<<j for j in range(q))
        assert all((dual&v).bit_count()%2==0 for v in columns)
        assert (dual&target).bit_count()%2==1
        result.update(dual_hex=hex(dual),target_hex=hex(target),annihilated_columns=len(columns),target_pairing=1)
    results.append(result)
out=dict(results=results,runtime_seconds=time.monotonic()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
(folder/'CERTIFICATES_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
