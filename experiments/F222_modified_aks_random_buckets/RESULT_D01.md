# F222-D01 result — positive finite coefficient signal, with an easy-gap caveat

## Result

The run completed 913 exact `(p,q,r)` rows.  Every tested fixed modulus had a
positive finite lower envelope.  There were no synchronized-support rows.

The smallest observed probabilities were:

- `r=3`: `153/17710` at `(p,q)=(461,463)`;
- `r=5`: `589/44676` at `(293,307)`;
- `r=7`: `474/55687` at `(467,479)`;
- `r=11`: `3917/122010` at `(491,499)`.

For `r=23,29,31`, every tested unit shift factored through a coefficient gcd.

## Scope correction

This is only a weak finite lead.  The consecutive-prime cohort had maximum
gap 14.  Of 913 rows, 585 satisfied `r>2*(q-p)`, where F222 already proves a
deterministic sparse-or-factor conclusion and Fermat is independently easy.

The remaining 328 rows still had positive probability.  Their smallest value
was the `r=3`, twin-prime row above.  On the largest twin-prime row, the exact
unreduced probability was

```text
1836 / 212520 = 153 / 17710 = 0.008639...
```

This is approximately `4/p`, not an inverse-polylogarithmic signal.  It is
compatible with an exponentially small fixed-modulus probability on a
bounded-gap infinite family.  The experiment does not establish that law.

The next useful numerical target is the genuine live regime
`q-p >= r/2` with broad nonconsecutive gaps, especially gaps of order
`sqrt(p)` and larger.  No theorem packet bytes were changed by this run.

