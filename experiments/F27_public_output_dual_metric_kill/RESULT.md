# F27 kill-first report: public output, scaled dual, and the residual cyclic quotient

**Status:** promoted as P37/X31/C34 after a corrected hostile re-audit and a
fresh proof-blind reconstruction.  A first reconstruction prompt incorrectly
required every nonzero Smith invariant to be coprime to \(N\) and was
rightly rejected; that failed artifact is preserved separately.

**Family:** F19.

**Closest prior route and material difference.**  The closest promoted result
is P35/X29.  P35 treats the public zero-syndrome coefficient kernel, its exact
rational-kernel quotient, direct sums, and one graph-lattice slice.  The
present report instead treats the two objects that P35 explicitly left open,

\[
\Lambda_{\rm out}(A,N)=A\mathbb Z^d+N\mathbb Z^t,
\qquad
\Lambda_{\rm dual}(A,N)=N\mathbb Z^d+A^{\mathsf T}\mathbb Z^t,
\]

and the smallest output quotient obtained from a fixed-completion
four-square batch.

**Classification.**  This is evidence against the exact auxiliary mechanism
that the general public output or scaled-dual lattice supplies a new
determinant, finite-quotient, or uniform output-membership/CVP signal merely
because the two unknown local output modules have different metric scales.
After elementary Smith-gcd branches are removed, the faithful Euclidean
quotient of either general lattice is also an exact public \(N\)-scaling.
The shortest-vector distribution result below is only for the explicit
two-dimensional cyclic quotient.  This is not a lower bound for lattices,
full-lattice SVP/CVP, coordinate-gcd signals in arbitrary dimension, biased
residual completions, nonlinear postprocessing, or arbitrary public matrices
manufactured from \(N\).

No computation was used.  Everything below is symbolic.

## Outcome

There are three exact collapses.

1.  For every integer matrix \(A\), both the public output lattice and the
    displayed scaled dual are themselves CRT intersections of their two
    local analogues.  Integer Smith form either exposes a proper divisor of
    \(N\) immediately or puts their abelian-group structure into a public
    diagonal form with entries only \(1\) and \(N\).  Projecting off the
    resulting public primitive exact directions leaves exactly an
    \(N\)-scaled public projected ambient lattice, with the analogous local
    \(p\)- and \(q\)-scalings.  A lattice vector is therefore in both local
    output modules; a CVP error has exactly the same two local output
    memberships as its target.

    These facts do not control Euclidean shortest vectors, closest vectors,
    or coordinate-gcd extraction in the original lattices.  In particular,
    for a fixed batch \(A\in\mathbb Z^{4\times m}\), the original
    \(\Lambda_{\rm dual}(A,N)\subseteq\mathbb Z^m\) is growing-dimensional.
    Its faithful quotient now has the stated uniform scaling, but
    full-lattice SVP/CVP and coordinate-gcd extraction remain open because
    the primitive exact directions can couple nonorthogonally to that
    quotient.

2.  For a fixed residual completion \(C=(z,w)\) that is unimodular modulo
    \(N\), and a batch satisfying the explicit surjectivity condition in
    Section 3, the proposed two-dimensional output quotient is indeed

    \[
    L_C=\{(c,d)\in\mathbb Z^2:wc-zd\equiv0\pmod N\}.
    \]

    Put \(g=\gcd(z,w)\), \(C_0=(z/g,w/g)\), and
    \(h=\gcd(g,N)\).  There is a publicly computable \(D\) with
    \(\det(C_0,D)=1\), and the exact general normal form is

    \[
    L_C=\mathbb ZC_0+\frac Nh\mathbb ZD.
    \]

    Thus \(1<h<N\) already factors \(N\), while \(h=N\) makes the
    determinant congruence vacuous.  On the nontrivial unfactored branch
    \(h=1\), the determinant kernel equals the actual cyclic output lattice,

    \[
    L_C=\mathbb ZC_0+N\mathbb ZD.
    \]

    After quotienting its public exact direction \(\mathbb ZC_0\), the
    informative metric rank is one, not two.

