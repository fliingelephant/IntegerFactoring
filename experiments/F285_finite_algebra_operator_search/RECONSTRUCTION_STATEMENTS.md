# F285 — Standalone general-d statement bundle

These are candidate statements for fresh blind reconstruction. This file
contains no proposed proof. No theorem here concerns general factoring or
arbitrary finite-algebra algorithms.

## Definitions and allowed dependencies

Let r,s be distinct primes, N=rs, and A a d-by-d matrix over Z/N. Write A_r
for its reduction over F_r. Define the F_r-linear operator

\[
L_r(H)=\sum_{i=0}^{N-1}A_r^i H A_r^{N-1-i}.
\]

For a matrix B, Cent(B)={H:HB=BH} and ad_B(H)=BH-HB. The multiplicative
order ord_s(r) is the least positive k such that r^k=1 modulo s. A matrix
has squarefree characteristic polynomial if that polynomial has no repeated
root in an algebraic closure. Unit characteristic discriminant over Z/N
means squarefree characteristic polynomials at both prime components.

Allowed standard dependencies: finite-field structure, cyclicity of finite
multiplicative subgroups of fields, irreducible polynomials and Frobenius
orbits, elementary linear algebra, and the polynomial root bound over a field.
The prime number theorem is allowed only for the final density corollary;
the finite exceptional-partner count must not use prime distribution.

## Claim 1 — Exact kernel and rank

If A_r has squarefree characteristic polynomial, then

\[
\ker L_r=\operatorname{Cent}(A_r^N),\qquad
\operatorname{rank}L_r=\operatorname{rank}(\operatorname{ad}_{A_r^N}).
\]

If lambda_1,...,lambda_d are the distinct eigenvalues of A_r in a splitting
field and m_z is the number with lambda_i^N=z, then

\[
\operatorname{rank}L_r=d^2-\sum_z m_z^2.
\]

## Claim 2 — Uniform dimension cutoff

If A_r has squarefree characteristic polynomial and ord_s(r)>d, then
rank(L_r)=d^2-d. No size condition r>d is required.

More generally, the same conclusion holds if ord_s(r) divides none of the
irreducible factor degrees of the characteristic polynomial of A_r.

## Claim 3 — Local sharpness

Let f=ord_s(r)>=2. If f<=d<r, there exists a squarefree monic polynomial
of degree d over F_r whose companion matrix A_r has

\[
\operatorname{rank}L_r=d^2-d-f(f-1).
\]

If f=1 and 2<=d<r, there exists such a squarefree companion matrix with
rank(L_r)<d^2-d. These are existence claims at a named prime, not assertions
that the matrices can be constructed without the factors of N.

## Claim 4 — Explicit exceptional-prime bound

Fix an odd prime p and an integer D>=1. Among prime numbers q in (p,2p),
let E_1 consist of those with ord_q(p)<=D, and E_2 of those with
ord_p(q)<=D. Then

\[
|E_1|<D(D+1)/2,\qquad
|E_2|\le\sum_{\substack{m\le D\\m\mid p-1}}\varphi(m)
\le D(D+1)/2,
\]

and |E_1 union E_2|<D(D+1).

For any q outside this union and every matrix A over Z/(pq), of any
dimension d<=D with unit characteristic discriminant, the local ranks of
D(A^(pq)) are both d^2-d. This is simultaneous over all such matrices and
dimensions, including matrices chosen adaptively.

## Claim 5 — Density interpretation

The fraction of prime q in (p,2p) in E_1 union E_2 is at most
D(D+1)/(pi(2p)-pi(p)). By the prime number theorem this is
O(D^2 log p/p). Consequently the fraction tends to zero along primes p for
every fixed bound D(p)=2^{C(log_2(log_2 p+1))^k}, with fixed C>0, k>=1
(or its integer floor).

## Scope and requested audit

These claims concern each individual operator's two local ranks. They do not
include ranks of sums, products, concatenations, projections, selected minors,
or arbitrary combinations of operators. They do not bound factor extraction
from individual entries or intermediate operations. Non-squarefree matrices
are excluded. No all-input factoring lower bound is claimed.

Please reconstruct or refute these claims independently, including zero
eigenvalues, splitting-field degrees, exact quantifiers, exceptional counts,
and the density dependency. An inability to reconstruct is inconclusive.
