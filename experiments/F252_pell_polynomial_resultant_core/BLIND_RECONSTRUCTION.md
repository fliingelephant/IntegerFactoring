# Blind reconstruction of F252

## Authentication and scope

- Read source: `STATEMENT.md` only.
- Expected SHA-256: `cf49a2ea6ef9158f7ed60e79385b5aad5f28bd7583e9404216eadadf30457cf7`.
- Observed SHA-256: `cf49a2ea6ef9158f7ed60e79385b5aad5f28bd7583e9404216eadadf30457cf7`.
- Snapshot authentication: **PASS**.

No other F252 artifact, ledger, or history was read.

## Independent reconstruction

Let

\[
S_i^2-D_iT_i^2=1,\qquad
f_i(X)=1+D_i(T_i-k_iX)^2,\qquad
a_i=f_i(N),
\]

with (D_i,S_i>0), (T_i,k_i\ge 0), and (N\ge3) odd. If
(y_i=T_i-k_iN), then

\[
a_i=1+D_i y_i^2\equiv 1+D_iT_i^2=S_i^2\pmod N.
\]

Hence 

\[
\gcd(a_i,N)=1\iff\gcd(S_i,N)=1.
\]

On this clean branch the supplied root is (x_i=S_i\bmod N). The two
kernels are exactly

\[
K_{\rm gen}=\left\{c\in\mathbb F_2^m:
\prod_i f_i(X)^{c_i}\in\mathbb Q(X)^{\times2}\right\},
\]

and

\[
K_N=\left\{c\in\mathbb F_2^m:
\prod_i a_i^{c_i}\in\mathbb Z^2\right\}.
\]

### 1. Content and irreducibility

For (k_i=0), the polynomial is the constant square

\[
f_i(X)=1+D_iT_i^2=S_i^2.
\]

For (k_i\ne0), expand

\[
f_i(X)=D_i k_i^2X^2-2D_iT_i k_iX+S_i^2.
\]

The Pell equation gives
(\gcd(S_i,D_i)=\gcd(S_i,T_i)=1). Therefore

\[
\operatorname{cont}(f_i)
=\gcd(D_i k_i^2,2D_iT_i k_i,S_i^2)
=\gcd(S_i^2,k_i^2,2k_i).
\]

The unscaled discriminant is

\[
(-2D_iT_i k_i)^2-4D_i k_i^2S_i^2=-4D_i k_i^2.
\]

After division by (q_i=\operatorname{cont}(f_i)), it is

\[
-\frac{4D_i k_i^2}{q_i^2}<0.
\]

Thus the primitive quadratic is irreducible over (\mathbb Q). This uses no
squarefree condition on (D_i).

### 2. Resultant and duplicates

For

\[
f=1+D(T-kX)^2,\qquad g=1+E(U-\ell X)^2,
\qquad \Delta=T\ell-Uk,
\]

direct elimination of (X) gives

\[
\operatorname{Res}_X(f,g)
=\left(DE\Delta^2+E\ell^2+Dk^2\right)^2
-4DEk^2\ell^2.
\]

If (D=E), difference of squares gives

\[
\operatorname{Res}_X(f,g)
=D^2\left(D\Delta^2+(k-\ell)^2\right)
       \left(D\Delta^2+(k+\ell)^2\right).
\]

Write (r=DE\Delta^2), (p=Dk^2), and (q=E\ell^2). Then

\[
\operatorname{Res}_X(f,g)
=(r+p+q)^2-4pq
=r^2+2r(p+q)+(p-q)^2.
\]

All three terms are nonnegative. Since (D,E>0), the resultant is zero
exactly when

\[
\Delta=0\quad\text{and}\quad Dk^2=E\ell^2.
\]

These conditions make the quadratic, linear, and constant coefficients
equal, so they are equivalent to (f=g) in (\mathbb Z[X]). Conversely,
polynomial equality gives both conditions. Because each post-wrap primitive
part is irreducible, two post-wrap rows are associates over (\mathbb Q)
exactly when the integer polynomials are equal.

If (D,E) are squarefree and (k,\ell>0), then
(Dk^2=E\ell^2) forces (D=E) and (k=\ell); then 
(\Delta=0) forces (T=U). Without squarefree normalization, the displayed
two-condition test is the exact scaled-duplicate criterion.

### 3. Generic kernel and normalized roots

Let (I_0=\{i:k_i=0\}), and partition the other indices by exact equality
of (f_i). Distinct classes have nonassociate irreducible primitive parts.
Unique factorization in (\mathbb Q[X]) therefore gives

\[
c\in K_{\rm gen}
\iff
\sum_{i\in C}c_i=0\pmod2
\quad\text{for every post-wrap class }C.
\]

