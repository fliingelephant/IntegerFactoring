# Public output/dual metric reconstruction

**Verdict: NOT RECONSTRUCTED for the literal theorem package.**

No computation was used. Most of the proposed negative boundary is correct,
and the exact corrected result is proved below. The literal package has one
decisive algebraic obstruction:

\[
A=(N)
\]

has rational rank \(u=1\), Smith invariant \(\sigma _1=N\), and
\(\gcd(\sigma _1,N)=N\). No proper factor is exposed, but the nonzero Smith
invariant is not coprime to \(N\). Moreover, the requested
\(E_{\rm out}=\mathbb Z\) would imply
\(L_{\rm out}(A,N)=\mathbb Z\), whereas the actual lattice is \(N\mathbb Z\).

The statement becomes true in either of two precise forms:

1. assume \(N\nmid\sigma_i\) for every nonzero Smith invariant; or
2. delete every Smith coordinate divisible by \(N\), and replace rational
   rank \(u\) by the effective modular rank defined below.

A second scope condition is needed for the random-direction claim: the finite
set of public short directions must be fixed independently of the uniformly
random local completion lines. An optimizer allowed to choose its metric or
direction after seeing those lines need not have sparse success.

## 1. CRT and the exact scaled duality

For \(B\in\mathbb Z^{m\times n}\), define

\[
O_r(B)=B\mathbb Z^n+r\mathbb Z^m,\qquad
K_r(B)=\{x\in\mathbb Z^n:Bx\equiv0\pmod r\}.
\]

Thus

\[
L_{\rm out}(A,r)=O_r(A),\qquad
L_{\rm dual}(A,r)=O_r(A^T).
\]

Let \(N=pq\), where \(p\ne q\) are primes. Then

\[
\begin{aligned}
O_N(B)&=O_p(B)\cap O_q(B),\\
O_p(B)+O_q(B)&=\mathbb Z^m,\\
O_N(B)&=qO_p(B)+pO_q(B),                                  \tag{1}\\
\mathbb Z^m/O_N(B)&\cong
 \mathbb Z^m/O_p(B)\times\mathbb Z^m/O_q(B).               \tag{2}
\end{aligned}
\]

The same four identities hold with \(O\) replaced by \(K\) and \(m\) by
\(n\).

For the intersection, if
\(y=Ba+px=Bb+qz\), choose \(c\) coordinatewise with
\(c\equiv a\pmod p\) and \(c\equiv b\pmod q\). Then \(y-Bc\) is divisible
by both primes, hence by \(N\). The reverse containment is immediate. The
sum is all of \(\mathbb Z^m\) because
\(p\mathbb Z^m\subseteq O_p(B)\),
\(q\mathbb Z^m\subseteq O_q(B)\), and \(p,q\) are coprime. Finally,

\[
q(Ba+px)+p(Bb+qz)=B(qa+pb)+N(x+z),
\]

and Bezout proves the reverse containment in the third line of (1). The
kernel proof is identical. Equation (2) is the standard map into the product
of quotients, using the first two lines of (1).

For a full lattice \(\Lambda\), let

\[
\Lambda^*=\{y:\langle y,\Lambda\rangle\subseteq\mathbb Z\}.
\]

The actual scaled-duality identities are

\[
\boxed{N\,O_N(B)^*=K_N(B^T),\qquad O_N(B)=N\,K_N(B^T)^*.}  \tag{3}
\]

Indeed, \(y\in O_N(B)^*\) implies \(Ny=k\in\mathbb Z^m\). Its remaining
integrality condition is

\[
\langle y,Bx\rangle\in\mathbb Z\ \text{for every }x
\quad\Longleftrightarrow\quad B^Tk\equiv0\pmod N.
\]

Taking duals gives the second equality. Hence

\[
\begin{aligned}
N L_{\rm out}(A,N)^*&=K_N(A^T),&
L_{\rm out}(A,N)&=N K_N(A^T)^*,\\
N L_{\rm dual}(A,N)^*&=K_N(A),&
L_{\rm dual}(A,N)&=N K_N(A)^*.                            \tag{4}
\end{aligned}
\]

