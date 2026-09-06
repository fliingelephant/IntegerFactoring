# Proof of F208

## 1. Divisor pairing and the sign selector

For every positive integer \(d\),

\[
 J_d(N)=
 \left\lfloor\frac Nd\right\rfloor-
 \left\lfloor\frac{N-1}{d}\right\rfloor
\]

is one exactly when \(d\mid N\), and is zero otherwise. Since \(N\) is not
a square, every divisor pair has one member below \(\sqrt N\) and one member
above it. Therefore

\[
\begin{aligned}
 A(N)
 &=
 \sum_{\substack{d\mid N\\d\leq B}}
 \left(
 d\chi(d)+\frac Nd\chi(N/d)
 \right).
\end{aligned}
\]

All divisors are odd, so their character values are signs. Multiplicativity
and \(\chi(d)^2=1\) give

\[
 \chi(N/d)=\chi(N)\chi(d)=\eta\chi(d).
\]

Inserting the exact jump and replacing \(N/d\) by
\(\lfloor N/d\rfloor\) on its support yields

\[
 A(N)=
 \sum_{d\leq B}\chi(d)
 \left(
 d+\eta\left\lfloor\frac Nd\right\rfloor
 \right)J_d(N).
\]

For \(N=pq\) with \(p<q\), one has \(p<\sqrt N<q\). Thus the only
divisors at most \(B\) are \(1,p\). The \(d=1\) term is \(1+\eta N\),
and the \(d=p\) term is

\[
 \chi(p)(p+\eta q).
\]

This proves the displayed formula for \(T\).

If \(\eta=1\), the parenthesis \(p+q\) is positive, so
\(\operatorname{sgn}T=\chi(p)\). If \(\eta=-1\), then \(p-q<0\), so
\(\operatorname{sgn}T=-\chi(p)\). Both cases are

\[
 \operatorname{sgn}T=\eta\chi(p).
\]

Since \(\eta=\chi(p)\chi(q)\), the same sign is \(\chi(q)\). Finally,
among \(2\leq d\leq B\), only \(p\) is a divisor, proving

\[
 \sum_{2\leq d\leq B}\chi(d)J_d(N)=\chi(p).
\]

This is an identity, not an evaluation procedure for the sum.

## 2. Proof of totalized floor reciprocity

Let \(N,d\) be odd positive integers and put \(g=\gcd(N,d)\). Consider
the integer rectangle

\[
 1\leq i\leq\frac{N-1}{2},
 \qquad
 1\leq j\leq\frac{d-1}{2}.
\]

It contains exactly

\[
 \frac{(N-1)(d-1)}4
\]

lattice points. The first floor sum

\[
 \sum_{i=1}^{(N-1)/2}\left\lfloor\frac{id}{N}\right\rfloor
\]

counts the points on or below the line \(jN=id\). The second floor sum

\[
 \sum_{j=1}^{(d-1)/2}\left\lfloor\frac{jN}{d}\right\rfloor
\]

counts the points on or above the same line. Every off-line point is counted
once. Every on-line point is counted twice.

The positive solutions of \(id=jN\) are

\[
 i=tN/g,\qquad j=td/g.
\]

The half-rectangle contains exactly the values

\[
 1\leq t\leq\frac{g-1}{2},
\]

because \(g\) is odd. Hence it has \((g-1)/2\) points on the line. It
follows that

\[
\begin{aligned}
 &\sum_{i=1}^{(N-1)/2}\left\lfloor\frac{id}{N}\right\rfloor
 +
 \sum_{j=1}^{(d-1)/2}\left\lfloor\frac{jN}{d}\right\rfloor\\
 &\qquad=
 \frac{(N-1)(d-1)}4+\frac{g-1}{2}.
\end{aligned}
\]

This proves

\[
 \Delta_N(d)=\frac{\gcd(d,N)-1}{2}.
\]

It remains to identify the support in the declared interval. Since
\(q<2p\),

\[
 N=pq<2p^2,\qquad
 B<\sqrt2\,p<2p.
\]

