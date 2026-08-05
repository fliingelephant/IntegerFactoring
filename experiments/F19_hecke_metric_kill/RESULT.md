# F19 candidate: the level-2 Eisenstein coefficient is the metric hint

**Status:** candidate proof; not yet hostile-audited or proof-blind reconstructed.

**Closest prior route and material difference.**  The closest promoted route is
F18's manufactured-metric-hint question.  F18 treats scaled Fermat scans and
literal square-residue wheels.  This route instead follows Inspiration A2 and
uses one fixed modular form whose exact Hecke data *is* the missing trace
`p+q`.  It therefore ends in an integer discriminant and square root, not a
polynomial computation over `Z/NZ` followed by a gcd.  No close Hecke or modular
coefficient route appears in `FAILED.md`.

**Computation:** none.  This is a proof-only candidate, so there is no run
manifest.

## 1. A fixed modular form

Write

\[
 E_2(z)=1-24\sum_{m\ge 1}\sigma_1(m)q^m,
 \qquad q=e^{2\pi i z},
\]

and define

\[
 F(z)=2E_2(2z)-E_2(z).
\tag{1}
\]

Although `E_2` is quasimodular, the anomalous terms cancel in (1), and `F` is a
holomorphic modular form of weight two on `Gamma_0(2)`.  Here is a direct check
of the only point that matters.  For
`gamma=(a b; c d)` in `Gamma_0(2)`, put `c=2c'`.  The matrix

\[
 \gamma' = \begin{pmatrix}a&2b\\c'&d\end{pmatrix}
\]

has determinant one and sends `2z` to `2 gamma z`.  The anomalous term in the
transformation of `2E_2(2z)` is therefore twice the term with lower-left entry
`c'`, exactly the anomalous term of `E_2(z)` with lower-left entry `c`; the
difference transforms with weight two.  Holomorphy at infinity is visible from
the displayed series.  At the other cusp, applying the weight-two slash by
`S=(0 -1;1 0)` and the same transformation formula gives

\[
 (F|_2S)(z)=\tfrac12E_2(z/2)-E_2(z),
\]

which has a holomorphic Fourier expansion in `q^(1/2)`.

The expansion of (1) is

\[
 F(z)=1+24\sum_{m\ge1} b_mq^m,
 \qquad
 b_m=\sigma_1(m)-2\,\mathbf 1_{2\mid m}\sigma_1(m/2).
\tag{2}
\]

If `m=2^a u` with `u` odd, then the geometric-series formula in (2) gives

\[
 b_m=\sigma_1(u).
\tag{3}
\]

In particular, for odd `m`, `b_m=sigma_1(m)`.  The normalized form is a Hecke
eigenform away from level two: (3) is multiplicative and, for every odd prime
`ell`,

\[
 b_{\ell^{r+1}}=b_\ell b_{\ell^r}-\ell b_{\ell^{r-1}}.
\]

Thus the `T_m` eigenvalue on this fixed Eisenstein line is `b_m` for odd `m`.

## 2. Exact coefficient or Hecke access factors directly

Let `N=pq` for distinct odd primes.  From (2)--(3),

\[
 b_N=\sigma_1(N)=(p+1)(q+1)=N+p+q+1.
\tag{4}
\]

Consequently an exact algorithm for the `N`-th normalized coefficient, or for
the `T_N` eigenvalue on this fixed line, yields

\[
 s=b_N-N-1=p+q.
\]

Compute the exact integer square root of

\[
 D=s^2-4N=(q-p)^2
\]

and return `(s-sqrt(D))/2,(s+sqrt(D))/2`, after checking integrality,
nontriviality, and product `N`.  This extraction uses no gcd.

The reduction has polynomial bit complexity.  Since
`(p-1)(q-1)>0`, one has `p+q<N+1`, so `b_N<2N+2` and has `O(log N)` bits.
Subtraction,
squaring, exact integer square root, and verification act on `O(log N)`-bit
integers.  Therefore a uniform `poly(log N)` exact coefficient routine would be
a uniform `poly(log N)` factoring routine on every distinct-odd-semiprime
input, without a balance promise.

