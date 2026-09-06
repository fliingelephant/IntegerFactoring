# F149 V2 candidate statement — compact large anchors canonicalize to an ordinary square-congruence target

## Status and scope

This is a proof-only boundary for the compact-large-anchor sector left open
by P131.  It gives an exact one-position criterion, an exact uniform-source
count on odd semiprimes, and a strict finite certificate.  It is not an
all-input source theorem and not a factoring algorithm.

The closest results are P71, P114, and P128--P131.  P128 retains the
unreduced presentation of a word.  P129 gives the bridge rank and root gate.
P130 reduces formal squared-action cycles to half-relations.  P131 shows
that every wrapped positive containment cycle needs square-root-scale raw
anchor mass, but leaves compact numerically large anchors open.

F149 isolates what numerical largeness itself contributes.  It proves that
the exact magnitude of a squared anchor disappears from the bridge square
class.  Only its residue modulo \(N\) selects a canonical endpoint.  A
single useful bridge is exactly an ordinary congruence of squares.  The
remaining possible gain is therefore a nonuniform source theorem for the
residues reached by compact words, or a multi-relation arithmetic closure.

## 1. Setup

Let \(N>1\) be odd.  Let \(1<q<N\) and \(a\ge1\) satisfy

\[
\gcd(qa,N)=1.
\]

The integer \(a\) can have any magnitude and can be stored by a compact
monomial presentation.  Put

\[
\alpha=[a]_N,
\qquad
c=[q\alpha^2]_N=[qa^2]_N,
\qquad
w=\iota_N(c).
\]

The P128 canonical and lifted exact values are

\[
C=cw,
\qquad
L_a=qa^2w.
\tag{1}
\]

Both are \(1\pmod N\).

## 2. Raw-anchor canonicalization

The square class of the lifted value is

\[
[L_a]=[qw]
\quad\text{in}\quad
\mathbb Q_{>0}^{\times}/(\mathbb Q_{>0}^{\times})^2.
\tag{2}
\]

It is independent of the exact magnitude and factor exponents of \(a\).
If

\[
L_\alpha=q\alpha^2w,
\]

then

\[
L_aL_\alpha=(qa\alpha w)^2.
\tag{3}
\]

The normalized root in (3) is \(+1\pmod N\).  Thus replacing a compact raw
anchor by its canonical residue changes the integer value only by a
root-\(+1\) square-class duplicate.  This comparison is algebraic; it does
not assert that \(\alpha\) is itself an allowed source word.

All containment data also canonicalize.  For every named block \(r\),

\[
r\mid[qa^2]_N
\quad\Longleftrightarrow\quad
r\mid[q\alpha^2]_N,
\]

and the exact residual is the same.  Hence raw numerical size alone cannot
create a new containment edge.

## 3. Exact singleton criterion

The two actual P128 columns in (1) form an exact square relation if and only
if

\[
\boxed{qc=s^2}
\tag{4}
\]

for an integer \(s>0\).  When (4) holds, their exact positive root is

\[
R=aws,
\]

and their normalized root is

