"""F322: exact Jerabek Lemma 4.7 involution and canonical path pilot.

Offline factors only label outputs. Public actions use n,a,b and node IDs.
"""
import argparse
import collections
import json
import math
import resource
import random
import signal
import time


class Pairing:
    def __init__(self, n, a, b):
        self.n, self.a, self.b = n, a % n, b % n
        self.h = n // 2
        self.bi = pow(b, -1, n)
        self.counts = collections.Counter()

    def rep(self, x):
        return (x + self.h) % self.n - self.h

    def f(self, a, x):
        if x == 0:
            return 1, 'swap01'
        if x == 1:
            return 0, 'swap01'
        xi = self.rep(pow(x, -1, self.n))
        if x > 0 and xi > 0:
            return xi, 'inverse'
        if self.rep(a*x) < 0 and xi < 0:
            return self.rep(pow(a, -1, self.n)*xi), 'scaled_inverse'
        return -x, 'negate'

    def g(self, x):
        if x >= 0:
            return 0, -x
        return (1 if self.rep(self.bi*x) < 0 else 2), -x

    def hmap(self, x):
        if x > 0:
            return 0, x
        if x == 0 or self.rep(self.a*x) < 0:
            return 1, x
        return 2, x

    def r(self, z):
        e, t = divmod(z, self.n)
        x = t - self.h
        if x != 0 and math.gcd(x, self.n) > 1:
            return z, 'nonunit'
        ax, bx = self.rep(self.a*x), self.rep(self.bi*x)
        if (e == 0 and x <= 0) or (e == 1 and x > 0 and ax > 0 and bx > 0) or (e == 2 and x > 0 and ax > 0 and bx < 0):
            y, branch = self.f(self.a, -x)
            ee, xx = self.g(y)
            branch = 'A:' + branch
        elif (e == 0 and x > 0) or (e == 1 and (x == 0 or x < 0 and ax < 0 and bx < 0)) or (e == 2 and x < 0 and ax > 0 and bx < 0):
            y, branch = self.f(self.bi, x)
            ee, xx = self.hmap(y)
            branch = 'B:' + branch
        elif e == 2 and (x == 0 or ax < 0 or bx > 0):
            y, branch = self.f(self.a*self.b % self.n, bx)
            ee, xx = 2, self.rep(self.b*y)
            branch = 'C:' + branch
        else:
            assert e == 1 and x != 0 and not (x > 0 and ax > 0 and bx > 0) and not (x < 0 and ax < 0 and bx < 0)
            ee, xx, branch = 1, -x, 'D:negate'
        return ee*self.n + xx+self.h, branch

    def decode(self, z):
        e, t = divmod(z, self.n)
        x = t-self.h
        d = math.gcd(x, self.n)
        if 1 < d < self.n:
            return {'factor': d, 'kind': 'nonunit'}
        y = -x if e == 0 and x <= 0 or e == 1 and x > 0 or e == 2 and x > 0 and self.rep(self.a*x) > 0 and self.rep(self.bi*x) < 0 else x
        if e == 2 and (x == 0 or self.rep(self.a*x) < 0 or self.rep(self.bi*x) > 0):
            y = self.rep(self.bi*x)
        for d in (math.gcd(y-1, self.n), math.gcd(y+1, self.n)):
            if 1 < d < self.n:
                return {'factor': d, 'kind': 'root1'}
        yi = pow(y, -1, self.n)
        for name, a in [('a', self.a), ('b', self.b), ('ab', self.a*self.b % self.n)]:
            for root in (yi, y):
                if root*root % self.n == a:
                    return {'root': root, 'radicand': a, 'kind': name}
        raise AssertionError(('bad endpoint', self.n, self.a, self.b, z, e, x, y))


def run(n, a, b, full, matching='adjacent'):
    p = Pairing(n, a, b)
    start_node = 0 if matching == 'adjacent' else 2*n+p.h
    ss = []
    for z in range(3*n):
        e,t = divmod(z,n)
        x=t-p.h
        if matching == 'adjacent':
            ss.append(z if z==0 else z+1 if z%2 else z-1)
        elif x:
            ss.append(e*n-x+p.h)
        else:
            ss.append((1-e)*n+p.h if e<2 else z)
    fixed, components = [], []
    if full:
        rr = [p.r(z)[0] for z in range(3*n)]
        assert all(rr[rr[z]] == z for z in range(3*n))
        fixed = [z for z in range(3*n) if rr[z] == z]
        for z in fixed:
            p.decode(z)
        seen = set()
        for start in range(3*n):
            if start in seen:
                continue
            todo, size, ends = [start], 0, 0
            while todo:
                z = todo.pop()
                if z in seen:
                    continue
                seen.add(z)
                size += 1
                ends += int(rr[z] == z) + int(z == start_node)
                todo.extend([rr[z], ss[z]])
            components.append([size, ends])
    z, steps, trace, branches = start_node, 0, [], []
    while True:
        y, branch = p.r(z)
        steps += 1
        p.counts[branch] += 1
        if len(trace) < 100:
            trace.append([z, y, branch])
        branches.append(branch)
        if y == z:
            result = p.decode(z)
            break
        assert y != start_node
        z = ss[y]
        assert steps <= 3*n
    runs, last = [], None
    for v in branches:
        if v == last:
            runs[-1] += 1
        else:
            runs.append(1)
            last = v
    return dict(n=n,a=a,b=b,matching=matching,steps=steps,result=result,fixed=len(fixed) if full else None,
                components=components if full else None,branches=p.counts,max_same_branch=max(runs),trace=trace)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=101)
    ap.add_argument('--seconds', type=int, default=25)
    ap.add_argument('--output', required=True)
    ap.add_argument('--matching', default='adjacent', choices=['adjacent','negation'])
    args = ap.parse_args()
    signal.alarm(args.seconds)
    started = time.monotonic()
    rows = []
    for n in range(3,args.limit+1,2):
        units = [x for x in range(1,min(n,9)) if math.gcd(x,n)==1]
        for a in units:
            for b in units:
                rows.append(run(n,a,b,True,args.matching))
    out = dict(status='completed',scope='All odd n through limit; a,b units in 1..8',limit=args.limit,rows=rows,
               elapsed_seconds=time.monotonic()-started,max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with open(args.output,'w') as f:
        json.dump(out,f,indent=2)
    print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
    print('instances',len(rows),'max_steps',max(r['steps'] for r in rows))
