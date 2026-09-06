# F133 statement — anchored feedback forces reuse of a large prime row

## Status

This is a proof-only kill-first result. It proves a source-side row-reuse
theorem and the quasipolynomial cost of the corresponding adaptive source.
It does not prove parity closure or a non-global square root. It is not an
integer-factoring theorem.

For a unit \(c\in\{1,\ldots,N-1\}\), write

\[
\iota_N(c)=c^{-1}_{\rm can}\pmod N,
\qquad
P_N(c)=c\iota_N(c).
\]

Thus \(P_N(c)\equiv1\pmod N\) and \(P_N(c)<N^2\).

## Theorem 1 — the exact anchored-carry law

Let \(B\ge2\) be an integer. Let \(q\) be an integer block such that

\[
1<q<\frac NB,
\qquad
\gcd(q,N)=1.
\]

Put \(w=\iota_N(q)\). For every prime

\[
\ell\le B,
\qquad
\ell\nmid Nq,
\]

let \(A_\ell\in\{0,\ldots,\ell-1\}\) be the unique integer for which

\[
w+NA_\ell\equiv0\pmod\ell.
\]

Then both endpoints below are already canonical integers:

\[
c_\ell=\ell q<N,
\qquad
z_\ell=\frac{w+NA_\ell}{\ell}<N,
\]

and

\[
\boxed{
\iota_N(\ell q)=z_\ell,
\qquad
P_N(\ell q)=q(w+NA_\ell).
}
\tag{1}
\]

Also,

\[
\boxed{A_\ell=0\iff \ell\mid w.}
\tag{2}
\]

Different carry digits give different exact values in (1).

## Theorem 2 — one anchor forces an odd large-prime row

Let \(r>B\) be a prime such that \(v_r(q)\) is odd. Define the eligible
prime product

\[
G_B(N,q)=
\prod_{\substack{\ell\le B\ {\rm prime}\\ \ell\nmid Nq}}\ell.
\]

If

\[
\boxed{G_B(N,q)>N^2B,}
\tag{3}
\]

then there is an eligible prime \(\ell\) for which

\[
A_\ell\ne0,
\qquad
v_r(w+NA_\ell)\equiv0\pmod2.
\]

Consequently,

\[
P_N(\ell q)\ne P_N(q),
\qquad
v_r(P_N(\ell q))\equiv1\pmod2.
\tag{4}
\]

The word “new” in (4) means new relative to the unary value \(P_N(q)\).
It need not be globally new relative to an arbitrary earlier relation
ledger. If it equals an earlier exact value, that earlier value already has
the same odd \(r\)-row.

The conclusion handles all higher valuations. It does not assume that
\(w+NA_\ell\) is squarefree. An even valuation can be \(0,2,4,\ldots\).

## Theorem 3 — the deduplicated ledger has row degree at least two

Suppose a source processes the unary value \(P_N(q)\) and all eligible
anchored values in Theorem 1. It keeps the first occurrence of every
distinct exact value. If (3) holds, then, after this exact-value
deduplication, at least two distinct retained values have odd \(r\)-adic
valuation.

Equivalently, the prime-parity row indexed by \(r\) has degree at least two.
Thus \(r\) is not a private row of the retained relation matrix.

This conclusion is independent of the old ledger. A value that duplicates
an old value is already present. Distinct carry digits give distinct exact
values, so global exact-value deduplication does not remove the two values
certified by the theorem.

## Theorem 4 — an elementary uniform anchor cutoff

Put

\[
n=\lceil\log_2(N+1)\rceil.
\]

For every \(n\ge64\), put \(B_0=n^3\). If

\[
1<q<\frac{N}{n^3},
\qquad
\gcd(q,N)=1,
\]

then

\[
G_{n^3}(N,q)>N^2n^3.
\tag{5}
\]

Therefore every prime \(r>n^3\) that occurs to odd order in \(q\) satisfies
the degree-at-least-two conclusion of Theorem 3.

The bound (5) is unconditional. It uses only an elementary lower bound for
the product of the primes at most \(n^3\). It does not use the prime number
theorem.

For inputs with \(n<64\), deterministic trial division is a fixed finite
preprocessing step. Its absolute cost is absorbed by every asymptotic
quasipolynomial bound below.

### Corollary 4A — polynomial row multiplicity

Under the hypotheses of Theorem 4, fix a prime \(r>n^3\) with
\(v_r(q)\) odd. Among the eligible anchors there are more than

\[
\boxed{\frac{n^2}{4}}
\tag{6}
\]

distinct nonzero carry digits \(A\) for which \(v_r(w+NA)\) is even.
Consequently, either a direct endpoint screen succeeds, or the globally
deduplicated ledger contains more than \(n^2/4\) distinct exact values with
odd \(r\)-adic valuation after the complete anchor scan. This quantitative
statement is stronger than the
degree-at-least-two conclusion, but the latter does not depend on the
uniform \(B_0=n^3\) estimate.

## Theorem 5 — conditional composition stays quasipolynomial

Put

\[
L=\lceil\log_2(n+1)\rceil,
\qquad
E=2^{L^2},
\qquad
T=L^2.
\]

Conditional on the declared F130 and F132 transcript-cost statements, start
from their complete retained transcript. Completely refine all accumulated
endpoints into an all-block
gcd-free basis. For each of \(T\) frozen rounds, do the following:

1. For every current block \(q\) and every
   \(1\le a\le\min(E,N-1)\), screen \(\gcd(a,N)\), and compute on the
   surviving unit branch
   \[
   c=[aq]_N,
   \qquad
   z=\iota_N(c),
   \qquad
   P=cz.
   \]
2. Run both direct sign screens on \(c,z\). Retain every distinct endpoint
   presentation before exact-value deduplication. Retain the first copy of
   every distinct exact value \(P>1\).
3. After the full frozen scan, batch-refine all accumulated endpoints into
   the next all-block basis.

After \(T\) rounds, run one complete P66 decode on the full exact-value
ledger. The conditional resulting deterministic bit complexity is

\[
\boxed{2^{O((\log n)^4)}}.
\tag{7}
\]

The integer anchor bank contains every eligible prime at most \(E\). For
\(n\ge64\), \(E\ge n^3\). Hence Theorem 4 applies inside this source to
every current block satisfying \(q<N/n^3\). One can also apply Theorems
2–3 directly with \(B=E\), which covers the smaller region
\(q<N/E,\ r>E\).

The same cost bound holds if the old F132 unary powers are repeated in each
anchored round, or if every pair \(a q^e\), \(1\le a,e\le E\), is processed.
These larger menus are not needed for Theorem 4.

## Exact remaining boundary

The result removes one obstruction: a large prime row carried oddly by a
small dynamic block cannot remain private after the declared anchor scan.
It does not cover these cases:

1. \(q\ge N/n^3\), where the selected products need not be unreduced;
2. blocks whose odd prime rows are all at most \(n^3\);
3. large primes that occur only to even order in the block; and
4. parity rows that become non-private but disappear later in a degree-one
   peeling cascade through other rows.

Most importantly, row degree at least two does not imply a binary kernel.
A binary kernel does not imply a non-global normalized root. No theorem
here proves that the composed source factors every input.
