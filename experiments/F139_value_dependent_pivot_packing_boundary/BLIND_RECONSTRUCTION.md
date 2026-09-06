# F139 proof-blind reconstruction

## Verdict

**PASS, with two terminology qualifications.** The mathematical content of
Theorems 1--6 is correct under the standard meanings of modular inverse,
binary parity row, and factor-free basis. Every displayed assertion in the
selected \(N=989\) certificate recomputes exactly. I found no rank defect and
no failed sign screen.

Two points are not self-contained in the statement.

1. The statement does not define \(\iota_N(q)\). The canonical endpoint claim
   needs \(\iota_N(q)\) to be the unique inverse in
   \(\{1,\ldots,N-1\}\). The equation \(qw=1+kN\) alone is not sufficient:
   replacing \(w\) by \(w+mN\) preserves that equation but can put an endpoint
   outside the canonical range.
2. The word **hyperforest** has more than one standard meaning. Theorem 5 is
   a full-rank, degree-one-peelable hyperforest. It is not a Berge forest (an
   incidence-graph forest) when \(t,d\ge2\), since
   \(p_1-u_1-p_2-u_2-p_1\) is an incidence cycle. The precise full-rank and
   peeling claims are correct.

These qualifications do not change the simultaneous-preservation theorem,
the deduplication theorem, the splice law, the countermodel, or the finite
certificate.

## Evidence boundary and source hash

I used only `STATEMENT.md`. I did not read a proof, manifest, audit, verifier,
output, ledger, predecessor artifact, or any other F139 file.

The SHA-256 of the statement used for this reconstruction is

```text
90f89961e4fb9f2a16bd8027cd6ea21092c3794e2e4994254b3ac7f57e04e148
```

It equals the expected hash.

## Canonical endpoint construction

In this section, take \(w=\iota_N(q)\) to mean \(1\le w<N\) and
\(qw\equiv1\pmod N\).

For an eligible \(\ell\), \(\gcd(\ell,N)=1\). Thus multiplication by \(N\)
is invertible modulo \(\ell\), so exactly one

\[
A_\ell\in\{0,\ldots,\ell-1\}
\]

satisfies \(w+NA_\ell\equiv0\pmod\ell\). Hence \(z_\ell\) is an integer.
The endpoint ranges are exact:

\[
0<c_\ell=\ell q\le Bq<N,
\]

and

\[
0<H_A=w+NA\le (N-1)+N(\ell-1)<\ell N.
\]

Since \(H_A\) is a positive multiple of \(\ell\), this gives
\(1\le z_\ell<N\). Also

\[
c_\ell z_\ell=(\ell q)(H_A/\ell)
=q(w+NA)=1+(k+qA)N.
\]

Thus both endpoints are in \(\{1,\ldots,N-1\}\), their product is \(1\)
modulo \(N\), and both endpoints are coprime to \(N\). This proves the stated
canonical inverse-pair property under the stated interpretation of
\(\iota_N\).

## Theorem 1: simultaneous preservation

Fix \(r\in\mathcal R_B(q)\), and define

\[
E_r=\{A\in D:r\mid H_A\}.
\]

