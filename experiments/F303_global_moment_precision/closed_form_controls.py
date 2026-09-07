"""Sparse exact controls for the root's closed M² formulas.

20sec alarm, <64MiB estimate. Direct products here are small verification
data, not a replacement for UNIT_PRODUCTS.md's polynomial-size algorithm.
"""
import json
import resource
import signal
import time
from pathlib import Path

signal.alarm(20)
started=time.monotonic()
inputs=[(8,3,0,0),(8,3,9,9),(16,1,1,1),(16,3,2,2),(32,7,3,3),
        (16,3,4,2),(16,5,6,2),(32,3,9,1),(32,5,17,1),
        (64,19,7,3),(128,45,6,5),(32,3,3,0)]
rows=[]
for M,N,a,b in inputs:
    k=M.bit_length()-1
    target=M*M
    units=list(range(1,M,2))
    actual=sum(u**a*(N*pow(u,-1,M)%M)**b for u in units)%target
    if a==b:
        product=1
        for u in units:
            product=product*u%target
        predicted=((M//2-a)*pow(N,a,target)+a*product*product*pow(N,a-M//2,target))%target
        guard=0
        unguarded=None
    else:
        j=a-b
        guard=(j&-j).bit_length()-1
        work=target<<guard
        positive=sum(u**j for u in units)%work
        negative=sum(pow(u,-j,work) for u in units)%work
        numerator=(a*pow(N,b,work)*positive-b*pow(N,a,work)*negative)%work
        assert numerator%(1<<guard)==0
        predicted=(numerator>>guard)*pow(j>>guard,-1,target)%target
        short=numerator%target
        unguarded=(short>>guard)*pow(j>>guard,-1,target)%target
        # Check the stronger first-order relation with its full guard.
        weighted=sum(u**j*((u*(N*pow(u,-1,M)%M)-N)//M) for u in units)
        lhs=(positive-pow(N,j,work)*negative)%work
        assert lhs==(j*M*pow(N,-1,work)*weighted)%work
    assert predicted==actual
    rows.append(dict(M=M,N=N,a=a,b=b,guard_bits=guard,actual_mod_M2=actual,
                     closed_mod_M2=predicted,without_guard_result=unguarded))
out=dict(packet='F303',status='exact_sparse_closed_formula_controls',checks=len(rows),
         runtime_seconds=time.monotonic()-started,
         max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
