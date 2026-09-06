# F139 statement — value-dependent pivot packing has a sharp rank boundary

## Status and scope

This is a candidate proof-and-certificate artifact. It has not passed a
hostile audit or a proof-blind reconstruction.

The result gives one exact positive theorem for a new source operation:
one public integer word can preserve many old private parity rows at once.
It also gives an exact negative boundary: simultaneous preservation does not
force a binary dependency. The result is not a complete-source obstruction,
a normalized-root theorem, or a factoring algorithm.

## Closest prior results and material difference

- P123/X75 prove that a wide one-parent anchored star can remain a peelable
  forest. They leave multi-block words open.
- P124/X76 prove a recenter-or-descend law for one released parent block.
  They explicitly leave value-dependent multi-block packing open.
- P125/X77 prove that row reuse requires a carry-class hit and that even
  complete row reuse need not cause a rank defect.

F139 makes the source operation materially different. It packs private
factor-free blocks owned by several old columns into one actual integer

\[
q<N/B,
\]

and then runs one complete anchored scan at that multi-owner word. This
creates a multi-parent layer, rather than another unary descendant or one
parent-child star. The positive theorem below is specific to that operation.
The negative result shows that the new operation still does not cross the
P125 rank gate by itself.

## Definitions

Let \(N\ge3\) be odd, let \(B\ge2\) be an integer, and let

\[
1<q<N/B,
\qquad
\gcd(q,N)=1.
\]

Write

\[
w=\iota_N(q)\in\{1,\ldots,N-1\},
\qquad
qw=1+kN.
\]

Here \(\iota_N(q)\) is the least positive inverse of \(q\) modulo \(N\).

For an **eligible integer anchor** \(\ell\le B\), meaning an integer with
\(1\le\ell\le B\) and \(\gcd(\ell,Nq)=1\), let
\(A_\ell\in\{0,\ldots,\ell-1\}\) be the unique carry digit with

\[
w+NA_\ell\equiv0\pmod\ell.
\]

If \(A=A_\ell\), put

\[
H_A=w+NA,
\qquad
c_\ell=\ell q,
\qquad
z_\ell=H_A/\ell,
\qquad
V_A=qH_A.
\]

Then \((c_\ell,z_\ell)\) is a canonical inverse pair and

\[
V_A=c_\ell z_\ell=1+(k+qA)N.
\]

Let \(D\subseteq\{1,\ldots,B-1\}\) be the set of occupied nonzero digits
in the completed anchor scan. Define

\[
\mathcal R_B(q)
=
\{r>B:\ r\text{ prime and }v_r(q)\text{ is odd}\}.
\]

Call \(A\in D\) **common-good** if

\[
v_r(H_A)\equiv0\pmod2
\quad\text{for every }r\in\mathcal R_B(q).
\]

Thus every large odd prime row of \(q\) remains odd in \(V_A\).

## Theorem 1 — simultaneous preservation

For each \(r\in\mathcal R_B(q)\), at most one digit in \(D\) is not
certified common-good by the test \(r\nmid H_A\). Consequently,

\[
\boxed{
\#\{A\in D:A\text{ is common-good}\}
\ge |D|-|\mathcal R_B(q)|.
}
\]

Moreover,

\[
\boxed{
|\mathcal R_B(q)|<\frac{\log q}{\log B}.
}
\]

In particular, when the P123 width branch supplies \(|D|=d\), at least

\[
d-\frac{\log q}{\log B}
\]

distinct occupied digits preserve all large odd rows of \(q\) at once.
The lower bound is interpreted as zero if its displayed right side is
negative.

This statement is stronger than applying P121 to one row at a time. The
same retained columns preserve the complete large odd support of the packed
word simultaneously.

## Theorem 2 — exact global-deduplication scope

Suppose the permanent old ledger contains distinct exact-value columns.
Assume that two primes

\[
r_1,r_2\in\mathcal R_B(q)
\]

are globally degree one in that full ledger and are owned by two different
old columns. Then every common-good \(V_A\) is different from every old
exact value. Different digits also give different exact values. Therefore
all common-good digits survive global first-occurrence exact-value
deduplication as new columns.

