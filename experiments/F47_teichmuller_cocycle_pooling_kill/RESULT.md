# F47 — canonical Teichmüller high digits: multiplicative cocycle pooling kill

**Family:** F12, following X16/P22.

**Status:** self-audited.

**Method:** preregistered proof-only mandatory kill test. No mathematical
computation was run, and no canonical durable-state file was changed.

## Verdict

The proposed multiplicative inconsistency decoder is killed exactly, but only
in its linear cocycle form. For every \(N\ge2\), exponentiation by \(N\) gives a
well-defined homomorphism

\[
A:(\mathbb Z/N\mathbb Z)^\times\longrightarrow
  (\mathbb Z/N^2\mathbb Z)^\times,
\qquad A(a)=a^N,
\]

and its reduction \(x\) modulo \(N\) is also a homomorphism. If

\[
A(a)=x(a)+Nh(a),\qquad
\lambda(a)=h(a)x(a)^{-1}\pmod N,
\]

using canonical representatives for \(A\) and \(x\), then every pair of unit
bases satisfies

\[
\boxed{
\lambda(ab)=\lambda(a)+\lambda(b)
 +c(x(a),x(b))x(ab)^{-1}\pmod N,}
\]

where

\[
c(x,y)=\frac{xy-\langle xy\rangle_N}{N}
\]

is the public canonical base-\(N\) carry. Consequently, on every finite network
of genuine multiplicative relations, the observed public values
\(\lambda(a)\) form one global solution of all edge equations over
\(\mathbb Z/N\mathbb Z\). Every edge residual, every ring-linear combination of
edge residuals, and every linear cycle-compatibility syndrome is therefore zero
modulo \(N\), and remains zero modulo every divisor of \(N\). There cannot be a
local-consistency mismatch between unknown CRT components in this system.

This does **not** imply that coefficient-matrix ranks at different primes,
matrix minors, Smith data, arbitrary eliminants, integer quotients of modularly
zero residuals, collision statistics, or nonlinear graph processing agree.
Those are not residual-consistency tests. No factor and no factoring algorithm
are obtained.

For squarefree \(N\), \(A\) is determined by \(x\), so equal \(x\)-values may be
merged. For nonsquarefree inputs this can fail: occurrence labels are mandatory.
The precise local reason is that a repeated odd prime, or a factor \(2^e\) with
\(e\ge3\), leaves a principal-unit coordinate in \(A\bmod p^{2e}\) which is
erased from \(x\bmod p^e\).

## 1. Well-definedness before any cocycle argument

Write \(\langle t\rangle_M\in[0,M)\) for the canonical representative of
\(t\bmod M\), and put

\[
G_N=(\mathbb Z/N\mathbb Z)^\times.
\]

