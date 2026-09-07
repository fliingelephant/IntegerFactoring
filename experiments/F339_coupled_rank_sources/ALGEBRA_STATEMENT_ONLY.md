# Statement-only reconstruction target: the N-linked rank jump

**Family:** route:F31

Status: candidate statements for independent reconstruction. Unpromoted.
Reconstruct the claims below from the definitions and declared dependencies.
No result about another jump rule or a general factoring algorithm is claimed.

## Definitions and declared dependencies

Let N>=3 be odd, let a be a unit modulo N, and let 1<=t<N. Set m=t+1.
For 0<=k<m put z(k)=a*k mod N in {0,...,N-1}, and let rnk(k) be the
zero-based rank of z(k) in the sorted set of these m distinct residues.
Define

    alpha=min_{1<=k<=t} z(k),     u=its unique index,
    beta=N-max_{1<=k<=t} z(k),   v=the maximum's unique index,
    L=u+v,   d=L-m,
    A={0,...,m-1},   B={m,...,L-1}.

The following real-orbit facts are declared dependencies:

1. alpha,beta>=1, max(u,v)<m<=L<=N, gcd(u,v)=1, and
   alpha*v+beta*u=N.
2. The cyclic successor of sorted orbit indices is

       k -> k+u       for 0<=k<m-u,
       k -> k-v       for v<=k<m,
       k -> k+u-v     for m-u<=k<v.

   Its positive physical gaps are alpha, beta, and alpha+beta, respectively.
   Empty intervals are omitted.
3. This successor is the first-return map to A of T(k)=k+u mod L.
   Its cycle starts at 0 and lists the indices in increasing physical rank.
   If w=u^(-1) mod L, then

       f(k)=w*k mod L,
       J(f)=#{0<=j<f: j*u mod L is in B},
       rnk(k)=f(k)-J(f(k))   for k in A.

The sorted arrays specify the mathematical objects; their construction is
not part of the proposed runtime sampler. A count

    #{0<=j<s: (k+j*u mod L) in B}

is publicly computable as

    FS(s,L,u,k+L-m)-FS(s,L,u,k),
    FS(s,L,u,b)=sum_{j=0}^{s-1} floor((j*u+b)/L).

Euclidean modular floor sums, modular inversion, uniform finite-integer
sampling with fair bits, and verified gcd computations are available.
The extrema can be obtained by binary search with public rank counts in
polynomial bit cost. All source generation, setup, randomness, rejected
endpoints, arithmetic, and verification are charged.

## Claim A: the selected coupling and its short direct menu

Define b=beta-alpha and

    q=b mod L=N*u^(-1) mod L,    Q=floor(N/L).

This is the jump q=(beta-alpha) mod L. It is not the separate jump rule
q=N mod L. For q=0 the selected attempt returns failure.

For q!=0 draw k uniformly from A and put k'=(k+q*u) mod L. If k' is
outside A, return failure. Otherwise test gcd(rnk(k')-rnk(k),N), accepting
only a divisor strictly between 1 and N.

For an accepted pair put s=min(q,L-q). If q>L/2 reverse the ordered pair;
otherwise retain its order. Call the resulting endpoints k0,k1. Let

    H=#{0<=j<s: (k0+j*u mod L) in B},
    D=(rnk(k1)-rnk(k0)) mod m in {1,...,m-1}.

Then

    D=s-H,    0<=H<=min(d,Q).

Consequently the direct menu

    M={s-h, m-s+h : 0<=h<=min(d,Q)}

contains a gcd argument, up to sign, for every coupled output. It has at
most 2(min(d,Q)+1) entries. Duplicate entries may be removed. Zero, gcd 1,
and gcd N are failures. Entries incompatible with 1<=s-h<m may be omitted.
Testing the whole menu finds a proper factor whenever any accepted pair for
that fixed a,t does so. Menu entries need not all be attained by pairs.

The claim is pointwise in a,t and does not require small d, adjacent u,v,
or uniform q. It asserts no source-success lower bound. The probability
that a parameter's complete menu succeeds is distinct from the original
attempt's probability over k, which includes endpoint failures.

For t=(N-1)/2, Q=1 and at most four entries suffice. For
t=floor((N-1)/8), Q<=7 and at most sixteen entries suffice. No uniform
small-menu cost is asserted for arbitrary t.

## Claim B: the half-orbit quotient and residual formulas

Now assume t=(N-1)/2 and m=(N+1)/2. Put

    r=min(a^(-1) mod N, N-(a^(-1) mod N)),
    s0=floor(t/r).

If a*r=1 mod N, the extrema are

    alpha=1, u=r, beta=s0+1, v=N-(s0+1)*r.

If a*r=-1 mod N, they are

    beta=1, v=r, alpha=s0+1, u=N-(s0+1)*r.

In both cases |beta-alpha|=s0 and L=N-s0*r.

For r>=2, the actual centered jump length is s=s0. A four-entry dominating
menu can be evaluated without the extrema search by using

    s, s-1, 2s-1, 2s-3.

Writing N=2*r*s+R gives an odd integer 1<=R<2r. The gcds of the four
displayed integers with N are, in the same order, the gcds of

    R, R+2r, R+r, R+3r

with N. Thus one inverse, one integer quotient, and four verified gcds
suffice for this dominating half-orbit menu.

For r=1, a is 1 or -1. The actual centered jump length is s=1, and its
dominating menu has no proper gcd. It is essential to use this branch:
substituting the raw quotient s0=t in the four-quotient menu is a different
source and can expose a separate factor 3. Claims C and D concern the
actual r=1 branch and the r>=2 menu above.

## Claim C: an explicit uniform-unit source bound

Let N=p*q for distinct odd primes p<=q. For ell in {p,q}, define

    B_ell=4*(floor(5N/(2ell^2))+1)
             *(floor(2N/ell^2)+1).

There are at most B_ell integers r in {1,...,(N-1)/2} for which the
half-orbit menu of Claim B accepts a proper divisor divisible by ell.
Here only unit r are eligible parameters; counting additional nonunits
in the bound is permitted. The r=1 branch has no successful output.

For uniform a on the units modulo N, the probability that the entire
Claim B menu has a proper factor is at most

    min(1, 2*(B_p+B_q)/phi(N)).

In particular, if q/p is bounded by a fixed constant, this probability
is O(1/N), with a constant depending only on that balance bound.
This is a menu-source probability bound, not an asserted formula for the
per-k coupling probability. It is conditional on a uniform unit parameter.
It excludes factors obtained by screening nonunits during source generation.
It asserts no such bound for an arbitrary biased parameter law.

## Claim D: bounded rational height on every odd composite input

Let N be any odd composite integer, including prime powers and repeated
factors, and let P be its least prime divisor. Let H be a positive integer
with 5H<=P. Suppose

    a=x*y^(-1) mod N,    1<=x,y<=H,

where x and y are units modulo N. Then the actual half-orbit menu in
Claim B has no proper factor. Therefore the selected half-orbit coupling
in Claim A has none either. The r=1 branch is included as specified above.

This concerns the stated unit branch and this specific observable.
Generation-screen factors remain legitimate separate outputs. P is an
analysis parameter; no runtime action uses the unknown least prime divisor.
No conclusion is claimed for larger heights, other windows, other jump
rules, or other uses of the rational parameter.