The word **globally** is necessary. A row that becomes degree one only after
earlier columns are removed by peeling does not give this conclusion. An
earlier removed column can contain that row, and a generated value can be an
old exact duplicate.

There is a factor-free public corollary. Refine the old values into a
pairwise-coprime P66 basis and split off every prime at most \(B\). Let
\(g_1,\ldots,g_t\) be nonsquare, \(B\)-rough residual blocks whose parity
rows are globally degree one and have distinct owner columns. If

\[
t\ge2,
\qquad
q=\prod_{i=1}^t g_i,
\qquad
q<N/B,
\]

then each \(g_i\) contains a hidden odd prime larger than \(B\), private to
its owner. The preceding deduplication conclusion applies to every
common-good digit. No factorization of the \(g_i\) is needed.

## Theorem 3 — conditional public packing cost

For an explicit quasipolynomial-size ledger and
\(B\le2^{(\log n)^{O(1)}}\), the following operation has
quasipolynomial cost.

1. Compute the complete factor-free basis and parity matrix.
2. Refine it against the public product of all primes at most \(B\).
3. Keep the nonsquare \(B\)-rough rows that are globally degree one.
4. For each owner column, keep its smallest qualifying block.
5. Sort these blocks and take the longest prefix whose product \(q\)
   satisfies \(Bq<N\).
6. Compute \(w=\iota_N(q)\), run \(\gcd(q-w,N)\) and
   \(\gcd(q+w,N)\), and stop with a factor if either screen is proper.
   Only on the null branch, run every anchored endpoint screen before
   exact-value deduplication.

The prefix has maximum cardinality among products using at most one listed
block from each owner. All operations use gcd, exact division, exact square
tests, sorting, and multiplication on the explicit transcript.

This is a conditional cost theorem only. There is no theorem that the two
smallest qualifying blocks have product below \(N/B\). The operation can
return fewer than two owners, in which case Theorem 2 gives no novelty
guarantee.

## Theorem 4 — exact multi-pivot splice law

Let an old binary parity matrix have globally private rows
\(p_1,\ldots,p_t\), owned by distinct columns
\(v_1,\ldots,v_t\). Let \(W\) contain the other old columns. Append new
columns \(u_1,\ldots,u_d\), each of which contains every row \(p_i\).
Delete the rows \(p_i\) and write the residual columns with hats.

Assume the old columns are independent. A dependency that selects the new
columns with a nonzero coefficient vector
\(\beta=(\beta_1,\ldots,\beta_d)\) exists exactly when

\[
\boxed{
\sum_{j=1}^d \beta_j
\left(
\widehat u_j+\sum_{i=1}^t\widehat v_i
\right)
\in\operatorname{colspan}(\widehat W).
}
\]

The pivot equations force every old owner coefficient to equal

\[
s=\sum_j\beta_j.
\]

Thus multi-pivot packing contracts all selected owner pivots to one exact
residual-class test. It does not make that test pass.

## Theorem 5 — scalable abstract countermodel

For arbitrary \(t\ge2\) and \(d\ge1\), take old pivot rows
\(p_1,\ldots,p_t\), fresh rows \(h_1,\ldots,h_d\), old columns

\[
v_i=e_{p_i},
\]

and new columns

\[
u_j=e_{p_1}+\cdots+e_{p_t}+e_{h_j}.
\]

Every new column preserves all \(t\) old private rows simultaneously. All
old pivots now have degree \(d+1\). Nevertheless, the \(h_j\) rows are
private, the complete matrix has rank \(t+d\), and degree-one peeling deletes
every column.

This is a multi-parent peelable incidence system. It realizes the
parity-incidence pattern
left possible after Theorems 1 and 2, but it has zero kernel.

## Theorem 6 — selected canonical certificate at \(N=989\)

Take

\[
N=989=23\cdot43,
\qquad
B=5.
\]

The two old canonical relations are

\[
\begin{aligned}
P_N(2)&=2\cdot495=990=1+N
=2\cdot3^2\cdot5\cdot11,\\
P_N(16)&=16\cdot680=10880=1+11N
=2^7\cdot5\cdot17.
\end{aligned}
\]

