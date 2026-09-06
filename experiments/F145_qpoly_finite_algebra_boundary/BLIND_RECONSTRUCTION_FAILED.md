# F145 statement-only blind reconstruction

## Isolation and verdict

Source read: `STATEMENT.md` only.

Source SHA-256:

```text
c00dfc7f43a2ec5fc5b39841a140f744a046f2e31f580d7c430e23963eb8e6bd
```

**Verdict: FAIL AS WRITTEN, with one scope defect.**

All displayed claims (1)--(20) reconstruct. The finite-algebra, Frobenius,
monomial, and Hasse arguments are sound. The failure is the unqualified prose
conclusion after (8): the assumptions stated there do not imply an
exponentially small rank-mismatch probability. That conclusion also needs

\[
M d^2=2^{o(n)},
\tag{A}
\]

and in particular it holds when both (M) and (d) are quasipolynomial in
(n). The final runtime claim has this intended meaning, and exact-scope item
7 points in the same direction. The condition is still absent from Part II's
formal inference. A concrete counterexample appears below.

## I. Uniform nonunits

Reduction modulo the Jacobson radical preserves units. The quotient map is
uniform on every fiber. Under

\[
A/J\simeq\prod_i \mathbb F_{r^{e_i}},
\]

an element is a unit exactly when every field coordinate is nonzero. Thus

\[
\Pr(a\text{ is not a unit})
=1-\prod_i(1-r^{-e_i}).
\]

The union bound gives the first inequality in (2). Also

\[
r^{-e_i}\le \frac{e_i}{r},
\qquad
\sum_i e_i=\dim(A/J)\le d.
\]

This proves the rest of (2). It also proves the nilpotent claim: changing the
radical while keeping the semisimple quotient does not change the nonunit
probability.

For a finite free (R)-algebra, CRT gives

\[
\mathcal A\simeq \mathcal A_p\times\mathcal A_q
\]

as finite sets and algebras. A uniform element therefore has independent
uniform reductions. Multiplication by (a_r) is singular exactly when (a_r)
is a nonunit. A proper gcd of (det(m_a)) with (N) occurs exactly when one,
but not both, reductions are nonunits. Hence its probability is

\[
\alpha_p(1-\alpha_q)+(1-\alpha_p)\alpha_q
=\alpha_p+\alpha_q-2\alpha_p\alpha_q.
\]

This proves (3). Conditional uniformity gives the same bound after every
adaptive transcript. A conditional union bound proves (4). If (M) and (d)
are quasipolynomial and the least factor is (2^{\Omega(n)}), then the right
side is (2^{-\Omega(n)}).

## II. Etale monogenicity and Krylov rank

Write

\[
A\simeq\prod_e (\mathbb F_{r^e})^{m_e},
\qquad
\sum_e e m_e=d<r.
\]

For each fixed (e), choose (m_e) pairwise distinct monic irreducible
polynomials of degree (e), and choose one root in each corresponding field
factor. There are enough choices. For (e=1), there are (r>d\) choices. For
(e\ge2), the number (I_r(e)) of degree-(e) irreducibles satisfies

\[
eI_r(e)
\ge r^e-\sum_{j=1}^{\lfloor e/2\rfloor}r^j
\ge r,
\]

while (m_e\le d/e<r/e). The minimal polynomials of the chosen coordinates
are pairwise coprime. The polynomial CRT then shows that the tuple (b) of
chosen roots generates (A). This proves (5).

Give (a) (d) scalar coordinates. The determinant of (K(a)) is a
polynomial in those coordinates of total degree at most

\[
0+1+\cdots +(d-1)=\frac{d(d-1)}2.
\]

It is not the zero polynomial because it is nonzero at a generator (b).
Schwartz--Zippel gives the stronger estimate

\[
\Pr(\operatorname{rank}K(a)<d)
\le \min\left(1,\frac{d(d-1)}{2r}\right),
\]

so (7) follows. If the two CRT ranks differ, at least one Krylov matrix is not
full rank. A union bound proves (8). Different factor-degree partitions do
not enter this argument.

### Counterexample to the prose conclusion after (8)

Take balanced primes (p<q), and let

\[
d=\lfloor\sqrt p\rfloor,
\qquad
\mathcal A_p=\mathbb F_p^d,
\qquad
\mathcal A_q=\mathbb F_{q^d}.
\]

Both reductions are etale, have dimension (d<\min(p,q)), and arise from a
finite free (R\)-algebra: use the CRT product

\[
\mathcal A=\mathcal A_p\times\mathcal A_q
\]

with the coordinatewise (R\simeq\mathbb F_p\times\mathbb F_q) action.

For (a_p\in\mathbb F_p^d), the Krylov rank is (d) exactly when its (d)
coordinates are pairwise distinct. Therefore

\[
\Pr(\operatorname{rank}K(a_p)=d)
=\frac{(p)_d}{p^d}\longrightarrow e^{-1/2}.
\]

For (a_q\in\mathbb F_{q^d}), failure of full rank means that (a_q) lies in
a proper subfield. Thus

\[
\Pr(\operatorname{rank}K(a_q)<d)
\le d q^{-d/2}=o(1).
\]

The two samples are independent. Their ranks mismatch with probability at
least (1-e^{-1/2}-o(1)). This is not (2^{-\Omega(n)}), even for one probe.
It does not contradict (8), whose right side is then of constant order.

Condition (A) repairs the inference. In the intended explicit
quasipolynomial-runtime model, (M,d=2^{(\log n)^{O(1)}}), so (A) holds on
balanced semiprimes.

## III. Genuine local Frobenius

