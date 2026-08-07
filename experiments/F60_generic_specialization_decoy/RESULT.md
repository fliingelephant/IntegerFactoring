# F60 — Unit-denominator generic dependencies are global-root decoys

**Status:** verifier-backed. The first version failed hostile audit because it
incorrectly claimed that every useful relation must be specialization-only.
This corrected version uses the exact unit-denominator subspace and passed a
fresh whole-proof audit plus proof-blind reconstruction.

**Verdict:** for an explicit family of completion relations, square
dependencies that already hold symbolically are not factor-bearing when their
symbolic root denominators are units modulo $N$. The normalized-root map
therefore factors through the quotient of the numeric square kernel by this
certified harmless subspace. A useful relation must lie outside that subspace.
It can be specialization-only, or it can be generic with a nonunit symbolic
denominator.

This is a source-filter theorem. It is not a source-success theorem and not a
factoring algorithm.

## Closest prior route and exact difference

The closest promoted result is P66. It computes the exact numeric square
kernel of any explicit polynomial-size integer list and proves that a basis is
complete for factor extraction. P64 explains global roots from exact endpoint
cycles in inverse-completion trajectories.

The result here adds a different layer. It compares the numeric kernel at the
given integer $N$ with the kernel of a fixed public symbolic lift. It proves
that the unit-denominator part of the latter kernel maps only to global signs.
Thus it separates certified generic decoys from the remaining relations. The
remainder can include both specialization-only dependencies and generic
dependencies with nonunit denominators. The theorem covers symbolic identities
whose retained numeric endpoint labels do not form cycles.

The algebra is elementary. No publication-level novelty is claimed without a
dedicated literature review.

## 1. Two square kernels

Let $N\ge3$ be odd. Let

\[
A_1(T),\ldots,A_m(T)\in\mathbb Q[T]
\]

be nonzero polynomials with

\[
A_i(0)=1,
\qquad
a_i:=A_i(N)\in\mathbb Z_{>0},
\qquad
a_i\equiv1\pmod N.
\tag{1}
\]

The inverse-completion case has

\[
A_i(T)=1+T K_i(T),
\qquad
A_i(N)=1+Nk_i=u_i v_i.
\]

Define the numeric kernel

\[
K_N=
\left\{
c\in\mathbb F_2^m:
\prod_i a_i^{c_i}\text{ is an integer square}
\right\}.
\tag{2}
\]

Define the generic kernel

\[
K_{\rm gen}=
\left\{
c\in\mathbb F_2^m:
\prod_i A_i(T)^{c_i}\text{ is a square in }\mathbb Q(T)
\right\}.
\tag{3}
\]

Both are binary vector spaces. For $c\in K_N$, let

\[
R_N(c)=\sqrt{\prod_i a_i^{c_i}}
\]

be the exact positive integer root.

## 2. Specialization containment

### Theorem 1

\[
\boxed{K_{\rm gen}\subseteq K_N.}
\tag{4}
\]

### Proof

Take $c\in K_{\rm gen}$ and put

\[
F_c(T)=\prod_i A_i(T)^{c_i}\in\mathbb Q[T].
\]

By definition, $F_c=S^2$ for some $S\in\mathbb Q(T)$. Write $S=P/Q$ with
coprime $P,Q\in\mathbb Q[T]$. Since $Q^2$ divides $P^2$ in the unique
factorization domain $\mathbb Q[T]$, $Q$ is constant. Hence one can take
$S\in\mathbb Q[T]$.

After evaluation at $N$,

\[
\prod_i a_i^{c_i}=S(N)^2.
\]

The left side is an integer. A rational number whose square is an integer is
an integer: if $S(N)=r/s$ in lowest terms, then $s^2\mid r^2$, so $s=1$.
Thus the product is an integer square and $c\in K_N$. $\square$

The containment can be strict. The quotient

\[
K_N/K_{\rm gen}
\tag{5}
\]

