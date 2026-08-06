# Public-output and dual-metric reconstruction

**Status: RECONSTRUCTED**

This note works only from the theorem package in the task.  All lattices are
full lattices in their stated ambient real vector spaces unless a projection
is explicitly taken.  For a lattice (L),

\[
L^*=\{x:\langle x,L\rangle\subseteq\mathbb Z\}
\]

is its Euclidean dual, and `covol` means Euclidean covolume in the real span.
The covolume of the zero lattice in the zero vector space is (1).

## 1. CRT, local cosets, uniform targets, and Euclidean duality

Let (N=pq), where (p\ne q) are primes, and let
(A\in\mathbb Z^{t\times d}).  Put

\[
\Lambda_{\rm out}(A,r)=A\mathbb Z^d+r\mathbb Z^t,
\qquad
\Lambda_{\rm dual}(A,r)=r\mathbb Z^d+A^T\mathbb Z^t
=\Lambda_{\rm out}(A^T,r).
\]

For (r=p,q,N), reduction modulo (r) identifies

\[
\Lambda_{\rm out}(A,r)/r\mathbb Z^t
=\operatorname{im}(A\bmod r).
\]

Consequently,

\[
\begin{aligned}
\Lambda_{\rm out}(A,N)
 &=\Lambda_{\rm out}(A,p)\cap\Lambda_{\rm out}(A,q),\\
\Lambda_{\rm out}(A,p)+\Lambda_{\rm out}(A,q)&=\mathbb Z^t.
\end{aligned} \tag{1.1}
\]

Indeed, membership in both local lattices gives coefficients modulo (p)
and modulo (q); coordinatewise CRT combines those coefficients modulo
(N).  The reverse inclusion is immediate.  The sum is all of
(\mathbb Z^t), since it contains
(p\mathbb Z^t+q\mathbb Z^t=\mathbb Z^t).
Applying the same proof to (A^T) gives

\[
\begin{aligned}
\Lambda_{\rm dual}(A,N)
 &=\Lambda_{\rm dual}(A,p)\cap\Lambda_{\rm dual}(A,q),\\
\Lambda_{\rm dual}(A,p)+\Lambda_{\rm dual}(A,q)&=\mathbb Z^d.
\end{aligned} \tag{1.2}
\]

Thus the natural quotient map is an exact CRT decomposition:

\[
\mathbb Z^t/\Lambda_{\rm out}(A,N)
\simeq
\mathbb Z^t/\Lambda_{\rm out}(A,p)
\times
\mathbb Z^t/\Lambda_{\rm out}(A,q), \tag{1.3}
\]

and likewise on the dual side.  In particular, arbitrary local cosets have
a common point, and their intersection is one coset of the public
(N)-lattice.

This also records the relevant invariance.  If
(\lambda\in\Lambda_{\rm out}(A,N)), then for (r=p,q,N)

\[
x-\lambda+\Lambda_{\rm out}(A,r)
=x+\Lambda_{\rm out}(A,r). \tag{1.4}
\]

Hence subtracting any public-lattice vector, including any chosen closest
one, cannot change either local coset or the predicate that the residual
belongs to exactly one local lattice.  The same statement holds for
(\Lambda_{\rm dual}).

Let

\[
\rho_r=\operatorname{rank}_{\mathbb F_r}(A\bmod r),
\qquad r=p,q.
\]

For (X) uniform modulo (N\mathbb Z^t), its reductions modulo (p) and
(q) are independent and uniform.  Therefore

\[
\Pr[X\in\Lambda_{\rm out}(A,r)]=r^{\rho_r-t}
\]

and the exact probability of membership in exactly one local output lattice
is

\[
p^{\rho_p-t}+q^{\rho_q-t}
-2p^{\rho_p-t}q^{\rho_q-t}. \tag{1.5}
\]

Since (A) and (A^T) have the same rank over every field, the corresponding
dual probability is

\[
p^{\rho_p-d}+q^{\rho_q-d}
-2p^{\rho_p-d}q^{\rho_q-d}. \tag{1.6}
\]

