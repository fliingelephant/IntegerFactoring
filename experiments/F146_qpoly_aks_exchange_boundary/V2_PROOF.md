# Proof of F146 V2

## 1. Exchange identity and exact gcd scope

Because \(\gcd(\det B,N)=1\), the determinant is a unit in
\(\mathbb Z/N\mathbb Z\). Thus

\[
[B\mid T]=B[I_A\mid C],
\qquad C=B^{-1}T.
\]

Fix equal-size sets \(I\subseteq[A]\) and \(J\subseteq[t]\). Factor \(B\)
from the selected \(A\)-column matrix. Expansion along the retained identity
columns gives

\[
\det E_{I,J}
=\varepsilon(I,J)\det(B)\det C[I,J].
\]

Multiplication by the unit \(\varepsilon(I,J)\det B\) preserves the gcd with
\(N\). Therefore

\[
\gcd(\det E_{I,J},N)
=\gcd(\det C[I,J],N).
\]

The definition of \(\gamma_B\) now gives the exact scan-success equivalence
for every composite \(N\).

If a determinant is zero modulo one prime divisor \(\ell\mid N\) and nonzero
modulo another prime divisor, its gcd with \(N\) is divisible by \(\ell\)
but is not divisible by every prime-power factor of \(N\). The gcd is
proper. Hence

\[
\delta_B\le s\quad\Longrightarrow\quad\gamma_B\le s
\]

for arbitrary composite \(N\).

Equivalently, \(\gamma_B\le\delta_B\), with the convention that either
radius can be infinite.

Now assume that \(N\) is squarefree. A determinant gcd is 1 exactly when
the determinant is nonzero modulo every prime divisor. The gcd is \(N\)
exactly when it is zero modulo every prime divisor. Thus the gcd is proper
exactly when its local zero status differs between prime divisors. Therefore

\[
\gamma_B=\delta_B
\]

for squarefree \(N\).

The converse fails without squarefreeness. For example, \(N=45\) and the
one-by-one determinant 15 give a proper gcd although the determinant is zero
modulo both distinct prime divisors. V2 treats such valuation-only events as
additional gcd successes.

## 2. Count and bit complexity

For support \(k\), choose the \(k\) removed base columns and the \(k\)
inserted tail columns. The exact count is

\[
\binom Ak\binom tk.
\]

Summing gives \(Q_s(A,t)\). If \(At\ge1\), every summand is at most
\((At)^s\), so

\[
Q_s(A,t)\le(s+1)(At)^s.
\]

If \(t=0\), only \(k=0\) occurs and \(Q_s(A,0)=1\). Both cases are covered
by

\[
Q_s(A,t)\le(s+1)\max\{1,At\}^s.
\]

If \(A,t\le n^c\) and \(s\le(\log(n+1))^d\), then

\[
\log_2 Q_s(A,t)
=O(s\log(n+1))
=O((\log(n+1))^{d+1}).
\]

The standard AKS parameter bounds give \(A,r=n^{O(1)}\), so the global error
matrix has polynomial construction cost. On the unit-base branch, compute
\(C=B^{-1}T\) with polynomially many ring operations. Adjugate or
division-free characteristic-polynomial methods avoid an unproved pivot
choice. A retained \(k\)-by-\(k\) determinant has \(k\le s\), so each test
has polynomial cost in \(n\) and \(s\). Modular reduction keeps operands at
\(O(n)\) bits. The total cost is quasipolynomial.

If \(t\le s\), every \(A\)-column subset contains at most \(t\) tail columns,
so every maximal minor occurs in the scan. The unit base fixes local rank
\(A\). Thus a local column-matroid mismatch is found. On squarefree inputs,
the preceding equivalence also shows that the complete maximal-minor gcd scan
succeeds exactly when the local column matroids differ. On non-squarefree
inputs, valuation-only gcd successes can occur even when their residue-field
matroids agree.

## 3. Near-threshold prime modulus

Put

\[
L=\log_2N,\qquad
x=\sqrt{r-1},\qquad
u=r-1-L^2>0.
\]

For \(A=\lfloor Lx\rfloor\),

