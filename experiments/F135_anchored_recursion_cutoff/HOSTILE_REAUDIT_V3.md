# F135 hostile re-audit v3 — pass

## Verdict

**PASS for the frozen version below.** I read all three preserved failed
audits in full and tried to refute the corrected statement from the setup
again. Every recorded objection is repaired. I found no new counterexample
to the endpoint scope, threshold alternatives, width constant, forest edge
cases, selected CRT family, or endpoint sign screens.

Audited frozen hashes:

- `STATEMENT.md`:
  `b03002c70c97e38506f6e0c4fc4585e4e5268ec59c2b3557f8f3600dd837ef02`
- `PROOF.md`:
  `646e667edea22eb586cf069c6efdfdd8198132e00372d47e7ae882208d91a7a2`

This verdict is only for the claims and strict scopes in those files. F135
is not a complete-source obstruction, a parity-closure theorem, a
normalized-root theorem, or a factoring algorithm.

## 1. All preserved objections are repaired

I checked `HOSTILE_AUDIT_FAILED.md`,
`BLIND_RECONSTRUCTION_FAILED.md`, and
`HOSTILE_REAUDIT_FAILED.md` line by line.

1. Equation (6) now has the operator `\mid`.
2. The refinement claim now concerns only residual blocks contributed by
   the reciprocal endpoints \(H_A/\ell\). It does not put an old block from
   the \(q\)-side inside \(R_A\).
3. The proof gets the complete anchor powers from the retained endpoint
   presentations and the public integer \(H_A\). It does not claim that an
   anchor occurs to full exponent in its own right endpoint.
4. The proof explicitly allows \(\gcd(q,H_A)>1\). A shared non-anchor part
   remains in \(R_A\), as required.
5. The case \(R_A=1\) is now a separate residual-exhaustion outcome. It is
   not called a small-block release.
6. The abstract tree assumes \(b\ge2\), so its geometric-sum formula has no
   unary denominator defect.
7. The sentence after (10) now repeats the threshold scope. It makes no
   residual-size claim for a bucket below its threshold. Thus the old
   \(N=77,B=2,q=19,w=73\) counterexample is excluded from that implication.
8. The setup now declares \(B\ge2\) to be an integer.

The old examples \(N=17,B=3,q=5,w=7\),
\(N=7,B=2,q=3,w=5\), and the residual-exhaustion example from the blind
audit agree with the corrected statement.

## 2. Setup and recursion cutoff

For every eligible prime \(\ell\), strict \(q<N/B\) and \(\ell\le B\)
give

\[
1<\ell q<N.
\]

The digit range gives

\[
0<w+NA_\ell<N\ell,
\]

so \(z_\ell=(w+NA_\ell)/\ell\) is an integer in
\(\{1,\ldots,N-1\}\). Also

\[
(\ell q)z_\ell=q(w+NA_\ell)\equiv1\pmod N.
\]

If \(A_\ell=0\), this product is exactly \(qw=P_N(q)\). If
\(A_\ell>0\), then

\[
z_\ell>\frac N\ell\ge\frac NB.
\]

Both endpoints are least-positive representatives. Inverse uniqueness is
symmetric, so

\[
\iota_N(z_\ell)=\ell q,
\qquad
P_N(z_\ell)=P_N(\ell q).
\]

These implications use only the complete reciprocal endpoint. The explicit
exclusions for a released proper block, a power, a multi-block word, or a
wrapped endpoint are necessary and are present.

## 3. Distinct-digit overlap and same-digit refinement

For distinct digits,

\[
H_j-H_i=N(A_j-A_i),
\qquad
\gcd(H_i,N)=1.
\]

Therefore

\[
\gcd(H_i,H_j)=\gcd(H_i,A_j-A_i)<B.
\]

Since \(z_i\mid H_i\) and \(z_j\mid H_j\), division by unrelated anchors
cannot create a common divisor. Hence the divisibility and strict bound in
(6) are correct without a denominator-coprimality assumption.

For one occupied digit, the distinct eligible anchors divide the same
integer \(H_A\). Their full prime powers form \(S_A\mid H_A\), and removing
them from any reciprocal endpoint leaves the non-anchor part \(R_A\).
Complete gcd-free refinement can only split this part. Every resulting
reciprocal-side residual block therefore divides \(R_A\). This remains true
when a non-anchor factor is shared with \(q\); such a factor is not removed
into \(S_A\).

The two strict estimates are exactly

\[
R_0\le \frac{w}{L_0}<\frac N{L_0}<\frac NB
\quad(L_0>B)
\]

and

\[
R_A\le\frac{H_A}{L_A}<\frac{NB}{L_A}<\frac NB
\quad(A>0,\ L_A>B^2).
\]

Thus a threshold bucket either supplies at least one reciprocal-side block
below \(N/B\), when \(R_A>1\), or has no non-anchor reciprocal residual,
when \(R_A=1\). No conclusion is asserted below the threshold.

## 4. Width constant and row quantifier

On the no-threshold branch, let \(G\) be the product of eligible primes and
let \(X\) be the product of excluded primes. The imported P121 bound and
the exact exclusion estimate give

\[
\log G
>\frac6{25}n^3+3\log n-2\log N.
\]

The bucket bounds give

\[
G=L_0\prod_{A>0}L_A\le B(B^2)^d=n^{6d+3}.
\]

