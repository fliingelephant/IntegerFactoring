# Formal-group linearization with both windows retained

Status: exact identities and author-checked recurrences; recursive kernel
closure and a quasipolynomial bound are not established. New files use only
the `FORMAL_DESCENT` prefix. Independent root-identity checks are recorded
separately under `ROOT_GAUSS_WINDOW`.

## Coordinate change

Let m=2^r, q=m^2, r>=3. The operation

    z ⊕ w = z+w+mzw mod q

has inverse `g(z)=-z/(1+mz)=-z+mz^2 mod q`. Define

    ell(z)=z-(m/2)z^2 mod q,
    E(w)=(1+q/2)w+(m/2)w^2 mod q.

Expanding shows `ell(z⊕w)=ell(z)+ell(w)`. Also `ell(E(w))=w`: the remaining
terms are `(q/2)(w-w^3)` and a multiple of `(m/2)^3`, both zero modulo q
for r>=3. Thus ell is a permutation, E is its inverse, and
`ell(g(z))=-ell(z)`.

For a faithful inverse chart, write u=u0 and gamma=N/u modulo q. Its two
retained conditions become

    u*E(w) mod q < q/2,
    D+gamma*E(-w) mod q < q/2.

The invariant u*gamma=N modulo q is unchanged. With X=uE(w) and
Y=D+gamma E(-w), the weighted difference and sum are

    gamma*X-u*(Y-D)=2Nw mod q,
    gamma*X+u*(Y-D)=mNw^2 mod q.

These identities linearize the group inverse, not the two wrapped windows.

## Exact Gauss support and high-lift contraction

Put zeta=exp(2pi*i/q), omega=zeta^m, and let I_q be the half-window indicator.
Using Fourier coefficients `hat I_q(a)=sum_(x<q/2) zeta^(-a*x)`, its only
nonzero frequencies are zero and odd a, with

    hat I_q(0)=q/2,  hat I_q(a)=2/(1-zeta^(-a)) for odd a.

For odd a,b the complete w phase is

    (m/2)(a*u+b*gamma)w^2+(1+q/2)(a*u-b*gamma)w.

Its sum vanishes unless `a*u=b*gamma mod 2m`. On that support let
j=(a*u-b*gamma)/(2m). The sum is exactly

    m*G_m(b*gamma)*omega^(-j^2/(b*gamma)),

where `G_m(c)=sum_(x mod m) omega^(c*x^2)`. Mixed zero/odd frequencies vanish.
All denominators in the phase are units. This is the independently checked
root identity; no cut has been removed, because both Fourier window factors
remain outside the complete Gauss sum.

Set `d=gamma/u mod q`, and parametrize the surviving frequencies by

    b=b0+m*t, b0 odd mod m, t mod m,
    a=d*b+2m*z mod q, z mod m/2.

The Gauss phase is `omega^(-u^2*z^2/(b0*gamma))`. Its standard Gauss factor
also depends only on b0. For

    A0=zeta^(-d*b0-2m*z), B0=zeta^(-b0),

the t sum is

    m/((1-A0^m)(1-B0^m)) * sum_(i mod m) A0^i B0^((D-d*i) mod m).

The sign is `d*i+j=D mod m` with the stated negative-exponent Fourier
convention. A convention with positive denominator exponents changes this
sign accordingly. Both displayed denominators are nonzero.

Define the weighted floor polynomial

    F(n,M,a,b;X,Y)=sum_(i=0)^(n-1) X^i*Y^floor((a*i+b)/M).

The polynomial in the t sum equals

    B0^D * F(m,m,d,m-1-D; omega^(-2z),omega^(-b0)).

Its prefactor B0^D cancels the outer Fourier factor zeta^(b0*D). Thus after
the high-lift sum, **all remaining roots of unity have order m, not q**.
At this stage there are m/2 choices of b0 and m/2 of z, before further work.

## Summing z gives an exact retained-window kernel

Expand the floor polynomial temporarily in i. The z sum is half a complete
Gauss sum: the integrand has period m/2. Moreover

    G_m(c)*G_m(-u^2/c)=2m

for odd c,u. Completing its square gives the exact contraction

    C = sum_(i mod m) W_(-d,m)(Psi(i)),
    Psi(i)=beta*i^2+floor((D-d*i)/m) mod m,
    beta=gamma/u^2 mod m,

where W_(a,m)(h) counts `0<=x<m/2` with `(a*x+h) mod m<m/2`.
Equivalently,

    C=q/4+(4/m)*sum_(b odd mod m)
      [sum_(i mod m) omega^(b*Psi(i))]
      /((1-omega^(-d*b))*(1-omega^(-b))).

This keeps every boundary term and yields m affine-window counts at modulus
m. It is exactly the earlier carry-weighted digit kernel, now recovered by
the formal-group/Gauss/Cauchy route. It is not a bounded number of instances
of the original one-variable near-affine family: the reduced quadratic
coefficient beta is a unit, and the carry is still position-sensitive.

The full integers d,D matter. If d=d0+m*d1 and D=D0+m*D1, then

    Psi(i)=beta*i^2-d1*i+D1+floor((D0-d0*i)/m) mod m.

Discarding the high quotients would change the count.

## Exact Euclidean step and the new boundary moment