Equivalently one may choose a uniform class in the relevant quotient in
(1.3); the same counts result.

For an integer matrix (B), define its congruence-kernel lattice by

\[
K_N(B)=\{x\in\mathbb Z^{\operatorname{cols}(B)}:Bx\equiv0\pmod N\}.
\]

The two scaled Euclidean-duality identities are

\[
N\Lambda_{\rm out}(A,N)^*=K_N(A^T),
\qquad
N\Lambda_{\rm dual}(A,N)^*=K_N(A). \tag{1.7}
\]

For example, (x\in\Lambda_{\rm out}(A,N)^*) implies
(y=Nx\in\mathbb Z^t), and integrality of
(\langle x,Az\rangle) for every (z\in\mathbb Z^d) is exactly
(A^Ty\equiv0\pmod N).  This is reversible.  Taking Euclidean duals also
gives the reciprocal forms

\[
N K_N(A^T)^*=\Lambda_{\rm out}(A,N),
\qquad
N K_N(A)^*=\Lambda_{\rm dual}(A,N). \tag{1.8}
\]

## 2. Smith branch and exact projected metrics

Take an integer Smith form

\[
UAV=S,
\qquad U\in{\rm GL}_t(\mathbb Z),\quad
V\in{\rm GL}_d(\mathbb Z),
\]

whose nonzero diagonal entries satisfy
(\sigma_1\mid\sigma_2\mid\cdots\mid\sigma_s).  Put
(\delta_i=\gcd(\sigma_i,N)).  If
(1<\delta_i<N), then (\delta_i) is immediately one of (p,q), so this
branch exposes a factor.

Suppose from now on that no such (\delta_i) occurs.  Then each
(\delta_i\in\{1,N\}).  Divisibility of the Smith entries implies
(\delta_i\mid\delta_{i+1}), so there is an integer (u),
(0\le u\le s), for which

\[
\delta_1=\cdots=\delta_u=1,
\qquad
\delta_{u+1}=\cdots=\delta_s=N. \tag{2.1}
\]

Thus every nonzero (\sigma_i) in the second block is divisible by (N).
There is no conclusion that (\sigma_i/N) is coprime to (N); it may have
additional factors (p) or (q).

Because unimodular matrices preserve integer coordinate lattices, for every
(r\in\{p,q,N\}),

\[
\begin{aligned}
U\Lambda_{\rm out}(A,r)
 &=S\mathbb Z^d+r\mathbb Z^t
  =\mathbb Z^u\oplus r\mathbb Z^{t-u},\\
V^T\Lambda_{\rm dual}(A,r)
 &=S^T\mathbb Z^t+r\mathbb Z^d
  =\mathbb Z^u\oplus r\mathbb Z^{d-u}.
\end{aligned} \tag{2.2}
\]

The first (u) coordinates are full because
(\gcd(\sigma_i,r)=1); all later nonzero Smith entries, as well as all zero
diagonal positions, contribute only (r\mathbb Z).  Define the primitive
direct summands

\[
E_{\rm out}=U^{-1}(\mathbb Z^u\oplus0)\subseteq\mathbb Z^t,
\qquad
E_{\rm dual}=V^{-T}(\mathbb Z^u\oplus0)\subseteq\mathbb Z^d. \tag{2.3}
\]

Then

\[
\boxed{
\Lambda_{\rm out}(A,r)=E_{\rm out}+r\mathbb Z^t,
\qquad
\Lambda_{\rm dual}(A,r)=E_{\rm dual}+r\mathbb Z^d.} \tag{2.4}
\]

Here “primitive” is literal: the displayed sublattices are images of a
coordinate direct summand under a unimodular map.

There is an exact metric statement after orthogonally removing these common
directions.  The following argument covers both sides.  Let
(E\subseteq\mathbb Z^n) be either primitive rank-(u) summand, let
(W=\operatorname{span}_{\mathbb R}E), and let
(\pi_E:\mathbb R^n\to W^\perp) be orthogonal projection.  Define the one
public projected ambient lattice

\[
P_E=\pi_E(\mathbb Z^n).
\]

Then, exactly and for every (r=p,q,N),

