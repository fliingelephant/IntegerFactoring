# F150 V2 candidate — reciprocal-anchor containment cycles are global-root traps

## Status

This is a narrowly repaired proof-only candidate. The original frozen
statement, proof, and failed hostile audit remain preserved. V2 has not
passed a fresh hostile audit or an independent blind reconstruction. It is
not a factoring algorithm.

The closest results are P129--P131. P129 gives the bridge-cycle root. P130
classifies formal squared-action cycles. P131 proves that every wrapped
positive containment cycle needs square-root-scale anchor mass. F150 studies
a different exact subfamily: a positive two-cycle in which each edge uses
the other center as its square anchor. It proves that every such cycle is a
global-root decoy, even though its residual product is automatically a
square.

For the factoring application, first process parity. If an integer input
\(N>2\) is even, then \(2\) is already a proper factor. The theorem below
therefore states the remaining odd-input branch explicitly.

## Setup

Let \(N\ge3\) be an odd integer, and let
\(x,y\in\{1,\ldots,N-1\}\) satisfy

\[
\gcd(xy,N)=1.
\]

Write \([z]_N\) for the least positive residue of the unit \(z\pmod N\).
Suppose there are positive integers \(S,T\) such that

\[
[xy^2]_N=yT,
\qquad
[yx^2]_N=xS.
\tag{1}
\]

These are the two positive containment edges

\[
x\xrightarrow{\text{anchor }y}y,
\qquad
y\xrightarrow{\text{anchor }x}x.
\]

Put

\[
h=[xy]_N.
\tag{2}
\]

## Theorem 1 — exact residual synchronization

Every reciprocal-anchor positive two-cycle satisfies

\[
\boxed{S=T=h.}
\tag{3}
\]

In particular,

\[
xh<N,
\qquad
yh<N.
\tag{4}
\]

Thus the second multiplication by the opposite center cannot introduce an
additional wrap while preserving that center as an exact positive factor.

## Theorem 2 — the cycle root is always global

The two P128 bridge values are

\[
D_x=(xy^2)[xy^2]_N=xy^3h,
\qquad
D_y=(yx^2)[yx^2]_N=yx^3h.
\tag{5}
\]

Their product is the exact integer square

\[
\boxed{
D_xD_y=(x^2y^2h)^2.
}
\tag{6}
\]

The supplied modular root from the two canonical residues is

\[
[xy^2]_N[yx^2]_N=xyh^2.
\]

Using the established P128/P131 convention, divide the positive exact root
in (6) by this supplied modular root. The normalized root is

\[
\boxed{
\rho=xyh^{-1}\equiv1\pmod N.
}
\tag{7}
\]

The inverse orientation \(h(xy)^{-1}\) is also \(1\pmod N\). In P131
notation, the anchor product is \(A=xy\), the residual square root is
\(h\), and the normalized root is \(A/h\).

Because \(N\) is odd, the two terminal gcds from this root are

\[
\gcd(\rho-1,N)=N,
\qquad
\gcd(\rho+1,N)=1.
\]

Therefore this cycle channel does not factor the preprocessed odd input.
A declared endpoint or sign screen can still factor \(N\) before the cycle
is decoded; that is a different channel.

Global first-occurrence exact-value deletion here means deletion among the
actual canonical and lifted P128 retained columns, with their supplied-root
metadata. Every such actual column is \(1\pmod N\) and has supplied root
\(1\). This deletion can remove the displayed dependency, but it cannot
change a surviving version into a useful root. This statement does not
authorize deletion of transformed bridge integers \(D\) by integer equality
without their indexed supplied roots.

## Corollary — ceiling-reciprocal metric selection

Let

\[
a\in\mathbb Z,
\qquad
1<a<\sqrt N,
\qquad
q=\left\lceil\frac Na\right\rceil,
\qquad
h=qa-N.
\tag{8}
\]

If \(h=0\), then \(a\mid N\), so the ordinary gcd/division screen
already finds a factor. If either \(a\) or \(q\) has a proper gcd with
\(N\), that screen also succeeds. Otherwise \(0<h<a<q<N\), both are
units, and one has

\[
[qa^2]_N=ah,
\qquad
[aq^2]_N=qh,
\tag{9}
\]

and both values are below \(N\). Hence the public reciprocal pair \(a,q\)
creates a literal reciprocal-anchor two-cycle, but Theorem 2 makes its
normalized root \(+1\).

Enumerating an explicitly generated quasipolynomial bank of such
near-reciprocal pairs remains a quasipolynomial operation. The cycle
relation itself supplies no factor-correlated non-global root.

## Exact null-screen certificate

For \(N=77\), take \(a=8\), \(q=10\), and \(h=3\). Then

\[
[10\cdot8^2]_{77}=24=8\cdot3,
\qquad
[8\cdot10^2]_{77}=30=10\cdot3.
\]

The canonical inverses are \(24^{-1}=61\) and \(30^{-1}=18\) modulo
\(77\), and all four endpoint sign gcds are \(1\). The bridge values
are

\[
D_q=15{,}360,
\qquad
D_a=24{,}000,
\qquad
D_qD_a=19{,}200^2.
\]

The supplied root is \(24\cdot30=720\), and both \(19{,}200\) and
\(720\) are \(27\pmod{77}\). Thus the standard normalized root is
\(19{,}200/720\equiv1\pmod{77}\). The cycle survives the ordinary
endpoint screens and still gives only the global root.

## Exact scope

F150 does not cover:

1. a two-cycle whose anchors are not the opposite centers;
2. a directed cycle of length at least three;
3. a hypercycle closed through older columns;
4. signed or negative-residue presentations;
5. a branch on which parity preprocessing, an endpoint gcd, or a sign screen
   already succeeds; or
6. an adaptive selector that forces a non-global root by another mechanism.

The live F26-Q target remains a nonreciprocal path or arithmetic hypercycle
whose residual square closes at square-root-scale anchor mass and whose
normalized root is non-global.
