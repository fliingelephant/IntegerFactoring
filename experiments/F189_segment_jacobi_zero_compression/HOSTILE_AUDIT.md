# F189 hostile audit

## Frozen inputs

- `MANIFEST.md`:
  `59cb0cee5ee3693cad18c194aad90034524f009c3b25e1f27de8a4527e31c764`
- `STATEMENT.md`:
  `2e7c4df447013db2e5ebc5d51045eec0abff3a36f1bf59760d74ae31f4adbfc1`
- `PROOF.md`:
  `ced9a963f902541836a1214a2d7afea4616ae53d7360b26c4d47e3434247c03e`
- `SELF_AUDIT.md`:
  `9fbba1461d4afcf3825609f461563fbdd61f50ae4035f44044562c0523cc56b1`

The three frozen-artifact hashes match the manifest. I read all four files
in full before review.

## Verdict

**PASS.** The exact identities, conditional algorithm, source probability,
and named-model lower bounds are correct within their stated scopes. I found
no false implication, parity defect, repeated-prime defect, missing affine
event, or hidden super-QP operation.

Two scope guardrails must remain explicit in any promotion:

1. The recurrence theorem is an order or state-dimension lower bound. It is
   not a lower bound on sparse description length: the annihilator
   `X^m-1` itself has a short sparse encoding.
2. The `O(n)` two-adic stratification is not an `O(n)` quotient-cell
   decomposition. It supplies no QP evaluator for the aggregate floor sums.

These guardrails agree with the frozen proof's final scope section. A later
summary must not drop the words `order`, `explicit`, or `table` when it
states the recurrence boundary.

## Hostile checks

### Arbitrary odd moduli and repeated prime powers

For

\[
 N=\prod_j r_j^{e_j},
\]

the Jacobi symbol is zero exactly when some `r_j` divides its numerator.
The parity of `e_j` does not change this: a zero Legendre factor remains
zero under every positive power. On the unit group, every local factor is a
sign. Hence

\[
 \chi_N(x)^2=\mathbf 1_{\gcd(x,N)=1}
\]

for every integer `x`, including when `N` is nonsquarefree. Therefore the
product over a segment is zero exactly when one segment member is a
nonunit. No squarefree hypothesis enters this part.

### Totalized half-floor identity

For positive odd `x,N`, let `g=gcd(x,N)`. In the rectangle

\[
 1\le i\le (N-1)/2,
 \qquad
 1\le j\le (x-1)/2,
\]

`F(x,N)` counts `jN <= ix`, while `F(N,x)` counts `ix <= jN`.
Every off-line point is counted once. Every equality point is counted
twice. The equality points are

\[
 (i,j)=k(N/g,x/g),
 \qquad 1\le k\le(g-1)/2.
\]

Both coordinate bounds give exactly this same range because `g` is odd.
Thus

\[
 F(x,N)+F(N,x)
 =\frac{(x-1)(N-1)}4+\frac{g-1}{2}.
\]

There is no boundary or strict-inequality error. Both displayed terms are
integers: each of `x-1` and `N-1` contributes a factor two, and `g-1` is
even.

Eisenstein's parity formula is invoked only for `g=1`. The proof does not
try to assign a sign to a zero Jacobi value. Multiplication by two and
subtraction of the rectangle term give

\[
 g-1
 =2(F(x,N)+F(N,x))-\frac{N-1}{2}(x-1),
\]

so summing over a multiset proves equation (8) exactly. Every summand
`g-1` is nonnegative and vanishes exactly on units. The weighted sum's zero
test is therefore equivalent to absence of a segment hit. The packet does
not confuse this weighted sum with the number of hit positions.

### Even members and quotient-cell scope

Removing the exact power of two from a positive segment member preserves
its gcd with odd `N`. For a segment contained below `2N`, the possible
two-adic valuations form `O(n)` strata. Within one stratum, the resulting
odd values form an arithmetic progression of step two, so pointwise use of
the floor identity is valid.