Let \(a\in G_N\), and let \(r\in\mathbb Z\) be any representative of it. If
\(r'=r+kN\), the binomial theorem gives

\[
(r+kN)^N-r^N
=N r^{N-1}kN
+\sum_{j=2}^{N}\binom Nj r^{N-j}(kN)^j
\equiv0\pmod{N^2}.
\tag{1.1}
\]

Thus replacement of a representative **before** exponentiation does not change
the residue modulo \(N^2\). This proof includes even \(N\) and \(N=2\); it uses
no squarefreeness assumption. Define

\[
A(a)=\langle r^N\rangle_{N^2}.
\tag{1.2}
\]

Because \(r\) is coprime to \(N\), \(A(a)\) is a unit modulo \(N^2\).

For \(a,b\in G_N\), take representatives \(r,s\). Any representative of the
product class \(ab\) differs from \(rs\) by a multiple of \(N\), so (1.1) gives

\[
A(ab)=\langle (rs)^N\rangle_{N^2}
=\langle A(a)A(b)\rangle_{N^2}.
\tag{1.3}
\]

Hence \(A\), understood as a residue-class-valued map, is a homomorphism. Its
canonical integer representatives need not multiply without a final reduction.

Now define

\[
x(a)=\langle A(a)\rangle_N=\langle r^N\rangle_N.
\tag{1.4}
\]

Reduction modulo \(N\) is a homomorphism, so

\[
x(ab)=\langle x(a)x(b)\rangle_N,
\tag{1.5}
\]

and \(x(a)\in G_N\). Finally, because \(A(a)\in[0,N^2)\) and
\(x(a)\in[0,N)\), there is a unique \(h(a)\in[0,N)\) such that

\[
A(a)=x(a)+Nh(a).
\tag{1.6}
\]

Thus \(h\) is always a well-defined function of the **base class** \(a\). It is
not yet legitimate to regard it as a function of the possibly colliding value
\(x(a)\).

## 2. Exact canonical-carry and normalized laws

Fix \(a,b\in G_N\), and abbreviate

\[
x=x(a),\quad y=x(b),\quad
z=\langle xy\rangle_N=x(ab),\quad
c=c(x,y)=\frac{xy-z}{N}.
\tag{2.1}
\]

These are exact integer definitions. Since \(1\le x,y\le N-1\), the carry is
an integer in \(0\le c\le N-2\). It is public, and \(z\) is a unit. Expanding
(1.6) gives

\[
\begin{aligned}
A(a)A(b)
&=(x+Nh(a))(y+Nh(b))\\
&\equiv z+N\{c+xh(b)+yh(a)\}\pmod{N^2}.
\end{aligned}
\tag{2.2}
\]

Comparison with \(A(ab)=z+Nh(ab)\) proves the exact high-digit law

\[
\boxed{
h(ab)\equiv c(x,y)+xh(b)+yh(a)\pmod N.}
\tag{2.3}
\]

The statement is a congruence, not necessarily equality between the displayed
canonical integers: reducing the product modulo \(N^2\) may remove a multiple of
\(N^2\).

Because every \(x(a)\) is a unit, define the public normalized digit

\[
\lambda(a)=h(a)x(a)^{-1}\pmod N
\tag{2.4}
\]

and the public normalized carry

\[
\kappa(x,y)=c(x,y)\langle xy\rangle_N^{-1}\pmod N.
\tag{2.5}
\]

Multiplying (2.3) by \(z^{-1}\), and using
\(z^{-1}x=y^{-1}\) and \(z^{-1}y=x^{-1}\) modulo \(N\), yields

\[
\boxed{
\lambda(ab)=\lambda(a)+\lambda(b)+\kappa(x(a),x(b))
\pmod N.}
\tag{2.6}
\]

This normalization is also the coordinate identity

\[
A(a)=x(a)\{1+N\lambda(a)\}\pmod{N^2}.
\tag{2.7}
\]

The canonical section \(u\mapsto u\in[0,N)\subset\mathbb Z/N^2\mathbb Z\)
has factor set \(\kappa\). Associativity of multiplication in
\((\mathbb Z/N^2\mathbb Z)^\times\) therefore gives, for all
\(x,y,w\in G_N\),

\[
\kappa(x,y)+\kappa(\langle xy\rangle_N,w)
=\kappa(y,w)+\kappa(x,\langle yw\rangle_N)
\pmod N.
\tag{2.8}
\]

Thus \(\kappa\) is the ordinary central \(2\)-cocycle of the canonical section.
Under the convention
\(\delta\lambda(a,b)=\lambda(ab)-\lambda(a)-\lambda(b)\), equation (2.6) says
that its pullback along the homomorphism \(x:G_N\to G_N\) is the coboundary of
the observed \(1\)-cochain \(\lambda\). Equation (2.8) can also be checked by
expanding the two parenthesizations of \(xyw\); no local prime or factorization
is being used.

## 3. Occurrence-labelled relation graphs and the decoder that is killed

A finite directed multiplicative relation graph consists of:

- a finite set \(V\) of **occurrences**, each carrying a public unit base
  \(a_v\in G_N\);
- a finite multiset \(E\) of directed multiplier edges, with maps
  \(s,m,t:E\to V\), such that

  \[
  a_{t(e)}=a_{s(e)}a_{m(e)}\quad\text{in }G_N.
  \tag{3.1}
  \]

One may view \(e\) as the directed edge \(s(e)\to t(e)\), labelled by the
multiplier occurrence \(m(e)\). Loops, repeated edges, repeated products, and
multiple occurrences of the same base are allowed.

For each vertex compute the public triple
\((x_v,h_v,\lambda_v)\). For an edge put

\[
\begin{aligned}
z_e&=\langle x_{s(e)}x_{m(e)}\rangle_N=x_{t(e)},\\
c_e&=\frac{x_{s(e)}x_{m(e)}-z_e}{N},\\
\kappa_e&=c_ez_e^{-1}\pmod N.
\end{aligned}
\tag{3.2}
\]

The carry is part of the edge label; omitting it changes the equation and can
manufacture a false syndrome.

Let \(R=\mathbb Z/N\mathbb Z\), and define \(B\in R^{E\times V}\) by giving row
\(e\) coefficient \(+1\) at \(t(e)\), coefficient \(-1\) at \(s(e)\), and
coefficient \(-1\) at \(m(e)\), adding coefficients when roles coincide. Then
(2.6) is exactly

\[
\boxed{B\lambda=\kappa\quad\text{in }R^E.}
\tag{3.3}
\]

Equivalently, every normalized edge residual

\[
r_e=\lambda_{t(e)}-\lambda_{s(e)}-\lambda_{m(e)}-\kappa_e
\tag{3.4}
\]

is zero modulo \(N\). The unnormalized residual

\[
\rho_e=h_{t(e)}-x_{s(e)}h_{m(e)}-x_{m(e)}h_{s(e)}-c_e
\tag{3.5}
\]

is likewise an integer multiple of \(N\).

This proves all of the following without a probabilistic assumption.

1. For every matrix \(L\) over \(R\), even one selected adaptively from the
   whole public transcript,

   \[
   L(B\lambda-\kappa)=0.
   \tag{3.6}
   \]

   Hence every ring-linear pooling of edge residuals is zero.

2. If \(\alpha^TB=0\), then

   \[
   \alpha^T\kappa=\alpha^TB\lambda=0.
   \tag{3.7}
   \]

   Thus every linear triangle, path, or cycle syndrome obtained by eliminating
   vertex variables is zero. The associativity triangle is the special case
   (2.8).

3. Reducing (3.3) modulo any divisor \(d\mid N\) gives a solution there. In
   particular the edge system cannot be consistent modulo one hidden prime and
   inconsistent modulo another.

4. For every prime \(p\mid N\), the augmented matrix satisfies

   \[
   \operatorname{rank}_{\mathbb F_p}[B\mid\kappa]
   =\operatorname{rank}_{\mathbb F_p}B,
   \tag{3.8}
   \]

   because the appended column is \(B\lambda\). This is only the usual
   coefficient-versus-augmented consistency statement within one field.

The killed decoder is therefore precise: it is any decoder whose proposed
factor signal is a nonzero local edge residual, an \(R\)-linear combination of
such residuals, a linear cycle compatibility failure, or an
augmented-versus-coefficient inconsistency of the genuine affine edge system.
The canonical representative of each such residual is \(0\), so taking its gcd
with \(N\) returns \(N\), not a proper factor.

Existence of the solution \(\lambda\) says nothing about whether
\(\operatorname{rank}(B\bmod p)\) equals
\(\operatorname{rank}(B\bmod q)\). It says still less about ranks of the
unnormalized coefficient matrix containing \(x\)-values, arbitrary minors,
Smith invariants, resultants or other eliminants, or nonlinear functions of the
graph transcript. Those quantities are not linear residual syndromes and are
not killed by (3.3).

## 4. Squarefree odd inputs: the exact local Teichmüller meaning

Assume now that \(N\) is squarefree and odd. Fix \(p\mid N\), and write

\[
N=pm,\qquad p\nmid m.
\]

For \(u\in\mathbb F_p^\times\), let
\([u]_p\in(\mathbb Z/p^2\mathbb Z)^\times\) be its Teichmüller lift,
characterized by

\[
[u]_p\equiv u\pmod p,\qquad [u]_p^{p-1}=1.
\]

Choose any unit lift of \(a\) modulo \(p^2\), and write it uniquely as

\[
a=[a\bmod p]_p(1+pt).
\]

Then

\[
(1+pt)^{pm}\equiv1\pmod{p^2},
\qquad [a\bmod p]_p^{pm}=[a\bmod p]_p^m,
\]

because the Teichmüller factor is fixed by the \(p\)-power map. Therefore

\[
\boxed{
A(a)\equiv[a\bmod p]_p^{\,N/p}
       =[x(a)\bmod p]_p\pmod{p^2}.}
\tag{4.1}
\]

This holds for every prime divisor \(p\), not just for a semiprime. CRT over the
pairwise coprime moduli \(p^2\) shows that \(A(a)\bmod N^2\) is the unique tuple
of local Teichmüller lifts of \(x(a)\bmod N\).

There is also an exact local formula for the normalized public digit. For the
canonical global integer \(x=x(a)\in[0,N)\), define

\[
q_p(x)=\frac{[x\bmod p]_p-x}{p}\pmod p.
\tag{4.2}
\]

The quotient is well defined modulo \(p\): changing an integer representative
of the Teichmüller class by \(p^2\) changes it by a multiple of \(p\). Reducing
\(A=x+Nh\) modulo \(p^2\) and using (4.1) gives

\[
h(a)\equiv m^{-1}q_p(x)\pmod p,
\qquad
\boxed{
\lambda(a)\equiv m^{-1}x^{-1}q_p(x)\pmod p.}
\tag{4.3}
\]

Thus the apparently local Teichmüller correction is exactly the reduction of
one global public assignment. To see the carry explicitly, let
\(z=\langle xy\rangle_N\) and \(c=(xy-z)/N\). Multiplicativity of Teichmüller
lifts gives

\[
q_p(z)\equiv mc+xq_p(y)+yq_p(x)\pmod p.
\tag{4.4}
\]

After multiplication by \(m^{-1}z^{-1}\), (4.4) is precisely (2.6) modulo
\(p\). Different hidden primes therefore do not receive incompatible cocycles;
they receive reductions of the same canonical carry equation.

An important collision consequence follows. If \(x(a)=x(b)\) as residues
modulo squarefree \(N\), then (4.1) gives
\(A(a)=A(b)\) modulo every \(p^2\mid N^2\), hence modulo \(N^2\). Consequently

\[
x(a)=x(b)\Longrightarrow h(a)=h(b),\ \lambda(a)=\lambda(b)
\quad(N\text{ squarefree}).
\tag{4.5}
\]

The exponent map \(a\mapsto x(a)\) need not be injective; nevertheless it is
safe in the squarefree case to quotient occurrences by their common \(x\)-value.
Equivalently, on the image \(x(G_N)\), \(\lambda\) is a genuine function and
\(\kappa\) restricts to its coboundary.

If \(2\mid N\) but \(N\) remains squarefree, the omitted local factor is
harmless and trivial: every unit is odd, \(N\) is even, and
\(a^N\equiv1\pmod4\). Since \(\mathbb F_2^\times=\{1\}\), this is exactly its
unique Teichmüller lift. Oddness was used above only to write the standard
\(1+p\mathbb Z_p\) decomposition.

## 5. What changes at \(p^e\parallel N\)

Let \(p^e\parallel N\) and \(m=N/p^e\), so \(p\nmid m\). The relevant CRT
component of \(A\) is now modulo \(p^{2e}\), not merely modulo \(p^2\).

### 5.1 Odd \(p\)

Choose any lift of the unit base to \(\mathbb Z/p^{2e}\mathbb Z\), and write

\[
a=\omega\eta,\qquad
\omega=[a\bmod p]_p,\qquad
\eta\in1+p\mathbb Z_p,
\]

where \(\omega\) is taken to Teichmüller precision \(p^{2e}\). Then

\[
\boxed{
A(a)\equiv \omega^m\eta^{p^e m}\pmod{p^{2e}},
\qquad
x(a)\equiv\omega^m\pmod{p^e}.}
\tag{5.1}
\]

The first identity uses \(\omega^{p^e}=\omega\); the second uses
\(\eta^{p^e m}\equiv1\pmod{p^{e+1}}\). Changing the chosen lift of \(a\) by a
multiple of \(p^e\) does not change (5.1) modulo \(p^{2e}\), consistently with
the global proof (1.1).

More precisely, the principal-unit power map

\[
\frac{1+p\mathbb Z_p}{1+p^e\mathbb Z_p}
\longrightarrow
\frac{1+p^{e+1}\mathbb Z_p}{1+p^{2e}\mathbb Z_p},
\qquad \eta\longmapsto\eta^{p^e m},
\tag{5.2}
\]

is an isomorphism. The \(p\)-adic logarithm identifies it with multiplication
by \(p^e m\) from
\(p\mathbb Z_p/p^e\mathbb Z_p\) to
\(p^{e+1}\mathbb Z_p/p^{2e}\mathbb Z_p\). Both groups have order
\(p^{e-1}\), and \(m\) is a unit. Thus:

- for \(e=1\), the principal factor is trivial and (4.1) is recovered;
- for every \(e\ge2\), \(x\bmod p^e\) erases the entire principal coordinate
  of the input modulo \(p^e\), while \(A\bmod p^{2e}\) retains it bijectively in
  the subgroup \(1+p^{e+1}\mathbb Z_p\).

The failure of descent from \(a\) to \(x\) is real. For the symbolic family
\(N=p^2\) with odd \(p\), take \(a=1\) and \(b=1+p\) modulo \(p^2\). Then

\[
x(a)=x(b)=1,
\]

but the binomial theorem gives

\[
A(a)=1,\qquad
A(b)=(1+p)^{p^2}\equiv1+p^3\pmod{p^4}.
\]

Hence \(h(a)=0\) while \(h(b)=p\pmod{p^2}\). Merging these two occurrences
solely because their \(x\)-values collide would impose a false equality.

### 5.2 The prime \(2\)

Let \(2^e\parallel N\), so \(m=N/2^e\) is odd.

- If \(e=1\), every odd \(a\) satisfies \(a^N\equiv1\pmod4\).
- If \(e=2\), every odd \(a\) satisfies \(a^N\equiv1\pmod{16}\), because
  \(4\mid N\) and \(a^4\equiv1\pmod{16}\).
- If \(e\ge3\), write the \(2\)-adic unit uniquely as

  \[
  a=(-1)^\epsilon\eta,\qquad \eta\in1+4\mathbb Z_2.
  \]

  The sign is killed and

  \[
  \boxed{
  A(a)\equiv\eta^{2^e m}\pmod{2^{2e}},
  \qquad x(a)\equiv1\pmod{2^e}.}
  \tag{5.3}
  \]

  Via the \(2\)-adic logarithm on \(1+4\mathbb Z_2\), exponentiation induces an
  isomorphism

  \[
  \frac{1+4\mathbb Z_2}{1+2^e\mathbb Z_2}
  \xrightarrow{\ \sim\ }
  \frac{1+2^{e+2}\mathbb Z_2}{1+2^{2e}\mathbb Z_2}.
  \tag{5.4}
  \]

  Thus \(A\) retains the \(e-2\) signless principal bits which \(x\) erases.

Combining the local statements gives an exact global criterion: as a function
on all unit inputs, \(A\) (and therefore \(h\)) is determined by \(x\) if and
only if the odd part of \(N\) is squarefree and \(8\nmid N\). For a squarefree
input this always holds. If an odd square divides \(N\), or if \(8\mid N\), CRT
lets one vary the retained local principal coordinate while fixing every other
local coordinate, producing equal global \(x\)-values and unequal global
\(A\)-values.

The universal laws (2.3) and (2.6) do not change at prime powers. What changes
is only whether \(h\) and \(\lambda\) descend from base occurrences to
\(x\)-vertices. On general \(N\), the safe graph is the occurrence-labelled
graph of Section 3. Same-base occurrences can always be identified by
well-definedness of \(A\); same-\(x\) occurrences cannot generally be identified.

## 6. Boundary and complexity audit

**Units.** The unnormalized law (2.3) extends formally wherever the products
are defined, but normalization requires \(x^{-1}\bmod N\), hence a unit base.
If a proposed sampler produces a nonunit \(a\), computing
\(\gcd(a,N)\) already either rejects it or returns a factor. This result makes no
claim about a separate nonunit decoder.

**Canonical carries.** The formulas use \(x,y,z\in[0,N)\) and the exact integer
carry in (2.1). Replacing this section by arbitrary lifts changes both the high
digit and its factor set. A coherent alternative section has its own coboundary
law, but noncanonical input lifts or proposed extra lift data are not analyzed
here.

**Collisions and repeated products.** Equal base classes have equal
\((A,x,h,\lambda)\) for every \(N\), so repeated product occurrences may be tied
together. Equal \(x\)-values alone may be tied together for squarefree \(N\) by
(4.5), but not for general \(N\). Multiple multiplication paths to the same
base give valid cycle equations and are already covered by (3.7). Multiple
paths whose endpoints merely have the same \(x\)-value must retain distinct
endpoints in the nonsquarefree case.

**Uniform bit complexity.** Let
\(n=\lceil\log_2(N+1)\rceil\). For each base, binary modular exponentiation
computes \(A=a^N\bmod N^2\) with \(O(n)\) multiplications and reductions on
\(O(n)\)-bit integers. Classical schoolbook arithmetic therefore gives the
explicit bound \(O(n^3)\) bit operations per vertex. Exact division for \(h\)
and extended Euclid for \(x^{-1}\bmod N\) also take \(O(n^2)\) bit operations
with classical algorithms. Each edge needs one product \(xy<N^2\), one exact
division by \(N\), and \(O(1)\) modular operations, hence \(O(n^2)\) bit
operations. Reducing after every operation keeps every value and every linear
syndrome at \(O(n)\) bits. Given a graph with \(V\) vertices and \(E\) edges,
the public transcript and all residuals are therefore computed in
\(O(Vn^3+En^2)\) bit operations and polynomial space. If \(V,E\) and the
factor-free relation-generation procedure are polynomial in \(n\), this is
uniform polynomial time. No unknown factor or local Teichmüller lift is needed;
the local formulas in Sections 4--5 are proofs, not factor-aware subroutines.

## 7. Material comparison with P22 and exact open scope

P22/X16 proves a probabilistic obstruction: on an infinite balanced
distinct-odd-semiprime family, direct gcds of any fixed polynomial-size list of
canonical high digits from one uniform base have exponentially small success.
It expressly leaves cross-base constructions open.

F47 is materially broader in base selection and relation structure but narrower
in what it rules out. The identity here is deterministic, applies to arbitrary
\(N\), and permits any finite collection of multiplicatively related unit bases,
including adaptive, engineered, and nonuniform choices. Such choices cannot
create an inconsistency in the genuine linear carry-cocycle equations. Unlike
P22, however, F47 gives no rarity bound for the individual digits and no
distributional statement at all.

The following remain open because they are not logically forced to synchronize
by existence of the solution (3.3):

- additive triples and other nonmultiplicative relations;
- nonlinear statistics of \(h,\lambda,x\), collision fibres, or whole graphs;
- engineered or adaptive nonuniform bases used by any decoder other than the
  killed residual-inconsistency decoder;
- inversion or partial inversion of the power map \(a\mapsto x(a)\);
- coefficient-matrix ranks across different CRT fields, minors, Smith data,
  arbitrary eliminants, and rank-based selectors not equivalent to testing
  augmented-system consistency;
- division by \(N\) of a canonically chosen integer residual which is already
  \(0\bmod N\), and other higher-carry operations;
- noncanonical lifts, extra input lift data, and levels beyond \(N^2\);
- occurrence-collision information on nonsquarefree inputs; and
- any proposed all-input success probability, recursion, or factoring theorem.

Accordingly the exact verdict is **method failure for multiplicative
linear-cocycle inconsistency pooling**, not evidence against all cross-base
\(N^2\)-adic constructions and not a factoring result.
