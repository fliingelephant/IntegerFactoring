# F180 blind reconstruction

## Source discipline

The SHA-256 of `STATEMENT.md` was verified before reading:

```text
9ae4beb80683a7b7e61c82a91891e2e1f849ac96d498f3570519bfbebb9b1f29
```

This reconstruction uses only that statement. No proof, audit, manifest, or
ledger was consulted.

## Verdict

**Strict statement-only verdict: FAIL AS WRITTEN.** The statement never
defines `n` as the bit length of `N`, or otherwise assumes that every
exponent `a` in a primary divisor \(\ell^a\parallel f_j\) satisfies
\(a\le n\). Without that condition, a primary part can be only partly
deleted. Equations (6)--(8), the stated hard-descendant characterization,
and the bit-cost bound are then false.

**Conditional verdict: PASS after one explicit size convention.** It is
sufficient to add

\[
n\ge \max_{j,\,\ell^a\parallel f_j}a
\quad\text{and}\quad
\log_2(N+3)=O(n).
\tag{A}
\]

The usual convention \(n=\lceil\log_2 N\rceil\) implies both requirements:
\(\ell^a\le f_j\le\varphi(R_j)\le R_j\le N\) gives \(a\le n\).
Under (A), all claimed algebraic and algorithmic conclusions follow. The
double-extinction resultant theorem, including arbitrary primary powers,
in fact remains valid without the first part of (A); it has a stronger
valuation proof given below.

## 1. Exact primary filtering

Put \(q=N+\delta\), \(A=A_\delta\), and \(E=A^n\). For every
\(\ell^a\parallel f_j\), the standard order identity gives

\[
\operatorname{ord}_{R_j}(y^E)
=\frac{f_j}{\gcd(f_j,E)},
\qquad
v_\ell\!\left(\operatorname{ord}_{R_j}(y^E)\right)
=\max\{a-nv_\ell(A),0\}.
\tag{B}
\]

Also,

\[
v_\ell(A)>0
\iff
\ell\nmid q\ \text{ and }\ \operatorname{ord}_\ell(q)\le K.
\tag{C}
\]

Indeed, if \(\ell\mid q\), then \(q^k-1\equiv-1\pmod\ell\) for every
\(k\). If \(q\) is a unit modulo \(\ell\), some factor \(q^k-1\),
\(1\le k\le K\), is divisible by \(\ell\) exactly when the order of \(q\)
modulo \(\ell\) is at most \(K\).

Equation (C) detects positive valuation only. It does not by itself show
that \(nv_\ell(A)\ge a\). Under (A), positive valuation is enough because
\(nv_\ell(A)\ge n\ge a\). Then (B) and (C) prove (6) and the product formula
(7). Without (A), (B) permits partial deletion and disproves the claimed
dichotomy.

### Explicit counterexample to (6)--(8)

Take

\[
n=1,\quad T=2,\quad K=1,\quad
N=27331=181\cdot151,\quad y=27189,
\]

with \(R_1=181\) and \(R_2=151\). This works for every fixed \(c\ge1\),
because \(K=\lceil(\log_2 2)^c\rceil=1\). The relevant residues are

\[
y\equiv39\pmod{181},\qquad y\equiv9\pmod{151},
\]

and direct modular exponentiation gives

\[
39^3\equiv132,\quad39^9\equiv1\pmod{181},
\qquad
9^5\equiv8,\quad9^{25}\equiv1\pmod{151}.
\]

Thus \((f_1,f_2)=(9,25)\). All explicit assumptions hold:
\(f_j>1\), \(\gcd(f_j,N)=1\), and \(\sigma(f_j)>2\ge1\).

For \(\delta=0\),

\[
A_0=N-1=27330,
\qquad v_3(A_0)=v_5(A_0)=1.
\]

Consequently \(z_0\) has local orders \(3\) and \(5\), not \(1\) and
\(1\). Numerically, \(z_0=8917\pmod N\) and
\(H_0=\gcd(8916,27331)=1\). Yet

\[
\operatorname{ord}_3(N)=\operatorname{ord}_5(N)=1\le K.
\]

Hence (7) incorrectly predicts full deletion of the \(3^2\) and \(5^2\)
parts, and the surviving orders directly contradict (8). This also refutes
the claim that an \(H_0=1\) descendant necessarily has a long public action
under the assumptions actually written.

Under (A), the remaining claims about \(H_\delta\) are correct. A value
\(1<H_\delta<N\) is a nontrivial factor by definition. If \(H_\delta=1\),
then no \(R_j\) divides \(z_\delta-1\), so every local filtered order is
nontrivial; (7) supplies a surviving primary part. For \(\delta=0\), a
prime \(\ell\mid f_j\) cannot divide \(N\) because
\(\gcd(f_j,N)=1\). Thus every prime in a surviving local order must satisfy
\(\operatorname{ord}_\ell(N)>K\), proving (8) under (A).

## 2. Resultants and synchronized extinction

Let

\[
F_k(X)=X^k-1,
\qquad
G_l(X)=(X+3)^l-1.
\]

### Nonvanishing and size

If \(F_k\) and \(G_l\) had a common complex root \(\alpha\), then
\(|\alpha|=|\alpha+3|=1\). But

\[
3=|(\alpha+3)-\alpha|
\le |\alpha+3|+|\alpha|=2,
\]

a contradiction. Therefore every \(R_{k,l}\) is nonzero.

Since \(F_k\) is monic,

\[
R_{k,l}
=\prod_{\alpha^k=1}\left| (\alpha+3)^l-1\right|.
\]

For every such \(\alpha\), \(|\alpha+3|\le4\), and hence

