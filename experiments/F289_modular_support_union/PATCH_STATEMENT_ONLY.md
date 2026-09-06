# Statement-only reconstruction request

No proof is included. Reconstruct or refute each claim from the definitions.
These claims do not provide an efficient optimizer or a complete factoring
algorithm. Do not read other files in this packet or inherited research notes.

## 1. An affine cover

Let N be odd, k>=1, M=2^k, h=max(1,floor(k/2)), and s=2^h. Define

    S = {(x,y) in Z_(>0)^2 : xy>=N and xy=N mod M}.

For each odd u in [1,s), define v=N*u^(-1) mod M and
delta=N*((u+s)^(-1)-u^(-1)) mod M, using least nonnegative residues.

Claim: S is the disjoint union, over those u, of

    [(u,v) + Z(s,delta) + Z(0,M)] intersect {x>0,y>0,xy>=N}.

There are exactly 2^(h-1) translates and each difference lattice has
determinant s*M.

## 2. Higher differences

Let r>=1, s=2^r, and u be odd. For f(u)=N/u modulo M, the d-th forward
difference with step s satisfies, for d>=1,

    Delta_s^d f(u) = (-1)^d d! N s^d / product_(i=0)^d (u+i*s) mod M.

If r*d+v2(d!)>=k, the map j -> N/(u+s*j) modulo M is represented on all
integer j by a polynomial of degree at most d-1 in the binomial basis
{binom(j,0),...,binom(j,d-1)}, with coefficients modulo M.

## 3. Constant-accuracy optimization is sufficient

Let N>=9 be any odd composite, n=ceil(log2(N+1)), and let M be the largest
power of two at most N/8. Use S from claim 1 with this M (also allowing
M=1, for which the product congruence imposes no restriction).

For each integer j in [-n,n], put

    a_j=2^max(j,0), b_j=2^max(-j,0),
    OPT_j = min_(x,y in S) (a_j*x+b_j*y).

Suppose any point Q_j=(x_j,y_j) in S is supplied with

    a_j*x_j+b_j*y_j <= (101/100)*OPT_j.

Claim: at least one supplied Q_j has x_j*y_j=N and x_j,y_j>1.
The query normals have O(n) bits, and there are O(n) queries. Thus an
optimizer satisfying this feasible relative guarantee with a uniform QP(n)
bit-cost bound would yield a splitter for every odd composite, with QP(n)
total cost. No cost bound for that optimizer is assumed to be established.