3.  In the unimodular coordinates \(v=aC_0+bD\), local output-line
    membership is just \(r\mid b\).  For a public output vector
    \(v=aC_0+NbD\), coordinatewise divisibility by exactly one factor is
    instead just \(r\mid a\), and

    \[
    \gcd(N,v_1,v_2)=\gcd(N,a).
    \]

    Both scalars are public.  The first is always divisible by both factors
    for a vector of \(L_C\); the second is a new scalar-gcd ticket, not a
    hidden metric invariant.  The lattice construction alone gives no
    inverse-polynomial bias for that ticket.

For exact SVP **in this two-dimensional cyclic quotient** there are two
rigorous negative regimes.  If
\(\lVert C_0\rVert^2<N\), the only shortest vectors are
\(\pm C_0\), so the scalar ticket is \(\pm1\).  More generally, on a
balanced distinct-odd-semiprime, if the local projective line of \(C\) is
uniform at each prime, the probability that *any* shortest vector has a
proper coordinate gcd is \(O(1/p+1/q)\).  P30 does not provide this
hypothesis for the completion \((z,w)\): it proves uniformity of the quaternion row and image
lines conditional on the completion.  A specially biased completion law
could therefore still make the public shortest-vector scalar divisible by a
factor.  That is the exact surviving gap for the cyclic quotient; it is not a
signal proved by its output/dual geometry.  The original growing-dimensional
scaled dual has a separate open metric gap.

## 1. General output lattices are CRT intersections

Let \(N=pq\), where \(p\) and \(q\) are distinct primes, and for
\(r\in\{p,q,N\}\) define

\[
\Lambda_{\rm out}(A,r)=A\mathbb Z^d+r\mathbb Z^t.
\]

Then

\[
\Lambda_{\rm out}(A,N)
=\Lambda_{\rm out}(A,p)\cap\Lambda_{\rm out}(A,q).
\tag{1.1}
\]

The forward inclusion is immediate.  Conversely, suppose \(y\) is in the
intersection.  There are coefficient vectors \(x_p,x_q\) such that

\[
y\equiv Ax_p\pmod p,
\qquad
y\equiv Ax_q\pmod q.
\]

Choose \(x\in\mathbb Z^d\) coordinatewise by CRT with
\(x\equiv x_p\pmod p\) and \(x\equiv x_q\pmod q\).  Then
\(y-Ax\) is divisible by both primes and hence by \(N\), proving (1.1).

This matters for extraction.  A shortest or otherwise selected vector of the
public output lattice lies in both local output lattices.  It cannot itself
witness membership in exactly one local output module.  This statement is
only about output-module membership; its ordinary coordinates could still
have a proper common gcd with \(N\).

The same coset invariance as in P35 holds.  If \(t\in\mathbb Z^t\) is a
target, \(v\in\Lambda_{\rm out}(A,N)\), and \(e=t-v\), then

\[
e\in\Lambda_{\rm out}(A,r)
\quad\Longleftrightarrow\quad
t\in\Lambda_{\rm out}(A,r)
\qquad(r=p,q).
\tag{1.2}
\]

Thus exact or approximate CVP in the public output lattice chooses a short
representative of a fixed public-output coset; it does not manufacture a
one-local coset.

Let \(s_r=\operatorname{rank}_{\mathbb F_r}(A\bmod r)\).  A target uniform
modulo \(N\) has

\[
\Pr(t\in\Lambda_{\rm out}(A,r))=r^{-(t-s_r)}.
\]

CRT makes the two residue components independent, so the exact one-local
probability is

\[
p^{-(t-s_p)}+q^{-(t-s_q)}
-2p^{-(t-s_p)}q^{-(t-s_q)}.
\tag{1.3}
\]

On balanced inputs this is exponentially small in \(\log N\) whenever the
common output codimension is positive.  If the common codimension is zero,
both local output lattices are all of \(\mathbb Z^t\), so the symmetric
difference is empty.

## 2. Smith form removes the proposed determinant mystery

Take an integer Smith form

\[
UAV=S=\operatorname{diag}(\sigma_1,\ldots,\sigma_\rho,0,\ldots,0),
\]

where \(U,V\) are unimodular and \(\rho=\operatorname{rank}_{\mathbb Q}A\).
Put

