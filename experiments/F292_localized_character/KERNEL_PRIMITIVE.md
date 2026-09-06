# F292: a fast individual quadratic-Gauss/Cauchy primitive

**Outcome:** the stated individual kernel at a rational root of unity, including
its Laurent finite part, reduces to polynomially weighted quadratic sums. Hiary's
uniform theorem supplies polynomial bit complexity in the input size and desired
absolute precision. This does not evaluate the remaining outer geometry sum.

**Status:** author-derived reductions and exact finite checks, using a published
algorithmic theorem. No implementation of Hiary's fast algorithm or independent
reconstruction of the new reduction has been completed in this packet.

## Exact reduction, derived before literature

Let e_q(x)=exp(2*pi*i*x/q), m>=1, and a,c,b integers. The linear phase c
is retained because translations and cone formulas can produce it. Put

    F_m(t;a,c,b)=sum_{z mod m} e_m(a*z^2+c*z)/(1-t*e_m(b*z)),
    G(a,c;m)=sum_{z mod m} e_m(a*z^2+c*z),
    ell=m/gcd(b,m).

For |t|<1, expanding the geometric denominator and grouping its period gives

    F_m(t;a,c,b)=P(t)/(1-t^ell),
    P(t)=sum_{n=0}^{ell-1} t^n G(a,c+b*n;m).               (1)

Both sides are rational functions, so the identity extends off their poles.
No termwise approximation is involved.

Here is the complete reduction of the coefficients of P to an arithmetic
progression carrying one quadratic phase. Let

    d=gcd(a,m), q=m/d, g0=gcd(d,b), h=d/g0, a'=a/d.

If g0 does not divide c, every coefficient is zero. Otherwise let

    n0=-(c/g0)*(b/g0)^(-1) mod h,
    L(j)=(c+b*n0)/d+(b*h/d)*j.

For h=1 take n0=0. Only n=n0+h*j survives. When q=1 the surviving value
is m. Otherwise a' is a unit modulo q, and the values are as follows:

1. For q odd,

       G(a,c+b*(n0+h*j);m)
         =d*G(a',0;q)*e_q(-(4*a')^(-1)*L(j)^2).

2. For q=2Q with Q odd, the value is zero unless L(j) is odd. In the surviving
   case it is

       2*d*G(2*a',0;Q)*e_Q(-(8*a')^(-1)*L(j)^2).

   Interpret the phase as1 when Q=1. This follows by pairing z and z+Q,
   and then using the even representative2x for each pair.

3. For4 dividing q, the value is zero unless L(j) is even. In the surviving
   case it is

       d*G(a',0;q)*e_q(-a'^(-1)*(L(j)/2)^2).

   This is direct square completion.

The parity condition restricts j to at most one progression. Writing
j=j0+v*r, v in{1,2}, therefore turns P into

    C*t^n_start*sum_{r=0}^{J-1} t^(s*r)*e(alpha*r^2+beta*r), (2)

or zero. Here J<=m, s=h*v, n_start=n0+h*j0, alpha,beta are explicit rationals with
O(log m)-bit descriptions, and C is a complete Gauss amplitude times a root
of unity. These parameters use gcds and modular inverses, not factors of m.

Complete quadratic Gauss amplitudes are polynomial-bit computable. Separate
the power of two from the odd part by shifts and use CRT. For an odd unit
modulus Q, G(a,0;Q)=epsilon_Q*(a/Q)*sqrt(Q), where epsilon_Q is1 or i according
to Q modulo4, and the Jacobi symbol is computed by its Euclidean algorithm.
For a odd and k>=2,

    G(a,0;2^k)=2^(k/2)*(1+i^a)          if k is even;
    G(a,0;2^k)=2^((k+1)/2)*e_8(a)      if k is odd.

The small moduli and a=0 are handled directly. These formulas also give exact
zero tests after the gcd/parity reduction.

## Exact-root poles and their finite parts

Let t0^ell=1 and use the local coordinate rho=t/t0. Define

    P0=P(t0), P1=t0*P'(t0).

The Laurent expansion is

    F_m(t0*rho)=A/(1-rho)+B+O(rho-1),
    A=P0/ell,
    B=((ell-1)*P0/2-P1)/ell.                            (3)

