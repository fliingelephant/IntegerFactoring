"""Exact canonical carry composition and self-composition controls."""
import json, random, resource, signal, time
from pathlib import Path
signal.alarm(30); start=time.monotonic(); rng=random.Random(307032)

def choose2(x):return x*(x-1)//2

def compose(g,f):
    e,b,h,i=g; a,v,c,d=f
    return e*a+b*c,e*v+b*d,h*a+i*c,h*v+i*d

def apply(f,x,L):
    a,b,c,d=f; y=(a*x+b)*pow(c*x+d,-1,L)%L
    return y,((c*x+d)*y-(a*x+b))//L

rows=[]; checks=0
for s in range(3,10):
    L=1<<s
    maps=[('h2_h2',(1,0,2,1),(1,0,2,1)),
          ('h2_h4',(1,0,2,1),(1,0,4,1)),
          ('high_self',(1,0,L//2,1),(1,0,L//2,1))]
    # Exact first-quotient map of an original N, built by composition.
    N=(rng.randrange(16*L,32*L)|1); n=(N-1)//2
    maps += [('original_scaling',(1,0,2,1),(-N,0,0,1)),
             ('original_translation',(-N,0,2,1),(1,n,0,1))]
    for label,f,g in maps:
        gf=compose(g,f); a,b,c,d=f; e,bg,h,i=g
        totals=[0]*8; triple=0; pair=0
        for x in range(L):
            y,qf=apply(f,x,L); z,qg=apply(g,y,L); zz,qc=apply(gf,x,L)
            A=c*x+d; B=e-h*z
            assert zz==z and qc==A*qg+B*qf
            pieces=[A*A*choose2(qg),B*B*choose2(qf),A*B*qf*qg,
                    choose2(A)*qg,choose2(B)*qf]
            assert sum(pieces)==choose2(qc)
            for j,v in enumerate(pieces):totals[j]+=v
            totals[5]+=choose2(qc); totals[6]+=choose2(qf); totals[7]+=choose2(qg)
            if label in ['h2_h2','high_self']:
                assert (2*x*z-x*y-y*z)%L==0
                assert qc==qf+qg+c*((2*x*z-x*y-y*z)//L)
            triple+=x*y*z
            pair+=2*x*z-x*y-y*z
            checks+=2
        cross=totals[2]%L
        rows.append(dict(s=s,L=L,N=N,label=label,f=f,g=g,composite=gf,
                         binomial_terms_modL=[t%L for t in totals[:5]],Bcomposite=totals[5]%L,
                         Bf=totals[6]%L,Bg=totals[7]%L,
                         crosscarry_modL=cross,crosscarry_v2=(cross&-cross).bit_length()-1 if cross else s,
                         triple_xyz_modL2=triple%(L*L),pair_skew_exact=pair,
                         omission_changes_answer=bool(cross)))

result=dict(rows=rows,exact_point_checks=checks,runtime_seconds=time.monotonic()-start,
            peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            scope='Exact composition controls; no closure of cross-carry trace asserted.')
Path(__file__).with_name('COMPOSITION_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(cases=len(rows),exact_point_checks=checks,runtime_seconds=result['runtime_seconds'],
                     peak_rss_bytes=result['peak_rss_bytes'],self_rows=[r for r in rows if r['label']=='h2_h2']),indent=2))
