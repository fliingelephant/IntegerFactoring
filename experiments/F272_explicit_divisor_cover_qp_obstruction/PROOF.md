# Proof of F272

## 1. The prime-mass inequality

For every prime \(p\leq X\), the \(X\)-divisor property supplies at least
one \(d\in D\) divisible by \(p\). Hence every such prime divides

\[
 P_D=\prod_{d\in D}d.
\]

The primes are pairwise coprime, so their product divides \(P_D\):

\[
 \prod_{p\leq X\atop p\ {\operatorname{prime}}}p\mid P_D.
\tag{23}
\]

Taking base-two logarithms gives

\[
 \vartheta_2(X)
 \leq\sum_{d\in D}\log_2d.
\tag{24}
\]

By the definition of binary length, \(d<2^L\) for every \(d\in D\).
Therefore

\[
 \sum_{d\in D}\log_2d<ML.
\tag{25}
\]

This proves (6). Collapsing duplicate pair differences only decreases
\(M\), and

\[
 M\leq K\leq |S|\,|T|,
\]

which proves (7).

If \(|s|,|t|<2^B\), then

\[
 0<|s-t|<2^{B+1}.
\]

Thus every nonzero difference has binary length at most \(B+1\), proving
(8).

Let \(n_X=\lceil\log_2(X+1)\rceil\). Any fixed quasipolynomial

\[
 Q(n_X)=2^{C(\log_2(n_X+1))^k}
\]

satisfies

\[
 \log_X Q(n_X)
 =O\!\left(\frac{(\log\log X)^k}{\log X}\right)=o(1).
\tag{26}
\]

Finite products of such bounds are \(X^{o(1)}\). If \(|S|,|T|,L\) were
all quasipolynomial in \(n_X\), the left side of (7) would be \(X^{o(1)}\),
while the Chebyshev lower bound makes the right side at least \(cX\). This
is impossible for all sufficiently large \(X\). No property of a grammar,
rank, or construction algorithm entered the proof.

## 2. Explicit prefactorization costs its output

Run the declared factor-output procedure conceptually on every ordered pair
\((s,t)\) with \(s\ne t\). For every prime \(p\leq X\), at least one
resulting difference is divisible by \(p\). The complete factorization of
that difference must write the binary name of \(p\) at least once.

Across all \(K\) outputs, the number of bits used just for one occurrence of
each required prime is at least

\[
 \sum_{p\leq X}\bigl(\lfloor\log_2p\rfloor+1\bigr)
 \geq\sum_{p\leq X}\log_2p
 =\vartheta_2(X).
\tag{27}
\]

If each output has at most \(F\) bits, the total is at most \(KF\), which
proves (10). Duplicate differences and repeated prime names only increase
the actual total. Negative differences cause no change because the
factorization is that of their absolute values. Zero pairs were excluded
before the procedure was invoked.

In a sequential bit model, a call cannot write more bits than a constant
multiple of its running time. Absorbing that fixed constant leaves the same
asymptotic lower bound for worst-case bit time. Equations (5), (9), and
(10) now give the quasipolynomial incompatibility exactly as in (26),
without any bound on the expanded magnitude of a difference.

## 3. Prime-pair incidence

For \(d\in D\), let

\[
 r(d)=|\{p\in\mathcal P:p\mid d\}|.
\]

The primes counted by \(r(d)\) are distinct and each is at least
\(a\sqrt X\). Hence

\[
 (a\sqrt X)^{r(d)}
 \leq\prod_{p\in\mathcal P\atop p\mid d}p
 \leq d
 \leq H.
\tag{28}
\]

Taking logarithms shows \(r(d)\leq h\).

Every unordered pair of distinct primes \(p,q\in\mathcal P\) satisfies

\[
 pq\leq b^2X\leq X.
\]

The divisor property therefore supplies a \(d\in D\) with \(pq\mid d\).
One fixed \(d\) contains exactly \(\binom{r(d)}2\) prime pairs from
\(\mathcal P\), at most \(\binom h2\). Counting incidences, with repeated
coverage allowed, gives

\[
 \binom v2
 \leq\sum_{d\in D}\binom{r(d)}2
 \leq M\binom h2.
\tag{29}
\]

This proves (13). Unlike the He--Sahai rank-one argument, it makes no claim
that two cover values share at most one band prime. It needs no such
intersection bound.

## 4. Exponent consequences

Under (14), every positive difference is smaller than the common height of
\(S\cup T\), so

\[
 \log H\leq X^{\alpha+o(1)},
 \qquad
 M\leq |S|\,|T|\leq X^{2\beta+o(1)}.
\tag{30}
\]

Equations (5), (6), and (30) imply

\[
 X^{1+o(1)}
 \leq X^{\alpha+2\beta+o(1)},
\]

