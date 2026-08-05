# Proof-blind reconstruction of the mixed-handed four-square boundary

## Verdict and scope

All eight stated claims follow from the residual fibre, the two one-sided ideal
parametrizations of the odd squarefree Hurwitz shell, and elementary rank-one matrix
algebra.  The bounds remain valid when normalization is chosen arbitrarily from the
entire preceding transcript; no canonical Euclidean-algorithm output is assumed.

The conclusion is deliberately narrow.  It bounds a union of specified rare
projective equalities, zero products, and stabilizer coincidences.  It is not a bound
on a decoder that jointly processes the ubiquitous nonzero data in many outputs.

No mathematical computation was run.  The numerical certificate in Section 8 is
expanded and checked by hand.

## 1. Conditional product-uniformity

Let \(N=pq\) for distinct odd primes, and let \(M\) be the odd squarefree modulus of
the residual-only finder, with \(N\mid M\).  The finder starts with exactly uniform
\((x,y)\in(\mathbf Z/M\mathbf Z)^2\), sets

\[
 R=-x^2-y^2\pmod M,
\]

and accepts/completes using only \(R\) and fresh randomness.  Fix an accepted
residual \(R\) and all completion randomness, so in particular \(z,w\) are fixed and

\[
 z^2+w^2=R\pmod M.
\]

The accepted residual is a unit.  Because the kernel is constant on every
\((x,y)\)-fibre, the conditional law of \((x,y)\) is uniform on

\[
 \mathcal F_R=
 \{(x,y)\bmod M:x^2+y^2=-R\pmod M\}.
\]

CRT gives the Cartesian product, not merely equal marginals,

\[
 \mathcal F_R\simeq
 \prod_{\ell\mid M}
 \{(x_\ell,y_\ell)\in\mathbf F_\ell^2:
                   x_\ell^2+y_\ell^2=-R\} .             \tag{1.1}
\]

Thus the local conic points at \(p\) and \(q\) are conditionally independent and
uniform.

Fix \(r\in\{p,q\}\), write

\[
 \chi_r=\left(\frac{-1}{r}\right),\qquad
 s_r=r-\chi_r,
\]

and define

\[
 \mathcal S_r=
 \{[u:v]\in\mathbf P^1(\mathbf F_r):u^2+v^2\ne0\}.
\]

There are \(1+\chi_r\) isotropic lines, so \(|\mathcal S_r|=s_r\).

Choose \(s,t\in\mathbf F_r\) with \(s^2+t^2=-1\) and split

\[
 i=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
 j=\begin{pmatrix}s&t\\t&-s\end{pmatrix},\qquad
 k=\begin{pmatrix}t&-s\\-s&-t\end{pmatrix}.             \tag{1.2}
\]

Put

\[
 A=zs+wt,\qquad B=zt-ws.
\]

Then \(A^2+B^2=-R\), and for

\[
 \beta=x+yi+zj+wk
\]

one has

\[
 \beta_r=
 \begin{pmatrix}
 x+A&y+B\\
 B-y&x-A
 \end{pmatrix}.                                         \tag{1.3}
\]

Its determinant is zero and the matrix is nonzero, hence rank one.  The map from the
conic to its row line is a bijection onto \(\mathcal S_r\).  Indeed, away from
\((x,y)=(-A,-B)\), a target \([u:v]\) for the first row requires

\[
 (x+A,y+B)=\lambda(u,v),
\]

and the conic equation reduces to

\[
 \lambda\bigl(\lambda(u^2+v^2)-2(Au+Bv)\bigr)=0.         \tag{1.4}
\]

Every non-isotropic line except \([-B:A]\) has the unique nonzero solution
\(\lambda=2(Au+Bv)/(u^2+v^2)\).  At the exceptional conic point, the first row is
zero and the second row is \((2B,-2A)\), supplying exactly \([-B:A]\).

The image-line map is another bijection.  Away from \((x,y)=(-A,B)\), use the first
column \((x+A,B-y)^T\); solving for a target line gives the same equation (1.4).
At the exceptional point the first column is zero and the second is
\((2B,-2A)^T\), again supplying the missing line.

The two local bijections act separately on the two CRT factors in (1.1).  Therefore,
conditional on the fixed residual and completion data,

