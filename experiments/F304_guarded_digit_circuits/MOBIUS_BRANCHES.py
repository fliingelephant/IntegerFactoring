"""Exact distinct-map controls for the quotient-state family."""
import json, random, resource, signal, time
from pathlib import Path
signal.alarm(30); start=time.monotonic(); rng=random.Random(304022)
rows=[]
for k in range(7,20):
    M=1<<k; N=rng.randrange(8*M,16*M)|1
    for r in range(1,(k-1)//3+1):
        R=1<<r; L=M//R; signatures=set(); recovered=[]
        for u0 in range(1,R,2):
            v0=N*pow(u0,-1,R)%R; n=(N-u0*v0)//R
            values=tuple((n-v0*x)*pow(u0+R*x,-1,L)%L for x in [0,1,2])
            d0=(values[1]-values[0])%L; d1=(values[2]-values[1])%L
            ratio=d0*pow(d1,-1,L)%L
            assert (ratio-1)%(2*R)==0
            inverse=(ratio-1)//(2*R)
            assert pow(inverse,-1,R)==u0
            signatures.add(values); recovered.append(u0)
        assert len(signatures)==R//2
        rows.append(dict(k=k,N=N,r=r,states=R//2,distinct_three_value_signatures=len(signatures)))
result=dict(rows=rows,runtime_seconds=time.monotonic()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            scope='Distinct literal quotient maps; no lower bound against aggregation of their sum.')
Path(__file__).with_name('MOBIUS_BRANCHES_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(cases=len(rows),maximum_states=max(r['states'] for r in rows),runtime_seconds=result['runtime_seconds'],peak_rss_bytes=result['peak_rss_bytes']),indent=2))
