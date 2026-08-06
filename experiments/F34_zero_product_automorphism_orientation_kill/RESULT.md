# F34 kill-first: zero-product automorphisms cannot desynchronize CRT axes without exposing a factor

**Status:** promoted as P44 after an amendment-verified hostile audit and a
fresh context-free proof-blind reconstruction.

**Family:** F23.

**Closest prior routes and material difference.**  F32 identifies the
quadratic-energy law, while F33 lifts it to uniform sampling from

\[
\Omega_N=\{(k,x)\in(\mathbb Z/N\mathbb Z)^2:kx=0\}.
\]

F33 tests coordinate heat bath.  The present report tests a genuinely
nonlocal alternative: make large moves by applying explicit algebraic
automorphisms of the zero-product variety.  This is also distinct from P15's
scalar phase-carrier rank theorem.  Here the obstruction is the permutation
of the two irreducible axes of a nodal scheme.

**Classification.**  This is evidence against the exact auxiliary claim that
a mixture of explicit \((\mathbb Z/N\mathbb Z)\)-algebra automorphisms of
\(kx=0\) can manufacture the independent local axis orientations needed for
factor-revealing pairs.  It is not evidence against noninvertible maps,
finite-set permutation polynomials, auxiliary-state chains, or general
nonlocal proposals.

No computation was used.

## Outcome

Let \(N=pq\) for distinct primes, put \(R=\mathbb Z/N\mathbb Z\), and let

\[
A_R=R[K,X]/(KX).
\]

Every \(R\)-algebra automorphism fixes the ideal \((K,X)\), as proved below.
For such an automorphism \(\Phi\), write its coordinate images intrinsically
in the quotient \(A_R/(K,X)^2\) as

\[
\begin{pmatrix}\Phi(K)\\ \Phi(X)\end{pmatrix}
\equiv
J_\Phi
\begin{pmatrix}K\\X\end{pmatrix}
\pmod{(K,X)^2},
\qquad
J_\Phi=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in M_2(R).
\tag{0.1}
\]

Over each of \(\mathbb F_p\) and \(\mathbb F_q\), the reduced automorphism
either preserves the two axes, in which case its matrix in (0.1) is diagonal
with nonzero diagonal entries, or swaps the axes, in which case it is
antidiagonal with nonzero antidiagonal entries.

There is an exact dichotomy.

1. If the two local axis permutations differ, one of
   \(\gcd(N,a),\gcd(N,b),\gcd(N,c),\gcd(N,d)\) is a proper divisor of \(N\).
2. If none of those four gcds is proper, the local axis permutations agree.
   In fact \(\Phi\) is globally either

   \[
   (K,X)\longmapsto(uK,vX)
   \quad\text{or}\quad
   (K,X)\longmapsto(uX,vK)
   \tag{0.2}
   \]

   for units \(u,v\in R^\times\).

Thus an explicit automorphism that desynchronizes the two CRT components
already contains a factor in its linear coefficients.  On the no-factor
branch, every automorphism merely rescales the two axes or swaps them
**synchronously**.

The non-factor-revealing part of \(\Omega_N\) is

\[
\mathcal A_N
=(R^\times\times\{0\})
\mathbin{\dot\cup}(\{0\}\times R^\times)
\mathbin{\dot\cup}\{(0,0)\}.
\tag{0.3}
\]

It is invariant under every automorphism on the no-factor branch.  Therefore
an adaptive random walk that starts in \(\mathcal A_N\) and whose only moves
are explicit \(R\)-algebra automorphisms either exposes a factor in a
Jacobian entry or never reaches a pair with a proper coordinate gcd.

This is incompatible with approximate uniform sampling.  For \(N=pq\),

\[
|\Omega_N|=(2p-1)(2q-1),
\qquad
|\Omega_N\setminus\mathcal A_N|=2N-2,
\tag{0.4}
\]

so uniform \(\Omega_N\) gives factor-revealing pairs mass

\[
\frac{2N-2}{(2p-1)(2q-1)}>\frac12.
\tag{0.5}
\]

Every law supported on \(\mathcal A_N\) is therefore at total-variation
distance greater than \(1/2\) from uniform.  Automorphism mixtures do not
provide the missing F32 sampler.

## 1. Automorphisms of the node over a field

Let \(F\) be any field and set

\[
A_F=F[K,X]/(KX).
\]

The two minimal prime ideals are

\[
P_K=(K),\qquad P_X=(X).
\tag{1.1}
\]

Indeed, the two quotients are polynomial rings in one variable, and
\(KX\) is squarefree.  Their sum

