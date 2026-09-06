# Proof of the F233 projective-coverage candidate

## 1. Zero-defect quotient children

Equation (1) gives `N=BH+1`.  For every `1<=u<B`,

\[
uN=(uH)B+u,
\]

with `0<u<B`.  Therefore the Euclidean quotient is `uH`, without a parity
restriction on `u`, and (4) is its shifted child.  Since `C<H`, every child
in the symmetric bank is positive.

## 2. Gap-ratio incidence

Let `ell|s_p`.  Then `p=1 mod ell`.  Reducing `BH=N-1` modulo `ell` gives

\[
BH\equiv q-1\equiv q-p=g\pmod\ell.
\tag{P1}
\]

The power of two `B` is a unit modulo the odd prime `ell`, so

\[
H\equiv gB^{-1}\pmod\ell.
\tag{P2}
\]

It follows that

\[
B(uH+c)\equiv ug+cB\pmod\ell,
\]

which proves the first equivalence in (8).

If instead `ell|s_q`, then `q=1 mod ell`, and

\[
BH\equiv p-1=p-q=-g\pmod\ell.
\]

This proves the second equivalence.

Every prime considered in (5) is coprime to `H`; hence (P2) also shows that
`rho_ell` is nonzero.  At the `p` orientation, capture is

\[
\rho_\ell=-cu^{-1};
\]

at the `q` orientation it is

\[
\rho_\ell=cu^{-1}.
\]

The set of allowed nonzero `c` is closed under negation, so these are the
same projective cover.  This proves (9).

For the paired assertion, every residual prime from `s_p` captured by
`uH+c` divides `ug+cB`.  Every residual prime from `s_q` captured by
`uH-c` divides

\[
-ug-cB=-(ug+cB).
\]

The two residual orders are coprime.  Their captured squarefree prime
products are therefore coprime and their product divides `|ug+cB|`.  This
proves (10).  The assertion is deliberately squarefree: saturation in
(12) can add a higher residual prime power even when the linear gap integer
contains that prime only once.

## 3. Saturation and exact progress

The word `W_0` contains every prime at most `Y` to valuation at least `n`,
and it contains every prime in `H` to the same valuation.  Every
prime-power valuation in `s_p,s_q<N` is less than `n`.  Likewise, when one
bank child exposes a prime `ell`, its `rad(A)^n` contribution contains the
complete `ell`-primary part of either residual order.

Consequently a primary `ell^e||s_p` survives exactly when all three
conditions hold:

1. `ell>Y`;
2. `ell` does not divide `H`;
3. no bank child is divisible by `ell`.

Equation (9) turns the last condition into
`rho_ell notin R_ell(U,C)`.  This proves the first formula in (13); the
second is symmetric.

P202 proves, for every completely factored word `W`, that the local return
probabilities of the projected uniform unit with exponent `WH` are

\[
1/r_p,\qquad1/r_q.
\]

It also proves that complete prime-power stripping subtracts exactly the
stale equal-order atom

\[
{1\over PQ}\sum_{d\mid M}\varphi(d)^2.
\]

Substitution of (13) gives (14).  Direct gcd screening is logically prior:
a proper child gcd already factors `N`, while a trivial screen leaves the
projected formula unchanged.

## 4. Universal coverage and avoidance

Fix a prime `ell>max(U,C)` and a nonzero `h mod ell`.  Consider the `U+1`
points

\[
0,h,2h,\ldots,Uh
\]

on the circle of `ell` residue positions.  Sort them and include the wrap
gap.  The `U+1` circular gaps sum to `ell`, so one gap has length at most

\[
\left\lfloor{\ell\over U+1}\right\rfloor.
\]

The endpoints of that gap differ by `uh mod ell` for some `1<=u<=U`, up
to sign.  Thus there is a nonzero integer `c` with

\[
|c|\le\left\lfloor{\ell\over U+1}\right\rfloor,
\qquad uh+c\equiv0\pmod\ell.
\tag{P3}
\]

The coefficient `c` cannot be zero because `h` is nonzero and `u<ell`.
If `ell<=C(U+1)`, equation (P3) has `|c|<=C`.  Hence every nonzero `h` is
covered, proving (15).

For the converse direction, each of the `U` denominators and `2C` nonzero
numerators supplies at most one residue `cu^{-1}`.  Therefore

\[
|\mathcal R_\ell(U,C)|\le2CU.
\]

It is also a subset of `F_ell^*`, proving (17).  If `ell-1>2CU`, at least
one nonzero residue is absent, which proves (16).  The displayed uniform
model probability is then just the cardinality of the hit set divided by
`ell-1`; it is not imported into the integer source.

Finally, suppose `ell` divides both `uH+c` and `vH+d`.  Elimination gives

\[
d(uH+c)-c(vH+d)=(ud-vc)H.
\]

Since `ell` does not divide `H`, one has

\[
ud-vc\equiv0\pmod\ell.
\]

But

\[
|ud-vc|\le2UC<\ell.
\]

Therefore the determinant is the integer zero, proving (18).  Such pairs
are scalar representatives of the same rational projective slope.  Any
scalar prime is at most `max(U,C)<ell` and cannot itself account for the
large prime.  Deduplication loses no large-prime incidence.

All residue classes for which the whole rectangle has a universal guarantee
occur at primes no larger than `2CU+1`, by (16).  A smooth word through
`Y_*` in (19) includes all of them, and numerical-QP bounds are closed under
products.  This proves the comparison with the P202 smooth source.

## 5. Bit cost and exact remaining requirement

There are `U(2C+1)` children, and

\[
0<uH+c\le UH+C.
\]

The zero-defect child `H` has at most `ceil(n/2)+O(1)` bits.  Thus the bank
child bound in the statement follows.  A numerical-QP number of recursive
calls with a fixed contraction has a numerical-QP recursion tree, under the
declared external all-input dispatcher.  Each child contributes no more
prime occurrences than its bit length, and raising its radical to `n`
adds only a factor `n` to the word height.  Modular powering and complete
puncturing are therefore numerical QP.

The proof supplies no actual-input distribution for `rho_ell`.  Equations
(9), (13), and (14) show exactly what remains: an all-input number-theoretic
law must force enough actual gap ratios into the small projective covers to
make one residual numerical QP, or it must provide a different correlated
base with inverse-QP factor-or-growth mass.  Generic finite-field coverage
cannot supply that law beyond the already affordable smooth cutoff.

