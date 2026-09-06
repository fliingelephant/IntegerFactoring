# F135 proof — anchored recursion cutoff and expanding-forest boundary

## 1. Cutoff and exact duplicates

P121 gives

\[
c_\ell=\ell q<N,
\qquad
z_\ell=\frac{w+NA_\ell}{\ell}<N,
\qquad
c_\ell z_\ell=q(w+NA_\ell)\equiv1\pmod N.
\tag{1}
\]

If \(A_\ell=0\), then

\[
c_\ell z_\ell=qw=P_N(q).
\]

This proves (2) of the statement. The endpoints can differ from the unary
presentation, so exact-value deletion must still occur after endpoint sign
screens and endpoint retention, as in P120.

If \(A_\ell>0\), then \(A_\ell\ge1\), and

\[
z_\ell
=\frac{w+NA_\ell}{\ell}
>\frac N\ell
\ge\frac NB.
\tag{2}
\]

This proves the strict cutoff.

Both \(c_\ell\) and \(z_\ell\) lie in \(\{1,\ldots,N-1\}\), and their
product is one modulo \(N\). Inversion is symmetric, so uniqueness of the
least positive inverse gives

\[
\iota_N(z_\ell)=c_\ell=\ell q.
\]

Therefore

\[
P_N(z_\ell)=z_\ell c_\ell=P_N(c_\ell).
\]

This proves Theorem 1.

## 2. Denominators in the reciprocal-overlap bound

Let \(A_i\ne A_j\). Since

\[
H_j-H_i=N(A_j-A_i)
\]

and

\[
\gcd(H_i,N)=\gcd(w,N)=1,
\]

the Euclidean algorithm gives

\[
\begin{aligned}
\gcd(H_i,H_j)
&=\gcd(H_i,N(A_j-A_i))\\
&=\gcd(H_i,A_j-A_i).
\end{aligned}
\tag{3}
\]

Every digit satisfies

\[
0\le A_i<\ell_i\le B.
\]

Thus

\[
1\le|A_i-A_j|\le B-1<B.
\tag{4}
\]

The denominators require no cancellation argument. Since \(z_i\mid H_i\)
and \(z_j\mid H_j\), every common divisor of \(z_i,z_j\) is a common divisor
of \(H_i,H_j\). Hence

\[
\gcd(z_i,z_j)\mid\gcd(H_i,H_j)<B.
\tag{5}
\]

No equality is asserted in (5). This proves Theorem 2.

## 3. What same-digit endpoint presentations can release

Fix one occupied digit \(A\). Every \(\ell\in\mathcal L_A\) divides
\(H_A\), so

\[
L_A\mid H_A,
\qquad
S_A\mid H_A,
\qquad
S_A\ge L_A.
\tag{6}
\]

The source retains the endpoint presentation

\[
(\ell q,H_A/\ell)
\]

for every \(\ell\in\mathcal L_A\), even when several presentations have the
same exact value. The block \(q\) is already named and
\(\gcd(q,\ell)=1\). Thus the left endpoint \(\ell q\) names the anchor
prime \(\ell\). The public integer \(H_A=w+NA\) is known exactly, so repeated
exact division computes every \(v_\ell(H_A)\), then \(S_A\) and \(R_A\),
without factoring \(H_A\).

For every retained reciprocal endpoint \(H_A/\ell\), removing all named
anchor-prime powers leaves the same non-anchor part \(R_A\). Complete
gcd-free refinement can only split that part into smaller blocks. A factor
shared by \(q\) and \(H_A\) causes no exception: eligibility gives
\(\ell\nmid q\), so the shared non-anchor factor remains in \(R_A\), although
refinement can identify it with an old \(q\)-side block. Therefore every
residual block contributed by the reciprocal \(H_A\)-side divides \(R_A\).
No claim is made about an old block supported only on the \(q\)-side.

For \(A=0\),

\[
R_0\le\frac w{L_0}<\frac N{L_0}.
\]

Thus \(L_0>B\) implies \(R_0<N/B\).

For \(A>0\), we use \(A\le B-1\) and \(w\le N-1\):

\[
H_A=w+NA
\le (N-1)+N(B-1)
=NB-1
<NB.
\tag{7}
\]

Consequently,

\[
R_A\le\frac{H_A}{L_A}<\frac{NB}{L_A}.
\]

If \(L_A>B^2\), then \(R_A<N/B\). Under this hypothesis, or under
\(L_0>B\) in the zero-digit case, every reciprocal-side residual block is a
positive divisor of \(R_A\), so it is no larger than \(R_A\). If \(R_A=1\),
no reciprocal-side residual block remains. This proves (9), (10), and the
first two branches of (13). No residual-size conclusion is asserted when the
corresponding bucket-product threshold fails.