\[
\mathfrak m=P_K+P_X=(K,X)
\tag{1.2}
\]

is therefore fixed by every \(F\)-algebra automorphism: an automorphism
permutes the two minimal primes and hence fixes their sum.  Geometrically,
the node is fixed.

An automorphism has only two possible component permutations.

### 1.1 Axis-preserving case

Suppose \(\phi(P_K)=P_K\) and \(\phi(P_X)=P_X\).  The induced automorphisms
on

\[
A_F/P_X\simeq F[K],
\qquad
A_F/P_K\simeq F[X]
\]

fix the origin.  Every automorphism of \(F[T]\) is affine linear: if
\(f\) and \(g\) are inverse substitution polynomials, then
\(\deg(f\circ g)=\deg f\deg g=1\).  Fixing zero removes the translation.
Consequently the two quotient maps are

\[
K\longmapsto uK,qquad X\longmapsto vX
\]

for \(u,v\in F^\times\).

Also \(P_K\cap P_X=0\) in \(A_F\).  Since \(\phi(K)\in P_K\) and its
image modulo \(P_X\) is \(uK\), their difference lies in both minimal
primes and is zero.  The same argument applies to \(X\).  Hence

\[
\phi(K)=uK,qquad \phi(X)=vX.
\tag{1.3}
\]

### 1.2 Axis-swapping case

If the two minimal primes are exchanged, the same quotient argument gives

\[
\phi(K)=uX,qquad \phi(X)=vK
\tag{1.4}
\]

for nonzero \(u,v\).  Equations (1.3)--(1.4) classify all
\(F\)-algebra automorphisms of the node.

In particular, the induced map on \(\mathfrak m/\mathfrak m^2\) is
respectively a nonsingular diagonal or nonsingular antidiagonal matrix.

## 2. CRT orientation dichotomy

Return to \(R=\mathbb Z/pq\mathbb Z\).  Reducing an \(R\)-algebra
automorphism and its inverse modulo \(r\in\{p,q\}\) gives an automorphism
of

\[
A_r=\mathbb F_r[K,X]/(KX).
\]

Section 1 shows that the reductions of \(\Phi(K)\) and \(\Phi(X)\) have
zero constant term in both field components.  CRT therefore gives
\(\Phi(K),\Phi(X)\in(K,X)\) globally.  Applying the same argument to
\(\Phi^{-1}\) proves that \((K,X)\) is fixed.  The canonical quotient

\[
A_R\longrightarrow A_R/(K,X)^2
\]

then makes the constant and linear parts independent of every choice of
polynomial representative: the relation \(KX\) already lies in
\((K,X)^2\).  Thus \(J_\Phi\) in (0.1) is intrinsic, and Section 1 applies
to both of its field reductions.

Suppose, for example, that \(\Phi_p\) preserves the axes while \(\Phi_q\)
swaps them.  Then

\[
\begin{array}{c|cccc}
&a&b&c&d\\ \hline
\bmod p&\ne0&0&0&\ne0\\
\bmod q&0&\ne0&\ne0&0.
\end{array}
\tag{2.1}
\]

Thus

\[
\gcd(N,a)=\gcd(N,d)=q,
\qquad
\gcd(N,b)=\gcd(N,c)=p.
\tag{2.2}
\]

The opposite mixed orientation interchanges \(p\) and \(q\).  Hence every
mixed-orientation automorphism exposes a proper factor through (0.1).

Conversely, assume all four gcds are trivial, meaning each is either \(1\)
or \(N\).  A coefficient is then nonzero in both fields or zero in both.
The support pattern of the two local monomial matrices must agree, so the
local orientations are synchronized.

The field classification also proves the stronger global statement (0.2).
If both local maps preserve axes, choose the CRT lifts \(u,v\in R^\times\)
of the corresponding nonzero local scalars.  Both field components of the
elements \(\Phi(K)-uK\) and \(\Phi(X)-vX\) vanish.  Injectivity of
\(A_R\simeq A_{\mathbb F_p}\times A_{\mathbb F_q}\) makes the elements
themselves zero.  The swapping case is identical.  No nonlinear term
survives.

For an explicit division-free straight-line circuit over \(R\), with
\(+,-,\times\) gates and explicitly specified residue constants, the four
entries of \(J_\Phi\) are computable without expanding a high-degree circuit.
Evaluate each gate in \(A_R/(K,X)^2\), storing the triple
\((c,\alpha,\beta)\) for \(c+\alpha K+\beta X\).  Multiplication is

