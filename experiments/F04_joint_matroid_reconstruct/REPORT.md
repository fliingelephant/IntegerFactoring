# Corrected bare F04 statement: proof-blind reconstruction

## Result

All four finite claims in the reconstruction request are true, with the scope
restrictions stated below. In particular:

1. The P14 local row ranks differ, \(23\) versus \(266\).
2. The P11 local row matroids are nevertheless the same free matroid, and all
   stated row/column prefix invariants agree.
3. The P11 **full column matroids differ**. The specified two-tail exchange is
   a basis over \(\mathbf F_{100000007}\) and is dependent over
   \(\mathbf F_{199999991}\).
4. Any explicitly specified global minor here can be formed and evaluated over
   \(\mathbf Z/N\mathbf Z\), without factors or ring division, in polynomial bit
   complexity when the matrix dimensions and shift range are
   \(\operatorname{poly}(\log N)\).

This is an instance-level statement. It is not a uniform separation theorem
and does not supply a top-level integer-factoring algorithm.

## Definition and construction order

For each \(a=1,\ldots,A\), form

\[
H_a=(X+a)^N-X^N-a
       \quad\text{in}\quad
R_N=(\mathbf Z/N\mathbf Z)[X]/(X^r-1),
\]

and let row \(a\) of \(M_N\) be the \(r\) coefficients of \(H_a\), in columns
\(0,\ldots,r-1\). Reduction \(R_N\to\mathbf F_\ell[X]/(X^r-1)\) for a prime
\(\ell\mid N\) is applied only after this global matrix exists.

The experiment follows this order literally. The factor-blind generator
accepts only \(N,r,A\), and its two global artifacts were frozen as:

| instance | bytes | SHA-256 |
|---|---:|---|
| P14 | 572432 | db44a8f0796ed74746f9acd4fee879eafcd37bc0edbfbe28fa67f5c3992c84d9 |
| P11 | 69501808 | d7fad69fdca2f97c1b28adb0fa1daf7d4d338e112c4d4c07d5bdb4d42a5b76c4 |

The factors occur only in later local-analysis commands. A second
factor-blind implementation (FLINT rather than Sage) recomputed all
\(2942\cdot2953=8{,}687{,}726\) P11 coefficients from the defining polynomial;
all matched.

## P14

Here

\[
N=79403=271\cdot293,\qquad r=269,\qquad A=266.
\]

### Rank \(23\) over \(\mathbf F_{271}\)

In characteristic \(271\), Frobenius and \(X^{269}=1\) give

\[
\begin{aligned}
(X+a)^N
  &=\bigl((X+a)^{271}\bigr)^{293}\\
  &=(X^{271}+a)^{293}\\
  &=(X^2+a)^{271+22}\\
  &=(X^4+a)(X^2+a)^{22}.
\end{aligned}
\]

This is also exactly the Lucas decomposition coming from the base-\(271\)
digits \(293=(1,22)_{271}\). Put \(y=X^2\). Then

\[
H_a=(y^2+a)(y+a)^{22}-y^{24}-a.
\]

The \(y^{24}\) terms cancel, so every coefficient is in the span of the
twenty-three functions \(a,a^2,\ldots,a^{23}\).

That upper bound is sharp. The following coefficients give a triangular
recovery of those monomials:

\[
\begin{aligned}
[y^{23}]H_a &= 22a,\\
[y^{24-m}]H_a
  &=\binom{22}{m}a^m+\binom{22}{m-2}a^{m-1}
       &&(2\le m\le22),\\
[y^0]H_a &=a^{23}-a.
\end{aligned}
\]

Every displayed leading coefficient is nonzero modulo \(271\). Hence the
coefficient templates of \(a,\ldots,a^{23}\) have rank \(23\).

The evaluation matrix at \(a=1,\ldots,266\) also has column rank \(23\):
its first 23 rows are a row-scaled Vandermonde matrix, with determinant

\[
\left(\prod_{a=1}^{23}a\right)
\left(\prod_{1\le u<v\le23}(v-u)\right)\ne0\pmod{271}.
\]

Therefore the local matrix has rank exactly \(23\).

### Rank \(266\) over \(\mathbf F_{293}\)

In characteristic \(293\),

\[
(X+a)^N
 =\bigl((X+a)^{293}\bigr)^{271}
 =(X^{293}+a)^{271}
 =(X^{24}+a)^{271}.
\]

In its binomial expansion, the \(k=271\) term lies in column
\(24\cdot271\equiv48\pmod{269}\) and is canceled by \(-X^N=-X^{48}\).

Take the 266 binomial indices \(k=2,\ldots,267\), and the corresponding
columns

\[
C=\{24k\bmod269:2\le k\le267\}.
\]

They are distinct because \(\gcd(24,269)=1\). No uncanceled term with another
index lands in one of these columns: the only possible collision is
\(k=2\) with \(k=271\), and the latter was just canceled. In the order
indexed by \(k\), this submatrix is

\[
\binom{271}{k}a^{271-k},
\qquad
1\le a\le266,\quad 2\le k\le267.
\]

