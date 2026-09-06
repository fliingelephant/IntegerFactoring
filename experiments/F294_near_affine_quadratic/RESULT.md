# F294: exact near-affine counts and positive slope-block averaging

**Family:** route:F31 (inverse-chart application; abstract counts scoped below)

Status: proof candidates and exact finite checks. No all-input factoring
algorithm or novelty claim is established. The fixed-N chart coupling is
retained explicitly and is not solved by the abstract block average.

## Model and an explicit special-slope evaluator

Put m=2^r, q=m^2, r>=1, and let beta be odd. For odd alpha and integer D,
write C(alpha,beta,D) for

    #{0<=j<q/2 : (alpha*j+m*beta*j^2+D) mod q < q/2}.

For alpha=1+m*t and D=m*c, write j=l+m*h. The low output digit is l and the
high output digit is `h+beta*l^2+t*l+c mod m`. Consequently

    C = sum_(l mod m) w_m(beta*l^2+t*l+c),
    w_m(z)=abs((z mod m)-m/2).

If t is odd, the complete quadratic value histogram has multiplicity two
on the parity class c and zero on the other class: its derivative is odd,
so each of the two roots modulo 2 lifts uniquely. For r>=2 this gives
`C=m^2/4` exactly.

If t is even, complete the square. Set

    b=(t/2)*beta^(-1) mod m, c0=c-beta*b^2 mod m.

The square histogram has O(r) dyadic residue strata. On every stratum whose
period is at most m/2, the triangular weight averages exactly to m/4,
regardless of its translated residue. Only the top strata remain:

* If r=2k>=2,

      C=m^2/4+2^k*(w_m(c0)+w_m(c0+beta*m/4)-m/2).

* If r=2k+1>=3,

      C=m^2/4+2^(k+1)*(w_m(c0+beta*m/8)-m/4).

For r=1 the answer is 1 when t is even, and `2*w_2(c)` when t is odd.
Thus one modular inverse and a constant number of integer operations
evaluate this position-sensitive count. Their bit cost is polynomial in r.

For completeness, the square strata used here have valuations 2v<r. When
r-2v>=3 their values form one residue class modulo 2^(2v+3), each with
multiplicity 2^(v+2). When r-2v is 2 or 1, there is one value with
multiplicity 2^(v+1) or 2^v. Zero has multiplicity 2^floor(r/2).

## A geometry-preserving opposite-slope identity

For any odd alpha and arbitrary D, with the aligned half windows above,

    C(alpha,beta,D)+C(-alpha,beta,D)=q/2+epsilon_D,

where epsilon_D is +1 if D mod q<q/2 and -1 otherwise. Indeed the map is
antipodal: shifting its argument by q/2 shifts its value by q/2. Negating
the input exchanges the two input halves except for the endpoints 0,q/2;
these give precisely epsilon_D.

This extends the special evaluator to alpha=-1 modulo m when D=m*c. It
also evaluates an opposite-slope-paired aggregate directly. Such an
aggregate is almost parameter-independent, so it need not retain useful
localization information.

## General odd slopes: an exact positive block evaluator

The stronger operation averages a whole slope block while holding its
polynomial coefficient and geometry fixed. It permits an arbitrary cyclic
input interval `[A,A+I)` of integer length 0<=I<=q and a translated cyclic
output half `[B,B+q/2)`.

Fix a, beta, D, and consider slopes `alpha_t=a+m*t`. For 0<=u<=r, sum over
`t=t0 mod 2^u`, with t ranging modulo m. Define

    L=2^(r-u), alpha0=a+m*t0, Q'=q/L,
    J0=ceil(A/L), K0=ceil((B-D)/L),
    E=ceil((A+I)/L)-J0,
    Gamma=m*beta*L.

Let R_count be the count for 0<=z<E whose residue modulo Q' under

    G(z)=Gamma*z^2+(alpha0+2Gamma*J0)*z
         +alpha0*J0+Gamma*J0^2-K0

lies in `[0,Q'/2)`. Then the exact slope-block sum is

    S_u = L*(I-E)/2 + L*R_count.

**Proof.** Varying the slope adds `q*j/L` per parameter step. If L does
not divide j, its orbit has an even power-of-two length. A translated output
half contains exactly half of that orbit, so such an input contributes L/2.
For exceptional inputs j=L*J, the parameter variation vanishes modulo q.
Those J form the cyclic interval starting J0 of length E. Dividing their
output by L gives the displayed polynomial, and the output interval starts
at K0. There are L identical contributions for each exceptional input. QED.

All terms are nonnegative. Therefore this is a valid positive group-count
identity, including zero tests, for its stated fixed-geometry parameter
family. No cancellation of potentially negative witness weights is used.

Here Q'=2^(r+u) and Gamma=2^(2r-u)*beta. If `u<=floor(r/2)`, Gamma vanishes
modulo Q': **one ordinary affine floor-sum evaluates the entire slope block**
in polynomial time in r, for general a, arbitrary D, translated windows,
and arbitrary input length I. This avoids enumerating either the slopes
or the exceptional input digits.

For larger u there is still an exact dimension reduction. A quadratic with
modulus 2^K and coefficient divisible by 2^R is affine on each input class
modulo 2^(K-R). Decomposing these classes gives at most

    2^max(0,2u-r)

