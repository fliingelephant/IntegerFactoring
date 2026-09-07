# Proof of the count-descent mass statements

**Family:** route:F31

Status: author proof. Independent reconstruction is still required. The
stronger distribution theorem discussed in SOURCES.md is not a dependency.

## Continued-fraction accounting

Use p_0=0,q_0=1 and p_{-1}=1,q_{-1}=0 for the convergents. For the digit
b_{j+1}, 0<=j<m, let r_j=|a*q_j-N*p_j|>0, with r_{-1}=N. The Euclidean
relations and determinant identities give

    r_{j-1}=b_{j+1}*r_j+r_{j+1},
    N=q_j*r_{j-1}+q_{j-1}*r_j.

Hence b_{j+1}*q_j*r_j<=N. The signed congruence is
a*q_j=+r_j or -r_j modulo N. Denominators increase strictly except that
q_0=q_1=1 is possible; those two convergents have opposite signs. Thus a
digit occurrence injects into its (a,q,sign,r) tuple.

If b_{j+1}>=B, then q*r<=N/B. For fixed q put g=gcd(q,N). Only r divisible
by g can satisfy a*q=+/-r modulo N. There are at most
floor(N/(B*q*g)) such r, and each signed congruence has at most g residue
solutions a. Dropping the unit restriction only enlarges the count. Summing
the two signs and q<=floor(N/B) gives

    sum_a #{digits>=B}<=2*sum_q N/(B*q).

Summing over B=1,...,N gives at most 2*N*H_N^2 for the total digit sum.
The kernel of the Jacobi character has size at least phi(N)/2, even when
the character is trivial. This gives E_J S<=M_N. If the distinct prime
divisors are ordered p_1<...<p_w, then p_i>=i+1 and

    N/phi(N)=product_i p_i/(p_i-1)<=w+1<=1+log_2 N.

Markov's inequality and H_N<=1+ln N finish the stated cutoff bound.

Replacing a/N by 1-a/N preserves the canonical digit sum: if b_1>1,
insert 1 and replace b_1 by b_1-1; if b_1=1, delete it and increase the
next digit by one. The one-digit endpoint cases give the same identity.
The reversed fraction [0;b_m,...,b_1] has denominator N and numerator
q_{m-1}. Its digit sum is unchanged after canonicalizing a possible final
1. The convergent determinant gives
a*q_{m-1}=(-1)^(m-1) modulo N. Combining reversal with the complement
identity proves inverse symmetry.

## Uniform prefix discrepancy

For j<m the convergent error satisfies
|a/N-p_j/q_j|<=1/(q_j*q_{j+1}). Compare any block of q_j consecutive
orbit points with the rotated equally spaced q_j-grid of step p_j/q_j.
All point displacements have the same direction and length at most
1/q_{j+1}<=1/q_j. For membership in (0,1/2), each of its two boundary
arcs contains at most two grid points, including endpoint cases. Thus at
most four memberships change. The rotated grid count differs from q_j/2
by at most one, so the absolute signed count defect of any block is at
most ten. This also covers denominator one and any initial phase.

Greedily decompose any t<N into lengths q_{m-1},...,q_0. Before choosing
the digit at q_j the remaining length is below q_{j+1}, and
q_{j+1}=b_{j+1}*q_j+q_{j-1}, so at most b_{j+1} such blocks are used.
The total number is at most S. Adding their defects proves |E_a(t)|<=10S
simultaneously for every t. At a unit rotation and t<N no orbit point is
zero, and odd N excludes 1/2, so (0,1/2) is exactly the stated Q count.

## Fixed-start arithmetic

With |E_j|<=D, t_{j+1}=(t_j-|E_j|)/2 gives

    t_0/2^j-D*(1-2^(-j))<=t_j<=t_0/2^j.

Both children at query j therefore lie between
t_0/2^(j+1)-D and t_0/2^(j+1)+D/2. For t_0=h these are included in
W(N,D), with k=j+2. Also gcd(h,N)=1.

Let a p-multiple w=m*p belong to W(p*q,D), and put M=2^k. Then

    |p*(q-M*m)-1|<=M*D.

The odd integer q-M*m is nonzero, so the left side is at least p-1.
This yields M>=(H-1)/D. Positivity m>=1 also gives
M<(p*q)/(p-D)<=2H/(1-D/p)<4H. Since H>=4, these scales lie in
[H/(2D),4H), which contains at most K(D) powers of two.

For fixed p and M, q must lie in intervals centered at M*m+1/p of radius
R=M*D/p. The number of m whose intervals meet [H,2H] is at most
H/M+2D/p+2. Each interval contains at most 2M*D/p+1 integers. Their product
is

    2H*D/p+H/M+4M*D^2/p^2+2D/p+4M*D/p+2.

Using p>=H, H/M<=2D, M<4H, and D<=H/4 bounds this by 27D, hence by
32D. We may count all integers in these intervals because the scale
restriction was already derived for the odd eligible q. Summing scales
proves the cofactor count. For prime pairs a proper nonunit is divisible
by p or q; sum the bound over the R_H choices of p and then use symmetry.

For the exact asymmetric condition, write q=M*l+r with 1<=r<M odd.
The nearest lower p-multiple is p*l; it is positive exactly when q>=M,
and its distance below the center is (p*r-1)/M. The nearest upper
p-multiple is p*(l+1), at distance (p*(M-r)+1)/M. Their respective allowed
distances are D and D/2. More distant multiples cannot be eligible unless
one of these nearest multiples is. This proves both directions.