\[
(c,\alpha,\beta)(c',\alpha',\beta')
=(cc',\ c\alpha'+c'\alpha,\ c\beta'+c'\beta).
\tag{2.3}
\]

The output linear coefficients are \(J_\Phi\).  This costs a constant number
of ring operations per gate and bit time polynomial in \(\log N\) plus the
encoded circuit length.  It is polynomial in the factoring input length
when a uniform sampler constructs circuits whose size and constant encoding
length are \(\operatorname{poly}(\log N)\).  Division/rational circuits,
branching programs, and black-box evaluators are not included.  The theorem
is conditional on the maps really being algebra automorphisms; efficiently
certifying that promise is a separate issue, not an escape from (2.2).

## 3. The factor-free region is invariant

For a residue \(z\bmod N\), failure of \(\gcd(z,N)\) to reveal a proper
factor means exactly that \(z\) is a unit or \(z=0\).  If \((k,x)\in
\Omega_N\) and neither coordinate reveals a factor, the product constraint
excludes two units.  The only possibilities are exactly the three disjoint
sets in (0.3).

A synchronized map (0.2) preserves units and zero, and hence maps
\(\mathcal A_N\) to itself.  This remains true for a swap.  Therefore, for
an arbitrary adaptive sequence \(\Phi_1,\Phi_2,\ldots\):

- if some selected map has different local orientations, (2.2) factors
  \(N\) before the move is needed;
- otherwise every selected map preserves \(\mathcal A_N\), regardless of
  how it was chosen from the preceding public history.

As far as local-axis orientation is concerned, randomizing over
automorphisms only randomizes a **global** preserve/swap bit.  Unit scalings
may vary too, but they never manufacture independent CRT orientation bits.

## 4. Uniform target mass and total variation

For fixed \(k\bmod N\), the annihilator equation \(kx=0\) has
\(\gcd(k,N)\) solutions.  Thus

\[
|\Omega_N|=S(N):=\sum_{k\bmod N}\gcd(k,N).
\tag{4.1}
\]

The sum is multiplicative, and \(S(r)=2r-1\) at a prime \(r\).  Hence

\[
S(pq)=(2p-1)(2q-1).
\tag{4.2}
\]

The three pieces in (0.3) have total cardinality

\[
2\varphi(N)+1
=2(p-1)(q-1)+1.
\tag{4.3}
\]

Subtracting (4.3) from (4.2) gives \(2N-2\), proving (0.4).  Moreover

\[
2(2N-2)-(2p-1)(2q-1)
=2p+2q-5>0,
\]

which proves (0.5).

If \(\mu\) is supported on \(\mathcal A_N\) and \(\pi\) is uniform on
\(\Omega_N\), then the event \(\Omega_N\setminus\mathcal A_N\) has
\(\mu\)-mass zero and \(\pi\)-mass greater than one half.  Therefore

\[
\|\mu-\pi\|_{\mathrm{TV}}>\frac12.
\tag{4.4}
\]

This conclusion is independent of mixing-time estimates: the proposed move
family is reducible on its factor-free branch.

## 5. Exact scope and reopen condition

The obstruction covers an adaptive or random mixture of explicit
\(R\)-algebra automorphisms of the affine scheme \(KX=0\), started from a
pair whose coordinate gcds are trivial.  It allows arbitrarily high degree
in the submitted division-free circuits, arbitrary unit scalings, and any
public rule for choosing the next automorphism.  Extraction time is measured
in the encoded circuit length; a polynomial-time factoring proposal must
construct circuits of size \(\operatorname{poly}(\log N)\).

It does **not** cover:

1. noninvertible endomorphisms or stochastic kernels not decomposed into
   algebra automorphisms;
2. polynomial maps that are permutations only of the finite set
   \(\Omega_N\) but are not automorphisms of its coordinate algebra;
3. auxiliary variables, lifted state spaces, tempering, projections, or
   nonreversible moves;
4. an initializer that already returns a proper-coordinate-gcd pair with
   inverse-polynomial probability—that initializer is itself a factoring
   routine;
5. division/rational circuits, branch-dependent programs, or opaque
   black-box maps from which the first-order coefficients cannot be
   accessed; or
6. prime powers and nonsquarefree moduli.

The obstruction on distinct semiprimes nevertheless refutes a claimed
**all-input automorphism-only sampler in this explicit, factor-free-start
model**, because such a sampler must also work on every distinct semiprime.
It does not refute an all-input sampler using any excluded move type above.

A retry is materially new only if it gives one of the excluded move types
with a proved stationary law and polynomial bit/fair-bit implementation, or
if it finds an explicit automorphism contradicting the axis classification.
Merely composing, randomizing, or adaptively selecting more node
automorphisms is covered.