\[
\delta_i=\gcd(\sigma_i,N)\quad(1\le i\le\rho).
\]

Then, as an exact lattice identity,

\[
U\Lambda_{\rm out}(A,N)
=\operatorname{diag}
(\delta_1,\ldots,\delta_\rho,
\underbrace{N,\ldots,N}_{t-\rho})
\mathbb Z^t.
\tag{2.1}
\]

Indeed, in the \(i\)-th Smith coordinate the subgroup generated by
\(\sigma_i\) and \(N\) is \(\delta_i\mathbb Z\); a zero Smith row contributes
\(N\mathbb Z\).

If any \(\delta_i\) satisfies \(1<\delta_i<N\), it is already a public
proper divisor.  On the branch where no such divisor occurs, every
\(\delta_i\) is \(1\) or \(N\).  Because the Smith entries form a
divisibility chain, for some \(u\)

\[
U\Lambda_{\rm out}(A,N)
=\mathbb Z^u\oplus N\mathbb Z^{t-u}.
\tag{2.2}
\]

This is an arithmetic normal form, not an orthogonal similarity: \(U\) can
distort Euclidean lengths.  The induced Gram form is nevertheless completely
public.  Therefore (2.2) does not prove that every metric algorithm fails;
it proves that the determinant and finite-quotient structure contain no
unexposed \(p/q\) scale after the elementary Smith-gcd tickets have been
removed.

The displayed P35 scaled dual is simply an output lattice for the transpose:

\[
\Lambda_{\rm dual}(A,N)
=N\mathbb Z^d+A^{\mathsf T}\mathbb Z^t
=\Lambda_{\rm out}(A^{\mathsf T},N).
\tag{2.3}
\]

Applying \(V^{\mathsf T}\) gives

\[
V^{\mathsf T}\Lambda_{\rm dual}(A,N)
=\operatorname{diag}
(\delta_1,\ldots,\delta_\rho,
\underbrace{N,\ldots,N}_{d-\rho})
\mathbb Z^d.
\tag{2.4}
\]

Consequently it has the same conclusions: it is the intersection of its
\(p\)- and \(q\)-local versions; Smith form either factors first or leaves
only \(1,N\) invariant factors; and a uniform target has one-local
probability

\[
p^{-(d-s_p)}+q^{-(d-s_q)}
-2p^{-(d-s_p)}q^{-(d-s_q)}.
\tag{2.5}
\]

As with \(U\), the unimodular transformation \(V^{\mathsf T}\) is generally
not orthogonal.  Equations (2.3)--(2.5) therefore prove no SVP, CVP-distance,
or coordinate-gcd theorem for \(\Lambda_{\rm dual}(A,N)\).  For the fixed
four-square batch below, this is the original rank-\(m\) lattice

\[
N\mathbb Z^m+A^{\mathsf T}\mathbb Z^4.
\]

Its full-lattice Euclidean optimizer and coordinate-gcd law remain open; it
is not the rotated two-dimensional lattice analyzed in Section 6.

### The general faithful quotients are exact public scalings

The no-factor Smith branch gives more than an arithmetic determinant
statement.  Define the public primitive exact-direction lattice

\[
E_{\rm out}
=U^{-1}(\mathbb Z^u\oplus0)
\subseteq\mathbb Z^t.
\]

Then (2.2) is equivalently

\[
\Lambda_{\rm out}(A,N)=E_{\rm out}+N\mathbb Z^t.
\tag{2.6}
\]

Indeed, after applying \(U\), both sides are
\(\mathbb Z^u\oplus N\mathbb Z^{t-u}\).  The same Smith entries are units
modulo both local primes in the first \(u\) positions and are divisible by
both primes in the remaining positions.  Hence

\[
\Lambda_{\rm out}(A,r)=E_{\rm out}+r\mathbb Z^t,
\qquad r\in\{p,q,N\}.
\tag{2.7}
\]

Let \(\pi_{\rm out}\) be orthogonal projection off
\(E_{\rm out}\otimes\mathbb R\).  Primitivity and (2.7) give the exact
faithful-quotient identities

\[
\pi_{\rm out}(\Lambda_{\rm out}(A,r))
=r\,\pi_{\rm out}(\mathbb Z^t),
\qquad r\in\{p,q,N\}.
\tag{2.8}
\]

