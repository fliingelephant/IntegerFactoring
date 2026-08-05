# F20 candidate: an unconditional four-square finder is still orientation-diffuse

**Status:** candidate proof. No hostile audit or proof-blind reconstruction has
run.

**Closest prior route and material difference.** P25 treats ideal iid-uniform
Hurwitz-shell samples. The F15 biased-sampling follow-up treats the
integer-coordinate slice, bounded transform menus, and a conditional
single-unit-orbit extractor, but explicitly leaves arithmetic four-square
finders open. This note analyzes the actual residual-conditioned architecture
of the unconditional Rabin--Shallit / Pollack--Treviño four-square finder. Its
outputs are highly nonuniform globally, yet their local row orientations are
exactly uniform on a projective line or on that line with two fixed points
deleted. This is a new distribution theorem, not an appeal to uniform-shell
sampling.

**Computation:** none. This is a proof-only candidate, so there is no run
manifest.

## 1. The sampler interface

Let \(N=pq\), with distinct odd primes, and let \(M\) be an odd squarefree
multiple of \(N\). Consider the following residual-conditioned construction.

1. Draw \(x,y\) exactly uniformly modulo \(M\).
2. Put \(R=-x^2-y^2\bmod M\).
3. Accept or reject using only \(R\) and fresh coins. On acceptance, construct
   \(z,w\), using only \(R\) and fresh coins, so that
   \(z^2+w^2\equiv R\pmod M\), \(R\) is a unit modulo \(M\), and
   \(\gcd(x,y,z,w)=1\).
4. Put \(\beta=x+yi+zj+wk\) in the Hurwitz order and compute a greatest
   common right divisor \(\alpha=\operatorname{gcrd}_R(N,\beta)\), normalized
   by a left unit.

The norm of \(\beta\) is divisible by \(M\), hence by \(N\). The standard
primitive Hurwitz-gcd lemma gives

\[
  \operatorname{nrd}(\alpha)=N.                 \tag{1}
\]

This interface includes the unconditional algorithm in Section 4 of Pollack
and Treviño, *Finding the Four Squares* (INTEGERS 18A, 2018). After trial
division by primes at most \(\log N\), that algorithm forms

\[
 M=N\prod_{\substack{\ell\le\log N\\\ell\equiv3\pmod4}}\ell
\]

on a balanced semiprime with no such small factor, draws \(x,y\) uniformly
modulo \(M\), and accepts according only to the residual \(R\). It writes the
accepted residual as \(z^2+w^2\) and applies exactly the Hurwitz gcd above.
Their unconditional density estimate gives expected polynomially many
arithmetic operations on integers of size \(N^{O(1)}\); exact interval sampling
and every arithmetic operation therefore also have polynomial bit cost. The
proof below does not assume that this output is uniform on a norm shell.

## 2. A local conic-to-projective-line bijection

Fix an odd prime \(r\mid N\), and write \(\chi_r=(-1/r)\). Conditional on an
accepted global residual \(R\) and on \(z,w\), CRT makes \((x,y)\bmod r\)
uniform on

\[
 C_R=\{(x,y)\in\mathbb F_r^2:x^2+y^2=-R\}.      \tag{2}
\]

The unit condition on \(R\) makes this a nonsingular conic of size

\[
 |C_R|=r-\chi_r.                                 \tag{3}
\]

Choose \(s,t\in\mathbb F_r\) with \(s^2+t^2=-1\), and use the splitting

\[
 i\longmapsto
 \begin{pmatrix}0&1\\-1&0\end{pmatrix},
 \qquad
 j\longmapsto
 \begin{pmatrix}s&t\\t&-s\end{pmatrix}.
\]

Then \(k=ij\), and the first row of the matrix for
\(\beta=x+yi+zj+wk\) is

\[
 (x+A,\ y+B),
 \qquad
 A=zs+wt,\quad B=zt-ws.                          \tag{4}
\]

The second row is \((-y+B,x-A)\), and

\[
 A^2+B^2=-(z^2+w^2)=-R.                          \tag{5}
\]

Equations (2) and (5) show that the row-line map is the following elementary
bijection:

\[
 C_R\longrightarrow
 \{[u:v]\in\mathbf P^1(\mathbb F_r):u^2+v^2\ne0\}. \tag{6}
\]

Indeed, except at \((x,y)=(-A,-B)\), the image is
\([x+A:y+B]\). For a proposed anisotropic line \([u:v]\), writing
\((x+A,y+B)=\lambda(u,v)\) in the conic equation gives

\[
 \lambda\bigl(\lambda(u^2+v^2)-2(Au+Bv)\bigr)=0. \tag{7}
\]

If \(Au+Bv\ne0\), (7) supplies exactly one nonzero \(\lambda\). If
\(Au+Bv=0\), the unique such line is \([B:-A]\), and it is the row line of
the exceptional matrix whose first row is zero. If \(u^2+v^2=0\), then
\(Au+Bv\ne0\), because \((A,B)\) is anisotropic, and (7) has no nonzero
solution. This proves (6), including the exceptional point.

Consequently the local row orientation of \(\beta\), conditional on all later
sampler choices, is exactly

\[
 R_r(\beta)\sim
 \begin{cases}
 \operatorname{Unif}(\mathbf P^1(\mathbb F_r)),&\chi_r=-1,\\
 \operatorname{Unif}(\mathbf P^1(\mathbb F_r)\setminus E_i),&\chi_r=+1,
 \end{cases}                                      \tag{8}
\]

