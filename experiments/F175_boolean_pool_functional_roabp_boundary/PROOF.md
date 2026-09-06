# F175 proof

## 1. Expansion across one variable

By symmetry it is enough to use the cut `X_1 | (X_2,...,X_K)`. Write

\[
 x=X_1,\qquad Y=(Y_1,\ldots,Y_{K-1})=(X_2,\ldots,X_K),
\]

and for `S subseteq [K-1]` put

\[
 L_S(Y)=\sum_{i\in S}Y_i.
\]

There are `d=2^{K-1}` such forms, including `L_emptyset=0`. Separating the
factors that contain `X_1` from those that do not gives the polynomial
identity

\[
 Q_K(x,Y)
 =Q_{K-1}(Y)\prod_{S\subseteq[K-1]}(x+L_S(Y)). \tag{1.1}
\]

Let `e_t` be the elementary symmetric polynomial of degree `t` in the
multiset of the `d` forms `L_S`. Since one form is zero,

\[
 Q_K(x,Y)
 =Q_{K-1}(Y)\sum_{t=0}^{d-1}e_t(Y)x^{d-t}. \tag{1.2}
\]

## 2. Every displayed coefficient is nonzero in characteristic greater
than `d`

Order the variables by

\[
 Y_1>Y_2>\cdots>Y_{K-1}
\]

and use the induced lexicographic monomial order. Group the nonzero forms
`L_S` by the least index in `S`. The group with least index `i` has size

\[
 c_i=2^{K-1-i},
\]

and every form in that group has leading monomial `Y_i`, with coefficient
one.

Fix `0<=t<=d-1`. To obtain the leading monomial of `e_t`, first select as
many forms as possible from the group of size `c_1`, then from the group of
size `c_2`, and continue. All fully used groups contribute coefficient one.
There is at most one partially used group. If that group has size `c_i` and
`u` of its forms are selected, its contribution is

\[
 \binom{c_i}{u}.
\]

No other selection or choice of a lower term has the same leading monomial:
it would first decrease the exponent of the earliest variable at which the
greedy choice is not followed. Hence the leading coefficient of `e_t` is
exactly `1` or one binomial coefficient `binom(c_i,u)`.

Every prime divisor of `binom(c_i,u)` is at most `c_i<d`. Therefore, if `r`
is prime and `r>d`, this leading coefficient is nonzero in `F_r`. Thus

\[
 e_t\ne0\quad\hbox{in }\mathbb F_r[Y]
 \qquad(0\le t\le d-1). \tag{2.1}
\]

The polynomial `Q_{K-1}` is a product of nonzero linear forms in the
integral domain `F_r[Y]`, so it is nonzero. It follows that every coefficient

\[
 C_t(Y)=Q_{K-1}(Y)e_t(Y) \tag{2.2}

\]

in (1.2) is nonzero. Moreover, `C_t` is homogeneous of degree

\[
 (d-1)+t.
\]

These degrees are distinct. Therefore `C_0,...,C_{d-1}` are linearly
independent over `F_r`.

## 3. Polynomial rank and function rank coincide here

The individual degree of `Q_K` in every variable is `d`: exactly half of
the nonempty subset factors contain a fixed variable. Since `d<r`, `Q_K` is
already the unique canonical polynomial of individual degree less than `r`
that represents its function on `F_r^K`.

Coefficient extraction in `x` cannot increase any other individual degree,
so

\[
 \deg_{Y_i}C_t\le d<r
 \qquad(1\le i<K). \tag{3.1}
\]

In (1.2), the `d` functions

\[
 x,x^2,\ldots,x^d
\]

are linearly independent on `F_r`, because `d<r`. The coefficient functions
`C_0,...,C_{d-1}` are also linearly independent on `F_r^{K-1}`. Indeed, a
linear combination of them has individual degree less than `r`; if it were
the zero function, uniqueness of canonical finite-field representatives
would make it the zero polynomial, contrary to Section 2.

Thus (1.2) is a rank-`d` factorization of the function matrix `mathcal M_1`,
and both factor matrices have rank `d`. Hence

\[
 \operatorname{rank}_{\mathbb F_r}\mathcal M_1=d. \tag{3.2}
\]

The same argument applies to every singleton cut by symmetry.

## 4. Functional ROABP consequence

Consider a functional ROABP in the variable order `pi`. Cut its matrix
product immediately after its first variable `x=X_{pi(1)}`. If that layer
has output width `w`, the computed function has a decomposition

\[
 f(x,Y)=\sum_{h=1}^{w} f_h(x)g_h(Y), \tag{4.1}

\]

where `f_h` and `g_h` are functions on the indicated finite sets. Therefore
the matrix of `f` across this cut has rank at most `w`. The entries in the
ROABP layers can be arbitrary functions; no degree, circuit-size, or
uniformity assumption is used.

If `f=Q_K` pointwise on `F_r^K`, Section 3 gives rank `d`, so

\[
 w\ge d=2^{K-1}. \tag{4.2}

\]

This proves the functional statement directly. Equivalently, one may replace
each arbitrary univariate layer function by its unique interpolating
polynomial of degree at most `r-1`. Because each variable appears in only one
layer, the product remains canonical in every variable. This explains why
nonuniform dependence on `r`, `N`, or public parameters and the use of
high-exponent univariate maps do not evade this particular model boundary.

## 5. Named model inclusions

A one-pass linear-state recurrence is a product of variable-dependent state
transition matrices, so (4.2) is its state-width lower bound. A tensor train
is the same matrix-product representation. In a tree tensor network where a
variable occurs only at its designated leaf, cutting the sole bond incident
to that leaf writes the output as a sum of at most the bond dimension many
functions separated across that singleton cut. The bond dimension is
therefore at least `d`. An exact separated character sum is also a
decomposition of the form (4.1).

A determinant of a small numeric matrix is not one of these inclusions in
general. Its expansion can have exponential functional ROABP width even when
Gaussian elimination evaluates it quickly. The theorem therefore does not
exclude a new Moore-style or other determinant identity.

## 6. P34 specialization and QP comparison

In P34,

\[
 K=\left\lfloor\log_2\lfloor\sqrt N\rfloor\right\rfloor-3,
 \qquad T=2^K,
\]

and `N=pq` with `p<q<2p`. Since

\[
 T\le\frac{\lfloor\sqrt N\rfloor}{8}
 <\frac{\sqrt2}{8}p<p,
\]

both hidden characteristics exceed `T`, hence exceed `d=T/2`. Also
`T>floor(sqrt(N))/16`, so `d=2^{Theta(n)}` for input bit length
`n=ceil(log_2(N+1))`.

For fixed `C>0` and fixed `k>=1`,

\[
 2^{C(\log_2(n+1))^k}=2^{o(n)}.
\]

Thus no QP-width evaluator in any of the named exact one-pass or separated
models computes the P34 product on every local input.