\[
\left|(\alpha+3)^l-1\right|
\le4^l+1<2^{2l+1}.
\]

Multiplication over the \(k\) roots proves the strict bound
\(\log_2R_{k,l}<k(2l+1)\) in (11).

### Prime support and arbitrary primary powers

Assume \(H_0=H_3=N\). Then, for every \(j\),

\[
f_j\mid A_0^n
\quad\text{and}\quad
f_j\mid A_3^n.
\tag{D}
\]

Fix \(\ell^a\parallel f_j\), and define

\[
u_k=v_\ell(F_k(N)),\quad
v_l=v_\ell(G_l(N)),\quad
U=\sum_{k=1}^K u_k,\quad
V=\sum_{l=1}^K v_l.
\]

Equation (D) gives \(a\le nU\) and \(a\le nV\). Because \(F_k\) and
\(G_l\) are monic integer polynomials, their resultant has an integral
Bezout identity

\[
R_{k,l}=B_{k,l}(N)F_k(N)+C_{k,l}(N)G_l(N)
\]

up to an irrelevant sign. Therefore

\[
v_\ell(R_{k,l})\ge\min(u_k,v_l).
\tag{E}
\]

The elementary inequality

\[
\sum_{k,l}\min(u_k,v_l)\ge\min(U,V)
\tag{F}
\]

follows, for example, by assuming \(U\le V\) and observing that
\(\sum_l\min(u_k,v_l)\ge\min(u_k,V)=u_k\) for every \(k\).
Combining (E) and (F) yields

\[
v_\ell(M)
=n\sum_{k,l}v_\ell(R_{k,l})
\ge n\min(U,V)
\ge a.
\]

Thus every \(\ell^a\parallel f_j\) divides \(M\), proving (13) with its
full prime-power multiplicity. This proof does not need \(a\le n\).
At the support-only level, \(U,V>0\) select some \(k,l\) for which \(N\)
is a common root of \(F_k,G_l\) modulo \(\ell\), so
\(\ell\mid R_{k,l}\).

## 3. Exact common-order recovery

Factor \(M\), set \(m=M\), and process each prime \(q\mid m\). While
\(q\mid m\), compute

\[
g=\gcd(y^{m/q}-1,N).
\]

Return \(g\) if \(1<g<N\). If \(g=N\), replace \(m\) by \(m/q\). If
\(g=1\), retain that copy of \(q\) and move to the next prime.

Initially every \(f_j\mid m\) by (13). A removal with \(g=N\) preserves
this invariant because \(y^{m/q}=1\pmod{R_j}\) for every \(j\). If a test
returns \(g=1\), then no \(f_j\) divides \(m/q\): otherwise
\(R_j\mid y^{m/q}-1\), forcing the gcd to be nontrivial. Since
\(f_j\mid m\), this means

\[
v_q(f_j)=v_q(m)
\]

for every \(j\) at the failed removal. Later steps do not change the
\(q\)-valuation. Therefore, if no factor is returned, every prime valuation
of the final \(m\) equals the corresponding valuation of every \(f_j\).
Hence

\[
m=f_1=\cdots=f_s>T\ge n.
\]

The retained factorization of \(M\) is an explicit factorization of \(m\),
so this proves the claimed exact common-order state.

## 4. Trichotomy

Under (A), the gcd outcomes exhaust all cases.

1. A proper \(H_0\) or \(H_3\), or a proper gcd during stripping, returns
   a factor.
2. \(H_0=H_3=N\) reaches the resultant construction. Section 3 then
   returns either a factor or a factored exact common order above \(n\).
3. If \(H_0=1\), (8) gives a long \(N\)-action period for every surviving
   primary prime. If \(H_0=N,H_3=1\), (7) says every original primary prime
   has \(N\)-action period at most \(K\), while every primary prime surviving
   the second filter either divides \(N+3\) or has
   \((N+3)\)-action period greater than \(K\).

This proves (14) and its two hard-branch descriptions under (A). Under the
literal statement, the explicit counterexample enters case \(H_0=1\) with
only short unit-action survivors, so the hard-branch description and the
last sentence of Section 3 are false. The synchronized-extinction closure
itself remains correct by Sections 2 and 3.

## 5. Cost and scope

The exact size before imposing a relation between \(N\) and \(n\) is

\[
\log_2(A_\delta^n)
=O\!\left(nK^2\log_2(N+3)\right).
\tag{G}
\]

Thus the claimed \(O(n^2K^2)\) bound follows from
\(\log_2(N+3)=O(n)\), but not from the written assumptions alone. For
example, with fixed \(n=1,T=2\), the allowed family \(N=7^e\) has units of
order \(3\) for every \(e\), while the size of \(A_0=N-1\) is unbounded.

The resultant bound gives \(O(K^2)\) bits per resultant and
\(O(nK^4)\) bits for \(M\). Exact Sylvester-determinant computation is
polynomial in these small degrees and heights. Trial division of each of
the \(K^2\) resultants uses at most \(2^{O(K^2)}\) bit operations in total.
The number of stripping iterations is polynomial in \(\log M\), and each
modular exponentiation and gcd is polynomial in \(\log M\) and \(\log N\).
Under (A), all polynomial factors in \(n\) are absorbed by

\[
2^{O(K^2)}=2^{(\log n)^{O(1)}}.
\]

Without \(\log N=O(n)\), this cannot be a bit-cost bound for processing the
input \(N\), so the literal complexity claim fails.

The stated scope boundary is otherwise accurate. The construction does not
force either nonsynchronized descendant to vanish, and it leaves a hard
branch. Therefore it is a conditional postprocessor, not an all-input
quasipolynomial-time factoring algorithm.
