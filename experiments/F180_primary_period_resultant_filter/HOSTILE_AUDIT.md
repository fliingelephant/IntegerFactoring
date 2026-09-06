# F180 hostile audit

## Frozen inputs

- `STATEMENT.md`:
  `9ae4beb80683a7b7e61c82a91891e2e1f849ac96d498f3570519bfbebb9b1f29`
- `PROOF.md`:
  `ef703570255ba10a68e034ba1d0434648f1411b2ef61f8a2bd3f0287a4117dd4`
- `SELF_AUDIT.md`:
  `c45905be68c99d1070cbfc3c6ddd46a5f2b53dbc7e3377cbf66c8b3f3b6efb1c`

All three hashes matched before review.

## Verdict

**PASS.** I found no false implication, prime-power defect, missing branch,
or super-QP operation. The result proves only its stated factor/common-order/
primary-period-hard trichotomy. It does not close the final hard branch or
prove QP integer factoring.

## Hostile checks

### Imported P160 interface

The proof uses exactly the promoted P160 guarantees. The public value (y)
is a unit, and its order (f_j) modulo each hidden prime-power component
(R_j) satisfies

\[
1<f_j<N<2^n,
\qquad
\gcd(f_j,N)=1,
\qquad
\sigma(f_j)>T\ge n.
\]

No equality of the hidden local orders is assumed. No hidden factor, local
order, or factorization of an evaluated value is used by the filter.

### Exact primary-power deletion

Fix (ell^a\parallel f_j). Since

\[
2^a\le \ell^a\le f_j<2^n,
\]

one has (a<n). For every integer exponent (e), the local order of
(y^e) has (ell)-adic valuation

\[
a-\min\{a,v_\ell(e)\}.
\]

If (ell\mid A_\delta), then
(v_\ell(A_\delta^n)\ge n>a), so the full (ell^a) part disappears.
If (ell\nmid A_\delta), the full part survives. Thus no partially
retained primary power is omitted from equation (7).

If (ell\mid N+\delta), every factor
((N+\delta)^k-1) is (-1\pmod\ell), so (ell\nmid A_\delta). Otherwise
(N+\delta) is a unit modulo (ell), and a factor vanishes modulo
(ell) exactly when

\[
\operatorname{ord}_\ell(N+\delta)\le K.
\]

This proves the claimed exact filter, including the nonunit alternative.

### Gcd behavior for arbitrary hidden prime powers

Let (R_j=p^b). Every filtered local order divides (f_j), hence is
coprime to (p). The kernel of

\[
(\mathbb Z/p^b\mathbb Z)^\times
\longrightarrow
(\mathbb Z/p\mathbb Z)^\times
\]

is a (p)-group. Therefore a filtered power is one modulo (p) if and
only if it is one modulo (p^b). Each (H_\delta) consequently contains
either the whole hidden component (R_j) or none of it. A value strictly
between one and (N) is a valid factor, and the endpoint values have the
componentwise meanings used in the proof.

In particular, (H_0=1) leaves a nontrivial primary part in every
component. The P160 relation (gcd(f_j,N)=1) excludes
(ell\mid N), so every prime in each surviving order has
(operatorname{ord}_\ell(N)>K). If (H_0=N), every prime supporting
every original (f_j) instead has (N)-action period at most (K).

### Double extinction and resultant support

Assume (H_0=H_3=N). Then, component by component,

\[
f_j\mid A_0^n,
\qquad
f_j\mid A_3^n.
\]

For each (ell^a\parallel f_j), primality of (ell) gives factors with
indices (k,l\le K) such that

\[
N^k-1\equiv0\pmod\ell,
\qquad
(N+3)^l-1\equiv0\pmod\ell.
\]

Thus the two defining polynomials for (R_{k,l}) have the common root
(N\pmod\ell). Reduction of the integer Sylvester determinant modulo
(ell), equivalently the integral resultant Bezout identity, proves
(ell\mid R_{k,l}).

No resultant vanishes over the integers. A common complex root (u) would
satisfy (|u|=|u+3|=1), but the reverse triangle inequality gives
(|u+3|\ge2). The root-product formula also gives

\[
R_{k,l}
=\prod_{u^k=1}|(u+3)^l-1|
<2^{k(2l+1)}.
\]

Hence the product of all (K^2) resultants contains at least one copy of
every prime supporting every (f_j). Raising that product to the (n)-th
power supplies at least (n>a) copies. This proves (f_j\mid M) for all
hidden components. Different primes and components may use different
pairs ((k,l)); taking the full pairwise product covers all of them.

### Factor-first exact-order recovery

The trial divisions give a complete public factorization of (M). Start
with the known common annihilator (M), and for a prime (ell) in its
factorization test

\[
\gcd(y^{M/\ell}-1,N).
\]

A global value permits one deletion. A proper value factors (N). A value
one means that every local order needs the current full (ell)-adic
exponent; otherwise the gcd would contain at least one full hidden
prime-power component. Therefore, on a no-factor run, the terminal exponent
has the same prime-adic valuation as every (f_j) at every prime. It is
their common exact order (m), with its inherited factorization. Since
(sigma(f_j)>T), this common value satisfies (m=f_j>T\ge n).

### Bit complexity

Each factor in (A_\delta) has (O(nK)) bits in the loose worst case, and
summing over (k\le K) gives

\[
\log A_\delta=O(nK^2),
\qquad
\log(A_\delta^n)=O(n^2K^2).
\]

There are (K^2) resultants, each of (O(K^2)) bits. Their expanded input
polynomials have degree (O(K)) and coefficient bit length (O(K)), so
exact Sylvester determinants take polynomial time in (K). Trial division
of all resultants costs (2^{O(K^2)}).

For completeness, the product before the outer power has (O(K^4)) bits,
and (M) has (O(nK^4)) bits. There are at most (O(nK^4))
factor-first deletion tests, each using an exponent of that bit length.
This remaining work is polynomial in (n) and (K). With
(K=\lceil(\log_2(n+1))^c\rceil) for fixed (c\ge1), all work is bounded
by

\[
2^{O(K^2)}=2^{(\log n)^{O(1)}}.
\]

### Scope boundary

The (H_0=1) and (H_3=1) descendants need not preserve the original
large-primary condition (sigma(f_j)>T): a short-action large primary part
can be deleted while a smaller long-action part survives. F180 does not
claim otherwise. What it does preserve in every hidden component is one
nontrivial primary part with the stated long-action or nonunit property.
The final limitation in the frozen statement is therefore accurate.

## Computation

No computational evidence is used in this verdict. An optional bounded
symbolic check was not run because SymPy is not installed; no replacement
package was installed or substituted. The proof checks above are exact.
