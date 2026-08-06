# F25 — a narrow obstruction to zero-syndrome hidden-modulus lattice amortization

**Status:** self-audited.

**Revision note:** substantively corrected after a hostile audit; a fresh
hostile re-audit is required before any stronger label.

**Family:** F19.

**Classification:** evidence against the exact auxiliary mechanism of gaining
a high-dimensional decoder merely by adding samples to the public
zero-syndrome Construction-A kernel, its shared-output coefficient/Gram
presentation, or the displayed block and below-threshold graph constructions.
The public output lattice, the scaled dual lattice, fixed-rank exact quotient
decoding, nonlinear sample-combining maps, and other target/metric choices
remain open.

No computation was used.  All statements below are symbolic.  The analysis
is restricted to distinct odd semiprimes when it uses the split rank-one
description; the narrow obstruction already applies on balanced semiprimes,
which is enough to defeat the analyzed construction as an all-input algorithm.

## Outcome

The attractive metric gap is real but belongs to two lattices that are not
public.  If \(\alpha\in\mathcal H\) has reduced norm \(N=pq\), then the
two intrinsic local kernel lattices have shortest Hurwitz length
\(\sqrt p\) and \(\sqrt q\), whereas their public CRT intersection has
shortest length \(\sqrt N\).  A basis for either local lattice would make
LLL more than adequate on all sufficiently large inputs.  But the determinant
of that basis already reveals the corresponding prime.

The standard public **zero-syndrome kernel** construction instead gives the
intersection of the two local kernels.  HNF, SNF, and LLL applied to that
kernel return vectors satisfying both local conditions, so the natural
syndrome gcd is \(N\), not a proper divisor.  An integer-target CVP call in
that kernel cannot change this: subtracting a point of the public intersection
preserves the target's two local syndromes.  After unequal local ranks have
already been separated by SNF minors, uniform targets hit exactly one kernel
with exponentially small probability in the common positive-rank case.

There is a second, independent loss in the many-sample coefficient and Gram
encodings.  Concatenating \(m\) samples into a map with a fixed four-dimensional
output creates an exact rational kernel of rank at least \(m-4\).  Those
prime-independent directions consume the apparent high-dimensional
short-vector gain.  After quotienting them out, the informative metric rank is
at most four.  Block-diagonalizing removes that exact kernel, but then the
local codimension grows linearly with \(m\), and the determinant scale stays
\(\sqrt p\) or \(\sqrt q\); there is no amortized dimension gain.

This establishes a narrow obstruction to the proposed high-dimensional
zero-syndrome amortization.  It does not close the broader F19 family.  In
particular, the public output and scaled-dual lattices derived in Section 7,
and a faithful fixed-rank exact metric decoder on the informative quotient,
are untested open routes.

## 1. Intrinsic setup and the extraction test

Fix the four-element \(\mathbb Z\)-basis

\[
\left\{1,i,j,\frac{1+i+j+k}{2}\right\}
\]

of the Hurwitz order
\(\mathcal H=\mathbb Z[i,j,(1+i+j+k)/2]\).

In these coordinates, reduced norm is a fixed positive-definite integral
quadratic form \(Q\).  Clearing the fixed denominator in its polar Gram matrix
changes all bit lengths by only a constant.  A norm-\(N\) sample has four
\(O(\log N)\)-bit coordinates.  Every Hurwitz-lattice determinant below is
an index or covolume relative to this fixed coordinate lattice; changing the
ambient Euclidean normalization multiplies all of them by one fixed constant.

For public samples \(\alpha_1,\ldots,\alpha_m\), let

\[
C=(\operatorname{coord}(\alpha_1)\ \cdots\
   \operatorname{coord}(\alpha_m))\in\mathbb Z^{4\times m}.
\]

For \(r\mid N\), define the lifted relation lattice

\[
K_r(C)=\{c\in\mathbb Z^m:Cc\in r\mathbb Z^4\}.
\]

If

\[
c\in K_p(C)\setminus K_q(C),
\]

then the completely public test

\[
g=\gcd\bigl(N,(Cc)_1,(Cc)_2,(Cc)_3,(Cc)_4\bigr)
\]

