# F303: global mixed moments through two base-M digits

**Family:** route:F31

**Evaluator simplification:** `CLOSED_FORM.md` proves direct off-diagonal
and diagonal formulas using only universal unit power sums and the unit
product. These replace the logarithmic construction for the actual M^2
evaluator. The full ratio below is retained as the structural tool for
higher-precision corrections.

**Outcome:** a deterministic polynomial-bit procedure computes every fixed
mixed moment modulo M^2, globally over the original canonical inverse graph.
The next precision has an exact reusable correction in weighted quadratic
carry moments. Those corrections are not yet computed efficiently.

**Status:** author-derived proofs and exact finite certificates, independent
reconstruction pending. No Archimedean moment approximation, ordinary global
Cauchy-resolvent evaluator, or factoring algorithm is established.

F303 was checked unused. The candidate was stated before literature:
combine an exact carry lift with a precision-aware input Mahler expansion.
The product-ratio construction below emerged during that derivation. F292's
Cochrane identity, F293's input sensitivity and F302's signed-moment lift
are relevant priors; none is used as a general obstruction.

## Definitions and the full weighted-carry identity

Let M=2^k with k>=3 and let N be any positive odd integer. Use N modulo M
only for the canonical inverse; retain the full N in the carry definition.
For each canonical odd unit0<u<M define

    v_u=N/u mod M, 0<v_u<M,
    q_u=(u*v_u-N)/M in Z,
    S_ab=sum_u u^a*v_u^b,
    U_j=sum_u u^j, P_M=product_u u,
    Q_(j,s)=sum_u u^j*q_u^s.

Inverse powers in U_j for j<0 are2-adic rational values with odd
denominators. The q_u are ordinary integer carries of the canonical product.
Their values and weights are not replaced by p-adic inverse lifts.
Replacing N by N-cM leaves S_ab unchanged but increases Q_(j,1) by c*U_j.
Thus a weighted-carry output for the full input cannot silently use only
N modulo M. The independent statement-only construction retains the needed
N modulo M^2 when computing Q_(j,1) modulo M.

Because v_u permutes the canonical unit set, the exact rational-function
identity is

    R(z)=P_M*product_u(z+u)/product_u(N+z*u)
        =product_u(1+M*q_u/(N+z*u)).                    (1)

This retains every weighted carry. As a formal series in z, its coefficients
are2-adic integral, R=1 mod M, and its2-adic logarithm converges
coefficientwise. Define

    L_j=(-1)^j*N^(j+1)*[z^j]log(R(z))/M.

Expanding the logarithm gives the exact2-adic identity

    L_j=sum_{s>=1}(-1)^(s+1)*binom(j+s-1,j)/s
                     *M^(s-1)*N^(1-s)*Q_(j,s).         (2)

For j=0 interpret the binomial factor as1. At each requested precision
only finitely many s survive. This is a reusable correction family, not
an assertion that its members are already evaluated.

The ratio in(1) is an auxiliary product identity. It is not the ordinary
global Cauchy resolvent. Its full enormous numerator and denominator are
not constructed; the needed logarithmic coefficients have the compact
formulas below.

## The accessible logarithmic coefficients

The left side of(1) gives

    L_0=N*log(P_M^2*N^(-phi(M)))/M,
    L_j=(N*U_j-N^(j+1)*U_(-j))/(j*M), j>=1.             (3)

The unit product and power sums in these expressions have the explicit
polynomial-bit algorithm in UNIT_PRODUCTS.md. Thus L_j modulo M^2 is
computable in polynomial bit cost in k and j, without enumerating u or v_u.

For L_0, the ratio P_M^2*N^(-phi(M)) lies in1+M Z_2. If its residue is1+w
modulo M^3, then log(1+w)=w-w^2/2 modulo M^3; terms of order at least3
vanish at this precision. Division by M produces L_0 modulo M^2.

For j>=1, compute the numerator of(3) modulo2^(3k+v_2(j)). It is divisible
by2^(k+v_2(j)); divide by that power of two exactly and invert the odd part
of j modulo M^2. The v_2(j) guard bits cannot be discarded. All quantities
remain polynomial-bit. Fixed small M are handled directly.

## A parity lemma needed by the precision argument

Pair u with M-u. Its inverse pairs v with M-v, so

    q_(M-u)=q_u+M-u-v_u=q_u mod2.

Both weights u^j and(M-u)^j are odd. Therefore Q_(j,1) and Q_(j,2) are
even, for every j>=0. In particular the second term of(2), which contains
M/2 rather than M, still vanishes modulo M after summation.

Keeping two carry orders in(2) gives

    L_j=Q_(j,1)-M*(j+1)*Q_(j,2)/(2N) mod M^2,          (4)
    L_j=Q_(j,1) mod M.                                (5)

For k>=3 every s>=3 term in(2) is divisible by M^2: its valuation is at
least(s-1)k-v_2(s). This proves(4) with the denominator losses counted.

## Mixed moments modulo M^2 and the third-digit correction

Use S_ab=S_ba to assume a>=b>=1, and put j=a-b. Since
u^a*v_u^b=u^j*(N+M*q_u)^b, binomial expansion and(4) give

    S_ab=N^b*U_j+b*M*N^(b-1)*L_j
           +(a*b*M^2/2)*N^(b-2)*Q_(j,2) mod M^3.       (6)

