# Proof of F197

## 1. Factorial and interval-product valuations

From \(p<\sqrt N<q\) and integrality of \(p\),

\[
p\le B<q.
\tag{22}
\]

Also \(q<2p\) gives \(N<2p^2\), hence \(B<2p\). The interval
\(1,\ldots,B\) contains exactly one multiple of \(p\), namely \(p\), and
contains no multiple of \(q\). Thus

\[
v_p(B!)=1,
\qquad v_q(B!)=0,
\tag{23}
\]

which proves (2) and (3).

For \(D=\prod_{j=1}^B(N-j)\), reduction modulo \(q\) gives factors
\(-j\), all nonzero because \(B<q\). Hence \(q\nmid D\). Modulo \(p\),
the only divisible factor is

\[
N-p=p(q-1).
\tag{24}
\]

It contains exactly one power of \(p\). Indeed, if \(p\mid q-1\), then
\(p<q<2p\) forces \(q=p+1\), impossible because \(p,q\) are odd. Thus
\(v_p(D)=1\), proving (5).

The identity (4) is the ordinary exact numerator/denominator formula for
the binomial coefficient. Equations (3) and (5) prove the stated
exact-division collapse. No assertion is made about a representation that
does not expose either product or residue.

## 2. Explicit block count

The dense coefficient vector of the degree-\(u\) polynomial \(P_u\) has
\(u+1\) positions. Covering \(B\) consecutive factors by width-\(u\)
blocks requires \(\lceil B/u\rceil\) block positions, including a possible
short final block. Dropping one harmless constant, the number of exposed
positions is at least

\[
u+\left\lceil\frac Bu\right\rceil.
\tag{25}
\]

Since \(\lceil B/u\rceil\ge B/u\), the arithmetic-geometric mean inequality
gives (7). This proves Theorem 2 only in its explicitly defined
representation model.

## 3. Published baby-step/giant-step and holonomic bounds

Bostan, Gaudry, and Schost describe the same block polynomial as (6), with
block width of order \(\sqrt L\). Their arbitrary-ring factorial statement
costs \(O(\mathsf M_R(\sqrt L)\log L)\) ring operations. They then sharpen
the evaluation of polynomial-coefficient recurrences; for fixed scalar
dimension, the resulting scale is quasi-linear in \(\sqrt L\).

The recurrence (8) places \(F=B!\) directly inside that framework. With
fast polynomial and residue arithmetic, substituting \(L=B\) gives

\[
B^{1/2+o(1)}\operatorname{poly}(n)
\tag{26}
\]

bit operations. Since \(B=\Theta(\sqrt N)\), this is the scale in (10).

Costa and Harvey explicitly work in multitape Turing bit complexity. Their
introduction reconstructs the factorial identity

\[
K!=f(0)f(L)\cdots f((L-1)L),
\qquad K=\lfloor\sqrt N\rfloor,
\tag{27}
\]

and the gcd extraction \(\gcd(K!\bmod N,N)\). They cite the BGS complete
factorization bound

\[
O\!\left(\mathsf M_{\rm int}(N^{1/4}\log N)\right)
\tag{28}
\]

and prove the refinement

\[
O\!\left(
\mathsf M_{\rm int}\!\left(
\frac{N^{1/4}\log N}{\sqrt{\log\log N}}
\right)
\right).
\tag{29}
\]

Both retain the \(N^{1/4}\) power. Equations (26)--(29) establish only the
claimed upper scales. They do not turn an algorithmic upper bound into a
general lower bound.

## 4. Exact modular-division laws

Equation (23) writes \(F=pU\) with \(\gcd(U,N)=1\). Therefore

\[
N\mid F(x-y)
\quad\Longleftrightarrow\quad
pq\mid pU(x-y)
\quad\Longleftrightarrow\quad
q\mid x-y,
\tag{30}
\]

which proves (11).

Likewise,

\[
N^2\mid F(x-y)
\quad\Longleftrightarrow\quad
p^2q^2\mid pU(x-y)
\quad\Longleftrightarrow\quad
pq^2\mid x-y,
\tag{31}
\]

which proves (12). The kernel modulo \(N^2\) consists of the \(p\)
multiples of \(pq^2\). If \(0\le x,y<N\), then \(|x-y|<N<q^2\), so
(31) forces \(x=y\). This proves the injectivity and nonunit assertions in
Theorem 4 without claiming an efficient custom decoder.

For (15), write \(F=a_2+kN^2\). Division by positive \(N\) and canonical
Euclidean remainders give

\[
R=a_2\bmod N,
\qquad
Q=\left\lfloor\frac{a_2}{N}\right\rfloor+kN.
\tag{32}
\]

Because \(0\le a_2<N^2\), its quotient by \(N\) is the canonical value of
\(Q\bmod N\). This proves (15). Reducing \(F=NQ+R\) modulo \(N\) also
gives

\[
\gcd(R,N)=\gcd(F,N)=p.
\tag{33}
\]

## 5. Exact-output size and quotient bits

The upper bound \(F\le B^B\) and the last \(\lfloor B/2\rfloor\) factors
give

\[
\left\lfloor\frac B2\right\rfloor
\log_2\!\left(\frac B2\right)
\le \log_2 F
\le B\log_2 B.
\tag{34}
\]

Thus \(\log_2F=\Theta(B\log B)=2^{\Theta(n)}\). The product \(D\) is at
least \((N-B)^B\), so its bit length is also exponential. Once \(F>2N\),
\(Q=\lfloor F/N\rfloor>F/(2N)\), and subtracting \(O(n)\) bits from the
bit length of \(F\) preserves \(2^{\Theta(n)}\). The excluded inputs form a
finite initial set.

It remains to prove that (16) is easy. Legendre's identity computes

\[
v_2(F)=\sum_{i\ge1}\left\lfloor\frac{B}{2^i}\right\rfloor
\tag{35}
\]

in polynomial time. If this valuation is at least \(n\), then \(f_2=0\).
Otherwise \(\lfloor B/2\rfloor<n\), hence \(B<2n+2\), and direct modular
multiplication of the \(B\) factors computes \(f_2\) in polynomial bit
time. This proves the claim uniformly.

Reducing \(F=NQ+R\) modulo \(2^n\) gives

\[
R\equiv f_2-NQ_2\pmod{2^n}.
\tag{36}
\]

Since \(N+1\le2^n\) and \(0<R<N\), the canonical residue in (18) is the
integer \(R\). Equation (33) then factors \(N\).

Finally, if \(F=a+kN2^n\) with \(a\) as in (19), Euclidean division by
\(N\) yields

\[
R=a\bmod N,
\qquad
Q=\left\lfloor\frac aN\right\rfloor+k2^n.
\tag{37}
\]

This proves (20) and Theorem 5.

## 6. One-child recursion

Let \(q(m)\) be a nondecreasing quasipolynomial dominating the per-node
term in (21). Unrolling the single chain gives

\[
T(m)\le T(0)+\sum_{j=1}^{m}q(j)
\le T(0)+mq(m).
\tag{38}
\]

Multiplication by \(m\) preserves the quasipolynomial class. Hence no
fixed-ratio contraction is needed. The explicit root cost (7), and the
published root upper scales (26)--(29), are separate statements; neither is
derived from the recursion depth. This proves Theorem 6.

