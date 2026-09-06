# F139 hostile re-audit — PASS

## Verdict

**PASS as claimed.** The two defects in the preserved first hostile audit
are repaired. No other theorem text changed. I found no false quantifier,
hidden factorization step, failed strict inequality, deduplication gap,
linear-algebra error, cost overflow, or certificate mismatch.

F139 remains a source-and-boundary theorem. It does not prove that a
qualifying multi-owner product always exists. It does not force a binary
dependency, a non-global normalized root, or a factor.

## Frozen inputs

- STATEMENT.md:
  90f89961e4fb9f2a16bd8027cd6ea21092c3794e2e4994254b3ac7f57e04e148
- PROOF.md:
  56f4d677fec4ea05644b41191689880473eea4bb3b25eb8ab1f33013f5aef757
- HOSTILE_AUDIT_FAILED.md:
  489219eb892a494657567db76576548231932d2a02e28fa70cf3c6da7b9c176c
- pre-reaudit MANIFEST.md:
  79dce9b638047ee4c340a811deebaa01b2d93ae6406e05af7441ea38c3c25a17
- verify.sage:
  d0cb52305d9ab1f75ec02f4b67fcbc1fae520b6dc424175aac077dbb940ea376
- OUTPUT.json and RUN.log:
  4cda0f1af6adf29f73fc7e5f0d0d74f85ca4b331c02e8cbabe61b97a7c0778ba

## Repair-scope check

The proof hash is unchanged. Reversing exactly these two edits in the
current statement reproduces the failed statement hash
810e37e044778b24db0901b7a35a2b9f403d065590e6c08edc5b2ee4f8119b8b:

1. Replace the explicit definition
   \[
   1\le\ell\le B,\qquad \gcd(\ell,Nq)=1
   \]
   by the former undefined phrase “eligible integer anchor.”
2. Replace the repaired \(\sum\) inside the boxed Theorem 4 formula by the
   former literal “sum.”

Thus only the two repairs required by HOSTILE_AUDIT_FAILED.md occurred. The
repaired eligibility condition agrees with the verifier and with the earlier
prime-anchor condition.

## 1. Canonical integer-anchor construction

Eligibility gives \(\gcd(\ell,Nq)=1\), so \(N\) is invertible modulo
\(\ell\) and the digit \(A_\ell\in[0,\ell-1]\) is unique. The size
conditions give

\[
1\le \ell q<N
\]

and

\[
0<w+NA_\ell<N\ell.
\]

Therefore \(z_\ell=(w+NA_\ell)/\ell\) is an integer in
\(\{1,\ldots,N-1\}\). Its product with \(\ell q\) is one modulo \(N\).
Inverse uniqueness proves that the displayed pair is canonical. This works
for composite integer anchors as well as prime anchors.

## 2. Simultaneous preservation and strict count

For each \(r\in\mathcal R_B(q)\), unitness of \(q\) gives \(r\nmid N\).
The equation

\[
w+NA\equiv0\pmod r
\]

has one residue class modulo \(r\). Two digits in \([1,B-1]\) cannot be
congruent modulo \(r>B\). Hence each large odd row excludes at most one
occupied digit. A union bound over the exact row set gives

\[
\#\{\text{common-good digits}\}
\ge |D|-|\mathcal R_B(q)|.
\]

Also,

\[
\prod_{r\in\mathcal R_B(q)}r\le q
\quad\text{and}\quad r>B,
\]

so

\[
B^{|\mathcal R_B(q)|}<q.
\]

The strict logarithmic bound follows. It remains valid when the row set is
empty because \(q>1\). A composite-anchor scan can add occupied digits to
the prime-anchor scan; it cannot weaken the P123 width lower bound.

## 3. Exact-value deduplication

A common-good value \(V_A=qH_A\) contains every row in
\(\mathcal R_B(q)\) oddly. If two such rows are globally degree one in
different old columns, equality of \(V_A\) with an old value would force
that old value to be both owners. This is impossible.

Different digits give different integers:

\[
V_A-V_{A'}=qN(A-A')\ne0.
\]