For the scaled dual, put

\[
E_{\rm dual}
=V^{-\mathsf T}(\mathbb Z^u\oplus0)
\subseteq\mathbb Z^d.
\]

For \(r\in\{p,q,N\}\), write
\(\Lambda_{\rm dual}(A,r)=r\mathbb Z^d+A^{\mathsf T}\mathbb Z^t\).
Let \(\pi_{\rm dual}\) be orthogonal projection off
\(E_{\rm dual}\otimes\mathbb R\).  Then

\[
\Lambda_{\rm dual}(A,r)=E_{\rm dual}+r\mathbb Z^d,
\qquad
\pi_{\rm dual}(\Lambda_{\rm dual}(A,r))
=r\,\pi_{\rm dual}(\mathbb Z^d).
\tag{2.9}
\]

Thus, after the public exact directions are removed, the two general
faithful quotients have public fixed shape and uniform scales \(p\),
\(q\), and \(N\); adding samples creates no hidden shape parameter in the
public quotient.  This still does not control a metric optimizer in the
**full** lattice.  Nonorthogonal coupling to \(E_{\rm out}\) or
\(E_{\rm dual}\) can affect the selected representative and its coordinate
gcd.

The two useful duality identities, with ordinary Euclidean duals, are

\[
N\Lambda_{\rm out}(A,N)^*=K_N(A^{\mathsf T}),
\qquad
NK_N(A)^*=\Lambda_{\rm out}(A^{\mathsf T},N).
\tag{2.10}
\]

The second is P35's formula.  The first follows directly by writing a dual
vector as \(u/N\): it pairs integrally with \(N\mathbb Z^t\) exactly when
\(u\in\mathbb Z^t\), and it pairs integrally with \(A\mathbb Z^d\) exactly
when \(A^{\mathsf T}u\equiv0\pmod N\).

## 3. When a fixed four-square batch really has the claimed quotient

Fix a completion \((z,w)\) and suppose the batch consists of columns

\[
\beta_i=(x_i,y_i,z,w)^{\mathsf T}\in\mathbb Z^4.
\]

Let \(A\) be the \(4\times m\) matrix with these columns and let \(T\) be
the \(3\times m\) matrix with columns \((x_i,y_i,1)^{\mathsf T}\).  Over
\(R=\mathbb Z/N\mathbb Z\), define

\[
\psi(u,v,s)=(u,v,sz,sw).
\]

The exact hypothesis needed for the simple quotient is that \(T\) is
surjective over \(R\).  This is publicly testable: if \(\Delta_3(T)\) is
the gcd of the \(3\times3\) minors, surjectivity is equivalent to

\[
\gcd(N,\Delta_3(T))=1.
\tag{3.1}
\]

If the gcd in (3.1) is proper, the batch has already factored \(N\).  Merely
saying that there are many samples or that their rational span has dimension
three is not enough; (3.1), or an equivalent module statement, is the needed
global condition.

Assume (3.1) and \(\gcd(N,z,w)=1\).  Then \(\psi\) is injective and

\[
\operatorname{im}(A\bmod N)
=R e_1\oplus R e_2\oplus R(0,0,z,w)^{\mathsf T}.
\]

Taking the full preimage in \(\mathbb Z^4\) gives

\[
\Lambda_{\rm out}(A,N)
=\mathbb Z^2\oplus
\bigl((z,w)\mathbb Z+N\mathbb Z^2\bigr).
\tag{3.2}
\]

The first two directions are public and saturated.  The remaining
two-dimensional quotient is

\[
(z,w)\mathbb Z+N\mathbb Z^2.
\tag{3.3}
\]

This is a quotient on the four-dimensional **output side**.  Its ordinary
rank-two Euclidean dual is likewise a quotient-side object.  Neither is the
original coefficient-side P35 lattice
\(\Lambda_{\rm dual}(A,N)=N\mathbb Z^m+A^{\mathsf T}\mathbb Z^4\).

The equality of (3.3) with the determinant-congruence definition of \(L_C\)
is proved next.  If (3.1) fails without exposing a factor, or if the batch
does not use one fixed completion, (3.2) must not be asserted; the general
Smith analysis of Sections 1--2 is the valid replacement.

