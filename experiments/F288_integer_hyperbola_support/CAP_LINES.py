"""F288 grouped cap certificates using exact lattice lines.

Resource budget: one process, 25 seconds, estimated <128 MB.
No factors guide normals, node order, directions, or quadratic tests.
"""
import json
import math
import signal
import sys
import time

def cap_lines(N,k,r,u,a,b,U,zlo,W):
    s=1<<r
    Q=1<<min(k,2*r+1)
    v=N*pow(u,-1,Q)%Q
    delta=N*(pow(u+s,-1,Q)-pow(u,-1,Q))%Q
    T=U-zlo
    if T==0:
        return s,Q,v,delta,a,b,zlo,1,0,0
    if W==0:
        return s,Q,v,delta,a,-b,0,1,0,0
    C1=(T*b*Q,2*W*b*Q)
    C2=(T*(-b*delta+a*s),2*W*(-b*delta-a*s))
    e1,e2=(1,0),(0,1)
    while True:
        n1=C1[0]**2+C1[1]**2
        n2=C2[0]**2+C2[1]**2
        if n2<n1:
            C1,C2,e1,e2=C2,C1,e2,e1
            n1=n2
        dot=C1[0]*C2[0]+C1[1]*C2[1]
        mu=(2*dot+n1)//(2*n1)
        if mu==0:
            break
        C2=(C2[0]-mu*C1[0],C2[1]-mu*C1[1])
        e2=(e2[0]-mu*e1[0],e2[1]-mu*e1[1])
    A1=Q*e1[0]-delta*e1[1]
    A2=s*e1[1]
    D=s*Q
    Az=b*A1+a*A2
    Aw=b*A1-a*A2
    phase=(A1*u+A2*v)*2*a*b
    denom=2*a*b*D
    low=min(Az*zlo,Az*U)-abs(Aw)*W-phase
    high=max(Az*zlo,Az*U)+abs(Aw)*W-phase
    lo=-(-low//denom)
    hi=high//denom
    return s,Q,v,delta,A1,A2,A1*u+A2*v,D,lo,hi

def query(N,k,a,b,line_cap=8,node_cap=100000):
    U=math.isqrt(17*a*b*N//4)
    zlo=math.isqrt(4*a*b*N)
    zlo+=zlo*zlo<4*a*b*N
    if U<zlo:
        return dict(status='empty',nodes=0,U=U)
    W=math.isqrt(U*U-4*a*b*N)
    h=max(1,k//2)
    stack=[(1,1)]
    nodes=lines=terminal=0
    depths={}
    start=time.monotonic()
    while stack:
        if nodes>=node_cap:
            return dict(status='budget_exhausted',nodes=nodes,lines=lines,depths=depths,U=U)
        r,u=stack.pop()
        nodes+=1
        depths[r]=depths.get(r,0)+1
        s,Q,v,delta,A1,A2,C0,D,lo,hi=cap_lines(N,k,r,u,a,b,U,zlo,W)
        if hi-lo+1>line_cap and r<h:
            stack.extend(((r+1,u+s),(r+1,u)))
            continue
        terminal+=1
        for j in range(lo,hi+1):
            lines+=1
            C=C0+D*j
            candidates=[]
            if A1==0:
                if C%A2==0:
                    y=C//A2
                    if y>0 and N%y==0:
                        candidates.append((N//y,y))
            else:
                disc=C*C-4*A1*A2*N
                if disc>=0:
                    sd=math.isqrt(disc)
                    if sd*sd==disc:
                        for numerator in (C-sd,C+sd):
                            if numerator%(2*A1)==0:
                                x=numerator//(2*A1)
                                if x>0 and N%x==0:
                                    candidates.append((x,N//x))
            for x,y in candidates:
                if (1<x<N and a*x+b*y<=U and (x-u)%s==0
                    and (y-v-delta*((x-u)//s))%Q==0):
                    return dict(status='factor',point=[x,y],nodes=nodes,lines=lines,
                        terminal=terminal,depths=depths,U=U,seconds=time.monotonic()-start)
    return dict(status='empty',nodes=nodes,lines=lines,terminal=terminal,depths=depths,
        U=U,seconds=time.monotonic()-start)

if __name__=='__main__':
    signal.alarm(25)
    started=time.monotonic()
    rows=[]
    for N,p,q in ((147053,307,479),(8464705853,73771,114743),
                  (2164905613373,1179733,1835081)):
        k=(N//8).bit_length()-1
        for a,b in ((1,1),(2,1),(4,3)):
            result=query(N,k,a,b)
            # Offline labels audit conclusions only, after the public query.
            assert N==p*q
            assert all(all(z%d for d in range(2,math.isqrt(z)+1)) for z in (p,q))
            if result['status']=='empty':
                assert min(a*p+b*q,a*q+b*p)>result['U']
            if result['status']=='factor':
                x,y=result['point']
                assert x*y==N and 1<x<N
            rows.append(dict(N=N,k=k,normal=[a,b],**result))
            print(N,k,a,b,result['status'],result['nodes'],file=sys.stderr,flush=True)
    print(json.dumps(dict(elapsed_seconds=time.monotonic()-started,line_cap=8,rows=rows),indent=2))
