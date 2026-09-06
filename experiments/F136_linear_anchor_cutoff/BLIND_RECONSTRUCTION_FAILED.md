# Blind reconstruction of F136

## Scope and verdict

I read only STATEMENT.md. Its SHA-256 is

    2a456da6341d4a055cf07305d463319b5fbcef3abd5344581b752f0d8aa0fa49

The elementary number-theoretic core of Theorems 1–3 is correct, including
the constants \(2^{18}\), \(21846\), \(12\), \(6/25\), and \(37/50\), under
the standard intended conventions listed below. Theorem 4 and some
algorithm-facing conclusions cannot be independently reconstructed from the
statement alone because their objects and cost bounds are not defined there.
For that reason, this is a failed *complete* blind reconstruction, not an
arithmetic refutation.

No numerical counterexample was found to any well-defined arithmetic claim.

## Conventions needed for Theorems 2 and 3

The statement does not define several terms. The conditional reconstruction
of Theorems 2 and 3 uses these standard meanings:

1. A unit block \(q\) is a positive integer with \(\gcd(q,N)=1\).
2. \(w=\iota_N(q)\) is the least positive inverse of \(q\) modulo \(N\), so
   \(1\leq w<N\).
3. \(P_N(q)=qw\), and an anchored endpoint is the stated exact integer
   \(P_N(\ell q)=q(w+NA_\ell)\).
4. Processing retains these exact endpoint integers as parity-matrix columns.
5. After named prime powers are removed from \(H_A\), every residual block
   produced by refinement divides the remaining cofactor.

Without these conventions, the references to \(\iota_N\), \(P_N\), unit
blocks, retained values, parity matrices, and residual blocks do not specify
mathematical propositions.

## Theorem 1

Let

\[
\psi(x)=\sum_{p^a\leq x}\log p
=\log\operatorname{lcm}(1,\ldots,\lfloor x\rfloor).
\]

Set \(m=\lfloor x/2\rfloor\). For every prime \(p\),

\[
v_p\binom{2m}{m}
=\sum_{j\geq1}\left(
\left\lfloor\frac{2m}{p^j}\right\rfloor
-2\left\lfloor\frac m{p^j}\right\rfloor
\right).
\]

Each summand is \(0\) or \(1\), and it vanishes for \(p^j>2m\). Therefore

\[
v_p\binom{2m}{m}\leq\lfloor\log_p(2m)\rfloor,
\]

so the central binomial coefficient divides
\(\operatorname{lcm}(1,\ldots,2m)\). It is the largest of the \(2m+1\)
binomial coefficients whose sum is \(4^m\). Hence

\[
\psi(x)\geq\log\binom{2m}{m}
\geq2m\log2-\log(2m+1)
>(x-2)\log2-\log(x+1).                                      \tag{A}
\]

Let \(K=\lfloor\log_2x\rfloor\). Prime-power bookkeeping gives

\[
\psi(x)-\vartheta(x)=\sum_{k=2}^{K}\vartheta(x^{1/k}).
\]

The elementary estimate \(\vartheta(y)\leq y\log y\) now gives

\[
\frac{\psi(x)-\vartheta(x)}x
\leq
\frac{\log x}{2\sqrt x}
+\frac{\log x\,(\log_2x-2)}{3x^{2/3}}.                       \tag{B}
\]

Indeed, the \(k=2\) term gives the first summand. For \(k\geq3\), use
\(x^{1/k}\leq x^{1/3}\), \(1/k\leq1/3\), and at most \(K-2\) terms.

After dividing (A) by \(x\) and subtracting (B),

\[
\frac{\vartheta(x)}x>
\log2-
\frac{2\log2+\log(x+1)}x-
\frac{\log x}{2\sqrt x}-
\frac{\log x\,(\log_2x-2)}{3x^{2/3}}.                        \tag{C}
\]

All three subtracted functions decrease for \(x\geq2^{18}\). For the last
one, put \(t=\log x\). Its logarithmic derivative is

\[
\frac1t+\frac1{t-2\log2}-\frac23.
\]

For \(t\geq18\log2\), the elementary bound \(\log2>1/2\) makes the sum of
the first two terms less than \(1/9+1/8<2/3\).

