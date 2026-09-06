# F158 hostile audit — PASS

## Frozen inputs

I read the complete frozen statement, proof, and manifest. The statement and
proof hashes matched the expected values before this audit:

- `STATEMENT.md`:
  `82c67580584de96200be0644b809ddd10f67fa24e5c088bd484342f3b4fee864`;
- `PROOF.md`:
  `6c4f6254709c25e0c5d673dc24e2ac4af843cb8e2d39adb3a7d18b86b4d756e7`;
- `MANIFEST.md`:
  `85cc9243c5d32f32ae83775ffb5fa9d1b94511d98f2b25ed4784a56de367b830`.

I did not modify a frozen input or a durable ledger. I ran no research
computation. The finite `N=77` arithmetic was checked directly from the
displayed integers.

## Verdict

**PASS.** The explicit-subgroup trichotomy, common-order certificate,
compact lift test, order-doubling induction, square-root capacity cutoff,
and F154 specialization are correct under their stated hypotheses.

The result is a conditional decoder and progress law. It is not a relation
source, a factoring algorithm, or by itself a publication-level novelty
claim. Its missing hypothesis is very strong: a source must return a factor
or an external coprime quadratic lift at every surviving state. Starting
from `(-1,2)`, the first such lift is a square root of `-1`. It does not
exist when either hidden prime is `3 modulo 4`. Even when it exists, the
tower can stop at the smaller hidden two-adic capacity long before its order
reaches `sqrt(N)`. These facts do not contradict the frozen scope; they show
how much work remains in the source theorem.

## 1. The explicit-subgroup priority rule is exhaustive

For `N=pq`, every gcd in the scan is one of `1,p,q,N`. A proper value gives
a factor. A value `N` means that `x` equals the scanned element modulo `N`.

Assume all scan gcds are one. If `x_r` belonged to the image `H_r` for
`r=p` or `q`, some listed `h in H` would satisfy `x=h modulo r`. Then
`r` would divide `gcd(x-h,N)`, which is impossible. Thus `x_r` is outside
`H_r` for both hidden primes.

Because `x^2 in H`, the coset of `x_r` in
`<H_r,x_r>/H_r` has order at most two. It is nonidentity, so the local
index is exactly two. The same argument modulo `N` gives global index two.
The priority rule matters: if one listed element equals `x` globally while
another comparison already gives a proper gcd, the algorithm returns the
factor first. Therefore the three reported outcomes are exhaustive and do
not conflict.

Successive no-factor, non-inert steps apply the same argument to the newly
generated subgroup. Hence all three size equalities in (6) follow by
induction. If the starting list has quasipolynomial size and the number of
doublings is polylogarithmic in `n`, the resulting list has
quasipolynomial size. The statement correctly does not claim that explicit
enumeration supports the `O(n)` compact tower.

## 2. The common-order certificate is exact

For either hidden prime `r`, let `d_r=ord_r(g)`. Equation (7) gives
`d_r | M`. If `d_r<M`, some prime `ell | M` has smaller exponent in
`d_r` than in `M`, and therefore `d_r | M/ell`. This makes
`g^(M/ell)=1 modulo r`, so the gcd in (8) is divisible by `r`. That
contradicts its value one. Thus both local orders equal `M`.

For odd `N`, `(-1)^2=1`, and

\[
\gcd((-1)^{2/2}-1,N)=\gcd(-2,N)=1.
\]

Therefore `(-1,2)` is a valid certificate for every odd input in the stated
semiprime scope. This does not create a square root of `-1`; it only gives a
valid initial state.

## 3. The compact lift trichotomy is exact

Since `gcd(a,M)=1`, `g^a` has exact order `M` in both hidden fields. The
internal square roots in the cyclic subgroup `<g_r>` correspond exactly to
solutions of

\[
2k=a\pmod M.
\]

