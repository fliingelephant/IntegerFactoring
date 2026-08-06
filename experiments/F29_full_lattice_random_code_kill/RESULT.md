# F29 kill-first report: the uniform full-lattice random-code model

**Status:** promoted as P39 after a corrected hostile audit, clean re-audit,
and strict proof-blind reconstruction.

**Family:** F19.

**Closest prior route and material difference.**  P35/X29 treats the public
zero-syndrome lattice.  The corrected F27 candidate treats the public output
and scaled-dual lattices after their public primitive exact directions are
orthogonally removed.  It deliberately leaves open a metric optimizer in the
original full lattice, where those exact directions can couple
nonorthogonally to the faithful quotient.  The present report analyzes that
full-lattice question in the clean model where the two local code subspaces
are independent and uniform.  It does not project the exact directions away.

**Classification.**  This is evidence against the exact auxiliary claim that
merely increasing the number of uniform local relations makes a
factor-divisible slice win exact SVP.  It is not a lattice lower bound and is
not a theorem about biased quaternion samples, dependent local subspaces,
LLL, CVP, nonlinear decoding, or arbitrary matrices manufactured from
\(N\).

No computation was used.  Everything below is symbolic.

## Outcome

Let \(N=pq\), let \(C_p\) and \(C_q\) be independent uniform
\(u\)-dimensional subspaces of \(\mathbb F_p^m\) and
\(\mathbb F_q^m\), and form their CRT Construction-A lattice

\[
L=\{x\in\mathbb Z^m:x\bmod p\in C_p,
                         \ x\bmod q\in C_q\}.
\]

The one-factor coordinate slices are exactly

\[
L\cap p\mathbb Z^m=pL_q,
\qquad
L\cap q\mathbb Z^m=qL_p,
\]

where \(L_r\) is the ordinary Construction-A lift of \(C_r\).
This already accounts jointly for every relation in the batch.

Put

\[
v_m=\frac{\pi^{m/2}}{\Gamma(m/2+1)},
\qquad
R_M=2v_m^{-1/m}N^{1-u/m},
\qquad
R_0=\min(R_M,N).
\]

Minkowski gives \(\lambda_1(L)\le R_M\), while the public vectors
\(Ne_i\) give \(\lambda_1(L)\le N\).  Hence every shortest vector has
length at most \(R_0\).  If

\[
\theta_r=\frac{r^u-1}{r^m-1},
\qquad a_m=\frac{\sqrt m}{2},
\]

then the probability that **any** shortest vector has proper coordinate gcd
with \(N\) is at most

\[
\boxed{
\theta_q v_m\left(\frac{R_0}{p}+a_m\right)^m
+
\theta_p v_m\left(\frac{R_0}{q}+a_m\right)^m.}
\tag{0.1}
\]

This is a tie-independent finite event bound.  Its cube-volume right-hand
side is deliberately loose in the fixed dimensions \(u<m<2u\).  For every
fixed \(u\), every fixed balance constant \(\kappa\), and every fixed \(K\),
uniformly over

\[
p\le q\le\kappa p,
\qquad
u<m\le(\log N)^K,
\]

the actual proper-gcd shortest-vector event has probability at most

\[
N^{-u/2+o(1)}.
\tag{0.2}
\]

Thus, with probability \(1-N^{-u/2+o(1)}\), every exact shortest vector
has coordinate gcd either \(1\) or \(N\), never a proper factor.  When
\(R_M<N\), every shortest vector in fact has gcd \(1\) on this event,
because its norm is below that of every nonzero vector in
\(N\mathbb Z^m\).  When \(R_M\ge N\), the trivial vectors \(\pm Ne_i\)
already attain the public radius; any factor-revealing tie is still covered
by (0.1).

The conclusion is stronger than a failure of a named tie-breaking rule: it
rules out the existence of any factor-revealing exact shortest vector with
overwhelming probability in this uniform model.  The full arithmetic model
remains open precisely because its local subspaces could be biased or
dependent in a way not captured here.

## 1. Exact CRT lattice and determinant

Assume throughout that \(p\ne q\) are primes and
\(1\le u<m\).  For \(r\in\{p,q\}\), define

\[
L_r=\{x\in\mathbb Z^m:x\bmod r\in C_r\}.
\]

Reduction modulo \(r\) maps \(\mathbb Z^m\) onto
\(\mathbb F_r^m\), and \(L_r\) is the preimage of a subspace of
codimension \(m-u\).  Therefore

