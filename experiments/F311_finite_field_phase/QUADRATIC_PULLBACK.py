"""Nonlinear finite-field inverse pullbacks and exact quadratic summation."""
import json, resource, signal, time
from pathlib import Path
signal.alarm(30); start=time.monotonic(); folder=Path(__file__).resolve().parent
prior=json.loads((folder/'output.json').read_text())

def mul(a,b,p,m):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a>>m:a^=p
    return z

def quadratic_total(anf,m):
    terms={j for j,v in enumerate(anf) if v}; factor=1; remaining=m
    while True:
        edge=next((t for t in terms if t.bit_count()==2),None)
        if edge is None:
            if any(terms-{0}):return 0
            return factor*(1<<remaining)*(-1 if 0 in terms else 1)
        i=edge&-edge;j=edge^i
        left=[t^i for t in terms if t&i and not t&j]
        right=[t^j for t in terms if t&j and not t&i]
        terms={t for t in terms if not t&edge}
        for a in left:
            for b in right:
                t=a|b
                if t in terms:terms.remove(t)
                else:terms.add(t)
        factor*=2;remaining-=2

rows=[];summary=[]
for field in prior['fields']:
    m=field['m'];q=1<<m;p=int(field['polynomial'],16);inverse=[0]*q
    for x in range(1,q):
        z=1;a=x;b=q-2
        while b:
            if b&1:z=mul(z,a,p,m)
            a=mul(a,a,p,m);b>>=1
        inverse[x]=z
    cases=[x for x in prior['rows'] if x['m']==m]
    for row in cases:
        table=int(row['truth_hex'],16)
        # Two cheap explicit bijections, plus all centers on a bounded subset.
        centers=range(q) if m<=6 and row['N']%(4*q) in [1,3,5,7] else [0,1]
        best=m;bestcenter=None;quad=None;visited=[]
        for center in centers:
            visited.append(center)
            bits=[(table>>(inverse[x]^center))&1 for x in range(q)]
            anf=bits[:];h=1
            while h<q:
                for a in range(0,q,2*h):
                    for j in range(h):anf[a+j+h]^=anf[a+j]
                h*=2
            degree=max((j.bit_count() for j,v in enumerate(anf) if v),default=0)
            if degree<best:best=degree;bestcenter=center
            if degree<=2:
                quad=quadratic_total(anf,m)
                assert quad==row['S']
                break
        absolute=abs(row['S'])
        quadratic_weight_allowed=not absolute or (absolute&(absolute-1)==0 and 2*(absolute.bit_length()-1)>=m)
        assert quad is None or quadratic_weight_allowed
        rows.append(dict(m=m,N=row['N'],encoding=row['encoding'],S=row['S'],
                         centers_tested=visited,minimum_degree=best,best_center=bestcenter,
                         quadratic_total=quad,quadratic_weight_allowed=quadratic_weight_allowed))
    local=[x for x in rows if x['m']==m]
    summary.append(dict(m=m,encodings={enc:dict(cases=sum(x['encoding']==enc for x in local),
                        quadratic_matches=sum(x['encoding']==enc and x['quadratic_total'] is not None for x in local),
                        quadratic_weight_possible=sum(x['encoding']==enc and x['quadratic_weight_allowed'] for x in local),
                        minimum_degree=min(x['minimum_degree'] for x in local if x['encoding']==enc))
                        for enc in ['ordinary','sign_log']}))
result=dict(rows=rows,summary=summary,runtime_seconds=time.monotonic()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            scope='Explicit nonlinear coordinate tests and a polynomial quadratic-sum evaluator when a fit exists. No uniform pullback constructor.')
(folder/'QUADRATIC_PULLBACK_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['summary','runtime_seconds','peak_rss_bytes']},indent=2))