returns \(p\).  The opposite difference returns \(q\).  The test is exact,
has polynomial bit complexity for polynomial-bit \(c\), and every returned
divisor can be verified by division.  If \(c\in K_p\cap K_q\), it returns
\(N\).

The same definition and test apply to any public integer matrix \(A\), not
only the four-coordinate matrix \(C\).  This includes compatible public
\(2\times2\) lifts, row/column stacks, and Gram matrices.

## 2. Exact Construction-A bookkeeping

Let \(A\in\mathbb Z^{t\times d}\), and put

\[
s_r=\operatorname{rank}_{\mathbb F_r}(A\bmod r).
\]

Reduction modulo \(r\) gives

\[
[\mathbb Z^d:K_r(A)]=r^{s_r},\qquad
\det K_r(A)=r^{s_r}.
\]

For \(N=pq\), CRT gives the exact identities

\[
K_N(A)=K_p(A)\cap K_q(A),\qquad
\det K_N(A)=p^{s_p}q^{s_q}.
\]

These formulas require no randomness.

There is a useful boundary case that should be removed before invoking any
metric algorithm.  Let \(\delta_k(A)\) be the gcd of the \(k\times k\) minors,
obtainable from the integer SNF.  For either prime \(r\),

\[
r\mid\delta_k(A)
\quad\longleftrightarrow\quad
\operatorname{rank}_{\mathbb F_r}(A)<k.
\]

Consequently, if \(s_p\ne s_q\), then some
\(\gcd(N,\delta_k(A))\) is already a proper factor.  This is a deterministic
polynomial-bit rank separator, not a lattice-decoding gain.  The genuinely new
case is therefore the equal-rank case.

### The disjunction is not a lattice

The desired set is

\[
\bigl(K_p(A)\setminus K_q(A)\bigr)
\cup
\bigl(K_q(A)\setminus K_p(A)\bigr).
\]

It is not additive.  More generally, if \(U,V\) are subgroups of an abelian
group and a subgroup \(L\) is contained in \(U\cup V\), then
\(L\subseteq U\) or \(L\subseteq V\).  Otherwise choose
\(x\in L\setminus U\) and \(y\in L\setminus V\); necessarily
\(x\in V\), \(y\in U\), and \(x+y\) lies in neither subgroup, a
contradiction.

Therefore a homogeneous linear system cannot represent the two-branch union
exactly.  A Construction-A lattice made with the public modulus \(N\) represents
the intersection.  A lattice soundly contained in the union must already have
selected one hidden branch.  This is only an obstruction to an exact linear
encoding; it is not a claim that the shortest vectors of every conceivable
larger public lattice avoid the union.

### Determinant and random-code scales

For a surrogate with \(s\) independent uniform parity checks over
\(\mathbb F_r\), a fixed nonzero residue vector satisfies the checks with
probability exactly \(r^{-s}\); such a matrix has full row rank with high
probability when \(d\ge s\).  Thus the expected count in a Euclidean ball of
radius \(R\) is approximately

\[
\frac{\operatorname{vol} B_d(R)}{r^s},
\]

and the usual determinant/Gaussian benchmark is

\[
R_r\asymp
\sqrt{\frac{d}{2\pi e}}\,r^{s/d}.
\]

For two independent CRT components of equal rank \(s\), the corresponding
public-intersection benchmark is

\[
R_N\asymp
\sqrt{\frac{d}{2\pi e}}\,N^{s/d},
\qquad
\frac{R_N}{R_p}\asymp q^{s/d}.
\]

These are optimistic random-code benchmarks, not distribution theorems for
Hurwitz outputs.  Minkowski gives the same determinant exponent with an
\(O(\sqrt d)\) upper-bound factor, but it does not say that the short vector
is informative.

For scalar coefficient relations, \(d=m\) and \(s\le4\).  If
\(m=Cn\) with \(n=\lceil\log_2(N+1)\rceil\) and balanced factors, then
\(p^{4/m}\) and the local/public ratio are only constants.  Standard
\(\delta=3/4\) LLL has approximation factor
\(2^{(m-1)/2}\), which overwhelms that scale.  If instead
\(m=O(\log n)\), the determinant gap is superpolynomial in \(n\) while the
LLL factor is polynomial.  This tempting latter determinant comparison still
does not by itself establish the advertised high-dimensional decoder: a basis
of \(K_p\) or \(K_q\) is not public, and the raw calculation hides the exact
kernel described next.  This statement does not address a different
fixed-rank quotient metric.