For the residual-only four-square source in P30,
\(z^2+w^2\) is a unit modulo \(N\), so
\(\gcd(N,z,w)=1\) automatically.  That is all the present argument needs;
it does not assume the stronger integer equality \(\gcd(z,w)=1\).
P30 does not say that independent finder calls share a completion or that
the matrix \(T\) satisfies (3.1).  Those are additional hypotheses of this
fixed-residual batch.

## 4. Exact cyclic normal form and every singular case

If \(C=(0,0)\), then the determinant congruence is vacuous and
\(L_C=\mathbb Z^2\); no normalization is needed.  Henceforth suppose
\(C\ne0\) and let

\[
C=(z,w),\qquad g=\gcd(z,w)>0,\qquad
C_0=(z/g,w/g).
\]

Then \(C_0\) is primitive.  Extended Euclid produces
\(D=(d_1,d_2)\in\mathbb Z^2\) with

\[
\det(C_0,D)=z_0d_2-w_0d_1=1.
\tag{4.1}
\]

Thus \((C_0,D)\) is a unimodular basis of \(\mathbb Z^2\).  Set

\[
h=\gcd(g,N),\qquad N_0=N/h.
\]

Writing \(g=hg_1\) and \(N=hN_0\), one has
\(\gcd(g_1,N_0)=1\), and hence

\[
N\mid g\det(C_0,v)
\quad\Longleftrightarrow\quad
N_0\mid\det(C_0,v).
\]

Every \(v\in\mathbb Z^2\) has a unique expression
\(v=aC_0+bD\), and (4.1) gives \(\det(C_0,v)=b\).  Therefore

\[
\boxed{
L_C=\mathbb ZC_0+N_0\mathbb ZD,
\qquad \det L_C=N_0.}
\tag{4.2}
\]

This proves the seed normal form and also gives its exact singular cases:

- if \(h=1\), then \(g\) is a unit modulo \(N\) and
  \(L_C=\mathbb ZC_0+N\mathbb ZD\);
- if \(1<h<N\), \(h\) is already a public proper divisor and the lattice
  determinant has fallen to \(N/h\); and
- if \(h=N\), the congruence is vacuous and \(L_C=\mathbb Z^2\).

The actual cyclic output lattice generated by the residual is

\[
O_C=C\mathbb Z+N\mathbb Z^2.
\]

In the same unimodular basis its exact normal form is

\[
O_C=h\mathbb ZC_0+N\mathbb ZD,
\qquad \det O_C=hN.
\tag{4.3}
\]

Indeed, the first coordinate ideal is generated by \(g\) and \(N\), hence
by \(h\), while the second is generated by \(N\).  Therefore

\[
O_C=L_C
\quad\Longleftrightarrow\quad h=1.
\tag{4.4}
\]

This is why the seed's unit hypothesis is essential.  Outside it, the
two-dimensional determinant kernel is the scaled-dual partner of the
two-dimensional cyclic output lattice, not the output lattice itself:

\[
NO_C^*=R(L_C),
\qquad
NL_C^*=R(O_C),
\tag{4.5}
\]

where \(R(x,y)=(-y,x)\).  The identities follow directly from dot-product
and determinant congruences.  Their determinant check is
\(\det(NO_C^*)=N/h=\det L_C\).

Equation (4.5) concerns only \(O_C,L_C\subseteq\mathbb Z^2\); it says
nothing about \(\Lambda_{\rm dual}(A,N)\subseteq\mathbb Z^m\) for the
original batch.

For \(N=pq\), the local lattice at a prime \(r\mid N\) is all of
\(\mathbb Z^2\) if \(r\mid g\), and otherwise is

\[
L_{C,r}=\mathbb ZC_0+r\mathbb ZD.
\tag{4.6}
\]

Thus every singular local-rank mismatch is already visible through
\(\gcd(g,N)\).  In the residual-unit case both local maps have rank one and
(4.6) applies at both primes.

There is also an even cheaper boundary.  If either
\(\gcd(N,z)\) or \(\gcd(N,w)\) is proper, it factors \(N\) before any
metric call.  On the unfactored branch each coordinate is either a unit
modulo \(N\) or zero modulo \(N\), with the two coordinates not both zero.

