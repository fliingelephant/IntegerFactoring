# F153 candidate — Jacobi-torus orientation is a compatible character, not a forced section disagreement

## Status

This is a proof-only kill-first candidate. It is not a factoring algorithm.
It has not passed hostile audit or statement-only blind reconstruction.

The closest promoted results are P55 and P57. P55 proves that a
Jacobi-minus-one Lucas torus exposes the exact signed factor gap. P57 proves
the corresponding ordinary trace aliases and isolates a mixed-root selection
problem. F151 V2 tests a Harvey--Hittmeir large-order element and proves that
its direct Kummer-coordinate splice loses the Jacobi orientation. F152 is an
unpromoted split-or-section framework; its blind reconstruction requires the
squareclass-independence and supplied-root-safe-dedup repairs. F153 uses only
the repaired formal principle: a source gives no factor when all of its
public lifts agree with one homomorphic section modulo global sign.

The material difference is an exact classification of the most direct ways
to combine P55 orientation with that section principle. Multiplicative
discriminant words, the forced one-step exponent halving, rational Cayley
halving, conjugation-preserving cross-discriminant maps, biquadratic norm
projections, and homomorphic transfer of an ordinary high-order element are
all treated explicitly.

Let

\[
N=pq,\qquad 3\le p<q
\]

with distinct odd primes, and put \(R=\mathbf Z/N\mathbf Z\). For a unit
discriminant \(D\), write

\[
A_D=R[w_D]/(w_D^2-D),\qquad
T_D=\{U\in A_D^\times:U\overline U=1\}.
\]

For every unit \(D\) with Jacobi symbol \(-1\), define the hidden orientation

\[
\epsilon(D)=\left(\frac Dp\right)\in\{\pm1\}.
\tag{1}
\]

Then \((D/q)=-\epsilon(D)\).

## Theorem 1 — every discriminant-word orientation is one linear character

Let \(D_1,\ldots,D_k\) be units of Jacobi symbol \(-1\). For integers
\(e_1,\ldots,e_k\), put

\[
F=\prod_iD_i^{e_i},\qquad
\delta=\sum_i e_i\pmod2,\qquad
\eta=\prod_i\epsilon(D_i)^{e_i}.
\tag{2}
\]

Then

\[
\boxed{
\left(\frac Fp\right)=\eta,
\qquad
\left(\frac Fq\right)=(-1)^\delta\eta.
}
\tag{3}
\]

Thus all hidden orientation data in multiplicative discriminant words is the
restriction of the single quadratic character \((\cdot/p)\). In particular:

1. if two word presentations have the same squareclass modulo both hidden
   primes, they have the same \(\eta\);
2. if a word is a square modulo \(N\), then \(\delta=0\) and \(\eta=1\); and
3. any relation-lift rule whose only hidden datum is the discriminant
   orientation factors through one homomorphism on the generated
   squareclass span.

Therefore two such multiplicative rules cannot force an F152-style section
disagreement. A disagreement must use information beyond the discriminant
quadratic characters, such as a coordinate, a carry, or a non-homomorphic
choice.

This is not a claim about every possible explicit-coordinate operation on
Lucas points.

## Theorem 2 — P55 has one exact, but tautological, public halving

Fix a Jacobi-minus-one \(D\), write \(\epsilon=\epsilon(D)\), and put

\[
g=q-p,qquad
m_p=p-\epsilon,qquad
m_q=q+\epsilon.
\tag{4}
\]

The two local torus orders are \(m_p,m_q\), and

\[
N-1-\epsilon g=m_pm_q.
\tag{5}
\]

For every \(U\in T_D\), P55 and one further exact identity give

\[
\boxed{U^{N-1}=U^{\epsilon g},}
\tag{6}
\]

\[
\boxed{U^{(N-1)/2}=U^{\epsilon g/2}.}
\tag{7}
\]

Both local orders are even, so \(m_pm_q/2\) is still a multiple of each
local order. Equation (7) is therefore valid pointwise, without a generator
assumption. Squaring (7) gives (6). The public value
\(U^{(N-1)/2}\) is a synchronized square root of \(U^{N-1}\); it creates no
non-global two-torsion element.

This direct division cannot be repeated uniformly. For \(k\ge2\), the
same proof would need both \(2^k\mid m_p\) and \(2^k\mid m_q\), as well as an
integral exponent \(g/2^k\). Already modulo four these conditions conflict:
if \(4\mid m_p,m_q\), then \(g\equiv-2\epsilon\pmod4\). Hence the P55
identity supplies exactly one universally valid factor of two, not a
halving ladder.

## Theorem 3 — Cayley halving is square-root selection, and its two ordinary branches are global

For a clean Cayley parameter \(t\), put

\[
U_D(t)=\frac{1+t w_D}{1-t w_D},
\qquad
z_D(t)=1-Dt^2.
\tag{8}
\]

On the branch where the displayed denominators and \(Dt\) are units, the
Cayley group law gives

\[
U_D(s)^2=U_D(t)
\quad\Longleftrightarrow\quad
Dt s^2-2s+t=0.
\tag{9}
\]

The discriminant of this quadratic is

\[
4z_D(t).
\tag{10}
\]

More exactly, a solution \(s\) gives