## 3. The exact-kernel loss in many-sample relations

Let

\[
\rho=\operatorname{rank}_{\mathbb Q}A,\qquad
K_0=\ker_{\mathbb Z}A.
\]

Then \(K_0\) is primitive of rank \(d-\rho\): indeed,
\(\mathbb Z^d/K_0\cong A\mathbb Z^d\), and the latter is a free abelian
group.  It is contained in every \(K_r(A)\).  For a scalar quaternion
coefficient matrix, \(\rho\le4\); for a concatenated multiplication map
\(\mathcal H^m\to\mathcal H\), again \(\rho\le4\).  Hence adding samples adds
mostly exact, prime-independent relations.

This can be quantified without a heuristic.  Let \(\pi\) be orthogonal
projection to \((K_0\otimes\mathbb R)^\perp\), and let
\(\Delta_0\) be the covolume of \(K_0\) in its real span.  Primitivity and
unimodularity of \(\mathbb Z^d\) give

\[
\det\pi(\mathbb Z^d)=\Delta_0^{-1}.
\]

For completeness, this is the standard orthogonal volume decomposition for
a primitive sublattice: a fundamental parallelepiped of \(K_0\), followed by
lifts of a basis of \(\pi(\mathbb Z^d)\), has total volume
\(\Delta_0\det\pi(\mathbb Z^d)=\det\mathbb Z^d=1\).  Moreover, projection
induces \(\mathbb Z^d/K_0\cong\pi(\mathbb Z^d)\), so
\([\pi(\mathbb Z^d):\pi(K_r)]=[\mathbb Z^d:K_r]=r^{s_r}\).  Thus all
projected lattices have real rank \(\rho\), and the general formulas are

\[
\det\pi(K_p)=\frac{p^{s_p}}{\Delta_0},\qquad
\det\pi(K_q)=\frac{q^{s_q}}{\Delta_0},\qquad
\det\pi(K_N)=\frac{p^{s_p}q^{s_q}}{\Delta_0}.
\]

If \(\rho>0\), then in the equal-local-rank case
\(s_p=s_q=u\le\rho\), their determinant-root scales in rank \(\rho\) are

\[
p^{u/\rho}\Delta_0^{-1/\rho},\qquad
q^{u/\rho}\Delta_0^{-1/\rho},\qquad
N^{u/\rho}\Delta_0^{-1/\rho}.
\]

Only in the clean full-local-rank case \(u=\rho\) do these specialize to

\[
p\Delta_0^{-1/\rho},\qquad
q\Delta_0^{-1/\rho},\qquad
N\Delta_0^{-1/\rho}.
\]

If \(\rho=0\), then \(A=0\), all three kernel lattices are
\(\mathbb Z^d\), and there is no syndrome information.

The distinction is essential: a shared-output Hurwitz multiplication map can
have \(\rho=4\) and common local rank \(u=2\).  Increasing \(m\) can change
\(\Delta_0\), but it changes all three displayed scales by the same factor.
The apparent exponent \(r^{s_r/d}\) in the full-dimensional lattice mixes
the informative rank-\(\rho\) quotient with \(d-\rho\) exact directions.
Quotienting therefore removes the claimed **high-dimensional amortization**;
it does not prove that a shortest or closest vector in a faithfully
constructed fixed-rank quotient metric cannot have useful one-local-only
divisibility.

If a basis of either projected local lattice were available, LLL in rank
\(\rho\le4\) would lose only the constant factor
\(2^{(\rho-1)/2}\).  The local basis is not public.  Exact SVP/CVP in a
public fixed-rank quotient is computationally tractable in principle, but
whether a specified public quotient, target, and extraction rule yield a
proper divisor is left open in Section 7.

## 4. CVP subtraction inside \(K_N\) cannot manufacture a syndrome

