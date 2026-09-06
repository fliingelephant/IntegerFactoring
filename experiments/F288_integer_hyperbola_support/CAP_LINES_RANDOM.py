"""Seeded low-bit-bias audit, with full cap-tree completion after detection.

F288; one process, hard28s, soft1.5s/300000nodes per query, <128 MB.
Labels construct inputs and audit outputs only. All searches use N alone.
"""
import json
import math
import random
import signal
import sys
import time
import CAP_LINES as cap
import PATCH_SUPPORT as oracle

SEED=202609070213

def isprime(z):
    return z>=2 and all(z%d for d in range(2,math.isqrt(z)+1))

def make_prime(rng,low,high,stress_bits=0):
    while True:
        z=rng.randrange(low,high)|1
        if stress_bits:
            s=1<<stress_bits
            z=(z//s)*s+(rng.randrange(3*s//4,s)|1)
        while z<high and not isprime(z):
            z+=2
        if z<high and (not stress_bits or z%(1<<stress_bits)>=3*(1<<stress_bits)//4):
            return z

def line_points(N,A1,A2,C):
    points=set()
    if A1==0:
        if C%A2==0:
            y=C//A2
            if y>0 and N%y==0:
                points.add((N//y,y))
    else:
        D=C*C-4*A1*A2*N
        if D>=0:
            sd=math.isqrt(D)
            if sd*sd==D:
                for top in (C-sd,C+sd):
                    if top%(2*A1)==0:
                        x=top//(2*A1)
                        if x>0 and N%x==0:
                            points.add((x,N//x))
    return points

def run(N,a,b,use_oracle=False):
    k=(N//8).bit_length()-1
    h=max(1,k//2)
    U=math.isqrt(17*a*b*N//4)
    zlo=math.isqrt(4*a*b*N)
    zlo+=zlo*zlo<4*a*b*N
    W=math.isqrt(U*U-4*a*b*N)
    stack=[(1,1)]
    nodes=lines=terminal=max_cover=max_terminal=0
    factors=set()
    first=None
    depths={}
    start=time.monotonic()
    initial_counts=oracle.counts.copy()
    while stack:
        if nodes>=300000 or (nodes%64==0 and time.monotonic()-start>=1.5):
            break
        r,u=stack.pop()
        nodes+=1
        depths[r]=depths.get(r,0)+1
        found=set()
        if use_oracle:
            p=oracle.support(N,*oracle.patch(N,k,r,u),a,b)
            if a*p[0]+b*p[1]>U:
                terminal+=1
                continue
            if p[0]*p[1]==N:
                found.add(p)
            if r<h:
                # Continue to leaves after a discovery for full-completion
                # work; a valid coarse optimizer alone is not an empty-cap proof.
                stack.extend(((r+1,u+(1<<r)),(r+1,u)))
            else:
                terminal+=1
        else:
            s,Q,v,delta,A1,A2,C0,D,lo,hi=cap.cap_lines(N,k,r,u,a,b,U,zlo,W)
            cover=max(0,hi-lo+1)
            max_cover=max(max_cover,cover)
            if cover>8 and r<h:
                stack.extend(((r+1,u+s),(r+1,u)))
                continue
            terminal+=1
            max_terminal=max(max_terminal,cover)
            for j in range(lo,hi+1):
                lines+=1
                for x,y in line_points(N,A1,A2,C0+D*j):
                    if (1<x<N and a*x+b*y<=U and (x-u)%s==0
                        and (y-v-delta*((x-u)//s))%Q==0):
                        found.add((x,y))
        if found and first is None:
            first=dict(nodes=nodes,lines=lines,seconds=time.monotonic()-start,
                       point=list(min(found)))
        factors.update(found)
    return dict(N=N,k=k,normal=[a,b],U=U,method='oracle' if use_oracle else 'lines',
        status='complete' if not stack else 'budget_exhausted',nodes=nodes,lines=lines,
        terminal=terminal,max_integer_line_cover=max_cover,max_terminal_lines=max_terminal,
        first_detection=first,factors=sorted(factors),depths=depths,
        seconds=time.monotonic()-start,
        oracle_counts={key:oracle.counts[key]-initial_counts[key] for key in initial_counts})

if __name__=='__main__':
    signal.alarm(28)
    started=time.monotonic()
    rng=random.Random(SEED)
    rows=[]
    inputs=[]
    for e in (12,16,20,24,28):
        B=1<<e
        for family in ('random_1','random_2','high_residue'):
            r=max(2,2*e//3-3)
            stress=r if family=='high_residue' else 0
            p=make_prime(rng,9*B//8,11*B//8,stress)
            q=make_prime(rng,3*B//2,15*B//8,stress)
            N=p*q
            label=dict(e=e,family=family,N=N,p=p,q=q,residue_bits=r,
                p_residue=p%(1<<r),q_residue=q%(1<<r))
            inputs.append(label)
            for a,b in ((1,1),(2,1)):
                result=run(N,a,b)
                expected=sorted((x,y) for x,y in ((p,q),(q,p)) if a*x+b*y<=result['U'])
                if result['status']=='complete':
                    assert result['factors']==expected,(label,result,expected)
                assert all(x*y==N and 1<x<N for x,y in result['factors'])
                rows.append(dict(e=e,family=family,**result))
                print(e,family,a,b,result['status'],result['nodes'],result['lines'],file=sys.stderr,flush=True)
                if e==12:
                    baseline=run(N,a,b,True)
                    if baseline['status']=='complete':
                        assert baseline['factors']==expected
                    rows.append(dict(e=e,family=family,**baseline))
    print(json.dumps(dict(seed=SEED,elapsed_seconds=time.monotonic()-started,
        resource=dict(hard_seconds=28,soft_query_seconds=1.5,node_cap=300000),
        inputs=inputs,rows=rows),indent=2))
