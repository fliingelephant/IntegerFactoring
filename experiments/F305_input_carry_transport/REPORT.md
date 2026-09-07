# F305: input transport to one fixed linear-carry measure

**Family:** route:F31

**Outcome:** changing N can be expressed through one fixed N=1 carry
measure and polynomial-time reciprocal-floor marginals. The transformed
unknown is linear in the carry, with a sharp floor weight. Its evaluation
is not established. A dyadic reflection exposes a smaller graph together
with an additional carry-bit term and retained precision.

**Status:** author-derived exact identities and small exact checks. No
quasipolynomial E2 evaluator, rectangle counter or external novelty claim
is made. No shared ledgers or commit were changed.

F305 was checked unused. The closest prior work is F303's global low-digit
moment constructor, F302's signed moment lift, and F304's guarded digit
filters. The operation here is input transport on a fixed inverse graph,
not the F303 high-input-lift average or exponent differentiation.

## Fix the reference graph once

Let M=2^k, k>=3. Reparametrize the units by canonical odd0<w<M and set

    u=w^(-1) mod M, 0<u<M,
    q1(w)=(u*w-1)/M,
    mu_M(w)=u*q1(w),
    f_(N,d)(w)=floor((N*w-d)/M).

For canonical odd0<N<M and0<=c,d<=M, v_N=N*w mod M. The output-domain shift is
y_d=v_N+M*1_(v_N<d), and exactly

    y_d=N*w-M*f_(N,d)(w).

With no input-domain shift,

    q_(0,d)=(u*y_d-N)/M=N*q1-u*f_(N,d).                 (1)

Thus all N use the same reference carry q1 and measure mu_M. Define the
unresolved linear-carry floor transform

    T_0(N,d)=sum_w mu_M(w)*f_(N,d)(w) mod M.            (2)

This is a sharper family than an unspecified new moment oracle: its
underlying measure is fixed at N=1, and N,d occur only in a linear floor.
The number of its sharp crossings still matters.

## A genuinely computable marginal

Since u*w=1+M*q1,

    u^2=w^(-2) mod2M.

Consequently

    R2(N,d)=sum_w u^2*f_(N,d)(w)^2 mod2M
           =sum_w w^(-2)*f_(N,d)(w)^2 mod2M

is computed without the inverse graph. So is

    R1*(N,d)=sum_w w^(-1)*f_(N,d)(w) mod2M.

FLOOR_MARGINALS.md derives and implements the polynomial-degree reciprocal
expansion and a degree-preserving Euclidean floor recurrence. These are
actual polynomial-bit constructions, not calls to a carry oracle.

For the canonical domain d=0, Q2(N)=sum q_(0,0)^2 is even. Equation(1)
then gives

    Q2(N)/2=N^2*Q2(1)/2-N*T_0(N,0)+R2(N,0)/2 mod M.   (3)

The same parity and(1) show that R2(N,0) is even here. This statement is
not extended to arbitrary shifted domains.

Let H(N)=sum q_(0,0) mod M, available from F303, and E2(N) be the second
elementary symmetric carry statistic. Then

    E2(N)=N^2*E2(1)+N*T_0(N,0)
             +(H(N)^2-N^2*H(1)^2-R2(N,0))/2 mod M.     (4)

The squares of the even H values are unambiguous after division by2,
given H modulo M. R2 must be retained modulo2M. Subtracting(4) for any two
odd inputs, including N and N+2^s when both are in the canonical range,
gives an exact input-difference equation with computable marginals and
two values of the same fixed-measure transform. It introduces no varying
inverse graph or unrelated modulus family.

The reference E2(1) is not being treated as free advice. It remains an
unknown global scalar at each modulus. The transform in(2) also remains
uncomputed for general inputs, so(4) is a reduction, not an E2 algorithm.

FULL_INPUT.md gives the exact computable correction from the canonical
input to every positive odd full N. The correction cancels from the
rectangle mixed contrast, but individual B values do change.

## Shifted domains: use binomial carries, not Q2/2

For an input shift c set

    alpha_c(w)=1_(u<c), x_c=u+M*alpha_c,
    q_c(w)=(x_c*w-1)/M=q1+w*alpha_c,
    mu_c=x_c*q_c=mu_M+alpha_c mod M,
    T_c(N,d)=sum_w mu_c*f_(N,d) mod M,
    H_c=sum_w q_c mod M,
    B_c0(1)=sum_w binom(q_c,2) mod M.

The first-carry marginal is computable:

    H_c=H_0+sum_{u odd<c}u^(-1) mod M.

H_0 comes from F303's unit product, and the reciprocal prefix uses the
same bounded-degree progression expansion as the other marginals.

The full shifted carry is

    q_cd=N*q_c-x_c*f_(N,d).