## Uniform and inverse starts

Fix one prime divisor v and suppose 1<=D<v/2. If a window at scale M=2^j,
j>=1, reaches a positive v-multiple, then M<=h/(v-D). Write ell for the
stated maximum scale index. At each scale, at most h/(M*v)+1 multiples
are relevant, and each covers at most 2M*D+1 integer starting values T.
Divide by h and sum over j=1,...,ell. The terms are bounded by

    2ell*D/v + 1/v + 4D/(v-D) + ell/h.

Here h>=v for an odd composite with at least two prime factors. Since
D>=1 and D<v/2, this is at most 4D*(ell+2)/v. The initial screen T adds
at most 1/v, giving D*(4ell+9)/v. A union bound over p and q proves V.

Under a uniform a in J_N, inverse representatives are uniform on J_N.
Folding the two signs has at most two preimages, so every possible T has
mass at most 2/|J_N|<=4/phi(N). Its mass on the eligible starting set is
therefore at most (4h/phi(N))*V. This uses only the marginal law of T;
it never assumes that the start and the multiplier are independent.

## The complete rare-event accounting

For one uniform multiplier, Markov gives
Pr(S>D/10)<=10*M_N/D. Off that event every defect at every adaptive query
is at most D. On a menu-empty fixed-start input this forbids all factor
outputs. For varying starts, success off the bad event requires membership
in the eligible start set just bounded. A union bound proves the claims,
including arbitrary dependence between a and a marginally uniform T.

With fresh conditional-uniform draws the same tail bound applies at each
query, even after conditioning on previous failures and reached t. There
are at most L_N queries, so sum those tail probabilities. This only
enlarges the set of possible successful attempts.

For the stated raw sampler, a draw is either a proper nonunit, a J_N unit,
or a rejected unit. The probability of a proper nonunit before the next
J_N unit is at most their per-draw probability ratio. On distinct-prime
N=p*q the ratio is

    (p+q-2)/(|J_N|)=2/(p-1)+2/(q-1)<=4/(H-1).

There is no possible gcd=N draw in the range 1,...,N-1. Summing over at
most L_N generated multipliers proves the additive accounting. A direct
perfect uniform sampler can omit this term, but its cost is not free.

For D=floor(sqrt H) and sufficiently large H, D<=H/4,
N/phi(N)<=2, H_N=O(log N), ell_p,ell_q=O(log N), and
4h/phi(N)<=4. The variable-start bound is therefore
O((log N)^3/sqrt H), with the extra logarithm only needed for fresh draws.

For the fixed start, the number of exceptional distinct ordered prime
pairs is at most 64*R_H*D*K(D). The declared prime-count bound implies
R_H>=3H/(5 ln H). Thus the exceptional fraction among all distinct pairs
is O((ln H)^2/sqrt H), tending to zero. For every sufficiently large H
there are menu-empty pairs, giving an unbounded family of inputs. The
same rare-event and generation bounds apply to them. Each restarted
attempt incurs at least one bit operation. Independent repetition has
expected attempts equal to the reciprocal success probability, or never
succeeds if that probability is zero. Since N is between H^2 and 4H^2,
this lower bound is a numerical power of N up to logarithms, not QP in
its bit length. No claim extends beyond the specified source and screens.

## Small numerical multipliers

Negating the multiplier exchanges Q and t-Q, so work with A=min(a,N-a).
At a query let k=floor(A*t/N), r=A*t-kN, and I=1 if r<=h, otherwise 0.
Since A is a unit and 1<=t<N, one has 1<=r<N.

The complete positive rotation intervals have lengths

    L_u=floor((u*N+h)/A)-floor(u*N/A).

Put delta_u=(u*N mod A)-((u*N+h) mod A); then
A*L_u=h+delta_u and |delta_u|<=A-1. If I=1, the final interval is partial:

    Q=t-floor(k*N/A)+sum_{u<k} L_u,
    2A*Q=2A*t-k*N+e,
    e=-k+2*(k*N mod A)+2*sum_{u<k} delta_u.

If I=0, the final interval is complete:

    Q=sum_{u<=k} L_u,
    2A*Q=(k+1)*N+e,
    e=-(k+1)+2*sum_{u<=k} delta_u.

Both cases have |e|<=2A*(k+1). Starting from R=-A, which represents
2A*h modulo N, represent the two children by

    R_Q=I*R+e,  R_other=(1-I)*R-e.

Thus each child residual is at most |R|+2A*(k+1) in absolute value.
Every continuation has k_next<=floor(k/2). If k=0 and A*t<=h, then
Q=t and the attempt stops. If k=0 and A*t>h, the next t is at most t/2,
so A*t_next<N/2 and the following query stops. There are at most two
zero-k queries.

Initially k_0<=floor((A-1)/2). The sum of positive k values is at most
2k_0, and the number of positive-k queries is at most k_0. Consequently

    sum_queries (k+1)<=3k_0+2<=(3A+1)/2.

Every retained or screened residual therefore has absolute value at most
A+2A*(3A+1)/2=3A^2+2A<=5A^2. A positive screened count w satisfies
0<w<N and gcd(2A,N)=1, so its residual cannot be zero. If a prime divisor
of N also divided w, it would divide this nonzero bounded residual. This
is impossible when every prime divisor exceeds 5A^2. Zero children are
not screened and cause only failure, as specified.