Let a public integer target \(t\in\mathbb Z^d\) be given, and let an exact or
approximate CVP procedure return any \(v\in K_N(A)\).  Put \(e=t-v\).  For
each \(r\in\{p,q\}\),

\[
e\in K_r(A)
\quad\longleftrightarrow\quad
t\in K_r(A),
\]

because \(v\in K_r(A)\).  Nearest-vector selection only chooses a short
representative of a syndrome coset; it cannot change which hidden local
syndromes vanish.

In particular, if \(t\) is uniform modulo \(N\), then exactly

\[
\Pr\bigl(e\in
(K_p\setminus K_q)\cup(K_q\setminus K_p)\bigr)
=p^{-s_p}+q^{-s_q}-2p^{-s_p}q^{-s_q}.
\]

For balanced factors this is exponential in the input length when **both**
local ranks are positive.  After the determinantal-divisor preprocessing, the
unseparated equal-rank case is either common positive rank, where polynomially
many uniform targets do not help, or common rank zero, where all syndromes
vanish and no proper syndrome is present.

For clarity, the zero-rank cases in the displayed exact formula are:

- if \(s_p=0<s_q\), then \(K_p=\mathbb Z^d\) and a uniform target lies in
  \(K_p\setminus K_q\) with probability \(1-q^{-s_q}\); the same input is
  already factored deterministically by the rank-mismatch minor;
- if \(s_q=0<s_p\), the statement is symmetric; and
- if \(s_p=s_q=0\), then every entry of \(A\) is divisible by \(N\), so
  \(K_p=K_q=K_N=\mathbb Z^d\) and the symmetric difference is empty.

A deliberately biased public target distribution is not ruled out, but it
needs a new distribution theorem; CVP subtraction inside \(K_N\) itself
supplies no bias.

This differs sharply from P19.  P19 uses exact CVP to enforce an already-public
Boolean multiplication disjunction.  Its squared-distance gap is only
\(M\) versus \(M+8\), a distance ratio

\[
\sqrt{1+8/M}=1+O(1/M),
\]

so ordinary lattice approximation is insufficient.  Here the hypothetical
local/intersection gap can be as large as \(\sqrt q\), but the local affine
set is not public.  Encoding nontrivial integers \(d,e>1\) with \(de=N\)
restores a nonlinear multiplication constraint and loses the claimed
simple-lattice advantage.

## 5. Exact Hurwitz block calculation

The strongest metric version uses multiplication rather than scalar
coefficients.  For one sample \(\alpha\), let

\[
M_\alpha:\mathcal H\to\mathcal H,\qquad x\mapsto\alpha x.
\]

In a Hurwitz basis this is a public \(4\times4\) integer matrix satisfying

\[
\det M_\alpha=N^2,\qquad
Q(M_\alpha x)=NQ(x).
\]

Modulo either odd prime divisor \(r\), the element \(\alpha\) is nonzero:
if \(\alpha=r\beta\) in \(\mathcal H\), then
\(r^2\mid\operatorname{nrd}(\alpha)=pq\), which is impossible.  It is
therefore a nonzero rank-one matrix in a split copy of
\(M_2(\mathbb F_r)\).  Left
multiplication therefore has rank two on the four-dimensional algebra.  Since
the determinant has valuation exactly two at both primes, the integer Smith
form is

\[
\operatorname{SNF}(M_\alpha)=\operatorname{diag}(1,1,N,N).
\]

It exposes \(N\) twice and neither proper factor.

Define the intrinsic local right ideals

\[
J_r(\alpha)=\{x\in\mathcal H:\alpha x\in r\mathcal H\}.
\]

They have index \(r^2\).  Here the required principality is the standard
one-sided norm-Euclidean theorem for the Hurwitz order.  A short proof fixes
the handedness: for a nonzero right ideal \(I\), choose
\(0\ne d\in I\) of minimum reduced norm.  Hurwitz norm-Euclidean
approximation gives, for every \(x\in I\), an \(h\in\mathcal H\) with

\[
\operatorname{nrd}(d^{-1}x-h)<1.
\]

Then \(x-dh\in I\) and
\(\operatorname{nrd}(x-dh)<\operatorname{nrd}(d)\), so minimality forces
\(x=dh\).  Hence \(I=d\mathcal H\).  Applying this to \(J_r\) gives