Thus the finite part requires only degree0 and degree1 polynomially weighted
quadratic sums from(2). If A=0, B is the actual removable-pole value. There
is no division by a numerically tiny1-t^ell in this computation.

The residue itself is a single complete Gauss sum. Write t0=e_ell(s0),
g=m/ell, b'=b/g, and z0=-s0*(b')^(-1) mod ell. Then

    A=e_m(a*z0^2+c*z0)*G(a*ell,2*a*z0+c;g).              (4)

For ell=1 take z0=0. Indeed the pole residues are precisely z=z0+ell*j,
0<=j<g. Hence individual removability can be recognized exactly by the
complete Gauss gcd/parity rules. It need not be guessed from a small floating
residue. Cancellation among several different kernels still requires the
actual relation furnished by the geometry; it is not asserted here.

Finite parts depend on the common deformation coordinate. If the geometry
uses t=t0*rho^v with nonzero integer v, the pole coefficient becomes A/v and
the finite part becomes

    B+A*(v-1)/(2*v).                                    (5)

If it uses t=t0*exp(-v*x), the constant term in x is B+A/2, while the pole
term is A/(v*x). These corrections must be retained before combining terms.
If a coefficient Q(rho) also varies in the common deformation, set
Q0=Q(1), Q1=Q'(1). The finite part of Q(rho)*F_m(t0*rho^v) is

    Q0*(B+A*(v-1)/(2*v))-Q1*A/v.

In particular Q(rho)=Q0*rho^r contributes
Q0*(B+A*(v-1-2*r)/(2*v)). Substituting the resonant values into varying
prefactors before taking finite parts can lose this correction. Evaluating
the original combined polynomial before pole-bearing decomposition avoids
this convention issue.

The substitution z->-z gives the phase-sensitive identity

    F_m(t;a,c,b)+F_m(1/t;a,-c,b)=G(a,c;m).               (6)

For c=0 only, at t0=1 or-1 whenever t0 is a pole root, (3) simplifies to

    B=(G(a,0;m)-A)/2.                                   (7)

For c=0 and-1 not a pole root, F_m(-1)=G(a,0;m)/2. These particular values
require only complete Gauss sums. For general c and t0, the paired finite
parts satisfy B_c(t0)+B_(-c)(t0^(-1))=G(a,c;m)-A_c(t0). This does not halve
the individual finite part when c is nonzero.

## The actual published fast-sum scope

Hiary, Annals of Mathematics174(2011),859--889, Theorem1.1, treats

    T(K,j;alpha,beta)=K^(-j) sum_{r=0}^K r^j e(alpha*r+beta*r^2).

For all real alpha,beta in[0,1), j>=0, and epsilon<exp(-1), define
nu=(j+1)log(K/epsilon). The theorem gives error at most A1*nu^kappa1*epsilon,
at most A2*nu^kappa2 arithmetic operations, and at most A3*nu^2 bits per
number, with absolute constants. The stated elementary operations include
logarithms and exponentials. Their bit cost is polynomial at that precision.
The polynomial error prefactor is absorbed by tightening epsilon. There is
no nonresonance or Diophantine condition. Section4 includes polynomial linear
combinations; small quadratic phases have a separate Euler--Maclaurin branch.
[Primary theorem](https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n2-p03-p.pdf).