There is generally no Euclidean-dual identity directly between
\(L_{\rm out}\) and \(L_{\rm dual}\); their ambient dimensions can differ.
Even in dimension one, \(A=(2)\), \(N=6\) gives
\(L_{\rm out}=L_{\rm dual}=2\mathbb Z\), but
\(N(2\mathbb Z)^*=3\mathbb Z\).

## 2. Smith form and the corrected public quotient theorem

Take Smith form

\[
UAV=S=\operatorname{diag}(\sigma_1,\ldots,\sigma_u)
\]

inside a \(t\times d\) rectangle, with
\(U\in{\rm GL}_t(\mathbb Z)\), \(V\in{\rm GL}_d(\mathbb Z)\), and
\(u=\operatorname{rank}_{\mathbb Q}A\). Put
\(\delta_i(r)=\gcd(\sigma_i,r)\). Directly in Smith coordinates,

\[
\begin{aligned}
U L_{\rm out}(A,r)
 &=\bigoplus_{i=1}^u\delta_i(r)\mathbb Ze_i
   \oplus r\mathbb Z^{t-u},\\
V^T L_{\rm dual}(A,r)
 &=\bigoplus_{i=1}^u\delta_i(r)\mathbb Ze_i
   \oplus r\mathbb Z^{d-u}.                               \tag{5}
\end{aligned}
\]

Therefore

\[
\begin{aligned}
[\mathbb Z^t:L_{\rm out}(A,r)]
 &=r^{t-u}\prod_{i=1}^u\delta_i(r),\\
[\mathbb Z^d:L_{\rm dual}(A,r)]
 &=r^{d-u}\prod_{i=1}^u\delta_i(r),                        \tag{6}\\
\det L_{\rm out}(A,N)
 &=N^{t-d}\det L_{\rm dual}(A,N).                          \tag{7}
\end{aligned}
\]

Equation (7) is an index/covolume relation, not an isometry or a Euclidean
duality.

Since \(N=pq\),

\[
\delta_i(N)\in\{1,p,q,N\}.                                \tag{8}
\]

The middle two values expose a proper factor. The last value is a
factor-silent modular-zero coordinate, which is the case omitted by the
literal package.

Assume no proper factor occurs and define

\[
I=\{i\le u:\delta_i(N)=1\},\qquad s=|I|.
\]

Define public primitive sublattices

\[
\begin{aligned}
E_{\rm out}^{\rm eff}
 &=U^{-1}\operatorname{span}_{\mathbb Z}\{e_i:i\in I\}
   \subseteq\mathbb Z^t,\\
E_{\rm dual}^{\rm eff}
 &=V^{-T}\operatorname{span}_{\mathbb Z}\{e_i:i\in I\}
   \subseteq\mathbb Z^d.                                  \tag{9}
\end{aligned}
\]

They are primitive because coordinate direct summands remain primitive under
unimodular maps. If \(i\in I\), then
\(\gcd(\sigma_i,r)=1\) for \(r=p,q,N\). If \(i\notin I\), (8) and the
absence of a proper gcd imply \(N\mid\sigma_i\), so
\(\gcd(\sigma_i,r)=r\). Substitution in (5) proves

\[
\boxed{
\begin{aligned}
L_{\rm out}(A,r)&=E_{\rm out}^{\rm eff}+r\mathbb Z^t,\\
L_{\rm dual}(A,r)&=E_{\rm dual}^{\rm eff}+r\mathbb Z^d,
\qquad r\in\{p,q,N\}.                                     \tag{10}
\end{aligned}}
\]

If one additionally assumes \(N\nmid\sigma_i\) for all \(i\le u\), then
\(I=\{1,\ldots,u\}\), \(s=u\), and these are exactly the requested lattices

\[
E_{\rm out}=U^{-1}(\mathbb Z^u\oplus0),\qquad
E_{\rm dual}=V^{-T}(\mathbb Z^u\oplus0).                   \tag{11}
\]

### Orthogonal projection

Let \(E\subseteq\mathbb Z^m\) be either lattice in (9), of rank \(s\), and
let \(P_E\) project orthogonally onto
\(W=\operatorname{span}_{\mathbb R}(E)^\perp\). Define

