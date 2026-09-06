# Proof of the F200 candidate

## 1. Range and the unique exceptional denominator

The balance assumptions give

\[
p\leq B<q,\qquad B<2p.
\tag{1}
\]

The adjacent-binomial identity from P171 is

\[
j(A_j-A_{j-1})=-NA_{j-1}.
\tag{2}
\]

Rearranging (2) gives

\[
{A_{j-1}\over j}={A_{j-1}-A_j\over N}.
\tag{3}
\]

If \(j\neq p\), then \(\gcd(j,N)=1\) by (1).  Equation (2) says that
\(j\mid NA_{j-1}\), so Euclid's lemma gives \(j\mid A_{j-1}\).  Hence
\(x_j=A_{j-1}/j\) is an integer.

At \(j=p\), P171 gives \(A_{p-1}\equiv1\pmod N\).  Thus, for an integer
\(g\),

\[
A_{p-1}=1+Ng=1+pqg,
\]

and

\[
x_p={1\over p}+qg\in\mathbb Z+{1\over p}.
\tag{4}
\]

The numerator \(A_{p-1}\) is one modulo \(p\), so (4) is in lowest terms
at \(p\).  This proves the delta identity in \(\mathbb Q/\mathbb Z\).

For a subset \(I\), equation (3) proves that \(D_I=NS_I\) is an integer.
If \(p\notin I\), then \(S_I\) is an integer and \(D_I\equiv0\pmod N\).
If \(p\in I\), then (4) gives \(S_I=m+1/p\) for an integer \(m\), so

\[
D_I=Nm+q\equiv q\pmod N.
\tag{5}
\]

The gcd assertions follow from (5).  In the product over \(I\), the only
integer not exceeding \(B\) that is divisible by either hidden prime is
\(p\).  This proves the product assertion.

For \(I=[a,b]\), summing (3) telescopes:

\[
S_I={1\over N}\sum_{j=a}^{b}(A_{j-1}-A_j)
={A_{a-1}-A_b\over N}.
\tag{6}
\]

## 2. The floor identity

For the root interval, (6) and \(A_0=1\) give

\[
S_{[1,B]}={1-A_B\over N}.
\tag{7}
\]

The definition \(A_B=Nh+1-q\) turns (7) into

\[
S_{[1,B]}={q-Nh\over N}={1\over p}-h.
\tag{8}
\]

Since \(0<1/p<1\), equation (8) gives

\[
\lfloor S_{[1,B]}\rfloor=-h.
\]

Equation (4) gives the general active-interval floor assertion.  Embedding
the rational \(1/p\) into \(\mathbb Z_2\) and reducing modulo \(2^t\)
gives \(p^{-1}\bmod2^t\), exactly P175's hidden reciprocal.

## 3. Transform geometry

In any additive coefficient group, the transform of a point mass is the
corresponding character value at every frequency.  Here the point mass has
value \(1/p\).  Walsh characters take values \(\pm1\), so every Walsh
coefficient is \(\pm1/p\) and is nonzero in \(\mathbb Q/\mathbb Z\).

For the ordinary discrete Fourier transform, the same calculation gives a
root of unity times \(1/p\).  A root of unity is an algebraic unit, so its
quotient by \(p\) is not an algebraic integer.  Every coefficient is
therefore nonzero modulo the cyclotomic integer ring.

An unnormalized Haar wavelet is \(+1\) on one child interval and \(-1\) on
the other.  It pairs to zero with the delta unless its parent interval
contains \(p\).  At each scale exactly one parent contains \(p\), and the
coefficient there is \(+1/p\) or \(-1/p\).  This proves all three transform
claims.

Under a cyclic Fourier transform, one difference multiplies a coefficient
by \(\zeta_M^{sh}-1\), up to the direction convention.  Iteration gives
the displayed product.  If \(M\) is a power of two and \(h\) is odd, then
\(\zeta_M^{sh}=1\) only for \(s=0\pmod M\).  Hence every nonzero frequency
survives.  For the rational point mass
\(v_j=p^{-1}\mathbf1_{j=p}\),

