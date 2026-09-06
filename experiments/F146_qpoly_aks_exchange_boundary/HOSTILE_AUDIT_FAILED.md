# F146 hostile audit — failed as frozen

## Frozen inputs and method

I audited the complete proof-only candidate with hashes

- `STATEMENT.md`:
  `0cc469a3e44393ed6ec28517b3de0c3b64b8cb473fe37d9835c4f220168bb257`;
- `PROOF.md`:
  `0c89b48f29979b3b0d0d8bdbae76d0b2bdecefdf9445d9cda87f923b7344d007`.

Both hashes matched `MANIFEST.md` before the audit. I did not modify either
frozen file. I used no research computation. The numerical P11 discussion was
checked against the already promoted P24 artifacts, not by a new run.

## Verdict

**FAIL as frozen, but narrowly repairable.** The exchange identity, the
quasipolynomial scan cost, the near-threshold tail estimate, and the explicit
CRT/Vandermonde delayed-disagreement family all survive. The frozen proof has
one false exact claim on its stated domain of arbitrary composite \(N\):

> a proper determinant gcd occurs exactly when the exchanged columns are a
> basis modulo some, but not all, prime divisors of \(N\).

This equivalence is true for squarefree \(N\), but false for non-squarefree
\(N\). Consequently the displayed progress parameter \(\delta_B\) does not
exactly characterize when the scan succeeds on the stated domain.

There is also a small endpoint defect in the displayed count bound when the
tail is empty. Both defects have local repairs. Neither damages the semiprime
CRT obstruction or the AKS/P11 application, but a frozen theorem containing a
false if-and-only-if cannot be promoted unchanged.

## 1. Fatal scope defect in the exact success criterion

Take the odd composite

\[
N=45,
\qquad
B=[1],
\qquad
T=[15].
\]

Then \(A=t=1\), \(\gcd(\det B,N)=1\), and \(C=B^{-1}T=[15]\). The
support-one exchange has determinant \(15\), so

\[
1<\gcd(15,45)=15<45.
\]

The scan therefore succeeds. However, the exchanged column is zero modulo
both distinct prime divisors \(3\) and \(5\). It is a basis modulo neither
local field. There is no “some but not all” local-field mismatch, and the
frozen definition gives no finite \(\delta_B\). Thus

\[
\text{scan succeeds}
\quad\not\Longleftrightarrow\quad
\delta_B\leq s
\]

for the stated class of composite inputs.

The reason is prime-power valuation. A determinant can contain every distinct
prime dividing \(N\), yet contain an insufficient power of one of them. Its
gcd with \(N\) is then proper although its reduction is dependent in every
residue field.

Two clean repairs are available:

1. restrict the exact equivalence and \(\delta_B\) statement to squarefree
   \(N\); or
2. keep arbitrary composite \(N\), state only that a local-field mismatch is
   sufficient for a proper gcd, and define scan success directly by
   \(1<\gcd(\det C[I,J],N)<N\).

The second repair is stronger for factoring because valuation-only splits are
additional successes. The explicit obstruction already uses \(N=pq\) with
distinct primes, so it is unchanged by either repair.

## 2. Exchange-minor identity passes

Because \(\det B\) is a unit in \(\mathbb Z/N\mathbb Z\), the factorization

\[
[B\mid T]=B[I_A\mid C],
\qquad C=B^{-1}T,
\]

is legal. Retaining the identity columns outside \(I\) and inserting the tail
columns in \(J\), followed by expansion along the retained identity columns,
gives

\[
\det E_{I,J}
=\varepsilon(I,J)\det(B)\det C[I,J].
\]

The sign depends on the fixed column-order convention and does not affect a
zero test or a gcd. Multiplication by the unit \(\det B\) preserves the gcd
with \(N\). Therefore every local-field zero-pattern mismatch does expose a
proper factor, for arbitrary \(N\). Only the converse fails as described
above.

## 3. Count and quasipolynomial cost

For an exchange of support \(k\), the removed base set and inserted tail set
can be chosen in exactly

\[
\binom Ak\binom tk
\]

ways. Hence

\[
Q_s(A,t)
=\sum_{k=0}^{\min(s,A,t)}\binom Ak\binom tk
\]

is exact.

When \(A,t\geq1\), each term is at most \((At)^s\), so

\[
Q_s(A,t)\leq(s+1)(At)^s.
\]

For polynomial \(A,t\) and \(s=(\log(n+1))^{O(1)}\), its logarithm is

\[
O(s\log n)=(\log(n+1))^{O(1)}.
\]

Polynomial preprocessing can compute \(C\) on the unit-base branch. A
division-free determinant algorithm then uses polynomially many
\(\mathbb Z/N\mathbb Z\) operations per \(k\)-by-\(k\) test. Residues stay at
\(O(n)\) bits. The total bit cost is quasipolynomial.

The frozen upper bound has a degenerate counterexample when \(t=0\) and
\(s\geq1\): its left side is \(Q_s(A,0)=1\), while its right side is
\((s+1)(A\cdot0)^s=0\). This is repaired by assuming a nonempty tail or by
using

\[
Q_s(A,t)\leq(s+1)\max\{1,At\}^{s}.
\]

All AKS and obstruction instances in F146 have \(t>0\), so this endpoint
does not change their conclusions.

If \(t\leq s\), every \(A\)-column subset contains at most \(t\) tail columns.
Thus the scan includes every maximal minor. Since the common base fixes rank
\(A\) in every local field, maximal bases determine the full column matroid.
The completeness claim passes.

## 4. Near-threshold prime-modulus corollary passes

Put

\[
L=\log_2N,
\qquad x=\sqrt{r-1},
\qquad u=r-1-L^2>0.
\]