measures square relations that appear only after the public parameter is
specialized to the given integer $N$.

This quotient is relative to the selected lift rule. The same numeric value
can be generic under one valid lift and specialization-only under another. For
example, at $N=15$ the value $16$ is obtained from both

\[
(1+T/5)^2
\qquad\text{and}\qquad
1+T.
\]

The first lift is a symbolic square and the second is not. No claim below
treats $K_{\rm gen}$ as an invariant of the numeric list alone.

## 3. Unit-denominator generic roots are global

For $c\in K_{\rm gen}$, choose $S_c\in\mathbb Q[T]$ with
$S_c^2=F_c$. Its sign is irrelevant. Let $d_c$ be the least positive integer
such that

\[
d_c S_c(T)\in\mathbb Z[T].
\tag{6}
\]

The two choices $S_c$ and $-S_c$ have the same $d_c$.

### Theorem 2

If

\[
\gcd(d_c,N)=1,
\tag{7}
\]

then

\[
\boxed{R_N(c)\equiv1\text{ or }-1\pmod N.}
\tag{8}
\]

Thus $c$ cannot yield a factor through the congruence-of-squares gcd.

### Proof

Equation (1) gives $F_c(0)=1$, so

\[
S_c(0)=1\quad\text{or}\quad-1.
\tag{9}
\]

The integer polynomial $d_c(S_c(T)-S_c(0))$ has zero constant term.
Therefore

\[
d_c\bigl(S_c(N)-S_c(0)\bigr)\equiv0\pmod N.
\]

Theorem 1 shows that $S_c(N)$ is an integer. Since $d_c$ is a unit modulo
$N$, equation (7) gives

\[
S_c(N)\equiv S_c(0)\equiv\pm1\pmod N.
\]

The positive root $R_N(c)$ is either $S_c(N)$ or $-S_c(N)$. It is therefore
also $1$ or $-1$ modulo $N$. $\square$

If $1<\gcd(d_c,N)<N$, the denominator itself has already exposed a factor.
If $gcd(d_c,N)=N$, this theorem makes no claim. The unit condition must not
be omitted. For example, with $N=15$ and

\[
S(T)=1+T/5,
\qquad
A(T)=S(T)^2,
\]

one has $A(0)=1$, $A(15)=16\equiv1\pmod {15}$, but $S(15)=4$ is a
non-global square root. The denominator $5$ is exactly a hidden factor.

A generic relation can remain useful even when the denominator gcd is $N$
rather than a proper factor. Let

\[
S(T)=1-\frac45T+\frac1{15}T^2,
\qquad
A(T)=S(T)^2.
\tag{10}
\]

Then $S(0)=1$, $S(15)=4$, $A(0)=1$, and $A(15)=16$. The one-dimensional
numeric and generic kernels are equal, while the least root denominator is
$15$. Its gcd with $N$ is the whole modulus, yet the positive root $4$ gives
the factors $3$ and $5$. Thus $K_N/K_{\rm gen}$ can be zero while a useful
generic relation exists.

## 4. The unit-denominator set is a computable subspace

For a nonzero rational polynomial $P$, let $d(P)$ be the least positive
integer that clears all coefficient denominators. Because every $A_i(0)=1$,
put

\[
D_i=d(A_i).
\tag{11}
\]

### Theorem 3

For every $c\in K_{\rm gen}$,

\[
\boxed{d_c^2=\prod_i D_i^{c_i}.}
\tag{12}
\]

Consequently,

\[
U_N:=\{c\in K_{\rm gen}:\gcd(d_c,N)=1\}
=K_{\rm gen}\cap
\{c:c_i=0\text{ when }\gcd(D_i,N)>1\}.
\tag{13}
\]

In particular, $U_N$ is a binary subspace and is computable from a basis of
$K_{\rm gen}$ by binary linear algebra and ordinary gcds.

### Proof

Fix a rational prime $p$. For a rational polynomial $P$ with constant term
$1$ or $-1$, define

