# Proof of the F146 boundary

## 1. Exchange identity

Work first over a commutative ring in which \(\det B\) is a unit.  Then

\[
[B\mid T]=B[I_A\mid C],\qquad C=B^{-1}T.
\]

Fix equal-size sets \(I\subseteq[A]\) and \(J\subseteq[t]\).  Form the
selected \(A\)-column matrix by retaining the base columns outside \(I\) and
adding the tail columns in \(J\).  Factor \(B\) on the left.  Expansion along
the unchanged identity columns leaves exactly the submatrix \(C[I,J]\).
Therefore

\[
\det E_{I,J}=\varepsilon(I,J)\det(B)\det C[I,J],
\qquad \varepsilon(I,J)\in\{1,-1\}.
\]

The sign is fixed by the chosen column order and is irrelevant to zero
status.  Since \(\det B\) is a unit modulo \(N\), multiplication by it does
not change the gcd with \(N\).  Hence a proper gcd occurs exactly when this
exchange is a basis modulo some, but not all, prime divisors of \(N\).

This also identifies the exact progress parameter:

\[
\delta_B=
\min\{\,|I|:
\det C[I,J]\text{ is zero in some but not all local fields}\,\}.
\]

The support-\(s\) scan succeeds exactly when \(\delta_B\le s\).

## 2. Count and bit complexity

For support \(k\), choose the \(k\) removed columns and the \(k\) inserted
columns independently.  The count is

\[
\binom Ak\binom tk.
\]

Summing gives the stated exact value \(Q_s(A,t)\).  If \(A,t\le n^c\), then

\[
Q_s(A,t)
\le(s+1)(At)^s
\le(s+1)n^{2cs}.
\]

For \(s\le(\log(n+1))^d\), its base-two logarithm is

\[
O(s\log(n+1))
=O((\log(n+1))^{d+1}).
\]

The standard AKS parameter bounds give \(A,r=n^{O(1)}\).  The global error
matrix is therefore formed in polynomial bit complexity.  First compute
\(\det B\).  A proper gcd already factors \(N\).  On the unit branch, compute
the inverse and \(C=B^{-1}T\) with polynomially many ring operations.  One
can use adjugate or division-free characteristic-polynomial methods, so no
unproved pivot choice is needed.  Each retained determinant has dimension at
most \(s\), and a division-free algorithm uses a polynomial number of ring
operations.  Modular reduction keeps every ring element at \(O(n)\) bits.
Multiplying this polynomial cost by \(Q_s(A,t)\) proves the
quasipolynomial bound.

If \(t\le s\), every \(A\)-column subset contains at most \(t\) tail columns.
It is therefore one of the scanned exchanges.  This proves completeness for
the full column matroid on the common-unit-base branch.

For the prime-modulus corollary, put

\[
L=\log_2N,\qquad x=\sqrt{r-1},\qquad u=r-1-L^2>0.
\]

Since \(\lfloor Lx\rfloor>Lx-1\),

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

Hence a polylogarithmic excess \(u\) gives a polylogarithmic tail and the
complete scan has the preceding quasipolynomial bound.

## 3. Arbitrarily delayed disagreement

Fix \(s\ge1\) and put \(d=s+1\).  Define integer matrices

\[
U\in\mathbb Z^{d\times s},\qquad U_{ih}=i^h,
\]

and

\[
V\in\mathbb Z^{s\times d},\qquad V_{hj}=j^h,
\]

where \(1\le i,j\le d\) and \(0\le h\le s-1\).  Put

\[
D=UV.
\]

For increasing positive evaluation points, every minor of a generalized
Vandermonde matrix is positive.  This follows from the usual Vandermonde
factor times a Schur polynomial with positive integer coefficients.

For row and column sets \(I,J\) of size \(k\le s\), Cauchy--Binet gives

\[
\det D[I,J]
=\sum_{K\subseteq[s],\ |K|=k}
\det U[I,K]\det V[K,J].
\]

Each summand is positive.  Hence every square minor of \(D\) of order at most
\(s\) is a positive integer.  Both \(U\) and \(V\) have rank \(s\), \(U\) is
injective, and \(V\) is surjective over \(\mathbb Q\).  Thus \(D\) has rank
\(s\), and

