# F284 — Compact q-binomial jets and their missing factor guarantee

**Family:** route:F02
**Status:** the central short-jet and uniform-index claims are promoted as P234
after independent reconstruction. Other observations remain exploratory.
No new factoring theorem or literature-level novelty claim is made.

## Question and difference from prior work

Can specialized Gaussian-binomial information be evaluated without the large
coefficient state in P21/F14, while retaining useful CRT asymmetry? `PRIOR.md`
locates the exact earlier scopes. Here the output is a short Taylor jet at a
fixed specialization, rather than the whole shifted product polynomial.

## A compact evaluator that actually works

Write G_(m,k)(t) for the Gaussian binomial polynomial and define

    R_(m,k)(z) = G_(m,k)(exp(z)) / binom(m,k).

This is a formal series over Q, with constant term 1. Let S_r(M)=sum_(i=1)^M i^r.
The product formula, expanded in Q[[z]], gives

    [z] log R = k(m-k)/2,
    [z^r] log R = B_r/(r r!) * (S_r(m)-S_r(k)-S_r(m-k))  (even r>=2),
    [z^r] log R = 0  (odd r>=3).

Here B_r are Bernoulli numbers with B_2=1/6. This follows by summing
log((exp(i z)-1)/(i z)); its linear coefficient is i/2 and its even
coefficient is B_r i^r/(r r!). Faulhaber's formula evaluates each S_r using
a number of rational operations polynomial in r, independent of M.
If l_i=[z^i]log R, exponentiation uses

    c_0=1,  c_j=(1/j) sum_(i=1)^j i l_i c_(j-i).

Thus the first J coefficients can be computed with bit cost polynomial in
J+log(m+1), without computing binom(m,k) or materializing G. Rational
coefficient sizes are polynomially bounded in those parameters.

For the central case m=2B,k=B, c_j is a polynomial in B of degree 2j,
with leading coefficient 1/(2^j j!). Its denominator primes are at most j+1:
this follows from the Bernoulli denominators, Faulhaber denominators, and the
series-exponentiation recurrence. Reduction modulo N is therefore valid when
all its prime factors exceed J+1; it does not divide by binom(2B,B) modulo N.

## Computation

SageMath 10.9, authoritative D05, verified 372 power-sum cases, 496 complete
order-12 jets against literal Gaussian polynomials, and 5,952 q-Lucas
specializations modulo cyclotomic polynomials. With B=2^512+12345, it computed
13 central coefficients without the enormous polynomial or central binomial.
The largest numerator was 12,273 bits and largest denominator 27 bits.
Local wrapper time was 2.111 seconds. This was local computation on a large
index, not a remote server run. Sources, outputs, and hashes are in
`RUN_MANIFEST.md`; failed setup/metadata runs remain in `FAILED_RUNS.md`.

S01 independently generated and factored central coefficient polynomials
c_1,...,c_12 and moment Hankel determinants H_1,...,H_5. In particular,

    c_1 = B^2/2,
    c_2 = B^2(3B^2+2B+1)/24,
    c_3 = B^4(B+1)^2/48,
    H_2 = B^2(2B+1)/12,
    H_3 = B^5(B-1)(5B+3)(2B+1)^2/2160.

Here mu_j=j!c_j and H_r=det(mu_(i+j))_(0<=i,j<r). A vanishing leading
principal determinant alone is not a proof that the full moment sequence has
small rank. All exact factorizations are retained in `output/S01.txt`.

## What survives for factoring

On the unresolved balanced branch N=pq, p<B=floor(sqrt(N))<q<2p, the ordinary
central binomial has gcd q with N. Indeed B=p+s with 2s<p, so its p-adic
valuation is zero; B<q<2B gives q-adic valuation one. Higher powers of these
primes do not enter the factorial ranges. This is already the P231 interval
content interface, not a new factorer.

The short normalized jet removes that guaranteed scalar. In particular c_0=1.
For p,q>3 on this branch, c_1,c_3,H_2 are units modulo N: none of B,B+1,2B+1
is divisible by either hidden prime. Other coefficients can still split:
at N=391 and B=19, gcd(c_2 mod N,N)=17; at N=247 and B=15, H_3 reveals 13
through its factor 5B+3. The latter factor is a small linear relation in B,
not evidence that moment rank supplies a new general success law.

There is a precise sparse-source bound for uniform random indices, distinct
from the fixed B=floor(sqrt(N)) choice. If p,q>J+1 and b is uniform modulo N,
the degree/root bound gives

    Pr[any c_j(b), 1<=j<=J, has a proper gcd with N]
      <= J(J+1)(1/p+1/q).

This only covers these coefficient probes and this sampler. It does not rule
out selected indices, other projections, adaptive combinations, or a different
factor-preserving normalization. A general all-input useful-source theorem
remains missing.

## Literature and next question

The cumulant viewpoint is established literature, so no novelty claim is made
for the log-jet identity. The primary abstract and author page for Billey and
Swanson's *Cyclotomic generating functions* (arXiv:2305.07620v3, 2024) identify
cumulants and provide a companion Sage notebook:
https://arxiv.org/abs/2305.07620v3
https://sites.math.washington.edu/~billey/papers/CGFs/

The August 2026 preprint *Mod-phi convergence for random variables with
cyclotomic generating functions* by Thale and Tuchel is a relevant follow-up:
https://arxiv.org/abs/2608.14143
Only its abstract has been inspected; no theorem from it is used here.
Exact quantitative formula matching still requires full-text comparison.

The next mathematical question is how to preserve a factor-asymmetric scalar
or extract different information while keeping this compact representation.
More unstructured gcd tests of low-order moments do not resolve that gap.