\[
\boxed{
\rho\equiv s(q\alpha)^{-1}\pmod N.
}
\tag{5}

Consequently,

\[
\boxed{
\gcd(R\pm1,N)=\gcd(s\pm q\alpha,N).
}
\tag{6}

The singleton is useful exactly when

\[
(q\alpha)^2\equiv s^2\pmod N
\]

has mixed local signs.  Thus one compact large-anchor hit is an ordinary
congruence of squares.  Computing and testing a supplied hit is easy; F149
does not supply a rule that finds one on every input.

## 4. Exact positive self-containment criterion

Put

\[
z=[\alpha^2]_N.
\]

Then the position is a directed self-containment edge \(q\to q\), namely

\[
c=qT,
\]

if and only if

\[
\boxed{qz<N.}
\tag{7}

In that case \(T=z\).  The self-loop is an exact singleton square relation
if and only if

\[
\boxed{z=S^2<N/q.}
\tag{8}

Its normalized root is \(S\alpha^{-1}\), the inverse of the P131 convention
\(\alpha/S\).  The factor test is exactly

\[
\gcd(\alpha-S,N),
\qquad
\gcd(\alpha+S,N).
\tag{9}

Equivalently,

\[
\alpha^2-S^2=hN
\]

for a public integer \(h\ge0\).  The case \(h=0\) gives the global root
\(+1\) and is not useful.  Thus a useful self-loop has \(h\ge1\) and gives
a Fermat-type difference of squares for a positive multiple of \(N\), not a
new decoder.

## 5. Exact uniform-residue count

Now let

\[
N=p\ell
\]

for distinct odd primes \(p,\ell\), and keep one fixed unit center \(q\).
Write uniquely

\[
q=du^2,
\]

where \(d\) is squarefree.  Define

\[
V_d=
\#\{v\ge1:dv^2<N,\ \gcd(v,N)=1\}.
\]

Among all \(\alpha\in(\mathbb Z/N\mathbb Z)^\times\), the exact number that
make (4) useful is

\[
\boxed{2V_d.}
\tag{10}

Therefore a uniform unit anchor residue has useful-singleton probability

\[
\boxed{
{2V_d\over\varphi(N)}
\le
{2\sqrt{N/d}\over\varphi(N)}
<
{4\over\sqrt{dN}}.
}
\tag{11}

For self-containment, put

\[
W_q=
\#\{S\ge1:qS^2<N,\ \gcd(S,N)=1\}.
\]

The exact useful count is \(2W_q\), so the probability is less than

\[
\boxed{{4\over\sqrt{qN}}.}
\tag{12}

Consequently, even

\[
M=2^{\operatorname{polylog} n}=2^{o(n)}

\]

uniform-marginal anchor trials have total singleton success probability at
most

\[
2^{-n/2+o(n)}.
\]

Independence is not needed for this union bound.  The theorem does not apply
to a factor-correlated or otherwise nonuniform compact-word source.  Such a
correlation is exactly the missing source-side possibility.

## 6. Presentation collisions and the P71 boundary

If two public anchor residues satisfy

\[
\alpha^2\equiv\beta^2\pmod N,
\]

then \(\alpha\beta^{-1}\) is a square root of one.  It either is a global
sign, or its two sign gcds give a proper factor.  Hence using a large word
only to reproduce a previously reached squared residue is exactly the P71
half-relation target.

More generally, let a collection of containment cycles have anchor-residue
product \(A_0\) and square residual product \(S^2\).  Its root is

\[
A_0S^{-1}\pmod N.
\]

If \(S\) also has a declared word presentation on the public generators,
this is a P71 bounded half-relation.  If it has no such presentation, the
closure is a genuine integer square-class event.  That second case is not
an order computation, but it is the standard congruence-of-squares target
of P128/P129.

## 7. Strict finite certificate

Take

\[
N=77=7\cdot11,
\qquad
q=2,
\qquad
a=25=5^2.
\]

Here \(a>\sqrt N\), \(a^2\not\equiv1\pmod N\), and

\[
[a^2]_{77}=9=3^2,
\qquad
[2a^2]_{77}=18=2\cdot3^2.
\]

The canonical inverse is \(w=30\), because

\[
18\cdot30=540=1+7\cdot77.
\]

Both direct endpoint screens are null:

\[
\gcd(18-30,77)=\gcd(18+30,77)=1.
\]

The canonical and lifted exact values are

\[
C=540,
\qquad
L_a=2\cdot25^2\cdot30=37500,
\]

and

\[
CL_a=4500^2.
\]

The normalized root is

\[
4500\equiv34\pmod{77},
\]

with

\[
\gcd(34-1,77)=11,
\qquad
\gcd(34+1,77)=7.
\]

This is a legal one-edge P131/P128 **source-semantic** certificate.  It is
strict only with respect to the displayed endpoint-sign screens.  It is not
claimed to be a surviving run of the complete small-input preprocessing,
which would already find a factor of \(77\).  It is not a formal
\(a^2\equiv1\) cycle.  However, its residual root \(3\) is public, so the
useful root is the bounded half-relation \(5^2/3\).  Equivalently, it is the
P128
same-residue collision between

\[
2\cdot3^2=18
\quad\text{and}\quad
2\cdot5^4=1250\equiv18\pmod{77}.
\]

Thus the certificate proves the local algebraic capability but no mechanism
beyond P71/P128 and no surviving all-algorithm input.

## 8. Comparison with earlier results and remaining theorem

- **P71:** repeated squared residues and formal roots are bounded
  half-relations.  F149 identifies the exact non-order remainder: an integer
  residual square root with no short public word presentation.
- **P114:** replacing a raw anchor by its canonical residue gives a
  degenerate repeated multiplier, not a new rank-mismatch rectangle.  A
  genuine two-anchor, two-center grid remains exactly P114.
- **P128:** the unreduced source remains useful because a compact word can
  reach a new residue.  Its raw squared factor mass does not change the
  parity column.
- **P129:** equation (4) is the one-bridge instance of the exact bridge
  square-class gate.  Multi-bridge arithmetic cycles remain possible.
- **P130:** formal endpoint cycles and squared-residue collisions stay in
  the half-order class.  F149 does not close cross-star arithmetic
  hypercycles.
- **P131:** a raw anchor above \(\sqrt N\) evades the numerical lower bound,
  but F149 shows that this evasion alone adds no modular or square-class
  information.

The exact remaining compact-anchor theorem is:

> Prove that the quasipolynomial sparse-word source reaches, on every
> surviving input or with inverse-quasipolynomial probability, a residue
> whose singleton square class closes as in (4), or a multi-relation
> arithmetic cycle whose residual product is a square and whose normalized
> root is non-global.

A positive result must use a factor-correlated deviation from the uniform
count (11), or must amortize many nonclosing relations.  Numerical raw-anchor
magnitude by itself cannot supply that deviation.