\[
J_r(\alpha)=d_r\mathcal H.
\]

The index identity
\([\mathcal H:d_r\mathcal H]=\operatorname{nrd}(d_r)^2\) forces
\(\operatorname{nrd}(d_r)=r\).  Norm is multiplicative, and every nonzero
Hurwitz integer has positive integral norm at least one, attained by a unit.
Consequently, with Hurwitz length \(\|x\|_Q=\sqrt{Q(x)}\), the minimum is
an equality, not just a determinant estimate:

\[
\det J_r=r^2,\qquad \lambda_1(J_r)=\sqrt r.
\]

The public congruence uses \(N\):

\[
\begin{aligned}
J_N(\alpha)
&=\{x:\alpha x\in N\mathcal H\}\\
&=\bar\alpha\mathcal H
=J_p(\alpha)\cap J_q(\alpha),
\end{aligned}
\]

so

\[
\det J_N=N^2,\qquad \lambda_1(J_N)=\sqrt N.
\]

More strongly, the natural basis of \(\bar\alpha\mathcal H\) has Gram
matrix exactly \(N\) times the fixed Hurwitz Gram matrix.  As an
origin-centered Euclidean lattice, \(J_N\) is just a rotated copy of
\(\sqrt N\mathcal H\).  Its determinant, successive minima, and shape contain
no \(p/q\) granularity.

For \(m\) samples, block diagonal multiplication gives

\[
D=\operatorname{diag}(M_{\alpha_1},\ldots,M_{\alpha_m}).
\]

Its local and public kernel lattices have

\[
\begin{array}{c|c|c|c}
&\text{rank}&\text{determinant}&\lambda_1\\ \hline
\bigoplus_iJ_p(\alpha_i)&4m&p^{2m}&\sqrt p\\
\bigoplus_iJ_q(\alpha_i)&4m&q^{2m}&\sqrt q\\
\bigoplus_iJ_N(\alpha_i)&4m&N^{2m}&\sqrt N.
\end{array}
\]

The determinant roots are \(\sqrt p,\sqrt q,\sqrt N\); adding blocks
does not improve them.  This is the other side of the rank-bookkeeping
dichotomy: shared-output concatenation has a large exact kernel, while
block-diagonalization has local codimension \(2m\).

If a basis of \(J_r\) were somehow supplied, four-dimensional LLL would return
a vector of length at most \(2^{3/2}\sqrt r\).  When the other prime exceeds
\(8\), this is shorter than every nonzero vector of \(J_N\), so the public syndrome
gcd would split \(N\).  Exact SVP returns a generator of norm exactly \(r\),
which is already the prime.  But a basis of \(J_r\) reveals

\[
r=\sqrt{[\mathcal H:J_r]},
\]

before LLL is called.  Constructing the branch is itself a factoring
interface.

Conversely, exact SVP in the public lattice \(J_N=\bar\alpha\mathcal H\)
returns a primitive norm-\(N\) element whose norm and coordinate gcd give no
proper factor.  If
\(x\in J_N\cap r\mathcal H\), then
\(Q(x)\ge Nr\): write \(x=\bar\alpha y\); divisibility
\(x\in r\mathcal H\) forces \(r\mid Q(y)\), so
\(Q(x)=NQ(y)\ge Nr\).  Hence, after trial division by the finitely many
small primes, even the standard four-dimensional LLL approximation to the
public ideal is too short to be a coordinatewise \(p\)- or \(q\)-torsion
vector.  Looking for a proper coordinate gcd inside the public intersection
does not rescue its shortest vectors.

## 6. The displayed graph embedding: exact unwrapped and threshold facts

A standard attempt to avoid selecting \(p\) or \(q\) is the public graph
lattice

\[
\Gamma_{a,b}(A,N)=
\{(ax,\b(Ax-Nz)):x\in\mathbb Z^d,
z\in\mathbb Z^t\},
\]

with positive rational weights cleared to integers.  Its block-triangular
basis gives

\[
\det\Gamma_{a,b}=a^d(bN)^t.
\]

