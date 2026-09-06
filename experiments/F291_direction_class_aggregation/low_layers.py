"""Three global low-stride direction representatives via exact 2D CVP.

F291; one process, 10-second alarm, <64 MB. All checks use public N only.
"""
import json
import math
from pathlib import Path
import signal
import time
from global_dominance import weight2

def representative(N,t,T,W,a,b):
    m=1<<(t+1)
    offset=(1<<t,0)
    w1,w2=(m,0),(N%m,1)
    v1=(T*b*m,2*W*b*m)
    v2=(T*(b*w2[0]+a),2*W*(b*w2[0]-a))
    target=(-T*b*offset[0],-2*W*b*offset[0])
    while True:
        norm=v1[0]**2+v1[1]**2
        if v2[0]**2+v2[1]**2<norm:
            v1,v2,w1,w2=v2,v1,w2,w1
            norm=v1[0]**2+v1[1]**2
        mu=(2*(v1[0]*v2[0]+v1[1]*v2[1])+norm)//(2*norm)
        if not mu:
            break
        v2=(v2[0]-mu*v1[0],v2[1]-mu*v1[1])
        w2=(w2[0]-mu*w1[0],w2[1]-mu*w1[1])
    det=v1[0]*v2[1]-v1[1]*v2[0]
    num=v1[0]*target[1]-v1[1]*target[0]
    floor=num//det
    best=None
    for j in (floor,floor+1):
        residual=(target[0]-j*v2[0],target[1]-j*v2[1])
        i=(2*(residual[0]*v1[0]+residual[1]*v1[1])+norm)//(2*norm)
        A=offset[0]+i*w1[0]+j*w2[0]
        B=i*w1[1]+j*w2[1]
        item=(weight2(T,W,a,b,A,B),A,B)
        if best is None or item<best:
            best=item
    _,A,B=best
    assert (A-N*B)%m==1<<t
    g=math.gcd(A,B)
    assert g&(g-1)==0
    return A//g,B//g,best

if __name__=='__main__':
    signal.alarm(10)
    start=time.monotonic()
    rows=[]
    for label in json.loads(Path(__file__).with_name('output.json').read_text())['inputs']:
        if label['e']!=16:
            continue
        N=label['N']
        for a,b in ((1,1),(2,1)):
            U=math.isqrt(17*a*b*N//4)
            zlo=math.isqrt(4*a*b*N)
            zlo+=zlo*zlo<4*a*b*N
            T=U-zlo
            W=math.isqrt(U*U-4*a*b*N)
            reps=[]
            for t in range(3):
                A,B,raw=representative(N,t,T,W,a,b)
                checks=0
                for x in range(-64,65):
                    for y in range(-64,65):
                        if (x-N*y)%(1<<(t+1))==1<<t:
                            assert raw[0]<=weight2(T,W,a,b,x,y)
                            checks+=1
                reps.append(dict(layer=t,primitive=[A,B],raw_weight2=raw[0],
                    raw_point=list(raw[1:]),finite_checks=checks))
            rows.append(dict(N=N,family=label['family'],normal=[a,b],representatives=reps))
    print(json.dumps(dict(elapsed_seconds=time.monotonic()-start,rows=rows),indent=2))