\[
\pi_E(E+r\mathbb Z^n)=rP_E. \tag{2.5}
\]

To see directly that (P_E) is a lattice and to compute its metric, write a
unimodular completion as (Q=[B\ C]), where the columns of (B) form a
basis of (E).  On the output side take (Q=U^{-1}), and on the dual side
take (Q=V^{-T}).  Then the (n-u) columns of (\pi_E C) are a basis of
(P_E): a relation among them would put an integer combination of the
columns of (C) in (E), impossible in the direct sum defined by (Q).
The Schur-complement identity applied to (Q^TQ), whose determinant is one,
gives

\[
\det(B^TB)\,
\det\!\left(C^T\pi_E C\right)=1.
\]

Consequently

\[
\begin{array}{c|c|c}
 & \dim P_E & \operatorname{covol}(rP_E)\\ \hline
\text{output} &t-u&r^{t-u}/\operatorname{covol}(E_{\rm out})\\
\text{dual}   &d-u&r^{d-u}/\operatorname{covol}(E_{\rm dual}).
\end{array} \tag{2.6}
\]

All boundary cases are included.  If (u=0), then (E=0),
(P_E=\mathbb Z^n), and (2.5) is just (r\mathbb Z^n).  If (u=n), then
primitivity forces (E=\mathbb Z^n), the quotient and (P_E) have rank
zero, and every projection is (0) with covolume (1).  If the ambient
rank itself is zero, both conventions agree.  It is possible that only one
of the output and dual quotients has rank zero when (t\ne d).

These objects have polynomial-bit exact constructions.  Polynomial-time
Smith/Hermite algorithms compute (U,V,S) with polynomial-size integer
data.  The projector is

\[
\pi_E=I-B(B^TB)^{-1}B^T
\]

(with the evident empty-matrix conventions), and (\pi_EC) is an explicit
rational basis.  Determinant bounds show that its numerators and
denominators have polynomial bit length; exact rational linear algebra
suffices.  This proves a theorem only for the orthogonal projections in
(2.5).  A nonorthogonal unimodular Smith transformation is not an isometry,
so (2.2) does **not** imply an SVP or CVP theorem for the original full
lattices.

## 3. A fixed-completion batch

Let

\[
\beta_i=(x_i,y_i,z,w)^T\in\mathbb Z^4,
\qquad 1\le i\le m,
\]

with the same completion (C=(z,w)^T) for every column.  Put

\[
T=\begin{pmatrix}
x_1&\cdots&x_m\\
y_1&\cdots&y_m\\
1&\cdots&1
\end{pmatrix},
\qquad
F_C(a,b,c)=(a,b,zc,wc).
\]

The public output map and lattice are

\[
\Phi:\mathbb Z^m\oplus\mathbb Z^4\longrightarrow\mathbb Z^4,
\qquad
\Phi(k,n)=\sum_i k_i\beta_i+Nn,
\qquad
\mathcal O=\operatorname{im}\Phi. \tag{3.1}
\]

Modulo (N), this is exactly

\[
\bar k\longmapsto F_C(T\bar k). \tag{3.2}
\]

Let (\Delta_3(T)) be the nonnegative gcd of all (3\times3) minors of
(T), with (\Delta_3(T)=0) when there are no such minors.  The following
are equivalent:

\[
T:(\mathbb Z/N)^m\twoheadrightarrow(\mathbb Z/N)^3,
\qquad
\gcd(N,\Delta_3(T))=1. \tag{3.3}
\]

Indeed, surjectivity is equivalent to rank three modulo both (p) and
(q), which is equivalent to some maximal minor being nonzero modulo each
prime.  The two witnessing minors need not be the same; the gcd criterion
is precisely what combines them.

Under (3.3), (3.2) ranges over every (F_C(a,b,c)), so

\[
\boxed{
\mathcal O=\mathbb Z^2\oplus O_C,
\qquad O_C=C\mathbb Z+N\mathbb Z^2.} \tag{3.4}
\]

If additionally (s_C=\gcd(N,z,w)=1), the cyclic subgroup generated by
(C\bmod N) has order (N), hence
([\mathbb Z^2:O_C]=N).

