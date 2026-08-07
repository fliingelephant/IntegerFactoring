# F76 fresh hostile audit — uniform-seed quotient collisions

## Artifact and verdict

**Candidate:**
`experiments/F76_uniform_seed_quotient_collision_kill/RESULT.md`

**Pinned SHA-256:**
`c7d24e5e57effd5242006d06c4b9b45c746398ecd6b6514dcaf6dcd7936669bd`

**Verdict: FAIL AS WRITTEN.**

The main large-common-prime bound is correct. Its proof does not need
independence. The adaptive-target, asymptotic, smoothness, and narrow scope
claims also survive. However, the displayed bound (2) is false for the
stated input class `N >= 3`. The setup does not stop on a prime input, because
trial division is declared to stop only when it finds a proper factor.

This is a small scope defect, not a failure of the source obstruction. It can
be repaired by assuming that `N` is composite, by stopping after a
polynomial-time primality test, or by stating the exponential estimate only
for the composite continuation branch. A fresh mathematical audit is needed
for any changed candidate version under the required workflow.

No computation was run. All checks below are symbolic.

## 1. Exact counterexample to (2)

Take

\[
N=3,\qquad n=\lceil\log_2(4)\rceil=2,\qquad B=3.
\]

These values satisfy the setup condition
`B >= max(3,n)`. Trial division through `B` finds only the divisor `3=N`,
which is not a proper factor. Therefore the candidate continues. Its claim
that every prime divisor of `N` is greater than `B` is false.

The displayed estimate (2) becomes

\[
\frac{N}{\varphi(N)}=\frac32
\le \exp\!\left(\frac{2}{3\log_2 4}\right)
=e^{1/3},
\]

but `e^(1/3) < 3/2`. Thus (2) is false exactly as stated.

The weaker estimate `N/phi(N) <= e`, which is all that (3) needs, still
holds on every continuation branch. If `N` is composite, the declared trial
division implies that every prime divisor exceeds `B`, so the candidate's
proof applies. If `N` is prime, then

\[
\frac{N}{\varphi(N)}=\frac{N}{N-1}\le\frac32<e.
\]

Hence (3) survives despite the invalid derivation through the stronger (2).

## 2. The large-common-prime probability bound passes

Fix `i`, `r`, and a prime `ell` dividing `C_r=1+rN`. Then
`gcd(ell,N)=1`. Among the canonical representatives `1,...,N-1`, at most
`floor((N-1)/ell) <= N/ell` are divisible by `ell`. Restricting to units
cannot increase this count. Therefore

\[
\Pr(\ell\mid U_i)\le\frac{N}{\ell\varphi(N)}.
\]

Inversion is a permutation of the unit group. Thus the canonical inverse
`V_i` is also uniform whenever `U_i` has a uniform marginal, and it satisfies
the same bound. Since `ell` is prime,

\[
\ell\mid U_iV_i
\quad\Longrightarrow\quad
\ell\mid U_i\ \text{or}\ \ell\mid V_i.
\]

The union bound gives

\[
\Pr(\ell\mid A_i)
\le\frac{2N}{\ell\varphi(N)}.
\]

No independence between `U_i` and `V_i`, or between different sample
indices, occurs in this argument.

Also, an integer greater than zero has at most its base-two logarithm in
distinct prime divisors. The candidate's deliberately loose value

\[
L=n+\lceil\log_2(R+1)\rceil+1
\]

does satisfy `log_2(C_r) <= L`. Summing first over the large prime divisors
of each fixed `C_r`, then over all `mR` fixed pairs `(i,r)`, proves (1).
Finally, if a prime divides `P=product_i A_i`, primality makes it divide at
least one `A_i`. This last union is also valid without independence.

## 3. Adaptive targets do not evade the union

The proved event already quantifies over every integer `r` in the public
range `1,...,R`. Therefore, for any random adaptive choice

\[
r_*=f(U_1,\ldots,U_m,\text{prior transcript})\in\{1,\ldots,R\},
\]

the event that `D_(r_*)` has a prime factor greater than `B` is a subset of
the displayed union over all fixed `r`. No distributional assumption on
`r_*` is needed.

This does not extend the theorem to feedback-generated seed states. The
proof still requires each `U_i` itself to have the uniform marginal law.
The candidate states this limitation correctly.

## 4. Composite inputs and prime powers pass

Suppose `N` is composite and trial division through `B` finds no proper
factor. Then no prime `q <= B` can divide `N`, because such a `q` would itself
be a proper factor. Hence every `q | N` satisfies `q >= B+1`, and

\[
\omega(N)\log_2(B+1)\le\log_2N<n.
\]

For every such `q`,

\[
-\log(1-1/q)\le\frac1{q-1}\le\frac1B.
\]

Summing over the distinct prime divisors proves the candidate's exponential
bound for this branch. Repeated prime factors cause no problem because
`N/phi(N)` depends only on the distinct primes.

In particular, for a prime power `N=q^e` with `e >= 2`, trial division stops
with the proper factor `q` when `q <= B`. If `q > B`, the displayed proof
applies with `omega(N)=1`. Thus there is no prime-power counterexample beyond
the prime-input defect above.

## 5. The asymptotic exponent and smoothness conclusion pass

For fixed constants `a,b,c`, the assumptions `m <= n^a` and `R <= n^b`
give

\[
L=n+O(\log n)=O(n).
\]

With `B=n^(a+b+c+3)`, the right side of (3) is in fact

\[
O\!\left(
\frac{n^{a+b+1}}{n^{a+b+c+3}}
\right)
=O(n^{-c-2}),
\]

which implies the stated weaker `O(n^(-c-1))` bound. Trial division through
a fixed polynomial in `n` has polynomial bit cost on the displayed
polynomial-size list of `O(n)`-bit auxiliary integers.

On the complementary event, no prime greater than `B` divides any `D_r`.
This is exactly the statement that every `D_r` is `B`-smooth. Trial division
therefore gives its complete prime factorization. The same process gives the
full `B`-smooth part of each `C_r` and of every endpoint in the explicit
polynomial-size sample list.

## 6. The narrow scope claim passes, but must stay narrow

Every prime factor of `D_r` is a prime factor of the public value
`C_r=1+rN`. On the high-probability event, all such primes are at most `B`,
so trial division of `C_r` exposes the complete numerical pool without the
gcd with the random product. Trial division of the sampled endpoints also
exposes which of these primes occur in `P`.

This does **not** make the smooth collision useless. The selected subset,
its multiplicities, its co-occurrence pattern, or its provenance can still
form a useful relation or separator. A product of small primes can also be
large. The candidate explicitly preserves these possibilities and proves no
factor-selection theorem. Therefore its exact conclusion is valid only as a
large-prime source obstruction: uniform seeds very rarely add a previously
hidden prime above the chosen polynomial trial bound. It is not an
obstruction to smooth-factor aggregation or to adaptively correlated
feedback.