Rows \(11\) and \(17\) have degree one and different owners in this frozen
two-column selected ledger. Refinement against the public primes at most five
exposes both as \(B\)-rough blocks. This certificate does **not** claim that
the rows are degree one in the complete F26-Q ledger or in the complete
canonical universe. Pack the two selected blocks:

\[
q=11\cdot17=187<N/5,
\qquad
\iota_N(q)=238,
\qquad
187\cdot238=44506=1+45N.
\]

The packed base screen is null:

\[
\gcd(187-238,N)=\gcd(187+238,N)=1.
\]

Every integer anchor \(1\le\ell\le5\) is eligible. The complete registered
anchor scan is:

\[
\begin{array}{c|c|c|c|c|c}
\ell&A_\ell&c_\ell&z_\ell&\kappa&c_\ell z_\ell\\ \hline
1&0&187&238&45&44506\\
2&0&374&119&45&44506\\
3&1&561&409&232&229449\\
4&2&748&554&419&414392\\
5&3&935&641&606&599335.
\end{array}
\]

The four distinct anchor values factor as

\[
\begin{aligned}
44506&=2\cdot7\cdot11\cdot17^2,\\
229449&=3\cdot11\cdot17\cdot409,\\
414392&=2^3\cdot11\cdot17\cdot277,\\
599335&=5\cdot11\cdot17\cdot641.
\end{aligned}
\]

Thus all three nonzero digits preserve rows \(11\) and \(17\). The two
zero-digit endpoint presentations are exact duplicates. Their endpoint
screens both run, and the selected relation ledger keeps one column.

For every displayed endpoint pair \((c,z)\),

\[
\gcd(c-z,N)=\gcd(c+z,N)=1.
\]

On rows

\[
(2,3,5,7,11,17,277,409,641)
\]

and columns

\[
(P_N(2),P_N(16),V_0,V_1,V_2,V_3),
\]

the parity matrix is

\[
\begin{pmatrix}
1&1&1&0&1&0\\
0&0&0&1&0&0\\
1&1&0&0&0&1\\
0&0&1&0&0&0\\
1&0&1&1&1&1\\
0&1&0&1&1&1\\
0&0&0&0&1&0\\
0&0&0&1&0&0\\
0&0&0&0&0&1
\end{pmatrix}.
\]

It has rank six and zero kernel. Rows \(7,3,277,641\) first peel the four
new columns. Rows \(11,17\) then peel the two old columns. Hence the exact
canonical layer reuses both packed selected pivots in every nonzero-digit
column, keeps four values distinct from the two selected old values, and
still does not create a dependency.

This is a selected-source certificate. It does not control the complete
F26-Q source at \(N=989\), global exact-value ordering outside the registered
six columns, or row degrees outside the registered old ledger. In particular,
it is not a hard all-source input or an integer-factoring counterexample.

## Exact failure statement

The following implication is false, even for canonical inverse relations
with null endpoint sign screens:

\[
\boxed{
\text{pack several global private pivots}
\;\Longrightarrow\;
\text{preserve them in many new columns}
\;\Longrightarrow\;
\text{rank defect}.}
\]

The first implication has the conditional counting theorem in Theorem 1 when
the occupied digit set is wide enough. The second implication fails because
every new cofactor can supply a fresh independent pivot.

## Next materially new gate

A valid retry must target the shifted residual classes from Theorem 4, not
only the packed pivot rows. It must prove one of the following all-input
alternatives within the declared quasipolynomial budget:

1. a qualifying product \(q<N/B\) exists and the shifted residual classes
   are linearly dependent modulo the remaining old columns;
2. failure to form such a product forces a different exact source progress
   event; or
3. repeated residual-aware repacking decreases a proved global potential
   faster than it creates fresh private rows.

No such potential is known. Column count, pivot degree, 2-core size, and
total private-row count are not monotone under the abstract peelable
incidence system.
After a rank defect, a separate theorem must still prove a non-global
normalized-root image.
