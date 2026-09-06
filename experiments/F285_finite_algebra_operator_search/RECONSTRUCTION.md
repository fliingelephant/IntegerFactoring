# F285 — Blind reconstruction

## Provenance and restrictions

The only mathematical input inspected for this reconstruction was:

`/Users/zhou/autoresearch/IntegerFactoring/experiments/F285_finite_algebra_operator_search/RECONSTRUCTION_STATEMENTS.md`

SHA-256:

`259375eb1a4494cd010055c61f5f5bb7f0927388216da05092a02bf8a5717377`

No result file, dimension-extension note, script, experimental output, ledger,
catalog, or live-route note was inspected. No numerical experiment was run.

## Outcomes

| Claim | Outcome |
|---|---|
| 1. Exact kernel and rank | Reconstructed as stated. |
| 2. Uniform dimension cutoff | Reconstructed as stated, including the factor-degree refinement. |
| 3. Local sharpness | Reconstructed as stated in both cases. |
| 4. Explicit exceptional-prime bound | Reconstructed as stated. |
| 5. Density interpretation | Reconstructed as stated for the asymptotic claim. The exact finite fraction is immediate whenever the interval contains a prime; nonemptiness for every stated `p` additionally invokes Bertrand's postulate, or can be omitted because PNT already gives eventual nonemptiness needed for the limit. |

## Claim 1: exact kernel and rank

Put \(F=\mathbb F_r\), and let \(K/F\) be a splitting field of the
characteristic polynomial of \(A_r\). A squarefree characteristic polynomial
has \(d\) distinct roots, and the minimal polynomial of \(A_r\) divides it.
Thus \(A_r\) is diagonalizable over \(K\). After a change of basis, write

\[
A_r=\operatorname{diag}(\lambda_1,\ldots,\lambda_d),
\]

where the \(\lambda_i\) are pairwise distinct. On a matrix unit \(E_{ij}\),
the scalar by which \(L_r\) acts is

\[
S_{ij}=\sum_{a=0}^{N-1}\lambda_i^a\lambda_j^{N-1-a}.
\]

If \(i=j\), then

\[
S_{ii}=N\lambda_i^{N-1}=0
\]

because \(r\mid N\) and the field has characteristic \(r\). This also covers
\(\lambda_i=0\). If \(i\ne j\), distinctness of the eigenvalues gives

\[
S_{ij}=\frac{\lambda_i^N-\lambda_j^N}{\lambda_i-\lambda_j}.
\]

Meanwhile,

\[
\operatorname{ad}_{A_r^N}(E_{ij})
=(\lambda_i^N-\lambda_j^N)E_{ij}.
\]

Hence the two extended operators have exactly the same zero matrix units:
all diagonal units, and precisely those off-diagonal units for which
\(\lambda_i^N=\lambda_j^N\). Therefore

\[
\ker (L_r\otimes_F K)
=\ker (\operatorname{ad}_{A_r^N}\otimes_F K).
\]

Both maps are defined over \(F\), so intersecting with \(M_d(F)\), or using
faithfulness of scalar extension, gives

\[
\ker L_r=\ker\operatorname{ad}_{A_r^N}
=\operatorname{Cent}(A_r^N).
\]

Their ranks over \(F\) consequently agree. If \(m_z\) counts the indices for
which \(\lambda_i^N=z\), the kernel over \(K\) is spanned by the \(E_{ij}\)
whose indices lie in the same fiber. Its dimension is \(\sum_zm_z^2\).
Scalar extension preserves rank, so

\[
\operatorname{rank}L_r=d^2-\sum_zm_z^2.
\]

A zero eigenvalue causes no extra case: squarefreeness makes it unique, and
its \(N\)-th power cannot equal that of a nonzero eigenvalue.

## Claim 2: uniform dimension cutoff