If \(A,A'\in E_r\), then

\[
r\mid H_A-H_{A'}=N(A-A').
\]

The prime \(r\) divides \(q\), while \(\gcd(q,N)=1\), so \(r\nmid N\).
It follows that \(r\mid A-A'\). But \(A,A'\in\{1,\ldots,B-1\}\) and
\(r>B\), so \(|A-A'|<r\). Hence \(A=A'\), and

\[
|E_r|\le1.
\]

For every \(A\notin E_r\), \(v_r(H_A)=0\), which is even. Therefore every
digit outside \(\bigcup_{r\in\mathcal R_B(q)}E_r\) is common-good. The union
bound gives

\[
\#\{A\in D:A\text{ is common-good}\}
\ge |D|-|\mathcal R_B(q)|.
\]

This is a simultaneous statement. The retained set is the complement of one
union over all large odd rows. It is not a different set for each row.

Let \(m=|\mathcal R_B(q)|\). Each prime in this set divides \(q\), and the
primes are distinct. Thus

\[
q\ge\prod_{r\in\mathcal R_B(q)}r>B^m.
\]

The inequality is strict because every \(r>B\). Consequently

\[
m<\frac{\log q}{\log B}.
\]

For \(m=0\), the same displayed inequality follows from \(q>1\). If
\(|D|=d\), the integer count is in fact strictly greater than
\(d-\log(q)/\log(B)\), so the statement's weaker “at least” wording is valid.
Replacing a negative lower bound by zero is also valid.

## Theorem 2: exact global deduplication

Let \(r_1,r_2\) be the two distinct globally private rows, with different
owner columns. If \(A\) is common-good, then

\[
v_{r_i}(V_A)=v_{r_i}(q)+v_{r_i}(H_A)\equiv1+0\equiv1\pmod2
\]

for \(i=1,2\). Suppose \(V_A\) equaled an old exact value \(X\). The column
of \(X\) would contain both rows \(r_1\) and \(r_2\). Global degree one would
make that column the owner of each row. This contradicts the premise that
the owners are different. Hence no common-good value is an old exact value.

For two different digits,

\[
V_A-V_{A'}=qN(A-A')\ne0.
\]

Thus different common-good digits also have different exact values. Global
first-occurrence deduplication retains one new column for each such digit.
Several anchors can present the same digit, but that does not create more
than one value for that digit.

The word **globally** has the stated exact scope: degree one is measured in
the full frozen old ledger before peeling. Degree one only in a residual
ledger is insufficient. For example, old parity columns with exact values
\(30,2,3\) have rows \(2\) and \(3\) in the first column and in their
respective singleton columns. Row \(5\) peels the \(30\) column. Rows \(2\)
and \(3\) are then private to different surviving columns, but a later exact
value \(30\) is still an old duplicate. This is precisely the failure that
global privacy excludes.

For the factor-free corollary, write the exponent of a pairwise-coprime
basis block \(g_i\) in old column \(X_j\) as \(e_{ji}\). Since \(g_i\) is not
a square, it has a prime \(p_i\) with odd \(v_{p_i}(g_i)\). Since it is
\(B\)-rough, \(p_i>B\ge2\), so \(p_i\) is odd. Pairwise coprimality means that
\(p_i\) occurs in no other basis block. Therefore

\[
v_{p_i}(X_j)\equiv e_{ji}\pmod2.
\]

The basis row being globally degree one makes \(p_i\) a globally private
prime row with the same owner. In
\(q=\prod_i g_i\), \(v_{p_i}(q)=v_{p_i}(g_i)\) is odd, so
\(p_i\in\mathcal R_B(q)\). Distinct blocks give distinct \(p_i\). When
\(t\ge2\), any two give Theorem 2's two different private owners. No
factorization is needed by the operation; existence of \(p_i\) is enough for
the proof.

## Theorem 3: conditional public packing cost

The cost claim is correct as a conditional claim for explicitly encoded
input. If the ledger size is quasipolynomial in the size parameter \(n\),
then pairwise gcd refinement and exact division take polynomial time in that
explicit size. A complete gcd-free basis has at most the total number of
input prime occurrences counted with bit-length multiplicity, so its
explicit representation and the standard refinement process remain within
that bound.

The primorial through \(B\) has at most \(B\) factors and bit length at most
\(B\log_2 B\). Both are quasipolynomial when

\[
B\le2^{(\log n)^{O(1)}}.
\]

It can be supplied as the stated public product or generated by a sieve in
quasipolynomial time. Refinement against it uses gcd and exact division. The
remaining work uses exact square tests, comparisons, sorting, multiplication,
extended gcd for inversion, and \(B\) endpoint gcd screens. Exact-value
deduplication on the explicit generated list is also quasipolynomial. No
factorization of the residual blocks is required.

The maximum-cardinality prefix assertion follows from order statistics. Let
\(a_i\) be the smallest qualifying block for owner \(i\), and sort them as

\[
a_1\le a_2\le\cdots\le a_m.
\]

Every choice of \(s\) different owners, even if it uses a different
qualifying block for an owner, has product at least
\(a_1a_2\cdots a_s\). Hence, if the prefix of length \(s\) fails
\(Bq<N\), every selection of \(s\) owners fails it. The longest feasible
prefix has maximum cardinality.

This proof gives no lower bound on that cardinality. The returned prefix can
have zero or one owner. If it is empty, its product is \(1\), and the
\(q>1\) setup for Theorems 1 and 2 is not activated. If it has one owner,
Theorem 2's two-owner novelty premise is not activated. These are scope
conditions, not cost failures. The statement correctly makes no existence
claim for two blocks below \(N/B\).

## Theorem 4: exact multi-pivot splice law

Work over \(\mathbf F_2\). Give owner \(v_i\) coefficient \(\alpha_i\), give
the new columns coefficients \(\beta_j\), and let the other old-column
coefficients be \(\gamma\). Put

\[
s=\sum_{j=1}^d\beta_j.
\]

At pivot row \(p_i\), only old column \(v_i\) and all new columns are present.
The dependency equation at that row is

\[
\alpha_i+s=0.
\]

Thus every owner coefficient is forced to the same value,
\(\alpha_i=s\). After deleting the pivot rows, the residual dependency
equation is

\[
\sum_{w\in W}\gamma_w\widehat w
+s\sum_{i=1}^t\widehat v_i
+\sum_{j=1}^d\beta_j\widehat u_j=0.
\]

Since \(s=\sum_j\beta_j\), the last two terms equal

\[
\sum_{j=1}^d\beta_j
\left(\widehat u_j+\sum_{i=1}^t\widehat v_i\right).
\]

Therefore a dependency with \(\beta\ne0\) implies that this shifted sum is
in \(\operatorname{colspan}(\widehat W)\). Conversely, if the shifted sum is
in that column span, choose witnessing coefficients \(\gamma\), set every
\(\alpha_i=s\), and restore the pivot rows. All pivot and residual equations
then vanish. This proves both directions and all quantifiers of the boxed
law. Old-column independence ensures there was no old-only dependency; the
algebraic equivalence for nonzero \(\beta\) is exact even before using that
extra premise.

## Theorem 5: scalable countermodel

In a dependency, give \(v_i\) coefficient \(\alpha_i\) and \(u_j\)
coefficient \(\beta_j\). Row \(h_j\) occurs only in \(u_j\), so every
\(\beta_j=0\). Row \(p_i\) then occurs only in \(v_i\) among columns with a
possibly nonzero coefficient, so every \(\alpha_i=0\). All \(t+d\) columns
are independent. The rank is therefore \(t+d\), and the kernel is zero.

Each \(p_i\) initially has degree \(d+1\): it occurs in \(v_i\) and in all
\(d\) new columns. Each \(h_j\) has degree one. Peeling on the \(h_j\) rows
deletes all \(u_j\). Each \(p_i\) then has degree one and peels \(v_i\). Thus
degree-one peeling deletes every column for every \(t\ge2,d\ge1\).

This proves the intended peelable or matroidal hyperforest claim. As noted in
the verdict, it does not prove Berge acyclicity, and Berge acyclicity is
false for \(t,d\ge2\). The statement's precise rank and peeling facts are
unambiguous and correct.

## Theorem 6: independent \(N=989\) certificate check

### Old selected relations and packed word

The modulus and old relations recompute as

\[
989=23\cdot43,
\]

\[
2^{-1}\bmod989=495,
\qquad
2\cdot495=990=1+989
=2\cdot3^2\cdot5\cdot11,
\]

and

\[
16^{-1}\bmod989=680,
\qquad
16\cdot680=10880=1+11\cdot989
=2^7\cdot5\cdot17.
\]

In this two-column ledger, row \(11\) occurs only in the first column and row
\(17\) only in the second. Removing the prime factors at most \(5\) leaves
the nonsquare \(5\)-rough blocks \(11\) and \(17\).

Their product satisfies

\[
q=187=11\cdot17,
\qquad 5q=935<989,
\qquad \gcd(q,N)=1.
\]

The least positive inverse is \(w=238\), because

\[
187\cdot238=44506=1+45\cdot989.
\]

The base signs are null:

\[
\gcd(187-238,989)=\gcd(-51,989)=1,
\]

\[
\gcd(187+238,989)=\gcd(425,989)=1.
\]

Since

\[
Nq=11\cdot17\cdot23\cdot43,
\]

every \(\ell\in\{1,2,3,4,5\}\) is eligible.

### Complete anchor scan

Solving \(238+989A\equiv0\pmod\ell\) gives the following independent table.
Here \(H=238+989A\) and \(\kappa=(V-1)/989\).

| \(\ell\) | \(A\) | \(H\) | \(c=187\ell\) | \(z=H/\ell\) | \(\kappa\) | \(V=cz\) | \(\gcd(c-z,N)\) | \(\gcd(c+z,N)\) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 238  | 187 | 238 | 45  | 44506  | 1 | 1 |
| 2 | 0 | 238  | 374 | 119 | 45  | 44506  | 1 | 1 |
| 3 | 1 | 1227 | 561 | 409 | 232 | 229449 | 1 | 1 |
| 4 | 2 | 2216 | 748 | 554 | 419 | 414392 | 1 | 1 |
| 5 | 3 | 3205 | 935 | 641 | 606 | 599335 | 1 | 1 |

Every \(c\) and \(z\) in the table lies in \(\{1,\ldots,988\}\). The two
\(A=0\) presentations have the same exact product but different endpoint
pairs. Both pairs pass both sign screens. Exact-value deduplication therefore
keeps one \(V_0\) column.

For completeness, the exact sign inputs for all displayed old and new
endpoint pairs are:

| \((c,z)\) | \(c-z\) | \(c+z\) | gcd minus | gcd plus |
|---|---:|---:|---:|---:|
| \((2,495)\) | -493 | 497 | 1 | 1 |
| \((16,680)\) | -664 | 696 | 1 | 1 |
| \((187,238)\) | -51 | 425 | 1 | 1 |
| \((374,119)\) | 255 | 493 | 1 | 1 |
| \((561,409)\) | 152 | 970 | 1 | 1 |
| \((748,554)\) | 194 | 1302 | 1 | 1 |
| \((935,641)\) | 294 | 1576 | 1 | 1 |

All gcds are with \(989\).

### Factorization, occupied digits, and deduplication

The four exact anchor values factor as

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

Trial division through the square roots confirms that \(277,409,641\) are
prime. These factorizations multiply back to the displayed values.

Here

\[
\mathcal R_5(187)=\{11,17\},
\qquad D=\{1,2,3\}.
\]

The corresponding nonzero-digit cofactors are

\[
H_1=1227=3\cdot409,
\quad
H_2=2216=2^3\cdot277,
\quad
H_3=3205=5\cdot641.
\]

None is divisible by \(11\) or \(17\). Thus all three nonzero digits are
common-good and preserve both old private parity rows. The zero-digit
cofactor is \(H_0=238=2\cdot7\cdot17\), so \(V_0\) has even \(17\)-valuation;
the statement does not claim that digit zero is common-good.

The four new exact values are pairwise distinct and are all different from
\(990\) and \(10880\). Thus the finite deduplication assertion holds even for
\(V_0\), while Theorem 2 already guarantees it for the three common-good
digits.

### Parity matrix, rank, and peeling

On the stated row and column orders, independent parity extraction gives

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

This exactly matches the displayed matrix. The following degree-one rows
give the stated peeling sequence:

| row | unique active column | exact value |
|---:|---|---:|
| 7 | \(V_0\) | 44506 |
| 3 | \(V_1\) | 229449 |
| 277 | \(V_2\) | 414392 |
| 641 | \(V_3\) | 599335 |
| 11 | \(P_N(2)\) | 990 |
| 17 | \(P_N(16)\) | 10880 |

At each step, the listed row has degree one among the remaining columns.
This peels all six columns. In any binary dependency, the unique row forces
the coefficient of its incident column to zero, step by step. Hence all six
columns are independent, the rank is \(6\), and the kernel dimension is
\(6-6=0\).

The certificate therefore packs two private selected-ledger pivots, preserves
both in three nonzero-digit new columns, passes every displayed sign screen,
and still has no dependency.

## Failure implication and scope

Theorem 5 refutes the parity-only implication for all \(t\ge2,d\ge1\). The
selected \(N=989\) certificate also refutes it inside the canonical inverse
construction with null endpoint screens. Fresh cofactor rows can force all
new coefficients to zero before the reused pivots can create a dependency.
Theorem 4 identifies the missing condition exactly: a nonzero shifted
residual combination must land in the span of the remaining old columns.

The finite calculation proves only the frozen six-column selected ledger.
It gives no information about row degrees or first-occurrence ordering in an
unread larger ledger, no complete-source obstruction, no all-input factoring
claim, and no normalized-root theorem. Historical claims about predecessor
artifacts and the epistemic claim that no potential is known are outside a
statement-only proof reconstruction.
