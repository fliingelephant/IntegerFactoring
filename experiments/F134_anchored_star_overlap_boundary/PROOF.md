# F134 proof — anchored-star overlap boundary

## 1. Exact congruence values

Since \(w=\iota_N(q)\), there is an integer \(k\ge0\) with

\[
qw=1+kN.
\]

For every declared digit \(A_i\),

\[
qH_i
=q(w+NA_i)
=1+(k+qA_i)N.
\tag{1}
\]

Thus \(P_i=qH_i\) is a positive integer congruent to \(1\) modulo \(N\).
If \(P_i=c_i z_i\) with both factors in \(\{1,\ldots,N-1\}\), then both
are units and \(c_i z_i\equiv1\pmod N\). Uniqueness of the inverse in that
interval gives \(z_i=\iota_N(c_i)\).

## 2. Pairwise overlap

For \(i\ne j\),

\[
H_j-H_i=N(A_j-A_i).
\]

Also \(H_i\equiv w\pmod N\), so \(\gcd(H_i,N)=1\). The Euclidean algorithm
gives

\[
\begin{aligned}
\gcd(H_i,H_j)
&=\gcd(H_i,N(A_j-A_i))\\
&=\gcd(H_i,A_j-A_i).
\end{aligned}
\]

Because the digits are distinct and lie in \([0,B]\),

\[
1\le |A_i-A_j|\le B.
\]

This proves (3). A prime \(r>B\) cannot divide two different arms. Their
large squarefree kernels are therefore pairwise coprime.

## 3. The star kernel

Let

\[
\nu(x)=(v_r(x)\bmod2)_r
\]

over all rational primes. Unique factorization gives
\(\nu(xy)=\nu(x)+\nu(y)\). For

\[
a=\nu(q),
\qquad
h_i=\nu(H_i),
\]

the \(i\)-th exact-value column is

\[
p_i=\nu(P_i)=a+h_i.
\]

Hence

\[
Mx
=\sum_i x_i(a+h_i)
=t(x)a+\sum_i x_i h_i.
\]

This proves (4).

Restrict (4) to primes \(r>B\). Section 2 shows that the restricted supports
of the \(h_i\) are disjoint.

If \(t(x)=0\), their sum can vanish only if every selected restricted vector
is zero. Thus every selected arm has

\[
\operatorname{sf}_{>B}(H_i)=1.
\]

If \(t(x)=1\), the disjoint supports of the selected \(h_i\) must have union
equal to the support of \(a\) above \(B\). Equivalently, their pairwise-
coprime squarefree integers multiply to

\[
\operatorname{sf}_{>B}(q).
\]

This proves (5) and its three consequences.

## 4. At most one odd coset

The parity functional \(t\) is linear. Its restriction to \(K\) has image
either \(\{0\}\) or \(\mathbb F_2\).

In the first case, \(K=K_{\rm even}\). In the second case, choose one
\(x_0\in K\) with \(t(x_0)=1\). Every odd \(x\in K\) satisfies

\[
x+x_0\in K_{\rm even}.
\]

Conversely, every vector in \(x_0+K_{\rm even}\) is odd and lies in \(K\).
This proves (6).

The claim uses one affine translate by one fixed anchor vector. It does not
extend to a union of stars with different anchors.

## 5. Private rows and factor-free decoding

Fix \(r>B\). If \(v_r(q)\) is even, the \(r\)-entry of the common anchor
vector \(a\) is zero. If \(v_r(H_i)\) is odd, Section 2 says that every
other \(H_j\) has zero \(r\)-entry. The \(r\)-row of the star matrix has
one \(1\), in column \(i\). Its row equation forces \(x_i=0\).

For \(x\in K_{\rm even}\), the common anchor term is zero even when
\(v_r(q)\) is odd. The same row argument applies to every odd large-prime
entry of every selected arm. This proves (7).

The rational-prime rows state the invariant transparently. P66 jointly
refines the displayed integers into pairwise-coprime gcd-free blocks,
removes exact perfect powers, and produces a binary matrix with the same
exact kernel. A private nonsquare cofactor becomes a private gcd-free parity
row. No factorization of that large cofactor is needed.

If \(B\) is quasipolynomial, there is also a direct test. Enumerate the
primes at most \(B\), divide all their powers from \(H_i\), and test the
remaining integer for being a square. It is a square exactly when
\(\operatorname{sf}_{>B}(H_i)=1\).

If old columns are present, the row equation is

\[
M_0y+Mx=0.
\]

Substitution from Section 3 gives (8). A row that occurs only once among
the new arms can occur in \(M_0y\). It is not then a degree-one row of the
combined matrix. The pairwise overlap theorem says nothing about old-row
incidence.

## 6. Endpoint presentations and duplicate exact values

Equation (1) is strictly increasing with \(A_i\), because \(qN>0\).
Distinct digits give distinct exact values.

Suppose an old column and a new occurrence have the same exact integer
\(P_i\). If both copies were kept, selecting both would give exact product
\(P_i^2\), with positive root \(P_i\). Equation (1) gives
\(P_i\equiv1\pmod N\). The duplicate direction therefore has normalized
root \(+1\). Keeping one exact column loses no useful P66 direction.

