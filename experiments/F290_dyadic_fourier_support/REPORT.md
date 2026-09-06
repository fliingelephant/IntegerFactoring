# F290: exact dyadic objective transforms and the remaining signed carry

**Family:** route:F31

Status: author-derived candidate proofs and exact finite
certificates. Independent reconstruction is pending. No support oracle or
all-input factoring algorithm is claimed.

## Object and scope difference

The object is the inverse graph modulo the known public modulus M=2^k,
with odd N, and its geometry-weighted count

    C_W = sum_{u odd mod M} W(u, N/u mod M).

The target cap has positive coordinates, xy>=N, and ax+by<=T, where
T^2/(4ab)<N+M. Every cap point satisfying xy=N mod M then has xy=N.
The public modulus lies between N/16 and N/8 in the pilot.

The Rust reader was used to load P49. Its Fourier-flatness theorem uses
the unknown-factor semiprime modulus N and complete prime-field sums.
It expressly leaves nonlinear and geometrically localized processing
open. Neither that bound nor a Fourier-equidistribution dismissal is
used here. The new compression below is specific to a known power of2.

## A weighted transform that really does compress

For odd a,b,N define the modular-objective histogram

    Q_M(s)=#{u odd mod M : au+bN/u=s mod M}.

For each K=1,...,k let m=floor(K/2), l=ceil(K/2), and let U_K
contain the odd u modulo2^l satisfying

    a u^2=bN mod2^m.

When m=0 this means U_1={1}. Define c_K(u)=au+bN/u mod2^K.
The set U_K has at most8 elements. The exact formula is

    2 Q_M(s)=1+sum_{K=1}^k 2^floor(K/2) sum_{u in U_K}
      [1_{s=c_K(u) mod2^K}-1_{s=c_K(u)+2^(K-1) mod2^K}].

Thus the entire histogram has a signed description with O(k) residue
classes, although it has M entries. Interval counts and linearly weighted
prefixes can be computed in polynomial bit complexity in k, using exact
integer arithmetic, without enumerating M or sqrt(M) Fourier modes.

Proof. For odd r modulo2^K, write each odd variable as u+2^l j.
The quadratic and higher terms of its inverse expansion vanish mod2^K.
Summing j modulo2^m kills all terms except a-bN/u^2=0 mod2^m.
Therefore the complete sum is

    S_(2^K)(r)=2^m sum_{u in U_K} e_(2^K)(r c_K(u)).

For a frequency of valuation k-K, the complete sum at M is2^(k-K)
times this sum. Fourier inversion, grouping by K, uses

    sum_{r odd mod2^K} e_(2^K)(rd)
      =2^(K-1)[1_{d=0 mod2^K}-1_{d=2^(K-1) mod2^K}].

The zero Fourier mode contributes1/2, proving the formula. The odd
square roots modulo2^m are obtained by bit lifting, with at most4
surviving roots for m>=3; for odd K each has two representatives mod2^l.

For an interval L<=s<=T, each residue class is counted by two integer
divisions. For the positive weight w(s)=T+1-s on that interval, its
contribution along a progression s=s_0+jq with n terms is

    n(T+1-s_0)-q n(n-1)/2.

The same method handles fixed-degree polynomial weights by finite power
sums. It is an exact compression of these modular objective weights.

## Exact pilot and useful zero certificates

`weighted_prefix.py` checked1,008 interval and weighted identities against
full histograms for M up to512 and several odd normals. It then used
the compressed formula up to M=2^20 and independently enumerated only
the short geometric cap for finite comparison. All arithmetic is exact;
runtime was0.02 seconds. Selected examples are:

| M | N | [L,T] | Modular count | True cap count | Stationary terms |
| ---: | ---: | --- | ---: | ---: | ---: |
| 4096 | 49153 | [444,447] | 32 | 2 | 50 |
| 16384 | 196609 | [887,895] | 0 | 0 | 62 |
| 65536 | 786433 | [1774,1791] | 64 | 0 | 74 |
| 1048576 | 12582913 | [7095,7165] | 48 | 0 | 98 |

A zero modular count is a valid fast certificate that the contained
positive cap is empty. A positive count is not a cap witness. The
distinction is actual coordinate placement, not numerical precision.

## The high-bit involution and an exact weighted recurrence

Let M=2L with L even. For each odd u in[0,L), let v=N/u mod L and

    c(u)=(N-uv)/L mod2,    chi(u)=(-1)^c(u).

The two lifts to the inverse graph modulo M are exactly

    (u, v+cL),   (u+L, v+(1-c)L).

