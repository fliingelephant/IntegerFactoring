# F76 corrected hostile re-audit — uniform-seed quotient collisions

## Artifact and verdict

**Candidate:**
`experiments/F76_uniform_seed_quotient_collision_kill/RESULT.md`

**Pinned SHA-256:**
`87a5706f674dfd507acaf1777ff69217c0a6040483c6651b41351c8a1bc84aac`

**Verdict: PASS.**

The added deterministic primality test repairs the only counterexample from
the first audit. On every branch that reaches the estimate for
`N/phi(N)`, the input is composite and every prime divisor of `N` is greater
than `B`. The large-common-prime bound, the independence-free union, the
adaptive-target claim, the prime-power cases, and the asymptotic consequence
all pass.

No computation was run. This is a fresh symbolic re-audit of the complete
corrected proof.

## 1. The corrected continuation invariant is valid

The setup first stops when `N` is prime. Therefore every input that reaches
trial division is composite. If trial division through `B` does not return a
proper factor, no prime `q <= B` can divide `N`: for composite `N`, every
prime divisor satisfies `1 < q < N` and would itself be a proper factor.
Thus the continuation branch has

\[
q>B\qquad\text{for every prime }q\mid N.
\tag{A}
\]

This includes prime powers. If `N=q^e` with `e>=2` and `q<=B`, trial
division stops with `q`. If `q>B`, condition (A) holds and the proof below
uses only the one distinct prime `q`.

There is no remaining small-input exception. Since `N>=3`,

\[
n=\lceil\log_2(N+1)\rceil\ge2,
\]

and the declared hypothesis gives `B>=3`. Prime inputs, including the old
counterexample `N=3`, stop before estimate (2). Composite inputs with a
small prime divisor stop during trial division.

## 2. The fixed-prime probability estimate is correct

Fix `i`, `r`, and a prime `ell` dividing

\[
C_r=1+rN.
\]

Because `C_r` is congruent to `1` modulo `N`, one has
`gcd(ell,N)=1`. Among the canonical representatives in
`1,...,N-1`, there are at most

\[
\left\lfloor\frac{N-1}{\ell}\right\rfloor
\le \frac N\ell
\]

multiples of `ell`. Restricting this set to units cannot increase its size.
Since `U_i` is uniform on the `phi(N)` unit representatives,

\[
\Pr(\ell\mid U_i)\le \frac{N}{\ell\varphi(N)}.
\]

Inversion permutes the unit group. Hence the canonical inverse `V_i` has the
same uniform marginal law and satisfies the same estimate. The two variables
need not be independent. Since `ell` is prime,

\[
\ell\mid U_iV_i
\quad\Longrightarrow\quad
\ell\mid U_i\ \text{or}\ \ell\mid V_i.
\]

The union bound therefore gives exactly

\[
\Pr(\ell\mid A_i)
\le \frac{2N}{\ell\varphi(N)}.
\tag{B}
\]

This argument also covers the degenerate sample `U_i=V_i=1`, for which
`A_i=1` and `K_i=0`.

## 3. The two outer unions need no independence

Let

\[
t=\lceil\log_2(R+1)\rceil.
\]

The integer inequalities `N<2^n` and `R<2^t` imply

\[
C_r=1+rN\le 1+RN\le2^{n+t}
\]

for every `1<=r<=R`. Thus `C_r` has at most
`log_2(C_r)<=n+t`, and hence at most the candidate's looser value

\[
L=n+t+1
\]

in distinct prime divisors. For every such divisor `ell>B`, estimate (B)
is at most `2N/(B phi(N))`. Summing over these divisors proves the fixed
`(i,r)` bound.

If a prime divides

\[
P=\prod_{i=1}^m A_i,
\]

Euclid's lemma makes it divide at least one `A_i`. A union over all `mR`
pairs therefore proves

\[
\Pr\!\left(\exists r\le R,\ \exists\ell>B:\ell\mid D_r\right)
\le \frac{2mRNL}{B\varphi(N)}.
\]

Only marginal uniformity of each `U_i` was used. The samples may have
arbitrary dependence across indices.

The same displayed event already contains every `r` in the declared range.
For any random or adaptive selection

\[
r_*=f(U_1,\ldots,U_m,\text{prior transcript})\in\{1,\ldots,R\},
\]

the event that `D_(r_*)` has a prime divisor greater than `B` is a subset of
this union. No conditional uniformity after observing `r_*` is needed.

## 4. The totient estimate now holds on every relevant branch

On the continuation branch, (A) implies that every distinct prime divisor
`q` of `N` satisfies `q>=B+1`. Consequently,

\[
(B+1)^{\omega(N)}\le\prod_{q\mid N}q\le N,
\]

so

\[
\omega(N)\log_2(B+1)\le\log_2N<n.
\]

For every `q>B`,

\[
-\log(1-1/q)=\log\!\left(1+\frac1{q-1}\right)
\le\frac1{q-1}\le\frac1B.
\]

Using the standard product formula for `phi` gives

\[
\log\frac N{\varphi(N)}
\le\frac{\omega(N)}B
\le\frac{n}{B\log_2(B+1)}.
\]

Repeated prime powers do not change this product. Because `B>=n`, the last
exponent is at most one (in fact it is smaller), and therefore

\[
\frac N{\varphi(N)}
\le \exp\!\left(\frac{n}{B\log_2(B+1)}\right)
\le e.
\]

This proves corrected estimates (2) and (3) for every branch on which they
are invoked.

## 5. The asymptotic exponent and polynomial work are correct

For fixed `a,b,c>=1`, the bounds `m<=n^a` and `R<=n^b` imply

\[
L=n+O(\log n)=O(n).
\]

With `B=n^(a+b+c+3)`, estimate (3) is actually

\[
O\!\left(
\frac{n^{a+b+1}}{n^{a+b+c+3}}
\right)
=O(n^{-c-2}),
\]

which implies the stated weaker `O(n^(-c-1))` result.

There are polynomially many samples and targets. Each `A_i` has `O(n)`
bits, their explicit product has `O(mn)` bits, and each `C_r` has
`O(n+log R)=O(n)` bits. Trial division through a fixed polynomial `B`, the
required products, and the gcd calculations therefore have polynomial bit
cost. If the constants are allowed to be nonintegral, replacing the displayed
`B` by its ceiling is the harmless standard rounding convention and leaves
all estimates unchanged.

On the complementary event, no prime above `B` divides any `D_r`; this is
exactly `B`-smoothness. Trial division completely factors every such `D_r`.
It also exposes the full `B`-smooth part of each public `C_r` and of each
explicit retained endpoint.

## 6. The conclusion stays within what was proved

The result rules out one proposed source of hard information: polynomially
many uniform inverse seeds are very unlikely to make a target `C_r` share a
prime above a suitably chosen polynomial trial bound. It does not rule out
useful products of small primes, useful multiplicity or provenance patterns,
or a separator assembled from smooth data. It also does not bound `D_r` by
`r`. The candidate states all of these limitations.

The final exclusion of adaptive canonical-residue or block-feedback seeds
must be read in its stated reason: those processes need not preserve the
uniform marginal hypothesis. If a particular adaptive process did preserve
every required uniform marginal, the theorem would still apply. The
candidate proves no blanket result for general feedback-generated states,
and it does not claim a factoring algorithm.

Thus the corrected artifact is valid at its exact narrow scope: an
independence-free, adaptive-target obstruction for fresh seeds with uniform
marginals.