Also \(p<\sqrt N\), so \(p\leq B\). Therefore \(B/2<p\leq B\).

For \(B/2<d\leq B\), the gcd with \(N=pq\) cannot be divisible by \(q\)
because \(d<q\). If it is divisible by \(p\), then \(d=kp\). But
\(d<2p\), so \(k=1\). Thus \(p\) is the unique nonunit in the interval.
Every even \(d\) has \(\chi(d)=0\), while \(p\) is odd. Consequently,

\[
\begin{aligned}
 2\sum_{\substack{B/2<d\leq B\\d\ {\rm odd}}}
 \chi(d)\Delta_N(d)
 &=2\chi(p)\frac{p-1}{2}\\
 &=\chi(p)(p-1).
\end{aligned}
\]

The direct interval has \(\Theta(B)=2^{\Theta(\log N)}\) entries. The
identity neither compresses that aggregate nor excludes a future
compression.

## 3. Dedekind reduction and cotangent poles

Let \(g=\gcd(h,k)\), \(h=gh_0\), and \(k=gk_0\). Every residue modulo
\(k\) has a unique expression

\[
 r=u+jk_0,\qquad
 0\leq u<k_0,\quad 0\leq j<g.
\]

The second sawtooth factor satisfies

\[
 \left(\left(\frac{hr}{k}\right)\right)
 =
 \left(\left(\frac{h_0u}{k_0}+h_0j\right)\right)
 =
 \left(\left(\frac{h_0u}{k_0}\right)\right).
\]

For the first factor, direct summation over \(j\) gives

\[
 \sum_{j=0}^{g-1}
 \left(\left(\frac{u+jk_0}{gk_0}\right)\right)
 =
 \left(\left(\frac{u}{k_0}\right)\right).
\]

For \(u>0\), this is the arithmetic sum

\[
 \sum_{j=0}^{g-1}
 \left(\frac{u/k_0+j}{g}-\frac12\right)
 =\frac{u}{k_0}-\frac12.
\]

For \(u=0\), the zero sawtooth term and the remaining \(g-1\) terms sum
to zero. Hence

\[
\begin{aligned}
 s(h,k)
 &=
 \sum_{u=0}^{k_0-1}
 \left(\left(\frac{u}{k_0}\right)\right)
 \left(\left(\frac{h_0u}{k_0}\right)\right)\\
 &=s(h_0,k_0).
\end{aligned}
\]

This proves \(s(h,k)=s(h/g,k/g)\).

The usual cotangent expression contains

\[
 \cot\left(\frac{\pi hr}{k}\right).
\]

This factor has a pole exactly when \(k\mid hr\), equivalently when
\(k/g\mid r\). Among \(1\leq r<k\), these residues are

\[
 r=j\,k/g,\qquad 1\leq j<g,
\]

so there are exactly \(g-1\) poles. The other cotangent is finite at these
residues. Thus the ordinary cotangent formula is nonsingular precisely on
the coprime branch. Its sawtooth regularization contracts the modulus only
after division by the gcd.

For \(h=p,k=N=pq\), the reduced arguments are \(1,q\). Both \(p\) and
\(q\) are already explicit in that reduction. No public smaller modulus is
created before the gcd event.

## 4. Triangular determinant shell

For fixed positive \(a,d\) with \(ad=N\), the declared triangular HNF
convention has exactly \(a\) choices

\[
 0\leq b<a.
\]

Every one receives the same weight \(\chi(a)\). Therefore

\[
 \sum_{\substack{ad=N\\0\leq b<a}}\chi(a)
 =
 \sum_{a\mid N}a\chi(a)
 =A(N).
\]

Now define

\[
 \mathcal C(X)=
 \sum_{\substack{a,d\geq1\\ad\leq X}}a\chi(a).
\]

The difference \(\mathcal C(N)-\mathcal C(N-1)\) retains exactly the
pairs satisfying \(ad=N\), and therefore equals \(A(N)\). Applying
Dirichlet-hyperbola rearrangement to either cumulative sum does not alter
this adjacent-shell condition. In floor notation the condition is precisely
\(J_a(N)\).

