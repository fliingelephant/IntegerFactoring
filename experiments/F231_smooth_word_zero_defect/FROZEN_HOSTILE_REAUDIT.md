# F231 frozen hostile re-audit

## Verdict

**PASS.** I found no false claim within the frozen packet's declared
balanced, distinct-prime, zero-defect, conditional-recursion scope. The
repaired correlated-source boundary excludes the stale joint atom. The
full two-adic argument correctly proves that `s_p=s_q=1` is impossible.
The exact stale law, constants, Las Vegas stage bound, word constructions,
aggregation, and bit-cost claims survive regression.

This verdict does not promote F231 and does not supply the missing
all-input dispatcher or residual-saturating word source.

## Authentication

I authenticated the five supplied frozen hashes before reading the
manifest or candidate contents. All matched exactly:

| Frozen file | SHA-256 |
|---|---|
| `STATEMENT.md` | `f7503be5f8db21697157bc6f267b5719e656d55b395f8d8d524c5a0661d1dd56` |
| `PROOF.md` | `02a8c7a863bbec8b4bbd2475b617456a1d4e059c44e693c96526f7ae60c663c5` |
| `SELF_AUDIT.md` | `a2ae6a640974d396940985c63892fa0263868f8cb1b095dced85439509e4b657` |
| `PROVENANCE.md` | `608ff1794971bfc2bb69eee64ce511823594372fad9016e4dcfd47a0a5a14331` |
| `MANIFEST.md` | `f8cedfa7a1829958f06435f4d1f1ddd0f6fed8b567a6fc5a7b42761e5ae95908` |

The imported identities also matched the hashes recorded in the manifest.
The preserved failed draft audit remained at
`6301af75b0cf075819e43040f8e862df6dcd874c21ace8941b621b9fd5cbd138`.

## Required hostile checks

1. **Return kernels and shared primes.** Primewise valuation of
   `gcd(H,P)=D` gives
   `gcd(WH,P)=D gcd(W,s_p)=P/r_p`, including when a prime divides both
   `D` and `s_p`. The symmetric identity holds at `q`. The residuals are
   coprime because they divide the coprime quotients `s_p,s_q`.
2. **Exhaustive stripping and exact stale atom.** Exactly one local return
   gives a proper initial gcd. Neither local return makes every divisor
   puncture useless. On a global return, unequal local order valuations
   expose a factor, while equal valuations recover the exact common order.
   Thus no progress occurs exactly on neither-return samples or on
   `o_p=o_q=d|M`. Independence and the cyclic exact-order count give the
   stale probability

   \[
   {1\over PQ}\sum_{d\mid M}\varphi(d)^2.
   \]

3. **Impossible equal residuals.** If `s_p=s_q=1`, then `P=Q=D` and
   `p=2^eD+1`, `q=2^fD+1`. Balance gives `f=e+1`. Expansion gives
   `v_2(N-1)=e`, whereas `N>2^(2e+1)` implies
   `floor(n/2)>=e+1`. This contradicts `B|N-1`. No terminal-capacity
   exception remains.
4. **Constants and termination.** One saturated residual makes the union
   of local returns certain. The stale bound is at most
   `(M/D)^2/(s_ps_q)<=1/(s_ps_q)<=1/3`, so every history has useful-event
   probability at least `2/3`, including `M=D`. Strict growth can occur
   fewer than `n` times before a factor; conditional geometric-tail bounds
   give almost-sure termination and at most `3n/2` expected stages. A
   beta-two terminal can only stop the process earlier.
5. **Arbitrary powers and child enrichment.** Every prime at most `Y` has
   valuation at least `n` in `Lambda_Y^n`, exceeding its possible
   valuation in an integer below `N`. Giving every prime divisor of the
   factored public child `H` exponent `n` similarly absorbs its full hidden
   residual primary part. The added logarithmic height is at most
   `n log_2 H=O(n^2)` and uses no hidden factor of `N`.
6. **Bit complexity.** A numerical-QP bound on the numerical value of `Y`
   makes the sieve, factor list, exponent length `O(nY log Y)`, modular
   powers, gcds, and all punctures numerical-QP. No running-time claim is
   based on the short encoding of an exponent valuation while ignoring the
   resulting word's logarithmic height.
7. **Lcm aggregation.** Lcm takes maximum listed valuations and has height
   and list size bounded by the input totals. Increasing `W` can reduce
   direct mismatch mass, but it weakly increases each return probability.
   The union-of-returns expression is coordinatewise monotone, and the
   stale term is independent of `W`; hence total factor-or-growth
   probability is monotone as claimed.
8. **Repaired correlated source.** Every frozen correlated-source sentence
   now requires inverse-QP mass of exactly-one returns or nonstale global
   returns, equivalently useful factor-or-growth mass for this decoder.
   It explicitly rejects marginal identity mass, which can be concentrated
   on simultaneous stale returns. The pre-freeze counterexample no longer
   applies.
9. **Scope.** The factorization of `H` is an explicit recursive premise.
   The packet claims neither an all-input dispatcher nor hidden-factor
   access. It also states correctly that P161 roughness does not imply
   residual saturation or numerical-QP residual size.

I modified no frozen input and did not modify the preserved
`HOSTILE_AUDIT.md`. I wrote only this re-audit. I used no numerical
experiment, remote run, web search, or finite fit.