This gives only `O(n)` symbolic progressions. It does not collapse the
number of values in them. In particular, `F(N,x)` has a varying denominator
and a varying summation limit as `x` changes. The proof establishes no QP
bound on the number of floor-quotient cells and no fast aggregate over such
cells. Its explicit statement that the stratification does not evaluate
the floor sums is necessary and correct.

A literal zero is public. The source and isolation ranges use positive
segments, so no hidden zero endpoint is omitted.

### Conditional one-child isolation

If a parent segment has zero product, querying a left child has two exact
outcomes. A zero answer retains that child. A nonzero answer certifies that
every left member is a unit, so the unqueried right child must contain a
nonunit. Thus only one oracle call is needed at each level.

The retained length is at most the ceiling of half the old length. A
singleton is reached in at most `ceil(log_2 L)` calls. Its gcd is greater
than one. The premise that the original interval contains no multiple of
`N` makes the gcd strictly below `N`.

The oracle-domain bounds are preserved. An interval of length below `N`
that contains no multiple of `N` lies between two consecutive multiples;
starting with `a<2N`, none of its retained children can acquire a start at
or beyond the next multiple. Equivalently, periodic normalization by a
multiple of `N` is available without changing any zero or gcd predicate.

Since `L<N`, the depth is `O(n)`. A polynomial number of calls to a fixed
QP oracle, plus gcd and interval arithmetic, remains QP. This is interval
localization, not a branching integer-factor recursion.

### Affine normalization and exact probabilities

After `U,V` pass their gcd screens, `V` is invertible and

\[
 U+tV\equiv V(a+t)\pmod N,
 \qquad a=UV^{-1}.
\]

The unit multiplier preserves every nonunit position. Independent uniform
units have a uniform quotient. CRT then makes the two local coordinates of
`a` independent and uniform on their nonzero residue classes.

For `r` equal to `p` or `q`, the root `-a mod r` is uniform on
`{1,...,r-1}`. Since `T<r`, an `r`-hit occurs exactly at one of the
`T-1` nonzero positions. Hence

\[
 \alpha_r=\frac{T-1}{r-1}.
\]

Independence gives the exact union probability

\[
 \rho_0=\alpha_p+\alpha_q-\alpha_p\alpha_q.
\]

The only improper hit occurs when both local roots use the same position.
For each of the `T-1` positions, CRT gives one unit class out of
`(p-1)(q-1)`. Thus

\[
 \beta=\frac{T-1}{(p-1)(q-1)}.
\]

If the two root positions differ, every hit singleton has gcd `p` or `q`.
If they agree, there are no other local roots because `T<p,q`; isolation
returns the public multiple of `N` and the trial restarts. Therefore

\[
 \rho_{\rm use}
 =\alpha_p+\alpha_q-\alpha_p\alpha_q-\beta
\]

is exact, not only a lower bound.

The power-of-two definition of `T` gives

\[
 \frac{\lfloor\sqrt N\rfloor}{16}<T
 \le\frac{\lfloor\sqrt N\rfloor}{8}.
\]

The promise `q<2p` gives `q<sqrt(2N)` and `T<p<q`. The proof's lower bound

\[
 \alpha_q-\beta
 >\frac{36}{848\sqrt2}\frac{51}{52}
 >\frac1{40}
\]

follows from `p>=53`; the displayed event is contained in the useful event.
The probability is explicitly conditional on the unit branch. Sampling
units, obtaining an earlier gcd factor, and rejecting the zero residue all
have expected constant overhead on the stated semiprime promise.

### Radical period, Fourier support, and recurrence order

The zero mask depends only on `m=rad(N)`. Over `Z/mZ`, the unit indicator
has a CRT-factorized Fourier coefficient. For every prime `ell|m`, the
local factor is `ell-1` at local frequency zero and `-1` otherwise. Since
`m` is squarefree, no local factor vanishes. Thus every Fourier coefficient
of the unit indicator is nonzero.

For the zero mask, the zero-frequency coefficient is
`m-phi(m)>0`, and every other coefficient is the negative of a nonzero
unit-indicator coefficient. Hence all `m` Fourier modes occur. This proves
both least period `m` and minimal complex constant-coefficient recurrence
order `m`; the minimal annihilator is `X^m-1`.

