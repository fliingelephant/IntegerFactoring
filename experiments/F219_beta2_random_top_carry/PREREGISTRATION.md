# F219-D01 preregistration: random top-multiplier carry fibres

## Closest prior route and material difference

The closest promoted results are P173 and P175. They identify the hidden
base-`N` quotient carry of

`A_1=(-1)^B binom(N-1,B)`

with a reciprocal prefix of the smaller factor. This experiment changes the
integer top parameter to

`A_r=(-1)^B binom(rN-1,B)`

and samples odd public multipliers `r`. P165 does not cover this test: no
random group base or local order is sampled. The tested observable is an
exact Euclidean quotient of an integer binomial coefficient.

## Frozen question

For balanced odd semiprimes `N=pq`, `p<q<2p`, put `B=floor(sqrt(N))` and

`h_r=(A_r-(1-rq))/N`.

For each declared precision `t`, enumerate the odd integers
`1 <= r < 2^t` and record the exact distribution modulo `2^t` of

`h_r` and `g_r = h_r/r`.

The main discovery question is whether either distribution has a large
universal atom, especially zero. If `g_r=c`, then the public residue

`z_r=N^(-1)(A_r-1) mod 2^t`

satisfies `p^(-1)=c-z_r/r mod 2^t`. Thus any publicly enumerable atom set
would give verified P175 candidates. Hidden factors are used only to label
the exact carry distribution and to verify the identity.

## Frozen cohort

- All odd primes `5 <= p <= 97`.
- For each `p`, all odd primes `p < q < 2p`.
- Precisions `4 <= t <= 11`.
- All odd canonical multipliers `1 <= r < 2^t`.

## Frozen outputs

For every `(N,p,q,t)`, output:

- fibre counts and image sizes for `h_r mod 2^t` and `g_r mod 2^t`;
- the zero-fibre counts;
- the maximum fibre counts and lexicographically first maximizing residues;
- a check of `h_r-z_r == r*p^(-1) mod 2^t` for every row.

The summary reports minima and maxima of the zero probabilities, maximum
atom probabilities, and image sizes at each `t`, plus the extremizing input.

## Interpretation thresholds

- `exact_universal_atom_lead`: one fixed residue has probability at least
  `1/16` for both `h_r` and `g_r` on every cohort input at `t=11`.
- `spreading_lead`: on every cohort input at `t=11`, both maximum atom
  probabilities are at most `1/16` and both images contain at least 16
  residues.
- `mixed`: neither condition holds.

These thresholds are discovery rules only. No finite outcome proves an
unbounded probability bound or a factoring algorithm.

## Resource estimate and command

The run performs fewer than 300,000 exact binomial evaluations with
`B < 140` and operands below 22,000,000. Expected runtime is below 60
seconds and peak memory below 100 MB. The local load before freezing was
1.38, 1.62, 1.69. `python3`, `gtimeout`, and `timeout` were prechecked and
available. The frozen command is:

```text
gtimeout 90s python3 experiments/F219_beta2_random_top_carry/search.py --output experiments/F219_beta2_random_top_carry/OUTPUT.json > experiments/F219_beta2_random_top_carry/RUN.log 2>&1
```