## 5. The two public scalars

Assume from now on that \(h=1\), so \(N_0=N\).  In ambient unimodular
coordinates,

\[
v=aC_0+bD.
\]

The local output-line condition is

\[
v\in L_{C,r}
\quad\Longleftrightarrow\quad r\mid b.
\tag{5.1}
\]

This is the first public scalar.  It is
\(b=\det(C_0,v)\).  For \(v\in L_C\), \(b\) is already divisible by
\(N\), so (5.1) holds at both primes and its natural gcd is \(N\).

Now write a vector of the public lattice as

\[
v=aC_0+NbD.
\tag{5.2}
\]

Because \((C_0,D)\) is unimodular, an integer unimodular coordinate change
preserves the ideal generated by the coordinates and \(N\).  Hence

\[
\gcd(N,v_1,v_2)
=\gcd(N,a,Nb)
=\gcd(N,a).
\tag{5.3}
\]

Here \(a=\det(v,D)\) is also public.  Equation (5.3) is the second scalar:
coordinatewise divisibility of a public output vector by exactly one hidden
prime is neither hidden nor encoded in the determinant scale; it is exactly
the event that a public coefficient \(a\) has a proper gcd with \(N\).

Equivalently,

\[
L_C\cap p\mathbb Z^2=pL_{C,q},
\qquad
L_C\cap q\mathbb Z^2=qL_{C,p}.
\tag{5.4}
\]

For example, if \(v=py\in L_C\), then
\(N\mid\det(C_0,v)=p\det(C_0,y)\), so
\(q\mid\det(C_0,y)\), which is exactly \(y\in L_{C,q}\).
The converse is immediate.  Thus the shortest vector in \(L_C\) that is
coordinatewise divisible by \(p\) has length
\(p\lambda_1(L_{C,q})\).  The apparently new metric event is a competition
between the public minimum and a hidden local sublattice minimum, but any
winning vector reveals the same scalar gcd (5.3).

These two scalars must not be conflated.  The \(b\)-condition tests local
*output-module membership*.  The \(a\)-condition tests ordinary
coordinatewise divisibility of a vector already in both output modules.

## 6. Exact shortest-vector and quotient geometry

Let \(\ell=\lVert C_0\rVert_2\).  Since
\(\det(C_0,D)=1\), the component of \(D\) perpendicular to \(C_0\) has
length \(1/\ell\).  Consequently every vector (5.2) with \(b\ne0\) obeys

\[
\lVert aC_0+NbD\rVert_2\ge\frac{N|b|}{\ell}.
\tag{6.1}
\]

The lattice already contains \(C_0\).  Therefore, if
\(\ell^2<N\), (6.1) is strictly larger than \(\ell\) for every
\(b\ne0\), while the nonzero \(b=0\) vectors are the multiples of
\(C_0\).  Hence

\[
\ell^2<N
\quad\Longrightarrow\quad
\operatorname{SVP}(L_C)=\{\pm C_0\}.
\tag{6.2}
\]

Their scalar \(a\) is \(\pm1\), so (5.3) cannot factor \(N\).

Orthogonally quotienting the public exact direction makes the collapse even
clearer.  If \(\pi\) projects onto \(C_0^\perp\), then

\[
\pi(\mathbb Z^2)=\frac1\ell\mathbb Z,
\qquad
\pi(L_{C,r})=\frac r\ell\mathbb Z,
\qquad
\pi(L_C)=\frac N\ell\mathbb Z.
\tag{6.3}
\]

Thus the two-dimensional object left after removing the first two
four-square coordinates still contains one exact rational direction.
Its faithful congruence quotient is the one-dimensional public lattice in
(6.3).  It has no internal shape parameter from which separate \(p\)- and
\(q\)-scales could be read.

The scaled Euclidean dual **of this rank-two cyclic quotient** gives no new
geometry on the unfactored branch.  Let \(R(x,y)=(-y,x)\) be quarter
rotation.  Directly from \(L_C=C_0\mathbb Z+N\mathbb Z^2\),

