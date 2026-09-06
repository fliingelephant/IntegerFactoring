# F176 V2 blind reconstruction

## Audit protocol

I read only `STATEMENT.md`. I did not read a proof, audit, manifest, V1 file,
or prior reconstruction.

Frozen statement SHA256:

```text
c7634a4c9a72552ce7d822857abe381623c343e8920dc3a859277913b260aac1
```

## Verdict

**PASS.** The stated factor/common-order/hard-base-two trichotomy is correct
for arbitrary odd composites, including repeated prime factors. Its uniform
deterministic cost is quasipolynomial. The result does not eliminate the hard
base-two outcome and therefore is not a factoring theorem.

## Independent reconstruction

### 1. Factor-first stripping

Let (x^B=1\pmod N), with the factorization of (B) known. Repeatedly try
each prime divisor (q\mid B) by computing

\[
\gcd(x^{B/q}-1,N).
\]

A proper gcd factors (N). A gcd equal to (N) permits the replacement
(B\leftarrow B/q). If stripping finishes without a factor, every failed
(q)-division has gcd one. Hence no hidden local order divides (B/q).
Every local order divides (B), so its (q)-adic valuation equals that of
the final (B), for every (q\mid B). Thus all local orders equal the final
(B).

This also proves the required coprimality with (N). Suppose a hidden
component is (p^a) and (p\mid B=\operatorname{ord}_{p^a}(x)). Then
(a\ge2), and the standard order-lifting law for odd prime powers gives

\[
\operatorname{ord}_{p^{a-1}}(x)\mid B/p.
\]

At the decisive rejected \(p\)-strip, let the current multiple be \(E\).
Then \(E/B\) is prime to \(p\), so \(E/p\) is a multiple of the local order
modulo \(p^{a-1}\), but not of \(B\). Hence \(x^{E/p}-1\) is divisible by
\(p^{a-1}\) but not by \(p^a\). Its gcd with \(N\) is therefore nontrivial
and proper. This contradicts a no-factor stripping run. Consequently
\(\gcd(B,N)=1\). Since \(N\) is odd, the same holds for \(2B\).

### 2. The absolute base-two screen

For a positive integer (t),

\[
t\mid\Lambda_n
\quad\Longleftrightarrow\quad
\text{every primary divisor }\ell^v\parallel t\text{ is at most }n.
\]

If (A=1), no local order of (2) divides (Lambda_n). Therefore every
local order has a primary divisor larger than (n), which proves (9).

If (A=N), all local orders divide the known factored multiple
(Lambda_n). The stripping argument above either factors (N), or returns
one factored exact common local order (m), coprime to (N).

### 3. A small common return cannot stall

If the common order satisfies (m\le n), then

\[
N\mid 2^m-1.
\]

For odd (N), the definition of (n) gives (N>2^{n-1}). Thus (m<n)
is impossible. Hence (m=n). A proper divisor of (2^n-1) is at most
((2^n-1)/2<2^{n-1}), so necessarily (N=2^n-1).

If (n) is composite, (2^{n/\ell}-1) is a nontrivial proper divisor for
any prime (ell\mid n). If (n) is prime, the composite-input promise
excludes (n=2), so (n) is odd. The orders of (2) and (-1) are then
the coprime values (n) and (2). Thus (-2) has exact order (2n>n)
in every hidden component. Therefore every common base-two return gives a
factor or a larger exact common-order state.

### 4. The relative scan

An odd prime power has only the square roots (1) and (-1). Therefore

\[
R_j\mid 2^{2e}-1
\quad\Longleftrightarrow\quad
e_j\mid e.
\]

If a first global return occurs at (e), then each (e_j\mid e). If some
(e_j<e), the earlier gcd at (e_j) contains (R_j); it is either a
proper factor or an earlier global return. Both contradict the branch under
consideration. Hence every (e_j=e). If all gcds through (C) are one,
the same observation shows every (e_j>C).

At a no-factor global return, stripping the known multiple (2e) gives a
common exact ordinary order (m). In an odd prime-power unit group,

\[
e=\begin{cases}
m/2,&m\text{ even},\\
m,&m\text{ odd}.
\end{cases}
\]

Thus (operatorname{lcm}(2,m)=2e). If (m) is even, (2) has this
order. If (m) is odd, (-2) has this order. The absolute-screen
certificate gives (sigma(m)>n), so (m>n) and (2e\ge m>n).
Factor-first stripping also gives (gcd(2e,N)=1).

If the scan has no return, (e_j>C). Since quotient order cannot exceed
ordinary order, every local absolute order also exceeds (C). This is
exactly the stated normalized hard base-two block.

### 5. Cost and recursion

(Lambda_n) has (O(n)) bits and a sieve through (n) constructs it and
its factorization in polynomial time. All absolute stripping exponents have
polynomial bit length. The relative loop makes (C) modular-power and gcd
calls. Trial division through a returned (e\le C), factoring (2e), and
the subsequent stripping remain within
(2^{(\log n)^{O(1)}}) bit operations. The Mersenne branch is polynomial.

A factor tree has fewer than (2n) nodes. Applying a QP routine to each
child and using deterministic primality testing therefore preserves the QP
bound. This counting includes prime powers and repeated prime factors.

## Scope check

The proof certifies the trichotomy only. It supplies no contradiction in
Outcome C and no QP method to localize unequal hidden orders of (2). The
statement's exclusions are therefore necessary and correctly prevent a
claim of QP factoring.