For one multiplication block, \(d=t=4\), so its determinant radius in
dimension eight is \(\sqrt{abN}\).  Direct sums do not change that root
scale.

The exact similarity calculation shows why the local kernel is not favored in
the unwrapped slice.  For a vector with \(z=0\),

\[
a^2Q(x)+b^2Q(M_\alpha x)
=(a^2+b^2N)Q(x).
\]

A unit input has this baseline length, while every nonzero
\(x\in J_r\) is at least a factor \(\sqrt r\) longer.  With wrapping,
the residual \(s=M_\alpha x-Nz\) of a local-kernel vector lies in
\(r\mathcal H\).  If it is nonzero, then \(Q(s)\ge r^2\).  Therefore, for
\(x\in J_r(\alpha)\), a CVP/SVP regime forcing residual length below \(r\)
selects only \(s=0\), which is precisely the public intersection \(J_N\).

Above that threshold, these calculations establish only an **absence of a
guaranteed saving** from local divisibility.  The elementary spacing intuition
is that conditioning a uniformly distributed scalar residue to be divisible
by \(p\) reduces the number of residues by \(p\) while increasing their
spacing by the same factor.  That is not a distribution theorem for the
actual multi-coordinate Hurwitz syndromes.  It does not rule out another
choice of weights, target, affine shift, or postprocessor.  The only general
CVP statement retained here is Section 4's exact coset invariance for CVP
inside \(K_N\).

## 7. Gram bookkeeping and public primal/dual lattices left open

### What the Gram calculation proves

Let \(T\) be the fixed polar Gram matrix of reduced norm and set

\[
G=C^{\mathsf T}TC.
\]

Its entries have \(O(\log N)\) bits and

\[
\operatorname{rank}_{\mathbb Q}G
=\operatorname{rank}_{\mathbb Q}C\le4,\qquad
c^{\mathsf T}Gc=Q(Cc).
\]

Positive definiteness of \(T\) gives
\(\ker_{\mathbb Q}G=\ker_{\mathbb Q}C\), so the exact integer kernel is
again \(K_0\).  A semidefinite shortest-vector call in coefficient space
first sees its zero directions.  Quotienting them leaves a metric object of
rank at most four.  This proves loss of the proposed **high-dimensional**
determinant amortization, not failure of a fixed-rank decoder.

Indeed, the image lattice

\[
I=C\mathbb Z^m\subseteq\mathcal H
\]

has rank at most four and the quotient quadratic form is exactly \(Q\) on
\(I\).  A basis of \(I\) is publicly computable, and exact fixed-dimensional
SVP/CVP is polynomial in the input bit length.  It remains **open** whether a
specified shortest/closest vector, target rule, and public extraction test on
this or another faithful quotient metric lands in a \(p\)-only or \(q\)-only
condition with inverse-polynomial probability.

If one instead uses only the linear modular kernel
\(Gc\equiv0\pmod r\), all determinant, intersection, random-target, and
rank-mismatch statements of Sections 2--4 apply with
\(s_r=\operatorname{rank}(G\bmod r)\).  The narrow obstruction closes that
linear zero-syndrome use of \(G\), not every metric use of its quotient.

The larger set

\[
\{c:Q(Cc)\equiv0\pmod p\}
\cup
\{c:Q(Cc)\equiv0\pmod q\}
\]

is a union of local quadrics, not a relation lattice.  Its useful points can
be tested by \(\gcd(N,Q(Cc))\), and a point of norm exactly \(p\) or \(q\)
gives the divisor directly.  But linearizing with variables
\(z_{ij}=c_ic_j\) requires the rank-one constraint
\(Z=cc^{\mathsf T}\).  Dropping that constraint creates a relaxation whose
linear solutions need not decode to any \(c\); enforcing it restores a
nonlinear/disjunctive search.  This is the same precise structural fault as
P19's convolution relaxation losing Boolean rank one, not a proof that all
quadratic decoding is hard.

The same limited rank bookkeeping applies if compatible public
\(2\times2\) representatives are granted.  Horizontal concatenation has
fixed output rank at most two and a large exact kernel; block diagonalization
has local rank \(m\) in dimension \(2m\), determinant root \(\sqrt r\); and
the displayed public modular kernel is the CRT intersection of the two local
line kernels.  This does not analyze other metrics or the output/dual
lattices below.

