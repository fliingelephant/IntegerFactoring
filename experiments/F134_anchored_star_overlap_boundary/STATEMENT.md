# F134 statement — anchored-star overlap boundary

## Status and prior boundary

This is a proof-only candidate. It gives an exact pruning theorem for one
anchored family of canonical-inverse values. It is not a source-success law,
a route killer, or an integer-factoring theorem.

The closest earlier results are:

- P117 identifies shared parity rows as the necessary interface for a new
  layer to close against retained old relations.
- P120 proves that one reused row need not survive degree-one peeling and
  that bounded all-block feedback remains quasipolynomial.
- The F133 candidate proves that a sufficiently rich small-anchor scan forces
  reuse of an odd large-prime row carried by a small dynamic block.

The material change here is local. After F133 forces old-row reuse, F134
describes the fresh-row structure inside one fixed anchored star. It proves
that two arms cannot amortize unrelated large-prime rows. It also identifies
the exact escapes: one odd anchor coset, an old/new cross-layer match, or
later promotion of a private block to a new anchor.

## Setup

Let \(N\ge3\) be odd. Fix a unit

\[
1<q<N,
\qquad
w=\iota_N(q)\in\{1,\ldots,N-1\},
\qquad
qw=1+kN.
\]

Let \(B\ge1\), and let the \(A_i\) be distinct integers in \([0,B]\). Define

\[
H_i=w+NA_i,
\qquad
P_i=qH_i=1+(k+qA_i)N.
\tag{1}
\]

The algebra below does not require \(P_i<N^2\). In a canonical-inverse
source, retain only a value with a presentation

\[
P_i=c_i z_i,
\qquad
1\le c_i,z_i<N.
\]

Equation (1) then implies \(z_i=\iota_N(c_i)\). Moving a divisor between the
two endpoints changes the presentation but not \(P_i\).

Define

\[
\operatorname{sf}_{>B}(x)
=
\prod_{\substack{r>B\ {\rm prime}\\v_r(x)\ {\rm odd}}}r.
\tag{2}
\]

Thus \(\operatorname{sf}_{>B}(x)=1\) exactly when the squarefree kernel of
\(x\) is \(B\)-smooth. This is parity smoothness. It does not say that
\(x\) itself is \(B\)-smooth.

## Theorem 1 — exact overlap law inside one star

For distinct arms \(i\ne j\),

\[
\boxed{
\gcd(H_i,H_j)
=\gcd(H_i,A_i-A_j)
\le |A_i-A_j|
\le B.
}
\tag{3}
\]

Consequently, every prime \(r>B\) divides at most one \(H_i\). The integers
\(\operatorname{sf}_{>B}(H_i)\) are pairwise coprime.

## Theorem 2 — exact even/odd star-kernel law

Let \(\nu(x)\) be the vector of rational-prime valuation parities of \(x\).
Put

\[
a=\nu(q),
\qquad
h_i=\nu(H_i),
\qquad
p_i=\nu(P_i)=a+h_i.
\]

Let \(M\) have columns \(p_i\), let \(K=\ker M\), and put

\[
t(x)=\sum_i x_i
\qquad
(x\in\mathbb F_2^I).
\]

Then

\[
\boxed{
x\in K
\iff
\sum_i x_i h_i=t(x)a.
}
\tag{4}
\]

If \(S=\{i:x_i=1\}\) and \(x\in K\), then

\[
\boxed{
\prod_{i\in S}\operatorname{sf}_{>B}(H_i)
=
\operatorname{sf}_{>B}(q)^{\,|S|\bmod2}.
}
\tag{5}
\]

Therefore:

1. If \(|S|\) is even, every selected arm has
   \(\operatorname{sf}_{>B}(H_i)=1\).
2. If \(|S|\) is odd, the pairwise-coprime large squarefree parts of the
   selected arms partition \(\operatorname{sf}_{>B}(q)\).
3. If \(\operatorname{sf}_{>B}(q)=1\), every selected arm in every star-only
   dependency has \(B\)-smooth squarefree kernel.

Let

\[
K_{\rm even}=K\cap\ker t.
\]

Either \(K=K_{\rm even}\), or any odd vector \(x_0\in K\) gives

\[
\boxed{
K=K_{\rm even}\;\dot\cup\;(x_0+K_{\rm even}).
}
\tag{6}
\]

Thus one fixed anchor contributes at most one odd coset beyond the even star
kernel.

## Theorem 3 — factor-free private-row consequence

Let \(r>B\). If \(v_r(q)\) is even and \(v_r(H_i)\) is odd, then the \(r\)-row
has degree one in the star matrix. Hence every \(x\in K\) has \(x_i=0\).

After restriction to \(K_{\rm even}\), the common anchor vector cancels.
Every odd large-prime row of an arm is then private among the residual arm
vectors. Therefore

\[
\boxed{
K_{\rm even}
\subseteq
\{x:x_i=0\text{ whenever }
\operatorname{sf}_{>B}(H_i)>1\}.
}
\tag{7}
\]

This is factor-free in the P66 sense. Complete joint gcd-free refinement
computes the same exact square-dependency kernel without factoring the large
blocks. If \(B\) is quasipolynomial, one can also remove the prime factors at
most \(B\) and square-test the remaining cofactor in quasipolynomial work.

The privacy conclusion is only for the star submatrix. If an old retained
matrix is \(M_0\), an old/new dependency satisfies

\[
\boxed{
M_0y+a\,t(x)+\sum_i x_i h_i=0.
}
\tag{8}
\]

An old column combination can cancel a row that is private among the new
arms. This is the P117 cross-layer gate.