Let \(f=\operatorname{ord}_s(r)\). Suppose two distinct nonzero eigenvalues
\(\lambda,\mu\) satisfy \(\lambda^N=\mu^N\), and put
\(\zeta=\lambda/\mu\). Then \(\zeta^{rs}=1\). A field of characteristic
\(r\) has no nontrivial element of multiplicative order \(r\), so
\(\zeta^s=1\). Since \(s\) is prime and \(\zeta\ne1\), \(\zeta\) has order
exactly \(s\).

Let \(a\) and \(b\) be the degrees over \(F\) of \(\lambda\) and \(\mu\).
They are degrees of irreducible factors of the characteristic polynomial.
Inside \(\mathbb F_{r^{\ell}}\), with \(\ell=\operatorname{lcm}(a,b)\), one
has

\[
\lambda\in\mathbb F_{r^a}^{\times},\qquad
\mu\in\mathbb F_{r^b}^{\times}.
\]

The ambient multiplicative group is cyclic. Therefore the product of these
two subgroups has order

\[
\operatorname{lcm}(r^a-1,r^b-1).
\]

It contains \(\zeta=\lambda\mu^{-1}\). Since \(\zeta\) has prime order \(s\),
the prime \(s\) divides \(r^a-1\) or \(r^b-1\). Equivalently,

\[
f\mid a\quad\hbox{or}\quad f\mid b.
\]

Thus, if \(f\) divides none of the irreducible factor degrees, no two
distinct eigenvalues have the same \(N\)-th power. Claim 1 then has
\(m_z=1\) for every \(z\), and

\[
\operatorname{rank}L_r=d^2-d.
\]

Every irreducible factor degree is at most \(d\). Hence \(f>d\) implies the
factor-degree hypothesis without any condition on the size of \(r\).

## Claim 3: local sharpness

First suppose \(f=\operatorname{ord}_s(r)\ge2\). Choose a primitive
\(s\)-th root of unity \(\zeta\) in an algebraic closure of \(F\). Its
Frobenius orbit has length exactly \(f\), because

\[
\zeta^{r^k}=\zeta
\quad\Longleftrightarrow\quad
r^k\equiv1\pmod s.
\]

Let \(g\in F[x]\) be its minimal polynomial. Then \(g\) is irreducible and
squarefree of degree \(f\), and all of its roots have \(N\)-th power one.

Because \(f>1\), one has \(s\nmid r-1\). Since \(s\) is prime,
\(\gcd(s,r-1)=1\). The map

\[
F\longrightarrow F,\qquad a\longmapsto a^s
\]

is consequently a bijection. For every \(a\in F\), Frobenius gives
\(a^N=a^{rs}=a^s\). Choose \(d-f\) distinct elements
\(a_1,\ldots,a_{d-f}\) of \(F\setminus\{1\}\). There are enough because
\(d<r\). Their \(N\)-th powers are pairwise distinct and none is one. Also,
none is a root of \(g\), since the roots of \(g\) have degree \(f>1\).

The polynomial

\[
h(x)=g(x)\prod_{j=1}^{d-f}(x-a_j)
\]

is therefore monic, squarefree, and of degree \(d\). Its roots have one
\(N\)-th-power fiber of size \(f\), while all other fibers have size one.
For the companion matrix of \(h\), Claim 1 yields

\[
\operatorname{rank}L_r
=d^2-\bigl(f^2+(d-f)\bigr)
=d^2-d-f(f-1).
\]

Now suppose \(f=1\). Then \(s\mid r-1\), so \(F\) contains a primitive
\(s\)-th root \(\zeta\ne1\). Since \(2\le d<r\), choose \(d\) distinct
elements of \(F\) that include \(1\) and \(\zeta\), and let \(h\) be the
product of their linear factors. It is monic and squarefree of degree \(d\).
The roots \(1\) and \(\zeta\) have the same \(N\)-th power, namely one.
Thus at least one fiber has size at least two, and Claim 1 gives

\[
\operatorname{rank}L_r<d^2-d.
\]

Both constructions are local existence arguments and use no knowledge of a
factorization algorithm.

## Claim 4: explicit exceptional-prime bound

