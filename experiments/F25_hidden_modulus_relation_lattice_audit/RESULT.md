# Hostile audit of F25 — hidden-modulus relation lattices

**Audit status:** focused hostile audit, symbolic only.

**Artifact audited:** `experiments/F25_hidden_modulus_relation_lattice/RESULT.md`.

**Computation:** none.

## Verdict in brief

The central narrow obstruction survives.  For a public integer map, the
zero-syndrome Construction-A lattice at modulus \(N=pq\) is exactly the
intersection of the two local kernel lattices.  Subtracting any vector of
that public intersection in a CVP call preserves both local syndromes.
For Hurwitz left multiplication by an element of squarefree norm \(N\), the
integer Smith form is indeed \(\operatorname{diag}(1,1,N,N)\), the two
nonpublic local right ideals have minima \(\sqrt p\) and \(\sqrt q\), and
their public intersection is \(\bar\alpha\mathcal H\), with minimum
\(\sqrt N\).  Shared-output concatenation also has a primitive exact
integer kernel of all but constant rank, while direct sums retain the same
determinant-root scale.  These facts rigorously defeat the proposed
*high-dimensional Construction-A amortization*.

The report nevertheless needs two mathematical scope corrections before it
can be reconstructed:

1. its projected determinant display treats only the clean case in which
   the common local rank equals the rational rank.  The common
   rank-deficient case is not a rank-mismatch separator and has different
   determinant exponents;
2. the declaration of method failure for “Gram” and standard public lattice
   formulations is too broad.  The public output lattice
   \(A\mathbb Z^d+N\mathbb Z^t\) and the public scaled dual
   \(N K_N(A)^*=N\mathbb Z^d+A^{\mathsf T}\mathbb Z^t\) are not analyzed.
   More basically, quotienting a Gram construction to rank at most four
   removes the claimed amortized dimension gain, but does not prove that an
   exact fixed-rank metric decoder cannot output a one-local-only vector.

Accordingly, the valid theorem is a narrow obstruction, not an exhaustive
failure of public linear or metric lattices.

## 1. Construction-A indices and the CRT intersection

Let

\[
K_r(A)=\{x\in\mathbb Z^d:Ax\in r\mathbb Z^t\},
\qquad
s_r=\operatorname{rank}_{\mathbb F_r}(A\bmod r).
\]

Reduction modulo \(r\) maps \(\mathbb Z^d\) onto the image of
\(A\bmod r\), whose cardinality is \(r^{s_r}\).  Its kernel is
\(K_r(A)\).  Hence

\[
[\mathbb Z^d:K_r(A)]=\det K_r(A)=r^{s_r}.
\]

For distinct primes \(p,q\), the congruence \(Ax\equiv0\pmod{pq}\) is
equivalent to the pair of congruences modulo \(p\) and \(q\).  Therefore

\[
K_N(A)=K_p(A)\cap K_q(A)
\]

and, by CRT on the image,

\[
[\mathbb Z^d:K_N(A)]=p^{s_p}q^{s_q}.
\]

These statements remain true for rectangular and rank-deficient matrices.
No independence assumption is present.

### Rank-mismatch separator

For nonzero \(k\)-th determinantal divisor \(\delta_k(A)\), reduction has
rank below \(k\) modulo \(r\) exactly when \(r\mid\delta_k(A)\).  If
\(s_p<s_q\), choosing \(k=s_q\) gives

\[
p\mid\delta_k(A),\qquad q\nmid\delta_k(A).
\]

The chosen divisor is nonzero because rank modulo \(q\) is \(k\), so rank
over \(\mathbb Q\) is at least \(k\).  Thus
\(\gcd(N,\delta_k(A))=p\); the opposite inequality gives \(q\).  Computing
the determinantal divisors from integer SNF has polynomial bit complexity
for a polynomial-size, polynomial-bit matrix.  This part of F25 is correct.

### Non-additivity

The subgroup lemma in F25 is correct.  If a subgroup \(L\) is contained in
\(U\cup V\) but in neither branch, take
\(x\in L\setminus U\) and \(y\in L\setminus V\).  Containment puts
\(x\in V\) and \(y\in U\).  Membership of \(x+y\) in either \(U\) or
\(V\) would force the other chosen vector into the subgroup from which it
was excluded.  Thus \(x+y\notin U\cup V\), a contradiction.

In fact the useful symmetric difference does not contain zero, so no
additive lattice can equal it literally.  The lemma supports only the
claimed exact homogeneous-encoding obstruction.  It does not constrain the
output distribution of a larger lattice or a nonlinear postprocessor, as
F25 correctly acknowledges.

