# F204 candidate — the beta-two q-product norm loses every odd target coefficient

## Status and scope

This is a frozen proof-only candidate awaiting hostile audit. It concerns the
fixed `m=2` coefficient in F203. It proves a boundary for four named
fast-forward mechanisms:

1. the binary q-product norm and its logarithmic derivative;
2. scalar modular monomials in the binary orbit `P(q),P(-q)`;
3. linear base-two Mahler equations for the target Lambert series; and
4. root-of-unity norms at a fixed odd prime.

It supplies no coefficient evaluator and no factoring algorithm. It is not a
lower bound against arbitrary algorithms, nonlinear or nonholomorphic
functional equations, vector-valued modular objects, QP-growing section state,
or an adaptive one-child integer decoder.

Let `chi` be the primitive character modulo four,

\[
 \chi(d)=
 \begin{cases}
  0,&2\mid d,\\
  1,&d\equiv1\pmod4,\\
  -1,&d\equiv3\pmod4.
 \end{cases}
\]

Define

\[
 A(n)=\sum_{d\mid n}d\chi(d),
 \qquad
 L(q)=\sum_{n\geq1}A(n)q^n,
\]

and, for `|q|<1`,

\[
 P(q)=\frac{(q;q^4)_\infty}{(q^3;q^4)_\infty}
 =\prod_{a\geq1}(1-q^a)^{\chi(a)}.
\]

For the balanced distinct-odd-semiprime promise of F203, exact evaluation of
`A(N)` factors `N`. F204 studies only proposed ways to fast-forward this
coefficient.

## 1. Exact binary norm and complete odd-coefficient freedom

In the formal power-series ring over the rationals,

\[
 \boxed{L(q)=-q\frac{d}{dq}\log P(q)}
\]

and

\[
 \boxed{P(q)P(-q)=P(q^2).}
\]

Consequently,

\[
 \boxed{L(q)+L(-q)=2L(q^2),}
\]

which is exactly the elementary relation

\[
 \boxed{A(2n)=A(n).}
\]

This norm has no hidden constraint at an odd index. More generally, let `R`
be any commutative rational algebra and let
`G(q)` belong to `1+qR[[q]]`. Write

\[
 \log G(q)=\sum_{n\geq1}g_nq^n.
\]

Then

\[
 G(q)G(-q)=G(q^2)
\]

if and only if

\[
 \boxed{2g_{2n}=g_n\quad(n\geq1).}
\]

Every coefficient `g_r` with odd `r` is arbitrary. Once those odd
coefficients are chosen, the relation uniquely sets

\[
 g_{2^vr}=2^{-v}g_r
 \qquad(r\text{ odd},\ v\geq0).
\]

Thus even the complete infinite family of iterated binary norm equations
contains no equation for the target logarithmic coefficient at an odd `N`.

## 2. Binary-orbit scalar modularity boundary

Put `q=exp(2 pi i tau)`. For integers `a,b` and a fixed real `alpha`, define

\[
 F_{a,b,\alpha}(\tau)
 =e^{2\pi i\alpha\tau}P(q)^aP(-q)^b.
\]

The following conclusion uses a precise scalar hypothesis. Suppose
`F_{a,b,alpha}` is a nonzero scalar meromorphic modular form of one fixed real
weight `k`, with a multiplier system, on a finite-index subgroup of
`SL_2(Z)`, and suppose it has the usual meromorphic Fourier expansion after a
scaling matrix at every rational cusp. Then

\[
 \boxed{a=b.}
\]

In particular, `P(q)` itself is not such a scalar modular form of any weight.
The conclusion also applies to scalar generalized-eta or Siegel-unit
identifications satisfying these ordinary cusp hypotheses.

On the other hand,

\[
 -q\frac{d}{dq}\log\bigl(P(q)^aP(-q)^b\bigr)
 =aL(q)+bL(-q).
\]

For odd `N`, its `q^N` coefficient is

\[
 \boxed{(a-b)A(N).}
\]

Therefore every binary-orbit monomial that retains the odd target coefficient
(`a != b`) fails the stated scalar modularity hypothesis. The only monomials
that survive this necessary cusp test (`a=b`) annihilate every odd target
coefficient. The theorem does not claim that the surviving monomials are
modular.

## 3. No linear base-two Mahler equation

There is no formal Laurent-series identity in `Q((q))` of the form

\[
 R_{-1}(q)+\sum_{i=0}^{s}R_i(q)L(q^{2^i})=0,
 \qquad R_i(q)\in\mathbb Q(q),
\]

in which at least one `R_i` with `i >= 0` is nonzero. Thus `L` satisfies no
homogeneous or inhomogeneous linear base-two Mahler equation over `Q(q)`.

The obstruction is explicit. Modulo two,

\[
 \boxed{A(n)\equiv1\pmod2
 \iff \operatorname{oddpart}(n)\text{ is a square}.}
\]

This binary sequence has an infinite two-kernel and is not two-automatic.
Primitive integral reduction of any claimed Mahler equation would instead
make its generating series algebraic over `F_2(q)`; Christol's theorem would
then make the sequence two-automatic, a contradiction.

This conclusion is limited to linear Mahler equations with a fixed finite
number of iterates and rational-function coefficients. It says nothing about
arbitrary nonlinear relations, QP-growing systems, or algorithms that do not
arise from such an equation.

## 4. Odd-prime root norms give only the local Euler recurrence

Let `ell` be an odd prime, let `zeta` be a primitive `ell`-th root of unity,
and put

\[
 \epsilon=\chi(\ell)\in\{+1,-1\}.
\]

Then

\[
 \boxed{
 \prod_{j=0}^{\ell-1}P(\zeta^jq)
 =\frac{P(q^\ell)^{1+\ell\epsilon}}
        {P(q^{\ell^2})^\epsilon}.}
\]

Logarithmic differentiation gives

\[
 \boxed{
 A(\ell k)
 =(1+\ell\epsilon)A(k)
 -\epsilon\ell\,\mathbf1_{\ell\mid k}A(k/\ell).}
\]

For a target `N`, a fixed public `ell` contracts to `A(N/ell)` only when
`ell` divides `N`, in which case `gcd(ell,N)` already factors `N`. If
`ell` does not divide `N`, the norm only relates `A(N)` to the larger
coefficient `A(ell N)`.

## 5. Exact boundary

The binary norm is an exact parity filter. It does not determine an odd
remote coefficient. Scalar modularization inside the displayed binary
monomial orbit either fails or deletes that coefficient. A fixed linear
binary Mahler system does not exist. Fixed odd-prime root norms reproduce the
ordinary local divisor-sum recurrence and give no hidden-factor contraction.

This is same-node information loss, not a recursion-depth objection. If a
future construction supplies one strictly smaller recursive child and QP
local work, the valid recurrence remains

\[
 T(n)\leq T(n-1)+\operatorname{QP}(n),
\]

which is numerical QP. F204 proves only that the named q-product mechanisms
do not supply that child or the missing odd coefficient.