The failure branches are exact:

* If (d_T=\gcd(N,\Delta_3(T))) is (p) or (q), that gcd itself exposes a
  proper factor.  If (d_T=N), maximal rank fails modulo both primes.  In
  either case the exact residue image is (F_C(\operatorname{im}T)), and
  the direct split (3.4) is not justified (though it may occur accidentally
  in a special input).
* If (3.3) holds but (s_C>1), the split (3.4) still holds algebraically,
  but its intended nonsingular cyclic tail does not.  In fact
  ([\mathbb Z^2:O_C]=Ns_C).  If (s_C=p) or (q), that gcd exposes a
  factor; if (s_C=N), then (C\equiv0\pmod N) and (O_C=N\mathbb Z^2).
* If both hypotheses fail, only (3.1)-(3.2), not either simplification, is
  available.

## 4. The two tail lattices and their exact duality

Assume first (C=(z,w)\ne0).  Set

\[
g=\gcd(z,w)>0,
\qquad h=\gcd(g,N),
\qquad C_0=C/g.
\]

The vector (C_0) is primitive, so choose (D\in\mathbb Z^2) with
(det(C_0,D)=1).  Define

\[
L_C=\{v\in\mathbb Z^2:w v_1-z v_2\equiv0\pmod N\}.
\]

Writing (v=aC_0+bD), one has

\[
w v_1-z v_2=\det(v,C)=-gb.
\]

Writing (g=hg'), (N=hN'), with (\gcd(g',N')=1), shows that
(N\mid gb) exactly when (N/h\mid b).  Meanwhile the first coordinate
ideal of (g\mathbb ZC_0+N\mathbb Z^2), in the unimodular basis
((C_0,D)), is (g\mathbb Z+N\mathbb Z=h\mathbb Z).  Hence

\[
\boxed{
L_C=\mathbb ZC_0+\frac Nh\mathbb ZD,
\qquad
O_C=h\mathbb ZC_0+N\mathbb ZD.} \tag{4.1}
\]

It follows that

\[
\det L_C=N/h,
\qquad
\det O_C=Nh,
\qquad
O_C\subseteq L_C,
\qquad
O_C=L_C\Longleftrightarrow h=1. \tag{4.2}
\]

For every (r\in\{p,q,N\}), put (h_r=\gcd(g,r)) and define the analogous
local lattices by replacing the congruence modulus and the public modulus by
(r).  The same proof gives

\[
L_C(r)=\mathbb ZC_0+\frac r{h_r}\mathbb ZD,
\qquad
O_C(r)=h_r\mathbb ZC_0+r\mathbb ZD, \tag{4.3}
\]

with determinants (r/h_r) and (rh_r), and equality exactly when
(h_r=1).

Thus all singular branches are visible.  If (h=p), then globally
(L_C=\mathbb ZC_0+q\mathbb ZD) and
(O_C=p\mathbb ZC_0+N\mathbb ZD); locally at (p),
(L_C(p)=\mathbb Z^2) and (O_C(p)=p\mathbb Z^2), while the (q)-local
lattices agree.  The case (h=q) is symmetric.  If (h=N), then
(L_C=\mathbb Z^2) and (O_C=N\mathbb Z^2).  Cases with exactly one of
(z,w) equal to zero require no exception: (4.1) still applies.

If (C=0), no (C_0) is defined and this case must be stated separately:

\[
L_0=\mathbb Z^2,
\qquad O_0=N\mathbb Z^2,
\qquad
L_0(r)=\mathbb Z^2,
\qquad O_0(r)=r\mathbb Z^2. \tag{4.4}
\]

Let (R(x_1,x_2)=(-x_2,x_1)).  For any rank-two lattice (M) of
covolume (\Delta), the adjugate formula for a basis gives

\[
\Delta M^*=R(M). \tag{4.5}
\]

Since ((1/h)O_C=L_C), (hL_C=O_C), and the two determinants in (4.2)
are (Nh) and (N/h), respectively, (4.5) yields the cross-duality
identities