This follows by expanding (u+epsilon L)(v+eta L) modulo2L:
the lift equation is epsilon+eta=c mod2. In particular shifting one
coordinate by M/2 shifts the other by M/2. Cutting only u to its lower
half divides a complete objective histogram by2, but cutting both
coordinates requires c=0.

For arbitrary W write W_ij=W(u+iL,v+jL). The exact signed recurrence is

    C_W = (1/2) sum_{u odd mod L}
      [W_00+W_01+W_10+W_11
       +chi(u)(W_00+W_11-W_01-W_10)].

For the lower-half square this becomes

    C_lower-square=(phi(L)+sum_u chi(u))/2.

The second term is the missing joint-placement correlation. For triangle
or cap weights it carries the corresponding difference of four weights.
This is an exact recurrence, but it is not closed in the unweighted
objective histogram.

## A counterexample to histogram-only localization

At M=16, N=3 and N=11 have identical full Q_M, but their lower-half
square counts are4 and0. More generally, for a=b=1, every N=3 mod8 and every
k>=3,

    Q_(2^k)(s)=4 if s=4 mod8, and0 otherwise.

Indeed for K>=4 the stationary square equation has no roots even mod4,
so only K<=3 remain; direct evaluation at8 gives the displayed law.
Hence all these N have identical histograms at every dyadic modulus.

The same failure occurs in the requested short-cap geometry. After
screening prime divisors through31, the exact pilot found:

    M=1024, L=227, T=228,
    N_1=12827: cap points (101,127),(127,101),
    N_2=12851: no cap points.

Both N have the same full dyadic objective histograms, the same L,T,
and modular interval count4. Both satisfy N/16<M<N/8 and
T^2<4(N+M). Thus the caps isolate exact products, not spurious product
levels. This disproves a recurrence that uses only those objective
histograms and these bounds to decide the cap. It is not a lower bound
for algorithms that use N and additional joint geometry.

For a=b=1 define A_M(s) by the actual, unwrapped sum x+y=s. Then
Q_M(s)=A_M(s)+A_M(M+s)=A_M(s)+A_M(M-s) for0<s<M, using simultaneous
complementation. The counterexample exhibits the information lost by
that addition. Increasing M does not force modular square roots of the
discriminant to become small real roots.

## The signed carry has a multiplicative-character representation

The carry is structured, not an arbitrary bit. For L=2^m,m>=2, choose
the character psi on units modulo2L defined by

    psi(-1)=1, psi(5)=exp(2pi i/2^(m-1)).

The unit group is generated by -1 and5, with5 of order2^(m-1).
The elementary squaring identity
5^(2^(m-2))=1+2^m mod2^(m+1) shows psi(1+L)=-1. Since uv=N mod L,

    chi(u)=psi(u)psi(v)/psi(N).

Thus the signed recurrence requires a geometrically truncated
multiplicative-character twist of the inverse graph at the previous
level. Completing the character sum alone would again discard its
canonical representative placement. This is a precise candidate next
transform, not an evaluation algorithm for that term.

## Why the shared stationary-root collapse does not immediately extend

Adding one transverse Fourier shift changes the phase to

    r(u+N/u)+8u.

At M=2^(2m), m>=5, and N=1 mod8, its stationary roots satisfy

    u^2=Nr/(r+8) mod2^m,   r odd.

As r varies, there are exactly2^(m-4) distinct ratios and2^(m-2)
distinct stationary roots. To see the ratio count, subtract two ratios:
its 2-adic valuation is3+v_2(r-s). Each ratio is1 mod8 and therefore
has4 roots, with disjoint root sets. This was checked for m=5,...,12.

Hence a direct reuse of the common-root-list compression already has
sqrt(M)/4 distinct roots for this one shifted ray. This is only a cost
statement about that reuse scheme. Reciprocity or a different signed
recurrence could still sum the phases without listing the roots.

## Remaining question and evidence

Can the weighted signed carry term in the exact four-child recurrence
be evaluated or bounded sharply in polynomial or quasipolynomial work,
using its character structure and the thin cap geometry? That is the
remaining operation. The complete objective transform is now cheap,
and histogram-only localization has an explicit finite counterexample.

Sources: weighted_prefix.py/json and carry_rectangle.py/json. The latter
verified112 lift recurrences and the two counterexamples. No hidden
factor labels were inputs to any public operation. The cap scan is an
offline exact certificate, not a proposed fast support implementation.
The local load was about2.1; all jobs were tiny and well below the stated
30-second/256-MB budget. No shared record, catalog, or commit was changed.