Using \(\log N<n\log2\), cancellation of \(3\log n\), followed by
division by \(6\log n\), gives exactly

\[
d>
\frac{n^3}{25\log n}
-\frac{n\log2}{3\log n}.
\]

There is no lost factor of two or three in (12).

The reused-row conclusion has the correct conditional quantifier. Fix any
prime \(r>B\) with odd \(v_r(q)\). If \(r\mid w\), no nonzero observed
digit makes \(H_A\) divisible by \(r\). If \(r\nmid w\), only the one
residue

\[
A\equiv-wN^{-1}\pmod r
\]

can do so. Because all digits are in \([0,B-1]\subset[0,r-1]\), at most
one occupied nonzero digit is exceptional. At least \(d-1\) distinct values
\(qH_A\) are therefore odd in row \(r\). Different digits give different
integers, and first-occurrence exact-value deduplication retains each such
integer somewhere in the global ledger.

The boxed alternative (13) is consequently read in the scope of the
immediately preceding covered-row quantifier: for every such \(r\), a
threshold bucket gives release or exhaustion, while the complementary
branch gives the displayed width in row \(r\). It does not assert that
\(q\) must contain a prime \(r>B\) to odd valuation.

## 5. Abstract forest, including boundary cases

For integer \(b\ge2\) and finite tree depth, align rows and columns in a
parent-before-child vertex order. Every column has its own diagonal one and
at most one additional one in an earlier parent row. The square matrix is
unitriangular, so its column kernel is zero.

Every internal row occurs in its own column and its \(b\) child columns.
Every leaf row has degree one. Leaf-first peeling removes one complete level
at a time and terminates at the root. The depth-zero case is also valid: it
is the one-by-one identity matrix.

For

\[
V=\frac{b^{T+1}-1}{b-1},
\]

\(b=n^{O(1)}\) and \(T=O((\log n)^2)\) imply

\[
\log V=O(T\log b)=O((\log n)^3).
\]

Thus the stated abstract transcript size is quasipolynomial. The statement
correctly makes no canonical-realization or complete-source claim.

## 6. Selected CRT family

The ten displayed CRT moduli are pairwise coprime. Their combined class is

\[
M=12{,}522{,}249{,}183{,}293{,}850,
\qquad
A=4{,}364{,}121{,}389{,}770{,}277,
\]

with \(\gcd(A,M)=1\). Primes \(P\equiv1\pmod M\) and
\(Q\equiv A\pmod M\) can be chosen in the two fixed disjoint relative
intervals by the prime number theorem in fixed arithmetic progressions.
Then \(P<Q<2P\), and disjoint increasing choices give infinitely many
distinct balanced semiprimes.

In fact these factors are also larger than every fixed quasipolynomial in
the input bit length for all sufficiently large family members. Here
\(P,Q=\Theta(X)\) and \(n=2\log_2X+O(1)\), while the logarithm of any fixed
quasipolynomial in \(n\) is \(O((\log n)^k)=o(n)\).

For every pair \((q_v,k_v)\), the square-modulus congruence gives

\[
1+k_vN\equiv q_v\pmod {q_v^2}.
\]

Thus \(v_{q_v}(C_v)=1\), and \(0<k_v<q_v\) makes
\(C_v/q_v\) the canonical inverse endpoint. The four carry equations

\[
7=2+5,
\quad17=2+3\cdot5,
\quad18=7+11,
\quad36=17+19
\]

together with the four anchor congruences give the edge presentations.
Their pairs \((c,k_v)\) are

\[
(15,7),(35,17),(143,18),(551,36),
\]

so \(k_v<c\) makes every quotient positive and less than \(N\).

Modulo the five block-prime squares, the incident residues are

\[
\begin{array}{c|l}
5&5,15,10\pmod{25}\\
11&11,44\pmod{121}\\
19&19,209\pmod{361}\\
23&23\pmod{529}\\
37&37\pmod{1369}.
\end{array}
\]

They are nonzero multiples of the row prime. All unlisted entries are
already nonzero modulo that prime. Hence (21) is the exact valuation-parity
submatrix. It is unitriangular. Rows \(23,37\), then \(11,19\), then \(5\)
give the claimed peeling cascade. Extra rows on the same five columns do not
change the degrees of these witness rows.

For any selected unit endpoint \(c\) with canonical inverse \(z\),

\[
\gcd(c-z,N)=\gcd(c^2-1,N),
\qquad
\gcd(c+z,N)=\gcd(c^2+1,N).
\]

Every selected \(c\) is at most \(551\). Once both prime factors exceed
\(551^2+1\), all displayed sign screens equal one. The values \(C_v\) are
distinct because their carries are distinct.

The construction controls only the five selected columns. It does not
control unselected source positions, and it proves no full-source nullity or
normalized-root claim.

## Final audit scope

F135 proves an exact recursive cutoff, a presentation-level
release/exhaustion/conditional-width alternative, an abstract incidence
obstruction, and a finite-depth selected canonical realization. It leaves
proper-block recursion, wrapped and multi-block feedback, cross-star
closure, complete-source behavior, and useful normalized roots open.

No mathematical repair is required for this frozen version. It can advance
to a fresh statement-only blind reconstruction, while all earlier failed
audits remain attached to their exact older hashes.