\[
[\mathbb Z^m:L_r]=r^{m-u},
\qquad
\det L_r=r^{m-u}.
\tag{1.1}
\]

Coordinatewise CRT identifies

\[
(\mathbb Z/N\mathbb Z)^m
\simeq\mathbb F_p^m\times\mathbb F_q^m.
\]

The preimage of \(C_p\times C_q\) is exactly

\[
L=L_p\cap L_q.
\tag{1.2}
\]

Its index and determinant are consequently

\[
[\mathbb Z^m:L]
=p^{m-u}q^{m-u}=N^{m-u},
\qquad
\det L=N^{m-u}.
\tag{1.3}
\]

No independence assumption is needed for (1.1)--(1.3).  Independence is
used only for the probability model later.

The model can also be viewed as a random full lattice of the form
\(E+N\mathbb Z^m\): choose local bases for \(C_p,C_q\), match them by
CRT, and lift the resulting rank-\(u\) free submodule modulo \(N\).
The theorem concerns the complete ambient lattice, not the orthogonal
projection off \(E\otimes\mathbb R\).

## 2. The proper-factor slices are exact local lifts

Suppose \(x\in p\mathbb Z^m\), and write \(x=py\).  Its reduction modulo
\(p\) is zero and hence lies in \(C_p\).  Since multiplication by \(p\)
is an invertible scalar modulo \(q\),

\[
x\bmod q\in C_q
\quad\Longleftrightarrow\quad
y\bmod q\in C_q.
\]

It follows that

\[
L\cap p\mathbb Z^m=pL_q.
\tag{2.1}
\]

The symmetric argument gives

\[
L\cap q\mathbb Z^m=qL_p.
\tag{2.2}
\]

Their intersection is

\[
L\cap N\mathbb Z^m=N\mathbb Z^m.
\tag{2.3}
\]

For a nonzero \(x\in L\), squarefreeness now gives the exact alternatives

\[
\gcd(N,x_1,\ldots,x_m)=
\begin{cases}
p,&x=py,\ y\in L_q,\ y\notin q\mathbb Z^m,\\
q,&x=qy,\ y\in L_p,\ y\notin p\mathbb Z^m,\\
N,&x\in N\mathbb Z^m,\\
1,&\text{otherwise}.
\end{cases}
\tag{2.4}
\]

Thus a proper coordinate gcd is not being approximated by a proxy: it is
exactly membership in one of the two punctured slices (2.1)--(2.2).

## 3. Uniform-subspace incidence

Let \(C\) be uniform among the \(u\)-dimensional subspaces of
\(\mathbb F_r^m\).  For every fixed nonzero
\(z\in\mathbb F_r^m\),

\[
\Pr(z\in C)=\theta_r
=\frac{r^u-1}{r^m-1}.
\tag{3.1}
\]

One proof double-counts pairs \((C,z)\) with \(0\ne z\in C\).
Every \(C\) contains \(r^u-1\) nonzero vectors, while transitivity of
\(\mathrm{GL}_m(\mathbb F_r)\) makes the number of subspaces through a
fixed nonzero \(z\) independent of \(z\).  Dividing by the
\(r^m-1\) possible nonzero vectors gives (3.1).

Only this marginal formula is needed for the union bounds.  In particular,
the proof of the \(p\)-slice bound uses only uniformity of \(C_q\), and
the proof of the \(q\)-slice bound uses only uniformity of \(C_p\).
Independence between the two subspaces is part of the clean model but is not
needed for the final union bound.

## 4. An exact finite bound for every dimension

Let

\[
Z_m(s)=\#\{y\in\mathbb Z^m:\|y\|_2\le s\}.
\]

Center a unit cube at each counted lattice point.  The cubes are disjoint,
and every such cube lies in the Euclidean ball of radius
\(s+\sqrt m/2\).  Hence

\[
Z_m(s)\le v_m\left(s+\frac{\sqrt m}{2}\right)^m.
\tag{4.1}
\]

Minkowski's convex-body theorem applied to the open Euclidean ball gives a
nonzero lattice vector whenever its volume is strictly larger than
\(2^m\det L\).  Taking an arbitrarily small enlargement and then a limit
yields

\[
\lambda_1(L)
\le 2v_m^{-1/m}(\det L)^{1/m}
=R_M.
\tag{4.2}
\]

Also \(Ne_i\in L\), so

\[
\lambda_1(L)\le R_0=\min(R_M,N).
\tag{4.3}
\]

