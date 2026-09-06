# F135 hostile audit — failed pending narrow statement repairs

## Verdict

**FAIL as written.** The main arithmetic results survived re-derivation, but
the frozen statement contains one false unqualified refinement claim, one
missing mathematical operator, and one undefined edge case in the abstract
tree theorem. The false refinement claim has a small exact counterexample.

The required repairs are local. I found no counterexample to the recursion
cutoff, denominator-safe overlap bound, release inequalities, width bound,
abstract forest for \(b\ge2\), or the selected canonical CRT family after the
declared selected-source restriction is enforced.

Audited frozen hashes:

- `STATEMENT.md`:
  `be8b976e72df20cfc1b19fe0e3618b9c23f508b45d00001db54558c42462a5fd`
- `PROOF.md`:
  `71a8e6501b1f9c4afa79e37923bd694ee5faf84b86ab140e698f4db33bd35807`

## 1. Exact recursion cutoff and duplicate law

For an eligible prime \(\ell\), P121 gives

\[
c_\ell=\ell q<N,
\qquad
z_\ell={w+NA_\ell\over\ell}<N,
\qquad
c_\ell z_\ell=q(w+NA_\ell)\equiv1\pmod N.
\]

If \(A_\ell>0\), then

\[
z_\ell>{N\over\ell}\ge {N\over B}.
\]

If \(A_\ell=0\), then

\[
c_\ell z_\ell=qw=P_N(q).
\]

Both endpoints are in \(\{1,\ldots,N-1\}\). Therefore inverse uniqueness
also gives

\[
\iota_N(z_\ell)=c_\ell,
\qquad
P_N(z_\ell)=P_N(c_\ell).
\]

This theorem passes. It correctly excludes released proper blocks, powers,
multi-block words, and wrapped feedback.

## 2. Denominator-safe overlap bound

For distinct digits,

\[
H_j-H_i=N(A_j-A_i),
\qquad
\gcd(H_i,N)=1.
\]

Thus

\[
\gcd(H_i,H_j)
=\gcd(H_i,A_j-A_i)
\le |A_j-A_i|<B.
\]

No coprimality between \(\ell_i\) and \(\ell_j\), or between a denominator
and the other numerator, is needed. Since \(z_i\mid H_i\) and
\(z_j\mid H_j\),

\[
\gcd(z_i,z_j)\mid\gcd(H_i,H_j)<B.
\]

The argument passes. However, equation (6) in `STATEMENT.md` currently says

```text
\gcd(z_i,z_j)mid\gcd(H_i,H_j)
```

and is missing the backslash before `mid`. It must be `\mid`.

## 3. Same-digit refinement: exact failure and repair

The statement currently says that, after anchor-prime powers are removed,
**every** remaining block divides a factor of \(R_A\), and that \(R_A=1\)
leaves no non-anchor residual. This is false if it refers to the full endpoint
basis. The old block \(q\) remains on the left endpoint side and need not
divide \(R_A\).

An exact counterexample is

\[
N=17,
\qquad B=3,
\qquad q=5,
\qquad w=7.
\]

Both eligible anchors \(2\) and \(3\) have digit \(A=1\), because

\[
H_1=w+N=24.
\]

The two endpoint presentations are

\[
(2q,H_1/2)=(10,12),
\qquad
(3q,H_1/3)=(15,8).
\]

Here

\[
L_1=6,
\qquad
S_1=2^3\cdot3=24,
\qquad
R_1=1.
\]

Complete refinement of \(10,12,15,8\) still contains the non-anchor block
\(5=q\). It does not divide \(R_1=1\). Therefore the two unqualified
sentences are false.

The intended and valid statement is narrower:

> After the named anchor-prime powers are removed, every residual block
> supported in the reciprocal endpoints \(H_A/\ell\), equivalently every
> residual block released from the \(H_A\)-side, divides \(R_A\). If
> \(R_A=1\), no non-anchor residual from the \(H_A\)-side remains.

With this restriction, the proof works. The size conclusions then apply to
the residual blocks released from \(H_A\), not to all old blocks in the
global basis.