\[
\sum_jv_jv_{j+h}=p^{-2}\mathbf1_{h=0}.
\]

The location cancels from this translation-averaged correlation.  These
claims do not cover nontranslation-invariant or nonlinear weighted
correlations.

For an odd index \(j\), inversion is a permutation modulo \(2^t\).  Thus
\(j^{-1}\equiv a\pmod {2^t}\) is the single arithmetic progression
\(j\equiv a^{-1}\pmod {2^t}\).  Only \(j=p\) contributes in
\(\mathbb Q/\mathbb Z\), so the residue-cell vector is a point mass at
\(a=p^{-1}\bmod2^t\).  Its Walsh transform is full by the preceding point-
mass calculation.

## 4. The multiscale gauge symmetry

For a parent \(v=v_0\sqcup v_1\), additivity gives

\[
s_v=s_{v_0}+s_{v_1}.
\tag{9}
\]

Also, for every fixed leaf \(\ell\),

\[
\mathbf1_{\ell\in v}
=\mathbf1_{\ell\in v_0}+\mathbf1_{\ell\in v_1}.
\tag{10}
\]

Subtracting \(u\) times (10) from (9) proves the claimed additivity of
\(c^{(\ell,u)}\).  Surjectivity of
\(\mathbb Z\to\mathbb Z/2^t\mathbb Z\) supplies an integer representative
for every leaf residue; summing those representatives supplies an exactly
additive integer labelling of the internal nodes.

For the true \(\ell=p\) and \(u=p^{-1}\), Theorem 1 says precisely that
the corrected values are the reductions of the ordinary integer parts.
For a false leaf they are only formal integer labels.  Additivity cannot
distinguish these cases because equations (9)--(10) hold identically for
every leaf.  Haar and Walsh transforms are invertible linear changes of the
same data and preserve this feasibility symmetry.

At precision \(t\) below P175's quarter threshold, \(2^t\leq N^{1/4}\).
The public balanced interval for \(p\) has length
\[
\lfloor\sqrt N\rfloor-\sqrt{N/2}+O(1)=\Theta(\sqrt N).
\]
For all sufficiently large \(N\), this length exceeds \(2^{t+1}\).
Hence each of the two odd residue classes supplied by the next reciprocal
lift has a representative in the balanced interval.  Public cell emptiness
does not break the symmetry in this range.

## 5. Endpoint accounting

Using (3),

\[
N\sum_{j=1}^{B}w_jx_j
=\sum_{j=1}^{B}w_j(A_{j-1}-A_j).
\]

Collect the coefficient of each \(A_j\).  The result is

\[
w_1A_0+\sum_{j=1}^{B-1}(w_{j+1}-w_j)A_j-w_BA_B.
\tag{11}
\]

Only the two boundaries and the adjacent changes of \(w\) occur.  The
power-of-two binomial interface already audited in P173 evaluates each
chosen \(A_j\bmod2^t\) after QP preprocessing.  Thus (11) is a QP
evaluator when the number of changes is QP.

An interval indicator has two changes.  The exact support test is still
\(\gcd(D_I,N)\), which factors by Theorem 1.

A nonempty residue class modulo \(2^t\) contributes one isolated run per
occurrence.  Its number of occurrences is

\[
{B\over2^t}+O(1).
\tag{12}
\]

At the P175 threshold, \(2^t=N^{1/4}/2^{(\log n)^{O(1)}+O(1)}\), while
\(B=N^{1/2}+O(1)\).  Substitution in (12) gives

\[
{B\over2^t}
=N^{1/4}2^{(\log n)^{O(1)}+O(1)},
\]

which is \(2^{\Omega(n)}\).  Literal use of (11) is therefore not QP.
The same count is the reciprocal of the uniform probability of sampling
the one exceptional index from its correct residue cell.

## 6. Local continuity and high-order characters