\[
\Gamma_E=P_E\mathbb Z^m.
\]

Because \(E\) is rational, \(\Gamma_E\) is a rank-\((m-s)\) lattice in
\(W\). From (10),

\[
\boxed{P_E(E+r\mathbb Z^m)=r\Gamma_E.}                     \tag{12}
\]

Consequently,

\[
\dim(r\Gamma_E)=m-s,\qquad
\operatorname{covol}_W(r\Gamma_E)
=r^{m-s}\operatorname{covol}_W(\Gamma_E).                 \tag{13}
\]

The fixed covolume is also explicit. Let
\(F=W\cap\mathbb Z^m\). For \(w\in W\),
\(\langle w,P_Ez\rangle=\langle w,z\rangle\), so

\[
\Gamma_E^*=F.
\]

If \(B_E\) is an integer basis matrix for primitive \(E\), complementary
minors (or the integral Hodge star of its primitive exterior product) give

\[
\operatorname{covol}(F)=\operatorname{covol}(E)
=\sqrt{\det(B_E^TB_E)}.
\]

Thus

\[
\operatorname{covol}_W(\Gamma_E)
=\frac{1}{\sqrt{\det(B_E^TB_E)}}.                          \tag{14}
\]

The dimension-zero covolume convention is \(1\). Equations (12)--(14) show
that the local quotient shape is fixed and public; only scalar multiplication
by \(r\) changes.

## 3. Fixed-completion batch and the cyclic slice

Let

\[
\beta_i=(x_i,y_i,z,w)^T\in\mathbb Z^4,\qquad 1\le i\le M,
\]

where \(z,w\) are fixed over the batch. The natural public linear output map
modulo \(r\) is

\[
b_r:(\mathbb Z/r)^M\longrightarrow(\mathbb Z/r)^4,\qquad
c\longmapsto\sum_i c_i\beta_i.                             \tag{15}
\]

Write

\[
T=\begin{pmatrix}
x_1&\cdots&x_M\\
y_1&\cdots&y_M\\
1&\cdots&1
\end{pmatrix},
\qquad
P=\begin{pmatrix}
1&0&0\\
0&1&0\\
0&0&z\\
0&0&w
\end{pmatrix}.
\]

The output-column matrix is \(B=PT\). The map
\(T:(\mathbb Z/N)^M\to(\mathbb Z/N)^3\) is surjective iff

\[
\gcd\!\left(N,\text{ all }3\times3\text{ minors of }T\right)=1.             \tag{16}
\]

Indeed, CRT reduces surjectivity to row rank three over both
\(\mathbb F_p\) and \(\mathbb F_q\). Over each field that is equivalent to
some maximal minor being nonzero, which is precisely (16). If \(M<3\), all
maximal minors are taken as zero, and surjectivity fails.

Surjectivity means \(T\mathbb Z^M+N\mathbb Z^3=\mathbb Z^3\). Applying the
integer map \(P\) in both directions gives

\[
\begin{aligned}
B\mathbb Z^M+N\mathbb Z^4
 &=P\mathbb Z^3+N\mathbb Z^4\\
 &=\mathbb Z^2\oplus
 \bigl((z,w)\mathbb Z+N\mathbb Z^2\bigr).                 \tag{17}
\end{aligned}
\]

Hence the only nontrivial output slice is

\[
O_C=C\mathbb Z+N\mathbb Z^2,\qquad C=(z,w)^T.              \tag{18}
\]

Assume \(C\ne0\), and set

\[
g=\gcd(|z|,|w|)>0,\qquad h=\gcd(g,N),\qquad C_0=C/g.
\]

The vector \(C_0\) is primitive. Extended Bezout gives
\(D\in\mathbb Z^2\) with

\[
\det(C_0,D)=1.                                             \tag{19}
\]

Thus \((C_0,D)\) is a unimodular basis. Since
\(g\mathbb Z+N\mathbb Z=h\mathbb Z\),

\[
\boxed{O_C=h\mathbb ZC_0+N\mathbb ZD.}                    \tag{20}
\]

Define the congruence kernel

