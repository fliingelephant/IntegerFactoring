# F139 final proof-blind reconstruction V2

## Source boundary and verdict

This reconstruction used only `STATEMENT.md`. I did not inspect a proof,
manifest, audit, prior blind report, verifier output, ledger, or predecessor
artifact.

The SHA-256 of the reconstructed statement is

```text
a01cd50a749a61d70aefac9b50fca91e4a87332ef882c343fccc07009b75f27b
```

**Verdict: PASS.** All six theorems follow from their stated assumptions. The
selected certificate at (N=989) is arithmetically exact. It has canonical
endpoints, null sign screens, four globally new selected-ledger values, rank
six, zero kernel, and the claimed complete peel order. The certificate proves
only the selected-source negative boundary claimed in the statement.

## Preliminary canonical facts

Let (A=A_\ell). Since \(\gcd(\ell,N)=1\), the congruence

\[
w+NA\equiv 0\pmod \ell
\]

has exactly one solution in \(\{0,\ldots,\ell-1\}\). Hence (z_\ell) is an
integer. Also

\[
1\le c_\ell=\ell q\le Bq<N.
\]

Using (1\le w\le N-1) and (0\le A\le\ell-1),

\[
0<H_A=w+NA\le (N-1)+N(\ell-1)=N\ell-1.
\]

Therefore

\[
1\le z_\ell=H_A/\ell<N.
\]

Finally,

\[
c_\ell z_\ell=qH_A=qw+qNA
=1+(k+qA)N\equiv1\pmod N.
\]

Thus (z_\ell) is the least positive inverse of (c_\ell) modulo (N),
and every registered pair is canonical. The value depends only on the digit:

\[
V_A=q(w+NA).
\]

Consequently, equal digits give equal exact values even if their endpoint
presentations differ, while different digits give different exact values.

## Theorem 1: simultaneous preservation