For a public modulus \(M\), a proper value of \(\gcd(M,N)\) already
factors.  On the factor-free branch \(\gcd(M,N)=1\), \(N\), \(p\), and
\(q\) are units modulo \(M\).
The rational localization \(\mathbb Z[1/N]\) therefore reduces to
\(\mathbb Z/M\mathbb Z\), and \(1/p\) reduces to \(p^{-1}\).  Every residue
modulo \(M\), including this one, is the reduction of an ordinary integer.
Taking a finite direct product changes none of these statements.
If \(N\mid M\), the unit argument does not apply; this is explicitly left
as the original composite-characteristic evaluation gate.

Every class modulo \(2^t\) contains an ordinary integer.  A predicate of
that class which accepts the reductions of all integers must accept every
class.  The inverse-limit version follows because ordinary integers are
dense in \(\mathbb Z_2\): the inverse image of a separating open set would
be an open neighbourhood disjoint from a dense set.  Uniformly convergent
Mahler series define continuous functions, so they inherit this boundary.

For an ordinary character, Theorem 1 gives

\[
e^{2\pi i mS_I}
=1\quad(p\notin I),
\qquad
e^{2\pi i mS_I}=e^{2\pi i m/p}\quad(p\in I).
\tag{13}
\]

The elementary bound \(|e^{i\theta}-1|\leq|\theta|\) gives

\[
\left|e^{2\pi i m/p}-1\right|\leq {2\pi|m|\over p}.
\]

Balance gives \(p=2^{\Theta(n)}\).  Hence a numerical-QP frequency has
exponentially small, rather than inverse-QP, separation.

As \(m\) ranges uniformly over \(0,\ldots,N-1\), its residue modulo \(p\)
is exactly uniform because \(N=pq\).  A constant fraction of the \(p\)-th
roots in (13) stay a fixed positive distance from one.  Thus the abstract
phase has constant distinguishing bias.

On the other hand, (5) gives

\[
e^{2\pi i mS_I}=e^{2\pi i mD_I/N}.
\tag{14}
\]

If \(\gcd(m,N)=1\), the right side is one exactly when \(N\mid D_I\),
which by Theorem 1 is exactly when \(p\notin I\).  Exact phase support on
the two children therefore selects the child containing \(p\).  Repeating
through a dyadic partition finds \(p\), and exact division verifies it.
This proves that the missing phase evaluator is itself a factoring
primitive, rather than a consequence of transform sparsity.

Finally, let \(K/\mathbb Q_2\) contain a primitive \(p\)-th root of unity.
Because \(p\) is odd, prime-to-two roots of unity reduce injectively into
the residue field \(\mathbb F_{2^f}^{\times}\), where \(f\) is the residue
degree.  Hence

\[
p\mid 2^f-1,
\qquad \operatorname{ord}_p(2)\mid f.
\]

The total extension degree is at least \(f\).  This proves the stated
small-degree representation boundary on a branch where
\(\operatorname{ord}_p(2)\) exceeds the chosen QP cap.
In the beta-two P159--P161 normalization, the final rough element is
\(w=2^E\) for a public exponent \(E\), and
\(\operatorname{ord}_p(w)\mid\operatorname{ord}_p(2)\).  Thus
\(\operatorname{ord}_p(w)>T\) implies the required
\(\operatorname{ord}_p(2)>T\).

## 7. What is and is not closed

The theorem proves exact obstructions for:

- locating the defect by finite 2-adic integrality;
- locating it by any value-local factor-free auxiliary residue;
- selecting a path by additive dyadic consistency;
- hoping that the singleton has sparse Walsh or Fourier support;
- materializing residue-prefix cells through endpoint summation; and
- representing the required odd-torsion phase in a small 2-adic extension
  on the corresponding high-order branch.

It proves no lower bound against a nonlinear statistic of the actual
integer parts, a new implicit phase algorithm, an Archimedean algorithm
that computes fractional parts without materializing the binomial, or an
arbitrary succinct arithmetic circuit.