\[
L_C=\{v\in\mathbb Z^2:wv_1-zv_2\equiv0\pmod N\}.           \tag{21}
\]

Writing \(v=aC_0+bD\), equation (19) gives

\[
wv_1-zv_2=-g\det(C_0,v)=-gb.
\]

Writing \(g=hg'\), \(N=hN'\) with \(\gcd(g',N')=1\) shows that
\(N\mid gb\) iff \(N/h\mid b\). Therefore

\[
\boxed{L_C=\mathbb ZC_0+(N/h)\mathbb ZD.}                 \tag{22}
\]

All determinant, equality, and scalar relations are now immediate:

\[
\det L_C=N/h,\qquad
\det O_C=Nh,\qquad
O_C=hL_C,\qquad
O_C=L_C\Longleftrightarrow h=1.                           \tag{23}
\]

Also

\[
\mathbb Z^2/O_C\cong
\mathbb Z/h\mathbb Z\oplus\mathbb Z/N\mathbb Z.           \tag{24}
\]

In particular, \(\gcd(N,z,w)=1\) is exactly \(h=1\), and then the quotient
is cyclic of order \(N\).

Let \(R(x_1,x_2)=(-x_2,x_1)\). For an oriented rank-two lattice \(\Lambda\)
of determinant \(\Delta\), a direct inverse-transpose calculation gives

\[
\Lambda^*=\frac1\Delta R\Lambda.
\]

Using (23),

\[
\boxed{
L_C^*=\frac1NRO_C,\qquad
O_C^*=\frac1NRL_C,
}
\quad\text{or equivalently}\quad
\boxed{NL_C^*=RO_C,\qquad NO_C^*=RL_C.}                   \tag{25}
\]

If \(C=0\), then \(O_C=N\mathbb Z^2\) and \(L_C=\mathbb Z^2\);
\(C_0\) is undefined. This edge case is excluded by
\(\gcd(N,z,w)=1\).

## 4. Primitive branch \(h=1\)

For \(r=p,q,N\), put

\[
O_C(r)=C\mathbb Z+r\mathbb Z^2,\qquad
L_C(r)=\{v:wv_1-zv_2\equiv0\pmod r\}.
\]

Since \(g\) is invertible modulo all three \(r\),

\[
\boxed{O_C(r)=L_C(r)=\mathbb ZC_0+r\mathbb ZD.}            \tag{26}
\]

For arbitrary \(u=\alpha C_0+\beta D\), this is the exact local membership
criterion

\[
u\in O_C(r)=L_C(r)\quad\Longleftrightarrow\quad r\mid\beta.                \tag{27}
\]

Now let

\[
v=aC_0+NbD\in L_C(N).
\]

Unimodularity of \((C_0,D)\) gives

\[
\begin{array}{lll}
p\mid a&\Longleftrightarrow v\in p\mathbb Z^2
       &\Longleftrightarrow v\in pO_C(q),\\
q\mid a&\Longleftrightarrow v\in q\mathbb Z^2
       &\Longleftrightarrow v\in qO_C(p),\\
N\mid a&\Longleftrightarrow v\in N\mathbb Z^2.             \tag{28}
\end{array}
\]

The same unimodular change preserves the ideal generated by vector
coordinates, so

\[
\boxed{\gcd(N,v_1,v_2)=\gcd(N,a,Nb)=\gcd(N,a).}            \tag{29}
\]

If \(\|C_0\|^2<N\), the shortest nonzero vectors of \(L_C\) are exactly
\(\pm C_0\). Indeed, when \(b=0\), the shortest nonzero multiples are
\(\pm C_0\). When \(b\ne0\),

\[
N|b|=|\det(C_0,v)|
\le\|C_0\|\,\|v\|,
\]

and hence

\[
\|v\|\ge\frac{N}{\|C_0\|}>\|C_0\|.
\]

The strict hypothesis matters; equality can produce ties.

For the orthogonal quotient, choose the unit coordinate

\[
\nu=RC_0/\|C_0\|
\]

on \(C_0^\perp\). Equation (19) yields
\(\langle D,\nu\rangle=1/\|C_0\|\). Projection kills the
\(C_0\)-coefficient, so