At \(x_0=2^{18}\), use \(1/2<\log2<1\) and
\(\log(x_0+1)<\log(2x_0)=19\log2<19\). The three error terms in (C) are
then less than

\[
\frac{21}{262144},\qquad
\frac{18}{1024}=\frac9{512},\qquad
\frac{18\cdot16}{3\cdot4096}=\frac3{128}.
\]

Their sum is less than \(337/8192<1/20\). Thus (C) is greater than
\(1/2-1/20=9/20>6/25\). This proves (1) for every real
\(x\geq2^{18}\), using only the advertised elementary ingredients.

For \(n\geq21846\), \(B=12n\geq262152>2^{18}\). Also \(N<2^n\), since
\(n=\lceil\log_2(N+1)\rceil\). The exponential-series bound

\[
e^{7/10}>
1+\frac7{10}+\frac1{2}\left(\frac7{10}\right)^2
+\frac1{6}\left(\frac7{10}\right)^3
=\frac{12013}{6000}>2
\]

shows \(\log2<7/10\). Consequently,

\[
\vartheta(B)>\frac6{25}(12n)=\frac{72}{25}n
>4n\log2>4\log N.
\]

Exponentiation proves (2). The threshold \(21846\) is the first integer
\(n\) for which \(12n\geq2^{18}\). The smaller inputs form a fixed finite
set, so finite trial division can handle them, without a claim of
practicality.

## Theorem 2

Let

\[
D=\prod_{\substack{\ell\leq B\ {\rm prime}\\ \ell\mid Nq}}\ell.
\]

Then \(D\leq\operatorname{rad}(Nq)\leq Nq<N^2/B\), and

\[
G_B(N,q)=\frac{\prod_{\ell\leq B}\ell}{D}
>\frac{N^4}{N^2/B}=N^2B.
\]

This proves (3).

For every occupied digit, define

\[
L_A=\prod_{A_\ell=A}\ell.
\]

Every named prime in \(L_A\) divides \(H_A\), and the buckets partition the
eligible primes. Thus

\[
G_B(N,q)=\prod_A L_A,
\qquad L_A\mid H_A.                                          \tag{D}
\]

Every occupied digit satisfies \(0\leq A<B\). Hence

\[
H_0=w<N,
\qquad H_A=w+NA<NB\quad(A>0).                                \tag{E}
\]

Let \(d\) be the number of occupied nonzero digits. If \(d\leq1\), (D) and
(E), inserting the harmless factor \(N\) if the zero bucket is absent, give

\[
G_B(N,q)<N(NB)=N^2B,
\]

contrary to (3). Therefore \(d\geq2\).

Now let \(r>B\) be prime with \(v_r(q)\) odd. Since \(q\) is a unit modulo
\(N\), \(r\nmid N\). If \(r\mid H_A\) and \(r\mid H_C\), then

\[
r\mid H_A-H_C=N(A-C),
\]

so \(r\mid A-C\). But distinct digits have \(0<|A-C|<B<r\), a
contradiction. Thus at most one digit, including digit zero, has
\(r\mid H_A\).

The unary endpoint \(qH_0\) and the endpoints for the at least two occupied
nonzero digits are distinct. All but at most one have

\[
v_r(qH_A)=v_r(q),
\]

which is odd. Exact-value deduplication therefore leaves at least two such
integers. This proves the arithmetic content of (4), conditional on the
matrix retaining the stated endpoints. The declared gcd-screen alternative
is algorithmic and is not defined in the statement.

The prose region with \(q<N/(12n+1)\) and \(r>12n+1\) is a strict subset of
the proved region \(q<N/B\), \(r>B\), because \(B=12n\). It is therefore
valid, though weaker than the boxed theorem.

## Theorem 3

Let

\[
Q_A=\prod_{\ell\in\mathcal L_A}\ell^{v_\ell(H_A)}
\]

be the full product of the named anchor-prime powers in \(H_A\), and let
\(R_A=H_A/Q_A\). Since \(Q_A\geq L_A\), (E) gives

