# A closed Newton error bank and a quotient-compatible moment functional

This continuation implements a cancellation-preserving summation rule.
Newton lifting closes in a triangular error bank. Exact quotient gates can
be handled without exponent-sized division guards by a new presentation of
the F303 product functional on canonical Möbius permutations. The resulting
one-patch moment oracle is non-enumerative and polynomial in the numerical
degree and input bit lengths. Repeated conditional quotients still create
many distinct maps; no whole rectangle oracle follows.

## 1. Newton steps genuinely close

Write delta=a squared-a and E=3a squared-2a cubed. Exactly,

    E=a+(1-2a)delta,
    delta(E)=delta squared(4delta-3).                         (1)

For an arbitrary integral weight W, retain

    V_j=sum W delta^j,  U_j=sum W a delta^j.

Powers of a reduce using a squared=a+delta. If delta has valuation at
least h at every point, terms delta^j vanish modulo 2^P when jh>=P.
Hence only O(P/h) scalar moments are needed. The exact update is

    V'_j=sum_(t=0..j) binom(j,t)4^t(-3)^(j-t) V_(2j+t),
    U'_j=sum_(t=0..j) binom(j,t)4^t(-3)^(j-t)
                    [U_(2j+t)+V_(2j+t+1)-2U_(2j+t+1)].        (2)

Terms can be discarded using both their displayed coefficient valuation
and h times their index. The new guaranteed error valuation is 2h.
For two coordinates the four sectors
delta_a^i delta_b^j times 1,a,b,ab suffice; retain only
i h_a+j h_b<P. The tensor update of (2) is exact. This is a triangular
precision bank, not a replacement of the trace of a product by products
of traces.

For a quotient q=floor(x/2), with epsilon the parity of x,

    q^d = [x^d+epsilon((x-1)^d-x^d)]/2^d.                   (3)

An approximate idempotent can replace epsilon in (3) if it is correct
modulo 2^(P+d) when output precision is P. With two quotient coordinates
there are only four parity sectors; the guard is P+d_1+d_2. Applying
(2) to each sector preserves cancellation inside its parity gate, but
this termwise implementation still increases the guard with the requested
power. The next construction avoids that particular division loss by
changing coordinates before applying the global product identity.

## 2. Canonical Möbius bank

Let L=2^s, s>=1. Let A,B be odd, C a positive even integer, n an integer,
and K=AB+Cn odd. Define on x=0,...,L-1

    D(x)=B+Cx,
    T(x)=(n-Ax)/D(x) in Z_2,
    y(x)=T(x) mod L in [0,L),
    q_x=[D(x)y(x)-(n-Ax)]/L.                                (4)

The map y is a permutation. Indeed its inverse is

    x=(n-B y)/(A+C y) mod L,

with odd denominator, and the determinant K is a unit.
No involution assumption A=B is necessary.

Consider the formal series

    R(W)= product_x(1+Wx) / product_x(1+W T(x)).              (5)

The numerator also equals product(1+W y(x)). Thus

    R(W)=product_x [1+L W q_x/(D(x)(1+W T(x)))].

Modulo L squared, cross-products of two corrections vanish, giving

    [W^(j+1)](R-1)/L = (-1)^j Q_j mod L,
    Q_j=sum_x q_x T(x)^j / D(x).                            (6)

All divisions by L in (6) are exact integer divisions of coefficients
already computed modulo L squared. Each formal-series denominator in (5)
has unit constant term; the coordinates x themselves need not be units.

For requested mixed moments S_ij=sum x^i y(x)^j,

    S_ij = sum_x x^i T(x)^j
           +j L sum_x x^i T(x)^(j-1) q_x/D(x) mod L squared. (7)

To compute the weighted carry in (7), substitute the exact inverse

    x^i T^(j-1) = T^(j-1)(n-BT)^i/(A+CT)^i.                (8)

Since C is even and A is odd, the denominator in (8) has a convergent
binomial expansion whose t-th term is divisible by 2^(t v2(C)).
Modulo L, terms with t v2(C)>=s can be discarded. Thus (8) is a
polynomial in T modulo L of degree at most
i+j-1+floor((s-1)/v2(C)). Its trace uses the finite Q bank (6).

## 3. No hidden enumeration in the universal terms

Let d be the requested numerical moment degree, d>=1, and put

    J=2d-1+floor((s-1)/v2(C)), E=J+1.

Computing (5) through W^E supplies every Q needed for i,j<=d.
The universal powers of T are computed by

    T(x)^j = (n-Ax)^j B^(-j)
             sum_t (-1)^t binom(j+t-1,t)(C x/B)^t.           (9)

At precision P only t<=floor((P-1)/v2(C)) is needed. Expand the
numerator of (9) and use ordinary sums sum_(0<=x<L) x^ell. These power
sums are obtained by the exact telescoping recurrence, without enumerating
the L inputs. The required degree bank is polynomial in s,d.