Fix (r\in\mathcal R_B(q)). Because (r\mid q) and \(\gcd(q,N)=1\), one has
\(r\nmid N\). If (r\mid H_A) and (r\mid H_{A'}), then

\[
r\mid H_A-H_{A'}=N(A-A'),
\]

so (r\mid A-A'). For distinct occupied nonzero digits,

\[
0<|A-A'|\le B-2<r,
\]

which is impossible. Thus at most one digit in (D) is divisible by a fixed
(r).

Let (E_r=\{A\in D:r\mid H_A\}). Every digit outside
\(\bigcup_{r\in\mathcal R_B(q)}E_r\) has (v_r(H_A)=0) for every relevant
row, so it is common-good. The union bound gives

\[
\#\{A\in D:A\text{ is common-good}\}
\ge |D|-\sum_r|E_r|
\ge |D|-|\mathcal R_B(q)|.
\]

This argument does not incorrectly discard a digit with a positive even
valuation: such a digit is common-good too. The divisibility test is only a
sufficient certificate, which is all the lower bound needs.

Put (m=|\mathcal R_B(q)|). The distinct primes in this set have odd positive
valuation in (q), so their product divides (q). Since every one is
strictly larger than (B),

\[
B^m<\prod_{r\in\mathcal R_B(q)}r\le q.
\]

Taking logarithms proves

\[
m<\frac{\log q}{\log B}.
\]

The stated width consequence is immediate after substituting (|D|=d).
The reference to a P123 branch is conditional and is not needed for this
deduction.

## Theorem 2: exact global deduplication

For a common-good digit and any (r\in\mathcal R_B(q)),

\[
v_r(V_A)=v_r(q)+v_r(H_A)\equiv1+0\equiv1\pmod2.
\]

In particular, (V_A) contains both private rows (r_1) and (r_2) with
odd parity. No old column can contain both. The unique old owner of (r_1)
is different from the unique old owner of (r_2), and every other old
column contains neither row. Equality with an old exact value would force
equality of all prime valuations and hence of these two parity entries. This
is impossible.

For (A\ne A'),

\[
V_A-V_{A'}=qN(A-A')\ne0.
\]

Thus the common-good values are mutually distinct and are absent from the
old exact-value ledger. First-occurrence exact-value deduplication retains
one new column for each such digit.

The word "globally" is essential. At parity-incidence level, take old
columns with supports

\[
\{r_1,r_2,h\},\qquad \{r_1\},\qquad \{r_2\}.
\]

The first column peels on its private row (h). After its removal, (r_1)
and (r_2) are degree one with different remaining owners. A generated
column equal to that first old exact value nevertheless contains both rows
and is an old duplicate. Post-peel privacy therefore cannot replace global
privacy in the proof above.

For the factor-free corollary, write every old value in a pairwise-coprime
basis. A nonsquare block (g_i) has some prime (r_i\mid g_i) with
(v_{r_i}(g_i)) odd. Since the block is (B)-rough, (r_i>B). Since the
basis is pairwise coprime, no other basis block contains (r_i). Therefore
the prime parity row of (r_i) across the old columns equals the parity row
of (g_i), and it is globally degree one at the same owner. Distinct blocks
give distinct primes. In

\[
q=\prod_i g_i,
\]

each selected (r_i) has odd valuation, so (r_i\in\mathcal R_B(q)). With
(t\ge2), any two selected blocks supply the two rows required above. Also,
each block divides an old relation value coprime to (N), so
\(\gcd(q,N)=1\). This is an existence argument about hidden primes; it does
not require factoring a block.

## Theorem 3: conditional quasipolynomial cost

Let the total explicit transcript length be quasipolynomial in (n). A
complete factor-free refinement needs only polynomially many nontrivial gcd
splits and exact divisions in that explicit length. Exponents, their parity,
and nonsquare status follow by exact division and exact square tests.

The product of all primes at most (B) has bit length at most

\[
\pi(B)\log_2 B\le B\log_2 B.
\]

This is quasipolynomial when
\(B\le2^{(\log n)^{O(1)}}\). It can also be constructed within that bound
using only factor-free refinement of the explicit list
\(2,3,\ldots,B\): because every prime (p\le B) itself occurs in the list,
the final pairwise-coprime basis separates every such (p). Thus no hidden
integer factorization is being assumed in the small-prime refinement.

There are at most quasipolynomially many basis rows and owner columns.
Selecting minima and sorting them has quasipolynomial cost. Prefix products
can be stopped when they cross (N/B). Extended Euclid computes the inverse
and its gcd certificate in polynomial bit complexity. There are at most
(B) integer anchors. Their carry digits, canonical endpoints, two gcd
screens per presentation, and the subsequent exact-value sorting or
deduplication all have quasipolynomial cost. Even a naive scan of all carry
digits costs (O(B^2)), still quasipolynomial. Running screens before
deduplication is important because one exact value can have more than one
endpoint presentation.

It remains to check the optimization claim. Let (m_i) be the smallest
qualifying block for owner (i), and sort them as

\[
m_1\le m_2\le\cdots\le m_s.
\]

Every choice of (k) owners and one qualifying block from each has product
at least the product of the corresponding owner minima, which in turn is at
least (m_1\cdots m_k). Hence a feasible (k)-owner product exists exactly
only if the (k)-term smallest-minima prefix is feasible. The longest
prefix therefore has maximum cardinality.

None of these cost or optimality facts forces the prefix length to be at
least two. If (Bm_1m_2\ge N), the claimed two-owner operation is
unavailable. The theorem correctly states this as a conditional cost result,
not an existence result.

## Theorem 4: exact multi-pivot splice law

Work over \(\mathbf F_2\). Give the old owner columns coefficients
\(\alpha_i\), the other old columns coefficients \(\gamma_w\), and the new
columns the fixed nonzero vector \(\beta\). In pivot row (p_i), the
dependency equation is

\[
\alpha_i+\sum_{j=1}^d\beta_j=0.
\]

Thus every owner coefficient is forced to the same bit

\[
s=\sum_j\beta_j.
\]

After deleting the pivot rows, the remaining equation is

\[
\sum_j\beta_j\widehat u_j
+s\sum_i\widehat v_i
+\sum_{w\in W}\gamma_w\widehat w=0.
\]

Since

\[
s\sum_i\widehat v_i
=\sum_j\beta_j\sum_i\widehat v_i,
\]

such coefficients \(\gamma_w\) exist exactly when

\[
\sum_j\beta_j
\left(\widehat u_j+\sum_i\widehat v_i\right)
\in\operatorname{colspan}(\widehat W).
\]

This proves both directions. A nonzero \(\beta\) makes the resulting
dependency nontrivial. Old-column independence ensures the issue under test
is genuinely a new dependency, rather than one already present in the old
ledger. The pivot equations impose the contraction, but they do not force
the residual membership test to pass.

## Theorem 5: scalable peelable countermodel

Consider a putative dependency

\[
\sum_i\alpha_i v_i+\sum_j\beta_j u_j=0.
\]

Row (h_j) occurs only in (u_j), so it forces \(\beta_j=0\). After all
new coefficients vanish, row (p_i) forces \(\alpha_i=0\). The (t+d)
columns are therefore independent and the rank is (t+d).

Each (p_i) initially has degree (d+1): it occurs in (v_i) and in all
(d) new columns. Each (h_j) has degree one. Peel (u_1,\ldots,u_d) on
the rows (h_1,\ldots,h_d). The remaining (p_i) rows then have degree one
and peel (v_1,\ldots,v_t). Thus every column peels although every new
column simultaneously contains every old pivot. This proves the abstract
zero-kernel boundary for all (t\ge2) and (d\ge1).

## Theorem 6: independent reconstruction at (N=989)

### Old relations and packed base

Direct calculation gives

\[
989=23\cdot43,
\]

and

\[
2^{-1}\bmod989=495,\qquad16^{-1}\bmod989=680.
\]

The old exact values are

\[
2\cdot495=990=1+989=2\cdot3^2\cdot5\cdot11,
\]

\[
16\cdot680=10880=1+11\cdot989=2^7\cdot5\cdot17.
\]

All four endpoints lie in \([1,988]\). In the two-column parity ledger,
row (11) occurs only in the first column and row (17) only in the
second. Removing the public rows (2,3,5) from the factor-free basis leaves
the nonsquare (5)-rough blocks (11) and (17).

Their product is

\[
q=187,\qquad5q=935<989,\qquad\gcd(q,989)=1.
\]

Moreover,

\[
w=187^{-1}\bmod989=238,
\]

because

\[
187\cdot238=44506=1+45\cdot989.
\]

The base sign quantities are (-51) and (425), and

\[
\gcd(-51,989)=\gcd(425,989)=1.
\]

### Complete anchor scan and canonical ranges

The prime factors of (Nq) are (11,17,23,43). Hence every
\(\ell\in\{1,2,3,4,5\}\) is eligible. Solving the five carry congruences
gives the following independently reconstructed table.

| \(\ell\) | \(A_\ell\) | \(c_\ell\) | \(z_\ell\) | \(\kappa=(c_\ell z_\ell-1)/989\) | \(c_\ell z_\ell\) | \(c_\ell-z_\ell\) | \(c_\ell+z_\ell\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 187 | 238 | 45  | 44506  | -51 | 425  |
| 2 | 0 | 374 | 119 | 45  | 44506  | 255 | 493  |
| 3 | 1 | 561 | 409 | 232 | 229449 | 152 | 970  |
| 4 | 2 | 748 | 554 | 419 | 414392 | 194 | 1302 |
| 5 | 3 | 935 | 641 | 606 | 599335 | 294 | 1576 |

Every (c_\ell) and (z_\ell) is in \([1,988]\), and every displayed
product is (1\bmod989). Direct gcd evaluation gives

\[
\gcd(c_\ell-z_\ell,989)
=\gcd(c_\ell+z_\ell,989)=1
\]

for all five rows. Thus all ten endpoint screens are null. The two
zero-digit presentations have the same exact value (44506), but both
screens are legitimately run before exact-value deduplication. The occupied
nonzero digit set is

\[
D=\{1,2,3\}.
\]

### Preservation, factorization, and exact deduplication

Here

\[
\mathcal R_5(187)=\{11,17\},
\qquad
2<\frac{\log187}{\log5}=3.25027053013\ldots.
\]

The carry numerators for the occupied nonzero digits are

\[
H_1=1227=3\cdot409,
\]

\[
H_2=2216=2^3\cdot277,
\]

\[
H_3=3205=5\cdot641.
\]

None is divisible by (11) or (17), so all three digits are
common-good. For comparison,
\(H_0=238=2\cdot7\cdot17\), so the zero digit does not preserve the
(17)-row parity.

The four distinct registered values factor as

\[
44506=2\cdot7\cdot11\cdot17^2,
\]

\[
229449=3\cdot11\cdot17\cdot409,
\]

\[
414392=2^3\cdot11\cdot17\cdot277,
\]

\[
599335=5\cdot11\cdot17\cdot641.
\]

They are pairwise distinct and none equals (990) or (10880). Thus
deduplication keeps one zero-digit value and all three nonzero-digit values.
Theorem 2 already certifies novelty for the three common-good values; the
zero-digit value is new here by direct comparison.

### Parity matrix, rank, splice check, and peeling

On the stated row and column orders, direct valuation parity gives

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

This exactly matches the statement. It has an immediate six-pivot order:

- row (7) pivots (V_0);
- row (3) pivots (V_1);
- row (277) pivots (V_2);
- row (641) pivots (V_3);
- after those columns are removed, row (11) pivots (P_N(2));
- row (17) pivots (P_N(16)).

Therefore all six columns are independent. The rank is six and the right
kernel is zero. This same order is a valid degree-one peel sequence. The
four first rows are degree one in the full matrix, and after their columns
are removed the two old private rows are degree one.

The splice law gives the same conclusion. Delete rows (11,17). The two
old residual columns both have support \(\{2,5\}\), so their sum is zero.
The four shifted residual new columns are therefore just the four new
residual columns. They have rank four, witnessed respectively by the fresh
rows (7,3,277,641). Since there are no other old columns in this selected
ledger, no nonzero \(\beta\) passes the residual span test.

## Exact boundary reconstructed

Within the frozen selected ledger, (11) and (17) are global private
pivots with different owners. The canonical packed operation preserves both
in all three nonzero-digit columns. Every endpoint sign screen is null. Yet
the resulting six-column parity matrix has full column rank and peels to
empty. This is a direct canonical counterexample to the claimed false
implication from simultaneous pivot preservation to a rank defect.

Nothing in this reconstruction promotes selected-ledger privacy to privacy
in a larger source, controls earlier exact values outside the six registered
columns, or produces a factoring algorithm. Those limitations are necessary
and agree with the statement's declared scope.