## 2. Primitive exact kernel and projected covolumes

Put

\[
\rho=\operatorname{rank}_{\mathbb Q}A,
\qquad
K_0=\ker_{\mathbb Z}A.
\]

The exact kernel is primitive: the quotient
\(\mathbb Z^d/K_0\) is isomorphic to the image \(A\mathbb Z^d\), a
torsion-free subgroup of \(\mathbb Z^t\).  Thus \(K_0\) has rank
\(d-\rho\).

Let \(\pi\) be orthogonal projection to
\((K_0\otimes\mathbb R)^\perp\) and let \(\Delta_0\) be the covolume of
\(K_0\) in its span.  Primitivity lets one lift a basis of
\(\pi(\mathbb Z^d)\) to a basis of \(\mathbb Z^d\) extending a basis of
\(K_0\).  Orthogonal volume decomposition then gives

\[
\det \pi(\mathbb Z^d)=\Delta_0^{-1}.
\]

Because \(K_0\subseteq K_r(A)\), projection induces

\[
\pi(\mathbb Z^d)/\pi(K_r(A))
\cong \mathbb Z^d/K_r(A).
\]

The report's clean display is therefore correct under its stated extra
assumption \(s_p=s_q=\rho\).

### Required common-rank correction

Equal local ranks need not equal rational rank.  If

\[
s_p=s_q=u\le \rho,
\]

then the projected lattices all have real rank \(\rho\), but their
covolumes are

\[
\det \pi(K_p)=\frac{p^u}{\Delta_0},\qquad
\det \pi(K_q)=\frac{q^u}{\Delta_0},\qquad
\det \pi(K_N)=\frac{N^u}{\Delta_0}.
\]

Their determinant-root scales are consequently

\[
p^{u/\rho}\Delta_0^{-1/\rho},\qquad
q^{u/\rho}\Delta_0^{-1/\rho},\qquad
N^{u/\rho}\Delta_0^{-1/\rho},
\]

not \(p,q,N\) times a common factor unless \(u=\rho\).  A shared-output
Hurwitz multiplication map can indeed have \(\rho=4\) and common local
rank two, so this is not an empty edge case.

This correction does not revive the advertised high-dimensional
amortization: \(\rho\le4\) for the scalar, Gram, and shared-output
quaternion maps in question.  Increasing the number of samples still adds
only exact rational-kernel directions.  It does, however, prevent the clean
full-rank formula from being presented as the complete equal-rank case.

The random-code determinant benchmarks in F25 are explicitly labelled
heuristics, not distribution theorems.  Their exponent bookkeeping is
correct for the stated surrogate.  They do not establish anything about the
actual Hurwitz sample distribution.

## 3. CVP syndrome invariance and its exact probability

For any \(v\in K_N(A)\), both \(Av\equiv0\pmod p\) and
\(Av\equiv0\pmod q\).  Hence, for \(e=t-v\),

\[
e\in K_r(A)\iff t\in K_r(A)
\qquad(r\in\{p,q\}).
\]

This holds regardless of how an exact or approximate CVP routine chooses
\(v\).  It is an exact coset invariant, so the CVP computation cannot
manufacture a zero local syndrome that the target did not already possess.

If \(t\) is uniform modulo \(N\), CRT makes its local residues independent.
Thus

\[
\Pr(t\in K_p)=p^{-s_p},\quad
\Pr(t\in K_q)=q^{-s_q},\quad
\Pr(t\in K_p\cap K_q)=p^{-s_p}q^{-s_q},
\]

and the symmetric-difference probability is exactly

\[
p^{-s_p}+q^{-s_q}-2p^{-s_p}q^{-s_q}.
\]

For balanced factors this is exponentially small in \(\log N\) when both
local ranks are positive.  The phrase “any positive local rank” should be
replaced by “both local ranks positive” or by the clean equal-positive-rank
case.  The zero-rank cases are exact:

- if \(s_p=0<s_q\), then \(A\equiv0\pmod p\), so
  \(K_p=\mathbb Z^d\), while a uniform target misses \(K_q\) with
  probability \(1-q^{-s_q}\).  This is the high-probability one-local event
  visible in the formula, but the same input is already factored
  deterministically by the rank-mismatch minor;
- the case \(s_q=0<s_p\) is symmetric;
- if \(s_p=s_q=0\), every entry of \(A\) is divisible by both \(p\) and
  \(q\), hence by \(N\).  Then
  \(K_p=K_q=K_N=\mathbb Z^d\), and the map supplies no proper syndrome.

Thus the uniform-target obstruction needed after rank-mismatch preprocessing
is precisely the common positive-rank case.

