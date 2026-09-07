# A polynomial-bit half-box counter modulo eight

**Family:** route:F31

**Status:** the half-box constructor is independently reconstructed in P243,
with exact finite controls. STATEMENT_ONLY.md and RECONSTRUCTION.md preserve
the checked scope. No exact count, arbitrary-cut counter, emptiness oracle,
or factoring algorithm is claimed.

## Actual gain and closest prior

P242 evaluates the complete unshifted transport modulo four. This packet
uses that value to compute a count on the original inverse graph, modulo
eight, without enumerating the graph. It is a fixed half/half rectangle;
the endpoints are not free parameters. C271/F311 retained finite half-phase
tables and small field models. C273/F314 represents arbitrary cut counts
modulo four but does not evaluate the trace. F317's affine blocks expose
the parity of the moving quotient. The construction here evaluates three
bits of that count for the original inverse map.

The Rust record search checked `half-box`, `modulo eight`, and the scoped
current records. F294's internal half-window is within a chart at another
modulus and does not supply this all-input constructor. This is a comparison
with inspected records, not a claim of external novelty.

## Smaller carries encode the half-box exactly

Let R=2^k, k>=3, and phi=R/2. For any positive odd full input N, set
nu=N mod R in [1,R), ell=(N-nu)/R, and, for odd 1<=u<R,

    v=nu/u mod R in [1,R),
    q_N(u)=(uv-N)/R.

The lift of v to the inverse graph modulo 2R is

    v + R*(q_N(u) mod 2).

Indeed the coefficient of R in the product is q_N(u)+u*(q_N(u) mod2),
which is even because u is odd. Consequently

    C(N,2R)=#{odd u<R : N/u mod 2R<R}=sum_u 1_(q_N(u) even).

For every integer q, including negative q,

    1_(q even)=1-q+2*binom(q,2)-4*binom(q,3) mod8.       (1)

For nonnegative q this is the binomial expansion of (1+(-1)^q)/2;
the same congruence holds for all integers, by its period-eight residue
check or the integral negative-binomial expansion modulo sixteen.
Writing H_N=sum q_N, B_N=sum binom(q_N,2), and A_N=sum binom(q_N,3),

    C(N,2R)=phi-H_N+2B_N-4A_N mod8.                     (2)

Thus the required precisions are eight for H, four for B, and two for A.

## The cubic parity has at most four fixed points

The permutation u -> nu/u modulo R is an involution and preserves q_N.
All nonfixed pairs cancel from A_N modulo two. An odd square root exists
exactly when N=1 modulo eight, and then the four roots are
a,-a,a+R/2,-a+R/2 modulo R.

For a root u, replacing u by R-u changes q by R-2u=2d with d odd. Since
binom(q,3) modulo two is the product of the two lowest bits of q,

    binom(q+2d,3)+binom(q,3)=q mod2.

The other root pair may be represented by a+R/2 with an optional negation
to return to [1,R). Its q parity differs by a+R/4, which is odd. Therefore

    A_N=1_(N=1 mod8) mod2.                               (3)

This proof also covers negative q and arbitrary full input lifts N.

## Two universal reference constants

Use the R/4=L residues h=1 modulo four below R as representatives for
sign pairs. Their inverses u are also 1 modulo four. For N=1 write
q=(hu-1)/R and d=(R-h-u)/2, so d is odd. The negative member has carry
q+2d. Since the positive-class sums of h and u both equal L(2L-1),

    H_1=2 sum_(h=1 mod4) q + R/2.

Inversion pairs cancel modulo two in the last sum except h=1 and
h=1+R/2. Their carries are 0 and L+1, respectively. Hence

    H_1=2 mod4.                                         (4)

For B_1, a sign pair contributes

    binom(q,2)+binom(q+2d,2)=q(q+1)+2-d mod4.

An inversion pair of distinct positive representatives therefore
contributes 2 modulo four. There are (L-2)/2 such pairs. The two fixed
positive representatives contribute 3 and L^2-L+1, respectively. Thus

    B_1=(L-2)+3+(L^2-L+1)=2 mod4,                       (5)

because L is even. The k=3 boundary is included.

## P242 supplies the remaining binomial carry bit

Reparametrize by w with u=w^(-1) modulo R, and set

    f(w)=floor(nu*w/R),
    q_1(w)=(uw-1)/R.