\[
\boxed{\langle P_{C_0^\perp}L_C,\nu\rangle
=\frac{N}{\|C_0\|}\mathbb Z.}                             \tag{30}
\]

Finally, \(h=1\) gives \(O_C=L_C\), and (25) becomes

\[
\boxed{NL_C^*=RL_C.}                                      \tag{31}
\]

Thus the two-dimensional scaled dual is only a quarter-turn of the same
public lattice.

## 5. Uniform targets and uniform local lines

### Uniform discrete CVP target

Let a target \(\tau\) be uniform in
\(\mathbb Z^2/N\mathbb Z^2\). Its CRT reductions
\(\tau_p,\tau_q\) are independent and uniform. The local output line
\(\ell_r=\mathbb F_r\overline{C_0}\) has \(r\) elements in
\(\mathbb F_r^2\), including zero, so

\[
\Pr(\tau_r\in\ell_r)=1/r.
\]

Consequently, exact membership at one and only one local factor has
probability

\[
\boxed{
\frac1p\left(1-\frac1q\right)
+\frac1q\left(1-\frac1p\right)
=\frac1p+\frac1q-\frac2N.}                                \tag{32}
\]

This exact formula is for a uniform discrete residue target. Continuous or
biased targets are different models.

### Primitive shortest-direction lemma

Let \(Q\) be a fixed positive-definite rational quadratic form on
\(\mathbb Z^2\), independent of the local completion lines. Define the
finite unoriented primitive shortest-direction set explicitly by

\[
\mathscr S_Q=
\left\{
\{v,-v\}:0\ne v\in\mathbb Z^2,
Q(v)=\min_{0\ne x\in\mathbb Z^2}Q(x)
\right\}.                                                  \tag{33}
\]

Every minimizer is primitive, since \(v=kw\), \(|k|>1\), would imply
\(Q(w)<Q(v)\). Moreover,

\[
|\mathscr S_Q|\le3.                                       \tag{34}
\]

To prove (34), apply a real linear map making \(Q\) Euclidean. Distinct
shortest vectors, with signs chosen so their angle lies in
\([0,\pi/2]\), must be separated by at least \(\pi/3\); otherwise their
difference is shorter. At most three unoriented directions with that
separation fit in a half-circle. This includes all hexagonal-lattice ties.

Now take distinct odd primes \(p,q\), and choose independently

\[
\ell_p\sim{\rm Unif}\bigl(\mathbb P^1(\mathbb F_p)\bigr),
\qquad
\ell_q\sim{\rm Unif}\bigl(\mathbb P^1(\mathbb F_q)\bigr).
\]

For \([v]\in\mathscr S_Q\), define the possible direct/dual hits

\[
H_r(v)=
\{\mathbb F_r\bar v,\ \mathbb F_r\overline{Rv}\}
\subseteq\mathbb P^1(\mathbb F_r),\qquad r=p,q.            \tag{35}
\]

Zero reductions cause no ambiguity: primitive \(v\) and \(Rv\) are nonzero
modulo every prime. If a nonprimitive candidate is first produced, divide by
its content. A proper gcd between that content and \(N\) is already a factor
revelation, not a directional event.

Let \(k_r(v)=|H_r(v)|\in\{1,2\}\). The value is one exactly for an isotropic
direction:

\[
\mathbb F_r\bar v=\mathbb F_r\overline{Rv}
\quad\Longleftrightarrow\quad
v_1^2+v_2^2\equiv0\pmod r.                                \tag{36}
\]

Distinct integer directions can also collide after reduction. Treating
(35) as a set counts every isotropic or inter-direction collision once and
can only reduce the probability.

For a fixed direction, let \(E_v\) be the event that a direct or rotated hit
occurs at exactly one local prime. Since
\(|\mathbb P^1(\mathbb F_r)|=r+1\), independence gives

\[
\Pr(E_v)=
\alpha_p(v)+\alpha_q(v)-2\alpha_p(v)\alpha_q(v),
\qquad
\alpha_r(v)=\frac{k_r(v)}{r+1}.                            \tag{37}
\]

Taking the union over every tied shortest direction and using (34),