The proof must also replace this sentence:

> records its complete exponent in the right endpoints

An anchor with exponent one is absent from its own right endpoint
\(H_A/\ell\). The correct source of the complete exponent is the retained
**endpoint presentation as a whole**, together with the already named
\(q\) and the known anchor \(\ell\). Since \(\ell\nmid q\), the left endpoint
\(\ell q\) isolates \(\ell\); the exact endpoint products retain all
exponents.

### Shared integer factors between \(q\) and \(H_A\)

Modular invertibility does not imply \(\gcd(q,H_A)=1\). For example,

\[
N=7,
\quad B=2,
\quad q=3,
\quad w=5,
\quad A=1,
\quad H_A=12,
\]

so \(\gcd(q,H_A)=3\). Here \(S_A=4\) and \(R_A=3\). This does not break
the repaired theorem. Eligibility gives \(\ell\nmid q\), so a factor shared
by \(q\) and \(H_A\) is not removed as an anchor factor. It remains in
\(R_A\). Complete gcd-free refinement exposes the common part, and every
such reciprocal-side block still divides \(R_A\).

## 4. Release inequalities and exact width

For an occupied bucket, \(S_A\ge L_A\). If \(A=0\), then

\[
R_0\le {w\over L_0}<{N\over L_0}.
\]

If \(A>0\), then \(A\le B-1\) and

\[
H_A=w+NA\le NB-1<NB,
\qquad
R_A<{NB\over L_A}.
\]

Therefore \(L_0>B\) or \(L_A>B^2\), respectively, gives the strict bound
\(R_A<N/B\). These inequalities pass once their conclusion is restricted to
the reciprocal-side residual blocks described above.

For \(B=n^3\), the imported elementary P121 bound is

\[
\vartheta(n^3)>{6\over25}n^3
\qquad(n\ge64).
\]

If \(X\) is the product of excluded primes, then

\[
X\le\operatorname{rad}(Nq)\le Nq<{N^2\over n^3}.
\]

Hence the eligible-prime product \(G\) satisfies

\[
\log G>{6\over25}n^3+3\log n-2\log N.
\]

On the no-release branch,

\[
G=L_0\prod_{A>0}L_A\le B(B^2)^d=B^{2d+1}.
\]

Using \(\log N<n\log2\) gives exactly

\[
d>{n^3\over25\log n}-{n\log2\over3\log n}.
\]

At \(n=64\), the right side is approximately \(2517.7367\), so the bound
is nonvacuous. The strict inequalities and the constant are correct.

For a prime \(r>B\) with odd \(v_r(q)\), the two valuation cases are also
correct:

- if \(r\mid w\), every nonzero observed digit has zero \(r\)-valuation;
- if \(r\nmid w\), only the one residue
  \(A\equiv-wN^{-1}\pmod r\) can have positive valuation.

Since all observed digits are in \([0,B-1]\subset[0,r-1]\), at most one
nonzero digit can be exceptional. Different digits give different exact
integers \(q(w+NA)\). First-occurrence deduplication keeps each value either
now or at its earlier occurrence. Thus the stated \(d-1\) row-width bound
passes.

## 5. Abstract forest and quasipolynomial cost

In a parent-before-child order, each column has its diagonal own-row entry
and at most one entry in an earlier parent row. The matrix is unitriangular,
so its column kernel is zero. Internal rows have degree \(b+1\), and peeling
from the leaves deletes the full tree.

For \(b\ge2\),

\[
V={b^{T+1}-1\over b-1},
\qquad
\log V=O(T\log b).
\]

Thus \(b=n^{O(1)}\) and \(T=O((\log n)^2)\) give
\(V=2^{O((\log n)^3)}\). This cost calculation passes.

The theorem must either state \(b\ge2\), or give the separate unary-tree
case \(b=1\), where \(V=T+1\). As written, formula (14) is undefined at
\(b=1\).

The proof correctly labels this as an abstract incidence obstruction. It
does not claim a canonical integer realization or a complete-source null.

## 6. Complete audit of the selected CRT family