The coefficient follows from
b*(j+1)/2+binom(b,2)=b*(j+b)/2=ab/2. Because Q_(j,2) is even, the last
term vanishes modulo M^2. Thus

    S_ab=N^b*U_j+b*M*N^(b-1)*L_j mod M^2               (7)

is a constructive global evaluator. Moments with an exponent zero are
ordinary unit power sums. The operation count is polynomial in k and the
requested degree bound, so a polynomial-degree bank is still polynomial-bit.

For the third digit, when ab is odd, the required quadratic carry datum is
Q_(j,2) modulo2M, equivalently Q_(j,2)/2 modulo M. Merely knowing it modulo M
loses a bit. Higher precisions similarly retain the explicit higher-s
corrections in(2). No fast constructor for those banks is supplied.

## S11 in product form and its exact next correction

Let Q1=Q_(0,1), Q2=Q_(0,2), and E2=(Q1^2-Q2)/2. The exact product equality
P_M^2=product_u(N+M*q_u) gives, modulo M^3,

    K=(N^(1-phi(M))*P_M^2-N)/M
      =Q1+(M/N)*E2 mod M^2.

The division is performed with the stated modular precision. Hence

    S11=phi(M)*N+M*K-M^2*N^(-1)*E2 mod M^3.             (8)

K is accessible by the unit-product algorithm. E2 modulo M is the missing
correction. Since Q1 modulo M is known and even, E2 is equivalently an
accessible term minus Q2/2 modulo M. For S11, its range0<=S11<M^3/2 means
that knowing the full residue modulo M^3 would determine it exactly.

Reflection also gives the exact ordinary identity

    S12=M*S11-M^2*(M^2+2)/24.

Thus this degree-three moment contains no additional information beyond S11
and universal power sums. It was checked independently in the pilot.

## Why the two digits are not an Archimedean approximation

The bound S_ab<M^(a+b+1)/2 fixes the relevant real scale. A congruence modulo
M^2 provides low digits, not a bound on omitted high digits. For example,

    M=4096, N=1,
    S11=8278714368,
    S11 mod M^2=7546880.

After division by M^3 these are approximately0.12047115 and0.00010982.
The residue is not a useful real approximation to the normalized moment.
For k>=3, Cochrane(N,M)=S11/M^2-M/8, so this computation fixes the Cochrane
fractional part while leaving its position-sensitive integer part unresolved.

The logarithm in(2) is also specifically2-adic. Ratios M*q_u/N can be large
in the real metric, so its series must not be reused as a convergent ordinary
Taylor expansion for the resolvent. No claim about F301's required absolute
error follows from(7).

An exact high-input-block average illustrates a further precision issue.
For a power of two R,

    sum_{t=0}^{R-1} S11(M*R,N+M*t)
       =R^2*S11(M,N)+M^3*R^2*(R^2-1)/8.               (9)

This follows by summing the two independent coordinate lifts of each pair
modulo M. Even if the left side were available cheaply modulo(MR)^2,
subtracting the correction and dividing by R^2 gives only S11 modulo M^2
again. The larger modulus alone does not gain a base-M digit in this
averaging procedure. Eight exact checks of(9) are retained.

## Input-Mahler experiment on the unresolved correction

The pilot computes the exact finite-difference coefficients at N=1+2t for
E2 modulo M, Q2 modulo2M, and the normalized residual

    H_k(t)=(S11-[phi(M)*N+M*K]_(mod M^3))/M^2 mod M
          =-N^(-1)*E2 mod M.

Thus the accessible first-moment contribution has already been subtracted.
For each modulus, up to65 consecutive odd inputs were used. These are exact
Mahler/Newton coefficients on that finite input set, not fitted recurrences.

At M=4096 the order64 coefficients are

    Delta^64 E2(0)=2398 mod4096, v_2=1;
    Delta^64 H_k(0)=1954 mod4096, v_2=1.

Consequently truncation at order63 fails even modulo4 at the input t=64.
This is a finite separating test for that cutoff, not a lower bound against
polynomial-degree or another aggregate representation. At the preceding
modulus M=2048 the order64 valuation of E2 is9, showing that the favorable
single-level observation cannot simply be carried to the next precision.
No sufficient uniform tail bound or correction evaluator has emerged.

## Evidence, cost and comparison status

`moment_precision.py` verifies464 small odd-input cases through M=4096.
There are3248 mixed-moment congruence checks modulo M^2,3248 corrected
identities modulo M^3, and2320 weighted-carry checks. The universal products
and positive/inverse power sums are separately compared with direct small
enumeration. Large-bit runs at k=32,64,128 use no unit enumeration; details
and operand sizes are in UNIT_PRODUCTS.md and the JSON output.

The named pilot has a60-second alarm and estimated peak below512MiB. It took
about1.14seconds and used19.1MiB. Preflight reported load2.20/2.20/2.22,
68% available memory and no swap; approved process inspection showed one
Apple process using a core. Source, complete coefficient arrays, JSON and
log are retained. No shared metadata or commit was changed.

The known Cochrane source in F292 concerns the same S11 statistic, and a
focused primary search found related Wilson/Newton quotient congruences.
SOURCE_LEADS.md now records the focused comparison, including Andreica's
published non-enumerative power-sum/Newton algorithm for the odd product.
Neither that primitive nor the mixed-moment identities carries an external
novelty claim.

The bounded progress is a genuine global constructor modulo M^2, plus the
explicit weighted quadratic-carry correction for the next digit. Ordinary
global moment accuracy and the global resolvent remain uncomputed.
