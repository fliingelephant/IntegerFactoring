# F135 statement — anchored recursion cutoff and expanding-forest boundary

## Status and closest prior results

This is a proof-only candidate. It is not a parity-closure theorem, a
complete-source obstruction, or an integer-factoring algorithm.

The closest earlier results are:

- P120 proves that one reused row need not survive degree-one peeling and
  that unary feedback on a complete old endpoint can be an exact duplicate.
- P121 proves that small prime anchors force more than \(n^2/4\) distinct
  exact values to reuse every covered odd large-prime row of a small block.
- F134 proves that different digits in one anchored star cannot share a
  prime larger than the carry range.

The material change is recursive. This result proves that every genuinely
new unreduced P121 arm has its reciprocal endpoint outside the small-block
region, and unary feedback on that endpoint is inert. It then gives an exact
presentation-release alternative, an abstract quasipolynomial forest that
meets all current local incidence conditions but has zero kernel, and a
finite canonical selected-source realization of two forest generations.

## Setup

Let \(N\ge3\) be odd. Let \(B\ge2\) be an integer, and let \(q\) be a unit
with

\[
1<q<\frac NB.
\]

Put

\[
w=\iota_N(q),
\qquad
qw=1+kN.
\]

For every eligible prime

\[
\ell\le B,
\qquad
\ell\nmid Nq,
\]

let \(A_\ell\in\{0,\ldots,\ell-1\}\) be the unique digit such that

\[
w+NA_\ell\equiv0\pmod\ell.
\]

Write

\[
H_\ell=w+NA_\ell,
\qquad
c_\ell=\ell q,
\qquad
z_\ell=\frac{H_\ell}{\ell}.
\]

P121 gives

\[
c_\ell,z_\ell\in\{1,\ldots,N-1\},
\qquad
\iota_N(c_\ell)=z_\ell,
\qquad
P_N(c_\ell)=qH_\ell.
\tag{1}
\]

## Theorem 1 — exact recursion cutoff and duplicate law

For every eligible \(\ell\):

1. If \(A_\ell=0\), then
   \[
   P_N(\ell q)=P_N(q)=qw.
   \tag{2}
   \]
   The anchored occurrence can refine endpoints, but it adds no exact
   relation value.
2. If \(A_\ell>0\), then
   \[
   \boxed{z_\ell>\frac NB.}
   \tag{3}
   \]
   Thus the reciprocal endpoint of every genuinely new arm lies outside the
   small-block hypothesis used by P121.
3. In both cases,
   \[
   \boxed{
   \iota_N(z_\ell)=\ell q,
   \qquad
   P_N(z_\ell)=P_N(\ell q).
   }
   \tag{4}
   \]
   Unary feedback on the complete reciprocal endpoint is an exact duplicate.

This theorem does not cover a proper block released from \(z_\ell\), a
power or multi-block word, or wrapped feedback on a large endpoint.

## Theorem 2 — reciprocal endpoints inherit the star-overlap bound

Take two eligible anchors \(\ell_i,\ell_j\) with distinct digits
\(A_i\ne A_j\). Put

\[
H_i=w+NA_i,
\quad
H_j=w+NA_j,
\quad
z_i=H_i/\ell_i,
\quad
z_j=H_j/\ell_j.
\]

Then

\[
\gcd(H_i,H_j)=\gcd(H_i,A_i-A_j)
\le |A_i-A_j|<B,
\tag{5}
\]

and, with no coprimality assumption on the denominators,

\[
\boxed{
\gcd(z_i,z_j)\mid\gcd(H_i,H_j),
\qquad
\gcd(z_i,z_j)<B.
}
\tag{6}
\]

Thus a prime larger than \(B\) cannot occur in reciprocal endpoints from two
different digits of one star. Equation (6) is only a divisibility and bound;
it does not claim equality after division by \(\ell_i,\ell_j\).

## Theorem 3 — release or a much wider reused row

For each digit \(A\in\{0,\ldots,B-1\}\), let

\[
\mathcal L_A=
\{\ell:\ell\text{ is eligible and }A_\ell=A\},
\qquad
L_A=\prod_{\ell\in\mathcal L_A}\ell.
\tag{7}
\]

Use the empty-product convention \(L_A=1\). Define \(S_A,R_A\) below only
when the bucket is occupied.

All primes in \(\mathcal L_A\) divide \(H_A=w+NA\). Define

\[
S_A=
\prod_{\ell\in\mathcal L_A}
\ell^{v_\ell(H_A)},
\qquad
R_A=\frac{H_A}{S_A}.
\tag{8}
\]

After retaining all endpoint presentations and running complete gcd-free
refinement, every non-anchor residual block contributed by the reciprocal
endpoints \(H_A/\ell\) divides \(R_A\). This statement concerns the
reciprocal \(H_A\)-side only; an old block supported only on the \(q\)-side
need not divide \(R_A\). Therefore:

\[
\boxed{
A=0,\ L_0>B
\quad\Longrightarrow\quad
R_0<N/B,
}
\tag{9}
\]

and

\[
\boxed{
A>0,\ L_A>B^2
\quad\Longrightarrow\quad
R_A<N/B.
}
\tag{10}
\]

In either threshold case (9) or (10), if \(R_A>1\), every reciprocal-side
residual block is small enough for the P121 size hypothesis. If \(R_A=1\),
the reciprocal-side residual is exhausted by the named anchor-prime powers.
Neither outcome by itself proves parity closure. Without the corresponding
threshold hypothesis, no bound \(R_A<N/B\) is claimed.