Define B_cd(N)=sum binom(q_cd,2), the root's integer-valued window target.
The exact transport is

    B_cd(N)=N^2*B_c0(1)+binom(N,2)*H_c
      +(R2(N,d)+R1*(N,d))/2
      +(M/2-N)*T_c(N,d) mod M.                         (5)

Here is the normalization behind the coefficient M/2-N. We have
x_c^2=w^(-2) modulo2M, but

    x_c=w^(-1)+M*q_c*w^(-1) mod2M,
    sum x_c*f=R1*+M*T_c mod2M.

Expanding binom(N*q_c-x_c*f,2) and substituting these relations proves(5).
The sum R2+R1* is always even: modulo2 its summands are f^2+f. Its division
by2 is therefore performed from a residue modulo2M. Neither shifted Q2
nor shifted H_c is assumed even. The pilot includes M=8,N=1,c=2,d=0,
where shifted Q2 is odd.

The c-only terms in(5) and the d-only marginals cancel in a mixed contrast.
Since mu_c-mu_0=1_(u<c) and
f_(N,d)-f_(N,0)=-1_(v_N<d),

    Delta_c Delta_d T_c=-C(c,d),
    Delta_c Delta_d B_cd=(N-M/2)*C(c,d) mod M.          (6)

This agrees with the root's direct rectangle bridge. It also states the
limitation clearly: the computable R marginals cancel in that contrast;
they do not supply the missing rectangle count. The new inverse-window
floor term in T_c-T_0 is not assumed computable.

## What is already known about the fixed measure

Every bounded-degree polynomial moment of mu_M modulo M is accessible
from F303. For r>=1,

    sum_w w^r*mu_M(w)=Q_(r-1,1)(M,1) mod M,

because u*w=1 mod M and q1 is symmetric under u/w interchange. For r=0
the answer is Q_(1,1)(M,1). The shifted measure adds only reciprocal-prefix
power sums. This gives a polynomial-moment functional, not a justified
rule for integrating a sharp floor or an integer-valued circuit against it.
No low-degree approximation of that floor has been assumed.

The special input N=M-1 has f=w-1, hence
T_0(M-1,0)=Q_(0,1)(M,1)-Q_(1,1)(M,1) modulo M. This is an actual fast
member of the family. For N=1, variable d instead gives the unresolved
prefix transform -sum_(w<d)mu_M(w).

## A dyadic reflection and its surviving correction

For d=0 let L=M/2 and f=f_(N,0). Full complementation gives

    mu_M(w)+mu_M(M-w)=u^2+1 mod M,
    f(M-w)=N-1-f(w).

Therefore

    T_0(N,0)=Gamma_N
          +2*sum_(w odd<L) mu_M(w)*(f(w)-(N-1)/2) mod M,

where the computable marginal is

    Gamma_N=sum_(w odd<L)(w^(-2)+1)*(N-1-f(w)) mod M.

To express the remaining measure on the genuinely smaller inverse graph,
put a=w^(-1) mod L, q_L=(a*w-1)/L and epsilon_w=q_L mod2. Exact lifting
gives u=a+L*epsilon_w and

    2*mu_M(w)=mu_L(w)+(L+1)*epsilon_w mod M.

Thus

    T_0(N,0)=Gamma_N+sum_(w odd<L)
       [mu_L(w)+(L+1)*epsilon_w]*(f(w)-(N-1)/2) mod M.   (7)

The graph modulus halves, but the output precision remains M and the
floor denominator is still M. A carry-bit weighted floor family appears.
There is no proved recursively closed total-state bound for those two
unknown terms. This is more precise than counting their pointwise
discontinuities as an obstruction.

The correction is nonzero on an actual aggregate: at M=16,N=3,
Gamma=14, the smaller-graph carry term is14, and the new indicator term
is14 modulo16. Their total is T=10. Omitting the indicator gives12.
This refutes only that omission, not another aggregate evaluator.

## Exact evidence and resource accounting

The single named pilot, `input_transport.py`, retains source, exact JSON
and logs. It checks11352 pointwise shifted transports,150 shifted binomial
identities,450 uniform marginal values, and25 reflection identities. It
also checks the canonical E2 formula(4) and shifted first-carry marginals.
All arithmetic is integer or exact Fraction arithmetic.

The fast marginal routine was exercised at M=2^24 and2^32 with zero unit
enumeration. Its largest case used15442 memoized Euclidean states,
degree18 and567-bit returned integers, taking about0.36seconds. The full
pilot took0.507seconds and used22.7MiB, under its30-second alarm and256MiB
estimate. Preflight reported load1.98/2.10/2.11,71% available memory and
no swap; approved process inspection showed one Apple process using a core.

The computable marginal has a proved polynomial state bound. The fixed
carry-measure transform and its smaller-graph correction do not yet have
one. No claim follows about arbitrary E2, shifted binomial carries, or
factorization. No further round is started by this bounded report.