The conclusion is about recurrence order, equivalently the dimension of a
literal linear state containing all active modes. It does not imply that
the sparse polynomial `X^m-1` needs `m` written coefficients, nor does it
exclude an implicit arithmetic evaluator. The frozen proof's phrase
`explicit recurrence tables` has the correct scope.

### Squarefree-semiprime correction

For `N=pq`, inclusion-exclusion gives

\[
 z_N=\delta_p+\delta_q-\delta_N,
\]

so adding the publicly recognizable global-zero spike yields
`c_N=delta_p+delta_q`. On `Z/NZ`, `delta_p` has exactly the `p`
frequencies divisible by `q`, and `delta_q` has exactly the `q`
frequencies divisible by `p`. Their supports meet only at frequency zero,
where both coefficients are positive. No cancellation is possible.

The union therefore has `p+q-1` modes. Its Fourier roots are exactly the
union of the `p`-th and `q`-th roots of unity, so its minimal annihilator is

\[
 \operatorname{lcm}(X^p-1,X^q-1)
 =\frac{(X^p-1)(X^q-1)}{X-1},
\]

of degree `p+q-1`. This statement does not extend to arbitrary composites,
and the packet does not claim that it does.

### Exact deterministic automaton size

Tracking the binary value modulo odd `m` supplies an `m`-state DFA. For the
lower bound, the nonunit set has no nonzero additive stabilizer. Given
`d != 0 mod m`, choose a prime `r|m` with `d != 0 mod r`, set `x=0 mod r`,
and, at every other local prime, avoid `x=-d`. CRT then gives `x` nonunit
and `x+d` a unit.

For two distinct residue states, multiplication of their difference by
`2^k` stays nonzero modulo odd `m`. Choosing `2^k>m` lets one encode the
required translation as a `k`-bit suffix, with leading zeros if needed.
The same suffix distinguishes the states. Every residue is reachable, so
Myhill--Nerode gives exactly `m` states.

This is a deterministic finite-state theorem with leading zeros allowed.
It is not a time lower bound for gcd algorithms, integer-register machines,
or implicit automata.

### Factorial, Kummer, and hidden-base boundary

The identity

\[
 \prod_{t=0}^{L-1}(a+t)=L!\binom{a+L-1}{L}
\]

is exact. If a hidden prime `r|N` satisfies `L<r`, then `L!` is an
`r`-adic unit. Divisibility of the product by `r` is therefore equivalent
to divisibility of the binomial coefficient by `r`.

Kummer applies to the addition of `L` and `a-1`. Since `L` has one base-`r`
digit, a carry exists exactly when the low digit starts one:

\[
 ((a-1)\bmod r)+L\ge r.
\]

An incoming low-digit carry can propagate, but that does not alter the
existence criterion. The condition is also exactly that the length-`L`
segment contains an `r`-multiple. Repeated powers of `r` in `N` do not
change this zero predicate.

No statement is made when `L>=r`. In that range `L!` need not be a unit and
`L` has more than one base-`r` digit. The carry reformulation also reveals
the hidden prime base; it does not make that base public or give an
evaluator.

### Approximation and final QP scope

On `p<q<2p`, every positive weighted summand is at least
`p-1>sqrt(N/2)-1`. Therefore an additive-error certificate strictly below
half this public gap distinguishes zero from nonzero. The packet supplies
no such certificate.

The affine splitter is conditional on a uniform exact QP zero oracle and on
the balanced squarefree-semiprime source. The floor identity and isolation
logic are valid for arbitrary odd `N`, but the constant source probability,
the `p+q-1` recurrence, and the approximation gap are not asserted outside
their stated promise. None of the recurrence, Fourier, DFA, Kummer, or
quotient-cell observations is promoted into a general factoring lower
bound.

## Computation and mutation record

No mathematical computation was used or run. The audit changed only this
`HOSTILE_AUDIT.md` file. It did not edit any frozen candidate artifact or
durable ledger.
