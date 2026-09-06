# F151 V2 candidate — large-order preprocessing certifies a clean short window and isolates one torus splice

## Status

This is a proof-only candidate. It uses the 2026 large-order theorem of
Harvey and Hittmeir as a black box, then proves elementary consequences for
the present source grammar. V1 failed its hostile audit because it called
carry effects the only remaining progress source. V2 removes that
unrestricted conclusion. It has not passed a fresh hostile audit or an
independent blind reconstruction. It is not a factoring algorithm.

The closest repository results are P55, P85, P132, and P133. P55 already
uses Jacobi-minus-one norm-one tori and exposes the exact signed factor gap.
P85 blocks generic fixed quasipolynomial word menus. P132 and P133 show that
generic finite-algebra and local-matroid probes remain insufficient at the
quasipolynomial scale. F151 tests two concrete suggestions from the new
literature: add a certified high-order source, and splice it into the P55
Jacobi-torus source.

Write

\[
n=\lceil\log_2(N+1)\rceil.
\]

Let

\[
4\le B<N-1,
\qquad
B=2^{(\log n)^{O(1)}}.
\tag{1}
\]

## Theorem 1 — factor or large order in every prime component

There is a deterministic quasipolynomial procedure that returns a proper
factor of `N`, or a unit `alpha` such that

\[
\boxed{
\operatorname{ord}_r(\alpha)>B
\quad\text{for every rational prime }r\mid N.
}
\tag{2}
\]

The procedure first invokes Harvey--Hittmeir with target `B`. If that call
does not factor `N`, it returns a unit with
`ord_N(alpha)>B`. The procedure then tests

\[
\gcd(\alpha^e-1,N),
\qquad 1\le e\le B.
\tag{3}
\]

If no proper gcd occurs, (2) holds. The extra scan is quasipolynomial.

This is stronger than a certified large global order. It rules out a short
order in every hidden prime component. It does not establish or exclude
factor correlation outside the explicit scan (3).

## Theorem 2 — the certified short power bank has no listed local collision

Assume the no-factor branch of Theorem 1. For

\[
1\le e\le\lfloor B/4\rfloor,
\qquad
c_e=[\alpha^e]_N,
\qquad
w_e=\iota_N(c_e),
\tag{4}
\]

all of the following gcds are one for distinct eligible `e,f`:

\[
\gcd(c_e-c_f,N),
\quad
\gcd(c_e+c_f,N),
\quad
\gcd(c_ec_f-1,N),
\quad
\gcd(c_ec_f+1,N),
\tag{5}
\]

and

\[
\boxed{
\gcd(c_e-w_e,N)=
\gcd(c_e+w_e,N)=1.
}
\tag{6}
\]

Thus the power positions are distinct and noninverse in every hidden prime
component, and every ordinary inverse-pair sign screen is null.

The associated canonical exact values

\[
P_e=c_ew_e=1+\kappa_eN
\tag{7}
\]

can still share integer factors, have equal exact values through different
endpoint presentations, or close only after factor-free refinement. The
large-order theorem does not control these integer effects. Within the
current canonical exact-value decoder, they remain possible progress
channels after the screens (5)--(6) are removed.

This theorem does not exclude larger exponents, component-order finding
beyond `B`, or any other value-dependent decoder. It certifies only the
listed short-window collision and sign screens.

## Theorem 3 — Pilatte's short basis is outside the proved QP sparse catalogue

Pilatte's unconditional theorem uses

\[
d=\lceil\sqrt{\log N}\rceil=\Theta(\sqrt n)
\tag{8}
\]

random small-prime generators and proves that the full relation lattice has
a basis of Euclidean norm

\[
\exp(O(d))=\exp(O(\sqrt n)).
\tag{9}
\]

Each such basis vector has a compact coordinate description, but this is not
a polylogarithmic-support existence theorem. A basis vector may use all
`d=Theta(sqrt(n))` coordinates. A brute-force catalogue guaranteed to cover
the complete promised Euclidean ball has

\[
\exp(\Theta(d^2))=\exp(\Theta(n))
\tag{10}
\]

candidate vectors, not quasipolynomially many.

Therefore Pilatte proves that short integer relations exist with high
probability, but does not put them inside the current classical
polylogarithmic-support QP catalogue. This is not a lower bound. A structured
classical sampler could still find them without enumerating the ball.

## Theorem 4 — the natural large-order/Jacobi-torus splice loses the asymmetry

Now restrict to

\[
N=pq
\]

with distinct odd primes. Let `Delta` be a unit with

\[
\left(\frac{\Delta}{N}\right)=-1,
\tag{11}
\]

and let `alpha` satisfy (2). Put

\[
x={\alpha+\alpha^{-1}\over2}\pmod N,
\qquad
b=\Delta^{-1}(x^2-1)\pmod N.
\tag{12}
\]

For each `r in {p,q}`,

\[
\boxed{
\left(\frac b r\right)
=
\left(\frac\Delta r\right).
}
\tag{13}
\]

Consequently the norm-one equation

\[
x^2-\Delta y^2=1
\tag{14}
\]

has a local `y` exactly in the split hidden component. It has no global
solution `y modulo N`. The standard map that would place `alpha` into the
split torus needs the missing local square root of `Delta` and cannot be
formed as one global torus point with this fixed `x`.

If only the public Kummer coordinate `x` is retained, then for every
nonnegative integer `m`,

\[
T_m(x)={\alpha^m+\alpha^{-m}\over2},
\tag{15}
\]

where `T_m` is the Chebyshev polynomial. Equation (15) is independent of
`Delta`. Thus the x-only order relations discard the forced split/nonsplit
orientation.

This closes only the most direct splice between Harvey--Hittmeir's scalar
large-order element and the P55 Jacobi torus. It does not close the actual
P55 Cayley points, coordinate-specific multi-relation decoders, or a new
win--win theorem inside the torus itself.

## Exact consequence

The cited advances and the elementary upgrades give two useful facts:

1. a deterministic QP source can be made collision-free for the exact
   short-window screens (5)--(6); and
2. a short relation basis exists with high probability in a larger
   `sqrt(n)`-dimensional search region.

These facts do not by themselves supply the missing factor-correlated
sampler. The live options include:

1. exploit the integer carries of the collision-free short power bank;
2. search larger exponents or component-order mismatches beyond `B`;
3. find a structured classical sampler for Pilatte's dense short lattice
   vectors; or
4. use explicit Lucas-torus coordinates in a way that retains the forced
   local orientation instead of projecting to the Kummer coordinate.