\[
\boxed{
N O_C^*=R(L_C),
\qquad
N L_C^*=R(O_C).} \tag{4.6}
\]

They remain true for (C=0) by direct substitution in (4.4), and locally
one has (rO_C(r)^*=R(L_C(r))) and
(rL_C(r)^*=R(O_C(r))).

## 5. The nonsingular line, coordinate slices, shortest vectors, and quotient

Now assume (h=1).  Then for all (r=p,q,N),

\[
L_C(r)=O_C(r)=\mathbb ZC_0+r\mathbb ZD. \tag{5.1}
\]

For an arbitrary (x=\alpha C_0+\beta D\), local output-line membership is
the exact divisibility test

\[
x\in L_C(r)\Longleftrightarrow r\mid\beta. \tag{5.2}
\]

Every public (N)-lattice vector has a unique expression

\[
v=aC_0+NbD. \tag{5.3}
\]

Because ((C_0,D)) is a unimodular integer basis, it preserves the ideal
generated by the coordinates.  Therefore

\[
\boxed{\gcd(N,v_1,v_2)=\gcd(N,a).} \tag{5.4}
\]

Let (r,s\in\{p,q\}) with (rs=N).  On the (r)-divisible coordinate
slice, (5.4) says (r\mid a), and

\[
\frac vr=\frac ar C_0+s bD.
\]

This divided vector is automatically on the (s)-local output line, while
the nontrivial same-(r) test is

\[
\boxed{v/r\in L_C(r)\Longleftrightarrow r\mid b.} \tag{5.5}
\]

Here one uses (\gcd(r,s)=1) in (5.2).  The exact slice identities are

\[
\begin{aligned}
L_C(N)\cap r\mathbb Z^2&=rL_C(s),\\
\{v\in L_C(N)\cap r\mathbb Z^2:v/r\in L_C(r)\}&=rL_C(N),\\
L_C(N)\cap N\mathbb Z^2&=N\mathbb Z^2,\\
\{v\in L_C(N):\gcd(N,v_1,v_2)=r\}
 &=r\bigl(L_C(s)\setminus s\mathbb Z^2\bigr).
\end{aligned} \tag{5.6}
\]

These formulas distinguish ordinary local membership (automatic for the
original (v\in L_C(N))) from the (r\mid b) test after division.

Suppose now that

\[
\|C_0\|^2<N. \tag{5.7}
\]

If (v=aC_0+NbD\ne0) has (b=0), then
(\|v\|=|a|\|C_0\|), with equality to (\|C_0\|) only for
(v=\pm C_0).  If (b\ne0), its component perpendicular to (C_0) has
length

\[
\frac{|\det(C_0,v)|}{\|C_0\|}
=\frac{N|b|}{\|C_0\|}
>\|C_0\|.
\]

Thus the complete shortest-vector set is exactly

\[
\operatorname{Short}(L_C)=\{C_0,-C_0\}. \tag{5.8}
\]

For the exact orthogonal quotient, identify (C_0^\perp) with
(\mathbb R) using the signed coordinate

\[
\psi(x)=\frac{\det(C_0,x)}{\|C_0\|}.
\]

Primitivity gives (\psi(\mathbb Z^2)=\|C_0\|^{-1}\mathbb Z), and (5.1)
gives

\[
\boxed{
\psi(L_C(N))=\frac N{\|C_0\|}\mathbb Z,
\qquad
\psi(L_C(r))=\frac r{\|C_0\|}\mathbb Z.} \tag{5.9}
\]

Finally, (4.6) becomes

\[
N L_C^*=R(L_C). \tag{5.10}
\]

The quotient in (5.9) is rank one.  The tail (L_C\subset\mathbb Z^2)
and its Euclidean dual in (5.10) are rank two.  Neither is the original
construction dual
(\Lambda_{\rm dual}(A,N)\subseteq\mathbb Z^m), which has ambient rank
(m); no identification between those differently ranked objects is being
made.

## 6. Exact probability in the cyclic CVP model

Let

\[
P=\psi(\mathbb Z^2)=\|C_0\|^{-1}\mathbb Z.
\]