The constant rows impose no condition because they are already squares.
Deleting them and retaining one member of each equality class leaves

\[
K_{\rm gen}=0.
\]

The square root is integral, not merely rational. For each class (C), let
(f_C) be its common polynomial and let
(r_C=\sum_{i\in C}c_i), which is even. Then one can take

\[
H_c(X)=
\prod_{\substack{i\in I_0\\c_i=1}}S_i
\prod_C f_C(X)^{r_C/2}\in\mathbb Z[X].
\]

Rows in one class have the same positive (S_i), because their constant
terms are equal. Consequently

\[
H_c(X)^2=\prod_i f_i(X)^{c_i},
\qquad
H_c(0)=\prod_i S_i^{c_i}.
\]

For the positive integer root
(R_c=\sqrt{\prod_i a_i^{c_i}}), evaluation at (N) gives

\[
R_c=|H_c(N)|
\equiv\pm H_c(0)
\equiv\pm\prod_i x_i^{c_i}\pmod N.
\]

Thus every generic dependency has a global normalized root. On the clean
branch, one of the two standard square-root gcds is (N) and the other is
(1), since (N) is odd and the supplied root product is a unit. Such a
dependency cannot split (N).

### 4. Resultant-supported numerical core

After the generic cleanup, let (J) contain one representative of each
post-wrap equality class. All pairwise resultants on (J) are nonzero. Set

\[
\mathcal R_i=\prod_{\substack{j\in J\\j\ne i}}
|\operatorname{Res}_X(f_i,f_j)|,
\quad
e_i=\left\lceil\log_2(a_i+1)\right\rceil,
\quad
g_i=\gcd(a_i,\mathcal R_i^{e_i}),
\quad
b_i=a_i/g_i.
\]

If a prime (p) divides both (a_i=f_i(N)) and (a_j=f_j(N)), then the
two reductions have the common root (N\bmod p). Hence

\[
p\mid\operatorname{Res}_X(f_i,f_j)\mid\mathcal R_i.
\]

Also (v_p(a_i)\le\log_2 a_i<e_i). Therefore
(\mathcal R_i^{e_i}) contains the full (p)-power occurring in (a_i).
It follows that

\[
\gcd(b_i,a_j)=1\quad(i\ne j),
\]

and, in fact, every prime in (b_i) is absent from both (g_i) and all
other rows. The exact consequences are:

1. If (b_i) is nonsquare, an odd valuation in (b_i) is a private parity
   pivot, so every (c\in K_N) has (c_i=0).
2. If (b_i) is square, removing it does not change the parity column:
   (a_i) and (g_i) have the same prime-parity vector.
3. Every prime in (g_i) divides (\mathcal R_i). Thus, after forced-zero
   rows are deleted and square (b_i)'s are discarded, the complete
   remaining parity problem is supported on explicit pairwise resultants.

This is localization only. It does not show that the remaining kernel is
zero. Specialization can create new square relations. In particular, a
singleton can specialize to a square even though it has no generic relation;
its supplied-root comparison still needs the standard gcd screen.

### 5. Complexity and exact boundary

The construction needs coefficient gcds, the closed resultant formula,
integer products and powers, gcds, exact division, square tests, and binary
linear algebra. A gcd-free coprime refinement can expose the required parity
columns without prime factorization.

If (L) is the total input bit length, then (m\le L). Each coefficient,
(a_i), and pairwise resultant has (O(\operatorname{poly}(L))) bits. The
bit length of each product (\mathcal R_i), and their total bit length, is
also polynomial in (L). Since (e_i=O(L)), the powers
(\mathcal R_i^{e_i}) remain polynomial-size. Standard exact-integer and
binary-linear-algebra algorithms therefore give deterministic
(\operatorname{poly}(L)) bit complexity without factoring.

An explicitly materialized quasipolynomial bank with quasipolynomial-size
coordinates still has quasipolynomial total work. This says nothing about a
bank whose implicit description expands to a larger explicit list.

The argument itself establishes exactly these new structural points:

1. generic-kernel elimination after constant-square and exact-duplicate
   cleanup;
2. the closed resultant and exact duplicate test; and
3. factor-free localization of specialization-only parity interactions.

It does **not** establish a private-prime theorem for all inputs, a
probability bound, a law for non-global roots, emptiness of the localized
core, or a factoring algorithm. The comparative descriptions of P68 and
F250 are not needed for, and were not used in, this reconstruction.

## Verdict

**PASS.** Every displayed algebraic identity and every internal implication
in the authenticated statement follows from the stated hypotheses. The
scope limitations are necessary and are stated correctly.