Let \(E_p(R)\) be the event that there is an
\(x\in L\) with \(\|x\|_2\le R\) and coordinate gcd \(p\).
By (2.4), write \(x=py\), where
\(0\ne y\bmod q\in C_q\).  For every fixed eligible \(y\), (3.1)
gives probability \(\theta_q\).  The sharp union bound is

\[
\Pr(E_p(R))
\le \theta_q
\#\{y\in\mathbb Z^m:\|y\|_2\le R/p,\ y\bmod q\ne0\}.
\tag{4.4}
\]

Enlarging only the number of eligible indices to all integer points in the
ball, and then applying (4.1), gives

\[
\Pr(E_p(R))
\le \theta_q Z_m(R/p)
\le \theta_q v_m\left(\frac Rp+a_m\right)^m.
\tag{4.5}
\]

Similarly,

\[
\Pr(E_q(R))
\le \theta_p v_m\left(\frac Rq+a_m\right)^m.
\tag{4.6}
\]

If any shortest vector exposes a proper factor, then either
\(E_p(R_0)\) or \(E_q(R_0)\) occurs.  Equations (4.5)--(4.6) prove the
boxed bound (0.1).  Because the event quantifies over all vectors up to the
known radius, it includes arbitrary multiplicity and every tie-breaking
rule.

The exact formulas remain valid for small primes and every
\(1\le u<m\).  They may be numerically larger than one, in which case the
trivial upper bound one is understood.  The sparse asymptotic conclusion
requires the balanced, fixed-\(u\), polynomial-dimension regime stated
next.

## 5. Balanced asymptotics

Fix \(u\ge1\), \(\kappa\ge1\), and \(K\ge1\).  Let

\[
p\le q\le\kappa p,
\qquad
u<m\le(\log N)^K,
\tag{5.1}
\]

and let \(p\to\infty\).  Constants and \(o(1)\) terms below may depend on
\(u,\kappa,K\), but not on the particular primes or dimension in (5.1).

### 5.1 The Minkowski-radius branch

Suppose \(R_M\le N\), so \(R_0=R_M\).  Put
\(s_p=R_M/p\).  Ignoring only the cube inflation for one line,

\[
\begin{aligned}
\theta_q v_m s_p^m
&=\frac{q^u-1}{q^m-1}
  \frac{2^mN^{m-u}}{p^m}\\
&=\frac{2^m}{p^u}
  \frac{q^{m-u}(q^u-1)}{q^m-1}\\
&<\frac{2^m}{p^u}.
\end{aligned}
\tag{5.2}
\]

The symmetric leading term is less than \(2^m/q^u\).

The condition \(R_M\le N\) is equivalent to

\[
\frac{2^m}{v_m}\le N^u.
\tag{5.3}
\]

Using

\[
v_m\le\left(\frac{2\pi e}{m}\right)^{m/2},
\tag{5.4}
\]

equation (5.3) implies

\[
m\log m=O(\log N).
\tag{5.5}
\]

Consequently \(m=o(\log N)\) and \(2^m=N^{o(1)}\).

It remains to justify the cube inflation in (4.5).  Because \(u\) is
fixed, there are only three cases.

- If \(u<m<2u\), balance gives
  \(s_p=O(p^{1-2u/m})=o(1)\), and likewise for \(R_M/q\).
  Eventually there is no nonzero integer \(y\) in either divided ball, so
  the corresponding event is empty by the sharp eligible-point bound
  (4.4).  The cube-volume relaxation (0.1) is not used in this case.
- If \(m=2u\), the two divided radii are bounded in terms of
  \(u,\kappa\).  The number of candidate \(y\)'s is therefore constant,
  while \(\theta_p,\theta_q=O(N^{-u/2})\).
- If \(m\ge2u+1\), balance and the formula for \(R_M\) give
  \(s_p,s_q\ge p^{c_u-o(1)}\) for a constant \(c_u>0\).
  Since \(m\) is only polylogarithmic,
  \(m a_m/s_p\) and \(m a_m/s_q\) tend to zero.  Hence
  \((1+a_m/s_r)^m=1+o(1)\).

Combining these cases with (5.2) yields

\[
\Pr(E_p(R_0)\cup E_q(R_0))
\le N^{-u/2+o(1)}
\tag{5.6}
\]

on the Minkowski-radius branch.

### 5.2 The public-\(N\)-radius branch

Suppose \(R_M>N\), so \(R_0=N\).  Since \(N/p=q\), (4.5) and
\(\theta_q\le2q^{u-m}\) give