Thus every common-good digit gives a distinct new exact value under the
stated two-owner hypothesis. The proof correctly requires global privacy in
the permanent old ledger. Privacy created only after peeling is not used.

The public factor-free corollary is sound. A nonsquare \(B\)-rough basis
block contains a hidden prime larger than \(B\) to odd valuation.
Pairwise-coprime basis blocks give different hidden primes. A globally
degree-one public block row makes each selected hidden odd prime private to
the same owner. The algorithm only tests gcds, exact divisions, and integer
squares. It never factors a rough block.

## 4. Conditional quasipolynomial cost

The product of primes through \(B\) has at most \(O(B\log B)\) bits by the
stated elementary bound. Its prime list is computable in time polynomial in
\(B\). For

\[
B\le 2^{(\log n)^{O(1)}},
\]

this is quasipolynomial in \(n\). Complete gcd-free refinement, exact square
tests, owner-row inspection, sorting, the packed inverse, sign screens, and
at most \(B\) anchor attempts remain quasipolynomial on an explicit
quasipolynomial transcript.

Keeping the smallest qualifying block per owner is optimal for cardinality.
For each \(s\), the product of the \(s\) smallest owner minima is no larger
than any other \(s\)-owner product. Hence the longest prefix with \(Bq<N\)
has maximum possible owner count under the declared one-block-per-owner
rule.

This is only a cost and selector theorem. The prefix may contain zero or one
owner. The statement does not claim otherwise.

## 5. Multi-pivot splice law

Let \(s=\sum_j\beta_j\). Each globally private pivot equation forces

\[
\alpha_i=s.
\]

After deleting the pivot rows, a dependency is equivalent to

\[
\widehat W\gamma+
\sum_j\beta_j
\left(
\widehat u_j+\sum_i\widehat v_i
\right)=0.
\]

This is exactly the repaired boxed column-span criterion. Conversely, a
solution to that membership condition reconstructs a full dependency by
setting every owner coefficient to \(s\). Old-column independence ensures
that a new dependency has \(\beta\ne0\).

The abstract hyperforest is full rank for every \(t\ge2,d\ge1\). Each
\(h_j\) is private to \(u_j\), so all new coefficients vanish. The old
pivot rows then kill all \(v_i\). The same rows give the complete declared
peeling order. Thus simultaneous multi-parent row reuse does not force a
rank defect.

## 6. \(N=989\) certificate

I reran

    gtimeout 300 sage verify.sage

with Sage proof arithmetic enabled. The fresh standard-output hash is

    4cda0f1af6adf29f73fc7e5f0d0d74f85ca4b331c02e8cbabe61b97a7c0778ba

and exactly matches the two frozen output files. Every named Boolean check
is true.

The replay verifies:

- \(989=23\cdot43\);
- \(5\cdot187<989\) and
  \(187\cdot238=1+45\cdot989\);
- both packed-base sign screens and every anchor sign screen are one;
- all five eligible integer anchors, digits, endpoint divisions, canonical
  inverse pairs, carries, exact values, and factorizations;
- exact-value first-occurrence deletion of the two zero-digit
  presentations;
- degree-one ownership of rows \(11\) and \(17\) in the frozen selected
  two-column old ledger;
- simultaneous odd preservation of those rows in digits \(1,2,3\);
- the exact full-support parity matrix, rank six, nullity zero, and complete
  six-step peeling witness.

The statement explicitly limits this computation to the selected
six-column source. It makes no claim about global ordering or row degrees in
the complete F26-Q source.

## 7. Preserved failed history and final scope

The invalid \(N=667\) certificate and all of its preregistration, revision,
empty-output, pin, verifier, and scope-incomplete output artifacts remain
preserved. The fatal packed-base screen

\[
\gcd(133+331,667)=29
\]

is explicit. None of that failed run is used as positive evidence.

The corrected F139 result therefore passes. Its exact remaining gate is the
one stated in the artifact: prove a qualifying packed word and a dependency
among the shifted residual classes, or prove a global potential that forces
equivalent progress. Even a rank defect would still need a separate
non-global normalized-root theorem.