\[
NL_C^*
=\{u\in\mathbb Z^2:C_0\cdot u\equiv0\pmod N\}
=RC_0\mathbb Z+N\mathbb Z^2
=R(L_C).
\tag{6.4}
\]

So \(NL_C^*\) is exactly an isometric rotation of the two-dimensional
cyclic output lattice, with identical successive minima and CVP distance
distribution.  Equivalently, this is P35's scaled dual applied to the
**one-row** map \((w_0,-z_0)\), whose coefficient kernel is \(L_C\).
It is not \(\Lambda_{\rm dual}(A,N)\) for the original fixed batch and
proves no geometric statement about that rank-\(m\) lattice.

### A uniform-line SVP bound

There is a clean distributional kill test, although its hypothesis is not
known for the actual completion source.  Assume in this subsection that
\(N=pq\) with distinct **odd** primes, and put

\[
\mathcal S_r=
\{[u:v]\in\mathbf P^1(\mathbb F_r):u^2+v^2\ne0\},
\qquad |\mathcal S_r|=r-\left(\frac{-1}{r}\right).
\]

Suppose

\[
p<q\le\kappa p
\]

for a fixed \(\kappa\), and suppose the projective line of
\(C\bmod r\) is uniform on \(\mathcal S_r\) at each
\(r\in\{p,q\}\).  Independence of the two lines is not needed.

The two-dimensional Hermite constant is
\(\gamma_2=2/\sqrt3\), so

\[
\lambda_1(L_C)^2\le\gamma_2 N.
\tag{6.5}
\]

If any shortest vector \(v\) has
\(\gcd(N,v_1,v_2)=p\), write \(v=py\).  Then

\[
0<\lVert y\rVert^2
\le\gamma_2\frac qp
\le\gamma_2\kappa.
\tag{6.6}
\]

The reduction \(y\bmod q\) is nonzero.  Otherwise \(q\) would divide both
coordinates of \(y\), so \(N\) would divide both coordinates of \(v=py\),
contrary to \(\gcd(N,v_1,v_2)=p\).  Membership \(v\in L_C\), reduced
modulo \(q\), therefore forces the well-defined projective equality

\[
[C\bmod q]=[y\bmod q].
\]

Define \(B_\kappa\) to be the number of primitive integer directions
\(\mathbb Z y_0\) admitting a nonzero primitive representative with
\(\lVert y_0\rVert^2\le\gamma_2\kappa\).  This is a constant depending
only on \(\kappa\).  Dividing \(y\) by its integer coordinate gcd can only
decrease its norm, and its reduction remains nonzero modulo \(q\).
Directions whose reductions collide or are isotropic only decrease the
number of supported lines.  Thus

\[
\Pr(\exists\text{ a shortest }v:
\gcd(N,v_1,v_2)=p)
\le \frac{B_\kappa}{|\mathcal S_q|}=O(1/q).
\tag{6.7}
\]

The symmetric event has probability \(O(1/p)\).  The bound concerns the
existence of any factor-revealing shortest vector, so it is independent of
tie-breaking.

P30 cannot be cited to supply the premise of (6.7).  It makes the row and
image line of \(\beta\bmod r\) uniform **conditional on fixed completion
data**.  It gives no uniformity theorem for the completion line
\([(z,w)]\) itself.  Consequently (6.7) kills a uniform free-cyclic output
model, not every residual-completion model.

## 7. CVP targets in the cyclic quotient

Write a public integer target uniquely as

\[
t=AC_0+BD.
\]

For any \(v=aC_0+NbD\in L_C\), the error is

\[
t-v=(A-a)C_0+(B-Nb)D.
\]

By (5.1),

\[
t-v\in L_{C,r}
\quad\Longleftrightarrow\quad
r\mid B
\quad\Longleftrightarrow\quad
t\in L_{C,r}.
\tag{7.1}
\]

Nearest-vector optimization can change the Euclidean size of the two
coefficients, but not \(B\bmod p\) or \(B\bmod q\).  If \(t\) is uniform
modulo \(N\), unimodularity makes \(B\) uniform modulo \(N\), and

\[
\Pr(r\mid B\text{ for exactly one }r\in\{p,q\})
=\frac1p+\frac1q-\frac2N.
\tag{7.2}
\]