\[
\begin{aligned}
r-A
&<r-Lx+1\\
&=(r-1-Lx)+2\\
&=x(x-L)+2\\
&=\frac{x}{x+L}u+2\\
&<u+2.
\end{aligned}
\]

A polylogarithmic positive excess \(u\) therefore gives a polylogarithmic
tail. Section 2 then gives the complete quasipolynomial scan.

## 4. Arbitrarily delayed disagreement

Fix \(s\ge1\) and put \(d=s+1\). Define

\[
U_{ih}=i^h,\qquad
V_{hj}=j^h,
\]

where \(1\le i,j\le d\) and \(0\le h\le s-1\). Put \(D=UV\).

Every generalized Vandermonde minor on increasing positive points and
increasing exponents is positive. For row and column sets \(I,J\) of size
\(k\le s\), Cauchy--Binet gives

\[
\det D[I,J]
=\sum_{K\subseteq[s],\ |K|=k}
\det U[I,K]\det V[K,J]>0.
\]

Both \(U\) and \(V\) have rank \(s\). Since \(U\) is injective and \(V\)
is surjective over \(\mathbb Q\), \(D\) has rank \(s\). Hence

\[
\det D=0.
\]

For the other field, use

\[
E_{ij}=i^{j-1},
\qquad1\le i,j\le d.
\]

Every square minor of \(E\) is a positive generalized Vandermonde
determinant.

The entries of \(D\) and \(E\) are at most \(s d^{2s}\). The Leibniz
formula bounds every square minor by

\[
H_s=d!\bigl(s d^{2s}\bigr)^d.
\]

Bertrand's postulate gives primes

\[
H_s<q<2H_s,
\qquad q<p<2q.
\]

Reduction modulo \(q\) preserves every nonzero proper minor of \(D\), while
its full determinant remains zero. Reduction modulo \(p\) preserves every
minor of \(E\). Entrywise CRT gives

\[
C\equiv E\pmod p,
\qquad C\equiv D\pmod q.
\]

In

\[
M_N=[I_d\mid C],
\qquad N=pq,
\]

every exchange through support \(s\) is a basis in both fields. The complete
support-\(d\) exchange is a basis modulo \(p\) and dependent modulo \(q\).
Thus the first local disagreement has support \(s+1\).

Moreover,

\[
\log H_s
=\Theta(s^2\log(s+1)),
\]

and both primes are within constant factors of \(H_s\). Therefore

\[
n=\lceil\log_2(N+1)\rceil
=\Theta(s^2\log(s+1)).
\]

It follows that \(s\) eventually exceeds every fixed power of \(\log n\).

For the padded version, set \(A=n^2\), append zeros below \(C\) to make an
\(A\)-by-\(d\) tail, and use the base \(I_A\). An exchange minor involving
a padded row is zero in both fields. A minor supported in the first \(d\)
rows has its old status. The first disagreement therefore remains at
support \(d=s+1\), while

\[
r=A+d,\qquad r/A\to1.
\]

This proves the general-matrix obstruction. The construction is not an AKS
error matrix.

## 5. Random-scale calibration of P11

For a uniform \(k\)-by-\(k\) matrix over \(\mathbb F_\ell\), the nonsingular
probability is

\[
\prod_{i=1}^k(1-\ell^{-i}).
\]

For \(k=2\), the singularity probability is

\[
z_\ell=\ell^{-1}+\ell^{-2}-\ell^{-3}.
\]

For independent local random matrices, one fixed minor has mismatch
probability

\[
z_p+z_q-2z_pz_q.
\]

Linearity of expectation does not require independence between different
minors. Multiplication by the P11 family sizes gives the values in the
statement. This is only a scale comparison.

For balanced semiprimes, \(p,q=2^{\Theta(n)}\). A quasipolynomial family
with uniform-scalar divisibility has union-bound success at most

\[
2^{(\log n)^{O(1)}}(p^{-1}+q^{-1})
=2^{-\Theta(n)+o(n)}.
\]

Thus a successful F04 continuation needs an AKS-specific arithmetic
concentration or deterministic hitting theorem. Candidate count alone is
not sufficient.
