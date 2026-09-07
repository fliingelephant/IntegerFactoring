# A computable bound for every count defect

**Family:** route:F31

Status: root-derived elementary continued-fraction bound. Not independently
reconstructed or promoted. No novelty, parameter-density, or path-length
claim is made.

Let N>1 be odd, let alpha=a/N be in (0,1) with gcd(a,N)=1, and write its finite simple
continued fraction as [0;b_1,...,b_m], using the usual final term b_m>=2.
Let p_j/q_j be its convergents, with q_0=1 and q_m=N. Put

    S(a,N)=b_1+...+b_m.

Extend the same prefix count by Q_a(t)=#{1<=y<=t:rep(a*y)>0} for t<N.
For E_a(t)=2Q_a(t)-t, the following bound holds
simultaneously for every integer 0<=t<N:

    |E_a(t)| <= 10*S(a,N).

In particular it can be applied at adaptively chosen prefix lengths; no
independence between a and the path's current t is needed. When t<=h, it
can be combined with F330's small-remainder bound by taking the smaller of
10*S(a,N) and |rep(a*t)| (with t=0 handled directly).

## Block bound

For j<m, the convergent identity gives

    |alpha-p_j/q_j| <= 1/(q_j*q_(j+1)),

and q_(j+1)>=q_j. Indeed, expressing alpha using the continued-fraction
tail xi>=b_(j+1) gives the error
1/[q_j*(q_j*xi+q_(j-1))], using the determinant of consecutive convergents.

Consider any q_j consecutive orbit points beta+l*alpha modulo one. The
comparison points beta+l*p_j/q_j form a rotated equally spaced q_j-grid.
Each point moves in the same direction by at most1/q_(j+1)<=1/q_j when
passing from the grid to the alpha orbit. Membership in the open interval
(0,1/2) can change only near its two endpoints. Each one-sided endpoint
arc of that length contains at most two grid points, including boundary
cases. Hence at most four memberships change. The number of grid points
inside (0,1/2) differs from q_j/2 by at most one. Thus every such orbit block
has

    |2*(accepted points)-q_j| <= 10.

The phase beta is arbitrary, so the bound applies to consecutive blocks
anywhere in a prefix. It also covers denominator one and all rational
endpoint coincidences with this conservative constant.

## Prefix decomposition

Expand t<N greedily using q_(m-1),...,q_0. Just before choosing the digit
for q_j, the remaining length is below q_(j+1). Since

    q_(j+1)=b_(j+1)*q_j+q_(j-1),

that digit is at most b_(j+1). The final remainder is zero because q_0=1.
There are therefore at most S(a,N) blocks, each of a convergent-denominator
length. Adding their block errors proves the bound. For the rational orbit
with beta=0, membership in (0,1/2) is exactly the definition of Q_a on
nonzero residues for odd N.

## What this supplies

The Euclidean algorithm computes S(a,N) and the certificate10*S(a,N) in
polynomial bit time, without factoring N. Its numerical value can be large;
this is not a uniform polynomial-size defect bound for every a. The remaining
parameter question is to bound how much Jacobi-positive input mass survives
a chosen public cutoff S(a,N)<=poly(log N). F333 permits an average contract
on that parameter set, but it does not supply the surviving mass or a useful
factor probability. Small defects alone also do not control inverse resets
or prove that a path terminates quickly.
