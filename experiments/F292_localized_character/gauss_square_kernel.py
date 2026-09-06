"""Exact F292 phase-sensitive Gauss-square kernel check; 30sec/64MiB."""
import json
import signal
import time
from pathlib import Path

signal.alarm(30)
started=time.monotonic()
cases=[]
for k in range(4,8):
    M=1<<k
    P=M//4
    logs={}
    u=1
    for j in range(P):
        logs[u]=(1,j)
        logs[-u%M]=(-1,j)
        u=5*u%M
    squares=[]
    for a in range(1,P,2):
        tau=[0]*M
        for u,(sign,j) in logs.items():
            tau[(u+4*a*j)%M]+=sign
        nonzero=[(i,v) for i,v in enumerate(tau) if v]
        square=[0]*M
        for i,v in nonzero:
            for j,w in nonzero:
                square[(i+j)%M]+=v*w
        squares.append((a,square))
    for z in (1,3,5,7,M-1):
        sign,index=logs[z]
        lhs=[0]*M
        for a,square in squares:
            for j,v in enumerate(square):
                lhs[(j-4*a*index)%M]+=sign*v
        rhs=[0]*M
        for u in range(1,M,2):
            inv=pow(u,-1,M)
            rhs[(u+z*inv)%M]+=M//4
            rhs[(u-z*inv)%M]-=M//4
        assert [lhs[i]-lhs[i+M//2] for i in range(M//2)] == [rhs[i]-rhs[i+M//2] for i in range(M//2)]
        cases.append(dict(k=k,M=M,z=z,primitive_odd_characters=len(squares)))
out=dict(packet='F292',route='F31',exact_kernel_checks=len(cases),
         runtime_seconds=time.monotonic()-started,cases=cases)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
