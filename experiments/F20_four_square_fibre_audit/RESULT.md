# F20 hostile audit — the obstruction survives in both matched handednesses

**Audit verdict:** pass with source, conditioning, and scope corrections. The
candidate's right-handed local distribution theorem is correct. Its application
to the unconditional Pollack–Treviño algorithm is also correct whenever the
post-preprocessing target is a distinct-odd-prime semiprime, after replacing the
candidate's abbreviated auxiliary-modulus description by the paper's exact
formula. No independence between the two unknown-prime components is needed for
the stated upper bounds.

The candidate is unnecessarily weak in one important respect: the natural
left-handed version does **not** escape. The image-line map is a second copy of
the same conic-to-projective-line bijection. A separately computed greatest
common left divisor, normalized on the right, inherits that image line just as a
greatest common right divisor, normalized on the left, inherits the row line.

This does **not** prove an image-line law for the gcrd output. Left multiplication
in the gcrd and its left-unit normalization can change image space. Similarly,
the result does not prove a row-line law for the gcld output. Mixed-handed tests
on the “wrong” one-sided output remain open.

This is the hostile-audit step only. Under the project's verification vocabulary,
the corrected and strengthened theorem still needs a proof-blind reconstruction
before it can be verifier-backed.

**Primary source checked:** Paul Pollack and Enrique Treviño, [*Finding the Four
Squares in Lagrange's Theorem*](https://pollack.uga.edu/finding4squares.pdf),
INTEGERS 18A (2018), especially Lemma 2 and Section 4. This audit uses the paper
itself, not a secondary description.

**Computation:** none. Every assertion below is proved symbolically, so no run
manifest is required.

## 1. Corrections required in the candidate

1. **Use the paper's exact auxiliary modulus.** After the paper's preliminary
   removal of \(2\) and of prime powers
   \(\ell\leq\log n\), \(\ell\equiv1\pmod4\), write

   \[
   P=\prod_{\substack{\ell\leq\log n\\\ell\equiv3\pmod4}}\ell,
   \qquad
   M=\frac{nP}{\gcd(n,P)}=\operatorname{lcm}(n,P).
   \]

   The factor \(\gcd(n,P)\) is not cosmetic. For example, \(n=21>20\) has
   \(P=3\): the paper uses \(M=21\), whereas the naive product \(nP=63\) is not
   squarefree. This does not refute the candidate's explicitly balanced branch,
   where both unknown primes eventually exceed \(\log n\) and hence
   \(\gcd(n,P)=1\), but it prevents extending the displayed \(nP\) formula to all
   distinct semiprimes. With the paper's formula, if the reduced \(n\) is
   squarefree then \(M\) is the squarefree union of the prime supports of \(n\)
   and \(P\), and is an odd multiple of \(n\).

2. **Describe the preprocessing accurately.** The paper does not simply remove
   every prime at most \(\log n\). It removes \(2\) and the small primes
   \(1\pmod4\), whose two-square representations have been precomputed. Small
   primes \(3\pmod4\) are instead inserted into \(P\), with the gcd quotient above
   preventing a repeated prime in \(M\).

3. **Restrict the conditional-uniformity wording.** Uniformity holds conditional
   on the accepted residual and on all acceptance/completion randomness whose law
   depends on \((x,y)\) only through that residual (equivalently, one may condition
   on the resulting \(z,w\)). It should not be phrased as conditioning on arbitrary
   later data computed from the full quaternion, such as the final gcd output.

4. **Close only the direct left-handed analogue.** The column/image calculation
   below proves the same exact law for \(\beta\), and a separately computed gcld
   inherits it. It does not imply that the image line of the paper's gcrd output is
   diffuse; that image can be changed by the left cofactor and left normalization.

5. **Do not upgrade marginal uniformity to CRT-component independence.** The row
   lines at the two unknown primes can be coupled through the accepted global
   residual and completion. Equation (10) of the candidate is exact only because
   two *executions* are independent at one fixed local prime. Equation (11) is a
   union bound, not an exact product law. The candidate uses the union bound
   correctly, but the theorem should say this explicitly.

6. **State the normalization side.** A gcrd is unique up to a **left** unit and
   must be left-normalized; this preserves row space. A gcld is unique up to a
   **right** unit and must be right-normalized; this preserves image space.

7. **Quantify the balanced obstruction.** “Polynomially many” means a single
   fixed uniform bound \(K(b)\leq Cb^c\), where
   \(b=\lceil\log_2(n+1)\rceil\) and \(C,c\) do not depend on the unknown factors.
   The exponentially small conclusion holds along an infinite family
   \(p<q<2p\), not uniformly over all unbalanced semiprimes.

The signs in the candidate are correct: the paper uses
\(R=(-x^2-y^2)\bmod M\), constructs \(z^2+w^2=R\) as an integer equality, and
therefore obtains \(M\mid x^2+y^2+z^2+w^2\).

## 2. The primary algorithm has the residual-only interface

Rename the paper's post-preprocessing odd target \(n\), and its auxiliary integer
\(M\) as above. Section 4 performs the following trial.

* It draws \(x,y\) independently and uniformly from \([1,M]\). This is exact
  uniform sampling modulo \(M\), including the zero residue represented by \(M\).
* It takes the least nonnegative residue
  \(R=(-x^2-y^2)\bmod M\), and rejects unless
  \(R\equiv1\pmod4\) and \(\gcd(R,M)=1\).
* It removes from \(R\) all powers of the known small primes
  \(\ell\equiv1\pmod4\), writing \(R=r_1s\). If \(s>1\), it draws an auxiliary
  integer \(u\), performs the stated modular exponentiation, and accepts only
  when it has thereby obtained a square root of \(-1\pmod s\). The lower-bound
  analysis uses prime \(s\), but correctness does not assume that an accepted
  \(s\) is prime.
* From the precomputed Gaussian representations of the factors of \(r_1\), and
  from \(\gcd_{\mathbb Z[i]}(s,a+i)\) for the accepted square root \(a\), it forms
  \(z+wi\) with \(z^2+w^2=r_1s=R\).

Every operation after \(R\) is formed uses only \(R\), precomputed public data,
and fresh randomness. Euclidean-algorithm tie choices may be fixed
deterministically or supplied with fresh randomness; either way they do not use
which preimage \((x,y)\) of \(R\) was drawn. Thus conditioning on acceptance and
completion cannot reweight different \((x,y)\) in the same residual fibre.

Lemma 5 of the paper proves \(\gcd(z,w)=1\), including when the accepted cofactor
\(s\) is composite. Hence \(\gcd(x,y,z,w)=1\). Lemma 2 proves that a greatest
common right divisor of \(n\) and

\[
\beta=x+yi+zj+wk
\]

has reduced norm \(n\). Consequently the paper fits the abstract interface on
every branch on which the reduced target \(n\) is a distinct-prime odd semiprime.
For squarefree \(n\), its \(M=\operatorname{lcm}(n,P)\) is squarefree and is a
multiple of \(n\).

On an infinite balanced family \(n=pq\), \(p<q<2p\), both primes exceed
\(\log n\) for all sufficiently large \(n\). No small factor is removed,
\(\gcd(n,P)=1\), and the candidate's simplified \(M=nP\) happens to be correct on
that branch.

## 3. Conditional CRT uniformity

Let \(M\) be an odd squarefree multiple of \(n=pq\), with \(p\ne q\) odd primes.
Suppose \(x,y\) are initially uniform modulo \(M\), and put

\[
R=-x^2-y^2\pmod M.
\]

Fix a unit residual \(R_0\pmod M\). Before acceptance/completion reweighting, the
conditional law is uniform on

\[
F_{R_0}(M)=
\{(x,y)\in(\mathbb Z/M\mathbb Z)^2:x^2+y^2=-R_0\}.
\]

CRT factors this set as the direct product of its local conics. Therefore, for
each prime \(r\mid n\), projection to the \(r\)-component has a constant number
of lifts and is uniform on

\[
C_{R_0}(r)=
\{(x,y)\in\mathbb F_r^2:x^2+y^2=-R_0\}.
\tag{1}
\]

An acceptance/completion kernel depending on \((x,y)\) only through \(R_0\)
multiplies every point in \(F_{R_0}(M)\) by the same weight. Conditioning further
on a positive-probability completion outcome \(z,w\) consequently leaves (1)
uniform. The unit hypothesis on \(R_0\) makes the conic nonsingular.

For \(c\ne0\), the standard quadratic-character sum gives

\[
\#\{(x,y):x^2+y^2=c\}=r-\chi_r,
\qquad
\chi_r=\left(\frac{-1}{r}\right).
\tag{2}
\]

The bijections below also rederive this count geometrically.

## 4. The split matrix and exact row-line bijection

Choose \(s,t\in\mathbb F_r\) with \(s^2+t^2=-1\), and split the quaternion algebra
by

\[
I=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
J=\begin{pmatrix}s&t\\t&-s\end{pmatrix},
\qquad
K=IJ.
\tag{3}
\]

Then \(I^2=J^2=-1\), \(IJ=-JI\), and \(1,I,J,K\) span
\(M_2(\mathbb F_r)\). Because \(r\) is odd, this also gives the required
splitting of the Hurwitz order modulo \(r\).

Put

\[
A=zs+wt,\qquad B=zt-ws.
\tag{4}
\]

Since \(z^2+w^2=R_0\pmod r\),

\[
A^2+B^2=-(z^2+w^2)=-R_0\ne0.
\tag{5}
\]

The matrix of \(\beta\) is

\[
B_\beta=
\begin{pmatrix}
x+A&y+B\\
-y+B&x-A
\end{pmatrix}.
\tag{6}
\]

Its determinant is \(x^2+y^2+z^2+w^2=0\pmod r\). It is nonzero whenever the
four coordinates are primitive, so it has rank one.

Except at \((x,y)=(-A,-B)\), the row line is \([x+A:y+B]\). To ask whether an
anisotropic line \([u:v]\) occurs, write

\[
(x+A,y+B)=\lambda(u,v).
\]

Substitution in (1) and use of (5) gives

\[
\lambda\bigl(\lambda(u^2+v^2)-2(Au+Bv)\bigr)=0.
\tag{7}
\]

If \(u^2+v^2\ne0\) and \(Au+Bv\ne0\), (7) has exactly one nonzero solution. The
sole anisotropic line with \(Au+Bv=0\) is \([B:-A]\). It is supplied by the
exceptional conic point \((-A,-B)\), where the first row vanishes and the second
row is \(2(B,-A)\). If \(u^2+v^2=0\), then \(Au+Bv\ne0\): otherwise the
anisotropic vector \((A,B)\) would lie in the orthogonal complement of an
isotropic line, which in dimension two is that same isotropic line. Equation (7)
then has no nonzero solution.

Thus the row-line map, with the exceptional point defined by its nonzero second
row, is a bijection

\[
C_{R_0}(r)\longrightarrow
S_r=
\{[u:v]\in\mathbf P^1(\mathbb F_r):u^2+v^2\ne0\}.
\tag{8}
\]

The set \(S_r\) has size \(r-\chi_r\). If \(\chi_r=-1\), it is all of
\(\mathbf P^1(\mathbb F_r)\). If \(\chi_r=1\), its complement consists of exactly
the two eigenlines for the row action \(L\mapsto LI\), i.e. right multiplication
by \(i\).

Combining (1) and (8), conditional on the residual and completion randomness, the
row line of \(\beta\) is exactly uniform on \(S_r\). Since \(S_r\) is independent
of \(R_0,z,w\), mixing over every accepted residual and completion preserves the
same exact marginal law.

## 5. The image-line map is the same bijection

The first column of (6) is

\[
\binom{x+A}{-y+B}.
\]

Set \(X=x+A\) and \(Y=-y+B\). The conic equation becomes

\[
X^2+Y^2=2(AX+BY).
\tag{9}
\]

For a proposed column line \([u:v]\), putting \((X,Y)=\lambda(u,v)\) yields
exactly (7). The exceptional zero-column point is now
\((x,y)=(-A,B)\); its second column is \(2(B,-A)^T\), so it again maps to
\([B:-A]\). The isotropic-line exclusion is identical.

Therefore the image-line map is also a bijection from \(C_{R_0}(r)\) to \(S_r\),
and the image line of \(\beta\) is exactly uniform on \(S_r\). When
\(\chi_r=1\), the omitted lines are the two eigenlines for the column action
\(v\mapsto Iv\), i.e. left multiplication by \(i\).

This calculation rules out the direct gcld/image analogue as an escape. It says
nothing about the image line of the gcrd output after left multiplication and
left-unit normalization.

## 6. Primitive Hurwitz gcd lemma and inherited lines

For completeness, the norm claim need not be assumed as a black box. Let
\(\mathcal H\) be the Hurwitz order, let \(n\) be odd, let
\(\beta=a+bi+cj+dk\) have primitive integer coordinates, and suppose
\(n\mid\operatorname{nrd}(\beta)\). If \(d_R\) is a greatest common right divisor,
then

\[
\mathfrak a=\mathcal Hn+\mathcal H\beta=\mathcal H d_R.
\]

Conjugation gives
\(\overline{\mathfrak a}=n\mathcal H+\bar\beta\mathcal H
=\bar d_R\mathcal H\), and hence

\[
\mathfrak a\overline{\mathfrak a}
=\operatorname{nrd}(d_R)\mathcal H.
\tag{10}
\]

Expanding the left side and using \(n\mid\beta\bar\beta\) shows that it is
contained in \(n\mathcal H\). Thus
\(\mathfrak b=n^{-1}\mathfrak a\overline{\mathfrak a}\) is a two-sided ideal of
\(\mathcal H\). It contains \(n\), all elements \(\bar\beta\varepsilon\), and all
elements \(\eta\beta\). In particular it contains

\[
\begin{aligned}
2a&=\beta+\bar\beta,\\
2b&=(-i)\beta+\bar\beta i,\\
2c&=(-j)\beta+\bar\beta j,\\
2d&=(-k)\beta+\bar\beta k.
\end{aligned}
\]

Primitivity gives \(2\in\mathfrak b\), and oddness gives
\(1\in(n,2)\subset\mathfrak b\). Hence
\(\mathfrak b=\mathcal H\), so (10) equals \(n\mathcal H\) and

\[
\operatorname{nrd}(d_R)=n.
\tag{11}
\]

Conjugating the argument proves the identical norm statement for a greatest
common left divisor \(d_L\).

Now specialize to squarefree \(n=pq\). A gcrd satisfies
\(n=\gamma d_R\) and \(\beta=\delta d_R\). Modulo \(r\in\{p,q\}\), (11) makes
\((d_R)_r\) a nonzero rank-one matrix: zero reduction would force
\(r^2\mid\operatorname{nrd}(d_R)\). Primitivity makes \(\beta_r\ne0\), and its
determinant is zero, so it too has rank one. Left multiplication gives

\[
\operatorname{row}(\beta_r)\subseteq\operatorname{row}((d_R)_r),
\]

and both spaces are nonzero one-dimensional spaces. They are equal. Replacing
\(d_R\) by a left associate to obtain integer coordinates does not change its row
space.

Similarly, \(n=d_L\gamma'\) and \(\beta=d_L\delta'\), so

\[
\operatorname{im}(\beta_r)=\operatorname{im}((d_L)_r).
\]

The gcld is unique up to a right unit; right-unit normalization preserves image
space. Consequently the actual gcrd output has the row law (8), and a separately
computed gcld output has the image law proved in Section 5.

There is no corresponding conclusion here about
\(\operatorname{im}((d_R)_r)\) or \(\operatorname{row}((d_L)_r)\).

## 7. Independent-output collision bounds need no local independence

Let \(D,D'\) be independent gcrd outputs of independent sampler executions. At
one fixed \(r\mid n\), their row lines are independent uniform points of the same
set \(S_r\). Therefore

\[
\Pr(R_r(D)=R_r(D'))=
\frac1{|S_r|}=\frac1{r-\chi_r}.
\tag{12}
\]

No assertion is made about independence of the \(p\)- and \(q\)-lines within one
execution.

If \(g_R\) generates
\(\mathcal HD+\mathcal HD'=\mathcal H g_R\), then modulo \(r\) the two minimal
left ideals agree exactly when the two row lines agree; otherwise their sum is
all of \(M_2(\mathbb F_r)\). Since
\(\operatorname{nrd}(g_R)\mid n\), this proves

\[
r\mid\operatorname{nrd}(g_R)
\quad\Longleftrightarrow\quad
R_r(D)=R_r(D').
\tag{13}
\]

A proper gcd requires exactly one of the two local equalities. Whatever their
dependence,

\[
\Pr(1<\operatorname{nrd}(g_R)<n)
\leq
\frac1{p-\chi_p}+\frac1{q-\chi_q}.
\tag{14}
\]

For \(K\) independent gcrd outputs, every-pair gcrd testing is at most

\[
\binom K2
\left(
\frac1{p-\chi_p}+\frac1{q-\chi_q}
\right).
\tag{15}
\]

The right-ideal/image-line proof gives (12)–(15) for independent **gcld outputs
tested with gcld**, using image lines. If both \(d_R\) and \(d_L\) are separately
computed from each source \(\beta\), unioning the two matched-handed tests only
multiplies the bound by two. This does not cover gcld tests on the \(d_R\)'s,
gcrd tests on the \(d_L\)'s, or mixed \(d_R,d_L\) pairs.

The conclusion also survives testing all twelve projective unit translates of
every pair in the matched handedness. For a fixed \(g\in G\), if \(L,L'\) are
independent uniform points of \(S_r\), then

\[
\Pr(Lg=L')=
\frac{|S_rg\cap S_r|}{|S_r|^2}
\leq\frac1{|S_r|}.
\]

Union over the twelve relative unit classes adds only a factor \(12\) to
(14)–(15). The same statement holds for left-unit translates of separate gcld
outputs in the image/gcld version. This argument does not require \(S_r\) to be
invariant under the unit group.

## 8. Projective Hurwitz units, small characteristics, and stabilizers

The 24 Hurwitz units are

\[
\{\pm1,\pm i,\pm j,\pm k\}
\ \cup\
\left\{
\frac{\pm1\pm i\pm j\pm k}{2}
\right\}.
\]

Their projective quotient

\[
G=\mathcal H^\times/\{\pm1\}\simeq A_4
\]

has three subgroups of order two and four subgroups of order three. For every
odd \(r\), the reduction \(G\to\operatorname{PGL}_2(\mathbb F_r)\) is faithful.
Indeed, projective scalarity would make all three imaginary coordinates vanish
modulo \(r\). An integral noncentral unit has an imaginary coordinate \(\pm1\),
and a half unit has all three imaginary coordinates \(\pm\tfrac12\), none zero
for odd \(r\). Thus only \(\pm1\) reduce to scalars. This includes \(r=3\).

A nonidentity projective matrix fixes at most two rational lines. Counting by
cyclic subgroups rather than by their nonidentity elements gives at most

\[
3\cdot2+4\cdot2=14
\]

lines with nontrivial stabilizer. The two members of an order-three subgroup have
the same fixed lines, including in characteristic \(3\). Hence the candidate's
global count \(14\) is valid.

It can be sharpened. An order-two unit has characteristic polynomial
\(T^2+1\), so it has rational fixed lines exactly when \(\chi_r=1\), two for each
of the three subgroups. A projective order-three half unit has characteristic
polynomial \(T^2\mp T+1\), of discriminant \(-3\). For \(r\ne3\), each of the
four order-three subgroups therefore has two fixed lines exactly when
\(\left(\frac{-3}{r}\right)=1\), and none otherwise. At \(r=3\), each is
non-scalar unipotent and has exactly one fixed line.

Fixed sets belonging to distinct cyclic subgroups do not overlap. Two distinct
order-three subgroups, or an order-two and an order-three subgroup, generate
\(A_4\); a shared line would then be invariant under all of \(G\). This is
impossible because the matrices of \(i\) and \(j\) anticommute and cannot share
an eigenline in odd characteristic. Two distinct involutions cannot share an
eigenline by the same anticommutation argument.

Let \(e_r\) be the number of points of the sampler support \(S_r\) with
nontrivial \(G\)-stabilizer. The exact count is

\[
e_r=
\begin{cases}
4,&r=3,\\
8\,\mathbf 1_{(-3/r)=1},&r\ne3,\ \chi_r=-1,\\
4+8\,\mathbf 1_{(-3/r)=1},&\chi_r=1.
\end{cases}
\tag{16}
\]

In the last line, the sampler deletes exactly the two fixed lines of the
involution represented by \(i\), leaving the four fixed lines of the other two
involutions. Formula (16) proves, and sharpens, the candidate's safe bounds
for a uniform supported line \(L_r\), with
\(H_r=\operatorname{Stab}_G(L_r)\):

\[
\Pr(H_r\ne1)\leq
\begin{cases}
\min(1,14/(r+1)),&\chi_r=-1,\\
\min(1,12/(r-1)),&\chi_r=1.
\end{cases}
\tag{17}
\]

The numerator \(14\) in the first line may be replaced by \(8\). The small cases
do not invalidate anything: at \(r=3\), all four projective lines have
order-three stabilizer; at \(r=5\), all four supported lines have a nontrivial
order-two stabilizer. Thus (17) is sometimes vacuous, but always correct.
Characteristic \(2\) remains excluded.

For a fixed norm-\(n\) gcrd output \(D_R\), write

\[
H_r^{\rm row}(D_R)=
\operatorname{Stab}_G(R_r(D_R)).
\]

If actual Hurwitz units \(U_1,U_2\) are independently uniform, their relative
projective class \(g=[U_1][U_2]^{-1}\) is uniform on \(G\), where brackets
denote the class modulo \(\{\pm1\}\), and

\[
R_r(D_RU_1)=R_r(D_RU_2)
\quad\Longleftrightarrow\quad
g\in H_r^{\rm row}(D_R).
\]

Therefore

\[
\Pr(\text{proper gcrd}\mid D_R)=
\frac{
|H_p^{\rm row}(D_R)\triangle H_q^{\rm row}(D_R)|
}{12}.
\tag{18}
\]

The relative order is important: for the row/right action it is
\(U_1U_2^{-1}\). Enumerating all twelve projective classes succeeds by this
mechanism exactly when
\(H_p^{\rm row}(D_R)\ne H_q^{\rm row}(D_R)\). If the two stabilizers differ, at
least one is nontrivial, so without any local independence

\[
\Pr\!\left(
H_p^{\rm row}(D_R)\ne H_q^{\rm row}(D_R)
\right)
\leq
\frac{e_p}{p-\chi_p}+\frac{e_q}{q-\chi_q}
=O(1/p+1/q).
\tag{19}
\]

For a separately computed gcld output \(D_L\), use image stabilizers and left
units. The relative class is \([U_2]^{-1}[U_1]\) for the column/left action,
still uniform on \(G\), and (18)–(19) are unchanged. This does not apply to
image stabilizers of \(D_R\).

## 9. Bit complexity and balanced-family quantifiers

The paper's Lemmas 3 and 4 supply
\(\Omega(M^2\log\log n/\log n)\) successful \((x,y)\)-trial mass after combining
the number of admissible residuals with the number of preimages of each unit
residual. On the prime-cofactor subfamily used for this lower bound, the fresh
modular-exponentiation trial succeeds with constant probability. Hence one
complete trial succeeds with probability
\(\Omega(\log\log n/\log n)\), independent restarts terminate almost surely, and
the expected number of trials is \(O(\log n/\log\log n)\). Accepted composite
cofactors do not endanger correctness, because the Gaussian and Hurwitz gcd
lemmas apply whenever the tested congruences and primitivity hold.

The paper counts arithmetic operations on integers of size \(n^{O(1)}\) and
obtains expected \(O((\lg n)^2/\lg\lg n)\) such operations for the unconditional
algorithm. Its bit-model footnote permits multiplication by the multiplication
cost \(\mathsf M(\lg n)\). The auxiliary product satisfies \(M=n^{O(1)}\), so all
residues, modular powers, Gaussian products, and quaternion Euclidean remainders
have \(O(\lg n)\) bits up to a fixed constant factor.

Exact draws from \([1,M]\) and from later residual-dependent intervals are
implemented by binary rejection sampling, using \(O(\lg n)\) expected random
bits per trial. This adds only polynomial bit cost. Hurwitz division checks the
two lattice cosets and reduces norm by a fixed factor; a gcd uses
\(O(\lg n)\) divisions. Thus one finder execution, either correctly matched
one-sided gcd, all 24 actual unit multiplications, and all twelve projectively
distinct matched-handed gcd comparisons have expected
\(\operatorname{poly}(\lg n)\) bit cost.

Now let \(b=\lceil\log_2(n+1)\rceil\), and fix constants \(C,c\) with
\(K(b)\leq Cb^c\). On \(p<q<2p\), \(p>\sqrt{n/2}\), so (15) is

\[
O\!\left(\frac{K(b)^2}{\sqrt n}\right)
=O\!\left(b^{2c}2^{-b/2}\right).
\tag{20}
\]

Separately computing and testing both matched handednesses and every unit class
changes only the absolute constant. The single-source survivor bound (19),
unioned over \(K(b)\) outputs, is

\[
O\!\left(\frac{K(b)}{\sqrt n}\right).
\tag{21}
\]

Bertrand's postulate supplies infinitely many distinct prime pairs
\(p<q<2p\), and both primes exceed \(\log(pq)\) eventually. Equations (20)–(21)
therefore give the claimed exponential smallness along an infinite balanced
family with fixed uniform polynomial \(K\). They are not a statement about
semiprimes having a fixed small factor, nor a lower bound on arbitrary factoring
algorithms.

## 10. Strongest corrected theorem

> **Matched-handed residual-fibre obstruction.** Let \(n=pq\), with \(p\ne q\)
> odd primes, and let \(M\) be an odd squarefree multiple of \(n\). Draw \(x,y\)
> exactly uniformly modulo \(M\), put \(R=-x^2-y^2\pmod M\), and use an
> acceptance/completion kernel that depends on \((x,y)\) only through \(R\) and
> fresh randomness. Suppose every accepted residual is a unit modulo \(M\),
> completion returns \(z,w\) with \(z^2+w^2\equiv R\pmod M\), and
> \(\gcd(x,y,z,w)=1\). Put \(\beta=x+yi+zj+wk\).
>
> For each \(r\in\{p,q\}\), conditional on the residual and completion
> randomness, both the row line and the image line of \(\beta\bmod r\) are
> exactly uniform on
>
> \[
> S_r=
> \{[u:v]\in\mathbf P^1(\mathbb F_r):u^2+v^2\ne0\}.
> \]
>
> Thus
> \(|S_r|=r-\left(\frac{-1}{r}\right)\): it is the full projective line when
> \(\left(\frac{-1}{r}\right)=-1\), and otherwise it is the projective line
> with exactly the two \(i\)-eigenlines deleted.
>
> A gcrd of \(n,\beta\), normalized by a left unit, has norm \(n\) and inherits
> the row line. A separately computed gcld, normalized by a right unit, has norm
> \(n\) and inherits the image line. Consequently, for either matched
> handedness, \(K\) independent outputs have every-pair proper-gcd probability
> at most (15); separately testing both matched handednesses and all twelve
> projective unit classes changes this only by an absolute constant. The
> single-source unit-orbit survivor probability is bounded by (19), with exact
> local exceptional counts (16).
>
> The unconditional Pollack–Treviño algorithm satisfies these hypotheses
> whenever its reduced target is a distinct-odd-prime semiprime, because its
> exact auxiliary modulus is
> \(M=nP/\gcd(n,P)=\operatorname{lcm}(n,P)\). Along every infinite balanced
> family \(p<q<2p\), any fixed polynomial number of independent finder calls and
> these direct matched-handed collision or unit-stabilizer tests has
> exponentially small success in the input bit length.

This theorem closes the direct gcrd/row and separately computed gcld/image
collision mechanisms for the named residual-conditioned arithmetic finder. It
does **not** establish independence of the two local components of one output;
cover even inputs, repeated-prime norms, or the ramified prime \(2\); analyze
arbitrary composites with deeper local ideal types; cover a completion that
inspects the particular preimage \((x,y)\); prove image diffusion for a gcrd
output or row diffusion for a gcld output; or rule out mixed-handed tests,
sample-dependent nonlinear combinations, hybrid invariants, or non-collision
quaternion methods. It is a method obstruction, not a factoring algorithm and
not an impossibility theorem for general four-square-based factoring.