\[
\lambda_p(P)=-\min_j v_p([T^j]P)=v_p(d(P)).
\]

The minimum is at most zero because the constant coefficient is a $p$-adic
unit. The Gauss valuation is multiplicative:

\[
\lambda_p(PQ)=\lambda_p(P)+\lambda_p(Q).
\]

To see this, scale each polynomial so all coefficients are $p$-integral and
at least one coefficient is a unit. Their nonzero reductions multiply to a
nonzero polynomial in the domain $\mathbb F_p[T]$.

Apply this identity to
$S_c^2=\prod_iA_i^{c_i}$. It gives

\[
2v_p(d_c)=\sum_i c_i v_p(D_i)
\]

for every $p$, which proves (12). For a prime $p\mid N$, every term on the
right is nonnegative. It vanishes exactly when no selected $D_i$ is divisible
by $p$. Taking all primes dividing $N$ gives (13). The right side of (13) is
the intersection of two binary subspaces. $\square$

## 5. The factor-bearing map factors through a certified quotient

For $c\in K_N$, condition (1) gives $R_N(c)^2\equiv1\pmod N$. P66's overlap
identity proves that

\[
\rho_N(c)=R_N(c)\pmod N
\tag{14}
\]

is a homomorphism from $K_N$ to the square roots of $1$ modulo $N$. Quotient
the target by its global subgroup $\{1,-1\}$ and write the result as
$\bar\rho_N$.

### Theorem 4

\[
\boxed{U_N\subseteq\ker\bar\rho_N.}
\tag{15}
\]

Consequently, $\bar\rho_N$ factors through $K_N/U_N$. Every useful square
relation lies outside $U_N$, but it need not lie outside $K_{\rm gen}$.

If a binary basis of the complete numeric kernel $K_N$ consists entirely of
generic relations with unit root denominators, then

\[
K_N=K_{\rm gen}=U_N
\]

and every numeric square relation has a global root. No subset of that batch
can factor $N$ through this decoder.

### Proof

Theorem 2 puts every vector in $U_N$ inside $\ker\bar\rho_N$. A homomorphism
factors through any subspace of its kernel.

For the final statement, Theorem 1 gives
$K_{\rm gen}\subseteq K_N$. If a basis of $K_N$ lies in $K_{\rm gen}$, the
reverse containment holds. The unit-denominator premise puts that basis in
$U_N$. Since $U_N$ is a subspace, it contains all of $K_N$. Each basis image
under $\rho_N$ is also global by Theorem 2, so every linear combination has a
global image. $\square$

The certified quotient need not be the exact signal quotient. Define

\[
Z_N=\ker\bar\rho_N
=\{c\in K_N:R_N(c)\equiv\pm1\pmod N\}.
\tag{16}
\]

Then $U_N\subseteq Z_N$. The exact quotient that classifies distinct
non-global root images is $K_N/Z_N$. The computable quotient $K_N/U_N$ can
still contain nonzero global-decoy classes. Thus a nonzero certified quotient
is necessary for this decoder to succeed, but it is not sufficient.

If every $D_i$ is coprime to $N$, then $U_N=K_{\rm gen}$ and the certified
residual quotient is the specialization quotient $K_N/K_{\rm gen}$.
Without this extra condition, example (10) shows that even a useful generic
relation can lie outside $U_N$.

## 6. Algorithmic change and bit complexity

For explicit lifts of polynomial total degree and coefficient bit length, the
filter is:

1. use P66 to compute the numeric kernel $K_N$;
2. factor the $A_i$ over $\mathbb Q[T]$, normalize every nonconstant
   irreducible factor to be monic, and use its exponent parity to compute
   $K_{\rm gen}$;
3. compute each $D_i$ as the least common multiple of its coefficient
   denominators and compute $\gcd(D_i,N)$;
4. return any proper denominator gcd immediately, and otherwise compute $U_N$
   from (13);
