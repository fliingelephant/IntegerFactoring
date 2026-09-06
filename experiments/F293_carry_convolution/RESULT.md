# Canonical half-square counts retain a phase-sensitive convolution

**Family:** route:F31

**Status:** root-derived identities and exact finite experiments. Independent
reconstruction is pending. No short coefficient evaluator or novelty claim.

## The exact position-sensitive object

For M=2^k, k>=2, and odd N, let

    C_M(N) = #{0<u,v<M/2 : u,v odd, uv=N mod M},
    epsilon(u) = +1 if the canonical u is below M/2, and -1 otherwise,
    H_M(N) = sum_(u unit mod M) epsilon(u)*epsilon(N/u mod M).

The two one-coordinate sign sums vanish, so

    C_M(N) = M/8 + H_M(N)/4.

Write each unit as sigma*5^t, where sigma is +/-1 and 0<=t<T=M/4. Put
a_j=epsilon(5^j mod M), P_k(z)=sum_j a_j*z^j. Multiplicative convolution gives

    H_M(sigma*5^t) = 2*sigma*[z^t](P_k(z)^2 mod(z^T-1)).

Thus this coefficient retains actual half-square placement. The algebraic
description is not a saving by itself: P_k has T coefficients.

For k>=3, a_(j+T/2)=-a_j. For k>=4, reflection j->t-j further reduces one
coefficient to at most T/4 sign products. If t is odd, use the T/4 consecutive
indices starting at (t+1)/2. If t is even, use T/4-1 indices starting at
t/2+1; the two remaining reflection-fixed contributions are +1 and -1 and
cancel. This proves the exact constant-memory Rust evaluator used below.

## An elementary precision law and its limit

For k>=4, a four-element action on the half-square gives

    C_M(N) = 2 mod4 if N=1 or7 mod8, and 0 mod4 otherwise.

The commuting involutions are coordinate swap and
(u,v)->(M/2-u,M/2-v). Their generic orbits have size four. The second
involution has no fixed odd pair. Swap has two fixed points exactly when
N=1 mod8. Swap followed by reflection has two fixed points exactly when
-N=1 mod8: completing the square reduces its equation to a unit square
root modulo M. The two exceptional types cannot coincide.

There is also an exact complementary-lift law

    C_M(N+M/2) = M/4-C_M(N).

For each lower-half u, the canonical inverse image changes by M/2, so exactly
one of the two target residues has its image in the lower half.

Consequently, for k>=5 and N=1 mod8,

    v2(2*C_M(N+M/2)-2*C_M(N)) = 3,

although the input difference has valuation k-1. For example M=32 has
C(1)=6 and C(17)=2. A low-input-precision approximation cannot discard the
top input bit even for this low output precision. This is not a complexity
lower bound: that bit is easy to read, and the exact sign covariance should
be retained rather than averaged away.

## The character square must retain its phase

Define the finite Bernoulli coefficient

    B(chi)=-(1/M)*sum_(u unit mod M) u*chi(u).

The sign transform vanishes unless chi is odd and primitive modulo M.
On that support it equals 4*B(chi), by pairing u with u+M/2. Therefore

    H_M(N)=16/phi(M)*sum_(chi primitive odd) B(chi)^2*bar(chi(N)).

The square has no conjugation. The analogous autocorrelation
R_M(N)=sum_u epsilon(u)*epsilon(Nu) instead uses |B(chi)|^2. It is cheap:
if A counts lower-half odd u whose linear image Nu is in the lower half,
then R=4A-M/2, and two ordinary affine floor sums compute A.

These moments are different. Multiplicatively shifting epsilon by 5 preserves
every autocorrelation but changes H_32(1)=8 to H_32(25)=-8. This only rules
out recovering the phase from that autocorrelation data alone; the known
canonical word supplies additional information.

For b_q(u)=u/q-1/2 on canonical units, put
Co(N,q)=sum_u b_q(u)*b_q(N/u). The elementary identity
epsilon_M=2*b_(M/2)-4*b_M yields

    H_M(N)=16*Co(N,M)-8*Co(N,M/2).

F292/RECIPROCITY.md identifies this as the Cochrane inverse-Bernoulli sum
and retains the two Gauss factors in its dual. Standard Dedekind
correlation reciprocity cannot be substituted for this square moment.

## Exact numerical and symbolic work

`convolution.py` used Sage integer polynomial multiplication through M=2^18,
and matched 510 direct inverse-graph histogram entries. It took 4.60 seconds
including Sage startup, with peak RSS 307,265,536 bytes. At k=18 the exact
convolution has 611 distinct values; no floating FFT rounding was used.

Early factorizations suggested extra vanishing moments. `word_moments.py`
tested them through k=24 in 2.83 seconds. The double zero at z=1 for k=5--8
does not persist: already k=9 has a half-word sum of -8 and only a simple
zero. This rejects the tested growing Prouhet-type cancellation pattern,
not arbitrary succinct representations.

`reciprocal_trace.rs`, compiled with optimization, evaluated N residues 1,3,5
for every k=4,...,34. It performed 6,442,450,910 exact sign products in
5.91 seconds, using constant memory. The outer 35-second guard recorded
completion in 7.26 seconds. Small cases were checked by separate inversion
enumeration. These residues also describe the half-square statistics of
full inputs 8M+1, 8M+3, and 8M+5; no semiprime promise is used.

`recurrence_check.py` tested a specific fixed-order-in-k model. For each
residue and each start k=4,8,12, the retained 11-by-11 Hankel determinant is
nonzero. Order-10 fits fail on their first held-out value; all smaller tested
orders fail or cannot be uniquely fitted. Thus the specified constant-
coefficient recurrences through order ten do not fit even these finite
windows. This does not exclude variable-coefficient, higher-order, eventual,
Euclidean, or other nonlinear recurrences.

The source, JSON data, raw trace, timeout status, and logs remain in this
packet. TRACE_PLAN.md records the estimate; the fresh preflight at 03:12
showed 73% memory available, load 2.09/2.06/2.06, and no numerical job.
No remote computation was required. The mathematical cost remains numerical
in M despite the small measured timings.

## Next mathematical operation

Seek an actual coefficient or reciprocal contractor that retains the square
phase and the coupled window, not a fitted higher-order depth recurrence.
The exact complementary-lift and character identities are reusable inputs.
P56 and P184 were read for prior scope; their named cocycle and selector
boundaries do not prove this contractor impossible. The cap-specific
localization problem still needs more than the full half-square count.