Now put

\[
n=\lceil\log_2(N+1)\rceil,
\qquad
B=n^3,
\qquad
n\ge64.
\]

Assume the P121 hypotheses for \(q\), and assume no bucket meets (9) or
(10):

\[
L_0\le B,
\qquad
L_A\le B^2\quad(A>0).
\tag{11}
\]

Let \(d\) be the number of occupied nonzero digits. Then

\[
\boxed{
d>
\frac{n^3}{25\log n}
-
\frac{n\log2}{3\log n}.
}
\tag{12}
\]

Here and only here, \(\log\) is natural. If \(r>B\) is prime and
\(v_r(q)\) is odd, at most one of these nonzero digits has
\(v_r(H_A)\) odd. Consequently, after global exact-value deduplication,
at least \(d-1\) distinct retained exact values have odd \(r\)-valuation,
unless a declared direct screen has already returned a factor.

Thus the P121 star has an exact trichotomy:

\[
\boxed{
\text{reciprocal-side small-block release, residual exhaustion,}
\quad\text{or}\quad
\Omega(n^3/\log n)\text{ distinct reused-row columns}.}
\tag{13}
\]

The second branch is not a dependency theorem.

## Theorem 4 — a noncanonical quasipolynomial expanding forest

Let \(\mathcal T\) be a full \(b\)-ary rooted tree of depth \(T\), where
\(b\ge2\). Give every
vertex \(v\) one binary row \(r_v\) and one column \(C_v\). Put a one in
row \(r_v\) of column \(C_v\), and, for a nonroot vertex, put one more one
in the row of its parent. Put zero in all other positions.

Then:

1. the matrix is unitriangular in any parent-before-child ordering;
2. its column kernel is zero;
3. every internal row has degree \(b+1\);
4. the residual child rows of one star are pairwise disjoint; and
5. degree-one peeling starts at the leaves and deletes every column.

The number of vertices is

\[
V=\frac{b^{T+1}-1}{b-1}.
\tag{14}
\]

For \(b=n^{O(1)}\) and \(T=O((\log n)^2)\),

\[
V=2^{O((\log n)^3)}.
\tag{15}
\]

This fits inside the declared quasipolynomial transcript budget. It proves
that row multiplicity, disjoint fresh rows, the current round cap, and the
state-size bound do not imply a dependency by abstract incidence counting.

This tree is deliberately noncanonical. It is not an integer relation
family and is not evidence that the complete feedback source fails.

## Theorem 5 — an exact canonical selected-source forest of depth two

There are infinitely many balanced, trial-hard, odd distinct-prime
semiprimes \(N=P Q\) for which the following five selected canonical exact
values form a two-generation forest.

Use the block primes and carries

\[
\begin{array}{c|ccccc}
v&0&1&2&3&4\\ \hline
q_v&5&11&19&23&37\\
k_v&2&7&17&18&36
\end{array}
\tag{16}
\]

and the anchored edges

\[
\begin{array}{c|cc}
\text{edge}&\ell&A\\ \hline
0\to1&3&1\\
0\to2&7&3\\
1\to3&13&1\\
2\to4&29&1.
\end{array}
\tag{17}
\]

The semiprimes lie in the CRT class

\[
\begin{aligned}
N&\equiv2\pmod {25},&
N&\equiv36\pmod {121},&
N&\equiv86\pmod {361},\\
N&\equiv60\pmod {529},&
N&\equiv1\pmod {1369},
\end{aligned}
\tag{18}
\]

and

\[
N\equiv2\pmod3,
\quad
N\equiv2\pmod7,
\quad
N\equiv5\pmod {13},
\quad
N\equiv4\pmod {29},
\quad
N\equiv1\pmod2.
\tag{19}
\]

Put \(C_v=1+k_vN\). Then

\[
\begin{aligned}
P_N(5)&=C_0,\\
P_N(15)=P_N(11)&=C_1,\\
P_N(35)=P_N(19)&=C_2,\\
P_N(143)=P_N(23)&=C_3,\\
P_N(551)=P_N(37)&=C_4.
\end{aligned}
\tag{20}
\]

The exact values are distinct. Their valuation-parity submatrix on the five
displayed block-prime rows is

\[
\boxed{
\begin{pmatrix}
1&1&1&0&0\\
0&1&0&1&0\\
0&0&1&0&1\\
0&0&0&1&0\\
0&0&0&0&1
\end{pmatrix}.}
\tag{21}
\]

It has full column rank. The rows \(23,37\) start a peeling cascade that
deletes all five selected columns, even if the values have additional prime
rows. For sufficiently large members of the family, every endpoint sign
screen in (20) is null.

This is an actual canonical-inverse family, but its scope is strict:

- it controls only the five selected values, not the complete source;
- its block primes are fixed small seeds, not the growing large rows in
  P121;
- unselected source columns can still create a dependency or factor; and
- it proves no normalized-root statement.

## Exact remaining gate

P121 cannot be iterated by simply feeding its complete new reciprocal
endpoint. A successful proof must force at least one operation absent from
the abstract forest:

1. a same-digit presentation bucket or old/cross-star overlap releases a
   proper block below \(N/B\);
2. wrapped, powered, or multi-block feedback closes large endpoints;
3. retained old columns close the fresh arm rows; or
4. a different arithmetic invariant forces a binary dependency and then a
   non-global normalized root.

For a negative result, an actual growing canonical family must control the
complete source. The abstract tree and the selected CRT family do not do so.