The exact input transport is q_nu=nu*q_1-u*f. Expanding the binomial
polynomial gives

    B_nu=nu^2 B_1+binom(nu,2)H_1-nu*T_R(nu)
              +sum_w (u^2*f^2+u*f)/2.                  (6)

This is an integer identity before reduction. To compute its last half
modulo four, retain the numerator modulo eight. Odd squares are 1 modulo
eight and u=w modulo eight, as R is divisible by eight. Put

    J_nu=sum_w (f(w)^2+w*f(w)) mod8.

Each summand is even. Dividing the even canonical residue by two gives
the required residue modulo four. Equations (4)--(6) therefore yield

    b_nu=B_nu mod4
         =2+nu*(nu-1)+J_nu/2-nu*T_R(nu) mod4.           (7)

P242 computes T_R(nu) modulo four for every canonical odd nu. Only
ordinary degree-two floor sums remain in J_nu: on w=a+8j, a=1,3,5,7,

    J_nu=sum_a sum_(j<R/8) [floor(nu*(a+8j)/R)^2
                                +a*floor(nu*(a+8j)/R)] mod8.

No increasing reciprocal-expansion degree is needed at this precision.

For completeness the implementation's Euclidean state is
(sum f, sum j*f, sum f^2), for f=floor((a*j+b)/m). Remove the integral
quotients of a/m and b/m by expanding a quadratic. In the normalized
case 0<=a,b<m, let Y=floor((a*(n-1)+b)/m), and let
t_l=ceil((m*l-b)/a), 1<=l<=Y. The three sums are

    nY-sum_l t_l,
    Y*n*(n-1)/2-(sum_l t_l^2-sum_l t_l)/2,
    nY^2-sum_l (2l-1)t_l.

These are the same three moments for a Euclidean child with slope m and
denominator a. The half is an exact integer. There are O(k) steps, with
O(k)-bit operands for the inputs used here. Zero length or normalized
zero slope gives zero moments directly.

## Full input and product precision

Since q_N=q_nu-ell, exact binomial translation gives

    B_N=B_nu-ell*H_nu+phi*binom(ell+1,2).

Here phi is divisible by four and H_N=H_nu-phi*ell. Thus

    B_N=b_nu-ell*H_N mod4.                              (8)

Compute H_N modulo eight using the odd-unit product P_R:

    H_N=((P_R^2-N^phi mod8R)/R)*N^(1-phi) mod8.          (9)

The numerator is the canonical residue modulo 8R and is divisible by R.
Indeed product_u(N+R*q_N(u))=P_R^2, and all terms of order at least two
in R vanish modulo 8R since R>=8. Division by R leaves three valid bits.
The remaining inverse is odd. P238 computes P_R modulo 8R with a finite
power-sum/Newton expansion; no large integer factorial is constructed.

Substituting (3), (7), (8), (9) in (2) is the final constructor. Its cost
is a fixed polynomial in k and the bit length of N. A conservative
schoolbook bound is O((k+bitlength(N)+1)^8), with polynomial space. The
floor moments and P242 use O(k) Euclidean or modular steps; the product
uses O(k) exact coefficients of O(k^2) bits and O(k^2) arithmetic steps.
No call enumerates a number of points exponential in k.

## Evidence and goal boundary

`pilot.py` loads only the three named P242 function definitions through
Python AST, without executing earlier experiment drivers. It implements
the P238 product at exactly k+3 guard bits and the displayed degree-two
floor recurrence. `pilot.json`, `pilot.log`, and `pilot.status.json`
retain the outputs and the external timeout result.

All 1,173 direct count comparisons passed. The pilot used every odd
residue modulo 2R through R=128, then specified and seeded residues
through R=4096. Every residue used three full input forms: r, 8*(2R)+r,
and 2^(3k)+r. The latter exercises large negative carries. The ordinary
floor routine passed 300 direct comparisons; all ten small product
comparisons passed. H, B, and A were separately checked on each count.

Nonenumerating calls at R=2^32,2^64,2^128,2^256 completed. The k=256
case took 0.585 seconds; the entire pilot used 0.797 seconds and
20,758,528 bytes peak RSS. Those large residues have a proof-based
constructor but no independent full-graph numerical check.

A zero residue does not prove emptiness. The half-box also contains
products N+t*(2R), whereas P237's short public rectangles enforce t=0.
The next mathematical task is to transport this count precision to sharp
endpoints, or to close the higher-precision binomial/section recurrence.
Neither operation is supplied here.
