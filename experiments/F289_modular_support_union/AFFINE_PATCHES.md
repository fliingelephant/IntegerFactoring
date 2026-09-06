# Affine patches, higher differences, and a sufficient support accuracy

**Family:** route:F31

**Status:** the three claims in `PATCH_STATEMENT_ONLY.md` passed fresh Sol
reconstruction and root review; P235 records that exact scope. The accompanying
certificate checks finite identities, not an optimizer's asymptotic cost.

## Exact cover of the inverse graph

Let N be odd, M=2^k, k>=1, h=max(1,ceil((k-1)/2)), and s=2^h.
For each odd u0 in [1,s), put

    v0 = N/u0 mod M,
    delta = N ((u0+s)^(-1) - u0^(-1)) mod M.

All denominators below are odd, hence invertible modulo M. The exact identity

    N/(u+2s) - 2N/(u+s) + N/u
        = 2 N s^2 / [u(u+s)(u+2s)]

vanishes modulo M because 1+2h>=k. Therefore, for every integer j,

    N/(u0+s*j) = v0 + delta*j mod M.

Consequently the positive set with xy>=N and xy=N mod M is the disjoint union
of 2^(h-1) lattice translates

    (u0,v0) + Z(s,delta) + Z(0,M),

intersected with xy>=N. Each lattice has determinant s*M. For M<=8 there is
one translate. A strict self-normal move between global hull vertices must
change translate: within one translate the F288 reflection argument applies.
The O(sqrt M) cover is not quasipolynomial in log M.

More generally, on the class u=u0+2^r*j, the d-th forward difference is

    Delta^d (N/u) = (-1)^d d! N 2^(r*d)
                    / product_(i=0)^d (u+i*2^r).

Its exact 2-adic valuation is r*d+v2(d!). If that quantity is at least k,
the inverse graph on the class is an integer-valued polynomial of degree
at most d-1 in j, in the binomial basis. This gives a compact higher-order
representation; optimizing over it remains an unresolved operation.

## A factor point has a global exposure interval

Let N=p*q with p,q>1. For positive a,b, if

    (a*p-b*q)^2 < 4*a*b*M,

the point (p,q) has smaller objective a*x+b*y than every feasible point with
xy>N. Indeed every such product is at least N+M, and AM-GM bounds its
objective below by 2*sqrt(a*b*(N+M)); the displayed inequality puts the
factor point strictly below that bound.

Writing t=(a/b)/(q/p) and tau=M/N, the interval is

    (sqrt(1+tau)-sqrt(tau))^2 < t
        < (sqrt(1+tau)+sqrt(tau))^2.

This statement concerns the union of all inverse classes. A minimum can be
a trivial factor point unless the normal also excludes the two axis ends.

## A one-percent approximation would suffice

For an odd composite N>=9, choose the largest power of two M<=N/8, so
N/16<M<=N/8. Query normals with ratios 2^j, -n<=j<=n, where n is the bit
length of N. At least one has t between 1/sqrt(2) and sqrt(2) for any
factor pair p,q>=3. Its factor objective C obeys

    C^2/(4*a*b*N) <= (3*sqrt(2)+4)/8.

A feasible answer of cost at most (101/100) times the true minimum has
product N, because

    (101/100)^2 * (3*sqrt(2)+4)/8 < 17/16 < 1+M/N.

It is a proper factor point. The costs of (1,N) and (N,1) are each at
least (7/5)*C: use p,q>=3 and 2/3<=t<=3/2 in

    cost(1,N)/C = (p+t/p)/(1+t),
    cost(N,1)/C = (t*q+1/q)/(1+t).

Thus O(n) constant-accuracy support queries at M=Theta(N) suffice to split
every odd composite. The normals have O(n) bits and use no factor labels.
The literal reduction cost is O(n*T(n)+poly(n)) for one-query cost T(n),
using the succinct instance (N,M,a,b). This fixes a concrete sufficient
accuracy and modulus; it does not construct an efficient support oracle.
In particular the number
of nodes visited by the affine hierarchy is still unbounded by QP(n).

Evidence and related work: the exact union pilot is `RESULT.md`; the
single-translate oracle and shared hierarchy are in
`../F288_integer_hyperbola_support/PATCH_SUPPORT.md`. No literature-level
novelty claim is made for the elementary difference or exposure identities.
