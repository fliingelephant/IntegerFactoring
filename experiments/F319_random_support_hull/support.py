"""F319 / route:F31. Exact unboxed SUPPORT using ABCS Algorithm 2 and SEEK.

No hidden factors. All points/directions are integer pairs. The ray cast is
implemented directly by exact quadratic roots and membership transitions.
"""
from math import isqrt


def raycast(n, p, v):
    x,y = p
    u,w = v
    a,b,c = u*w, x*w+y*u, x*y-n
    if a < 0:
        a,b,c = -a,-b,-c
    roots = []
    if a:
        discriminant = b*b-4*a*c
        if discriminant >= 0:
            root = isqrt(discriminant)
            ceil_root = root + (root*root != discriminant)
            roots = [(-b+root)//(2*a),(-b-ceil_root)//(2*a)]
    elif b:
        roots = [-c//b]
    candidates = sorted({r+j for r in roots for j in (-1,0,1,2) if r+j>=0})
    for k in candidates:
        x0,y0 = x+k*u,y+k*w
        x1,y1 = x0+u,y0+w
        inside0 = x0>0 and y0>0 and x0*y0>=n
        inside1 = x1>0 and y1>0 and x1*y1>=n
        if inside0 != inside1:
            return k
    return None


def nextpt(n, p):
    x,y = p
    bottom = (n+x-1)//x
    if bottom < y:
        return x,bottom
    inside,outside = (1,0),(0,-1)
    while True:
        k = raycast(n,(x+inside[0],y+inside[1]),outside)
        assert k is not None
        inside = inside[0]+k*outside[0],inside[1]+k*outside[1]
        k = raycast(n,(x+outside[0],y+outside[1]),inside)
        if k is None:
            break
        outside = outside[0]+k*inside[0],outside[1]+k*inside[1]
    k = raycast(n,p,inside)
    return None if k is None else (x+k*inside[0],y+k*inside[1])


def seek(n, start):
    p = start,(n+start-1)//start
    for _ in range(n.bit_length()+2):
        q = nextpt(n,p)
        if q is None:
            break
        p = q
    # At least logarithmically many forward calls, or the rightmost vertex.
    # Reverse from this genuine vertex until crossing the coordinate cutoff.
    while True:
        previous = nextpt(n,(p[1],p[0]))
        if previous is None:
            return p
        previous = previous[1],previous[0]
        if previous[0] < start:
            return p
        p = previous


def support(n, a, b):
    low,high = 1,n
    best = (1,n)
    while low <= high:
        middle = (low+high)//2
        v = seek(n,middle)
        if (a*v[0]+b*v[1],v[0]*v[1]) < (a*best[0]+b*best[1],best[0]*best[1]):
            best = v
        w = nextpt(n,v)
        if w is None:
            high = middle-1
            continue
        change = a*(w[0]-v[0])+b*(w[1]-v[1])
        if change == 0:
            return min((v,w),key=lambda z:z[0]*z[1])
        if change < 0:
            low = v[0]+1
        else:
            high = middle-1
    return best