All \(\binom{271}{k}\) are nonzero modulo \(293\). Reverse the columns, factor
\(a^4\) from row \(a\), and factor the binomial coefficient from each column.
What remains is the ordinary Vandermonde matrix

\[
(a^t)_{\ 1\le a\le266,\ 0\le t\le265}.
\]

The evaluation points \(1,\ldots,266\) are distinct and nonzero in
\(\mathbf F_{293}\), so this determinant is nonzero. Thus the rank is
exactly \(266\).

### Canonical first-column minor

For the naturally ordered columns \(0,\ldots,265\), exact local elimination
gives

\[
\det B\equiv
\begin{cases}
0&\pmod{271},\\
30&\pmod{293}.
\end{cases}
\]

The first value also follows immediately from rank \(23\). The second was
computed independently from the explicit Frobenius formula above by a
pure-Python elimination, after checking every one of the \(266\cdot269\)
local coefficients against the frozen global artifact.

The unique CRT residue is

\[
\det B\equiv71815\pmod{79403},
\qquad
\gcd(71815,79403)=271.
\]

Consequently the two P14 row matroids differ (their full ground sets have
different ranks), and the first-266-column minor is also a direct column
certificate.

## P11 row matroids and prefixes

Here

\[
\begin{aligned}
N&=20000000499999937\\
 &=100000007\cdot199999991,\\
r&=2953,\qquad A=2942.
\end{aligned}
\]

Let \(B=M_N[:,0:2942]\). Reduction of the same frozen global \(B\) gives

\[
\det B\equiv
\begin{cases}
56136614&\pmod{100000007},\\
132391112&\pmod{199999991}.
\end{cases}
\]

Both are nonzero, so all \(A\) rows are independent over both fields.
Therefore each row matroid, on the \(A\) labeled rows, is the free matroid
\(U_{A,A}\). In particular, the first \(s\) rows have rank \(s\) for every
\(0\le s\le A\).

The first \(A\) columns are also independent. Every subset of them is
independent, so for the full-row column prefix through column \(t-1\),

\[
\operatorname{rank}M_N[:,0:t]=\min(t,A)
\qquad(0\le t\le r)
\]

over both fields. The greedy lexicographic scan therefore accepts columns
\(0,1,\ldots,A-1\), making this the lexicographically first column basis in
both local column matroids.

The CRT lift of the base determinant is

\[
16315256998204520\pmod N,
\qquad
\gcd(16315256998204520,N)=1.
\]

These facts prove equality of the stated row matroids and prefix invariants;
they do **not** imply equality of the full column matroids.

## P11 full-column countercertificate

Let \(T=M_N[:,2942:2953]\), let

\[
I=(423,2336),\qquad J=(2,6),
\]

and let

\[
S=(\{0,\ldots,2941\}\setminus I)\cup\{2944,2948\},
\]

listed in increasing global-column order.

### Exchange identity and sign

Over either local field, \(B\) is invertible. Put \(W=B^{-1}T\). First form
the in-place replacement matrix \(R\), replacing base column \(i_s\) by tail
column \(T[:,j_s]\). Factoring \(B\) and expanding along the unchanged
identity columns gives the generalized Cramer identity

\[
\det R=\det B\cdot\det W[I,J].
\]

To change the in-place order to the increasing order of \(S\), the two
replacement columns cross

\[
\sigma=(A-2-423)+(A-1-2336)=2517+605=3122
\]

columns. Hence

\[
\boxed{\det M_N[:,S]
 =(-1)^{3122}\det B\det W[I,J]
 =+\det B\det W[I,J].}
\]

Thus the requested sign is \(+\).

### Numerical certificate

The two extracted \(2\times2\) blocks are

\[
W[I,J]\equiv
\begin{pmatrix}
30945557&78659553\\
34487144&95932680
\end{pmatrix}
\pmod{100000007},
\]

whose determinant is \(67899852\), and

\[
W[I,J]\equiv
\begin{pmatrix}
24939532&14453382\\
84036612&100604502
\end{pmatrix}
\pmod{199999991},
\]

whose determinant is \(0\). Therefore

\[
\det M_N[:,S]\equiv
\begin{cases}
56136614\cdot67899852
   \equiv15564403&\pmod{100000007},\\
0&\pmod{199999991}.
\end{cases}
\]

A separate computation formed the sorted matrix \(M_N[:,S]\) directly and
recomputed both determinants, obtaining the same \(15564403\) and \(0\);
that audit does not use the exchange identity.

The global CRT residue is

\[
\det M_N[:,S]\equiv2473353088699106\pmod N,
\]

and

\[
\gcd(2473353088699106,N)=199999991.
\]

Thus \(S\) is a basis over \(\mathbf F_{100000007}\) but dependent over
\(\mathbf F_{199999991}\), proving that the full column matroids differ.

### Exhaustive one-/two-tail scan

Using the exact \(W=B^{-1}T\) matrices (both solves were checked by
multiplying \(BW=T\)), all exchanges using one or two of the 11 tail columns
were scanned:

| family | candidates | bases mod \(100000007\) | bases mod \(199999991\) | first-only | second-only |
|---|---:|---:|---:|---:|---:|
| one tail | 32362 | 32362 | 32362 | 0 | 0 |
| two tails | 237941605 | 237941605 | 237941603 | 2 | 0 |

The two first-field-only exchanges are

1. removed \((423,2336)\), tail offsets \((2,6)\);
2. removed \((1618,1874)\), tail offsets \((3,10)\).

These counts are exhaustive only for the one- and two-tail families. They
make no claim about exchanges using 3 through 11 tail columns.

## Factor-free, division-free evaluation

Let \(L=\lceil\log_2N\rceil\), and suppose \(r,A\), and the number/range of
shifts are bounded by \(\operatorname{poly}(L)\).

### Forming the global matrix

Represent an element of \(R_N\) by its \(r\) coefficients. Binary
exponentiation computes \((X+a)^N\) using \(O(L)\) cyclic polynomial
multiplications. A naive cyclic multiplication costs \(O(r^2)\) additions
and multiplications in \(\mathbf Z/N\mathbf Z\). Thus all rows cost

\[
O(A\,r^2L)
\]

ring operations. Only addition, subtraction, multiplication, and canonical
reduction modulo \(N\) are required; no factor, primality test, inverse, or
division in \(\mathbf Z/N\mathbf Z\) is used.

### Determinant over the composite ring

After selecting the specified \(A\times A\) global minor, use the
Samuelson--Berkowitz algorithm. For a block decomposition

\[
Q=\begin{pmatrix}a&R\\ C&M\end{pmatrix},
\]

its recursive Toeplitz factor is built from

\[
1,\ -a,\ -RC,\ -RMC,\ldots,-RM^{m-2}C.
\]

Multiplying these Toeplitz factors recursively returns the characteristic
polynomial of \(Q\); its constant coefficient is
\((-1)^A\det Q\). This construction is valid over every commutative ring
and uses only addition, negation, and multiplication. Iterating the
matrix-vector products naively takes \(O(A^4)\) ring operations. Keeping
each result reduced modulo \(N\) keeps operands at \(O(L)\) bits. Hence the
bit complexity is polynomial in \(L\) under the stated size bounds.

This proves that the specified exchanged determinant (and the base
determinant) is factor-free and division-free evaluable. The local
computations and CRT above certify what that global polynomial expression
equals: determinant commutes with ring reduction because it is an
integer-coefficient polynomial in the entries.

“Division-free” here means no algebraic division or inversion in
\(\mathbf Z/N\mathbf Z\); ordinary machine algorithms may of course use
remainder operations to maintain canonical residues.

## Exact scope and limitations

- The proof establishes the two named finite instances and the explicitly
  stated conditional complexity bound.
- The P11 row matroids, row prefixes, column prefixes, and lexicographic base
  agree; the full column matroids do not.
- The exhaustive scan covers only minors with one or two tail columns.
- No factor-free rule is supplied for choosing \(r,A\), the shifts, or the
  successful exchange for arbitrary composite \(N\).
- Nothing here proves that some such determinant always has a nontrivial gcd
  with \(N\), or even that two local matroids always differ.
- Therefore the fixed-instance gcd certificate is not promoted to a uniform
  separation theorem or a general factoring algorithm.

## Reproducibility and audit trail

All files are confined to this reconstruction directory. No canonical proof
or prohibited experiment directory was read or edited.

Key runs:

| run | hard timeout | purpose | result |
|---|---:|---|---|
| 004_generate_P14_global | 120 s | factor-blind P14 formation | success |
| 005_generate_P11_global | 900 s | factor-blind P11 formation | success, 134.464 s |
| 006_analyze_P14_local | 300 s | Sage local determinant/rank pass | success |
| 010_analyze_P11_flint | 900 s | exact local determinants and all-tail solves | success |
| 014_scan_tail_minors_examples | 600 s | exhaustive one-/two-tail scan | success |
| 016_direct_audit_P11 | 300 s | direct sorted-minor determinants | success |
| 017_independent_audit_P14 | 300 s | every-entry formula check and independent elimination | success |
| 022_audit_all_P11_global_rows | 900 s | independent factor-blind check of all 8,687,726 entries | success, 158.759 s |
| 023_final_cross_audit_after_full_recompute | 300 s | cross-artifact assertions, CRT, gcd, primality | success |

Every run used src/run_logged.py, which disconnects stdin, enforces a hard
wall-clock timeout, kills the whole process group on expiry, and retains
stdout, stderr, a manifest, and SHA-256 hashes.

Preserved failures:

- 001_benchmark_global_row: Sage could not write its default user cache.
- 002_benchmark_global_row: successful arithmetic followed by a Sage integer
  JSON-serialization error.
- 007_analyze_P11_local: the generic Sage matrix backend was intentionally
  interrupted after more than 14 minutes with no field result; its empty logs
  and an explicit interruption manifest are retained. The exact FLINT
  replacement is run 010, not a silent substitution.

The final audit, provenance inventory, source files, compiler outputs, global
matrices, solve matrices, logs, and manifests are all retained under runs/,
src/, and artifacts/.