This is exponentially small on balanced inputs.  The same statement holds
for CVP in the rotated rank-two lattice \(NL_C^*\) by (6.4).  It does not
extend to CVP in the original rank-\(m\) \(\Lambda_{\rm dual}(A,N)\).

A deliberately biased target distribution is not ruled out.  Equation (7.1)
pinpoints its burden: it must manufacture a public scalar \(B\) divisible
by exactly one unknown factor with inverse-polynomial probability.  CVP does
not amplify that probability.

## 8. Bit complexity

All reductions above are polynomial in the ordinary bit model.

- Smith and Hermite normal forms, determinantal divisors, and the displayed
  gcds have deterministic polynomial bit complexity for polynomial-size
  \(A\).
- The SNF transformations give polynomial-bit bases of \(E_{\rm out}\) and
  \(E_{\rm dual}\); their rational Gram matrices and exact orthogonal
  projection data are computable in polynomial bit complexity.
- Extended Euclid constructs \(C_0,D\) with polynomial-bit coefficients.
  If \(z,w\) have \(B\) bits, a standard Bezout choice for \(D\) has
  \(O(B)\) bits.
- The basis \((C_0,ND)\) has polynomial bit length.  Two-dimensional Gauss
  reduction gives exact SVP, and fixed-dimensional closest-vector
  enumeration gives exact CVP, in deterministic time polynomial in that bit
  length.
- The quotient maps, scalar coordinates \(a,b\), norms, gcds, and candidate
  divisions all have polynomial bit complexity.

This does not make exact SVP or CVP polynomial in a growing-dimensional
output/dual lattice.  Only the fixed-rank quotient has that guarantee.

## 9. Exact obstruction and surviving reopen condition

The kill-first conclusion is:

> The public output and P35 scaled-dual lattices are CRT intersections.
> Smith form either factors \(N\) before metric reduction or removes every
> hidden finite-quotient scale except public \(1,N\) invariant factors.
> Projecting off the resulting public primitive exact directions leaves
> exactly an \(N\)-scaled public projected ambient lattice, with local
> \(p\)- and \(q\)-scalings.  These general statements close the proposed
> determinant, faithful-quotient-shape, and uniform
> output-membership/CVP signals; they do not control full-lattice
> coordinate-gcd shortest vectors in arbitrary dimension.
> For a full fixed-residual four-square batch, the remaining output quotient
> is the cyclic lattice \(\mathbb ZC_0+N\mathbb ZD\); after its public exact
> direction is removed, it is one-dimensional, and the scaled Euclidean dual
> of this **rank-two quotient** is merely a rotation.  Uniform CVP targets in
> this quotient have exponentially small one-local mass.
> Under uniform local completion lines, factor-revealing shortest vectors
> in this quotient are also exponentially sparse on balanced inputs.

This closes neither the whole output/dual family nor the top-level factoring
problem.  For the cyclic quotient, the exact surviving scalar is the
coefficient \(a_*\) of a specified shortest or closest vector in (5.2).
An actual continuation of that quotient route is materially new only if it
proves, for a fully specified factor-free four-square completion or target
distribution,

\[
\Pr(1<\gcd(N,a_*)<N)\ge1/\operatorname{poly}(\log N)
\]

on every required input class, with ties, sample generation, and recursion
accounted for.  P30 does not give that distribution theorem.  Artificially
choosing \(C\) or a target from knowledge of a factor can plainly force the
event, so no deterministic impossibility claim for arbitrary biased inputs
is made.

Other materially new reopen mechanisms are a nonlinear combination whose
informative rational rank grows with the number of samples, or an affine
metric law not reducible to the two public scalar coordinates above.  A
specified **full-lattice** SVP/CVP or coordinate-gcd law for the original
\(N\mathbb Z^m+A^{\mathsf T}\mathbb Z^4\), with inverse-polynomial
factor extraction, also remains materially open; merely projecting off its
public exact directions is covered by (2.9).  Adding fixed-residual samples,
taking the scaled Euclidean dual \(NL_C^*\), applying SVP/CVP to \(L_C\), or
sampling uniform quotient targets is covered by this obstruction.
