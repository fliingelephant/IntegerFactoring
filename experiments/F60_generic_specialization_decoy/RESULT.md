# F60 — Generic dependencies are global-root decoys

**Status:** candidate. This version has not yet passed hostile audit or
proof-blind reconstruction.

**Verdict:** for an explicit family of completion relations, square
dependencies that already hold symbolically are not factor-bearing when their
symbolic root denominators are units modulo $N$. The normalized-root map
therefore factors through the quotient of the numeric square kernel by this
generic kernel. A useful sampler must create a specialization-only dependency,
not only a dependency.

This is a source-filter theorem. It is not a source-success theorem and not a
factoring algorithm.

## Closest prior route and exact difference

The closest promoted result is P66. It computes the exact numeric square
kernel of any explicit polynomial-size integer list and proves that a basis is
complete for factor extraction. P64 explains global roots from exact endpoint
cycles in inverse-completion trajectories.

The result here adds a different layer. It compares the numeric kernel at the
given integer $N$ with the kernel of a public symbolic lift before $N$ is
substituted. It proves that the latter kernel maps only to global signs under a
checkable denominator condition. Thus it separates generic algebraic
dependencies from specialization-only dependencies. It covers symbolic
identities whose retained numeric endpoint labels do not form cycles.

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
\]

one has $S(0)=1$ but $S(15)=4$, a non-global square root of $1$ modulo $15$.
The denominator $5$ is exactly a hidden factor.

## 4. The factor-bearing map lives on a quotient

For $c\in K_N$, condition (1) gives $R_N(c)^2\equiv1\pmod N$. P66's overlap
identity proves that

\[
\rho_N(c)=R_N(c)\pmod N
\tag{10}
\]

is a homomorphism from $K_N$ to the square roots of $1$ modulo $N$. Quotient
the target by its global subgroup $\{1,-1\}$ and write the result as
$\bar\rho_N$.

Let

\[
U_N=
\{c\in K_{\rm gen}:\gcd(d_c,N)=1\}.
\tag{11}
\]

Define $G_N=\operatorname{span}_{\mathbb F_2}(U_N)$. This definition does not
assume that the displayed denominator condition is itself closed under binary
addition.

### Theorem 3

\[
\boxed{G_N\subseteq\ker\bar\rho_N.}
\tag{12}
\]

Consequently, $\bar\rho_N$ factors through $K_N/G_N$. Every useful square
relation lies outside the generic unit-denominator subspace.

If a binary basis of the complete numeric kernel $K_N$ consists entirely of
generic relations with unit root denominators, then

\[
K_N=K_{\rm gen}
\]

and every numeric square relation has a global root. No subset of that batch
can factor $N$ through this decoder.

### Proof

Theorem 2 puts every generator in $U_N$ inside
$\ker\bar\rho_N$. A kernel is a subspace, so it also contains their span
$G_N$. A homomorphism factors through any subspace of its kernel.

For the final statement, Theorem 1 gives
$K_{\rm gen}\subseteq K_N$. If a basis of $K_N$ lies in $K_{\rm gen}$, the
reverse containment holds. Each basis image under $\rho_N$ is global by
Theorem 2. Since $\rho_N$ is a homomorphism, every linear combination of the
basis also has a global image. $\square$

## 5. Algorithmic change

P66 computes $K_N$. The new filter is:

1. attach a public symbolic lift $A_i(T)$ to each sampled relation;
2. identify the generic square subspace and check its root denominators;
3. remove that certified global-decoy subspace from the numeric kernel; and
4. test a basis of the remaining specialization quotient.

When the symbolic lifts have polynomial total representation size and their
square classes can be computed in polynomial bit complexity, this filter is
also polynomial. It is not another scalar followed by one gcd. It changes the
state passed from the source to the decoder: the decoder now retains only
dependencies created by specialization.

This filter does not make the quotient nonzero. A factoring theorem still
needs a sampler with an all-input inverse-polynomial law that makes
$\bar\rho_N$ nonzero on that quotient.

## 6. Exact finite certificate from F59-D03

F59-D03 applied this distinction to the 12 preregistered deterministic-offset
batches from F59-D02. Their numeric kernel dimensions sum to $19$.

- Twelve basis vectors are the direct $(N-1)^2$ relation.
- Seven basis vectors survive removal of every global square singleton and
  removal of the raw trajectory started at $N-1$.
- All 19 basis products lift to exact squares over $\mathbb Q[T]$.
- Every symbolic root has constant term $1$ or $-1$ and denominator coprime
  to its tested $N$.
- Therefore the generic and numeric kernels are equal on all 12 batches, and
  every dependency in every tested batch is a global-root decoy.

The seven residual instances reduce to four symbolic root polynomials. Four
instances share

\[
\frac{(T-3)(T-5)(2T-1)}{15},
\]

whose constant term is $-1$. The other roots have degrees $3$, $6$, and $7$
and coefficient-denominator least common multiples $230$, $22533$, and
$5040$. Their constant terms are respectively $-1$, $1$, and $-1$.

Sage independently checked each of the 19 polynomial square identities. The
run used exact rational arithmetic. Its authoritative source, log, and output
SHA-256 hashes are, respectively,

`5306268bf01ac569f2c75ca0be635dc1b8ed6bffc0065f6a307bbd6abf515d42`,
`7ca87cd0e1255ef7879450bdb50ed0a1b429f4dbefded71e8dcfb20c5d989ebe`,
and
`9c62739d882055f480b14b0d2d6b271cb894842c9a07b9d2965220d475d20f84`.

This is finite evidence about one sampler. It is not an asymptotic obstruction
for all offset batches and not evidence for factor correlation.

## 7. Remaining gap

The old target was “make a dependency.” The sharper target is:

> From bare $N$, produce in polynomial time a polynomial-size relation list
> whose specialization quotient contains a vector with non-global root, with
> inverse-polynomial probability on every composite input.

A dimension gap $K_N/K_{\rm gen}\ne0$ is necessary but not sufficient. A
specialization-only relation can still have root $1$ or $-1$. The root-image
condition remains the factor-bearing event.