For \(A=\lfloor Lx\rfloor\),

\[
\begin{aligned}
r-A
&<r-Lx+1\\
&=x(x-L)+2\\
&=\frac{x}{x+L}u+2\\
&<u+2.
\end{aligned}
\]

Therefore a polylogarithmic positive excess \(u\) gives a polylogarithmic
tail. The complete exchange scan is then quasipolynomial. The candidate
correctly labels this as a conditional cost result. It does not assert that
such a prime AKS modulus or a common unit base exists for every input.

## 5. CRT/Vandermonde delayed-disagreement family passes

Fix \(s\geq1\) and \(d=s+1\). With exponent indices \(0,\ldots,s-1\), write

\[
U_{ih}=i^h,
\qquad V_{hj}=j^h,
\qquad D=UV.
\]

Every generalized Vandermonde minor on increasing positive points and
increasing exponents is positive. For row and column sets \(I,J\) of size
\(k\leq s\), Cauchy--Binet gives

\[
\det D[I,J]
=\sum_{|K|=k}\det U[I,K]\det V[K,J]>0.
\]

The orientations agree because \(V[K,J]\) is the transpose of the usual
generalized Vandermonde ordering. Both \(U\) and \(V\) have rank \(s\), so
\(D\) has rank \(s\) and its full \(d\)-by-\(d\) determinant is zero.

For

\[
E_{ij}=i^{j-1},
\]

every square minor, including \(\det E\), is a positive generalized
Vandermonde determinant.

The entry bound

\[
|D_{ij}|,|E_{ij}|\leq s d^{2s}
\]

is conservative. The Leibniz formula then bounds every minor of either
matrix by

\[
H_s=d!\bigl(s d^{2s}\bigr)^d.
\]

Bertrand's postulate supplies primes

\[
H_s<q<2H_s,
\qquad q<p<2q.
\]

Thus reduction modulo \(q\) preserves every nonzero proper minor of \(D\),
while \(\det D=0\) stays zero. Reduction modulo \(p\) preserves every minor
of \(E\). Entrywise CRT gives one matrix \(C\pmod{pq}\) with these two local
reductions. In

\[
M_N=[I_d\mid C],
\]

all exchanges through support \(s\) are bases in both fields, while the full
support-\(s+1\) exchange is a basis modulo \(p\) and dependent modulo \(q\).
No earlier mismatch is possible. This proves the exact delayed-disagreement
claim.

Finally,

\[
\log H_s
=\log(d!)+d\bigl(\log s+2s\log d\bigr)
=\Theta(s^2\log(s+1)).
\]

Since both primes are within constant factors of \(H_s\),

\[
n=\lceil\log_2(pq+1)\rceil
=\Theta(s^2\log(s+1)).
\]

It follows that \(s\) eventually exceeds every fixed power of \(\log n\).
The quantifier needed to obstruct every fixed polylogarithmic exchange radius
is correct.

## 6. Padding passes, with the stated distinction

After \(N\) and \(n\) are fixed, set \(A=n^2\), keep the \(d=s+1\) tail
columns, put \(C\) in their first \(d\) rows, and make all later rows zero.
An exchange minor using a padded row is zero in both fields. An exchange
minor supported in the first \(d\) rows has its old status. Hence there is no
mismatch through support \(s\), and the old support-\(s+1\) mismatch remains.

The padded matrix no longer has the unpadded property that every small
exchange is a basis: many are dependent in both fields. The frozen statement
only claims that padding preserves the first disagreement and gives
AKS-scale dimensions. Read that way, it is correct. It also correctly says
that the padded matrix is not an AKS error matrix.

## 7. P11 calibration and prior-route scope pass

The P24 artifacts give

\[
A=2942,
\qquad t=11,
\qquad
\binom A2\binom t2=237{,}941{,}605,
\]

with zero, two, and two respectively for the first-field zeros,
second-field zeros, and zero-pattern mismatches. They also give no mismatch
among the \(2942\cdot11=32{,}362\) one-tail exchanges.

For a uniform random \(2\)-by-\(2\) matrix over \(\mathbb F_\ell\),

\[
z_\ell=1-(1-\ell^{-1})(1-\ell^{-2})
=\ell^{-1}+\ell^{-2}-\ell^{-3}.
\]

The frozen expectations \(2.3794\), \(1.1897\), and \(3.5691\), and the
one-tail expectation near \(0.000485\), agree with the promoted P11 sizes and
primes. They are explicitly a random comparison, not a model asserted for
the AKS matrix. Linearity of expectation needs no independence between
different minors.

For balanced semiprimes, \(p,q=2^{\Theta(n)}\). A quasipolynomial family with
only random-scalar divisibility has union-bound success

\[
2^{(\log n)^{O(1)}}(p^{-1}+q^{-1})
=2^{-\Theta(n)+o(n)}.
\]

That scale conclusion is correct.

The closest-prior comparison is also accurate. P24 supplies one
factor-assisted finite discovery at exchange support two and no uniform
selector. F146 adds an exact cost boundary and a general representable-
matroid obstruction. The obstruction is not an AKS counterexample. It does
not rule out an AKS-specific low-support theorem based on the coefficient
formula.

## 8. Required disposition

Do not promote the frozen F146 statement and proof. A corrected version can
retain all substantive results if it:

1. removes the false arbitrary-composite if-and-only-if, either by a
   squarefree hypothesis or by a one-way mismatch implication;
2. replaces the exact progress parameter by the actual proper-gcd condition
   when arbitrary composites remain in scope; and
3. handles \(t=0\) explicitly in the elementary count bound.

No new construction or experiment is needed for this repair. A corrected
frozen statement should receive a fresh hostile audit and a statement-only
blind reconstruction before promotion.