First, the **linear** weighted floor polynomial has a short rational
recurrence. Reduce a,b modulo M using

    F(n,M,a,b;X,Y)
      =Y^floor(b/M)*F(n,M,a mod M,b mod M;X*Y^floor(a/M),Y).

With 0<a<M, 0<=b<M, let `H=floor((a*(n-1)+b)/M)` and
`P_n(X)=(1-X^n)/(1-X)`. Then

    F(n,M,a,b;X,Y)=P_n(X)
      +(Y-1)/(1-X) *
        ( F(H,a,M,M-b+a-1;Y,X)-X^n*P_H(Y) ).

The modulus decreases by the Euclidean step. The formula is a polynomial
identity wherever its rational expressions are defined, with removable
limits at exceptional roots. Unrolling it gives O(log M) rational terms.
Successive prefactors telescope because the new second variable is the old
first variable. Each term has at most two binomial denominators in monomials
of the original X,Y.

The quadratic carry kernel requires more than this primitive. Let

    S(t)=sum_(i=0)^(t-1) omega^(A*i^2+B*i),
    H_quad=sum_(i=0)^(n-1) omega^(A*i^2+B*i)*Z^floor((a*i+b)/M),

again with reduced 0<a<M,0<=b<M. Exact summation by floor levels gives

    H_quad=Z^H*S(n)
       -(Z-1)*sum_(j=1)^H Z^(j-1)*S(ceil((M*j-b)/a)).

The new function is therefore a **floor-indexed incomplete Gauss moment**.
Complete Gauss sums at an odd or even modulus do not, by themselves,
evaluate its varying prefix lengths. The issue is retained boundaries,
not the appearance of an odd modulus in Euclidean reciprocity.

One can Fourier-expand each prefix S(t). Its boundary factor is
`(1-omega^(-h*t))/(1-omega^(-h))`, with the h=0 value interpreted as t.
Applying the linear floor recurrence to the resulting j sum leaves short
rational terms, but the complete Gauss modulus is still m and the boundary
phase must still be summed. Thus a smaller outer floor index is not yet a
halving of the full problem's bit-size resource.

## What kernel class a short decomposition actually produces

The high-lift approach makes this growth explicit. Insert the O(log m)-term
decomposition of F into the b0,z expression instead of expanding all i.
Away from poles, the terms are smaller-modulus sums of the form

    sum_(b odd mod m) sum_(z mod m/2)
      G_m(b*gamma)*omega^(-u^2*z^2/(b*gamma)+L(z,b))
      /product_j(1-omega^(-2p_j*z-q_j*b)),

where L is linear with known integer coefficients. In general there are
**up to three Cauchy denominators**, rather than the original two. Two come
from consecutive Euclidean rays; the remaining one is the nonvanishing
factor `1-omega^(-d*b)`. The common numerator Y-1 cancels the other original
window denominator. The initial full-period geometric term is handled
separately on its resonance set.

The two consecutive ray vectors are unimodular. For b odd, their denominator
zeros cannot occur simultaneously. A ray denominator can vanish only when
its b coefficient is even, in which case its z coefficient is odd and it
has exactly one zero modulo m/2. Therefore there are O(log m) resonance
families, not an unrecorded numerical tolerance problem.

Their removable limits introduce first derivatives. If a local term is
`N(epsilon)/(1-exp(p*epsilon))`, its finite part is

    N(0)/2-N'(0)/p.

The residues cancel in the full polynomial. Differentiating the other
binomial denominator can produce a **squared Cauchy denominator**. A proposed
closed recurrence must therefore include these first-moment/resonant kernels
or prove an additional cancellation. Substituting zero for an undefined
term is incorrect.

This identifies an explicit enlarged family: complete quadratic-Gauss/Cauchy
sums with three linear denominator factors, plus first-derivative resonance
terms. I have not proved that this family maps into a fixed-complexity family
under another square-root descent. In particular no recurrence
`T(n)<=poly(n)*T(n/2)` follows from merely naming these smaller-modulus sums.
The short rational terms are generally complex or signed. They are not
individually positive witness counts; only the fully recombined count has
the original interpretation.

## Exact checks and scope

`FORMAL_DESCENT.py` passed:

* 2112 logarithm/inverse checks and 192 group-law checks;
* 24 two-window counts compared to the retained m-term contraction;
* all 12 earlier actual charts with r>=3, including the count-18 example;
* 100 exact rational tests of the Euclidean generating-function recurrence;
* 32 exact quadratic boundary-moment identities represented in
  `Z[X]/(X^(m/2)+1)`.

At m=256 the four random contractions retained 157–163 distinct phases and
85–94 nonzero differences between opposite half-phase histogram entries.
This finite observation does not prove a lower bound, but it gives no
complete-histogram collapse of the carry term.

The final validation followed a resource read of 73% available memory and
load 3.37. It used one Python process, a 20-second alarm, estimated <128 MB,
and completed in about 0.12 seconds. Source, parameters, outputs and log are
retained. The independent ROOT_GAUSS_WINDOW packet validates the preceding
Gauss and high-lift identities separately.

The constructive result is an exact modulus-q to modulus-m descent with
all cuts and phases retained, and an explicit description of the new
incomplete-Gauss/three-denominator/resonant terms required by reciprocity.
It is not yet an efficient recursively closed evaluator or a factoring
algorithm.