\[
\Pr(E_p(N))
\le2v_mq^u\left(1+\frac{a_m}{q}\right)^m.
\tag{5.7}
\]

The inflation factor is \(1+o(1)\) uniformly under (5.1), because a
polylogarithmic \(m\) and \(a_m\) are negligible compared with the
balanced prime \(q\).  The symmetric bound is

\[
\Pr(E_q(N))
\le2v_mp^u(1+o(1)).
\tag{5.8}
\]

If \(m=o(\log N)\), the branch inequality

\[
R_M>N
\quad\Longrightarrow\quad
v_mN^u<2^m
\tag{5.9}
\]

turns (5.7) into

\[
2v_mq^u(1+o(1))
\le \frac{2^{m+1}}{p^u}(1+o(1))
=N^{-u/2+o(1)}.
\tag{5.10}
\]

If \(m\) is not \(o(\log N)\), use (5.4) directly.  Already for
\(m\ge\log N/\sqrt{\log\log N}\),

\[
\log v_m
\le-\tfrac12m\log m+O(m)
=-\omega(\log N),
\]

so (5.7)--(5.8) are smaller than any fixed negative power of \(N\).
The intermediate split can be taken at
\(\log N/\sqrt{\log\log N}\): below it \(m=o(\log N)\) and (5.10)
applies; above it the volume bound applies.  Thus (5.6) holds on this
branch as well.

This proves (0.2).

## 6. What many relations did and did not amortize

The local code contains \(r^u\) residue classes regardless of \(m\), while
its codimension grows as \(m-u\).  The public lattice has determinant
\(N^{m-u}\).  A vector divisible by \(p\) discards the \(p\)-condition but
must land in the \(q\)-code after division.  For each fixed divided vector,
that costs the exact incidence probability

\[
\theta_q\asymp q^{u-m}.
\]

The number of divided vectors available below the public shortest-vector
radius grows with \(m\), but the Euclidean-ball calculation cancels its
leading \(q^m\) growth and leaves the factor

\[
\frac{2^m}{p^u}
\]

on the nontrivial-radius branch.  The branch condition itself forces
\(2^m=N^{o(1)}\).  Once dimension is so large that the Minkowski radius
exceeds \(N\), the public vectors \(Ne_i\) cap the minimum and the shrinking
unit-ball volume supplies the obstruction.  This is a joint calculation
over all short relations, not a union of independently generated scalar-gcd
tickets.

## 7. Effectiveness and scope

The lattice is specified by bases for \(C_p,C_q\) only in the hidden local
analysis.  A public CRT lift can be represented by a polynomial-bit integer
basis whenever the underlying public relation construction supplies it.
All determinant, slice, norm, and gcd identities above are exact and have
polynomial-size descriptions for \(m=\operatorname{poly}(\log N)\).

No polynomial-time exact-SVP algorithm in growing dimension is claimed.
The theorem grants even an exact SVP oracle and shows that its entire
shortest-vector set almost surely lacks a proper coordinate gcd in the
uniform model.  It therefore says nothing about computational hardness of
SVP and nothing about a different statistic of the full lattice.

The following remain open:

- arithmetic or quaternion sources whose two local subspaces are biased or
  dependent rather than uniform;
- a public rule that manufactures such a bias from bare \(N\);
- CVP with a biased target, affine shifts, successive minima, or a joint
  statistic of many nonshortest vectors;
- LLL or another polynomial-time reduction whose output distribution is not
  governed by the exact shortest-vector event analyzed here;
- dimensions or output ranks outside the fixed-\(u\), polynomial-\(m\),
  balanced-semiprime asymptotic;
- nonlinear combinations, block codes, or a decoder not reducible to the
  coordinate gcd of one selected vector.

## 8. Exact obstruction and reopen condition

The kill-first conclusion is:

> In the independent uniform local-subspace model, adding polynomially many
> relation coordinates does not make a one-factor slice win exact SVP.  A
> deterministic public radius contains every shortest vector, and the
> probability that any vector in that radius has coordinate gcd \(p\) or
> \(q\) is \(N^{-u/2+o(1)}\) for fixed local dimension on balanced
> semiprimes.

A retry is materially new only if it specifies a factor-free arithmetic
source or target law and proves that its bias defeats the exact incidence
bound, or if it supplies a different full-lattice observable with an
inverse-polynomial factor-extraction law and a polynomial-time evaluator.
Merely increasing \(m\) under independent uniform local subspaces, or
quotienting the public exact directions already handled by F27, is covered
by this obstruction.