The argument applies only to targets uniform modulo \(N\), or to target
distributions whose local-syndrome probabilities are separately controlled.
F25 correctly leaves deliberately biased public target generation open.

## 4. Exact Hurwitz multiplication calculation

Assume \(N=pq\) with distinct odd primes and
\(\alpha\in\mathcal H\) has reduced norm \(N\).  Squarefreeness already
forces \(\alpha\) to be primitive: if \(\alpha=r\beta\) for a rational
prime \(r\), then \(r^2\mid\operatorname{nrd}(\alpha)\).

In a Hurwitz basis, left multiplication \(M_\alpha\) is integral and

\[
\det M_\alpha=N^2,
\qquad
Q(M_\alpha x)=NQ(x).
\]

For either \(r\in\{p,q\}\), the reduction of \(\alpha\) is nonzero.  The
odd-prime reduction of the Hurwitz order is \(M_2(\mathbb F_r)\), and
\(\det(\alpha)=0\) there.  Hence \(\alpha\) is a nonzero rank-one
\(2\times2\) matrix.  Left multiplication by such a matrix has rank two on
the four-dimensional matrix algebra.

It follows that exactly two Smith invariant factors of \(M_\alpha\) are
divisible by \(p\), and exactly two are divisible by \(q\).  The determinant
has valuation two at each prime and no other prime divisor.  The divisibility
chain in SNF therefore forces

\[
\operatorname{SNF}(M_\alpha)
=\operatorname{diag}(1,1,N,N).
\]

This reasoning also shows why the conclusion would require modification for
a non-squarefree norm or at the ramified prime two; those cases are outside
the stated local theorem.

### Local right ideals, orientation, and minima

The set

\[
J_r(\alpha)=\{x\in\mathcal H:\alpha x\in r\mathcal H\}
\]

is a right ideal: right multiplication preserves the defining condition.
The rank-two local multiplication calculation gives index \(r^2\).  The
Hurwitz order is one-sided norm-Euclidean, and hence has one-sided ideal
class number one, so this right ideal is of the form
\(d_r\mathcal H\).  The orientation in F25 is therefore correct.  Since

\[
[\mathcal H:d_r\mathcal H]
=\operatorname{nrd}(d_r)^2,
\]

one has \(\operatorname{nrd}(d_r)=r\).  Multiplicativity of norm and the
existence of Hurwitz units give

\[
\det J_r=r^2,
\qquad
\lambda_1(J_r)=\sqrt r.
\]

This uses the standard principality theorem for the Hurwitz order; a final
canonical proof should either cite that named fact explicitly or include its
short Euclidean-division proof.

For the public modulus,

\[
J_N(\alpha)=\{x:\alpha x\in N\mathcal H\}
=\bar\alpha\mathcal H.
\]

The nontrivial inclusion follows by writing
\(\alpha x=Ny=\alpha\bar\alpha y\) and cancelling nonzero \(\alpha\) in
the rational quaternion division algebra.  CRT also gives
\(J_N=J_p\cap J_q\).  Polarizing
\(Q(\bar\alpha y)=NQ(y)\) shows that the natural Gram matrix is exactly
\(N\) times the fixed Hurwitz Gram matrix.  Thus

\[
\det J_N=N^2,
\qquad
\lambda_1(J_N)=\sqrt N.
\]

All direct-sum determinant and minimum formulas in F25 follow immediately.
The local direct sums have determinant roots \(\sqrt p\) and
\(\sqrt q\); the public one has root \(\sqrt N\).  Adding blocks does not
improve these roots.

The standard \(\delta=3/4\) LLL bound
\(\|b_1\|\le2^{(4-1)/2}\lambda_1\) justifies the stated constant
\(2^{3/2}\).  If the other prime is greater than eight, such a local-basis
output is shorter than every nonzero public-intersection vector.  A basis of
the local ideal already exposes \(r\) through the square root of its index,
so invoking LLL after receiving that basis adds no factor-free information.

Finally, if \(x=\bar\alpha y\in J_N\cap r\mathcal H\), then
\(r^2\mid Q(x)=NQ(y)\), whence \(r\mid Q(y)\) and
\(Q(x)\ge Nr\).  This verifies the coordinate-divisibility lower bound and
the “small-prime cleanup” comparison with four-dimensional LLL.  It is a
claim about coordinate-gcd extraction from those short public vectors, not a
lower bound against arbitrary postprocessing.

## 5. Graph-lattice determinant and threshold

For integer weights \(a,b>0\), the variable-to-vector map defining

\[
\Gamma_{a,b}(A,N)
=\{(ax,b(Ax-Nz)):x\in\mathbb Z^d,z\in\mathbb Z^t\}
\]