The projected public lattice is (NP), and the local projected lattices are
(pP) and (qP).  In the discrete cyclic CVP model, choose a target class
uniformly in

\[
P/NP\simeq\mathbb Z/N,
\]

choose any lift (y\in P), and subtract any chosen closest vector
(\lambda\in NP).  If the resulting integer residue is (K\bmod N), then
membership in (pP) is (p\mid K), and membership in (qP) is
(q\mid K).  There are (q) multiples of (p), (p) multiples of (q),
and one common multiple in (\mathbb Z/N).  Hence

\[
\boxed{
\Pr[\text{exactly one local projected lattice}]
=\frac1p+\frac1q-\frac2N.} \tag{6.1}
\]

If another closest lattice vector is chosen, it differs from the first by
an element of (NP).  The residue (K\bmod N), and therefore both local
membership predicates, are unchanged.  This handles ties without a
tie-breaking assumption.  Formula (6.1) is for a uniform **discrete cyclic
class**, not for an arbitrary or continuous target distribution.

## 7. Marginally uniform nonisotropic completion lines

Assume in this section that (p<q\le\kappa p) are distinct odd primes.  For
an odd prime (r), define

\[
S_r=\{[u:v]\in\mathbb P^1(\mathbb F_r):u^2+v^2\ne0\}.
\]

The projective line has (r+1) points.  An isotropic direction must have
(v\ne0), and then (x=u/v) solves (x^2=-1).  There are two such roots
when the Legendre symbol (\left(\frac{-1}{r}\right)=1), and none when it
is (-1).  Therefore

\[
\boxed{|S_r|=r-\left(\frac{-1}{r}\right).} \tag{7.1}
\]

In particular, (|S_r|\ge r-1).

Let ((\ell_p,\ell_q)) have any joint distribution on
(S_p\times S_q), subject only to each marginal being uniform.  Define

\[
L(\ell_p,\ell_q)=
\{v\in\mathbb Z^2:v\bmod r\in\ell_r\text{ for }r=p,q\}. \tag{7.2}
\]

Here each projective line denotes its one-dimensional vector subspace,
including zero.  CRT shows that the allowed residue set has
(p q=N) elements inside the (N^2)-element ambient residue space, so

\[
[\mathbb Z^2:L(\ell_p,\ell_q)]=N. \tag{7.3}
\]

Equivalently, CRT-lift nonzero representatives of the two lines to a vector
(C\bmod N).  Then (\gcd(N,C_1,C_2)=1), and (7.2) is precisely the
nonsingular (L_C) above.

We will bound the event

\[
\mathcal E=\{\text{some shortest nonzero }v\in L(\ell_p,\ell_q)
\text{ has }1<\gcd(N,v_1,v_2)<N\}. \tag{7.4}
\]

Every determinant-(N) planar lattice has a nonzero vector of Euclidean
length at most (\sqrt{2N}): apply Minkowski's convex-body theorem to
slightly enlarged squares of area (>4N), then take the limit.  Hence every
shortest vector (v) satisfies

\[
\|v\|\le\sqrt{2N}. \tag{7.5}
\]

Suppose first that the coordinate gcd in (7.4) is (p).  Write
(v=pa\).  It is essential that

\[
a\bmod q\ne0; \tag{7.6}
\]

otherwise (N) would divide both coordinates of (v).  Since (p) is a
unit modulo (q), membership of (v) in (7.2) forces

\[
\ell_q=[a\bmod q]. \tag{7.7}
\]

The divided vector cannot also satisfy the (p)-local line condition.  If
(a\bmod p\in\ell_p), then (7.7) would put (a) itself in the global lattice,
contradicting (\|a\|=\|v\|/p<\|v\|).  In particular (a\bmod p\ne0).  This
is the random-line version of the divide-then-test identity (5.5).

Let (d=\gcd(a_1,a_2)>0), with signs ignored, and let (a_0=a/d).  Relation
(7.6) and the preceding nonzero (p)-reduction imply (\gcd(d,N)=1), so
([a_0\bmod q]=[a\bmod q]).  Thus only the primitive integer direction of
(a) matters.  From (7.5) and balance,

