# F135 hostile re-audit — failed on one remaining scope defect

## Verdict

**FAIL as written.** All objections in the two first-round failed audits are
repaired. The corrected arithmetic implications, width theorem, abstract
forest, and selected CRT family survive re-derivation. However, the paragraph
after (10) states its small-block conclusion without the antecedent of (9) or
(10). Taken literally, that sentence is false. There is a small, null-screen
distinct-semiprime counterexample.

There is also a minor type omission: the general setup does not declare
\(B\) to be an integer, although Theorem 3 uses
\(\{0,\ldots,B-1\}\). The earlier P121 statement declared this explicitly.

Audited frozen hashes:

- STATEMENT.md:
  b9fed1e148e8e88d022b322c4c3c3675e1ee2bb2dad37954340dd39346688a5b
- PROOF.md:
  805b8bc9255c7c0be5d60fcab5c6d1d585d2f8da7ba2009c28ef06d2661e06e9

## 1. Every earlier objection is repaired

I checked both preserved failed audits in full.

1. Equation (6) now uses \(\mid\).
2. The refinement claim is now restricted to residual blocks contributed by
   the reciprocal \(H_A\)-side. It no longer claims that an old block
   supported only on the \(q\)-side divides \(R_A\).
3. The proof now obtains the full anchor-prime exponent from the retained
   endpoint presentation and the known integer \(H_A\), not from the right
   endpoint alone.
4. The proof explicitly allows \(\gcd(q,H_A)>1\) and correctly leaves every
   shared non-anchor part in \(R_A\).
5. The abstract tree now assumes \(b\ge2\), so its geometric-sum formula is
   defined.
6. The final alternative now includes residual exhaustion when \(R_A=1\).

The old counterexamples \(N=17,B=3,q=5\) and
\(N=7,B=2,q=3\) no longer refute the corrected reciprocal-side statement.

## 2. Remaining false unqualified sentence

After proving the two conditional implications

\[
A=0,\ L_0>B\Longrightarrow R_0<N/B
\]

and

\[
A>0,\ L_A>B^2\Longrightarrow R_A<N/B,
\]

the statement says:

> If \(R_A>1\), every reciprocal-side residual block is small enough for the
> P121 size hypothesis.

This sentence does not repeat either left-hand condition. It is false for a
bucket that does not cross its product threshold.

Take

\[
N=77=7\cdot11,\qquad B=2,\qquad q=19,\qquad w=73.
\]

Then

\[
1<q<N/B,\qquad 19\cdot73=1+18N,\qquad \gcd(q,N)=1.
\]

The only eligible anchor is \(\ell=2\). Its digit is \(A=1\), and

\[
H_1=w+N=150,\qquad
c=2q=38,\qquad
z=H_1/2=75.
\]

Thus

\[
P_N(38)=38\cdot75=1+37N.
\]

For this occupied bucket,

\[
L_1=2,\qquad S_1=2,\qquad R_1=75.
\]

The reciprocal endpoint \(75\) is itself a non-anchor gcd-free residual
block in the local endpoint set, but

\[
75>77/2=N/B.
\]

No direct screen hides the issue:

\[
\gcd(19-73,77)=\gcd(19+73,77)=1,
\]

\[
\gcd(38-75,77)=\gcd(38+75,77)=1.
\]

There is no contradiction with implication (10), because
\(L_1=2\le B^2=4\). The counterexample only refutes the subsequent
unqualified sentence.

The minimal repair is:

> Whenever the antecedent of (9) or (10) holds, if \(R_A>1\), every
> reciprocal-side residual block is small enough for the P121 size
> hypothesis. If \(R_A=1\), the reciprocal-side residual is exhausted.

With that qualification, the release/exhaustion/width alternative is valid.

## 3. Missing integer declaration

The setup currently says only \(B\ge2\). Theorem 3 then indexes buckets by

\[
A\in\{0,\ldots,B-1\}.
\]

This notation requires integer \(B\). The quantitative specialization
\(B=n^3\) is an integer, but the preceding general theorems are stated before
that specialization. The minimal repair is to write:

> Let \(B\ge2\) be an integer.

This is a type repair, not a change to the result.

## 4. Results that survive hostile re-derivation

### Recursion cutoff and duplicate law

For every eligible anchor,

\[
z_\ell={w+NA_\ell\over\ell}<N,\qquad
\ell q<N,\qquad
(\ell q)z_\ell\equiv1\pmod N.
\]

If \(A_\ell>0\), then

\[
z_\ell>N/\ell\ge N/B.
\]

Inverse uniqueness gives

\[
\iota_N(z_\ell)=\ell q,\qquad
P_N(z_\ell)=P_N(\ell q).
\]

Theorem 1 passes.

### Distinct-digit overlap

For \(A_i\ne A_j\),

\[
\gcd(H_i,H_j)
=\gcd(H_i,N(A_i-A_j))
=\gcd(H_i,A_i-A_j)<B,
\]

because \(\gcd(H_i,N)=1\). Since \(z_i\mid H_i\) and
\(z_j\mid H_j\), the denominator-safe divisibility in (6) follows. Theorem 2
passes.

### Conditional release bounds and width

The repaired reciprocal-side scope makes

\[
R_0<N/B\quad(L_0>B),\qquad
R_A<N/B\quad(A>0,\ L_A>B^2)
\]

correct. On the complementary branch, the eligible-prime product gives

\[
d>
{n^3\over25\log n}
-{n\log2\over3\log n}.
\]

For a prime \(r>B\) occurring oddly in \(q\), at most one nonzero digit can
make \(H_A\) divisible by \(r\). Hence at least \(d-1\) distinct values
\(qH_A\) have odd \(r\)-valuation. Exact-value deduplication preserves their
first occurrences. These arguments pass.

### Abstract forest

In a parent-before-child order, the displayed square matrix is triangular
with diagonal one. Its kernel is zero, and leaf-first degree-one peeling
deletes it. For \(b=n^{O(1)}\) and \(T=O((\log n)^2)\), its size is
\(2^{O((\log n)^3)}\). Theorem 4 passes under its corrected \(b\ge2\)
assumption.

### Selected canonical CRT family

The CRT moduli are pairwise coprime, and their combined class is

    A = 4364121389770277
    M = 12522249183293850
    gcd(A,M) = 1

The square-modulus conditions give exact valuation one in each named unary
row. The anchor congruences and carry identities give all four duplicate
presentations. The five-by-five parity submatrix is exactly the displayed
unitriangular matrix. The selected-source scope is stated correctly.

As an independent finite check, the previously reconstructed member

    P = 12584860429210319251
    Q = 15131241134808741077

has two Sage-certified prime factors. Native exact arithmetic reproduced all
nine canonical identities, all named parity entries, and all endpoint sign
gcds equal to one. Theorem 5 passes as a selected-source result.

## Required repairs before another audit

1. Qualify the sentence after (10) by the antecedent of (9) or (10).
2. Declare \(B\ge2\) to be an integer in the general setup.

No other counterexample was found. The corrected theorem and proof need new
frozen hashes and another hostile audit. This failed re-audit must remain in
the record.
