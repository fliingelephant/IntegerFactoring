"""F291 exact common-direction/phase reuse discriminator.

One process, 25-second alarm, estimated <128 MB. Reuses retained seeded
random and late-DFS inputs. Factors never select directions or patch actions.
"""
import collections
import importlib.util
import json
import math
from pathlib import Path
import signal
import time

signal.alarm(25)
started=time.monotonic()
base=Path(__file__).resolve().parents[1]/'F288_integer_hyperbola_support'
spec=importlib.util.spec_from_file_location('cap_lines',base/'CAP_LINES.py')
cap=importlib.util.module_from_spec(spec)
spec.loader.exec_module(cap)
random_inputs=json.loads((base/'CAP_LINES_RANDOM_output.json').read_text())['inputs']
late_inputs=json.loads((base/'CAP_LINES_LATE_output.json').read_text())['inputs']
chosen=[dict(z) for z in random_inputs if z['e'] in (16,20,24,28) and z['family']=='random_1']
chosen += [dict(z,family='late_dfs') for z in late_inputs if z['e'] in (16,20,24,28)]
rows=[]
for label in chosen:
    N=label['N']
    k=(N//8).bit_length()-1
    r=max(2,N.bit_length()//3-3)
    s=1<<r
    Q=2*s*s
    assert Q<=1<<k
    for a,b in ((1,1),(2,1)):
        U=math.isqrt(17*a*b*N//4)
        zlo=math.isqrt(4*a*b*N)
        zlo+=zlo*zlo<4*a*b*N
        W=math.isqrt(U*U-4*a*b*N)
        directions=collections.Counter()
        certificates=collections.Counter()
        stride_hist=collections.Counter()
        max_directions=set()
        lines=set() if N.bit_length()<=42 else None
        raw_lines=0
        max_stride=0
        examples=[]
        for u in range(1,s,2):
            ss,QQ,v,delta,A1,A2,C0,D,lo,hi=cap.cap_lines(N,k,r,u,a,b,U,zlo,W)
            assert ss==s and QQ==Q
            g=math.gcd(A1,A2)
            A,B=A1//g,A2//g
            sign=-1 if A<0 or (A==0 and B<0) else 1
            A,B=sign*A,sign*B
            stride=math.gcd(A*s+B*delta,B*Q)
            assert stride==D//g
            d=delta//s
            assert stride==s*math.gcd(A+B*d,2*s)
            phase=(A*u+B*v)%stride
            maximum=(A*(u*u+s)-B*N)%(2*s)==0
            assert maximum==(stride==Q)
            if maximum:
                assert A%2 and B%2
                assert (phase*phase-4*A*B*N-s*s)%Q==0
                other=s-u
                other_v=N*pow(other,-1,Q)%Q
                assert (A*other+B*other_v+phase)%Q==0
                max_stride+=1
                max_directions.add((A,B))
            directions[A,B]+=1
            certificates[A,B,stride,phase]+=1
            stride_hist[stride//s]+=1
            raw_lines+=max(0,hi-lo+1)
            if lines is not None:
                for j in range(lo,hi+1):
                    assert (C0+D*j)%g==0
                    lines.add((A,B,sign*(C0+D*j)//g))
            if len(examples)<6:
                examples.append(dict(u=u,direction=[A,B],stride=stride,phase=phase,
                                     max_stride=maximum,line_count=max(0,hi-lo+1)))
        rows.append(dict(N=N,e=label['e'],family=label['family'],normal=[a,b],r=r,s=s,
            classes=s//2,distinct_directions=len(directions),
            distinct_direction_stride_phase=len(certificates),
            direction_reuse_hist=dict(collections.Counter(directions.values())),
            certificate_reuse_hist=dict(collections.Counter(certificates.values())),
            stride_multiplier_hist=dict(stride_hist),max_stride_classes=max_stride,
            max_stride_directions=len(max_directions),
            raw_line_equations=raw_lines,
            unique_line_equations=None if lines is None else len(lines),examples=examples))
print(json.dumps(dict(elapsed_seconds=time.monotonic()-started,
    input_provenance='F288 seeds202609070213 and202609070214; inputs retained below',
    inputs=chosen,rows=rows),indent=2))