\[
0<\|a_0\|\le\|a\|\le\sqrt{2q/p}\le\sqrt{2\kappa}. \tag{7.8}
\]

If instead the coordinate gcd is (q), writing (v=qa) gives the symmetric
facts

\[
a\bmod p\ne0,
\qquad \ell_p=[a\bmod p],
\qquad a\bmod q\notin\ell_q,
\qquad \|a_0\|\le\sqrt{2p/q}<\sqrt2. \tag{7.9}
\]

Define the finite, deterministic set of primitive directions

\[
\mathcal B_\kappa=
\{a\in\mathbb Z^2:\gcd(a_1,a_2)=1,
\ 0<\|a\|\le\sqrt{2\kappa}\}/\{\pm1\},
\qquad M_\kappa=|\mathcal B_\kappa|. \tag{7.10}
\]

For each prime (r), reduce these directions modulo (r), discard any
isotropic reductions, and merge projective collisions; call the resulting
subset of (S_r) (D_r).  A primitive integer vector never reduces to zero
modulo a prime, and

\[
|D_r|\le M_\kappa. \tag{7.11}
\]

Isotropic candidates cannot equal the sampled nonisotropic line and hence
are correctly discarded.  Distinct bounded integer directions that collide
projectively modulo a small prime only decrease the cardinality.

The existence of a (p)-divisible shortest vector implies
(\ell_q\in D_q), while the existence of a (q)-divisible shortest vector
implies (\ell_p\in D_p).  Marginal uniformity and a union bound now give

\[
\begin{aligned}
\Pr(\mathcal E)
&\le \frac{|D_q|}{|S_q|}+\frac{|D_p|}{|S_p|}\\
&\le M_\kappa\left(\frac1{q-1}+\frac1{p-1}\right)\\
&\le \frac{3M_\kappa}{2}
\left(\frac1p+\frac1q\right),
\end{aligned} \tag{7.12}
\]

where the last inequality holds for every odd prime, including (3).
Thus all small-prime cases are already covered (and could alternatively be
absorbed into the constant depending on (\kappa)).  The argument concerns
the existence of **any** bad shortest vector, so arbitrary ties among
shortest vectors need no selection rule.  Finally, no joint independence is
used: the (p)-divisible event is bounded solely through the (q)-marginal,
the (q)-divisible event solely through the (p)-marginal, and then the two
bounds are added.

## 8. Complexity and exact negative boundary

All deterministic reductions above have polynomial bit complexity in the
dimensions and input bit length:

* gcd, extended-gcd, and CRT construct (g,h,C_0,D) and all displayed
  bases with polynomial-size integers;
* Smith/Hermite algorithms construct the decompositions and primitive
  summands in Section 2, while exact rational linear algebra constructs the
  orthogonal projected bases;
* the fixed-completion criterion can be checked either by Smith form or by
  the (O(m^3)) many (3\times3) minors and gcds;
* planar lattice reduction and the one-dimensional cyclic closest-point
  operation are polynomial-bit procedures.  The set
  (\mathcal B_\kappa) is finite for fixed (kappa).

Computing a proper gcd encountered in a Smith entry, completion, or vector
does expose (p) or (q).  The results do not guarantee that such a gcd
will occur.  In fact, (7.12) says that the advertised shortest-vector event
is rare under its stated line model.

The exact boundary is therefore:

* biased completion lines or biased cyclic targets are not covered by the
  probability formulas;
* a batch without one fixed completion and the surjective-(T) hypothesis
  has only the unsplit image description (3.1)-(3.2);
* nonlinear combinations are outside the integer-linear output map;
* the projected metric identities do not imply an SVP/CVP statement for a
  full lattice after a nonorthogonal Smith transformation;
* optimizing coordinate gcd in the original rank-(m), nonorthogonally
  coupled construction lattice remains open; the rank-two tail dual and
  rank-one orthogonal quotient do not solve that problem.

Accordingly, this reconstruction is a collection of exact conditional
structure and probability theorems.  It is **not a factoring algorithm**.