Let \(k=|E_1|\). For each \(q\in E_1\), set
\(m_q=\operatorname{ord}_q(p)\le D\). Then \(q\mid p^{m_q}-1\). Grouping
the distinct primes by \(m_q\) shows

\[
\prod_{q\in E_1}q
\;\bigm|\;
\prod_{m=1}^{D}(p^m-1).
\]

Every \(q\in(p,2p)\) is strictly larger than \(p\). Consequently

\[
p^k
<\prod_{q\in E_1}q
\le\prod_{m=1}^{D}(p^m-1)
<p^{\sum_{m=1}^{D}m}.
\]

It follows, without a prime-distribution estimate, that

\[
|E_1|<\frac{D(D+1)}2.
\]

For \(E_2\), the map \(q\mapsto q-p\) injects the primes in \((p,2p)\)
into \(\mathbb F_p^\times\), and it preserves the residue class whose order
is being measured. The cyclic group \(\mathbb F_p^\times\) has exactly
\(\varphi(m)\) elements of order \(m\) when \(m\mid p-1\), and none
otherwise. Hence

\[
|E_2|
\le\sum_{\substack{m\le D\\m\mid p-1}}\varphi(m)
\le\sum_{m=1}^{D}m
=\frac{D(D+1)}2.
\]

The union bound, with the strict first inequality, gives

\[
|E_1\cup E_2|<D(D+1).
\]

Now take \(q\notin E_1\cup E_2\) and \(d\le D\). Then

\[
\operatorname{ord}_q(p)>D\ge d,
\qquad
\operatorname{ord}_p(q)>D\ge d.
\]

Unit characteristic discriminant supplies squarefree characteristic
polynomials at both components. Apply Claim 2 first with \((r,s)=(p,q)\)
and then with \((r,s)=(q,p)\). The two local ranks are both \(d^2-d\).
The exceptional sets depend only on \(p\) and \(D\), so this conclusion is
simultaneous over all eligible dimensions and matrices, regardless of how a
matrix is selected.

For completeness, the directional derivative of the power map is exactly
the stated operator, since in the dual-number ring

\[
(A+tH)^{pq}=A^{pq}
+t\sum_{i=0}^{pq-1}A^iHA^{pq-1-i}\pmod {t^2}.
\]

## Claim 5: density interpretation

Write

\[
M(p)=\pi(2p)-\pi(p).
\]

Whenever \(M(p)>0\), Claim 4 immediately gives

\[
\frac{|E_1\cup E_2|}{M(p)}
<\frac{D(D+1)}{M(p)},
\]

which implies the stated non-strict upper bound. The PNT gives

\[
M(p)\sim\frac{p}{\log p},
\]

so, for \(D\ge1\), the exceptional fraction is

\[
O\!\left(\frac{D^2\log p}{p}\right).
\]

Fix \(C>0\) and an integer \(k\ge1\), and put

\[
D(p)=2^{C(\log_2(\log_2p+1))^k}
\]

or take its integer floor. Then

\[
\log D(p)=O((\log\log p)^k)=o(\log p),
\]

so \(D(p)=p^{o(1)}\). More explicitly,

\[
\log\!\left(\frac{D(p)^2\log p}{p}\right)
=2\log D(p)+\log\log p-\log p\longrightarrow-\infty.
\]

Thus the exceptional fraction tends to zero along prime \(p\).

There is one dependency-level detail in the exact finite-\(p\) wording.
Bertrand's postulate ensures \(M(p)>0\) for every odd prime \(p\), but it was
not named among the allowed dependencies. It is unnecessary for the density
conclusion: the PNT gives eventual positivity as well as the displayed
asymptotic. Thus Claim 5 is fully reconstructed asymptotically; its exact
all-\(p\) fraction statement is either read conditionally on \(M(p)>0\), or
uses Bertrand only to establish that the denominator is nonzero.

## Scope check

Every argument above concerns one derivative operator and its two component
ranks. None of the proofs extends the statement to combinations of operators,
selected entries or minors, intermediate computations, or a general factoring
lower bound.