Conversely, the factors compute (4) immediately.  More generally, a complete
factorization of any `m` computes `b_m` from (3) and the product formula for
`sigma_1`; there are at most `log_2 m` prime factors counted with multiplicity,
and all intermediate values have polynomial bit length.  Exact access to this
apparently favorable coefficient is thus not an independent granted primitive.

## 3. Even modular coefficient access suffices

The conclusion does not require the coefficient as an unbounded integer.  Give
an oracle the odd index `N` and an arbitrary supplied modulus `Q`, and suppose it
returns the coefficient `[q^N]F=24b_N modulo Q` in time polynomial in
`log N+log Q`.

Let `n=ceil(log_2(N+1))`, choose

\[
 M=2^n,\qquad Q=24M,
\]

and take the least residue `r` returned modulo `Q`.  Because the integer
coefficient and the modulus are both divisible by 24, so is `r`, and

\[
 u=r/24=b_N\pmod M.
\]

For any nontrivial semiprime,

\[
 0<p+q<N+1\le M.
\]

Hence the least residue

\[
 s=(u-(N+1))\bmod M
\]

is the *integer* `p+q`, not merely its congruence class.  The preceding
discriminant extraction factors `N`.  Both `M` and `Q` have `O(n)` bits.

Thus a factor-free polylogarithmic algorithm for this coefficient modulo
user-supplied `O(log N)`-bit moduli already factors every distinct odd
semiprime.  Merely changing from exact integers to modular output does
not remove the hidden factoring lemma.

## 4. Approximate access is exactly a manufactured metric hint

Suppose instead that an algorithm returns an integer `h` satisfying

\[
 |h-b_N|\le B(n).
\]

Then `h-N-1` is a radius-`B(n)` hint for `p+q`.  When `B` is polynomial, scan the
`2B+1` integer candidates, square-test `t^2-4N`, and verify the resulting product.
This is deterministic polynomial bit complexity.  The same statement for the
unnormalized coefficient permits error `24B` after division/rounding.

So this fixed modular form does identify an ideal way for bare `N` to manufacture
a metric hint.  But producing even a polynomial-additive approximation to the
relevant Hecke eigenvalue is already sufficient to factor.  An analytic or
algebraic evaluator must therefore be justified at that precision rather than
treated as a standard modular-form subroutine.

## 5. What this kills, and what remains open

This closes only the following shortcut:

> call an exact, large-modulus, or polynomial-additive-accuracy evaluator for the
> `N`-th coefficient/`T_N` eigenvalue of the fixed level-2 Eisenstein form, then
> regard `p+q` as cheaply obtained modular-form data.

The terminal access problem is factoring-equivalent on balanced semiprimes.  A
q-expansion algorithm that enumerates divisors, decomposes `T_N` using the prime
factorization of `N`, or materializes `N` coefficients is also not polynomial in
the input bit length.

This is **not** a generic obstruction to Inspiration A2.  It does not rule out a
different modular form, a low-dimensional Brandt or modular-symbol object with a
factor-free binary-index evaluator, a local rank mismatch, a compressed
coefficient algorithm whose output is not `sigma_1(N)`, or an invariant that
reveals a factor without reconstructing `p+q`.  It supplies no top-level
factoring algorithm.

## Candidate theorem

> **F19 coefficient-hard metric theorem.**  For the fixed form
> `F=2E_2(2z)-E_2(z)` in `M_2(Gamma_0(2))`, the normalized coefficient and odd
> Hecke eigenvalue at an odd semiprime `N=pq` equal
> `sigma_1(N)=N+p+q+1`.  Exact access, access modulo an arbitrary supplied
> `O(log N)`-bit modulus, or additive `poly(log N)`-accuracy access factors every
> product of two distinct odd primes in polynomial bit complexity by a verified integer
> discriminant computation, without a terminal gcd.  Hence those evaluator
> interfaces cannot be assumed as factor-free primitives; the theorem does not
> preclude other modular/automorphic separators.
