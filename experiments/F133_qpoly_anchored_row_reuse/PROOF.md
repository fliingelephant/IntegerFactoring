# F133 proof — anchored feedback and forced row reuse

## 1. Canonical endpoint calculation

Fix an eligible prime \(\ell\). Since \(\ell\nmid N\), there is a unique

\[
A_\ell\in\{0,\ldots,\ell-1\}
\]

such that

\[
w+NA_\ell\equiv0\pmod\ell.
\]

The hypothesis \(q<N/B\) and the bound \(\ell\le B\) give

\[
0<\ell q<N.
\tag{1}
\]

Also,

\[
0<w+NA_\ell
\le (N-1)+N(\ell-1)
=N\ell-1.
\]

Therefore

\[
z_\ell=\frac{w+NA_\ell}{\ell}
\]

is an integer in \(\{1,\ldots,N-1\}\). It satisfies

\[
(\ell q)z_\ell
=q(w+NA_\ell)
\equiv qw
\equiv1\pmod N.
\]

Thus \(\ell q\) and \(z_\ell\) are the least positive endpoint pair, and

\[
P_N(\ell q)=q(w+NA_\ell).
\tag{2}
\]

The defining congruence gives

\[
A_\ell=0
\iff w\equiv0\pmod\ell
\iff \ell\mid w.
\tag{3}
\]

Finally, the right side of (2) is strictly increasing as an integer function
of \(A_\ell\). Hence different carry digits give different exact values.
This proves Theorem 1.

## 2. The bad carry digits occupy two small integers

The block \(q\) is a unit modulo \(N\). Since \(r\mid q\), this implies

\[
r\nmid N.
\tag{4}
\]

First suppose \(r\mid w\). If \(A\) is a nonzero anchor digit, then

\[
0<A<B<r.
\]

Together with (4), this gives

\[
w+NA\not\equiv0\pmod r.
\]

Thus every nonzero digit has

\[
v_r(w+NA)=0,
\tag{5}
\]

which is even.

Now suppose \(r\nmid w\). There is one residue

\[
A_*\equiv-wN^{-1}\pmod r,
\qquad
0\le A_*<r,
\]

for which \(r\mid w+NA_*\). Every observed anchor digit satisfies

\[
0\le A_\ell<\ell\le B<r.
\]

Therefore, if \(v_r(w+NA_\ell)\) is odd, then necessarily

\[
A_\ell=A_*.
\tag{6}
\]

This remains true for valuations \(3,5,\ldots\). Digits different from
\(A_*\) have valuation zero. A digit equal to \(A_*\) can itself have even
valuation, but treating the entire digit as bad only weakens the argument.

## 3. Product bound and one nonzero good digit

For each fixed integer digit \(A\), every eligible prime with
\(A_\ell=A\) divides the integer \(w+NA\). Since the primes are distinct,
their product also divides that integer.

If \(r\mid w\), all primes with digit zero have product at most

\[
w<N.
\]

The condition \(G_B(N,q)>N^2B\) therefore forces a nonzero digit. By (5),
it has even \(r\)-valuation.

If \(r\nmid w\), suppose that every nonzero digit with even valuation were
absent. By (6), all eligible primes would then have digit \(0\) or \(A_*\).
If the digit \(A_*\) occurs, it is less than \(B\), and

\[
w+NA_*<NB.
\]

The product of the eligible primes would divide

\[
w(w+NA_*)<N^2B.
\]

If \(A_*\) does not occur, the smaller bound \(G_B(N,q)\le w<N\) applies.
Both conclusions contradict (3) of the statement. Hence a nonzero digit
with even valuation exists.

For this digit,

\[
v_r(P_N(\ell q))
=v_r(q)+v_r(w+NA_\ell)
\equiv1\pmod2.
\]

Since its digit is nonzero, (2) also gives

\[
P_N(\ell q)>qw=P_N(q).
\]

This proves Theorem 2, including exact-value distinctness relative to the
unary value.

## 4. Why exact-value deduplication still leaves two odd columns

There are three cases.

### Case 1: \(r\nmid w\)

The unary value has

\[
v_r(P_N(q))=v_r(q)+v_r(w)\equiv1\pmod2.
\]

Section 3 supplies one nonzero good digit. Its exact value is also odd in
\(r\), and it is different from \(P_N(q)\).

### Case 2: \(r\mid w\) and \(v_r(w)\) is even

Again the unary value is odd in \(r\). The product condition forces a
nonzero digit, and (5) makes its distinct exact value odd in \(r\).

### Case 3: \(r\mid w\) and \(v_r(w)\) is odd

Here the unary value is even in \(r\), so one anchored value would not be
enough. Suppose no nonzero digit occurred. Then
\(G_B(N,q)\le w<N\), a contradiction. Suppose instead that exactly one
distinct nonzero digit \(A\) occurred among all eligible anchors. The
product of the zero-digit primes divides \(w\). The product of the
\(A\)-digit primes divides \(w+NA\). Hence

