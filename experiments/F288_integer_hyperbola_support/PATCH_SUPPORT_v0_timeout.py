"""Exact ABCS NEXT/SEEK adapters and a dyadic union-support pilot.

F288 continuation. One process, 55-second alarm, estimated <128 MB.
ABCS arXiv:2501.19193 Algorithm 2, Lemma 3.9 and Theorem 3.14.
No hidden factors choose queries. All arithmetic is integral.
"""
import heapq
import json
import math
import signal
import time

signal.alarm(55)
started=time.monotonic()
counts=dict(raycasts=0,next_calls=0,seek_calls=0,support_calls=0)

def inside(N,p):
    return p[0]>0 and p[1]>0 and p[0]*p[1]>=N

def raycast(N,p,v):
    counts['raycasts']+=1
    A=v[0]*v[1]
    B=p[0]*v[1]+p[1]*v[0]
    C=p[0]*p[1]-N
    if A<0:
        A,B,C=-A,-B,-C
    if not A:
        roots=[(-C)//B] if B else []
    else:
        D=B*B-4*A*C
        if D<0:
            roots=[]
        else:
            r=math.isqrt(D)
            roots=[(-B+r)//(2*A),(-B-r-(r*r!=D))//(2*A)]
    for j in sorted({z for r in roots for z in (r,r+1) if z>=0}):
        p0=(p[0]+j*v[0],p[1]+j*v[1])
        p1=(p0[0]+v[0],p0[1]+v[1])
        if inside(N,p0)!=inside(N,p1):
            return j
    return None

def nextpt(N,s,d,m,p):
    counts['next_calls']+=1
    M=s*m
    if inside(N,(p[0],p[1]-M)):
        j=raycast(N,p,(0,-M))
        return (p[0],p[1]-j*M)
    if p[1]<=s:
        return None
    if p[1]<2*s:
        # Lemma 3.9's translated last-row exception.
        y=p[1]-s
        j=(-pow(d,-1,m))%m if m>1 else 0
        x=p[0]+s*j
        k=max(0,(N-x*y+M*y-1)//(M*y))
        return (x+k*M,y)
    inn=(s,s*d)
    out=(0,-M)
    while True:
        o=raycast(N,(p[0]+inn[0],p[1]+inn[1]),out)
        assert o is not None
        inn=(inn[0]+o*out[0],inn[1]+o*out[1])
        i=raycast(N,(p[0]+out[0],p[1]+out[1]),inn)
        if i is None:
            break
        out=(out[0]+i*inn[0],out[1]+i*inn[1])
    j=raycast(N,p,inn)
    return None if j is None else (p[0]+j*inn[0],p[1]+j*inn[1])

def seek(N,s,d,m,origin,t):
    counts['seek_calls']+=1
    M=s*m
    # The last vertex is the first point in the bottom positive lattice row.
    ymin=(origin[1]-1)%s+1
    inv=pow(d,-1,m) if m>1 else 0
    j=((ymin-origin[1])//s*inv)%m if m>1 else 0
    xmax=origin[0]+s*j
    xmax+=M*((N-xmax*ymin+M*ymin-1)//(M*ymin))
    if t>xmax:
        return None
    x=origin[0]+s*((max(1,t)-origin[0]+s-1)//s)
    j=(x-origin[0])//s
    y=(origin[1]+s*d*j-1)%M+1
    y+=M*((N-x*y+M*x-1)//(M*x))
    p=(x,y)
    for _ in range((N+M).bit_length()+2):
        q=nextpt(N,s,d,m,p)
        if q is None:
            break
        p=q
    # We now have a true vertex. Reverse to the first vertex at x>=t.
    while True:
        q=nextpt(N,s,inv,m,(p[1],p[0]))
        if q is None or q[1]<t:
            return p
        p=(q[1],q[0])

def support(N,s,d,m,origin,a,b):
    counts['support_calls']+=1
    lo,hi=1,N+s*m
    best=None
    while lo<=hi:
        t=(lo+hi)//2
        p=seek(N,s,d,m,origin,t)
        if p is None:
            hi=t-1
            continue
        if best is None or (a*p[0]+b*p[1],p[0]*p[1],p)<(a*best[0]+b*best[1],best[0]*best[1],best):
            best=p
        q=nextpt(N,s,d,m,p)
        sign=1 if q is None else a*(q[0]-p[0])+b*(q[1]-p[1])
        if sign==0:
            return min((p,q),key=lambda z:(z[0]*z[1],z))
        if sign>0:
            hi=t-1
        else:
            lo=p[0]+1
    return best

def patch(N,k,r,u):
    s=1<<r
    M=1<<min(k,2*r+1)
    v=N*pow(u,-1,M)%M
    delta=N*(pow(u+s,-1,M)-pow(u,-1,M))%M
    assert delta%s==0
    return (s,delta//s,M//s,(u,v))

rows=[]
# Small exact validation across all leaf patches, including translated end rows.
for N,k in ((10541,4),(147053,6)):
    h=max(1,k//2)
    M=1<<k
    for u in range(1,1<<h,2):
        s,d,m,origin=patch(N,k,h,u)
        for a,b in ((1,1),(2,1),(465,317)):
            p=support(N,s,d,m,origin,a,b)
            brute=None
            for x in range(u,N+M+1,s):
                y=(origin[1]+s*d*((x-u)//s)-1)%M+1
                y+=M*((N-x*y+M*x-1)//(M*x))
                point=(x,y)
                if brute is None or (a*x+b*y,x*y,point)<(a*brute[0]+b*brute[1],brute[0]*brute[1],brute):
                    brute=point
            assert p==brute,(N,k,u,a,b,p,brute)
            rows.append(dict(N=N,k=k,u=u,normal=[a,b],optimizer=p,defect=p[0]*p[1]-N))

# Hierarchical integer-lattice lower bounds, compared to all leaf supports.
hierarchy=[]
for N,k,a,b in ((147053,8,465,317),(147053,12,1,1),(147053,12,3,2)):
    h=max(1,k//2)
    M=1<<k
    leaves=[]
    for u in range(1,1<<h,2):
        leaves.append(support(N,*patch(N,k,h,u),a,b))
    exact=min(leaves,key=lambda z:(a*z[0]+b*z[1],z[0]*z[1],z))
    p=support(N,*patch(N,k,1,1),a,b)
    queue=[(a*p[0]+b*p[1],1,1,p)]
    best=None
    visited=1
    accepted=pruned=0
    while queue:
        lower,r,u,p=heapq.heappop(queue)
        if best is not None and lower>a*best[0]+b*best[1]:
            pruned+=1
            continue
        if p[0]*p[1]%M==N%M:
            accepted+=1
            if best is None or (lower,p[0]*p[1],p)<(a*best[0]+b*best[1],best[0]*best[1],best):
                best=p
            # This certifies support cost; global product tie optimum need not
            # be covered when other points on this coarse face are excluded.
            continue
        assert r<h
        for child in (u,u+(1<<r)):
            q=support(N,*patch(N,k,r+1,child),a,b)
            heapq.heappush(queue,(a*q[0]+b*q[1],r+1,child,q))
            visited+=1
    assert a*best[0]+b*best[1]==a*exact[0]+b*exact[1]
    hierarchy.append(dict(N=N,k=k,normal=[a,b],leaf_count=len(leaves),
        hierarchical_calls=visited,accepted=accepted,pruned=pruned,
        optimizer=best,exhaustive_optimizer=exact,defect=best[0]*best[1]-N))
print(json.dumps(dict(elapsed_seconds=time.monotonic()-started,counts=counts,
    exact_patch_checks=rows,hierarchy=hierarchy),indent=2))