## 4. Exact width on the no-release branch

Now take \(B=n^3\) and \(n\ge64\). The P121 elementary primorial proof gives

\[
\vartheta(n^3)>\frac6{25}n^3.
\tag{8}
\]

The product \(X\) of the primes at most \(n^3\) excluded because they divide
\(Nq\) satisfies

\[
X\le\operatorname{rad}(Nq)\le Nq<\frac{N^2}{n^3}.
\tag{9}
\]

Therefore the eligible prime product \(G\) satisfies

\[
\log G
>\frac6{25}n^3+3\log n-2\log N.
\tag{10}
\]

The occupied digit buckets partition the eligible primes, so

\[
G=L_0\prod_{A>0,\ \mathcal L_A\ne\varnothing}L_A.
\tag{11}
\]

On the no-release branch (11) of the statement, if \(d\) is the number of
occupied nonzero digits, then

\[
G\le B(B^2)^d=B^{2d+1}.
\tag{12}
\]

Since \(B=n^3\), equations (10)--(12), together with
\(\log N<n\log2\), give

\[
(6d+3)\log n
>
\frac6{25}n^3+3\log n-2n\log2.
\]

After cancelling \(3\log n\) and dividing by \(6\log n>0\),

\[
d>
\frac{n^3}{25\log n}
-
\frac{n\log2}{3\log n}.
\tag{13}
\]

Fix a prime \(r>B\) with \(v_r(q)\) odd. If \(r\mid w\), every nonzero
digit \(A<r\) has

\[
w+NA\not\equiv0\pmod r,
\]

so its \(r\)-valuation is zero. If \(r\nmid w\), there is only one residue

\[
A_*\equiv-wN^{-1}\pmod r
\]

that can have positive \(r\)-valuation. All observed digits lie in
\([0,B-1]\subset[0,r-1]\), so at most one observed nonzero digit equals
\(A_*\). Thus at least \(d-1\) occupied nonzero digits have even
\(r\)-valuation in \(H_A\), and their values \(qH_A\) have odd
\(r\)-valuation.

Different digits give different exact integers. Global first-occurrence
deduplication keeps each integer once; if one occurred earlier, it is already
in the ledger. This proves Theorem 3.

## 5. The abstract expanding forest

Order the vertices of \(\mathcal T\) so that every parent occurs before its
children. The column \(C_v\) has a one in its own row \(r_v\), zero in the
own row of every later or unrelated vertex, and possibly one additional
entry in the earlier parent row. The square row-by-column matrix is therefore
triangular with every diagonal entry one. Its determinant over
\(\mathbb F_2\) is one, so its kernel is zero.

An internal row \(r_v\) occurs in \(C_v\) and in the \(b\) child columns.
Its degree is \(b+1\). A leaf row occurs only in its own column. Delete all
leaf rows and columns. The parents of those leaves now have degree one.
Repeating this operation level by level deletes the complete matrix.

The vertex count is the geometric sum

\[
V=1+b+\cdots+b^T=\frac{b^{T+1}-1}{b-1}.
\]

If \(b=n^{O(1)}\) and \(T=O((\log n)^2)\), then

\[
\log V=O(T\log b)=O((\log n)^3).
\]

This proves Theorem 4. No integer labels or canonical congruences were used,
so the construction is only an abstract incidence obstruction.

## 6. The selected canonical forest CRT class

The moduli in (18)--(19) are pairwise coprime. Every displayed residue is
coprime to its modulus. CRT therefore gives one reduced residue class
\(A\pmod M\), where \(M\) is fixed.

Choose primes

\[
P\equiv1\pmod M,
\qquad
Q\equiv A\pmod M
\]

in the disjoint intervals

\[
P\in[X,1.1X],
\qquad
Q\in[1.2X,1.3X].
\]

The prime number theorem in fixed arithmetic progressions supplies such
primes for all sufficiently large \(X\). Then \(N=PQ\equiv A\pmod M\) is
odd, balanced, and has distinct factors. Along an unbounded sequence of
disjoint intervals, this gives infinitely many semiprimes. Since
\(P,Q=\Theta(X)\) while the bit length is \(2\log_2X+O(1)\), both factors
eventually exceed every fixed polynomial in that bit length.

### 6.1 Unary carries and valuation one

For each pair \((q_v,k_v)\) in (16), the corresponding square-modulus
condition has the form

\[
N\equiv(q_v-1)k_v^{-1}\pmod{q_v^2}.
\tag{14}
\]

The exact residues are:

\[
\begin{array}{c|c|c}
(q_v,k_v)&k_v^{-1}\pmod{q_v^2}&
(q_v-1)k_v^{-1}\pmod{q_v^2}\\ \hline
(5,2)&13&2\\
(11,7)&52&36\\
(19,17)&85&86\\
(23,18)&147&60\\
(37,36)&1331&1.
\end{array}
\tag{15}
\]

Thus

\[
C_v=1+k_vN\equiv q_v\pmod{q_v^2}.
\tag{16}
\]

In particular, \(v_{q_v}(C_v)=1\). Reduction of (14) modulo \(q_v\)
also gives \(N\equiv-k_v^{-1}\pmod{q_v}\), so \(q_v\mid C_v\). Since
\(0<k_v<q_v\),

\[
0<\frac{C_v}{q_v}<N.
\]

Hence \(P_N(q_v)=C_v\).

### 6.2 Anchored duplicate presentations

The edge data satisfy

\[
\begin{aligned}
7&=2+1\cdot5,\\
17&=2+3\cdot5,\\
18&=7+1\cdot11,\\
36&=17+1\cdot19.
\end{aligned}
\tag{17}
\]

The four anchor congruences in (19) are exactly

\[
N\equiv-k_v^{-1}\pmod\ell
\]

for the child carry \(k_v\) and edge anchor \(\ell\):

\[
\begin{array}{c|c|c}
(\ell,k_v)&-k_v^{-1}\pmod\ell&\text{declared residue}\\ \hline
(3,7)&2&2\\
(7,17)&2&2\\
(13,18)&5&5\\
(29,36)&4&4.
\end{array}
\tag{18}
\]

For an edge from parent block \(q_u\) to child carry \(k_v\), with digit
\(A\), equation (17) gives

\[
1+k_vN=1+(k_u+Aq_u)N=q_u(w_u+AN).
\]

The anchor congruence makes this integer divisible by \(\ell q_u\). The
four anchored left endpoints and carries satisfy

\[
(\ell q_u,k_v)=(15,7),(35,17),(143,18),(551,36),
\]

so \(k_v<\ell q_u\). Therefore

\[
0<\frac{1+k_vN}{\ell q_u}<N.
\]

It is the canonical inverse of \(\ell q_u\), proving every equality in
(20).

### 6.3 Exact parity incidence

The square-modulus congruences give

\[
N\equiv2,3,10,14,1
\pmod{5,11,19,23,37},
\tag{19}
\]

respectively. Substituting the five carries
\(2,7,17,18,36\) shows that the only divisibilities among the five
block-prime rows and five values are those in (21).

The claimed one-entries have exact valuation one. Modulo the corresponding
squares, their residues are

\[
\begin{array}{c|c}
\text{row}&\text{nonzero multiples for incident columns}\\ \hline
5&C_0\equiv5,\ C_1\equiv15,\ C_2\equiv10\pmod{25}\\
11&C_1\equiv11,\ C_3\equiv44\pmod{121}\\
19&C_2\equiv19,\ C_4\equiv209\pmod{361}\\
23&C_3\equiv23\pmod{529}\\
37&C_4\equiv37\pmod{1369}.
\end{array}
\tag{20}
\]

Every displayed multiple is nonzero modulo the prime square. The remaining
entries are nonzero already modulo the row prime. This proves matrix (21).

Its determinant is one. Also, row \(23\) occurs only in \(C_3\), and row
\(37\) occurs only in \(C_4\). Peel those columns. Row \(11\) then occurs
only in \(C_1\), and row \(19\) only in \(C_2\). Peel them. Row \(5\) then
peels \(C_0\). Additional prime rows in the same five integer values do not
remove any of these degree-one witnesses.

The carries \(k_v\) are distinct, so the exact integers \(C_v=1+k_vN\) are
distinct and survive exact-value deduplication.

### 6.4 Direct screens and scope

All selected left endpoints belong to the fixed set

\[
\{5,11,19,23,37,15,35,143,551\}.
\]

For a unit \(c\) and its inverse \(z\), multiplication by \(c\) gives

\[
\gcd(c-z,N)=\gcd(c^2-1,N),
\qquad
\gcd(c+z,N)=\gcd(c^2+1,N).
\]

For sufficiently large \(X\), both prime factors of \(N\) exceed
\(551^2+1\). Neither can divide any nonzero fixed integer \(c^2\pm1\) in
the displayed set. All selected direct screens are therefore one.

The initial quasipolynomial seed bank eventually contains every fixed block
prime in (16), and the declared anchor scan contains (17). Thus these are
actual selected positions of the source. No congruence controls its other
positions. This completes the proof of Theorem 5 and its strict scope.
