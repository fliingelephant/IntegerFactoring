# F227 self-audit

## Scope checks

- The theorem treats distinct odd balanced semiprimes only. It does not
  claim an arbitrary-composite factoring algorithm.
- The upper bound covers a fresh uniform unit after each candidate, and
  candidate laws whose largest atom is at most a QP multiple of uniform.
  It does not cover deterministic bases or a useful heavy candidate atom.
- The lower bound for a fixed base is conditional on a hidden local-order
  criterion. It is not asserted that the algorithm can recognize or produce
  such a base on every input.
- The result grants complete factorizations of all `x-1` values in the
  negative direction. There is no hidden claim that those factorizations
  are free in a positive algorithm.

## Edge and quantifier checks

1. `p` is in the declared interval because `q<2p`; `q` and `2p` are above
   it. Hence `p` is the unique direct nonunit candidate.
2. `L` is explicitly even. This forces every candidate to be odd and
   excludes `x-1=p`, the only possible hidden-factor multiple below `q`.
3. The local root count uses `F_r^*`, not the unit group modulo a repeated
   prime power. This matches the squarefree-semiprime scope.
4. The AP gcd lemma works even when its linear congruence is insoluble. The
   proof upper-bounds it by the soluble-case count.
5. A primary certificate is invoked only after global return. No certificate
   is claimed after `gcd(a^A-1,N)=1`.
6. The useful-event upper bound deliberately overcounts global returns and
   the true candidate. This is safe for an obstruction.
7. The factor-first stripping proof handles surplus prime powers in `A` by
   repeated division. A one-shot primary test would not by itself recover
   the exact common order.
8. The positive criterion uses the guaranteed `p`-side congruence. No
   compatibility of the `q`-side return progression is assumed.
9. The stale case is exactly equal local orders already dividing `L`.
   Unequal local orders split during stripping, and an equal order outside
   `L` strictly enlarges the modulus.
10. The preterminal asymptotic uses only `S(n)>=1`. Multiplying by any fixed
    numerical-QP diffuseness or trial cap remains `p^{o(1)}`.
11. Corollary D uses roughness of the full local order, not only a large
    prime-power divisor. This matches the P161 output and would not follow
    from P159's weaker large-primary-component statement alone.

## Attack attempts

### Could factoring `A` bias the already sampled uniform base?

No. The theorem conditions on `x` and all public preprocessing before the
fresh uniform unit is drawn. Its CRT reductions remain independent and
uniform. A rejection rule which changes the final candidate law is covered
only when the resulting largest atom remains QP-diffuse; a heavy law is
explicitly outside scope.

### Could a new block be certified without any local return?

Not by the declared F220-style channel. Its sound primary tests require
`a^A=1 mod N`. The theorem does not claim a lower bound against methods
which use the nonreturn values jointly in another way.

### Does the direct event invalidate the exponential estimate?

No. Its mass is at most `eta`, which is `p^{-1/2+o(1)}` under the diffuse
preterminal hypotheses because `H=Theta(p/L)` and `L=O(sqrt(p))`.

### Does QP recursive branching become super-QP?

No. The depth is logarithmic in `n`, and multiplying
`2^{poly(log n)}` costs along size halvings only increases the fixed
polylogarithmic exponent by one.

## Self-audit result

No internal contradiction was found. The candidate should receive a fresh
hostile audit and then a statement-only reconstruction before promotion.