\[
 (\operatorname{row}_p\beta,\operatorname{row}_q\beta)
 \text{ is uniform on }\mathcal S_p\times\mathcal S_q,  \tag{1.5}
\]

and, separately,

\[
 (\operatorname{im}_p\beta,\operatorname{im}_q\beta)
 \text{ is uniform on }\mathcal S_p\times\mathcal S_q.  \tag{1.6}
\]

The conditional laws in (1.5)--(1.6) do not depend on the fixed data, so the same
product laws hold after mixing over it.  This does **not** say that the row pair and
the image pair of the same \(\beta\) are jointly independent.

## 2. Shell orbits and arbitrary-normalization atom bounds

Let

\[
 \mathcal H=\mathbf Z\left[i,j,\frac{1+i+j+k}{2}\right],
 \qquad
 \Sigma_N=\{D\in\mathcal H:\operatorname{nrd}(D)=N\}.
\]

For a projective line \(L_r\subset\mathbf F_r^2\), the matrices whose rows lie in
\(L_r\) form a two-dimensional minimal left ideal of \(M_2(\mathbf F_r)\).  Given a
pair \((L_p,L_q)\), take the CRT preimage of these two local ideals in \(\mathcal H\).
It has index \(p^2q^2=N^2\).  The Hurwitz order is left Euclidean, so this ideal is
\(\mathcal H D\); right multiplication by \(D\) has lattice determinant
\(\operatorname{nrd}(D)^2\), whence \(\operatorname{nrd}(D)=N\).  Its generator is
unique up to a left unit.  Conversely, every norm-\(N\) element gives such a pair.
Thus

\[
 \mathcal H^\times\backslash\Sigma_N
 \longleftrightarrow
 \mathbf P^1(\mathbf F_p)\times\mathbf P^1(\mathbf F_q) \tag{2.1}
\]

by row lines.  Dually, right-unit orbits are parametrized by image-line pairs.

There are 24 Hurwitz units, and their actions on nonzero shell elements are free.
Consequently

\[
 |\Sigma_N|=24(p+1)(q+1).                               \tag{2.2}
\]

For completeness, the primitive odd-norm lemma used below follows directly from
ideal multiplication.  If \(m\) is odd,
\(\gamma=a+bi+cj+dk\) has integral primitive coordinates, and
\(m\mid\operatorname{nrd}(\gamma)\), write

\[
 \mathcal Hm+\mathcal H\gamma=\mathcal H d=:I.
\]

Then

\[
 I\bar I=\operatorname{nrd}(d)\mathcal H\subseteq m\mathcal H.
\]

The two-sided ideal \(m^{-1}I\bar I\) contains \(m\), as well as
\(\gamma,\bar\gamma,\bar\gamma i,i\gamma,\bar\gamma j,j\gamma,
\bar\gamma k,k\gamma\).  It therefore contains

\[
 2a,\quad2b,\quad2c,\quad2d.
\]

Primitivity puts 2 in the ideal, and oddness of \(m\) then puts 1 in it.  Hence
\(I\bar I=m\mathcal H\), so \(\operatorname{nrd}(d)=m\).  Conjugation gives the
dual gcld lemma.  This also proves that the gcds below lie on \(\Sigma_N\).

Let \(D_R\) be a greatest common right divisor of \(N\) and \(\beta\).  The
primitive odd-norm lemma gives \(\operatorname{nrd}(D_R)=N\), and reduction of

\[
 \mathcal HN+\mathcal H\beta=\mathcal H D_R
\]

shows that \(D_R\) inherits the row line of \(\beta\) at both primes.  All gcrd
generators differ by a left unit.  We now allow the choice of that left unit to be an
arbitrary, even randomized, function of the entire transcript.