\[
r=1-Dts,\qquad r^2=z_D(t),
\tag{11}
\]

and a square root \(r^2=z_D(t)\) gives the two displayed halves

\[
s_\pm=\frac{1\pm r}{Dt}.
\tag{12}
\]

The two halves obtained from the globally opposite roots \(r,-r\) differ by
the global torus element \(-1\) in both CRT components. They do not give a
factor. A pair of roots that differs in only one hidden component already
gives a non-global square root of one through \(r'/r\), and therefore
factors \(N\) by a gcd before the torus comparison adds anything.

Thus ordinary doubling and the two synchronized quadratic branches do not
force a non-global two-torsion lift. A useful halving rule must make a mixed
CRT choice, and that choice is itself the missing factor-bearing operation.

The excluded cases \(t=0\) or a nonunit denominator are either trivial or
must be handled by the usual gcd screen; no success probability is asserted.

## Theorem 4 — standard cross-discriminant operations preserve the same character

Let \(D,E\) both have Jacobi symbol \(-1\), and put

\[
F=DE,\qquad
\eta=\epsilon(D)\epsilon(E).
\tag{13}
\]

Then \(F\) has the same local quadratic character \(\eta\) at both hidden
primes. For every \(W\in T_F\),

\[
\boxed{
W^{N-1}=W^{\eta(p+q-2\eta)}.
}
\tag{14}
\]

Thus equal hidden orientations give the exponent \(p+q-2\), while opposite
hidden orientations give \(-(p+q+2)\). This is a new exact sum-type relation,
but its branch bit is only the character product \(\eta\). It does not by
itself provide the hidden exponent or a non-global root.

There are also two exact algebraic obstructions.

First, a conjugation-preserving \(R\)-algebra isomorphism

\[
A_D\longrightarrow A_E
\]

exists exactly when there is a unit \(b\in R\) with

\[
b^2=D E^{-1}.
\tag{15}
\]

It sends \(w_D\) to \(b w_E\). Such a square root exists exactly when
\(\epsilon(D)=\epsilon(E)\). The two synchronized choices \(b,-b\) differ
only by global conjugation. Two mixed CRT choices already expose a factor.

Second, in the biquadratic algebra

\[
B=R[w_D,w_E]/(w_D^2-D,w_E^2-E),
\tag{16}
\]

embed \(U\in T_D\) and \(V\in T_E\). The three quadratic relative norms of
\(UV\) are

\[
\boxed{
\operatorname{Nm}_{B/A_D}(UV)=U^2,
\quad
\operatorname{Nm}_{B/A_E}(UV)=V^2,
\quad
\operatorname{Nm}_{B/A_F}(UV)=1.
}
\tag{17}
\]

Therefore the direct product-plus-relative-norm construction returns only
the old points squared or the identity. It does not manufacture a new
cross-discriminant torus lift.

Equations (14)--(17) do not exclude traces, resultants, derivatives, lifts
modulo \(N^2\), or another non-norm projection of the full biquadratic
coordinates.

## Theorem 5 — ordinary large order cannot transfer through a uniform torus homomorphism

Let \(r\) be an odd prime and suppose \(D\) is nonsquare modulo \(r\). Then

\[
|\mathbf F_r^\times|=r-1,
\qquad
|T_D(\mathbf F_r)|=r+1.
\]

Every group homomorphism

\[
\phi:\mathbf F_r^\times\longrightarrow T_D(\mathbf F_r)
\]

has image order dividing

\[
\gcd(r-1,r+1)=2.
\tag{18}

\]

Hence a Harvey--Hittmeir element of large ordinary multiplicative order
cannot retain that order under any homomorphic transfer into the nonsplit
side of a Jacobi-minus-one torus. On the split side an isomorphism needs a
square root of \(D\); on the nonsplit side no high-order homomorphic image
exists.

The natural non-homomorphic Kummer map

\[
x=(\alpha+\alpha^{-1})/2
\]

is exactly the F151 boundary: constructing its missing \(y\)-coordinate
requires a local square root on only the split side, while the public
Chebyshev relations in \(x\) lose \(D\). Choosing \(t\) as a function of a
large-order \(\alpha\) is another non-homomorphic map, and the ordinary order
certificate gives no torus-order theorem for it.

## Exact conclusion and next gate

The tested splice does not force two incompatible decorated sections.
Its hidden discriminant data is one linear quadratic character. Doubling,
the universally valid exponent halving, synchronized Cayley halving,
cross-discriminant isomorphisms, relative norms, and homomorphic high-order
transfer all preserve that compatibility or require the factor-bearing mixed
choice in advance.

The next viable gate must add an operation that is not determined by this
character section. A precise target is:

> Construct, in quasipolynomial work, an explicit coordinate-level map on
> two or more Lucas discriminants whose two presentations land in the same
> repaired F152 squareclass fibre but whose lift quotient is forced to be a
> non-global root; or prove that a non-norm biquadratic invariant gives a
> factor-correlated value with inverse-quasipolynomial probability.

Theorem 4 identifies the smallest live algebra for that test: the full
biquadratic coordinates before relative norm. A torus-native large-order
procedure would also be new, but large order alone would remove collisions;
it would not invalidate the character-section obstruction.
