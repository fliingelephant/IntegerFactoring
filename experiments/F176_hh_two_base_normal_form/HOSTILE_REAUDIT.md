# F176 V3 hostile re-audit

## Frozen inputs

- STATEMENT.md: c7c4c9963c078dc1ba4d68a86a81fa4cd9e46626ab6fa9d8645779b92d6b4b1f
- PROOF.md: 6100a81be386458c9e875ed5dc042ee9906ed3691c57fcd2950f27485be4316a
- SELF_AUDIT.md: 8c40f7d97410db1b06733e71bba30dd131332f8577a49e415018551f45ae7534
- MANIFEST.md: 198805cf6df897c08d081c4d7646b8880849996e0c428a15d5f34bd221ad543d

## Verdict

**PASS.** I found no false assertion, missing branch, prime-power defect, or
super-QP operation. The theorem proves only its stated trichotomy. It does
not prove QP factoring because Outcome C remains open.

## Hostile checks

### Fixed caps and \(\Lambda_B\)

For every fixed numerical choice
\[
n\le B<N-1,\qquad C\ge n,\qquad
B,C=2^{(\log n)^{O(1)}},
\]
a sieve through the numerical value \(B\) is QP. The loose bound
\(\log_2\Lambda_B\le\log_2(B!)=O(B\log B)\) makes construction,
storage, modular exponentiation, and all divisor-stripping calls QP.
Products of these QP costs remain QP. Fixed QP cap formulas are eventually
smaller than \(N-1\); the stated fixed finite threshold covers the remaining
inputs.

The identity
\[
r\mid\Lambda_B\iff \sigma(r)\le B
\]
is exact. Hence \(A=1\) proves
\(\sigma(\operatorname{ord}_{R_j}(2))>B\) separately in every hidden
prime-power component.

### The \(A=N\) branch

When \(A=N\), every local order divides the known factored multiple
\(\Lambda_B\). Factor-first stripping either finds a mixed CRT or partial
prime-power gcd, or leaves the same prime-adic valuation in every local
order. Thus it returns one exact common order \(m\).

The range \(n<m\le B\) is correctly Outcome B. Outcome B requires only
\(m>n\), not \(m>B\). If \(\gcd(m,N)>1\), it is a proper factor because
\(m\le\varphi(R_j)<N\). Otherwise the order is coprime to \(N\), as Outcome
B requires.

### The small common return

For odd \(N\), \(N>2^{n-1}\). Therefore
\[
N\mid2^m-1,\quad m\le n
\]
forces \(m=n\) and \(N=2^n-1\). Composite \(n\) gives the proper divisor
\(2^{n/\ell}-1\). Prime \(n\) is odd under the composite-input promise.
The commuting elements \(2\) and \(-1\) then have coprime orders \(n\) and
2, so \(-2\) has exact local order \(2n\). Also
\(N\equiv1\pmod n\), which proves \(\gcd(2n,N)=1\).

### Relative first return

For every odd prime power, the squaring kernel is exactly
\(\{1,-1\}\). Thus
\[
R_j\mid2^{2e}-1\iff e_j\mid e.
\]
Before a first global return, any local return would make \(G_e\)
nontrivial and hence either expose a proper factor or be an earlier global
return. Therefore a no-factor first global return forces every \(e_j=e\).
If all scanned gcds are one, every \(e_j>C\).

At a global return, \(2e\) is a known annihilating multiple. Stripping
returns a factor or a common exact ordinary order \(m\). Local cyclicity
gives
\[
e=\frac{m}{\gcd(m,2)},\qquad
\operatorname{lcm}(2,m)=2e.
\]
Taking \(h=2\) for even \(m\), and \(h=-2\) for odd \(m\), gives exact
common order \(L=2e\). The absolute certificate gives \(m>B\), so
\(L\ge m>B\ge n\). The stripping gcd screen gives
\(\gcd(m,N)=1\), and oddness of \(N\) gives \(\gcd(L,N)=1\).

### Outcome C and recursion

On the final branch, both certificates hold componentwise:
\[
\sigma(\operatorname{ord}_{R_j}(2))>B,\qquad e_j>C.
\]
Since quotient order does not exceed absolute order, the latter also gives
\(\operatorname{ord}_{R_j}(2)>C\).

The relative loop has \(C\) iterations. Trial division through
\(\sqrt C\), factoring \(2e\), and all state encodings are QP. A complete
binary factor tree has fewer than \(2n\) nodes because its prime leaves,
with multiplicity, number at most \(\lfloor\log_2N\rfloor\). Therefore
factor recursion, including repeated prime factors, adds only a polynomial
factor.

## Scope

The quantifier is over each fixed pre-registered QP choice of \(B,C\).
It is not one cap with an input-dependent unbounded QP exponent. No step
rules out Outcome C or localizes unequal hidden orders of \(2\).