Fix \(r\in\{p,q\}\), let \(r'\) denote the other prime, and fix an arbitrary line
\(L\in\mathbf P^1(\mathbf F_r)\).  By the dual image parametrization, the number of
actual shell elements with image \(L\) at \(r\) is

\[
 24(r'+1):
\]

there are \(r'+1\) choices for the other image line and 24 elements in each
right-unit orbit.  After identifying the central signs, this is \(12(r'+1)\)
projective shell elements.

View these elements as incidences

\[
 (\text{row-pair orbit},\text{projective left-unit class}).
\]

It follows that at most \(12(r'+1)\) row-pair orbits contain *any* left associate
whose image at \(r\) is \(L\).  A transcript-dependent normalization cannot make the
event occur outside that set of row pairs.  The actual finder row pair is uniform on
the \(s_rs_{r'}\) pairs in \(\mathcal S_r\times\mathcal S_{r'}\), conditionally as
well as unconditionally.  Therefore

\[
 \boxed{
 \Pr(\operatorname{im}_rD_R=L)
 \le\frac{12(r'+1)}{s_rs_{r'}}.}                         \tag{2.3}
\]

For every odd prime \(a\),

\[
 \frac{a+1}{s_a}\le\frac32:                             \tag{2.4}
\]

the ratio is 1 if \(\chi_a=-1\), while \(\chi_a=1\) forces \(a\ge5\) and gives
\((a+1)/(a-1)\le3/2\).  Hence

\[
 \frac{12(r'+1)}{s_rs_{r'}}
 =\frac{12}{r+1}\frac{r+1}{s_r}\frac{r'+1}{s_{r'}}
 \le\boxed{\frac{27}{r+1}}.                             \tag{2.5}
\]

For a separately computed greatest common left divisor \(D_L\), right-ideal
reduction gives

\[
 \operatorname{im}_rD_L=\operatorname{im}_r\beta.
\]

Its allowed integral normalization is on the right.  Interchanging rows with images
and left with right in the preceding incidence count gives the dual bound

\[
 \boxed{
 \Pr(\operatorname{row}_rD_L=L)
 \le\frac{12(r'+1)}{s_rs_{r'}}
 \le\frac{27}{r+1}.}                                    \tag{2.6}
\]

The quantifier in (2.3) and (2.6) is important: the line \(L\) is arbitrary, and the
normalization rule may depend on the whole transcript.  Only the finite left- or
right-associate orbit is used.

## 3. Every independent-output hand and both product orders

Call the inherited orientation of \(D_R\) its **good row**, and that of \(D_L\) its
**good image**.  At a fixed prime \(r\), a good line is uniform on a set of size
\(s_r\), so every atom is at most \(1/s_r\).  A wrong image of \(D_R\), or wrong row
of \(D_L\), has every atom at most \(27/(r+1)\) by Section 2.  Fixed projective
bijections preserve these atom bounds.

If \(X,Y\) come from independent finder transcripts and \(f,g\) are fixed
projective bijections, then

\[
 \Pr(f(X)=g(Y))
 \le \min\bigl(\max_L\Pr(X=L),\max_L\Pr(Y=L)\bigr).      \tag{3.1}
\]

Here “independent outputs” includes the normalization choices: each normalization
may use its own complete call transcript and private randomness, but not the other
output's transcript.  A joint rule that chooses both normalizers after seeing both
calls is an adaptive joint decoder and is not justified by (3.1).

Thus a comparison involving at least one good orientation costs at most \(1/s_r\),
while a wrong--wrong comparison costs at most \(27/(r+1)\).  Since
\(1/s_r\le(3/2)/(r+1)\), every case is bounded by \(27/(r+1)\).

This covers all one-sided gcd hands for all choices of output types:

* a gcrd compares \(\operatorname{row}_r(A)\) with
  \(\operatorname{row}_r(B)\);
* a gcld compares \(\operatorname{im}_r(A)\) with
  \(\operatorname{im}_r(B)\);
* \(A,B\) may independently be either a \(D_R\) or a separately computed \(D_L\).

To justify the first two bullets, reduce the ideal defining the one-sided gcd modulo
\(r\).  Two rank-one matrices generate the same minimal left ideal exactly when
their row lines agree; distinct minimal left ideals sum to all of \(M_2(\mathbf F_r)\).
Thus \(r\) divides the norm of their gcrd exactly at row equality.  The right-ideal
argument gives image equality for a gcld.  Since both inputs have squarefree norm
\(pq\), a proper gcd norm occurs exactly when the corresponding equality holds at
one of \(p,q\), but not both.

It also covers both matrix-product orders.  For nonzero rank-one matrices,

\[
 AB=0
 \quad\Longleftrightarrow\quad
 \operatorname{im}(B)=\ker(A).                          \tag{3.2}
\]

The kernel line of \(A\) is a fixed projective-dual transform of its row line.
Consequently

\[
 AB=0\iff \operatorname{im}(B)=\kappa(\operatorname{row}(A)),
\]

and

\[
 BA=0\iff \operatorname{im}(A)=\kappa(\operatorname{row}(B)).
\]

For every assignment \(A,B\in\{D_R,D_L\}\), these are again good--good,
good--wrong, or wrong--wrong equalities between independent outputs.  Inserting any
fixed Hurwitz-unit/projective transforms merely replaces the displayed maps by fixed
projective bijections.

For the product test, take the integer gcd of \(N\) with the four doubled Hurwitz
coefficients of \(AB\) (or \(BA\)); doubling is harmless because \(N\) is odd.  It
is proper exactly when the product matrix vanishes at one prime and not the other.

A proper one-sided gcd or a proper product-zero divisor requires its local relation
to hold at exactly one of \(p,q\).  No independence between the two local events is
needed for the union bound

\[
 \boxed{
 \Pr(\text{proper outcome for one fixed comparison})
 \le27\left(\frac1{p+1}+\frac1{q+1}\right).}             \tag{3.3}
\]

Equation (3.3) is per fixed menu entry.  If a predetermined projective menu has
\(T\) entries, its union has probability at most \(27T\) times the parenthesis.  If
\(K\) independent outputs and all pairs are used, another factor at most \(K^2\)
appears.  These statements remain valid for any fixed polynomials \(K,T\) in input
bit length.

There are infinitely many odd-prime pairs \(p<q<2p\), by Bertrand's postulate.  On
this balanced family, \(p,q=\Theta(\sqrt N)\).  If
\(L=\lceil\log_2(N+1)\rceil\) and \(K,T\le\operatorname{poly}(L)\), all the named
independent-output tests together succeed with probability at most

\[
 O\left(\frac{K^2T}{\sqrt N}\right)
 =2^{-L/2+O(\log L)}.                                   \tag{3.4}
\]

The residual-only finder and the standard fixed normalizations and direct
gcd/product tests use expected \(\operatorname{poly}(L)\) bit operations, including
exact random-bit generation; hence a polynomial batch of such operations has
expected polynomial bit cost.  (The probability bounds themselves also allow an
arbitrary per-call normalization rule, but no efficiency claim is made for an
arbitrarily expensive rule.)  Equation (3.4) says the named polynomial-time batch's
success is exponentially sparse, and blind repetition of that batch would have
exponential expected cost.  It does not apply to a genuine joint decoder whose
output is not the union of these rare relations.

## 4. Wrong-hand single-output unit stabilizers

The projective Hurwitz-unit group

\[
 G=\mathcal H^\times/\{\pm1\}
\]

has order 12 and is \(A_4\).  Its action on \(\mathbf P^1(\mathbf F_r)\) is faithful
for every odd \(r\), including 3.  Indeed, a projectively trivial unit would reduce
to a scalar in \(M_2(\mathbf F_r)\).  Apart from \(\pm1\), every Hurwitz unit has a
noncentral coefficient \(\pm1\) or \(\pm1/2\), which cannot vanish in odd
characteristic.

The union \(E_r\) of lines with nontrivial stabilizer has size at most 14.  The three
involution subgroups each fix at most two projective lines, contributing at most six.
The eight elements of order three form four cyclic subgroups, and the two
nonidentity elements in one subgroup have the same fixed set, of size at most two.
They contribute at most eight more.  This count also covers characteristic 3, where
an order-three element can be nontrivial unipotent and has only one fixed line.

For a fixed gcrd output \(D_R\), draw actual left units \(U_1,U_2\) independently
and uniformly from the 24 units and compare \(U_1D_R,U_2D_R\) by a gcld.  Their
relative projective class is uniform in \(G\).  If

\[
 H_r^{\rm im}(D_R)=\operatorname{Stab}_G(\operatorname{im}_rD_R),
\]

then, exactly,

\[
 \Pr(\text{proper gcld}\mid D_R)
 =\frac{|H_p^{\rm im}(D_R)\mathbin\triangle
          H_q^{\rm im}(D_R)|}{12}.                       \tag{4.1}
\]

In particular, an exhaustive menu of the 12 relative projective classes succeeds if
and only if the two stabilizers differ.  If both wrong-hand lines lie outside their
exceptional sets, both stabilizers are trivial.  The atom bound (2.5) therefore gives

\[
\begin{aligned}
 \Pr(H_p^{\rm im}(D_R)\ne H_q^{\rm im}(D_R))
 &\le \Pr(\operatorname{im}_pD_R\in E_p)
      +\Pr(\operatorname{im}_qD_R\in E_q)\\
 &\le378\left(\frac1{p+1}+\frac1{q+1}\right).
\end{aligned}                                            \tag{4.2}
\]

because \(14\cdot27=378\).  Dually, right-unit multiples of one \(D_L\), compared
by gcrd through its wrong row lines, obey the same exact conditional formula and the
same bound.  Polynomially many outputs remain exponentially sparse on the balanced
family.

## 5. The total same-source row--image graph

Let

\[
 C=zj+wk.
\]

In the splitting (1.2), left multiplication by \(C\) is represented on column
vectors by

\[
 J_{C,r}=\begin{pmatrix}A&B\\B&-A\end{pmatrix}.          \tag{5.1}
\]

Since \(A^2+B^2=-R\),

\[
 J_{C,r}^2=-R I,                                        \tag{5.2}
\]

a unit scalar.  We claim the total graph

\[
 \boxed{
 \operatorname{im}_r(\beta)=
 J_{C,r}\operatorname{row}_r(\beta)}                    \tag{5.3}
\]

at every conic point, including the exceptional ones.

Suppose first that the first row

\[
 v=(x+A,y+B)
\]

and first column

\[
 u=(x+A,B-y)^T
\]

are nonzero.  A direct determinant calculation, using
\(x^2+y^2=A^2+B^2\), gives

\[
\begin{aligned}
 \det(u,J_{C,r}v^T)
 &=(x+A)(Bx-Ay)\\
 &\quad-(B-y)(Ax+By+A^2+B^2)\\
 &=B(x^2+y^2-A^2-B^2)=0.
\end{aligned}
\]

As \(J_{C,r}\) is invertible, \(J_{C,r}v^T\ne0\), proving (5.3) there.

At the row-exception point \((x,y)=(-A,-B)\), the row line is
\([B:-A]\), while the image is the vertical line.  But

\[
 J_{C,r}(B,-A)^T=(0,A^2+B^2)^T,
\]

so (5.3) still holds.  At the column-exception point \((-A,B)\), the row line is
\([0:1]\), while the second column gives image line \([B:-A]\); and

\[
 J_{C,r}(0,1)^T=(B,-A)^T.
\]

These checks remain valid when the two exceptional points coincide (which can occur
when \(B=0\)).  Thus the graph is total.

This identity exhibits dependence that Sections 2--4 intentionally did not discard:
row and image of one raw output are deterministically linked once \(C\) is known.

## 6. Exact split-free same-source unit criteria

For a Hurwitz quaternion \(X\), let \([i](X)\) denote its \(i\)-coefficient.  The
integer \(2[i](X)\) is defined even for a half-integral Hurwitz element.  In every
odd local splitting of the form (1.2), transpose fixes the matrices of \(1,j,k\) and
negates the matrix of \(i\).  Hence

\[
 X_r\text{ is symmetric}
 \quad\Longleftrightarrow\quad
 2[i](X)=0\pmod r.                                      \tag{6.1}
\]

For a nonzero rank-one matrix, symmetry is equivalent to equality of its row and
image lines: writing it as \(uv^T\), those lines agree exactly when \(u\) and \(v\)
are proportional.  Formula (6.1) therefore turns a projective same-source relation
into an intrinsic quaternion coefficient test, with no choice of \(s,t\) remaining.

First take the left gcd \(D_L\), which inherits \(\operatorname{im}\beta\), and a
right unit \(U\).  Put

\[
 Q_L=\bar C D_L.
\]

Because \(C\bar C=\bar C C=R\) and (5.3) holds,

\[
 \operatorname{im}_rQ_L
 =\bar C\operatorname{im}_rD_L
 =\bar C C\operatorname{row}_r\beta
 =\operatorname{row}_r\beta.                            \tag{6.2}
\]

Left multiplication by the invertible \(\bar C\) does not change a row line, and
right multiplication by \(U\) does not change an image line.  Applying (6.1) to
\(Q_LU\) yields the exact criterion

\[
 \boxed{
 \operatorname{row}_r(D_LU)=\operatorname{row}_r\beta
 \quad\Longleftrightarrow\quad
 2[i](\bar C D_LU)=0\pmod r.}                            \tag{6.3}
\]

Now take the right gcd \(D_R\), which inherits \(\operatorname{row}\beta\), and a
left unit \(U\).  The row line of \(\bar CUD_R\) is still
\(\operatorname{row}\beta\).  Its image equals that row line precisely when
\(\operatorname{im}(UD_R)=C\operatorname{row}\beta=operatorname{im}\beta\).
Thus

\[
 \boxed{
 \operatorname{im}_r(UD_R)=\operatorname{im}_r\beta
 \quad\Longleftrightarrow\quad
 2[i](\bar CUD_R)=0\pmod r.}                             \tag{6.4}
\]

These are the two requested split-free criteria.

Normalization does not alter an exhaustive projective menu.  Replacing \(D_L\) by
\(D_LV\) sends the variable class \(U\) in (6.3) to \(VU\), a permutation of the
12 classes of \(G\).  Replacing \(D_R\) by \(VD_R\) sends \(U\) in (6.4) to
\(UV\), again a permutation.  The two actual signs give opposite coefficients and
the same zero test.

## 7. What the same-source criteria do and do not prove

Equations (6.3)--(6.4) make each fixed unit-class test exact, but they do not show
that one of the 12 coefficients must vanish modulo exactly one factor.  Section 8
gives a finite certificate where none vanishes modulo either factor.  That certificate
refutes such a universal claim; it does not establish an asymptotic distribution.

## 8. Hand verification of the \(N=91\) certificate

Take

\[
 N=91=7\cdot13,\qquad M=273=3\cdot7\cdot13,
\]

and

\[
 \beta=172+82i+k.
\]

First,

\[
 172^2=29584,\qquad 82^2=6724,\qquad
 172^2+82^2=36308=273\cdot132+272.
\]

Thus \(R=-172^2-82^2\equiv1\pmod{273}\), and \((z,w)=(0,1)\) is a completion;
in particular \(C=k\).  Moreover

\[
 \operatorname{nrd}(\beta)=36309
 =273\cdot133=91\cdot399=3\cdot7^2\cdot13\cdot19.       \tag{8.1}
\]

The coefficients are primitive because one of them is 1.

Define

\[
 D_R=\frac{-19+i+j+k}{2},\qquad
 D_L=\frac{-19+i-j+k}{2}.                                \tag{8.2}
\]

Both have norm

\[
 \frac{19^2+1+1+1}{4}=\frac{364}{4}=91.                 \tag{8.3}
\]

The required right-sided factorizations are

\[
\begin{aligned}
 91&=\bar D_R D_R,\\
 \beta&=\frac{-35-19i-j-3k}{2}\,D_R.
\end{aligned}                                            \tag{8.4}
\]

The left-sided factorizations are

\[
\begin{aligned}
 91&=D_L\bar D_L,\\
 \beta&=D_L\,\frac{-35-19i+j-3k}{2}.
\end{aligned}                                            \tag{8.5}
\]

For example, multiplying the numerator vectors in the second line of (8.4) gives

\[
 (688,328,0,4),
\]

and division by 4 gives \((172,82,0,1)\).  The last line gives the same numerator
vector.  Each complementary factor has norm

\[
 \frac{35^2+19^2+1+3^2}{4}=\frac{1596}{4}=399,
\]

consistent with (8.1).  Thus \(D_R\) is a common right divisor and \(D_L\) a common
left divisor of norm 91; the primitive odd-norm lemma makes them a gcrd and gcld,
respectively.

Use the following 12 representatives of the projective unit classes, in this order:

\[
\begin{gathered}
 1, i, j, k,\\
 \frac{1-i-j-k}{2},\ \frac{1-i-j+k}{2},\
 \frac{1-i+j-k}{2},\ \frac{1-i+j+k}{2},\\
 \frac{1+i-j-k}{2},\ \frac{1+i-j+k}{2},\
 \frac{1+i+j-k}{2},\ \frac{1+i+j+k}{2}.
\end{gathered}                                           \tag{8.6}
\]

Since \(\bar C=-k\),

\[
 (-k)D_L=\frac{1-i-j+19k}{2}.
\]

For \(U=u_0+u_1i+u_2j+u_3k\), direct quaternion multiplication gives

\[
 2[i]((-k)D_LU)=-u_0+u_1-19u_2-u_3.                    \tag{8.7}
\]

Evaluating (8.7) on (8.6) gives, in order,

\[
 \boxed{(-1,1,-19,-1,9,8,-10,-11,10,9,-9,-10).}        \tag{8.8}
\]

Similarly, left multiplication by \(-k\) sends the coefficient vector of \(U\) to
\((u_3,u_2,-u_1,-u_0)\).  Multiplication on the right by \(D_R\) therefore gives

\[
 2[i]((-k)UD_R)=u_0-u_1-19u_2+u_3,                     \tag{8.9}
\]

and the same ordered unit list yields

\[
 \boxed{(1,-1,-19,1,10,11,-9,-8,9,10,-10,-9).}         \tag{8.10}
\]

The absolute values occurring in (8.8)--(8.10) are

\[
 \{1,8,9,10,11,19\}.
\]

None is divisible by 7 or 13, so every displayed coefficient is coprime to 91.
Consequently neither complete 12-class same-source menu has a zero at \(7\) or
\(13\).  This is one exact finite obstruction only; no asymptotic conclusion is
drawn from it.

## 9. The narrow pooling statement

For independent samples indexed by \(t\), define

\[
 Q_t=\bar C_tD_{L,t},
 \qquad
 L_{t,r}=\operatorname{row}_r\beta_t.
\]

Equation (6.2) gives, at each \(r=p,q\),

\[
 \boxed{\operatorname{im}_rQ_t=L_{t,r}.}                \tag{9.1}
\]

The reductions of the Hurwitz units span all of \(M_2(\mathbf F_r)\): already
\(1,i,j,k\) are a basis in odd characteristic.  Therefore

\[
 \operatorname{span}_{\mathbf F_r}\{Q_tU:U\in\mathcal H^\times\}
 =Q_tM_2(\mathbf F_r).                                   \tag{9.2}
\]

Since \(Q_t\) has rank one, this is the two-dimensional right ideal consisting of
all matrices whose columns, hence whose image, lie in \(L_{t,r}\).

For a nonempty pooled subset \(T\), its full unit span is the sum of these right
ideals.  If all \(L_{t,r}\), \(t\in T\), coincide, the sum is one two-dimensional
ideal.  If two of the lines are distinct, they span \(\mathbf F_r^2\), and every
matrix can be formed column by column as a sum of vectors in the two lines.  The sum
is then all of \(M_2(\mathbf F_r)\), of dimension four.  Equivalently, two distinct
such ideals have zero intersection, so dimension three cannot occur.  Hence

\[
 \boxed{
 \dim\operatorname{span}\{Q_tU:t\in T, U\in\mathcal H^\times\}
 =\begin{cases}
 2,&\text{all }L_{t,r}\text{ coincide},\\
 4,&\text{otherwise}.
 \end{cases}}                                            \tag{9.3}
\]

For a fixed subset of size at least two, the dimension-two outcome is therefore just
an all-equal event among independent uniform lines in \(\mathcal S_r\), with
probability \(s_r^{1-|T|}\le1/s_r\).  A predetermined polynomial family of
dimension-only subset profiles is a polynomial union of such equality/birthday
events and remains exponentially sparse on balanced semiprimes.  Singleton subsets
always have dimension two and contain no local separation information.

## 10. Boundary left open

The arguments above do not cover any of the following:

* adaptive or implicitly defined subset selection;
* use of the exact pooled row spaces rather than their dimensions;
* systems formed from coefficients, pivots, or minors;
* resultants or other elimination across many relations;
* noncommutative products of sample-dependent quaternions;
* spectral or discrepancy statistics;
* nonlinear joint decoders;
* bias in the actual fibre point beyond the projective marginals proved here.

Those mechanisms can combine common nonzero information and need not succeed by the
occurrence of one rare equality.  Treating them as a union of the tests bounded above
would be a quantifier error.  Conversely, the exact same-source graph and coefficient
criteria identify structure a future joint analysis may use; they do not themselves
supply a factor.