has block-triangular basis

\[
\begin{pmatrix}
aI_d&0\\
bA&-bNI_t
\end{pmatrix}.
\]

Therefore

\[
\det \Gamma_{a,b}=a^d(bN)^t.
\]

For \(d=t=4\), its determinant root in dimension eight is
\(\sqrt{abN}\), and direct sums preserve that root.  Clearing fixed rational
weights first merely renames the resulting integer weights and does not
alter the argument.

For one Hurwitz multiplication block and \(z=0\), norm similarity gives

\[
a^2Q(x)+b^2Q(M_\alpha x)
=(a^2+b^2N)Q(x).
\]

Thus a nonzero \(x\in J_r\) is at least \(\sqrt r\) times as long as a
unit input in this unwrapped slice.  With wrapping, the residual
\(s=M_\alpha x-Nz\) of a local-kernel input belongs to \(r\mathcal H\);
if nonzero, \(Q(s)\ge r^2\).  Consequently, any regime that separately
forces residual Hurwitz length below \(r\) forces \(s=0\), hence the public
intersection.

These exact statements are correct.  The prose above the threshold should
remain a lack-of-guarantee statement: it does not prove that every choice of
weights, target, affine shift, or postprocessor fails.  In particular, the
counting sentence about spacing and density is heuristic intuition and
should not be promoted as an unbounded distribution theorem.

## 6. Gram construction: what is proved and what remains open

With positive-definite rational Gram matrix \(T\),

\[
G=C^{\mathsf T}TC
\]

satisfies

\[
\ker_{\mathbb Q}G=\ker_{\mathbb Q}C,
\qquad
\operatorname{rank}_{\mathbb Q}G
=\operatorname{rank}_{\mathbb Q}C\le4,
\qquad
c^{\mathsf T}Gc=Q(Cc).
\]

Positive definiteness is essential for the first equality and is available
here.  A semidefinite SVP formulation in coefficient space has the exact
kernel \(K_0\); quotienting it leaves a metric lattice of rank at most four.
Likewise, the linear modular kernel of \(G\) obeys the Construction-A
formulas with its own local ranks, which may be smaller than the rank of
\(C\) because isotropic reduction can create additional degeneracy.

The set defined only by \(Q(Cc)\equiv0\pmod r\) is a quadric, not a
linear kernel.  The report correctly identifies that a linear lift
\(Z=cc^{\mathsf T}\) must retain its rank-one constraint; dropping it is a
relaxation, and enforcing it restores a nonlinear condition.

What does **not** follow is failure of every Gram-metric decoder.  Since the
quotient rank is at most four, exact SVP/CVP on the quotient metric is
fixed-dimensional once a faithful quotient instance is constructed.  The
report proves that there is no *dimension-amortized determinant advantage*;
it does not prove that a specified shortest or closest quotient vector can
never have \(p\)-only or \(q\)-only divisibility.  Such a decoder still
needs a distribution and extraction theorem, but it remains an open
possibility rather than a refuted one.

### Public primal and dual lattices omitted from the scope claim

Two canonical public lattices associated with \(A\) are

\[
\Lambda_{\rm out}(A,N)
=A\mathbb Z^d+N\mathbb Z^t
\]

and

\[
\Lambda_{\rm dual}(A,N)
=N K_N(A)^*
=N\mathbb Z^d+A^{\mathsf T}\mathbb Z^t.
\]

The dual identity follows because every
\(z+(1/N)A^{\mathsf T}y\) pairs integrally with \(K_N(A)\), and equality
of indices follows from Smith normal form.  Both lattices are computable
without knowing \(p\) or \(q\).  They are respectively the output
Construction-A lattice and the scaled dual of the kernel Construction-A
lattice.

In the equal-rank case their Smith invariants do not automatically reveal a
factor: CRT aligns equal numbers of \(p\)- and \(q\)-torsion components into
\(N\)-components.  But their *geometry* is not covered by the statement that
vectors of \(K_N\) satisfy both local zero conditions.  Vectors in these
lattices generally are not vectors of \(K_N\).  A metric algorithm on them
could only be ruled out by an additional shortest-vector, target-distribution,
or quotient-shape theorem.

These two lattices are not presently counterexamples to the narrow F25
obstruction, and this audit does not prove that either factors \(N\).  They
are untested standard formulations.  They *are* counterexamples to a literal
universal reading of “every public construction gives the intersection” or
“LLL on a public lattice returns a vector satisfying both local kernels.”
For example, with the scalar matrix \(A=(1)\),
\(K_N(A)=N\mathbb Z\) but
\(N K_N(A)^*=\mathbb Z\); its shortest vector \(1\) is not in either
zero-syndrome kernel.  This example reveals no factor—it only shows why the
intersection/coset proof cannot be transferred to the dual formulation.