affine floor-sums for the residual count. Ordinary Euclidean floor-sum
reciprocity evaluates each in polynomial time. For u=r this returns the
numerical 2^r cost of an individual general-slope count; it is not a
polynomial-time individual evaluator.

An output condition on `F(j)-nu*j mod q` is handled by replacing alpha by
alpha-nu, provided nu is fixed across the slope block. An even nu preserves
the odd-slope permutation setting. This is a modular linear strip, not an
arbitrary curved cap.

## Why direct reciprocity does not solve an individual general slope

Write alpha=a+m*t, 0<=a<m. The exact unaveraged digit decomposition is

    C = sum_(l mod m) W_a(beta*l^2+t*l+floor((a*l+D)/m)),

where W_a(g) counts h in `[0,m/2)` with `(a*h+g) mod m<m/2`.
Each W_a is an affine floor-sum, but the carry depends on l and remains
correlated with the quadratic term. Dropping it is incorrect: at r=2,
alpha=3,beta=1,D=0 the actual answer is 5, whereas dropping the carry gives 6.

Applying Euclidean reciprocity separately to W_a produces variable lengths
depending on that quadratic/carry argument and generally changes the modulus
to a, which need not be a power of two. The complete dyadic square histogram
cannot then be substituted for the position-sensitive sum. The block
identity above succeeds by identifying the exceptional input subgroup
before that reciprocity, rather than discarding this correlation.

## Faithful actual inverse charts

Consider a fixed odd N modulo m^3 and an odd base u0 in `[1,m)`. Put

    v0=N/u0 mod m^3,
    alpha=-N/u0^2 mod m^2,
    beta=N/u0^3 mod m,
    D=floor(v0/m).

For x=u0+m*j, the inverse y=N/x modulo m^3 is exactly

    y=(v0 mod m)+m*((alpha*j+m*beta*j^2+D) mod m^2).

Thus the original coordinate half-box corresponds exactly to the half-window
count above. But the parameters are correlated: D is generally **not** a
multiple of m, and alpha, beta, D all come from the same N and u0.

The special slopes alpha=+/-1 modulo m only occur when
`u0^2=-/+N mod m`. For r>=3 each solvable condition selects four bases among
m/2 odd bases. The plus case requires N=7 modulo 8 and the minus case N=1
modulo 8; otherwise neither special family appears. Even these bases need
not satisfy D=m*c. Hence the closed special formula alone does not cover
the actual inverse family.

An origin shift j=j'+j0 changes all of

    alpha' = alpha+2m*beta*j0 mod q,
    D' = D+alpha*j0+m*beta*j0^2 mod q,
    input interval = [-j0,q/2-j0) mod q.

Beta and N remain fixed. The high slope parameter traverses one parity
class, but **neither the constant nor the window remains fixed**. The
abstract fixed-geometry block formula cannot be applied to this orbit as
though those changes were absent.

An exact witness is N=147053,r=3,u0=1, which gives
`(alpha,beta,D)=(19,5,13)` and count 18. Four faithful origins give:

| j0 | alpha' | D' | Input start | Count |
|---:|---:|---:|---:|---:|
| 0 | 19 | 13 | 0 | 18 |
| 1 | 35 | 8 | 63 | 18 |
| 2 | 51 | 19 | 62 | 18 |
| 3 | 3 | 46 | 61 | 18 |

Their sum is 72. Holding D=13 and the input interval fixed instead gives
18+14+16+16=64. The latter is a correctly evaluated **different** parameter
family, not a count of the same inverse witnesses.

## A faithful universal-polynomial normalization

There is a normalization that preserves N exactly. Set j=u0*z modulo q
and gamma=N/u0 modulo q. Then

    alpha*j+m*beta*j^2 = gamma*(-z+m*z^2) mod q.

Every chart has the same polynomial `-z+m*z^2`, but its two half windows become

    u0*z mod q < q/2,
    D+gamma*(-z+m*z^2) mod q < q/2,

with the invariant `u0*gamma=N mod q`. These are two coupled multiplicatively
wrapped windows. They cannot be replaced by ordinary translated intervals
without another exact transformation and cost bound. This is the concrete
faithful bridge left open, rather than an unspecified “general slope” gap.

## Validation, cost, and next step

`evaluator.py` is import-safe and uses exact integers only. With seed
202609070326 it passed 96 special-formula checks, the corresponding
opposite-slope checks, 125 general-slope block checks with translated half
windows, and 125 checks with arbitrary translated input lengths. Each block
was compared to the sum of its individually brute-counted slopes.

Sixteen actual inverse-chart cases at r=2..5 for N=147053 and 8464705853
checked every chart residue, a faithful origin shift, the universal-polynomial
normalization, and the complete parity orbit of faithful origins. The
decoupling witness is retained in `output.json`.

The final run took 0.30 seconds under a 25-second alarm, one process,
estimated memory below 128 MB. Preflight showed 72% available memory and
load 2.18. Source, parameters, exact counts, and log/output are retained.
No fitted running-time claim or external service is used.

The positive operation is polynomial-cost counting of large fixed-geometry
slope blocks, with nonnegative residual counts. The next research task is
an equally exact aggregation of the **coupled window orbit** produced by
actual inverse-chart changes. Averaging slopes while freezing that geometry,
or averaging N over lifts, does not supply the needed fixed-N count.