For the semiprime, the public shells \(a=1,N\) contribute
\(1+\eta N\). The two nontrivial shells contribute
\(p\chi(p)+q\chi(q)\), which is \(T\). The HNF description is therefore a
literal representation of the same target, not a smaller state.

## 5. The diagonal reduced form

A primitive positive definite binary quadratic form \([a,b,c]\) has
discriminant \(b^2-4ac\). Thus

\[
 [p,0,q]
\]

has discriminant \(-4pq=-4N\). Since \(0\leq |0|\leq p<q\), it is
reduced. Negating the middle coefficient leaves it unchanged, so its proper
class is ambiguous.

A diagonal form \([a,0,c]\) of the same discriminant satisfies \(ac=N\).
If it is reduced, then \(a\leq c\). The only such divisor choices for the
distinct semiprime are

\[
 [1,0,N]\quad\text{and}\quad[p,0,q].
\]

The first is the principal form. If the second were properly equivalent to
it, every integer represented by the second would also be represented by the
first. The second represents \(p\) at \((1,0)\). But the equation

\[
 x^2+Ny^2=p
\]

has no integer solution: \(y\neq0\) makes the left side at least \(N>p\),
and \(y=0\) would make the prime \(p\) a square. Hence \([p,0,q]\) is
nonprincipal.

Its leading coefficient directly exposes \(p\), and its residue modulo four
is the selector \(\chi(p)\). Reduction of the public principal form stays in
the principal class and cannot produce this form.

## 6. Pair symmetry and two-square counts

Assume \(\eta=-1\) and \(W_N(d)=W_N(N/d)\). Pairing complementary
divisors gives

\[
\begin{aligned}
 &\chi(d)W_N(d)+\chi(N/d)W_N(N/d)\\
 &\qquad=
 \chi(d)W_N(d)+\eta\chi(d)W_N(d)=0.
\end{aligned}
\]

Summing over all pairs proves

\[
 \sum_{d\mid N}\chi(d)W_N(d)=0.
\]

The statement applies only when the representation formula has this exact
pair-symmetric divisor weight.

The standard two-square formula is

\[
 r_2(N)=4\sum_{d\mid N}\chi(d).
\]

Multiplicativity of the divisor sum gives

\[
 r_2(N)=4(1+\chi(p))(1+\chi(q)).
\]

If \(\eta=1\), the two character values agree, and hence

\[
 r_2(N)=8(1+\chi(p)).
\]

If \(\eta=-1\), one local factor \(1+\chi(\cdot)\) is zero, so
\(r_2(N)=0\) independently of which prime is smaller. This proves the
claimed representation boundary.

## 7. Exact Archimedean magnitude

From Section 1,

\[
 T=\chi(p)(p+\eta q).
\]

If \(\eta=1\), its absolute value is \(p+q\), and

\[
 |T|^2-4N
 =(p+q)^2-4pq
 =(q-p)^2.
\]

If \(\eta=-1\), its absolute value is \(q-p\), and

\[
 |T|^2+4N
 =(q-p)^2+4pq
 =(p+q)^2.
\]

Thus either exact magnitude supplies the two factors through the usual
sum-and-difference formulas. It supplies no separate smaller recursive
integer. This is an equivalence for the exact magnitude, not a method for
computing it.

## 8. Scope of the proof

Every conclusion above is an exact identity inside a declared
representation. None proves that the signed divisor OR has no succinct
nonlinear evaluation. In particular, the proof does not cover:

1. a nonlinear combination of QP many floor or Dedekind values;
2. a compressed arithmetic circuit for the adjacent HNF shell;
3. implicit navigation to a nonprincipal class without listing forms;
4. asymmetric or incomplete theta and representation statistics;
5. an adaptive integer carry that retains only the sign;
6. a support-preserving smaller child with a proved lift; or
7. a globally nested one-child recursion.

Those interfaces remain open.