There are `gcd(2,M)` solutions when soluble and none otherwise, so there are
at most two. Under the additional coprimality hypothesis the situation is
even narrower: if `M` is even, then `a` is odd and there is no solution; if
`M` is odd, there is one solution.

If `x` matches an internal candidate in one hidden field only, its comparison
gcd is proper. If it matches in both fields, the gcd is `N` and `x` is in
`<g>` globally. If no match occurs, `x` is outside `<g_r>` for both hidden
primes.

Let `e_r=ord_r(x)`. From `ord_r(x^2)=M`,

\[
\frac{e_r}{\gcd(e_r,2)}=M.
\]

If `e_r` were odd, then `e_r=M`; the unique subgroup of order `M` in the
cyclic group `F_r^*` would contain `x`, contrary to the no-match branch.
Thus `e_r` is even and `e_r=2M`. Exact order `2M` also verifies every gcd
screen needed for the next certificate `(x,2M)`. Updating the supplied
factorization of `M` only increments the exponent of two.

The alternatives are exclusive under the stated priority. With
`gcd(a,M)=1`, there cannot be two different internal candidates that create
an unhandled mixture of an `N` gcd and a proper gcd.

## 4. The capacity cutoff and cost are correct but loose

Induction gives common local order `M_t=2^t M_0`. Therefore

\[
M_t\mid p-1
\quad\text{and}\quad
M_t\mid q-1.
\]

Since `p<q` and `N=pq`, one has `p<sqrt(N)`, and hence
`M_t <= p-1 < sqrt(N)`. A genuine expansion at or above the displayed
cutoff is impossible. The number of attempted levels before that cutoff is
`O(n)`. Each compact test uses at most two gcds and polynomial-size modular
arithmetic, so the decoder is polynomial once the source hypothesis is
granted.

This cutoff is only an outer capacity bound. For the universal start, all
orders are powers of two. The actual number of possible expansions is at
most

\[
\min\{v_2(p-1),v_2(q-1)\}-1.
\]

For example, if either prime is `3 modulo 4`, no first lift with square
`-1` exists. A source satisfying Section 6 must return a factor at such a
state. Thus the source theorem already contains the difficult factor-correlated
step; the order argument does not manufacture it.

The phrase “supplies a non-inert coprime quadratic lift at every level” must
retain the statement's explicit `factor or lift` meaning. A literal promise
of a lift at every level is false once the local two-adic capacity is
exhausted. Sections 4 and 6 state the needed factor-or-lift version clearly
enough, so this is a reading constraint rather than a counterexample.

## 5. The F154 specialization is valid and conditional

F154 defines `s_v` as the inverse of `z_v` and has

\[
z_v^2=Q(v)\pmod N.
\]

Therefore

\[
s_v^2=Q(v)^{-1}\pmod N,
\]

which belongs to `H=<q_1,...,q_m>`. Every such `s_v` is a legal input to
the explicit-list theorem. The `N=77` certificate is exact:

\[
|\langle9\rangle|=\operatorname{lcm}(3,5)=15,
\quad
26^2=60=9^{-1}\pmod {77},
\]

and

\[
\gcd(26-9^2,77)=\gcd(-55,77)=11.
\]

For the compact theorem, membership in a multigenerator subgroup is not
enough. The source must also give one certified common-order generator, the
exponent presentation `Q(v)^(-1)=g^a`, and `gcd(a,M)=1`. F158 explicitly
lists these extra hypotheses and does not attribute them to F154 or F156.

## 6. Scope and novelty boundary

The mathematical engine is the elementary fact that adjoining a square root
outside a subgroup creates an index-two extension, combined with exact
order certificates and CRT gcd comparisons. Its useful project-level
contribution is the precise monotone progress measure and compact
factor-or-inert-or-double interface. The theorem does not show that public
canonical relations hit an external root, that such hits have inverse-QP
density, or that feedback can repeat on every input.

A fresh blind reconstruction is still required before promotion under the
project protocol.
