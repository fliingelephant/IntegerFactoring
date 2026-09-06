# F235 strict statement-only reconstruction

## Verdict

PASS.  Every displayed claim was reconstructed from the frozen statement.

## Independent reconstruction summary

1. If the two local two-adic valuations differ, then
   `v2(N-1)=min(e,f)`.  Zero defect makes both factors exceed incompatible
   multiples of `B`, contradicting `N<2^n`; hence `e=f`.
2. Reduction of `N-1` modulo the two odd local orders gives
   `gcd(H,P)=gcd(H,Q)=D`.
3. For `d=2^eD`, exact valuation bookkeeping gives
   `gcd(E,p-1)=d gcd(W,s_p)` and its `q` analogue.  Cyclic root counts and
   CRT give the independent return probabilities.
4. Conditional global return leaves two independent uniform elements of
   `C_(2^e)`.  Their exact two-order exponents have masses
   `2^(-e),2^(j-1-e)`.  The Miller chain splits exactly when the two
   exponents differ, yielding `mu_e=(2/3)(1-4^(-e))`.
5. Adding exclusive-return and Miller-success atoms gives the exact complete
   trial law and the `1/2` saturation bound.
6. `ord_(s_p)(N)<=K` or its `q` analogue makes the corresponding residual
   divide one factor of `W_K`; the word has fewer than `nK(K+1)/2` bits.
7. The `n`-th powers of public children contain every residual primary
   supported by their union.  No child factorization is needed.
8. All construction, modular-power, square-chain, and gcd costs are
   polynomial in `n+log W`, hence numerical quasipolynomial for the declared
   word families.

The reconstruction explicitly confirmed that none of these steps proves an
all-input QP bound on the smaller meta-order.