\[
\boxed{
\Pr\bigl(\exists[v]\in\mathscr S_Q:E_v\bigr)
\le
\min\!\left\{1,\frac6{p+1}+\frac6{q+1}\right\}
\le6\left(\frac1p+\frac1q\right).}                         \tag{38}
\]

This handles zero reductions, isotropic directions, collisions, all ties,
and small-prime constants. If rotated dual directions are excluded, replace
\(6\) by \(3\). For one fixed direct direction, the exact probability is

\[
\frac1{p+1}+\frac1{q+1}
-\frac2{(p+1)(q+1)}.
\]

Independence is essential. After observing \(\ell_p\), one can choose a
primitive lift \(v\) of that line and then a positive-definite form for which
\(\pm v\) are the unique shortest vectors. The hit at \(p\) then has
probability one, not \(O(1/p)\). Thus (38) does not analyze an adaptive
optimizer on a full coupled lattice whose metric depends on the completion
lines.

## 6. Bit complexity and edge cases

For an integer \(a\), let

\[
\operatorname{bl}(a)=1+\lceil\log_2(1+|a|)\rceil,
\]

and let \(\mathcal L\) be the full binary encoding length of \(N\), all
dimensions and matrix entries, and all batch entries. Every public
construction above is deterministic in \(\mathcal L^{O(1)}\) bit operations:

- Deterministic Smith-form algorithms compute \(S,U,V\) with
  polynomial-bit intermediate and output integers. The \(u\) gcds with \(N\)
  are extended-Euclid computations; each alleged factor is checked by
  \(1<\delta_i(N)<N\).
- Bases in (9) are selected columns of \(U^{-1}\) and \(V^{-T}\). For a
  basis \(B_E\), the exact rational projector is
  \[
  P_E=I-B_E(B_E^TB_E)^{-1}B_E^T.
  \]
  Fraction-free determinant/inversion and Hermite or Smith reduction construct
  \(\Gamma_E\), its dimension, and its squared covolume with polynomial bit
  lengths. No floating-point orthogonalization is needed.
- Condition (16) can be checked using the
  \(\binom M3=O(M^3)\) maximal minors, reducing each modulo \(N\) before the
  running gcd, or by Smith form of \(T\). Computing \(g,h,C_0,D\) takes two
  extended-gcd calculations.
- Membership, determinant, norm, and rotation identities use exact
  integer/rational arithmetic. In dimension two, exact Gauss reduction finds
  (33) and all ties in polynomial bit complexity.

These bounds are polynomial in binary input length, never in the numerical
value \(N\). The proof uses \(p,q\) only for analysis; it does not assume
that an algorithm knows them.

All algebraic sections allow \(p=2\); only the projective/isotropic counting
lemma assumes odd primes. Rank zero and zero-dimensional complements use
empty bases and covolume one. Formulas involving \(C_0\) require \(C\ne0\);
the zero case was given separately. The condition \(\gcd(N,z,w)=1\) forces
\(h=1\). All metric statements use the ordinary Euclidean inner product.

## 7. Exact negative boundary

After correcting the Smith-rank issue, the no-proper-factor branch has only
the public primitive summands (9) and the scalar quotient families (12).
Their dimensions are \(t-s\) and \(d-s\), their covolumes scale exactly as
\(r^{t-s}\) and \(r^{d-s}\), and their normalized shapes contain no local
directional information.

For a fixed-completion batch satisfying (16) and
\(\gcd(N,z,w)=1\), the nontrivial output quotient is the single cyclic slice
\(O_C=L_C\). Its shortest direction is the public line
\(\mathbb RC_0\) under the stated length condition; its orthogonal quotient
is the one-dimensional lattice \(N\mathbb Z/\|C_0\|\); and its scaled
two-dimensional dual is merely a rotation. Uniform lucky target membership
has exact probability (32), while a fixed independent family of public
shortest directions has the sparse bound (38).

This is a negative boundary, not a factoring algorithm. Biased completions,
biased targets, and an optimizer on the full nonorthogonally coupled lattice
whose output coordinates may reveal a factor remain open. Nonlinear
constructions also remain open.