## Theorem 4 — normalization and exact-value deletion

Distinct digits give distinct integers \(P_i\). First-occurrence exact-value
deletion therefore does not merge two arms of one star.

If \(P_i\) occurred earlier, retaining two identical columns would add only
the duplicate dependency with exact positive root \(P_i\). Since
\(P_i\equiv1\pmod N\), this direction has normalized root \(+1\). Deleting
the duplicate loses no useful P66 root.

An alternative endpoint presentation can still refine the later generator
basis. The theorem therefore does not delete presentation-level feedback.
Any canonical endpoint normalization leaves the exact value and every parity
conclusion unchanged.

## Certificate A — the odd anchor coset can be global

Take

\[
N=25,
\qquad
q=18,
\qquad
w=7,
\qquad
B=1,
\qquad
(A_0,A_1)=(0,1).
\]

Then

\[
H_0=7,
\qquad
H_1=32,
\qquad
\gcd(H_0,H_1)=1,
\]

and

\[
P_0=18\cdot7=126=1+5N,
\qquad
P_1=18\cdot32=576=24^2=1+23N.
\]

The canonical endpoint presentations \((18,7)\) and \((24,24)\) have only
nonproper sign screens:

\[
\begin{aligned}
\gcd(18-7,25)&=1,&
\gcd(18+7,25)&=25,\\
\gcd(24-24,25)&=25,&
\gcd(24+24,25)&=1.
\end{aligned}
\]

The one-column dependency on \(P_1\) is odd. Although

\[
\operatorname{sf}_{>1}(H_1)=2,
\]

the same odd prime occurs in \(q\), so it cancels. The decoded root is

\[
24\equiv-1\pmod{25}.
\]

Thus the unqualified smoothness claim is false, and the exceptional odd
coset can be a useless global root.

## Certificate B — a retained old relation closes a nonsmooth new arm

Take

\[
N=143=11\cdot13,
\qquad
q=28,
\qquad
w=46,
\qquad
B=1,
\qquad
(A_0,A_1)=(0,1).
\]

The arms are

\[
H_0=46,
\qquad
H_1=189,
\qquad
\gcd(H_0,H_1)=1.
\]

The zero-carry value is

\[
P_0=28\cdot46=1288=1+9N.
\]

For the nonzero carry, move the divisor \(3\) from \(H_1\) to the anchor:

\[
P_1=28\cdot189
=84\cdot63
=5292
=1+37N
=3\cdot42^2.
\]

Retain the older distinct relation

\[
P_*=102\cdot136
=13872
=1+97N
=3\cdot68^2.
\]

All endpoint sign screens are null:

\[
\begin{aligned}
\gcd(28-46,143)&=1,&
\gcd(28+46,143)&=1,\\
\gcd(84-63,143)&=1,&
\gcd(84+63,143)&=1,\\
\gcd(102-136,143)&=1,&
\gcd(102+136,143)&=1.
\end{aligned}
\]

The new and old values close:

\[
P_1P_*=(3\cdot42\cdot68)^2=8568^2,
\]

and

\[
\gcd(8568-1,143)=13,
\qquad
\gcd(8568+1,143)=11.
\]

Yet

\[
\operatorname{sf}_{>1}(H_1)=21.
\]

The anchor cancels the prime \(7\), and the old relation cancels the prime
\(3\). This is a useful nonzero-carry cross-layer closure. It proves that
the star-only theorem does not turn retained feedback into ordinary
smoothness.

## Certificate C — a private row can become the next anchor

Take \(N=49\) and \(B=1\). In the first star, let

\[
q=16,
\qquad
w=46.
\]

The digits \(0,1\) give

\[
\begin{aligned}
H_0&=46,
&P_0&=16\cdot46=736=1+15N,\\
H_1&=95=5\cdot19,
&P_1&=16\cdot95=38\cdot40=1520=1+31N.
\end{aligned}
\]

Here \(\gcd(H_0,H_1)=1\). The prime \(19>B\) occurs oddly only in \(P_1\)
inside this star. Endpoint refinement exposes \(19\). Feed it next:

\[
q'=19,
\qquad
w'=31,
\qquad
P'=19\cdot31=589=1+12N.
\]

All named screens are null:

\[
\begin{aligned}
\gcd(16-46,49)&=1,&
\gcd(16+46,49)&=1,\\
\gcd(38-40,49)&=1,&
\gcd(38+40,49)&=1,\\
\gcd(19-31,49)&=1,&
\gcd(19+31,49)&=1.
\end{aligned}
\]

The values \(P_1=1520\) and \(P'=589\) are distinct and both have odd
\(19\)-valuation. Exact-value deletion keeps both. A row that was private
in the first star has degree at least two after the second round.

This certificate proves loss of privacy. It does not claim a square
dependency.

## Scope and algorithmic consequence

The theorem proves

\[
\boxed{
\text{one fixed star cannot amortize unrelated large primes across its arms.}
}
\]

It does not prove that one fixed star, retained feedback, or multi-round
feedback fails. A live source can still use:

1. an arm whose large-prime part is already a square;
2. the one possible odd anchor coset;
3. an old/new cross-layer match as in Certificate B; or
4. promotion of a private cofactor as in Certificate C.

For different anchors \(q,q'\), the arm difference contains

\[
(w_q-w_{q'})+N(A-A'),
\]

not only \(N(A-A')\). The bound in (3) no longer applies.

The result gives no density bound for \(w+NA=s y^2\) with \(s\)
\(B\)-smooth. It gives no closure theorem and no non-global-root law. It is
a pruning theorem for false forms of within-star amortization.
