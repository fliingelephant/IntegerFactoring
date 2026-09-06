# F219 result

## Proof result

The strongest randomized result is the exact true-refinement waiting law.

- Primary prime-power order contributions can be certified and accumulated
  across unrelated annihilators without constructing one element of the
  combined order.
- Combining their modulus with a beta-two reciprocal prefix gives modulus
  `L_s=lcm(M,2^s)`.
- Uniformly guessing a finer prefix modulo `L_t` hits the true refinement
  with probability `L_s/L_t`. The exact mean time to that hit is `L_t/L_s`.
  Along this guaranteed route, expected cost remains
  `N^(1/4)/L_s`, up to logarithmic factors.
- A wrong refinement can still return a verified factor. Therefore the
  displayed cost is an upper bound obtained through the true class, not a
  lower bound on the actual Las Vegas runtime.
- Odd top multipliers in `(-1)^B binom(rN-1,B)` are affine bijections between
  carry guesses and reciprocal-prefix guesses. Randomizing `r` alone does
  not change this law.
- On the infinite bounded-gap family already used by P165, every accumulated
  ordinary primary modulus divides `gcd(p-1,q-1)=O(1)`. The P175
  quarter-minus-polylog carry prefix remains necessary for this combined
  terminal.

Thus Las Vegas is still a live direction. To improve the certified
true-prefix route, its randomness must obtain integer-correlated bias.
The present proof does not rule out exploitable verified factors from wrong
refinements. Uniform carry values and generic ordinary primary accumulation
do not improve the proved true-hit bound.

## F219-D01

The preregistered run completed in 2.3 seconds.

- Verdict: `spreading_lead`.
- Exact identity checks: 432,480.
- At `t=11`, image sizes ranged from 176 to 840 among 1,024 odd top
  multipliers.
- At `t=11`, maximum fibres ranged from 3 to 33.
- `N=77` had no zero carry in the canonical multiplier range at any tested
  precision `4 <= t <= 11`.

The output and log SHA-256 hashes are
`b87a8f378497c8d618e96797e02e484c4d75cd907fd18a9930d6044d89724ed9`
and
`92d10d0d43d8cde6a12d389e1eadcabc7624fc842287e31c5640e7a2f24b5fe5`.

## F219-D02

The frozen command failed before mathematical work:

```text
ModuleNotFoundError: No module named 'sympy'
```

No alternate command was run. D02 supplies no evidence.
