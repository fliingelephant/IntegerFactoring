# Proof of the F158 certified quadratic-tower win–win

## 1. Explicit-subgroup trichotomy

Let `H_r` denote the image of `H` in `F_r^*`, for `r=p,q`.

If a gcd in (3) is proper, the first branch is immediate. If a gcd is `N`,
then `x=h` modulo `N`, so `x` belongs to `H`.

Assume every gcd is one. If the image `x_r` belonged to `H_r`, the
definition of an image would give some `h\in H` with `x=h modulo r`. Then
`r` would divide `gcd(x-h,N)`, a contradiction. Hence `x_r` is outside
`H_r` for both hidden primes.

Because `x^2\in H`, the coset of `x_r` in
`<H_r,x_r>/H_r` has order at most two. It is nontrivial, so it has order
exactly two. This proves (4). The identical quotient argument modulo `N`
proves the global index two.

Applying the argument successively proves (6) by induction. The total size
of all explicitly listed groups through level `t` is a geometric series
bounded by `2|H_t|`, so a polylogarithmic number of doublings preserves a
quasipolynomial cost. A linear number of doublings can make the list
exponential, which is why the compact theorem is separate.

For the displayed `N=77` specialization, `9` has order `3` modulo `7` and
order `5` modulo `11`, hence order `15` modulo `77`. Direct reduction gives
`26^2=60=9^(-1) modulo 77`. Also `9^2=81`, so

\[
\gcd(26-81,77)=11.
\]

This is exactly the proper-gcd branch of Theorem 1.

## 2. Exact local-order certificate

Let `d_r=ord_r(g)`. Equation (7) gives `d_r|M`.

If `d_r<M`, then the prime-power factorization of `M` contains a rational
prime `ell` whose exponent in `d_r` is smaller than its exponent in `M`.
Thus

\[
d_r\mid M/\ell.
\]

It follows that `r` divides `g^(M/ell)-1`, contradicting (8). Therefore
`d_p=d_q=M`, which proves (9).

For the universal initial pair, `(-1)^2=1` and `-1` has exact order two in
every odd prime field. Equivalently, (7) holds for `M=2`, while (8) is

\[
\gcd((-1)^{2/2}-1,N)=\gcd(-2,N)=1.
\]

Hence `(-1,2)` is always certified after the ordinary parity preprocessing.

## 3. Internal roots and mixed roots

Assume (10). Since `gcd(a,M)=1`, the element `g^a` has exact order `M` in
both hidden fields.

Inside the cyclic group `<g_r>` of order `M`, an element `g_r^k` squares
to `g_r^a` exactly when

\[
2k=a\pmod M.
\]

This congruence has `gcd(2,M)` solutions when it is soluble and none
otherwise. Hence there are at most two public internal-root candidates
`g^k` modulo `N`.

If `x` matches one candidate in exactly one hidden field, the corresponding
gcd in (12) is proper. If it matches one candidate in both fields, that gcd
is `N` and `x` is globally in `<g>`.

Suppose the congruence is insoluble, or every comparison gcd is one. Then
`x` cannot lie in `<g_r>` for either hidden prime. But `x^2` lies in that
subgroup. The explicit-subgroup quotient argument therefore doubles each
local subgroup.

Let `e_r=ord_r(x)`. The order of `x^2` is

\[
\frac{e_r}{\gcd(e_r,2)}=M.
\]

If `e_r` were odd, this would give `e_r=M`, placing `x` in the unique
subgroup of order `M`, namely `<g_r>`, a contradiction. Therefore `e_r` is
even and `e_r=2M`. This proves (13).

The exact local order `2M` implies all certificate equations for `(x,2M)`.
Its factorization is obtained from the supplied factorization of `M` by
incrementing the exponent of two. The next state is therefore public and
compact.

## 4. Tower capacity

Induction on (13) gives

\[
ord_p(g_t)=ord_q(g_t)=M_t=2^tM_0.
\]

Every element order divides the multiplicative-group order, so

\[
M_t\mid p-1
\quad\text{and}\quad
M_t\mid q-1.
\]

Because `p<q` and `N=pq`, one has `p<sqrt(N)`. Hence

\[
M_t\le p-1<\sqrt N.
\]

This contradicts (17). Each level uses at most two gcds, a bounded number of
modular exponentiations, and arithmetic on `O(n)`-bit exponents. The first
`t` with (17) is at most `ceil(log2(sqrt(N)/M_0))`, which is `O(n)`. Thus the
decoder and capacity argument are polynomial if the stated source supplies
one usable lift at every level.

## 5. Section-completion specialization

F154 gives

\[
s_v=\iota_N(z_v),
\qquad
z_v^2=Q(v)\pmod N.
\]

Inverting the second congruence gives

\[
s_v^2=Q(v)^{-1}\pmod N.
\]

Since `Q(v)` is a product of the generators `q_j`, its inverse lies in
`H=<q_1,...,q_m>`. This proves (18), so Theorem 1 applies whenever `H` is
explicitly enumerable.

If `H=<g>` has the certified common order and the provenance supplies
`Q(v)^(-1)=g^a` with `gcd(a,M)=1`, Theorem 3 applies verbatim. No part of
F154 guarantees this cyclic presentation, coprimality, or a non-inert lift.
The final source claim is therefore sufficient for factoring but remains
unproved.