The ten CRT moduli are pairwise coprime. Combining the displayed
congruences gives

\[
M=12{,}522{,}249{,}183{,}293{,}850,
\qquad
A=4{,}364{,}121{,}389{,}770{,}277,
\]

with \(\gcd(A,M)=1\). Thus both residue classes \(1\pmod M\) and
\(A\pmod M\) are reduced.

Because \(M\) is fixed, the prime number theorem in arithmetic progressions
gives, for every sufficiently large \(X\), a prime

\[
P\equiv1\pmod M,
\quad P\in[X,1.1X],
\]

and a prime

\[
Q\equiv A\pmod M,
\quad Q\in[1.2X,1.3X].
\]

Choose an increasing sequence with disjoint containing intervals. Then the
resulting semiprimes are distinct, odd, and satisfy \(P<Q<2P\). For each
fixed polynomial in the bit length, both factors exceed it for all
sufficiently large members. These are the required PNT-AP and trial-hardness
quantifiers; there is no uniform cutoff over all polynomials at once.

For every pair \((q_v,k_v)\), the square-modulus congruence gives

\[
1+k_vN\equiv q_v\pmod {q_v^2}.
\]

Thus \(v_{q_v}(C_v)=1\). Since \(0<k_v<q_v\), the quotient
\(C_v/q_v\) lies in \((0,N)\), so \(P_N(q_v)=C_v\).

The carry identities are exact:

\[
7=2+5,
\quad17=2+3\cdot5,
\quad18=7+11,
\quad36=17+19.
\]

The four anchor congruences make the child value divisible by the displayed
\(\ell q_u\). In each case the child carry is smaller than the selected left
endpoint:

\[
(\ell q_u,k_v)=(15,7),(35,17),(143,18),(551,36).
\]

Therefore the quotient is again in \((0,N)\), and every equality in (20)
is canonical.

Reducing the five values modulo the five block-prime squares gives the
incident residues

\[
\begin{array}{c|l}
5&5,15,10\pmod{25}\\
11&11,44\pmod{121}\\
19&19,209\pmod{361}\\
23&23\pmod{529}\\
37&37\pmod{1369}.
\end{array}
\]

Each is a nonzero multiple of its row prime. Every unlisted entry is already
nonzero modulo that prime. Hence matrix (21) is the exact valuation-parity
submatrix, not only a divisibility matrix. Its determinant is one. Rows
\(23,37\), then \(11,19\), then \(5\), give the stated peeling order inside
the selected five-column family. Extra prime rows on those same columns do
not change the degrees of these five witness rows.

For a selected unit endpoint \(c\) and its canonical inverse \(z\),

\[
\gcd(c-z,N)=\gcd(c^2-1,N),
\qquad
\gcd(c+z,N)=\gcd(c^2+1,N).
\]

All selected left endpoints are at most \(551\). Once both prime factors of
\(N\) exceed \(551^2+1\), neither can divide a nonzero displayed
\(c^2\pm1\). Thus all selected sign screens are one.

The selected-source wording is essential and is stated correctly. An
unselected column can increase one of the five row degrees, create a
dependency, or return a factor. The CRT conditions do not control the full
source. Exact-value duplicates such as \(P_N(15)=P_N(11)\) collapse to one
value column, but the five integers \(C_0,\ldots,C_4\) are mutually distinct
because their carries are distinct.

## Required repairs before re-audit

1. Add the missing backslash in statement equation (6): `\mid`.
2. Restrict the Theorem 3 refinement and \(R_A=1\) claims to residual blocks
   from the reciprocal \(H_A\)-side. Do not quantify over the old \(q\)-side
   blocks in the global basis.
3. In the proof, replace “complete exponent in the right endpoints” with an
   exact endpoint-presentation argument. Explicitly allow
   \(\gcd(q,H_A)>1\) and explain why the shared part lies in \(R_A\).
4. State \(b\ge2\) in Theorem 4, or add the separate \(b=1\) formula.

After these repairs, the candidate needs a fresh hostile re-audit. It must
not be promoted from this failed audit.
