# Proof of the F179 two-shift resultant closure

## 1. Meaning of the gcd scans

Modulo a hidden component \(R_j\), equation (5) vanishes exactly when

\[
f_j\mid (N+\delta)^k-1.
\tag{1}
\]

If this holds on a proper nonempty subset of components, the gcd is a proper
factor. On a no-factor run, a scan with no global return has every gcd equal
to one.

For \(\delta=0\), equation (3) gives \(\gcd(N,f_j)=1\). Hence the least positive
\(k\) satisfying (1) is \(\operatorname{ord}_{f_j}(N)\). If no component
has such a \(k\le K\), (6) follows. If one component had such a \(k\) while
another did not, the corresponding gcd would be proper.

For \(\delta=3\), a component on which \(N+3\) is a unit has the same order
interpretation. A nonunit can never have a positive power equal to one.
This proves the alternative (7)--(8).

## 2. Divisibility by the resultant

Global returns at \(a,b\) give

\[
f_j\mid P(N),
\qquad
f_j\mid Q(N)
\tag{2}
\]

for every \(j\). The Sylvester-matrix identity supplies polynomials
\(A,B\in\mathbb Z[X]\) such that

\[
A(X)P(X)+B(X)Q(X)=\operatorname{Res}_X(P,Q).
\tag{3}
\]

Evaluating at \(X=N\) and using (2) proves (11).

## 3. Nonvanishing and size

If the resultant were zero, the two monic polynomials would share a complex
root \(z\). Then

\[
|z|=1,
\qquad
|z+3|=1.
\]

But the reverse triangle inequality gives \(|z+3|\ge3-|z|=2\), a
contradiction. Thus \(R>0\).

Using the \(a\) roots of \(P\),

\[
R=\prod_{z^a=1}\left|(z+3)^b-1\right|.
\tag{4}
\]

For every such \(z\),

\[
\left|(z+3)^b-1\right|
\le4^b+1<2^{2b+1}.
\]

Taking the product proves (12).

## 4. Exact order recovery

The degrees are at most \(K\), so the resultant is computable exactly in
time polynomial in \(K\) and its output bit length. Trial division through
\(\sqrt R\) costs \(2^{O(K^2)}\), which is QP for fixed \(c\).

Since every \(f_j\mid R\), the completely factored integer \(R\) is a
common annihilating multiple for \(y\). Standard factor-first stripping
tests prime divisors of the current multiple by gcds of modular powers. An
unequal prime-adic exponent among the local orders produces a proper gcd.
On the no-factor branch, stripping terminates at their common exact order
\(m\), with its factorization. Equation (3) of the statement implies
\(m>T\ge n\).

All exponents in (5) have \(O(Kn)\) bits. Together with the resultant and
order-reduction bounds, the full procedure has uniform deterministic QP bit
cost.

This proves the trichotomy. The proof supplies no bound on the surviving
shift periods.
