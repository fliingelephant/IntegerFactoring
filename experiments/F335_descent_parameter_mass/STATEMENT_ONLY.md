# Uniform-source count-descent mass

**Family:** route:F31

Status: frozen author statement for independent reconstruction. No external
novelty claim and no conclusion about factoring mechanisms outside the policies
defined here. The discrepancy bound below is a conclusion to reconstruct,
not an assumed result from F330.

Let N>1 be odd, h=(N-1)/2, U_N the units represented by 1,...,N-1, and
J_N={a in U_N: Jacobi(a,N)=1}. Write the canonical finite continued fraction

    a/N=[0;b_1,...,b_m],  b_m>=2,  S(a,N)=sum_i b_i.

Put H_m=sum_{j=1}^m 1/j and

    M_N=4*N*H_N^2/phi(N).

For 0<=t<N define

    Q_a(t)=#{1<=y<=t: 1<=a*y mod N<=h},
    E_a(t)=2*Q_a(t)-t.

A count-descent query screens gcd(t,N), then both nonzero child counts
Q_a(t) and t-Q_a(t). It returns any proper divisor, fails if a child is zero
or t<=1, and otherwise continues at t'=min(Q_a(t),t-Q_a(t)). No other
factor screens, root routines, or parameter-dependent starting rules are
included. An attempt has at most L_N=1+ceil(log_2 N) queries.

## 1. An elementary parameter bound and inverse symmetry

For every N and a as above,

    S(a,N)=S(N-a,N)=S(a^(-1) mod N,N),
    |E_a(t)|<=10*S(a,N)  for every integer 0<=t<N.

For every integer B>=1,

    sum_{a in U_N} #{i:b_i>=B}
        <= (2*N/B)*H_floor(N/B),

where H_0=0. Consequently,

    sum_{a in U_N} S(a,N)<=2*N*H_N^2,
    E_{a uniform J_N} S(a,N)<=M_N
        <=4*(1+log_2 N)*(1+ln N)^2.

In particular the public cutoff
S<=8*(1+log_2 N)*(1+ln N)^2 retains at least half of J_N. These are
pointwise-in-N bounds, with no averaging over denominators.

## 2. Fixed-start eligibility and balanced cofactor count

For integer D>=1 define the enlarged fixed-start menu

    W(N,D)={w in Z_{>0}: |w-(N-1)/2^k|<=D for some integer k>=2}.

If a fixed-h descent has |E|<=D at every query, each screened child belongs
to W(N,D); the initial h is always coprime to N. This remains true when
multipliers vary between queries.

Let H>=4, 1<=D<=H/4, and fix an odd integer p in [H,2H]. Among odd integer
q in [H,2H], at most

    32*D*K(D),  K(D)=1+floor(log_2(8D)),

have a positive multiple of p in W(p*q,D). Every such multiple occurs at
a scale obeying

    (H-1)/D<=2^k<4*H.

If R_H is the number of primes in [H,2H], at most

    64*R_H*D*K(D)

ordered pairs of distinct primes p,q in that interval have any proper
nonunit in W(p*q,D).

An exact criterion for the original asymmetric child window is also valid.
For odd p,q, M=2^k, k>=2, r=q mod M, and D>0, the interval

    [(p*q-1)/M-D, (p*q-1)/M+D/2]

contains a positive p-multiple exactly when at least one condition holds:

    q>=M and p*r-1<=M*D;
    2*p*(M-r)+2<=M*D.

## 3. Uniform sources, with rare large defects retained

Suppose N=p*q with distinct primes p,q in [H,2H], H>=4, and
W(N,D) has no proper nonunit, for 1<=D<=H/4. A fixed-h attempt with one
uniform a in J_N retained throughout has factor probability at most

    10*M_N/D.

If each query draws a fresh independent uniform a in J_N, the bound is
10*L_N*M_N/D. No large-defect attempt is removed from these statements;
its entire probability is included in the bound.

For starts that vary, let 1<=D<min(p,q)/2, and define

    ell_v=max(0,floor(log_2(h/(v-D)))),
    V(N,D)=sum_{v in {p,q}} D*(4*ell_v+9)/v.

A uniform T in {1,...,h} has probability at most V(N,D) that T itself or
a positive integer in any symmetric window
[T/2^j-D,T/2^j+D], j>=1, is divisible by p or q.

Consequently a count descent with T marginally uniform in {1,...,h} and
one marginally uniform a in J_N has factor probability at most

    10*M_N/D+V(N,D).

Independence of a and T is not required for this inequality. If instead
T=min(a^(-1) mod N, N-a^(-1) mod N), with a uniform in J_N, the bound is

    10*M_N/D+(4*h/phi(N))*V(N,D).

For fresh multipliers replace the first term by 10*L_N*M_N/D, provided
each new multiplier is conditionally uniform in J_N given the past and
the start has the stated marginal law.

If uniform J_N sampling is implemented by independent draws from 1,...,N-1,
returning a proper generation gcd and otherwise rejecting Jacobi-negative
units, add at most 4*L_N/(H-1) to any attempt bound above. With a single
generated multiplier, L_N can be replaced by 1 in that additive term.

Taking D=floor(sqrt(H)), the variable-start bounds are
O((log N)^3/sqrt(H)) on every sufficiently large balanced semiprime.
There also exist infinitely many balanced distinct-prime inputs with the
same upper bound for the fixed-h policy. The only external number-theoretic
dependency allowed for this existence conclusion is the established bound

    pi(2H)-pi(H)>3H/(5 ln H),  H>=21,

from Rosser--Schoenfeld (1962), Corollary 3, equation (3.8).

Thus independent repetition of exactly these uniform-source attempts has
expected work at least sqrt(H)/poly(log N) on an infinite family, or does
not succeed at all. This does not bound a cheaply generated biased source,
other starting rules, branching or shifted counts, extra factor screens,
root outputs, or other factoring algorithms. Rejection sampling a biased
source must charge discarded uniform draws; direct biased sampling is a
different policy.

## 4. A separate small-multiplier obstruction

For an arbitrary unit a let A=min(a,N-a). The literal fixed-h descent with
this a makes the same unordered child queries as with A. If the least prime
divisor of N exceeds 5*A^2, the attempt returns no factor.

This last statement has no uniform-source assumption. It does not extend
to small modular inverses, general short rational inputs, changing A
between queries, or other starting values.
