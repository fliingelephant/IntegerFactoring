# F219-D02 preregistration: full two-adic period at the first zero-carry failure

F219-D01 found that the canonical range `1 <= r < 2^t` has no zero carry
for `N=77=7*11` at every tested `4 <= t <= 11`. Integer-valued binomial
polynomials can have a larger period than `2^t`, so D02 tests the complete
standard period rather than treating that canonical slice as a global law.

For `B=8`, the standard period of `binom(77r-1,8) mod 2^t` divides
`2^(t+3)`. For each `4 <= t <= 16`, enumerate every odd
`1 <= r < 2^(t+3)`, compute

`h_r=(binom(77r-1,8)-1+11r)/77`,

and record the exact fibre distributions of `h_r mod 2^t` and
`g_r=h_r/r mod 2^t`. Also check period equality at every enumerated `r`
against `r+2^(t+3)`. SymPy may be used only to print and factor the exact
rational polynomial and its derivative; the authoritative distribution uses
integer `math.comb`.

The frozen outcomes are:

- `full_period_zero_kill` if both zero fibres are empty for every `t`;
- `full_period_spreading` if a zero fibre occurs but at `t=16` both maximum
  atom probabilities are at most `1/64` and both image sizes are at least
  64;
- `full_period_atom_lead` if either maximum atom probability at `t=16`
  exceeds `1/16`;
- `mixed` otherwise.

This is finite discovery evidence only. A later theorem must prove the
period and any unbounded fibre law.

Resource estimate: 1,048,000 binomial evaluations of degree 8, below 30
seconds and 100 MB. `python3` and `gtimeout` were prechecked. Frozen command:

```text
gtimeout 90s python3 experiments/F219_beta2_random_top_carry/full_period_77.py --output experiments/F219_beta2_random_top_carry/D02_OUTPUT.json > experiments/F219_beta2_random_top_carry/D02_RUN.log 2>&1
```

