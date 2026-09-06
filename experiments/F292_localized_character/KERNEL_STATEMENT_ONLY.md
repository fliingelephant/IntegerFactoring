# Statement-only reconstruction: one quadratic-Gauss/Cauchy kernel

Do not read the author derivation or other research records. The only permitted
external algorithmic dependency is the quadratic-sum theorem stated below.
Reconstruct the reduction, including zero/nonunit cases and bit costs.

## Definitions and output

Let m,D>=1, a,b,c,s be integers, and let

    e_q(x)=exp(2*pi*i*x/q), t0=e_D(s), ell=m/gcd(b,m),
    F(t)=sum_(z=0)^(m-1) e_m(a*z^2+c*z)/(1-t*e_m(b*z)).

F is regarded as a rational function, so removable values are interpreted
by continuation. Let J,p>=0 be desired output degree and absolute precision.
The local coordinate is rho=t/t0.

If t0^ell!=1, request the coefficients through degree J in

    F(t0*rho)=sum_(j=0)^J B_j*(rho-1)^j+O((rho-1)^(J+1)).

If t0^ell=1, request A and the coefficients through degree J in

    F(t0*rho)=A/(1-rho)+sum_(j=0)^J B_j*(rho-1)^j
                                      +O((rho-1)^(J+1)).

Claim: deterministic algorithms approximate every requested complex
coefficient to absolute error at most2^(-p) in bit complexity polynomial in
the combined ordinary binary length of (m,D,a,b,c,s), J, and p. This counts
precision/output degrees J,p themselves, not just their logarithms. No
factorization of m or D is supplied. No degree-D cyclotomic field is to be
materialized. The algorithm also decides exactly whether A=0 in the second
case, hence whether the potential pole is removable.

The following asserted identities may be reconstructed as part of the claim:

    G(a,c;m)=sum_(z=0)^(m-1) e_m(a*z^2+c*z),
    P(t)=sum_(n=0)^(ell-1) t^n*G(a,c+b*n;m),
    F(t)=P(t)/(1-t^ell).

At a potential pole, put P0=P(t0), P1=t0*P'(t0). The asserted first terms are

    A=P0/ell, B_0=((ell-1)*P0/2-P1)/ell.

An algorithm that explicitly sums all ell or m terms is not sufficient.
No cost claim is made here for sums over many distinct outer kernel indices
or for a product of several Cauchy denominators.

## Declared external dependency

Hiary, Annals of Mathematics174(2011),859--889, Theorem1.1, gives an explicit
algorithm for normalized sums

    K^(-j)*sum_(r=0)^K r^j*exp(2*pi*i*(alpha*r+beta*r^2)).

For any K>0, j>=0, real alpha,beta in[0,1), and0<epsilon<exp(-1), put
nu=(j+1)*log(K/epsilon). With absolute constants A1,A2,A3,kappa1,kappa2,
the error is at most A1*nu^kappa1*epsilon, the operation count at most
A2*nu^kappa2, and working numbers have at most A3*nu^2 bits. Elementary
operations include arithmetic, positive logarithms and complex exponentials.
Their usual arbitrary-precision bit costs are polynomial. The theorem has
no nonresonance condition. The K=0 one-term case is available directly.

Use this theorem as a declared dependency, not as a request to reproduce its
proof. Account for its error prefactor, normalization, and the precision
needed to supply the rational phases occurring in your reduction. Standard
complete quadratic Gauss identities and Euclidean gcd/Jacobi algorithms may
be derived or used explicitly with their hypotheses.