where \(E_i\) is the pair of eigenlines of right multiplication by \(i\).
The support in (8) is independent of \(R,z,w\). Mixing over every accepted
residual therefore leaves the same exact law.

## 3. The Hurwitz gcd output has the same row line

Write \(N=\gamma\alpha\) and \(\beta=\delta\alpha\). Reduction modulo
\(r\mid N\) makes \(\alpha_r\) a nonzero rank-one matrix by (1) and
squarefreeness. The primitive-coordinate condition makes \(\beta_r\ne0\).
Left multiplication cannot enlarge row space, so

\[
 \operatorname{row}(\beta_r)\subseteq
 \operatorname{row}(\alpha_r).
\]

Both sides are nonzero subspaces of the one-dimensional row space of
\(\alpha_r\), hence they are equal. Left-unit normalization preserves row
space. Thus

\[
 R_r(\alpha)=R_r(\beta),                          \tag{9}
\]

and the actual norm-\(N\) output of the arithmetic finder obeys (8).

## 4. Cross-sample one-sided gcds remain rare

Let \(\alpha,\alpha'\) be independent outputs of any sampler satisfying the
interface. From (8),

\[
 \Pr(R_r(\alpha)=R_r(\alpha'))
 =\frac1{r-\chi_r}.                               \tag{10}
\]

A proper greatest common right divisor requires equality at exactly one of
\(p,q\). Without assuming independence between the two CRT components of one
sample, the union bound gives

\[
 \Pr(1<\operatorname{nrd}\operatorname{gcrd}_R(\alpha,\alpha')<N)
 \le \frac1{p-\chi_p}+\frac1{q-\chi_q}.           \tag{11}
\]

For \(K\) independent outputs and every-pair testing, multiply (11) by
\(\binom K2\). On \(p<q<2p\), every polynomial \(K\) in \(\log N\) still has
exponentially small success along the balanced family. The quaternion gcd
norm would be the factor on a proper event; no terminal integer gcd is needed,
but the event remains too rare.

## 5. The single-orbit stabilizer survivor also fails on this law

Let

\[
 G=\mathcal H^\times/\{\pm1\}\simeq A_4,
 \qquad H_r(\alpha)=\operatorname{Stab}_G(R_r(\alpha)).
\]

Random right-unit translates of one \(\alpha\) expose a proper one-sided gcd
with exact probability

\[
 \frac{|H_p(\alpha)\triangle H_q(\alpha)|}{12}.   \tag{12}
\]

For every odd \(r\), no nonidentity projective Hurwitz unit reduces to a
scalar: its imaginary coordinates are \(0,\pm1\) or half-integers, so scalar
reduction would force the unit to be \(\pm1\). A nonscalar projective matrix
fixes at most two lines. The three order-two subgroups of \(A_4\) contribute
at most six exceptional lines; the four order-three subgroups contribute at
most eight. Hence at most fourteen lines have nontrivial stabilizer.

When \(\chi_r=-1\), (8) gives

\[
 \Pr(H_r(\alpha)\ne1)\le\min\left(1,\frac{14}{r+1}\right). \tag{13}
\]

When \(\chi_r=+1\), the two omitted lines are exactly those fixed by the
order-two element \(i\). The remaining exceptional union has size at most
twelve, so

\[
 \Pr(H_r(\alpha)\ne1)\le\min\left(1,\frac{12}{r-1}\right). \tag{14}
\]

If both local stabilizers are trivial, their symmetric difference is empty.
Therefore a union bound over (13)--(14) shows that the chance a single finder
output even enters the survivor stratum \(H_p\ne H_q\) is

\[
 O(1/p+1/q)=O(N^{-1/2})                           \tag{15}
\]

on balanced inputs. Polynomially many independent finder outputs and all
twelve right-unit translates remain exponentially unlikely to help.

## 6. Scope

The exact obstruction applies to residual-conditioned samplers whose acceptance
and completion depend on \((x,y)\) only through \(R=-x^2-y^2\), including the
named unconditional four-square algorithm on the squarefree-semiprime branch.
It also applies if the accepted-residual distribution is arbitrarily biased or
adaptive: the conditional support in (8) is fixed.

It does not cover a finder that uses additional information about the particular
preimage \((x,y)\), coordinate caps rather than complete residue fibers, a left
rather than right orientation chosen to exploit a different conditional law,
non-squarefree inputs, or a non-collision quaternion invariant. It does not
prove that every polynomial-time four-square finder is orientation-diffuse and
supplies no top-level factoring algorithm.

## Candidate theorem

> **F20 residual-fibre obstruction.** On a distinct-odd-semiprime input, the
> output of the unconditional residual-conditioned Hurwitz four-square finder
> has, modulo each unknown prime \(r\), an exactly uniform row line on
> \(\mathbf P^1(\mathbb F_r)\) if \((-1/r)=-1\), and on that projective line
> with the two \(i\)-eigenlines deleted if \((-1/r)=+1\). Consequently
> polynomially many independent outputs have exponentially small cross-sample
> one-sided-gcd probability on balanced inputs, and polynomially many outputs
> have exponentially small mass on the unequal-\(A_4\)-stabilizer stratum needed
> by the single-unit-orbit extractor. This closes that specified unconditional
> arithmetic finder, not arbitrary nonuniform quaternion algorithms.