From power sums of x and T(x), guarded Newton identities give the two
elementary-symmetric coefficient banks. To output them modulo 2^(2s),
start at precision

    2s+v2(E!)

and compute the t-th symmetric coefficient at precision
2s+v2(E!/t!). Formal division then gives (5). These are precisely
the integer-division guards justified for the F303 product construction.
All exact ordinary power sums have polynomial bit height in s,d; the
modular binomial expansions, coefficient arrays, and input reductions have
polynomial cost in s,d and the bit lengths of A,B,C,n.

This proves a non-enumerative polynomial-bit constructor for the one-map
bank S_ij modulo L squared. It is not obtained by requesting enormous
precision for the original u,v monomials. Its proof uses the same first-order
product mechanism as P238; no independent novelty claim is made.

## 4. Actual quotient coordinates and repeated gates

For the original graph modulo M, fix R=2^r, an odd u0<R, and
v0=N/u0 mod R. Set

    u=u0+R x, v=v0+R y, L=M/R,
    A=v0, B=u0, C=R, n=(N-u0 v0)/R.                         (10)

Then (4) is exactly the original graph on this low-residue patch; K=N.
For the first quotient r=1, u0=v0=1, so this gives the entire original
odd graph in coordinates (u-1)/2,(v-1)/2. The new oracle therefore computes
all normalized first-quotient moments modulo (M/2) squared directly.
It avoids the degree-dependent guard caused by expanding those normalized
powers into original-coordinate monomials.

For further exact quotient gates, split x=e+2X and y=f+2Y.
The parity f is uniquely determined by e through f=n-e mod 2. Each of
the two branches has the same form (4), at modulus L/2, with

    A'=A+C f, B'=B+C e, C'=2C,
    n'=(n-Cef-Ae-Bf)/2.                                    (11)

The determinant remains A'B'+C'n'=K. Thus the class closes, the bit
heights remain polynomial, and (6)-(9) apply independently to either
branch. Crucially, (11) has two actual branches, not a single averaged
map. Carry/window correlations choose their contributions.

The windows remain faithful too. If a canonical interval [H,H+2^t)
has r<=t, then H is divisible by R and its condition on u0+Rx becomes
the same interval [H/R,(H+2^t)/R) for every odd u0<R. In particular,
half-windows remain half-windows on every patch until the last scale.
The distinct family below is therefore not caused by inventing different
window boundaries on each patch.

## 5. A concrete growth family for this exact map representation

The r-bit original-coordinate patches in (10) number 2^(r-1). These
maps are actually distinct, not only differently written, whenever
k>=3r+1. To see this, let delta_0=T(1)-T(0) and
delta_1=T(2)-T(1), reduced modulo L. Both are odd and

    delta_0/delta_1 = (B+2C)/B = 1+2C/B mod L.              (12)

For C=2^r, equation (12) recovers B inverse modulo 2^(k-2r-1).
When k>=3r+1 this precision includes B modulo 2^r, hence recovers
the distinct original u0. Three values of each map already distinguish
all the branches. At r=floor((k-1)/3) this literal exact-map bank has
Theta(2^(k/3)) distinct states.

This is a state count for (11), not a lower bound against combining their
sum in another representation. It leaves the constructive target precise:
aggregate the Möbius product/carry banks over the correlated u0 family
without evaluating each separately. The earlier F289 affine cover has the
same residue family, but the present operation constructs normalized
modular moments before linearization; it is not an affine support oracle.

## 6. Exact controls and sources

`MOBIUS_BANK.py` implements (5)-(9) without enumerating x inside the
oracle. Its separate audit enumerates actual original-N patches and checks
both Q_j and every S_ij through degree three. All 780 checks passed for
k=4 through 9, with r=1,2, or floor(k/2). Runtime was 0.020 seconds;
peak RSS was 17,694,720 bytes. Source, output, and log are retained.

`MOBIUS_BRANCHES.py` verifies (12) and the distinct-map count on randomized
original N for k=7 through 19. Its small exact signatures do not enumerate
the graph. Its output and log retain the case counts and resources.

`MOBIUS_BANK_GROWTH.py` separately counts distinct degree-two moment and
carry banks at k=7,10,13,16,19 and r=floor((k-1)/3). There are
2,4,8,16,32 patches. The observed moment-bank counts are 2,2,8,16,32;
carry-bank counts are 2,4,8,16,32. Thus equality of moment banks does
occasionally merge maps, and the proof of map distinctness is not promoted
to a theorem about every truncated bank. The tested exact carry banks show
the concrete growth that remains after this cancellation-preserving rule.
This follow-up took 0.011 seconds and 18,137,088 peak RSS bytes.

`SOURCE_LEADS.md` is the unchanged source-support note supplied by the
root. Roblot's bounded-measure/Mahler theorem requires a quantitative
cutoff; Caruso et al.'s D-finite evaluator requires a certified equation
and analytic bounds. Neither is invoked to justify the circuit trace.
The positive bank here is proved directly by formal products and guarded
coefficient arithmetic. No complete rectangle-count or factoring claim
is made.