Every squarefree reduction splits as a product of finite fields. On a factor
(mathbb F_{r^e}), the normal basis theorem gives a basis cyclically permuted
by absolute Frobenius. Its characteristic polynomial is (T^e-1). Taking
products proves (9).

Factor over (mathbb Z[T]):

\[
H_\lambda(T)=\prod_{m\ge1}\Phi_m(T)^{b_m},
\qquad
b_m=\#\{e\in\lambda:m\mid e\}.
\]

Unique factorization recovers every (b_m). Descending Möbius inversion
recovers the number of parts equal to each (e). Thus
(lambda\mapsto H_\lambda) is injective.

Let (C(T)in R[T]) be the division-free characteristic polynomial of the
given glued matrix. Its reductions are (H_{\lambda_p}) and
(H_{\lambda_q}). Every coefficient of (H_\lambda) has absolute value at
most (2^{s}\le2^d). Hence the difference between corresponding coefficients
of two such polynomials has absolute value at most (2^{d+1}).

Enumerate all partitions (mu) of (d). For every coefficient (j), compute

\[
\gcd(C_j-(H_\mu)_j,N).
\]

When (mu=\lambda_p), all differences vanish modulo (p). Injectivity gives
one coefficient that differs from (H_{\lambda_q}) over the integers. The
size bound and (q>2^{d+1}) show that this difference is nonzero modulo (q).
That gcd is (p). The symmetric argument can return (q). This reconstructs
the extraction claim.

There are \(\exp(O(\sqrt d))\) partitions. Division-free characteristic
polynomial computation is polynomial in the matrix size and coefficient bit
length. If (d=(\log n)^{O(1)}), the whole procedure has
(2^{(\log n)^{O(1)}}) bit complexity.

Conversely, known factors let us compute

\[
y_p=X^p\bmod(f,p),
\qquad
y_q=X^q\bmod(f,q).
\]

For (g\in A_r), (F_r(g)=g(y_r)). CRT-gluing the coordinates of the basis
images gives the matrix of (F). Thus the genuine glued map and a factor
certificate are interreducible on the stated mismatch promise. The public
map (x\mapsto x^N) has no reason to equal this CRT-glued map.

## IV. Monomial maps

Put (Q=r^e). The nonzero elements of (K) form a cyclic group of order
(Q-1). The equation (x^E=x) has the root zero and exactly
(gcd(E-1,Q-1)) nonzero roots. This proves (11), (12), and the density
inequality.

Choose (t\in\{1,\ldots,Q-1\}) with (t\equiv E\pmod{Q-1}). Then (x^E) and
(x^t) are the same function, including at zero. Because (r) is prime in
the standing setup, every additive map on (K) is (mathbb F_r)-linear. It
has a unique linearized representative

\[
L(X)=\sum_{j=0}^{e-1}c_jX^{r^j}.
\]

If (X^t) is additive, (X^t-L(X)) has (Q) roots and degree below (Q).
It is therefore the zero polynomial. This forces (t=r^j) and (c_j=1) for
one (j). The converse follows from Frobenius additivity. This proves (13).
The cyclic group also gives (14).

Modulo (p-1), (p^k\equiv1), so

\[
N^k\equiv q^k\pmod{p-1}.
\]

This proves (15). When (q) is a unit modulo (p-1), the definition of
multiplicative order proves (16). If (e\mid k), then
(p^k\equiv1\pmod{p^e-1}), and the same calculation proves (17). These are
exact congruence criteria. They do not imply an order-hitting theorem for an
adaptive exponent menu.

## V. Hasse coefficients

For (1\le k<p), the identity

\[
k!\binom Nk=N(N-1)\cdots(N-k+1)
\]

can be reduced modulo (p) and modulo (q). The denominator (k!) is a unit
in both fields, while the numerator contains the factor (N). Hence both
primes divide (inom Nk), which proves (19).

At (k=p), the numerator has exactly one factor divisible by (p), namely
(N), and (p!) also has exactly one. Thus (p\nmid\binom Np). The numerator
has one factor divisible by (q), while (q\nmid p!), so
(q\mid\binom Np). Since (N) is squarefree, (20) follows.

If the least factor is (2^{\Omega(n)}), every numerical truncation order

\[
K(n)=2^{(\log n)^{O(1)}}
\]

is below (p) for all sufficiently large (n). Every positive-order
coefficient through (K(n)) is then zero modulo both CRT factors. The first
selective coefficient is at the unknown index (p). This reasoning says
nothing about sparse large indices or compressed interval evaluation.

## Scope audit

The proof mechanisms inspect only these exceptional events:

- a uniform sample is a nonunit in exactly one CRT component;
- a fresh uniform Krylov sample is rank-deficient in a component;
- a supplied genuine Frobenius has different characteristic polynomials;
- a monomial exponent satisfies an exact field-order congruence; or
- a numerically low Hasse coefficient is selective.

They do not control factor-correlated sources, reuse of one sample through
adaptive polynomials, joint decoding of ordinary nonzero values, succinct
nonmonomial maps, adaptive order-hitting menus, compressed high-index Hasse
evaluation, exponential-rank algebras, or intermediate elimination data.
Thus the eight exclusions in the exact-scope section are accurate.

The final quasipolynomial boundary is also accurate when “quasipolynomial”
applies to both the number of probes and the explicit algebra rank. The
frozen Part II text must state that rank condition for the reconstruction to
receive an unqualified pass.

## Independent computational checks

SageMath checks found no collision among (H_\lambda) for (d\le12), matched
the additivity criterion on sampled fields up to order (49), and matched
(19)--(20) on several small semiprimes. These checks are supplementary. The
arguments above do not depend on them.