and therefore \(\alpha+2\beta\geq1\).

For fixed \(0<a<b\leq1\), the prime number theorem gives

\[
 v=\pi(b\sqrt X)-\pi(a\sqrt X)
   =X^{1/2+o(1)},
\tag{31}
\]

where the suppressed factor is of order \(1/\log X\). Also

\[
 h\leq
 \frac{X^{\alpha+o(1)}}{(1/2+o(1))\log X}
 =X^{\alpha+o(1)}.
\tag{32}
\]

If \(h<2\) infinitely often, (13) already fails once \(v\geq2\).
Otherwise (13), (30)--(32) give

\[
 X^{1+o(1)}\leq X^{2\beta+2\alpha+o(1)},
\]

so \(\alpha+\beta\geq1/2\). Keeping the logarithmic factors in (31) and
(32) yields the same exponent conclusion.

If the explicit factor-output time is \(F\leq X^{\gamma+o(1)}\), then
(9), (10), and (5) give

\[
 X^{1+o(1)}\leq X^{2\beta+\gamma+o(1)},
\]

which proves (17).

The cited He--Sahai theorem supplies the stronger rank-one length bound
(18) when \(\log H=o(\sqrt X)\). Its proof uses the identity that the
difference of two terms in one arithmetic progression is an index
difference times one common step. A rank-two difference has two independent
coefficients, so that step of their proof is unavailable. F272 does not
replace it with a higher-rank obstruction.

Umans--Wang Theorem 5.5 maps their prefactored parameters to deterministic
integer-factoring time

\[
 \widetilde O\!\left(N^{\max(\alpha,\beta)/2+o(1)}\right).
\]

At \(\alpha=\beta=1/3\), this is \(N^{1/6+o(1)}\), which is exponential
in the binary input length. This establishes the stated relevance boundary.

## 5. Prime separation

For distinct primes \(p,q\leq X\), a separating integer \(A_i\) exists
exactly when \(c(p)\ne c(q)\). Thus all \(\pi(X)\) codewords are distinct,
and the binary cube contains at most \(2^m\) words. This proves (20).

At most one of these distinct words is the all-zero word. Every other prime
appears as a divisor of at least one \(A_i\), and hence its binary name
appears in at least one explicit complete factorization. If \(p_0\) is the
possible omitted prime, the total factor-output length is at least

\[
 \vartheta_2(X)-\log_2p_0
 \geq\vartheta_2(X)-\log_2X.
\tag{33}
\]

The total is at most \(mF\), proving (21).

## 6. Why the succinct interval seam is not refuted

The proof of Theorem 1 charges the expanded binary lengths of the cover
values. A circuit that returns a huge value modulo a supplied modulus need
not expand that value, so (6) is not a circuit lower bound. The proof of
Theorem 2 instead charges complete explicit prime-factor output. A decoder
that recursively uses gcds and modular products without ever printing the
cover value's full factorization lies outside that theorem too.

Suppose the interval evaluator (22) were available. First apply a
deterministic polynomial-time primality test. On a composite \(N\), let
\(X=\lfloor\sqrt N\rfloor\), compute the product of \([1,X]\) modulo
\(N\), and take its gcd \(g\) with \(N\). A least prime factor of \(N\)
is at most \(X\), so \(g>1\). If \(g<N\), it is already a proper divisor.

It remains to handle \(g=N\). Maintain an interval \(I\subseteq[1,X]\)
whose exact product is divisible by \(N\). Split \(I=I_0\sqcup I_1\) into
two consecutive subintervals and compute

\[
 g_0=\gcd\!\left(\prod_{j\in I_0}j\bmod N,N\right).
\]

If \(1<g_0<N\), return it. If \(g_0=N\), continue with \(I_0\). If
\(g_0=1\), coprimality and \(N\mid\prod_{j\in I_0}j\prod_{j\in I_1}j\)
imply \(N\mid\prod_{j\in I_1}j\), so continue with \(I_1\). This is one
recursive path of depth \(O(\log X)\). It cannot reach a singleton
\(I=\{j\}\), because then \(N\mid j\leq X<N\). A proper divisor must
therefore be returned earlier. Factoring the two smaller outputs recursively
creates at most \(\log_2N\) nontrivial split nodes, because every leaf is
at least two and their product is \(N\). A quasipolynomial cost at each
node therefore remains quasipolynomial after the polynomial node factor.
Standard primality tests and output verification are polynomial-time. This
is the exact reason a uniform evaluator of (22) is strong enough.

Conversely, F197 proves on balanced distinct semiprimes that
\(\gcd(\lfloor\sqrt N\rfloor!,N)\) is already the smaller factor. Thus the
full-interval instance of (22) is already factor-bearing. F272 neither
constructs that evaluator nor treats it as a weaker assumption than the
target theorem.