For the single Hurwitz multiplication block, the similarity
\(J_N=\bar\alpha\mathcal H\) strongly suggests no hidden \(p/q\) shape in
its dual either: its dual is, up to the fixed codifferent/Gram convention,
the inverse similarity of a fixed lattice.  That verifies the single-block
intuition.  It does not supply the missing theorem for arbitrary scalar,
Gram, or multi-sample output lattices.

Thus F25 may say that its analyzed kernel, block, and graph formulations
fail to produce a one-local syndrome.  It may not say that all canonical
public linear/Gram lattices, or all HNF/SNF/LLL uses of them, have been
closed.

## 7. Relation to P19 and P30

The comparison with P19 is accurate.  P19's exact CVP instance encodes a
public nonlinear multiplication disjunction through one-hot variables and
has an additive squared-distance gap of eight after integral scaling.  F25
instead posits a large local/intersection metric ratio, but the shorter
local branch lattice is unavailable.  Neither theorem supplies a
polynomial-time exact-CVP algorithm for the other construction.

The comparison with P30 is also correctly scoped.  More than four scalar
samples can have abundant local linear dependencies without any pairwise
projective collision, so P30's birthday bound is not a lower bound on this
many-sample decoder.  F25 supplies a deterministic obstruction to the
specific zero-syndrome linear-lattice formulation.  It does not extend
P30's distribution theorem to mixed nonlinear combinations, and it does not
derive biased targets from P30.

## 8. Bit complexity and quantifiers

For \(m\le n^c\) and \(O(n)\)-bit sample coordinates, all displayed matrices
have polynomial dimensions and polynomial-bit entries.  The determinant
bit bounds in F25 are correct:

- \(\log\det K_N(C)\le4\log N\) because each local rank is at most four;
- the block determinant \(N^{2m}\) has \(O(m\log N)\) bits;
- graph-lattice determinants have polynomial bit length for polynomial-bit
  weights.

Integer HNF/SNF, kernel bases, rational projection matrices, LLL, gcd,
reduced norm, and division verification are polynomial-bit operations on
these inputs.  Exact CVP in growing dimension is not included in that list
and must not be silently treated as polynomial; F25 does not do so.

The symbolic failures are established already on distinct balanced odd
semiprimes.  That is sufficient to kill the proposed route as an all-input
factoring algorithm, but it is not a theorem about non-squarefree norms,
even inputs, or arbitrary composites.  Since no factoring algorithm survives,
there is no missing recursion or prime-power runtime proof to audit.

## Required corrections to the candidate artifact

Before promotion or blind reconstruction, the candidate should:

1. replace the clean projected determinant discussion by the general
   \((\rho,u)\) formula above, while retaining the clean full-rank formula
   as a corollary;
2. change the uniform-target claim to require both local ranks positive,
   noting that unequal ranks are already deterministically separated;
3. narrow “method failure for Gram” to failure of the high-dimensional
   exact-kernel/determinant-root amortization and of the explicitly analyzed
   linear modular kernel;
4. explicitly leave the public output lattice, scaled dual lattice, and
   fixed-rank quotient metric decoder open unless a new theorem analyzes
   their outputs;
5. keep the graph-lattice above-threshold and coordinate-spacing discussion
   as absence of a success guarantee, not an impossibility result; and
6. cite or prove one-sided principality of the Hurwitz order when promoting
   the ideal-minimum statement.

With those corrections, the surviving theorem is:

> Public zero-syndrome Construction A over \(N=pq\) gives the CRT
> intersection, CVP subtraction from that lattice preserves both local
> syndromes, shared-output maps have only constant informative quotient
> rank, and Hurwitz multiplication blocks/direct sums have exact local
> minima \(\sqrt p,\sqrt q\) but public minimum \(\sqrt N\).  Hence merely
> adding norm-\(N\) samples and applying HNF/SNF/LLL/CVP to the displayed
> kernel/intersection constructions does not realize the proposed
> high-dimensional hidden-branch decoder.

## Final disposition

**PASS WITH CORRECTIONS.**

The required revision changes determinant exponents and the mathematical
scope of the claimed method failure, so a **fresh hostile re-audit is
required after revision**.  Strict proof-blind reconstruction is warranted
only if that corrected version passes the fresh audit.  The original broader
claim that the Gram and canonical public-lattice formulations are closed
should not be sent to reconstruction or promoted.