Kuznetsov's *Computing the truncated theta function via Mordell integral*,
Theorem2, gives the unweighted sum to absolute error epsilon in
O(log(n/epsilon)^3) arithmetic operations on O(log(n/epsilon))-bit numbers,
with O(log(n/epsilon)^2) memory. Its normalized recursion has new length at
most n/2. The weighted bounds used here come from Hiary's theorem; Kuznetsov's
stated Theorem2 is not being extended silently to all derivative orders.
[Primary paper](https://arxiv.org/abs/1306.4081).

Both full texts are cached. Citation keys are `hiary_2011_nearly` and
`kuznetsov_2015_computing`. The official fetch/render manifests and logs are in
`reference_theta_algorithms/SOURCE_MANIFEST.json`.

## Input precision and absolute-error accounting

At an exact rational root of unity t0, formula(2) has real rational phase
coefficients. Multiplication by t0 simply changes the linear coefficient.
For P1, the extra weight is n_start+s*r. Higher Taylor coefficients require
falling-factorial weights of the desired degree. Expanding them into powers
of r produces only polynomially many terms for polynomial degree. Their
coefficients have O(j*log m+j*log(j+1)) bits.

The normalization K^(-j) in Hiary's theorem must be undone. A target error
eta in sum r^j e(...) requires error eta/K^j in T. Consequently it adds
j*log K precision bits, rather than a factor K^j to the operation count.
Complete Gauss amplitudes, scalar weights and divisions in(3) likewise add
only polynomially many precision bits. K=0 is a direct one-term case.

Input-phase precision is also explicit: because0<=(r/K)^j<=1, the absolute
derivatives of T with respect to alpha and beta are at most4*pi*K^2 and
4*pi*K^3 for K>=1. Hence phase input error eta/(8*pi*K^3), tightened by the
coefficient norm of the final combination, suffices. The rational phase
descriptions here can be computed exactly, or rounded to that many bits.
No tiny distance to a rational resonance appears in this bound.

It follows that the Laurent finite part, and any specified fixed or
polynomial-degree collection of Taylor coefficients, is computable with
polynomial bit cost in log m, the degree, coefficient/input bit lengths,
and log(1/eta). This is a valid individual primitive.
For a rational root of unity of order D that is not a pole, the denominator
in(1) has magnitude at least4/D. Thus its additional precision cost is
O(log D), already part of the input size.

## Interior t and uniformity near poles

For arbitrary t with |t|<1, put Delta=|1-t^ell|. Direct use of(1) requires
the numerator to absolute error O(eta*Delta). Thus the cost includes
log(1/Delta), as well as the bit length of the description of t. This is real
conditioning at a genuine pole, not a resonance exclusion in the theta
algorithm. A claim uniform in arbitrary near-pole t using only log m and
log(1/eta) would omit this input/output precision parameter.

The damping in(2) does not create a length-dependent obstruction. Set
lambda=-s*log|t|. Truncate r when lambda*r exceeds
B=O(log(m/(eta*Delta))). The discarded tail is bounded by its number of
terms times its maximum magnitude. On the retained range lambda*r<=B,
Taylor approximation of exp(-lambda*r) of degree O(B) suffices; the
Lagrange remainder is bounded by B^(D+1)/(D+1)!. This reduces the damped
sum to polynomially weighted real-phase quadratic sums. Coefficient norms
have logarithm O(B), which is included in the error budget.

For a removable pole, or a combination whose pole cancellation is already
proved, use local regular Taylor coefficients instead of subtracting large
values. Other distinct pole roots are separated by at least4/ell. For
|rho-1|<=1/ell, the regular-part coefficients of degree j are bounded by
m*(ell/4)^(j+1). Therefore O(log(m/eta)) coefficients give a controlled
local approximation; their polynomial-weight evaluation is covered above.
This yields stability near the removed pole without an inverse-distance
cost. Genuine uncancelled pole terms still require their own precision.

## Exact checks and the surviving outer cost

`quadratic_cauchy_kernel.py` is a small Sage certificate, not an implementation
of the fast theta algorithm. The exact check totals are retained in its JSON.
The final totals are447 Gauss reductions,43 interior kernels and117 finite
parts; the run took0.268seconds after Sage initialization and used248.4MiB.
All equalities are exact in cyclotomic fields. The initial39 kernels include
odd, even, nonunit and zero coefficients. Four further nonzero-c controls
check the affine progression reduction, finite parts and paired-c symmetry.
The nonzero removable example(m,a,c,b,t0)=(8,1,0,4,1) has value2*zeta_8.

The script has a30-second timeout. The estimated peak was below256MiB; the
measured peak and runtime are retained in its JSON. The resource snapshot
reported load2.88/2.49/2.19,73% free memory and no swap; approved process
inspection showed one Apple process using a core. Source, JSON and log are
retained beside this report.

If a remaining expression has B0 distinct outer indices, evaluating these
kernels separately still costs B0 times their polynomial bit cost, with
additional accuracy according to the outer coefficient norm. Nothing in
Hiary's theorem, Kuznetsov's theorem, or the reduction above contracts B0.
The primitive removes the individual quadratic/Cauchy-kernel obligation;
it does not remove the outer summation obligation.
