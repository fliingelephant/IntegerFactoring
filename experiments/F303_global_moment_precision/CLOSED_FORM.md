# Closed global formulas modulo M^2

**Outcome:** the root's simplification is correct. The M^2 evaluator needs
only universal unit power sums and one unit product. It does not need a
truncated R(z) or a logarithm. R(z) remains useful for the higher-precision
correction structure in REPORT.md.

**Scope/status:** M=2^k, k>=3, odd N, nonnegative integer exponents;
root-derived formulas, checked algebra and sparse exact controls. No
external novelty claim or Archimedean approximation is made. No material
was sent to the blind reconstruction worker.

Use the canonical residues v_u=N/u mod M and the notation

    A_j=sum_{u odd<M}u^j,
    Pi_M=product_{u odd<M}u, phi=phi(M)=M/2,
    q_u=(u*v_u-N)/M.

For j<0, A_j is a2-adic rational power sum with odd denominators. These are
the U_j and P_M of the earlier report. N may first be reduced modulo M.

## Off-diagonal formula and the exact division precision

For a>b>=0, j=a-b,

    S_ab = (a*N^b*A_j-b*N^a*A_(-j))/j mod M^2.          (1)

Compute the numerator modulo2^(2k+v_2(j)). Divide its residue by2^v_2(j)
exactly, then multiply by the inverse of the odd part of j modulo M^2.
Using only2k bits before division is insufficient. For a<b, use the exact
symmetry S_ab=S_ba. When b=0 the answer is simply A_a; (1) agrees with it.

## Direct proof, including the guard-bit valuation

The inverse map is an involution of the canonical unit set, and

    u^(-j)=N^(-j)*v_u^j*(1+M*q_u/N)^(-j).

For every integer h>=1, the weighted carry moment

    Q_(j,h)=sum_u u^j*q_u^h

is even. Indeed u pairs with M-u, v pairs with M-v, and
q_(M-u)=q_u+M-u-v_u has the same parity as q_u. Both unit weights are odd.
The u/v involution also gives sum_u v_u^j*q_u^h=Q_(j,h).

Consequently binomial expansion yields

    N^j*A_(-j)=A_j-(j*M/N)*Q_(j,1)
      +sum_{h>=2}(-1)^h*binom(j+h-1,h)*(M/N)^h*Q_(j,h).

The identity
h*binom(j+h-1,h)=j*binom(j+h-1,h-1) gives

    v_2(binom(j+h-1,h))>=v_2(j)-v_2(h).

Every h>=2 term therefore has valuation at least

    h*k+v_2(j)-v_2(h)+1 >= 2k+v_2(j).

The extra1 is supplied by the even carry moment. This proves the stronger
congruence

    A_j-N^j*A_(-j)=(j*M/N)*Q_(j,1) mod2^(2k+v_2(j)).   (2)

Also, expanding u^a*v_u^b=u^j*(N+M*q_u)^b gives

    S_ab=N^b*A_j+b*M*N^(b-1)*Q_(j,1) mod M^2.

Multiplying by j and using(2) proves (1), since a=j+b. This proof needs
neither the truncated ratio nor its logarithm, and justifies the full
precision retained before division.

## Diagonal formula

For a=b=t>=0,

    S_tt=(phi-t)*N^t+t*Pi_M^2*N^(t-phi) mod M^2.        (3)

Negative exponents of N are modular inverses of a known odd unit. To prove
the formula, use the exact permutation product

    Pi_M^2=product_u(N+M*q_u)
      =N^phi+M*N^(phi-1)*Q_(0,1) mod M^2.

On the other hand,
S_tt=phi*N^t+t*M*N^(t-1)*Q_(0,1) mod M^2. Substitution gives(3).
The case t=0 gives phi directly, including when t-phi is negative.

## Actual evaluator and costs

For a requested degree bank, compute the universal A_j,A_(-j) and Pi_M
using UNIT_PRODUCTS.md, at2k+max_j v_2(j) bits as needed. Then apply(1)
or(3). These procedures are polynomial in k and the degree bound. The
exponents and divisions do not require enumerating the unit group.

The modulo-M^3 correction and master weighted-carry series from REPORT.md
are unchanged. In particular this simplification does not compute the
missing quadratic-carry bank or high Archimedean digits.

## Sparse controls

`closed_form_controls.py` checked12 cases with M=8,...,128. They include
t=0, diagonal t>phi, negative modular exponents, b=0, and off-diagonal
j=2,4,8,16. It also checks(2) at the required guarded precision.

Two concrete guard-loss examples are:

| M,N,a,b | Correct residue modulo M^2 | Result after dropping guard bits |
|---|---:|---:|
|16,3,4,2|232|104|
|32,5,17,1|720|16|

The small direct products and inverse sums are verification data only.
The polynomial universal constructor was not replaced or broadly retested.
The integer-only run took0.0002seconds and used16.1MiB, under a20-second
alarm and a64MiB estimate. Preflight reported load1.88/1.95/1.99,68%
available memory and no swap. Source, JSON and log are retained; no shared
records or commit were changed.