\[
A=0,\ L_0>B
\quad\Longrightarrow\quad
R_0\leq\frac{H_0}{L_0}<\frac NB,
\]

and

\[
A>0,\ L_A>B^2
\quad\Longrightarrow\quad
R_A\leq\frac{H_A}{L_A}<\frac{NB}{B^2}=\frac NB.
\]

If \(R_A=1\), this is residual exhaustion. Otherwise every factor block of
\(R_A\) is also smaller than \(N/B\). This proves the release bounds,
conditional on the stated interpretation of refinement.

On the no-release branch, with an empty zero bucket interpreted as
\(L_0=1\), (D) gives

\[
G_B(N,q)=L_0\prod_{A>0}L_A
\leq B(B^2)^d=B^{2d+1}.                                      \tag{F}
\]

For a sharper lower bound than (3), reuse the proof of (3) before weakening
its constants:

\[
\begin{aligned}
\log G_B(N,q)
&=\vartheta(B)-\log D\\
&>\frac{72}{25}n-2\log N+\log B\\
&>2\left(\frac{36}{25}-\log2\right)n+\log B.                 \tag{G}
\end{aligned}
\]

Combining (F) and (G) yields

\[
d>\left(\frac{36}{25}-\log2\right)\frac n{\log B}.
\]

Since \(B=12n\), \(\log2<7/10\), and
\(36/25-7/10=37/50\),

\[
d>
\frac{37n}{50\log(12n)}
>
\frac{37n}{50\log(13n)}.
\]

This proves (6), with a stronger intermediate bound. The earlier argument
showing that at most one \(H_A\) is divisible by \(r\) shows that at least
\(d-1\) of the distinct nonzero-digit endpoints \(qH_A\) have odd
\(r\)-valuation. Subtracting one from an
\(\Omega(n/\log n)\) lower bound preserves that asymptotic order.

The release thresholds and their complements are exhaustive. Therefore the
arithmetic alternatives in (7) follow, again conditional on the meanings of
retention and refinement.

## Theorem 4: not reconstructible from the statement

The displayed parameter definitions alone imply

\[
L=\Theta(\log n),\qquad \log_2E=L^2,
\qquad T=L^2,
\qquad E^T=2^{L^4}=2^{O((\log n)^4)}.
\]

They do not say that the transcript has at most \(E^T\) nodes, that
refinement costs only polynomial work per node, or that the decoder fits the
same bound. The following necessary inputs are absent:

- the anchored all-block source and its anchor/cost guarantee;
- the adaptive transcript's branching and depth bounds;
- the representation and bit cost of complete gcd-free refinement;
- the definition and complexity of the P66 decode.

Thus (8) would follow from a suitable external composition theorem with an
\(E^{O(T)}\) work bound, but no such theorem or hypothesis appears in the
statement. The assertion that the existing source already contains all
anchors through \(B\) is likewise external. I cannot prove or refute (8)
under the strict blind restriction.

## Exact consequence and remaining gap

For an integer \(q\), its squarefree kernel is not \(B\)-smooth exactly when
some prime \(r>B\) has odd \(v_r(q)\). Applying Theorem 2 to each such prime
proves the stated arithmetic dichotomy for \(n\geq21846\). Replacing \(N/B\)
by the smaller \(N/(12n+1)\) remains valid.

Row multiplicity at least two does not by itself force a binary kernel. For
example, over \(\mathbb F_2\),

\[
\begin{pmatrix}
1&1&0\\
1&0&1\\
1&1&1
\end{pmatrix}
\]

has every row of weight at least two but determinant \(1\), so its right
kernel is zero. This independently confirms the stated logical gap. The
specific claims attributed to P121, P122, F135, and P66 cannot be checked
without reading prohibited external material.

## Counterexample log

- No counterexample was found to Theorem 1, inequalities (2), (3), or (6),
  or to the elementary release bounds.
- The full-rank matrix above is not a counterexample to F136. It is a
  counterexample to the stronger, explicitly rejected inference that reused
  rows alone force a nonzero binary kernel.
- Undefined algorithmic terms prevent a truth-valued blind test of the
  matrix-retention claims and (8). This is missing specification, not a
  counterexample.
