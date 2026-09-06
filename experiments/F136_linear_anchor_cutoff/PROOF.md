# F136 proof — linear anchor cutoff and wide-or-release law

## 1. An elementary lower bound for the prime product

Write

\[
\vartheta(x)=\sum_{p\le x}\log p,
\qquad
\psi(x)=\sum_{p^k\le x}\log p.
\]

The central-binomial and least-common-multiple argument used in P121 gives,
for every \(x\ge2\),

\[
\psi(x)
\ge(x-1)\log2-\log(x+1).
\tag{1}
\]

Also,

\[
\psi(x)-\vartheta(x)
=\sum_{k=2}^{\lfloor\log_2x\rfloor}\vartheta(x^{1/k})
\le\frac{\sqrt{x}(\log x)^2}{\log2}.
\tag{2}
\]

Therefore

\[
\frac{\vartheta(x)}x
\ge
\left(1-\frac1x\right)\log2
-\frac{\log(x+1)}x
-\frac{(\log x)^2}{\sqrt{x}\log2}.
\tag{3}
\]

For \(x\ge2^{18}\), the first two terms on the right increase with \(x\).
Indeed, if

\[
h(x)=\log2-\frac{\log2+\log(x+1)}x,
\]

then

\[
h'(x)=
\frac{\log2+\log(x+1)-x/(x+1)}{x^2}>0.
\]

The last magnitude

\[
g(x)=\frac{(\log x)^2}{\sqrt{x}\log2}
\]

decreases for \(\log x>4\). It is therefore enough to check \(x=2^{18}\).
Use the rational bounds

\[
\frac{69}{100}<\log2<\frac7{10},
\qquad
\frac1{\log2}<\frac{145}{100},
\qquad
\log(2^{18}+1)<19\log2<\frac{133}{10}.
\]

The right side of (3) is then greater than

\[
\left(1-2^{-18}\right)\frac{69}{100}
-\frac{133/10}{2^{18}}
-\frac{(126/10)^2(145/100)}{512}
=\frac{31500973}{131072000}.
\]

Since

\[
\frac{31500973}{131072000}
-\frac6{25}
=\frac{43693}{131072000}>0,
\]

we obtain

\[
\vartheta(x)>\frac6{25}x
\]

for every \(x\ge2^{18}\). This proves Theorem 1.

## 2. The linear cutoff

Let \(n\ge21846\) and \(B=\lceil12n\rceil\). Then

\[
B\ge2^{18}.
\]

Theorem 1 gives

\[
\vartheta(B)>\frac6{25}B\ge\frac{72}{25}n.
\]

Also \(\log2<7/10\), so

\[
\frac{72}{25}n>\frac{14}{5}n>4n\log2.
\]

Since \(N<2^n\),

\[
\prod_{\ell\le B\ {\rm prime}}\ell
=\exp(\vartheta(B))
>2^{4n}
>N^4.
\tag{4}
\]

Let \(X\) be the product of the primes at most \(B\) that divide \(Nq\).
Then

\[
X\le\operatorname{rad}(Nq)\le Nq<\frac{N^2}{B}.
\tag{5}
\]

Dividing (4) by (5) gives

\[
G_B(N,q)>N^2B.
\]

This proves (3).

## 3. Forced row reuse

Fix a prime \(r>B\) with \(v_r(q)\) odd. Since \(q\) is a unit modulo \(N\),
\(r\nmid N\).

For one fixed carry digit \(A\), the product of all eligible anchor primes in
that digit bucket divides \(w+NA\). The zero bucket has product below \(N\).
A nonzero bucket has product below \(NB\).

If \(r\mid w\), every nonzero digit \(A<B<r\) satisfies

\[
v_r(w+NA)=0.
\]

If \(r\nmid w\), at most one observed digit can satisfy

\[
r\mid w+NA,
\]

because all observed digits lie in \([0,B-1]\subset[0,r-1]\).

If no nonzero good digit existed, the full eligible prime product would fit
inside the zero bucket and at most one bad bucket. It would be less than
\(N^2B\), contradicting Section 2.