5. extend a basis of $U_N$ to a basis of $K_N$ and run P66's exact-root gcd
   screens only on the added quotient representatives.

Deterministic rational-polynomial factorization is polynomial in degree and
coefficient bit length. The total factored degree is the sum of the input
degrees. Clearing denominators increases bit length by at most the sum of the
input denominator bit lengths. No factorization of rational unit contents is
needed. If every nonconstant factor parity of a selected product is even,
evaluation at $T=0$ and $A_i(0)=1$ force the remaining rational unit to be a
square. Conversely, a rational-function square has even valuation at every
nonconstant irreducible. The parity matrix therefore computes $K_{\rm gen}$
exactly. The parity matrix, the coordinate restrictions in (13), and the basis
extension have polynomial dimensions. Exact roots have at most half the total
bit length of the selected numeric product. Thus all five steps have
polynomial bit complexity in the explicit numeric list, the explicit lift
list, and $\log N$.

This is not another scalar followed by one gcd. It changes the decoder state:
the certified harmless subspace is removed before root tests. The remaining
quotient can contain specialization-only relations and generic relations with
nonunit denominators. The filter does not make this quotient nonzero and does
not make its root image non-global.

## 7. Exact finite certificate from F59-D03

F59-D03 applied this distinction to the 12 preregistered deterministic-offset
batches from F59-D02. Their numeric kernel dimensions sum to $19$.

- Twelve basis vectors are the direct $(N-1)^2$ relation.
- Seven basis relation values survive removal of every global square singleton
  and removal of the raw trajectory started at $N-1$. In the second variant,
  duplicate provenance from the $N-2$ trajectory supplies the same retained
  quotient values; the original raw occurrences do not survive.
- All 19 basis products lift to exact squares over $\mathbb Q[T]$.
- Every symbolic root has constant term $1$ or $-1$ and denominator coprime
  to its tested $N$.
- Therefore $K_N=K_{\rm gen}=U_N$ on all 12 batches, and every dependency in
  every tested batch is a global-root decoy.

These lifts are public but relative to the tested input and executed branch.
Their coefficients use the known modulus, inverse value, and trajectory
provenance. The statement “generic” means that $T$ remains indeterminate after
that lift rule is applied; it does not mean that one $N$-independent polynomial
family was fixed for all inputs.

The seven residual instances reduce to four symbolic root polynomials. Four
instances share

\[
\frac{(T-3)(T-5)(2T-1)}{15},
\]

whose constant term is $-1$. The other roots have degrees $3$, $6$, and $7$
and coefficient-denominator least common multiples $230$, $22533$, and
$5040$. Their constant terms are respectively $-1$, $1$, and $-1$.

The source checked each identity with exact rational-pair arithmetic and then
with Sage polynomial arithmetic as a second backend. Its authoritative source, log, and output
SHA-256 hashes are, respectively,

`5306268bf01ac569f2c75ca0be635dc1b8ed6bffc0065f6a307bbd6abf515d42`,
`7ca87cd0e1255ef7879450bdb50ed0a1b429f4dbefded71e8dcfb20c5d989ebe`,
and
`9c62739d882055f480b14b0d2d6b271cb894842c9a07b9d2965220d475d20f84`.

This is finite evidence about one sampler. It is not an asymptotic obstruction
for all offset batches and not evidence for factor correlation.

## 8. Remaining gap

The old target was “make a dependency.” The sharper target is:

> From bare $N$, produce in polynomial time a polynomial-size relation list
> whose quotient $K_N/U_N$ contains a vector with non-global root, with
> inverse-polynomial probability on every composite input.

A nonzero quotient $K_N/U_N$ is necessary but not sufficient. It can contain a
specialization-only relation or a generic relation with nonunit denominator,
and either type can still have root $1$ or $-1$. A proper denominator gcd is
already a factor. Otherwise the non-global root-image condition remains the
factor-bearing event.
