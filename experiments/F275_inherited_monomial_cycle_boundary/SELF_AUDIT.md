# F275 author self-audit

## Verdict

`PASS` as a narrow proof-only candidate. Fresh hostile and statement-only
audits are still required before promotion.

## 1. Claim-to-proof check

Theorem A is proved by writing every old exponent as its parity plus twice a
nonnegative integer. The transformed exact square then pulls back to an old
exact square. The positive-root and supplied-root formulas cancel the same
square factors, leaving exactly the old normalized root times one global
sign.

Theorem B is proved from the two perfect matchings of a simple even cycle.
Both alternating edge products equal the same carrier product modulo `N`.
This gives the normalized-root formula and the exact signed-gcd equalities.

The reduced-complement boundary follows from the exact lift identity

\[
 a(N-a)=[-a^2]_N+
 \left(a-1-\left\lfloor{a^2\over N}\right\rfloor\right)N
\]

and from reduction of the unreduced operand product modulo `N^2`.

## 2. Essential hypotheses

1. The old and transformed rows are units modulo `N`. This makes every
   normalized-root division and gcd invariance valid.
2. The monomial exponents are nonnegative integers. Division or rational
   rows require a separate integral normal form.
3. Each multiplier `s_j^2` is an exact integer square.
4. The transformed supplied root is inherited up to a global sign. An
   arbitrary second root must first undergo the explicit signed comparison.
5. The label-only cycle identity uses a simple even cycle. It uses its two
   perfect matchings.
6. Canonical reduction is additive and is outside the monomial theorem.

## 3. Deliberate nonclaims

F275 does not prove any of the following.

- Every relation among monomial rows is global. A relation with
  `M^Tc != 0` pulls back to an old relation and can preserve its useful root.
- A lower bound for canonical sections or factoring.
- A rank theorem for reduced complement products.
- A private-pivot theorem for any independent canonical row family.
- A classification of odd graph cycles.
- A classification of additional square-class dependencies among graph
  carriers.
- A bound on numerical prime coincidences after canonical reduction.
- A result for F270. F270's same-modulus union must still be recomputed from
  its exact row values.
- A reason to launch a reduced-complement search without a new mechanism.

## 4. Closest-boundary check

- P217/F252 localizes specialization-only shared primes by pairwise
  resultants after generic Pell duplicates are removed. It does not supply an
  all-input private-pivot theorem.
- P218/F253 shows that clean odd-multiple Pell identities give global decoys
  and that fixed-past fibre bounds do not control a retrospective kernel.
- F268-D04 is finite evidence that every row of every tested separate
  canonical scalar bank had a private nonsquare pivot.
- The proposed F270 union is materially different because it rebuilds one
  factor-free block system from all same-modulus families. It is not an
  exact monomial replacement of those rows.

The F275 statements neither duplicate nor strengthen these boundaries beyond
their stated exact interface.

## 5. Root-sign and gcd check

If `Z` and `X` are unit roots of the same row, then `eta=X/Z` is a root of
one. Multiplication by the unit `Z` preserves both signed gcds. Thus a
non-global discrepancy is already a factor; otherwise `X=+Z` or `-Z` on the
no-factor branch. This validates the root-inheritance reduction.

On an even cycle,

\[
 R\equiv P_0^2\equiv P_1^2,
 \qquad X=P_0P_1.
\]

Therefore `rho=P_0/P_1`, and multiplying `P_0-P_1` or `P_0+P_1` by the unit
`P_0` yields `R-X` or `R+X` modulo `N`. The two gcd equalities are exact.

## 6. Evidence boundary

No source code, checker, compile, benchmark, local search, remote search,
corpus, empirical result, or ledger edit belongs to this packet. Hashing the
proof artifacts freezes text only. A mathematical change requires a new
version and fresh audits.