\[
G_B(N,q)\le w(w+NA)<N^2B,
\]

contrary to the hypothesis. There are therefore at least two distinct
nonzero digits. Equation (5) makes both corresponding exact values odd in
\(r\), and Section 1 makes the values distinct.

In all three cases, the processed source contains two distinct exact values
with odd \(r\)-valuation. If either value was already in the permanent
ledger, it remains there. If it was absent, first-occurrence retention adds
it. Exact-value deduplication cannot identify the two distinct integers.
Thus the final prime-parity row \(r\) has degree at least two. This proves
Theorem 3.

This argument is stronger than an unconditional claim that one anchored
value is globally new. Such a claim is false for an arbitrary old ledger,
which can already contain that exact integer. The degree conclusion is
immune to that issue.

## 5. An elementary primorial lower bound

Write

\[
\vartheta(x)=\sum_{p\le x}\log p,
\qquad
\psi(x)=\sum_{p^k\le x}\log p.
\]

All logarithms in this section are natural. We first establish a coarse
bound sufficient for \(x=n^3\).

Let \(m=\lfloor x/2\rfloor\). For every prime \(p\),

\[
v_p\binom{2m}{m}
=\sum_{j\ge1}
\left(
\left\lfloor\frac{2m}{p^j}\right\rfloor
-2\left\lfloor\frac{m}{p^j}\right\rfloor
\right).
\]

Every summand is \(0\) or \(1\), and there are at most
\(\lfloor\log_p(2m)\rfloor\) nonzero positions. Hence

\[
\binom{2m}{m}\mid\operatorname{lcm}(1,\ldots,2m).
\]

The central binomial coefficient is at least the average of the \(2m+1\)
binomial coefficients. Therefore

\[
\psi(x)
\ge\log\binom{2m}{m}
\ge2m\log2-\log(2m+1)
\ge(x-1)\log2-\log(x+1).
\tag{7}
\]

The exact prime-power identity is

\[
\psi(x)-\vartheta(x)
=\sum_{k=2}^{\lfloor\log_2x\rfloor}
\vartheta(x^{1/k}).
\]

Using the elementary bound \(\vartheta(y)\le y\log y\), we get

\[
\psi(x)-\vartheta(x)
\le\frac{\sqrt{x}(\log x)^2}{\log2}.
\tag{8}
\]

Set \(x=n^3\). For \(n\ge64\), the function
\((\log n)/\sqrt n\) is decreasing and

\[
\frac{\log n}{\sqrt n}
\le\frac{\log64}{8}<0.52.
\]

Also

\[
\frac1{\log2}<\frac{145}{100},
\qquad
\log2>\frac{69}{100},
\qquad
\log(n^3+1)<n.
\]

The last inequality holds at \(n=64\), and its margin increases because
the derivative of \(n-\log(n^3+1)\) is positive in the declared range.
Equations (7)–(8) now give

\[
\begin{aligned}
\vartheta(n^3)
&\ge(n^3-1)\log2-\log(n^3+1)
  -\frac{9n^{3/2}(\log n)^2}{\log2}\\
&>0.24n^3\\
&>4n\log2.
\end{aligned}
\tag{9}
\]

For completeness, the discarded prime-power term is less than

\[
9\frac{145}{100}\left(\frac{13}{25}\right)^2
  \frac{n^3}{8}
=\frac{220545}{500000}n^3.
\]

Thus the first strict inequality in (9) follows from

\[
\left(\frac{69}{100}-\frac{220545}{500000}\right)n^3-n-\frac{69}{100}
>\frac6{25}n^3,
\]

which reduces to
\(891n^3>100000n+69000\). This holds at \(n=64\), and its margin
increases. The last line of (9) follows from
\((6/25)n^2>4\log2\).

Since \(N<2^n\), (9) implies

\[
\prod_{\ell\le n^3\ {\rm prime}}\ell
=\exp(\vartheta(n^3))
>2^{4n}
>N^4.
\tag{10}
\]

Let \(X\) be the product of the primes at most \(n^3\) that divide \(Nq\).
Then

\[
X\le\operatorname{rad}(Nq)\le Nq<\frac{N^2}{n^3}.
\]

Dividing (10) by \(X\) gives

\[
G_{n^3}(N,q)>N^2n^3.
\]

This proves Theorem 4 without the prime number theorem.

We now keep the excess primorial mass instead of using only the last
inequality. Fix \(r>n^3\) with \(v_r(q)\) odd. Let \(g\) be the number of
distinct nonzero carry digits \(A\) among the eligible anchors for which
\(v_r(w+NA)\) is even.

If \(r\mid w\), every nonzero digit is counted by \(g\). If \(r\nmid w\),
Section 2 shows that every nonzero digit not counted by \(g\) must be the
single residue \(A_*\). Thus all eligible primes occur in at most these
carry buckets:

1. the zero digit;
2. the \(g\) good nonzero digits; and
3. at most one bad nonzero digit.

The product of the primes in the zero bucket divides \(w<N\). For every
nonzero digit \(A<n^3\), its bucket product divides

\[
w+NA<Nn^3.
\]

Consequently,

\[
G_{n^3}(N,q)<N(Nn^3)^{g+1}.
\tag{11}
\]

On the other hand, (9) and \(X<N^2/n^3\) give

\[
\log G_{n^3}(N,q)
>\frac6{25}n^3+3\log n-2\log N.
\tag{12}
\]

Combining (11)–(12), using \(\log N<n\log2\), gives

\[
g>
\frac{(6/25)n^3+3\log n-3n\log2}
     {n\log2+3\log n}
-1.
\tag{13}
\]

For \(n\ge64\), the function \((\log n)/n\) is decreasing, and

\[
\log2<\frac7{10},
\qquad
\frac{\log n}{n}\le\frac{\log64}{64}<\frac{13}{200}.
\]

The denominator in (13) is therefore less than
\((179/200)n\), while its numerator is greater than
\((6/25)n^3-(21/10)n\). Hence

\[
g>
\frac{48n^2-599}{179}
>\frac{n^2}{4}.
\tag{14}
\]

The last inequality is equivalent to \(13n^2>2396\), which holds throughout
the declared range. Different digits give distinct exact values by
Section 1, and every one has odd total \(r\)-valuation. First-occurrence
deduplication therefore retains more than \(n^2/4\) such values. This proves
Corollary 4A.

Inputs with
\(n<64\) form the fixed range \(N<2^{64}\). Trial division through
\(\lfloor\sqrt N\rfloor\) handles this range using a fixed absolute number
of bit operations, which asymptotic quasipolynomial notation absorbs.

## 6. Cost of the composed adaptive source

Let \(\mathcal A_t\) be the full accumulated endpoint transcript before
anchored round \(t\), and put

\[
\Lambda_t=
\sum_{a\in\mathcal A_t}\lceil\log_2(a+1)\rceil.
\]

Let \(M_t\) be the number of blocks in its complete all-block gcd-free
basis. Every block is greater than one, and one copy of each block divides
the product of the transcript endpoints. Therefore

\[
M_t\le\Lambda_t.
\tag{15}
\]

Conditional on the declared F130 and F132 transcript-cost statements, their
composition supplies an initial explicit transcript with

\[
\Lambda_0\le2^{O(L^4)}.
\tag{16}
\]

One anchored round processes at most \(M_tE\) endpoint pairs. Both canonical
endpoints are below \(N\), so appending all of them gives

\[
\Lambda_{t+1}
\le\Lambda_t+2nEM_t
\le(1+2nE)\Lambda_t.
\tag{17}
\]

After \(T=L^2\) rounds,

\[
\log_2\Lambda_T
\le O(L^4)+T\log_2(1+2nE)
=O(L^4).
\tag{18}
\]

The total number of anchored positions is at most

\[
E\sum_{t<T}M_t
\le ET\Lambda_T
=2^{O(L^4)}.
\]

Every position needs polynomially many \(n\)-bit operations. Complete
gcd-free refinement is polynomial in its explicit endpoint input length.
The exact-value ledger has \(2^{O(L^4)}\) entries below \(N^2\). Therefore
the final complete P66 refinement, binary kernel computation, exact root
products, and gcd screens also cost \(2^{O(L^4)}\).

If one processes every pair \(a q^e\), then one round has at most
\(M_tE^2\) endpoint pairs and (17) becomes

\[
\Lambda_{t+1}\le(1+2nE^2)\Lambda_t.
\]

Its logarithmic multiplier is still \(O(L^2)\), so (18) is unchanged. This
proves Theorem 5.

For \(n\ge64\), \(L\ge\log_2 n\ge6\), so

\[
E=2^{L^2}\ge2^{3\log_2n}=n^3.
\]

The algorithmic anchor bank therefore includes the full prime subbank used
in Theorem 4. The initial F130 seed phase has already tested the gcd of
every integer in this bank with \(N\); an implementation can also repeat
that public screen before using an anchor.

## 7. What the theorem does not force

Two columns incident to the same row can each have other private rows. A
degree-one peeling cascade can then remove both columns. Thus row degree
two is not a closure theorem. Even a nonzero binary kernel can map only to
the two global square roots \(+1,-1\pmod N\).

The unreduced identity also needs \(q<N/B\). It gives no comparable control
for a large wrapped block. It gives no large-prime row if every odd row of
the block is small, or if every large prime occurs to even order.

The exact advance is therefore source-side: fixed public anchors force real
parity-row reuse in a large explicit block region, and the adaptive closure
remains quasipolynomial. The parity-closure and normalized-root gates remain
open.