If the unary value \(qw\) is odd in row \(r\), it and one nonzero good-digit
value are two distinct odd-row exact values. If the unary value is even
because \(v_r(w)\) is odd, the same product argument forces at least two
distinct nonzero digits. Both have zero \(r\)-valuation in their fresh
cofactor and hence odd total \(r\)-valuation after multiplication by \(q\).

Different digits give different exact integers. First-occurrence exact-value
deletion cannot remove either integer from the permanent ledger. This proves
Theorem 2.

## 4. Presentation release

For one occupied digit \(A\), every prime in \(\mathcal L_A\) divides
\(H_A=w+NA\). Retaining all endpoint presentations

\[
(\ell q,H_A/\ell)
\]

and the old block \(q\), followed by complete gcd-free refinement, names the
anchor primes and removes their full powers from the represented
\(H_A\)-part. Let

\[
S_A=
\prod_{\ell\in\mathcal L_A}\ell^{v_\ell(H_A)},
\qquad
R_A=H_A/S_A.
\]

Every residual block supported on the remaining \(H_A\)-part divides
\(R_A\).

For \(A=0\),

\[
R_0\le\frac{w}{L_0}<\frac{N}{L_0}.
\]

Thus \(L_0>B\) gives \(R_0<N/B\).

For \(A>0\), use \(A\le B-1\) and \(w\le N-1\):

\[
H_A=w+NA<NB.
\]

Therefore

\[
R_A\le\frac{H_A}{L_A}<\frac{NB}{L_A}.
\]

If \(L_A>B^2\), then \(R_A<N/B\). Every positive residual block is at most
\(R_A\). This proves the release statements.

## 5. Width when no bucket releases

Assume

\[
L_0\le B,\qquad L_A\le B^2\quad(A>0).
\]

The occupied buckets partition the eligible primes. If \(d\) is the number
of occupied nonzero digits, then

\[
G_B(N,q)
=L_0\prod_{A>0}L_A
\le B^{2d+1}.
\tag{6}
\]

Sections 1 and 2 give the sharper logarithmic lower bound

\[
\begin{aligned}
\log G_B(N,q)
&=\vartheta(B)-\log X\\
&>\frac6{25}B+\log B-2\log N.
\end{aligned}
\tag{7}
\]

Combine (6)--(7) and cancel \(\log B\):

\[
2d\log B
>\frac6{25}B-2\log N.
\]

Since \(B\ge12n\), \(\log N<n\log2<7n/10\), and
\(B\le13n\),

\[
2d\log B
>\left(\frac{72}{25}-\frac75\right)n
=\frac{37}{25}n.
\]

Consequently,

\[
d>
\frac{37n}{50\log B}
\ge
\frac{37n}{50\log(13n)}.
\]

For a fixed \(r>B\), the argument in Section 3 leaves at most one bad
nonzero digit. The other \(d-1\) digits give distinct values odd in row
\(r\). This proves Theorem 3.

## 6. Conditional cost and exact scope

Theorem 4 assumes an all-block source that already processes every integer
anchor through \(E=2^{L^2}\) for \(T=L^2\) frozen rounds, including complete
refinement and the final parity decode, within the displayed
quasipolynomial bound. At the declared endpoint \(n=21846\), one has
\(L=15\). In general, the definition of \(L\) gives \(n\le2^L-1\).
Therefore, for every \(L\ge15\),

\[
B=12n<12\cdot2^L<2^{L^2}=E.
\]

Consequently,

\[
B=\lceil12n\rceil<E.
\]

The F136 scan is therefore a literal subbank of the source in the hypothesis.
It adds no position. The assumed bound remains

\[
2^{O((\log n)^4)}.
\]

For \(n<21846\), direct trial division has a fixed absolute operation bound.
It can be placed before the asymptotic source without changing uniform
quasipolynomial complexity.

This is a conditional composition statement, not a new derivation of the
imported source cost.

If \(q<N/B\) has no odd prime row above \(B\), then its squarefree kernel is
composed only of primes at most \(B\). Trial division through \(B\) can expose
that public parity in polynomial work.

The result does not cover blocks \(q\ge N/B\), and it does not convert row
reuse or width into a kernel. P122 and F135 show why a wide star can remain a
peeling forest.