The endpoints of the deleted occurrence can still be retained before
deletion and can refine the next all-block basis. Any redistribution of
factors between two endpoints keeps their product, parity column, and exact
positive roots unchanged.

## 7. Certificate A

For \(N=25\),

\[
18\cdot7=126=1+5\cdot25.
\]

Thus \(w=7\) is the canonical inverse of \(q=18\). With digits \(0,1\),

\[
H_0=7,
\qquad
H_1=7+25=32,
\qquad
\gcd(7,32)=1.
\]

The second exact value is

\[
18\cdot32=576=24^2=1+23\cdot25.
\]

The endpoint pairs \((18,7)\) and \((24,24)\) lie below \(25\). Their four
sign gcds are

\[
\gcd(11,25)=1,
\quad
\gcd(25,25)=25,
\quad
\gcd(0,25)=25,
\quad
\gcd(48,25)=1.
\]

The values \(126\) and \(576\) are distinct. Also

\[
q=2\cdot3^2,
\qquad
H_1=2^5.
\]

Their odd \(2\)-valuations cancel in \(P_1\). Its positive root is
\(24\equiv-1\pmod{25}\). This proves Certificate A.

## 8. Certificate B

For \(N=143=11\cdot13\),

\[
28\cdot46=1288=1+9\cdot143.
\]

Thus \(w=46\) is the canonical inverse of \(q=28\). The digits \(0,1\) give

\[
H_0=46,
\qquad
H_1=46+143=189,
\qquad
\gcd(46,189)=1.
\]

For the nonzero carry,

\[
\begin{aligned}
qH_1
&=28\cdot189\\
&=84\cdot63\\
&=5292\\
&=1+37\cdot143\\
&=3\cdot42^2.
\end{aligned}
\]

The older relation is

\[
\begin{aligned}
102\cdot136
&=13872\\
&=1+97\cdot143\\
&=3\cdot68^2.
\end{aligned}
\]

All endpoints lie below \(143\). Direct calculation gives

\[
\begin{array}{c|c}
\text{sign value}&\gcd(\text{sign value},143)\\ \hline
28-46=-18&1\\
28+46=74&1\\
84-63=21&1\\
84+63=147&1\\
102-136=-34&1\\
102+136=238&1
\end{array}
\]

The values \(1288,5292,13872\) are pairwise distinct. The last two have
positive joint root

\[
R=3\cdot42\cdot68=8568.
\]

Finally,

\[
8568-1=13\cdot659,
\qquad
8568+1=11\cdot779.
\]

Thus the decoder returns both proper factors. Since

\[
H_1=3^3\cdot7,
\qquad
\operatorname{sf}_{>1}(H_1)=21,
\]

the useful closure is not star-only smoothness. The prime \(7\) cancels
against \(q=2^2\cdot7\), and the prime \(3\) closes against the old relation.
This proves Certificate B.

## 9. Certificate C

For \(N=49\),

\[
16\cdot46=736=1+15\cdot49.
\]

Thus \(w=46\) is the canonical inverse of \(16\). For digits \(0,1\),

\[
H_0=46,
\qquad
H_1=46+49=95,
\qquad
\gcd(46,95)=1.
\]

The second exact value has the canonical presentation

\[
16\cdot95=1520=38\cdot40=1+31\cdot49.
\]

Its factorization is \(1520=2^4\cdot5\cdot19\), whereas
\(736=2^5\cdot23\). Row \(19\) has degree one in the first star. Refinement
of \(38=2\cdot19\) exposes \(19\).

The canonical inverse of \(19\) is \(31\), because

\[
19\cdot31=589=1+12\cdot49.
\]

This new value is distinct from \(736\) and \(1520\), and its
\(19\)-valuation is odd. The screen calculations are

\[
\begin{array}{c|c}
\text{sign value}&\gcd(\text{sign value},49)\\ \hline
16-46=-30&1\\
16+46=62&1\\
38-40=-2&1\\
38+40=78&1\\
19-31=-12&1\\
19+31=50&1
\end{array}
\]

Exact-value deletion keeps both \(19\)-incident columns. This proves
Certificate C.

## 10. Exact boundary

Within one star, the overlap law blocks the usual large-prime strategy of
letting one prime occur once in each of two partial relations. Such a prime
cannot occur in two arms when it exceeds the carry range.

The theorem leaves four mechanisms:

1. One arm can contain its large primes to even valuation.
2. The unique odd coset can match the anchor.
3. Old retained columns can cancel fresh rows through (8).
4. A private block can become a later anchor.

For a second anchor \(q'\), its inverse differs from \(w\). The arm
difference is

\[
(w_q-w_{q'})+N(A-A'),
\]

not \(N(A-A')\). No bound by \(B\) follows.

Nothing here bounds the density of parity-smooth arms. Nothing forces (8)
to have a solution. Even if it does, nothing forces a non-global root. The
result is a pruning theorem, not a progress law.