### Two public lattices not covered by the intersection theorem

For every public \(A\in\mathbb Z^{t\times d}\), define the full-rank public
output lattice

\[
\Lambda_{\rm out}(A,N)=A\mathbb Z^d+N\mathbb Z^t
\subseteq\mathbb Z^t.
\]

It is generated by the columns of \((A\ \ NI_t)\).  Reduction modulo \(N\)
identifies

\[
\mathbb Z^t/\Lambda_{\rm out}
\cong
(\mathbb Z/N\mathbb Z)^t/
\operatorname{im}(A\bmod N),
\]

so CRT and the local ranks give

\[
\det\Lambda_{\rm out}
=p^{t-s_p}q^{t-s_q}.
\]

This is an output-space lattice, not a sublattice of the coefficient kernel
\(K_N(A)\), so Sections 2 and 4 do not determine its shortest or closest
vectors.

The other standard public object is the scaled dual of the kernel lattice:

\[
\Lambda_{\rm dual}(A,N)
=N K_N(A)^*
=N\mathbb Z^d+A^{\mathsf T}\mathbb Z^t.
\]

To derive the identity, every

\[
z+\frac1N A^{\mathsf T}y,
\qquad z\in\mathbb Z^d, y\in\mathbb Z^t,
\]

pairs integrally with \(K_N(A)\), giving the inclusion

\[
\mathbb Z^d+\frac1N A^{\mathsf T}\mathbb Z^t
\subseteq K_N(A)^*.
\]

Modulo \(\mathbb Z^d\), the lattice on the left has
\(p^{s_p}q^{s_q}\) elements, because the transpose has the same local ranks
as \(A\).  Its covolume is therefore
\((p^{s_p}q^{s_q})^{-1}=\det K_N(A)^*\), proving equality.  Scaling by
\(N\) gives the displayed public formula and

\[
\det\Lambda_{\rm dual}
=\frac{N^d}{p^{s_p}q^{s_q}}
=p^{d-s_p}q^{d-s_q}.
\]

When \(s_p=s_q=u\), the two determinants specialize to

\[
\det\Lambda_{\rm out}=N^{t-u},
\qquad
\det\Lambda_{\rm dual}=N^{d-u}.
\]

Their Smith invariants need not expose a proper factor in this equal-rank
case, but their geometry is not controlled by the kernel-intersection proof.
For the sanity check \(A=(1)\), one has
\(K_N=N\mathbb Z\) but
\(N K_N^*=\mathbb Z\); its shortest vector is not in either zero-syndrome
kernel.  This example gives no factor, but proves that the Section 4 argument
cannot simply be transferred to the scaled dual.

No shortest-vector, closest-vector, quotient-shape, or target-distribution
theorem for \(\Lambda_{\rm out}\) or \(\Lambda_{\rm dual}\) is proved here.
Whether either lattice, alone or combined with the fixed-rank metric above,
has an inverse-polynomial one-local extraction law is explicitly **open**.

## 8. Relation to P30's birthday obstruction

This candidate genuinely differs from pair collision.  With more than four
scalar samples, local linear relations exist abundantly even when no two row
or image lines coincide.  Therefore P30's pairwise birthday bound is not a
lower bound for this decoder.

The deterministic obstruction proved for the displayed zero-syndrome
amortization is:

1. the abundant local code is not public;
2. its public zero-syndrome lift is the CRT intersection;
3. fixed-output concatenation pads the geometry with exact relations; and
4. block diagonalization removes those relations only by making the local
   codimension linear in the sample count.

These four facts do not analyze \(\Lambda_{\rm out}\),
\(\Lambda_{\rm dual}\), or a different fixed-rank quotient metric.

P30 remains relevant to the source distribution.  It proves that the actual
residual-only four-square outputs do not already supply matched-handed
collisions or fixed-unit stabilizer bias with polynomial probability.  Nothing
in the present analysis extends that theorem to mixed-handed comparisons or
nonlinear combinations.  Conversely, nothing in P30 supplies the biased CVP
targets or the public branch lattice missing here.