\[
\det D=0.
\]

For the other field, use the square Vandermonde matrix

\[
E_{ij}=i^{j-1},\qquad1\le i,j\le d.
\]

Every square minor of \(E\) is a positive integer, including \(\det E\).

All entries of \(D\) are at most

\[
s d^{2s}.
\]

The same quantity bounds the entries of \(E\).  By the Leibniz formula, every
square minor of either matrix has absolute value at most

\[
H_s=d!\bigl(s d^{2s}\bigr)^d.
\]

Choose a prime \(q\) with

\[
H_s<q<2H_s
\]

and then a prime \(p\) with

\[
q<p<2q.
\]

Two applications of Bertrand's postulate supply the primes.  They are
distinct and satisfy \(q<p<2q\).  Reduction
modulo \(q\) preserves the nonzero status of every proper minor of \(D\), but
its full determinant stays zero.  Reduction modulo \(p\) preserves the
nonzero status of every minor of \(E\).

Let \(N=pq\).  Entrywise CRT gives a matrix

\[
C\in(\mathbb Z/N\mathbb Z)^{d\times d}
\]

such that

\[
C\equiv E\pmod p,
\qquad
C\equiv D\pmod q.
\]

Finally put

\[
M_N=[I_d\mid C].
\]

Every exchange of \(k\le s\) base columns has determinant, up to sign, equal
to a \(k\)-by-\(k\) minor of \(C\).  It is nonzero in both fields.  The one
exchange of support \(d=s+1\) replaces the complete identity base with the
complete tail.  Its determinant is nonzero modulo \(p\) and zero modulo
\(q\).  Thus the first local matroid disagreement has exchange support
exactly \(s+1\).

Lastly,

\[
\log H_s=\Theta(s^2\log(s+1)).
\]

The chosen primes lie between constant multiples of \(H_s\), so

\[
n=\lceil\log_2(N+1)\rceil
=\Theta(s^2\log(s+1)).
\]

It follows that \(s\) grows faster than every fixed power of \(\log n\).
This proves the claimed asymptotic obstruction for the displayed matrix.

There is also a dimension-preserving padding.  After \(N\), hence \(n\), is
fixed, set

\[
A=n^2,\qquad r=A+d.
\]

Extend \(C\) to an \(A\)-by-\(d\) matrix \(\widetilde C\) by putting \(C\) in
its first \(d\) rows and zeros in all later rows.  Use

\[
\widetilde M_N=[I_A\mid\widetilde C].
\]

An exchange determinant is, up to sign, a square minor
\(\widetilde C[I,J]\).  If \(I\) contains a padded row, this determinant is
zero in both fields.  If \(I\subseteq[d]\), it is one of the original minors
of \(C\).  Thus all exchanges through support \(s\) still agree, while the
support-\(d\) exchange on the first \(d\) rows still differs.  The padded
dimensions satisfy \(A,r=n^{O(1)}\), \(r-A=s+1\), and \(r/A\to1\).

## 4. Random-scale calibration of P11

For a uniform \(k\)-by-\(k\) matrix over \(\mathbb F_\ell\), the nonsingular
probability is

\[
\prod_{i=1}^k(1-\ell^{-i}).
\]

At \(k=1\), the zero probability is \(1/\ell\).  At \(k=2\), it is

\[
z_\ell=\ell^{-1}+\ell^{-2}-\ell^{-3}.
\]

For independent local random matrices, one fixed minor has a zero-pattern
mismatch with probability

\[
z_p(1-z_q)+(1-z_p)z_q
=z_p+z_q-2z_pz_q.
\]

Linearity of expectation does not require independence between different
minors.  Multiplication by the exact P11 family sizes gives the numerical
expectations in the statement.  They are scale comparisons only.  No random
model is asserted for the AKS coefficient matrix.

For a balanced semiprime, \(p,q=2^{\Theta(n)}\).  If a family of
quasipolynomially many determinant residues has only uniform-scalar
divisibility, a union bound gives

\[
2^{(\log n)^{O(1)}}(p^{-1}+q^{-1})
=2^{-\Theta(n)+o(n)}.
\]

Therefore a successful F04 continuation needs an arithmetic concentration
or a deterministic hitting theorem.  Candidate count alone is not enough.
