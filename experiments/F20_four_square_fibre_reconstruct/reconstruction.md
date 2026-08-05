# Proof-blind reconstruction: the four-square residual fibre and matched one-sided tests

## Verdict

The corrected claim is true, with the scope qualifications in its last paragraph.  The
essential local fact is stronger than a counting heuristic: after a residual and a
completion have been fixed, each nonzero conic fibre is carried **bijectively** to the
set of non-isotropic projective lines.  The exceptional conic point at which the first
row (or first column) vanishes supplies exactly the one projective line missed by the
usual nonexceptional formula.

The Pollack--Treviño source claim was checked against the primary paper:
Paul Pollack and Enrique Treviño, [*Finding the Four Squares in Lagrange's
Theorem*](https://www.pollack-math.net/finding4squares.pdf), INTEGERS 18 (2018),
article A15.  In particular, the preprocessing and modulus below are those in
Section 4, not a simplified substitute.  Their paper counts arithmetic operations;
the exact-uniform random-bit and bit-complexity conversion is supplied below.

No computation was used in this reconstruction.

## 1. Setup and the conditional fibre law

Let

\[
  n=pq
\]

with distinct odd primes \(p,q\), and let \(M\) be an odd squarefree multiple of
\(n\).  Initially \((x,y)\) is exactly uniform in \((\mathbf Z/M\mathbf Z)^2\), and

\[
  R=-x^2-y^2\pmod M.
\]

The acceptance/completion kernel sees \((x,y)\) only through \(R\) and fresh
randomness.  Fix an accepted residual \(\rho\) and fix the completion randomness (or,
equivalently, a particular completion outcome of positive conditional probability).
Every point in

\[
  F_\rho=\{(x,y)\bmod M:x^2+y^2=-\rho\pmod M\}
\]

had the same initial mass \(M^{-2}\), and the kernel assigns the same conditional
weight to every such point.  Therefore \((x,y)\mid(\rho,\text{completion data})\) is
uniform on \(F_\rho\).

As \(M\) is squarefree, CRT identifies this fibre with

\[
  F_\rho\simeq
  \prod_{\ell\mid M}
  \{(X,Y)\in\mathbf F_\ell^2:X^2+Y^2=-\rho\}.
\]

Consequently its projection at each \(r\in\{p,q\}\) is uniform on the corresponding
conic.  Acceptance says that \(\rho\) is a unit modulo \(M\), so this conic has
nonzero right-hand side.

This conditioning step is exactly where the residual-only hypothesis is used.  A
kernel allowed to inspect \(x\) or \(y\) separately could reweight a conic fibre and
the conclusion would fail.

## 2. Explicit local splitting and the two bijections

Fix an odd prime \(r\mid n\), put

\[
  \chi_r=\left(\frac{-1}{r}\right),\qquad
  \mathcal S_r=\{[u:v]\in\mathbf P^1(\mathbf F_r):u^2+v^2\ne0\}.
\]

There are \(1+\chi_r\) isotropic projective lines (two if \(-1\) is a square and none
otherwise), whence

\[
  |\mathcal S_r|=r+1-(1+\chi_r)=r-\chi_r.                 \tag{2.1}
\]

Choose \(s,t\in\mathbf F_r\) with \(s^2+t^2=-1\).  Such a pair exists; in fact a
standard quadratic-character count gives \(r-\chi_r>0\) solutions to
\(s^2+t^2=-1\).  Since 2 is invertible, reduction of the Hurwitz order has the basis
\(1,i,j,k\), and the assignment

\[
 i\longmapsto
 I=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
 j\longmapsto
 J=\begin{pmatrix}s&t\\t&-s\end{pmatrix}
                                                        \tag{2.2}
\]

gives an isomorphism \(\mathcal H/r\mathcal H\simeq M_2(\mathbf F_r)\).  Indeed,
\(I^2=J^2=-1\), \(IJ=-JI\), and the four displayed basis matrices are linearly
independent.  Also

\[
 IJ=\begin{pmatrix}t&-s\\-s&-t\end{pmatrix}.
\]

Fix the completion \((z,w)\) modulo \(r\), and set

\[
  A=zs+wt,\qquad B=zt-ws.
\]

Since \(s^2+t^2=-1\),

\[
  A^2+B^2=-(z^2+w^2)=-\rho.                              \tag{2.3}
\]

For

\[
  \beta=x+yi+zj+wk
\]

the split matrix is

\[
  \beta_r=
  \begin{pmatrix}
    x+A&y+B\\
    -y+B&x-A
  \end{pmatrix}.                                         \tag{2.4}
\]

Its determinant is \(x^2+y^2+z^2+w^2=0\).  It is not the zero matrix because
\(x^2+y^2=-\rho\ne0\), so it has rank one and hence well-defined row and image
lines.

### Row line

Write \(c=-\rho=A^2+B^2\ne0\).  Except at \((x,y)=(-A,-B)\), use the first row and
consider

\[
  (x,y)\longmapsto[x+A:y+B].                              \tag{2.5}
\]

Given a non-isotropic target \([u:v]\), a nonzero first row on that line has the form
\((x+A,y+B)=\lambda(u,v)\).  The conic equation becomes

\[
  \lambda^2(u^2+v^2)-2\lambda(Au+Bv)=0.                  \tag{2.6}
\]

If \(Au+Bv\ne0\), there is exactly one allowed nonzero value,

\[
  \lambda=\frac{2(Au+Bv)}{u^2+v^2}.
\]

There is exactly one non-isotropic target for which \(Au+Bv=0\), namely
\([-B:A]\); it is non-isotropic because \(A^2+B^2=c\ne0\).  That target is supplied
by the omitted conic point.  At \((x,y)=(-A,-B)\), the first row vanishes but the
second row is

\[
  (2B,-2A),
\]

whose line is \([-B:A]\).  Thus (using the nonzero row when the first row vanishes)
the conic maps bijectively to \(\mathcal S_r\).

### Image line

Except at \((x,y)=(-A,B)\), use the first column:

\[
  (x,y)\longmapsto[x+A:B-y].                              \tag{2.7}
\]

Writing this column as \(\lambda(u,v)^T\) gives

\[
  x=\lambda u-A,\qquad y=B-\lambda v,
\]

and exactly the same equation (2.6).  Hence every target other than \([-B:A]\) has
one preimage.  At the exceptional point \((-A,B)\), the first column vanishes and the
second column is again \((2B,-2A)^T\), supplying \([-B:A]\).  This is a second
bijection from the conic to \(\mathcal S_r\).

Combining these bijections with Section 1 proves, for each \(r=p,q\), that conditional
on the accepted residual and completion randomness, both the row line and the image
line of \(\beta_r\) are exactly uniform on \(\mathcal S_r\).  The two assertions are
separate: they do not assert independence between the row and image line of the same
matrix.

## 3. The primitive one-sided-gcd norm lemma and handedness

Let

\[
 \mathcal H=\mathbf Z\left[i,j,\frac{1+i+j+k}{2}\right].
\]

The following is Pollack--Treviño Lemma 2; a complete argument is included because
both primitivity and the side of normalization matter here.

**Primitive gcrd lemma.**  Let \(m\) be odd and let
\(\gamma=a+bi+cj+dk\in\mathcal H\) have integral coordinates with
\(\gcd(a,b,c,d)=1\).  If \(m\mid\operatorname{nrd}(\gamma)\), then every greatest
common right divisor of \(m\) and \(\gamma\) has reduced norm \(m\).

**Proof.**  Put

\[
  L=\mathcal Hm+\mathcal H\gamma=\mathcal H d.
\]

Conjugation gives the right ideal

\[
  \bar L=m\mathcal H+\bar\gamma\mathcal H=\bar d\mathcal H.
\]

Here and below the product of ideals means the additive ideal generated by all
products.  Then

\[
  L\bar L=\mathcal H d\bar d\mathcal H
          =\operatorname{nrd}(d)\mathcal H.               \tag{3.1}
\]

Expanding the other description of the product shows \(L\bar L\subseteq m\mathcal H\):
both cross terms contain a factor \(m\), and
\(\gamma\bar\gamma=\operatorname{nrd}(\gamma)\) is divisible by \(m\).  Therefore

\[
  B=m^{-1}L\bar L
\]

is a two-sided ideal of \(\mathcal H\).  It contains \(m\), every element
\(\bar\gamma\epsilon\), and every element \(\epsilon\gamma\), for
\(\epsilon\in\mathcal H\).  In particular it contains

\[
 \gamma+\bar\gamma=2a,\quad
 \bar\gamma i-i\gamma=2b,\quad
 \bar\gamma j-j\gamma=2c,\quad
 \bar\gamma k-k\gamma=2d.
\]

Primitivity gives \(2\in B\).  Since \(m\) is odd and \(m\in B\), Bézout gives
\(1\in B\), so \(B=\mathcal H\).  Thus (3.1) equals \(m\mathcal H\).  Intersecting
the two central ideals with \(\mathbf Z\), or comparing their lattice indices, gives
\(\operatorname{nrd}(d)=m\).  ∎

The corresponding gcld statement follows by conjugation.

Apply the lemma with \(m=n\) and \(\gamma=\beta\).  Completion makes \(\beta\)
primitive, and \(n\mid M\mid\operatorname{nrd}(\beta)\), so a gcrd \(D_R\) and a
separately computed gcld \(D_L\) both have norm \(n\).

A Hurwitz quaternion of odd norm can be made integral by multiplication by a unit.
For clarity, if

\[
 D=\tfrac12(a+bi+cj+dk),\qquad a,b,c,d\text{ odd},
\]

choose signs \(e_0,e_1,e_2,e_3\in\{\pm1\}\) satisfying

\[
 e_0\equiv a,\quad e_1\equiv-b,\quad e_2\equiv-c,\quad e_3\equiv-d\pmod4.
\]

Then \(e=(e_0+e_1i+e_2j+e_3k)/2\) is a unit and \(eD\) has integral
coordinates.  A gcrd generator is ambiguous by a unit **on the left**, so this is the
correct normalization and does not change its row line.  By conjugation, a gcld is
normalized by a unit **on the right**, which does not change its image line.

It remains to verify inheritance.  Modulo \(r\mid n\),

\[
  \mathcal Hn+\mathcal H\beta=\mathcal H D_R
\]

becomes

\[
  M_2(\mathbf F_r)\beta_r=M_2(\mathbf F_r)(D_R)_r.        \tag{3.2}
\]

For a nonzero rank-one matrix \(C\), \(M_2C\) is exactly the set of matrices whose
rows lie in the row line of \(C\).  Both matrices in (3.2) are nonzero rank one:
\(\beta_r\) was handled above, and \(\operatorname{nrd}(D_R)=pq\) is divisible by
\(r\) but not \(r^2\).  Equality in (3.2) therefore gives

\[
  \operatorname{row}_r(D_R)=\operatorname{row}_r(\beta).
\]

Similarly,

\[
  n\mathcal H+\beta\mathcal H=D_L\mathcal H
\]

reduces to equality of right ideals.  Since \(CM_2\) is the set of matrices whose
columns lie in \(\operatorname{im}(C)\),

\[
  \operatorname{im}_r(D_L)=\operatorname{im}_r(\beta).
\]

This proves precisely the claimed handedness and no more.

## 4. Independent calls and matched-handed collision bounds

Take two independent finder calls and their normalized gcrd outputs \(D_1,D_2\).
Let \(G_R\) be a gcrd of \(D_1,D_2\).  Since it right-divides an element of norm
\(n=pq\),

\[
  \operatorname{nrd}(G_R)\in\{1,p,q,n\}.                 \tag{4.1}
\]

Reduction of \(\mathcal H D_1+\mathcal H D_2\) modulo \(r\) shows

\[
 r\mid\operatorname{nrd}(G_R)
 \quad\Longleftrightarrow\quad
 \operatorname{row}_r(D_1)=\operatorname{row}_r(D_2).    \tag{4.2}
\]

Indeed, equal row lines give one minimal left ideal; two distinct row lines span all
of \(M_2(\mathbf F_r)\).  Each local row line is uniform on \(\mathcal S_r\), and
the calls are independent, so

\[
 \Pr(\operatorname{row}_r(D_1)=\operatorname{row}_r(D_2))
 =\frac1{r-\chi_r}.                                      \tag{4.3}
\]

A proper gcd norm is the exclusive-or of the equality events at \(p\) and \(q\).
Without making any independence assumption about those two local events, the union
bound gives

\[
 \Pr(1<\operatorname{nrd}(G_R)<n)
 \le \frac1{p-\chi_p}+\frac1{q-\chi_q}.                  \tag{4.4}
\]

The same proof, with image lines and right ideals, gives (4.4) for a gcld of two
separately computed normalized gcld outputs.  This is what “matched handedness”
means.

For \(K\) independent calls, all unordered pairs in one handedness therefore have
success probability at most

\[
 \binom K2\left(\frac1{p-\chi_p}+\frac1{q-\chi_q}\right). \tag{4.5}
\]

Fixed unit classes only multiply this bound by a constant.  More explicitly, for
gcrd outputs the relevant transforms are right units.  For fixed projective unit
classes \(g,h\), equality of transformed row lines has probability

\[
 \frac{|\mathcal S_r g\cap\mathcal S_r h|}{|\mathcal S_r|^2}
 \le\frac1{|\mathcal S_r|}.                              \tag{4.6}
\]

There are only 12 relative projective classes; all 24 actual units collapse modulo
the central signs.  For gcld outputs, the analogous fixed transforms are left units
and the same estimate applies to image lines.  Thus testing both handednesses and
all relative projective unit classes costs at most the fixed factor \(24\) in (4.5).

## 5. A single unit orbit

Let

\[
  \overline{\mathcal H^\times}=\mathcal H^\times/\{\pm1\}=:G.
\]

This group has order 12 and is \(A_4\): the classes of \(i,j,k\) form the normal
Klein four subgroup, while the eight half-integral classes have order three and
cyclically permute its three nonidentity elements.

For a fixed gcrd output \(D_R\), define

\[
 H_r^{\rm row}(D_R)=
 \{g\in G:\operatorname{row}_r(D_R)g=\operatorname{row}_r(D_R)\}.
\]

Draw actual right units \(U_1,U_2\) independently and uniformly from the 24 units.
Their projective classes are independent uniform elements of \(G\), and the relative
class \(g=[U_1U_2^{-1}]\) is uniform in \(G\).  The local row lines of
\(D_RU_1,D_RU_2\) agree exactly when \(g\in H_r^{\rm row}(D_R)\).  By (4.1)--(4.2),

\[
 \Pr\bigl(\text{proper gcrd}(D_RU_1,D_RU_2)\mid D_R\bigr)
 =\frac{|H_p^{\rm row}(D_R)\mathbin\triangle
          H_q^{\rm row}(D_R)|}{12}.                      \tag{5.1}
\]

If the two stabilizers differ, this gives expected at most 12 independent unit-pair
trials; if they agree, no number of such trials can work.

For a fixed, separately computed gcld output \(D_L\), use actual left units
\(U_1D_L,U_2D_L\) and define image-line stabilizers.  The identical argument gives

\[
 \Pr\bigl(\text{proper gcld}(U_1D_L,U_2D_L)\mid D_L\bigr)
 =\frac{|H_p^{\rm im}(D_L)\mathbin\triangle
          H_q^{\rm im}(D_L)|}{12}.                        \tag{5.2}
\]

### Faithfulness, including characteristic 3

For every odd \(r\), the action \(G\to\operatorname{PGL}_2(\mathbf F_r)\) is
faithful.  If a unit acts trivially projectively, its reduction in
\(M_2(\mathbf F_r)\) is scalar.  In the basis \(1,i,j,k\), every unit other than
\(\pm1\) has at least one noncentral coefficient equal to \(\pm1\) or \(\pm1/2\).
These coefficients are nonzero in every odd characteristic.  Hence the kernel is
exactly the already-quotiented \(\{\pm1\}\).  This argument does not exclude
\(r=3\); in particular the order-three elements become nontrivial unipotents rather
than scalars there.

### Exact exceptional-line counts

Let \(E_r^{\rm row}\subseteq\mathcal S_r\) be the row lines having nontrivial
\(G\)-stabilizer, and define \(E_r^{\rm im}\) analogously.  The two sets have the
same cardinality, denoted \(e_r\).

For \(r\ge5\), the three projective involutions are represented by the pure units.
Each has characteristic polynomial \(T^2+1\), hence two rational fixed lines exactly
when \(\chi_r=1\).  Their fixed-line pairs are disjoint: a common eigenline for, say,
\(i\) and \(j\) would contradict \(ij=-ji\) in odd characteristic.  This gives six
projective fixed lines when \(\chi_r=1\).  Exactly two of them, the fixed lines of
\(i\), satisfy \(u^2+v^2=0\) and are excluded from \(\mathcal S_r\).  Thus
involutions contribute exactly four lines to \(E_r\) when \(\chi_r=1\), and zero
otherwise.

There are four cyclic subgroups of order three.  A half-integral unit representing a
nonidentity element has determinant 1 and trace \(\pm1\), so its characteristic
discriminant is \(-3\).  Each subgroup therefore has two rational fixed lines exactly
when \(\left(\frac{-3}{r}\right)=1\).  Fixed lines belonging to distinct order-three
subgroups are disjoint, and none overlaps an involution-fixed line: otherwise the
corresponding subgroups would generate all of \(A_4\), forcing a global fixed line and
in particular a forbidden common eigenline for \(i,j\).  The order-three contribution
is consequently eight or zero.  Hence

\[
 \boxed{
 e_r=4\,\mathbf1_{\left(\frac{-1}{r}\right)=1}
      +8\,\mathbf1_{\left(\frac{-3}{r}\right)=1}
 \quad(r\ge5).}                                          \tag{5.3}
\]

In characteristic 3, the involutions have no rational eigenlines.  Each of the four
order-three subgroups is nontrivial unipotent and has one fixed line.  Faithfulness
forces the resulting \(A_4\)-action on the four points of \(\mathbf P^1(\mathbf F_3)\)
to be the transitive degree-four action, so these four lines are distinct, each with a
cyclic stabilizer of order three.  Since \(\chi_3=-1\), all four projective lines lie
in \(\mathcal S_3\).  Thus

\[
 \boxed{e_3=4.}                                           \tag{5.4}
\]

Since each local finder line is uniform on \(\mathcal S_r\),

\[
 \Pr(H_r\ne\{1\})=\frac{e_r}{r-\chi_r}.                  \tag{5.5}
\]

If both local stabilizers are trivial then they are equal.  No assumption about their
joint distribution is needed for

\[
 \Pr(H_p\ne H_q)
 \le \frac{e_p}{p-\chi_p}+\frac{e_q}{q-\chi_q}
 =O\left(\frac1p+\frac1q\right).                         \tag{5.6}
\]

Equations (5.3)--(5.4) sharpen the cruder union-of-fixed-points bound of 22.

## 6. The unconditional Pollack--Treviño finder really has this interface

This subsection uses the notation of the present claim; Pollack--Treviño call the
modulus below \(N\).

Their unconditional algorithm first removes the factor 2 and every prime
\(\ell\le\log n\), \(\ell\equiv1\pmod4\), retaining their exponents and known
two-square representations for later multiplication.  Thus the residual input is odd
and has no such prime divisor.  Restrict now to the claimed case in which that
residual input is still the distinct-prime semiprime \(n=pq\).  Put exactly

\[
 P=\prod_{\substack{\ell\le\log n\\\ell\equiv3\ (4)}}\ell,
 \qquad
 M=\frac{nP}{\gcd(n,P)}=\operatorname{lcm}(n,P).          \tag{6.1}
\]

Because \(n\) and \(P\) are squarefree and odd, \(M\) is an odd squarefree multiple
of \(n\).  The gcd in (6.1) is essential when a prime factor of \(n\) is itself among
the small \(3\bmod4\) primes.

In each trial the algorithm draws \(x,y\) uniformly from \([1,M]\), which is exactly
uniform modulo \(M\), and sets the least nonnegative residual

\[
 R=(-x^2-y^2)\bmod M.
\]

It rejects unless \(R\equiv1\pmod4\) and \(\gcd(R,M)=1\).  From an accepted
residual it removes the full powers of the precomputed primes
\(\ell\le\log n\), \(\ell\equiv1\pmod4\), writing \(R=R_1m\).  If \(m>1\), it
draws fresh \(u\in[1,m-1]\), computes

\[
 s=u^{(m-1)/4}\pmod m,
\]

and restarts unless \(s^2\equiv-1\pmod m\).  On success, the precomputed Gaussian
prime factors give \(a^2+b^2=R_1\), while

\[
 U+Vi=\gcd_{\mathbf Z[i]}(m,s+i)
\]

has norm \(m\) by their Lemma 1.  (If \(m=1\), take \(U=1,V=0\).)  Defining

\[
 z+wi=(a+bi)(U+Vi)
\]

gives \(z^2+w^2=R\), not merely a congruence.  Their Lemma 5 proves
\(\gcd(z,w)=1\), even if the successful \(m\) was composite.  Thus the completed
quaternion is primitive.

Here is the source's primitivity argument in the present notation.  The Gaussian
integer \(a+bi\) uses only one of the two conjugate Gaussian primes above each
rational prime dividing \(R_1\).  If a rational prime \(v\) divided both \(z\) and
\(w\), both conjugate primes \(\pi,\bar\pi\) above \(v\) would divide
\((a+bi)(U+Vi)\).  They cannot both divide \(a+bi\) by construction, and they cannot
both divide \(U+Vi\), since then the rational integer \(v\) would divide the common
divisor of \(m\) and \(s+i\), forcing \(v\mid s+i\) in \(\mathbf Z[i]\), which is
impossible because the coefficient of \(i\) is 1.  The only remaining allocation puts
one conjugate prime in each factor.  It would make \(v\) divide both \(R_1\), which
is supported on primes at most \(\log n\), and \(m\), from which all those primes
were removed.  This is again impossible.

Every rejection condition, the stripping of \(R_1\), the modular exponentiation,
the Gaussian gcd, and the final \((z,w)\) depend on \((x,y)\) only through \(R\) and
the fresh draw \(u\).  Also \(\gcd(R,M)=1\) makes every accepted residual a unit.
This is exactly the residual-only interface of Sections 1--2.

Pollack--Treviño Lemma 3 gives, for every unit \(a\bmod M\), the exact fibre size

\[
 M\prod_{\ell\mid M}
 \left(1-\left(\frac{-1}{\ell}\right)\frac1\ell\right).
\]

Because (6.1) includes every small \(3\bmod4\) prime and the reduced input includes
no small \(1\bmod4\) prime, their estimate makes this
\(\gg M\sqrt{\log\log n}\).  Their Lemma 4 supplies
\(\gg M\sqrt{\log\log n}/\log M\) residual integers \(R=R_1m\) for which \(m\) is
a prime \(1\bmod4\), exceeds \(\log n\), and does not divide \(M\).  Multiplying
the number of such residuals by their fibre sizes and dividing by the \(M^2\) choices
of \((x,y)\) gives probability \(\gg\log\log n/\log n\); conditional on such an
\(m\), exactly half of the nonzero \(u\)'s pass the square-root test.  Thus a whole
trial has success probability \(\Omega(\log\log n/\log n)\).  Hence the number of
trials is geometric with mean
\(O(\log n/\log\log n)\) and termination is almost sure.  They use
\(M\le n^{O(1)}\) and obtain

\[
 O\left(\frac{(\lg n)^2}{\lg\lg n}\right)
\]

expected arithmetic operations on \(O(\log n)\)-bit integers, in addition to a
smaller preprocessing term.  Their paper explicitly uses an arithmetic-operation
model and notes the conversion by multiplication complexity.

For completeness, exact uniform sampling introduces no hidden real-random oracle.
To sample uniformly from a range of size \(B\), draw
\(b=\lceil\log_2B\rceil\) fair bits, interpret them as \(T<2^b\), and reject if
\(T\ge B\).  Each round succeeds with probability greater than \(1/2\), so the draw
uses fewer than \(2b\) random bits in expectation and is exactly uniform.  Each
trial therefore uses \(O(\log n)\) expected random bits, and all trials together use
\(O((\log n)^2/\log\log n)\).  With schoolbook multiplication and division, the
source's operation count, all rejection overhead, preprocessing, Gaussian and
Hurwitz Euclidean algorithms, and verification are bounded by a fixed crude
polynomial such as

\[
 C(1+\lceil\log_2 n\rceil)^5
\]

in expected bit operations.  All intermediate integers have \(O(\log n)\) bits.
The finitely many inputs omitted by the source's \(n>20\) convention are handled
directly.  Thus the source algorithm is an unconditional exact-random finder of the
required kind for the reduced semiprime case.

## 7. Balanced semiprimes: the direct tests remain exponentially unlikely

There are infinitely many pairs of odd primes

\[
  p<q<2p
\]

by applying Bertrand's postulate after infinitely many choices of \(p\).  For
\(n=pq\) in this family,

\[
  p\asymp q\asymp\sqrt n.
\]

Let \(L=\lceil\log_2(n+1)\rceil\) and let \(K\le C_0L^c\) be any fixed polynomial
number of independent finder calls.  Testing every pair in both matched handednesses
and every relative projective unit class has, by (4.5)--(4.6), probability at most

\[
 O\left(\frac{K^2}{\sqrt n}\right).
\]

For the within-one-output unit-orbit test, even testing all unit pairs can succeed only
when the two local stabilizers differ.  Equations (5.3)--(5.6) and a union bound over
the \(K\) outputs give

\[
 O\left(\frac K{\sqrt n}\right).
\]

The combined success probability is therefore

\[
 2^{-L/2+O(\log L)},
\]

which is exponentially small in input bit length.  For sufficiently large balanced
primes, both factors exceed \(\log n\), so the semiprime is already in the reduced
case needed in Section 6.

## 8. Hostile scope audit

1. The proof controls the **row line of a gcrd output** and the **image line of a
   separately computed gcld output**.  It gives no law for the image line of the
   gcrd: left normalization can change that line.  Dually, it gives no law for the
   row line of the gcld.  Mixed-handed tests are therefore open.

2. The result concerns direct pairwise one-sided gcd collisions, their fixed unit
   transforms, and the single-output unit-stabilizer mechanism.  A sample-dependent
   nonlinear combination is not reduced to these events.

3. Oddness and squarefreeness are structural, not cosmetic.  At 2 the Hurwitz algebra
   is ramified; for repeated prime norms, reductions may have rank zero and higher
   local ideal depth.  Nothing here covers even norms or repeated-prime norms.

4. Marginal uniformity is all that was used in (4.4), (5.5), and (5.6).  In
   particular, no unproved independence of the \(p\)- and \(q\)-collision or
   stabilizer events was inserted.

5. This is an obstruction for the named tests on a special input family, not a
   factoring algorithm and not an impossibility theorem for integer factoring.