## 9. Bit complexity and the missing Las Vegas success theorem

Let \(m\le n^c\).  The public objects have polynomial size:

- \(C\) has \(4m\) entries of \(O(n)\) bits;
- \(G\) has \(m^2\) entries of \(O(n)\) bits;
- the multiplication block matrix has rank \(4m\) and
  \(O(n)\)-bit entries;
- \(\log\det K_N(C)\le4n\), while the block determinant has
  \(2mn\) bits; and
- the graph embedding has polynomial rank and polynomial determinant bit
  length (and has \(O(mn)\) determinant bits when the weights have
  \(O(n)\)-bit numerators and denominators); and
- \(\Lambda_{\rm out}\) and \(\Lambda_{\rm dual}\) have the explicit
  polynomial-size generator matrices above and determinant bit length
  \(O((d+t)n)\).

Integer HNF/SNF, rational projection data, LLL, gcds, reduced norms, and
candidate division checks therefore all have polynomial bit complexity.
Exact SVP/CVP on the rank-\(\rho\le4\) quotient is also a fixed-dimensional
polynomial-bit operation.  Exact CVP in any growing-dimensional construction
is not being treated as polynomial.  No coefficient-size obstruction is
asserted.

What is missing is a success theorem.  The unconditional polynomial-time
outcomes proved here are:

- a factor when the two local ranks differ, via a determinantal divisor; or
- vectors of the public intersection, whose natural syndrome extraction is
  trivial.

No every-input sampler is known to make the rank-mismatch event occur with
inverse-polynomial probability.  Uniform CVP targets in the public kernel
have the exact exponentially small probability above, and constructing a
local lattice basis already reveals its prime through its determinant.  The
output, dual, and fixed-rank quotient routes have no proved extraction law in
either direction.  Consequently this artifact establishes no every-input Las
Vegas algorithm and supplies no recursion or prime-power runtime proof.  That
is an absence of a proved algorithm, not a refutation of the explicitly open
routes.

## 10. Exact scope and reopen condition

The narrow obstruction is:

> For public linear relation maps built from the samples, zero-syndrome
> Construction A over \(N\) constructs the CRT intersection, while the useful
> local disjunction is not additive.  Shared-output many-sample encodings have
> only constant informative quotient rank, and block encodings retain
> \(\sqrt r\) determinant scale.  HNF/SNF/LLL on the displayed public kernel
> stays in the CRT intersection, and CVP subtraction from that kernel preserves
> the target's local syndromes.  These facts defeat the claimed
> high-dimensional zero-syndrome amortization, while leaving output, dual, and
> fixed-rank metric decoding open.

The immediate open tests are the geometry and extraction laws of
\(\Lambda_{\rm out}\), \(\Lambda_{\rm dual}\), and a faithful rank-at-most-four
quotient decoder.  A successful continuation needs at least one of the
following exact new ingredients:

1. a theorem for the public output or scaled-dual lattice whose specified
   LLL/SVP/CVP output is proved to yield a verifiable one-local condition
   with probability at least \(1/\operatorname{poly}(n)\);
2. a faithful fixed-rank quotient construction whose exact optimizer is
   proved to lie in
   \(K_p\triangle K_q\) with probability at least \(1/\operatorname{poly}(n)\)
   for an explicit expected-polynomial sample distribution on every balanced
   semiprime;
3. a nonlinear joint decoder for the union of the two local codes, with a
   proof that it does not assume a local basis, a factor, or a rank-one lift
   oracle;
4. a public target-generation rule with a proved inverse-polynomial bias
   toward exactly one local syndrome, since nearest-vector reduction itself
   preserves the target syndrome; or
5. a construction whose rational informative rank grows with \(m\) while its
   local codimension remains small, together with exact determinant,
   approximation, extraction, and every-input distribution bounds.

The exact reopen condition for the **closed narrow mechanism** is a new
construction or theorem that changes the rank bookkeeping or proves a biased
one-local output; merely increasing \(m\), applying HNF/SNF before LLL, or
asking exact CVP on the public intersection does not do so.  This sentence
does not place the untested output, dual, fixed-rank, affine, or nonlinear
routes behind a reopen barrier: they remain open now.
